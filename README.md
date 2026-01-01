# 🧠 BLANKai - Alzheimer's MRI Classifier

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

> A Deep Learning application to classify Alzheimer's Disease stages from MRI scans using Convolutional Neural Networks.

---

## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Directory Structure](#-directory-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📖 Project Overview

BLANKai is a professional-grade machine learning project designed to assist in the early detection of Alzheimer's disease. Using a custom Convolutional Neural Network (CNN) architecture, the model analyzes brain MRI scans and classifies them into four stages:

1. **Non Demented**
2. **Very Mild Demented**
3. **Mild Demented**
4. **Moderate Demented**

Visualizations and an interactive web interface are provided via Streamlit.

---

## ✨ Key Features

- **High Accuracy Model**: Custom CNN with separable convolutions and batch normalization.
- **Interactive UI**: User-friendly web interface for real-time image analysis.
- **Comprehensive Analysis**: visual confidence scores and probability distributions.
- **Reproducible Pipeline**: Clear notebook for training and data processing.

---

## 📂 Directory Structure

```plaintext
BLANKai/
├── .github/            # GitHub Actions and workflows
├── docs/               # Documentation and assets
│   └── MODEL_CARD.md   # Detailed model performance info
├── notebooks/          # Jupyter notebooks for training
│   └── training_pipeline.ipynb
├── src/                # Source code
│   ├── app.py          # Streamlit application entry point
│   ├── config.py       # Configuration and constants
│   └── model.py        # Model architecture definition
├── tests/              # Unit tests
├── requirements.txt    # Project dependencies
├── setup.py            # Package installation script
└── README.md           # Project documentation
```

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pranav-P-S/BLANKai.git
   cd BLANKai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Running the Web Application
To start the interactive interface:

```bash
streamlit run src/app.py
```

Upload a `.jpg` or `.png` MRI scan to see the classification results immediately.

### Training the Model
To retrain the model or explore the data pipeline, open the notebook:

```bash
jupyter notebook notebooks/training_pipeline.ipynb
```

---

## 🧠 Model Details

For specific details on the architecture, training process, and performance metrics, please refer to the [Model Card](docs/MODEL_CARD.md).

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by Pranav P S**
