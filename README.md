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
  ▶️ <a href="deeplearning\deep_Learning_project\videos\Recording #12.mp4">Watch the GUI demo</a>
</p>

## 📸 Project Screenshots

<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep1.PNG" width="900">
</p>

<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep2.PNG" width="900">
</p>
<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep3.PNG" width="900">
</p>
<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep4.PNG" width="900">
</p>

<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep5.PNG" width="900">
</p>
<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep6.PNG" width="900">
</p>
<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep7.PNG" width="900">
</p>
<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep8.PNG" width="900">
</p>

<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep9.PNG" width="900">
</p>

<p align="center">
  <img src="C:\Users\Test\Desktop\deeplearning\deep_Learning_project\images\deep10.PNG" width="900">
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

&lt;div align="center"&gt;

![Best Model Results](./images/best_model_results.png)
_Figure 7: Final optimized model performance metrics_

&lt;/div&gt;

---

## 🏗️ Enhanced Model Architecture (Functional API)

&lt;div align="center"&gt;

![Functional API Model](./images/functional_api_model.png)
_Figure 8: Functional API model with multiple hidden layers_

&lt;/div&gt;

### Model Features:

- ✅ Multiple hidden layers with increased capacity
- ✅ Changed activation functions (ReLU, Sigmoid, etc.)
- ✅ Advanced optimization techniques

&lt;div align="center"&gt;

![Enhanced Training Curves](./images/enhanced_training.png)
_Figure 9: Training and validation loss/accuracy for enhanced model_

&lt;/div&gt;

---

## 📊 Confusion Matrix Analysis

&lt;div align="center"&gt;

![Confusion Matrix](./images/confusion_matrix.png)
_Figure 10: Confusion matrix showing prediction accuracy across all digit classes (0-9)_

&lt;/div&gt;

---

## 🔬 Optimizer Comparison (Q2)

&lt;div align="center"&gt;

![Optimizer Comparison Chart](./images/optimizer_comparison.png)
_Figure 11: Bar chart comparing validation accuracy across different optimizers_

&lt;/div&gt;

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

## 🎯 Vanishing Gradient Problem & Solutions (Q3)

&lt;div align="center"&gt;

![Vanishing Gradient Problem](./images/vanishing_gradient.png)
_Figure 12: Demonstration of vanishing gradient problem with sigmoid activation_

![ReLU Solution](./images/relu_solution.png)
_Figure 13: Comparison of gradient flow: Sigmoid vs ReLU_

&lt;/div&gt;

### Mathematical Proof

**Before (Sigmoid):**
Gradient Flow = [0.25] × [0.25] × [0.25] × [0.25] × Loss_Gradient
Resulting Term = 0.0039 × Loss_Gradient ⚠️ Vanished!

**After (ReLU):**
Gradient Flow = [1.0] × [1.0] × [1.0] × [1.0] × Loss_Gradient
Resulting Term = 1.0 × Loss_Gradient ✅ Preserved!

<div align="center">

![Fixed Model Training](./images/fixed_model_training.png)
_Figure 14: Training curves after applying ReLU and proper initialization_

</div>

---

## 💥 Exploding Gradient Problem & Solutions (Q4)

<div align="center">

![Exploding Gradient](./images/exploding_gradient.png)
_Figure 15: Demonstration of exploding gradients in deep networks_

![Gradient Clipping](./images/gradient_clipping.png)
_Figure 16: Effect of gradient clipping on training stability_

</div>

### Gradient Norms Comparison

**Before Clipping:**

Gradient Norms: [1542.85, 4098.12, 9854.33]
Norm (Size): 10815.4 ❌ Unstable!

**After Clipping (threshold=1.0):**
Gradient Norms: [0.142, 0.378, 0.911]
Norm (Size): 1.0 ✅ Stable!

---

## 🛡️ Dropout Regularization (Q5)

<div align="center">

![Dropout Effect](./images/dropout_effect.png)
_Figure 17: Comparison of training with and without Dropout layers_

</div>

### Performance Impact

| Dropout                  | Accuracy    |
| ------------------------ | ----------- |
| Before (No Dropout)      | ~97.64%     |
| After (With Dropout 0.3) | **~98.10%** |

<div align="center">

![Dropout Training Curves](./images/dropout_curves.png)
_Figure 18: Training vs Validation loss curves showing reduced overfitting with Dropout_

</div>

---

## ⚡ Activation Functions Comparison (Q6)

<div align="center">

![Activation Functions](./images/activation_comparison.png)
_Figure 19: Performance comparison of different activation functions_

</div>

| Activation Function | Accuracy    |
| ------------------- | ----------- |
| **ReLU**            | **~98.10%** |
| Sigmoid             | ~93.50%     |
| Tanh                | ~97.60%     |
| Leaky ReLU          | ~98.00%     |
| ELU                 | ~97.90%     |

---

## 🏗️ Model Depth vs Width Analysis (Q7)

<div align="center">

![Wide vs Deep vs Balanced](./images/architecture_comparison.png)
_Figure 20: Comparison of Wide, Deep, and Balanced model architectures_

</div>

### Architecture Results

| Strategy               | Description                | Accuracy   |
| ---------------------- | -------------------------- | ---------- |
| Wide Model (1024→512)  | Few layers, many nodes     | ~97.5%     |
| Deep Model (5 layers)  | Many layers, fewer nodes   | ~97.8%     |
| **Balanced + Dropout** | **Moderate depth + width** | **~98.2%** |

