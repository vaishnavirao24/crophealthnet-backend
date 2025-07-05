# 🌿 CropHealthNet - Plant Disease Detection API

A deep learning API for detecting plant leaf diseases using a ResNet18 model trained on the *PlantDoc* dataset. Includes explainability via Grad-CAM and deployable backend with FastAPI.

---

## 📁 Dataset: PlantDoc

- 📦 *Source*: [PlantDoc Kaggle Dataset](https://www.kaggle.com/datasets/pratikkayal/plantdoc-dataset)
- 🌿 *Classes*: 38 real-world crop diseases (e.g., Tomato Leaf Curl, Apple Scab)
- 🧾 *Format*: Folder structure (/train/ClassName/*.jpg, /test/ClassName/*.jpg)
- 🧹 *Preprocessing*:
  - Resized/cropped to 224×224
  - Augmented with rotation, color jitter, flips
  - Normalized using ImageNet mean & std


---

## 🧠 Model Details

| Component | Description |
|----------|-------------|
| 🔍 Architecture | ResNet18 (pretrained on ImageNet) |
| 🧪 Modification | Final layer changed to nn.Linear(..., 38) |
| 🏋‍♂ Training | 80/20 split + validation, trained for 20 epochs |
| 🧠 Optimizer | Adam with weight decay |
| 🎯 Accuracy | Train ~77%, Validation ~50%, Test ~45% |
| 📤 Export | TorchScript .pt model (for production) |

---

## 🛠 Features

- ✅ *Image Upload* (via FastAPI)
- ✅ *Disease Prediction* (ResNet18 model)
- ✅ *Trust Score* (Softmax confidence)
- ✅ *Explainability* (Grad-CAM heatmaps)
- ✅ *TorchScript* Model Export
- ✅ *FastAPI*-based Inference API

---
