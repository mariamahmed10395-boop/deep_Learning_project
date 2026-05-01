# 🧠 Deep Learning Final Project

### Created by George Samuel

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-2.x-red)](https://keras.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-green)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📹 Project Demo Video

&lt;div align="center"&gt;

### 🎬 Project Overview & Results

<p align="center">
  ▶️ <a href="videos\gui.mp4">Watch the GUI demo</a>
</p>

## 📸 Project Screenshots

<p align="center">
  <img src="images\deep1.PNG" width="900">
</p>

<p align="center">
  <img src="images\deep2.PNG" width="900">
</p>
<p align="center">
  <img src="images\deep3.PNG" width="900">
</p>
<p align="center">
  <img src="images\deep4.PNG" width="900">
</p>

<p align="center">
  <img src="images\deep5.PNG" width="900">
</p>
<p align="center">
  <img src="images\deep6.PNG" width="900">
</p>
<p align="center">
  <img src="images\deep7.PNG" width="900">
</p>
<p align="center">
  <img src="images\deep8.PNG" width="900">
</p>

<p align="center">
  <img src="images\deep9.PNG" width="900">
</p>

<p align="center">
  <img src="images\deep10.PNG" width="900">
</p>

## 🔍 Grid Search Optimization

### Parameter Exploration

&lt;div align="center"&gt;

![Grid Search Process](./images/grid_search_progress.png)
_Figure 6: Grid Search progress bar showing parameter combinations being tested_

&lt;/div&gt;

### Grid Search Parameters Table

| batch_size | optimizer_1 | optimizer_2 | learning_rate_1 | learning_rate_2 |
| ---------- | ----------- | ----------- | --------------- | --------------- |
| 2          | adam        | rmsprop     | 0.001           | 0.01            |
| 4          | adam        | rmsprop     | 0.001           | 0.01            |
| 8          | adam        | rmsprop     | 0.001           | 0.01            |
| 16         | adam        | rmsprop     | 0.001           | 0.01            |
| 32         | adam        | rmsprop     | 0.001           | 0.01            |
| 64         | adam        | rmsprop     | 0.001           | 0.01            |

### 🏆 Best Parameters Found

| Parameter         | Value   | Accuracy   |
| ----------------- | ------- | ---------- |
| **Batch Size**    | 20      |            |
| **Optimizer**     | RMSprop |            |
| **Learning Rate** | 0.001   | **97.86%** |

### Model Features:

- ✅ Multiple hidden layers with increased capacity
- ✅ Changed activation functions (ReLU, Sigmoid, etc.)
- ✅ Advanced optimization techniques

---

### Results Summary

| Optimizer | Accuracy    |
| --------- | ----------- |
| SGD       | ~95.50%     |
| Momentum  | ~97.20%     |
| RMSprop   | ~97.50%     |
| AdaDelta  | ~96.80%     |
| Adagrad   | ~96.50%     |
| **Adam**  | **~97.80%** |

---

### Mathematical Proof

**Before (Sigmoid):**
Gradient Flow = [0.25] × [0.25] × [0.25] × [0.25] × Loss_Gradient
Resulting Term = 0.0039 × Loss_Gradient ⚠️ Vanished!

**After (ReLU):**
Gradient Flow = [1.0] × [1.0] × [1.0] × [1.0] × Loss_Gradient
Resulting Term = 1.0 × Loss_Gradient ✅ Preserved!

---

### Gradient Norms Comparison

**Before Clipping:**

Gradient Norms: [1542.85, 4098.12, 9854.33]
Norm (Size): 10815.4 ❌ Unstable!

**After Clipping (threshold=1.0):**
Gradient Norms: [0.142, 0.378, 0.911]
Norm (Size): 1.0 ✅ Stable!

---

## 🛡️ Dropout Regularization (Q5)

### Performance Impact

| Dropout                  | Accuracy    |
| ------------------------ | ----------- |
| Before (No Dropout)      | ~97.64%     |
| After (With Dropout 0.3) | **~98.10%** |

---

## ⚡ Activation Functions Comparison (Q6)

| Activation Function | Accuracy    |
| ------------------- | ----------- |
| **ReLU**            | **~98.10%** |
| Sigmoid             | ~93.50%     |
| Tanh                | ~97.60%     |
| Leaky ReLU          | ~98.00%     |
| ELU                 | ~97.90%     |

---

### Architecture Results

| Strategy               | Description                | Accuracy   |
| ---------------------- | -------------------------- | ---------- |
| Wide Model (1024→512)  | Few layers, many nodes     | ~97.5%     |
| Deep Model (5 layers)  | Many layers, fewer nodes   | ~97.8%     |
| **Balanced + Dropout** | **Moderate depth + width** | **~98.2%** |

---

## 📐 Data Normalization Importance (Q8)

**Key Benefits:**

- ⚡ Faster convergence (normalized vs unnormalized)
- 🎯 Equal feature contribution
- 🛡️ Numerical stability
- 🎨 Better activation function performance

---

## 🔄 Batch Normalization (Q9)

| Batch Normalization | Accuracy    |
| ------------------- | ----------- |
| Before              | ~97.90%     |
| After               | **~98.50%** |

---

## 🎲 Weight Initialization Comparison (Q10)

| Initialization | Accuracy    | Convergence           |
| -------------- | ----------- | --------------------- |
| Random Normal  | ~96.50%     | Slow, unstable        |
| Xavier/Glorot  | ~97.60%     | Good for Sigmoid/Tanh |
| **He Normal**  | **~98.50%** | **Fast and stable**   |

---

### Comparison

| Feature                | Vanilla | Stacked      |
| ---------------------- | ------- | ------------ |
| Layers                 | Single  | Multiple     |
| Capacity               | Limited | Higher       |
| Reconstruction Quality | Good    | Better       |
| Feature Learning       | Basic   | Hierarchical |

---

### Architecture Details:

Encoder: 784 → 256 → 128 → 64 → 32 → 16 → 2 (Bottleneck)
Decoder: 2 → 16 → 32 → 64 → 128 → 256 → 784

### 2-Node Bottleneck Visualization

**Benefits of 2-Node Bottleneck:**

- 📉 Maximum compression
- 📊 Easy visualization in 2D space
- 🎯 Forces learning of most essential features

---

## 📈 Final Accuracy Comparison (Q14)

| Model Architecture        | Test Accuracy |
| ------------------------- | ------------- |
| Basic Sequential          | 97.60%        |
| Grid Search Optimized     | 97.86%        |
| Functional API (Enhanced) | 98.10%        |
| With Dropout              | 98.10%        |
| With Batch Normalization  | 98.50%        |
| He Initialization + ReLU  | 98.50%        |
| **Best Balanced Model**   | **~98.50%**   |

---

## 🎛️ Callbacks & TensorBoard (Q15)

### Implemented Callbacks:

- ✅ `EarlyStopping` - Stop training when validation loss plateaus
- ✅ `ModelCheckpoint` - Save best model weights
- ✅ `TensorBoard` - Real-time visualization
- ✅ `ReduceLROnPlateau` - Adaptive learning rate adjustment

---

### Techniques Applied:

| Technique         | Effectiveness |
| ----------------- | ------------- |
| L2 Regularization | ⭐⭐⭐⭐      |
| Dropout (0.3-0.5) | ⭐⭐⭐⭐⭐    |
| Data Augmentation | ⭐⭐⭐        |
| Early Stopping    | ⭐⭐⭐⭐⭐    |

---

## 🚀 How to Run

### Prerequisites

```bash
# Install required packages
pip install scikeras tensorflow scikit-learn matplotlib pandas seaborn

deep-learning-final-project/
├── 📓 Deep-Learning_Final_Project.ipynb    # Main project notebook
├── 📁 models/                              # Saved model weights
│   ├── mnist_autoencoder.h5
│   └── mnist_model.keras
├── 📁 src/                                 # Source code
│   ├── mnist_gui.py
│   └── train_model.py
├── 📄 README.md                            # This file
└── 📄 requirements.txt                     # Python dependencies
```
