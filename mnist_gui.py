import sys
import numpy as np
import os
from keras.models import load_model
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TF logs
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QPushButton, QLabel, QFrame)
from PySide6.QtGui import QPainter, QPen, QColor, QImage, QFont, QLinearGradient
from PySide6.QtCore import Qt, QPoint, QSize

STYLESHEET = """
QMainWindow {
    background-color: #0f172a;
}
QWidget {
    color: #f8fafc;
    font-family: 'Segoe UI', Inter, sans-serif;
}
QLabel {
    font-size: 14px;
}
QLabel#title {
    font-size: 24px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 10px;
}
QPushButton {
    background-color: #38bdf8;
    color: #0f172a;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #7dd3fc;
}
QPushButton:pressed {
    background-color: #0284c7;
}
QPushButton#clearBtn {
    background-color: #334155;
    color: #f8fafc;
}
QPushButton#clearBtn:hover {
    background-color: #475569;
}
QFrame#canvasFrame {
    background-color: #000000;
    border: 2px solid #334155;
    border-radius: 12px;
}
QFrame#statsFrame {
    background-color: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
}
"""

class DrawingCanvas(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("canvasFrame")
        self.setFixedSize(280, 280)
        self.image = QImage(self.size(), QImage.Format_Grayscale8)
        self.image.fill(Qt.black)
        self.drawing = False
        self.lastPoint = QPoint()
        
    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        # Draw with a slight inset if border is thick, but drawing over the frame is fine
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.white, 20, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            
    def clear(self):
        self.image.fill(Qt.black)
        self.update()
        
    def get_mnist_array(self):
        # Resize to 28x28 using smooth transformation for better quality
        scaled_img = self.image.scaled(28, 28, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        ptr = scaled_img.bits()
        arr = np.frombuffer(ptr, dtype=np.uint8).reshape((28, 28))
        # Normalize
        arr = arr.astype('float32') / 255.0
        return arr.reshape(1, 28, 28, 1)


class PredictionBar(QWidget):
    def __init__(self, digit):
        super().__init__()
        self.digit = digit
        self.probability = 0.0
        
        self.setFixedHeight(30)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 2, 5, 2)
        self.setLayout(layout)
        
        self.lbl_digit = QLabel(str(digit))
        self.lbl_digit.setFixedWidth(20)
        self.lbl_digit.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        self.bar_bg = QFrame()
        self.bar_bg.setStyleSheet("background-color: #334155; border-radius: 4px;")
        self.bar_bg.setFixedHeight(12)
        
        self.lbl_prob = QLabel("0.0%")
        self.lbl_prob.setFixedWidth(50)
        self.lbl_prob.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.lbl_prob.setStyleSheet("color: #94a3b8; font-size: 12px;")
        
        layout.addWidget(self.lbl_digit)
        layout.addWidget(self.bar_bg, 1)
        layout.addWidget(self.lbl_prob)
        
    def set_probability(self, prob):
        self.probability = prob
        self.lbl_prob.setText(f"{prob*100:.1f}%")
        if prob > 0.5:
            self.lbl_digit.setStyleSheet("font-weight: bold; font-size: 16px; color: #38bdf8;")
            self.lbl_prob.setStyleSheet("color: #38bdf8; font-size: 12px; font-weight: bold;")
        else:
            self.lbl_digit.setStyleSheet("font-weight: bold; font-size: 16px; color: #f8fafc;")
            self.lbl_prob.setStyleSheet("color: #94a3b8; font-size: 12px;")
        self.update()
        
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.probability > 0:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            
            # Find the geometry of the bar_bg
            rect = self.bar_bg.geometry()
            fill_width = int(rect.width() * self.probability)
            if fill_width > 0:
                bar_rect = rect.adjusted(0, 0, -rect.width() + fill_width, 0)
                
                # Gradient
                grad = QLinearGradient(bar_rect.topLeft(), bar_rect.topRight())
                if self.probability > 0.5:
                    grad.setColorAt(0, QColor("#0284c7"))
                    grad.setColorAt(1, QColor("#38bdf8"))
                else:
                    grad.setColorAt(0, QColor("#475569"))
                    grad.setColorAt(1, QColor("#64748b"))
                    
                painter.setBrush(grad)
                painter.setPen(Qt.NoPen)
                painter.drawRoundedRect(bar_rect, 4, 4)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Digit Classifier - Deep Learning Final")
        self.setFixedSize(650, 450)
        
        # Load Model
        self.model = None
        self.load_model()
        
        self.setup_ui()
        
    def load_model(self):
        try:
            from keras.models import load_model
            model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mnist_model.keras")
            if os.path.exists(model_path):
                self.model = load_model(model_path)
            else:
                print("Model not found. Run train_model.py first.")
        except Exception as e:
            print(f"Error loading model: {e}")
            
    def setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(30)
        
        # Left Panel - Canvas
        left_panel = QVBoxLayout()
        
        title = QLabel("Draw a Digit")
        title.setObjectName("title")
        left_panel.addWidget(title)
        
        self.canvas = DrawingCanvas()
        left_panel.addWidget(self.canvas)
        
        btn_layout = QHBoxLayout()
        self.btn_clear = QPushButton("Clear Canvas")
        self.btn_clear.setObjectName("clearBtn")
        self.btn_clear.clicked.connect(self.clear_canvas)
        
        self.btn_predict = QPushButton("Predict Digit")
        self.btn_predict.clicked.connect(self.predict)
        
        btn_layout.addWidget(self.btn_clear)
        btn_layout.addWidget(self.btn_predict)
        left_panel.addLayout(btn_layout)
        
        # Right Panel - Results
        right_panel = QVBoxLayout()
        
        res_title = QLabel("Prediction Confidence")
        res_title.setObjectName("title")
        right_panel.addWidget(res_title)
        
        self.stats_frame = QFrame()
        self.stats_frame.setObjectName("statsFrame")
        stats_layout = QVBoxLayout(self.stats_frame)
        stats_layout.setContentsMargins(15, 15, 15, 15)
        
        self.bars = []
        for i in range(10):
            bar = PredictionBar(i)
            self.bars.append(bar)
            stats_layout.addWidget(bar)
            
        right_panel.addWidget(self.stats_frame)
        right_panel.addStretch()
        
        main_layout.addLayout(left_panel)
        main_layout.addLayout(right_panel, 1)
        
    def clear_canvas(self):
        self.canvas.clear()
        for bar in self.bars:
            bar.set_probability(0.0)
            
    def predict(self):
        if self.model is None:
            print("Model not loaded!")
            return
            
        img_array = self.canvas.get_mnist_array()
        
        # Check if empty (all zeros)
        if np.max(img_array) == 0:
            print("Canvas is empty.")
            return
            
        predictions = self.model.predict(img_array, verbose=0)[0]
        
        for i, prob in enumerate(predictions):
            self.bars[i].set_probability(float(prob))

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()