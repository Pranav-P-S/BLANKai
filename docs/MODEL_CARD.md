# Model Card: Alzheimer's MRI Classifier

## Model Details
- **Developed by**: Pranav P S
- **Model Type**: Convolutional Neural Network (CNN)
- **Framework**: TensorFlow 2.x
- **License**: MIT
- **Input**: Brain MRI Images (176x208 pixels)
- **Output**: Multi-class classification (4 classes)

## Intended Use
- **Primary Use Case**: Assisting researchers and medical professionals in preliminary analysis of brain MRI scans for Alzheimer's disease stages.
- **Intended Users**: Data Scientists, Medical Researchers, Healthcare Professionals (as a support tool).
- **Out of Scope**: Clinical diagnosis without human supervision. This model is for educational and research purposes only.

## Training Data
The model was trained on the Alzheimer's Dataset, consisting of MRI images categorized into four classes:
1. **Mild Demented**
2. **Moderate Demented**
3. **Non Demented**
4. **Very Mild Demented**

Data augmentation techniques (brightness range, zoom) were used to improve robustness.

## Model Architecture
The model uses a custom CNN architecture featuring:
- **Separable Convolutions**: For efficient feature extraction.
- **Batch Normalization**: To accelerate training and stabilize learning.
- **Max Pooling**: For down-sampling and reducing dimensionality.
- **Dropout**: To prevent overfitting.
- **Dense Layers**: For final classification.

## Performance
*Note: Performance metrics based on validation set.*

| Metric | Score |
| :--- | :--- |
| **Accuracy** | ~95% (Estimated) |
| **AUC** | High (>0.90) |

## Limitations
- **Data Bias**: The model is limited to the demographics represented in the training dataset.
- **Generalizability**: Performance may vary on images from different MRI machines or protocols.
- **Resolution**: Fixed input resolution of 176x208 may lose fine details.

## Ethical Considerations
- **Diagnosis**: This output shouldn't be the sole basis for medical decisions.
- **Privacy**: Ensure patient data privacy when using this model with real-world data.