<div align="center">

![Architecture Training](./images/architecture_training.png)
_Figure 21: Training curves for different architecture strategies_

</div>

---

## 📐 Data Normalization Importance (Q8)

<div align="center">

![Normalization Effect](./images/normalization_effect.png)
_Figure 22: Impact of data normalization on training convergence speed_

</div>

**Key Benefits:**

- ⚡ Faster convergence (normalized vs unnormalized)
- 🎯 Equal feature contribution
- 🛡️ Numerical stability
- 🎨 Better activation function performance

---

## 🔄 Batch Normalization (Q9)

<div align="center">

![Batch Normalization](./images/batch_norm.png)
_Figure 23: Model architecture with Batch Normalization layers_

![Batch Norm Results](./images/batch_norm_results.png)
_Figure 24: Training stability improvement with Batch Normalization_

</div>

| Batch Normalization | Accuracy    |
| ------------------- | ----------- |
| Before              | ~97.90%     |
| After               | **~98.50%** |

---

## 🎲 Weight Initialization Comparison (Q10)

<div align="center">

![Initialization Comparison](./images/initialization_comparison.png)
_Figure 25: Training curves comparing different weight initialization strategies_

</div>

| Initialization | Accuracy    | Convergence           |
| -------------- | ----------- | --------------------- |
| Random Normal  | ~96.50%     | Slow, unstable        |
| Xavier/Glorot  | ~97.60%     | Good for Sigmoid/Tanh |
| **He Normal**  | **~98.50%** | **Fast and stable**   |

---

## 🏭 Autoencoders (Q11)

### Vanilla Autoencoder

<div align="center">

![Vanilla Autoencoder](./images/vanilla_autoencoder.png)
_Figure 26: Vanilla autoencoder architecture with single hidden layer (32 neurons)_

![Vanilla Reconstruction](./images/vanilla_reconstruction.png)
_Figure 27: Original vs Reconstructed images (Vanilla)_

</div>

### Stacked Autoencoder

<div align="center">

![Stacked Autoencoder](./images/stacked_autoencoder.png)
_Figure 28: Stacked autoencoder with multiple encoder/decoder layers_

![Stacked Reconstruction](./images/stacked_reconstruction.png)
_Figure 29: Original vs Reconstructed images (Stacked)_

</div>

### Comparison

| Feature                | Vanilla | Stacked      |
| ---------------------- | ------- | ------------ |
| Layers                 | Single  | Multiple     |
| Capacity               | Limited | Higher       |
| Reconstruction Quality | Good    | Better       |
| Feature Learning       | Basic   | Hierarchical |

---

## 🔇 Denoising Autoencoder (Q12)

### 6-Layer Encoder & Decoder Design

<div align="center">

![Denoising Autoencoder Architecture](./images/denoising_autoencoder_6layer.png)
_Figure 30: 6-layer denoising autoencoder architecture_

</div>

### Architecture Details:

Encoder: 784 → 256 → 128 → 64 → 32 → 16 → 2 (Bottleneck)
Decoder: 2 → 16 → 32 → 64 → 128 → 256 → 784

<div align="center">

![Noisy Input](./images/noisy_input.png)
_Figure 31: Original vs Noisy input images_

![Denoised Output](./images/denoised_output.png)
_Figure 32: Noisy input vs Denoised output comparison_

</div>

### 2-Node Bottleneck Visualization

<div align="center">

![Bottleneck Visualization](./images/bottleneck_2d.png)
_Figure 33: 2D visualization of the bottleneck layer (2 nodes) showing digit clustering_

</div>

**Benefits of 2-Node Bottleneck:**

- 📉 Maximum compression
- 📊 Easy visualization in 2D space
- 🎯 Forces learning of most essential features

---

## 🔥 PyTorch Conversion (Q13)

<div align="center">

![PyTorch Model](./images/pytorch_model.png)
_Figure 34: Equivalent PyTorch model architecture_

</div>

### PyTorch Training Results

<div align="center">

![PyTorch Training](./images/pytorch_training.png)
_Figure 35: PyTorch model training curves_

</div>

---

## 📈 Final Accuracy Comparison (Q14)

<div align="center">

![Final Comparison](./images/final_accuracy_comparison.png)
_Figure 36: Final accuracy comparison across all model architectures_

</div>

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

<div align="center">

![TensorBoard Dashboard](./images/tensorboard_dashboard.png)
_Figure 37: TensorBoard dashboard showing real-time training metrics_

![Early Stopping](./images/early_stopping.png)
_Figure 38: Early stopping callback preventing overfitting_

</div>

### Implemented Callbacks:

- ✅ `EarlyStopping` - Stop training when validation loss plateaus
- ✅ `ModelCheckpoint` - Save best model weights
- ✅ `TensorBoard` - Real-time visualization
- ✅ `ReduceLROnPlateau` - Adaptive learning rate adjustment

---

## 🎓 Student Performance Dataset (Bonus Challenge)

<div align="center">

![Dataset Overview](./images/student_dataset.png)
_Figure 39: Student performance dataset overview and features_

![Overfitting Solutions](./images/overfitting_solutions.png)
_Figure 40: Comparison of overfitting mitigation techniques_

</div>

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
