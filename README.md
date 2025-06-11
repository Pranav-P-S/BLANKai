# Alzheimer's Dataset Image Classification using TensorFlow

This project uses TensorFlow to build and train a convolutional neural network (CNN) for classifying images from the Alzheimer's Dataset. The CNN is designed to classify images into four categories: Mild Demented, Moderate Demented, Non-Demented, and Very Mild Demented. It includes data preprocessing, model building, training, evaluation, and visualization of performance metrics.

## Project Overview

The goal of this project is to create a deep learning model that can accurately classify brain MRI images into different stages of Alzheimer's disease. The steps involved in the project include:

1. **Data Loading and Preprocessing**:
   - Loading images from directories using `tf.keras.preprocessing.image.ImageDataGenerator`.
   - Performing data augmentation such as brightness adjustment and zoom to enhance model robustness.
   - Splitting the dataset into training, validation, and testing sets.

2. **Model Architecture**:
   - Defining a CNN architecture using TensorFlow's Keras API.
   - Using separable convolution layers, batch normalization, max pooling, dropout, and dense layers.
   - Compiling the model with categorical cross-entropy loss and metrics such as accuracy, precision, recall, and AUC.

3. **Training and Evaluation**:
   - Training the model on the training data with early stopping and learning rate scheduling.
   - Evaluating the model performance on the validation set using accuracy, loss, AUC, and precision metrics.
   - Visualizing training history with plots for accuracy, loss, AUC, and precision over epochs.

4. **Model Deployment and Testing**:
   - Saving the trained model in H5 format for deployment.
   - Testing the model on the separate test set and generating classification reports.
   - Reporting metrics such as precision, recall, and F1-score for each class.

5. **GitHub Repository Structure**:
   - **`app.py`**: Main script containing the entire TensorFlow pipeline from data loading to model evaluation.
   - **`requirements.txt`**: List of Python dependencies required to run the project.
   - **`README.md`**: Markdown file providing an overview of the project, installation instructions, usage examples, and results.

## Requirements

- Python 3.6+
- TensorFlow 2.x
- NumPy
- Matplotlib
- scikit-learn
- Seaborn
- Pillow (PIL)

## Installation and Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Pranav-P-S/BLANKai.git
   cd your_repository
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:

   - Modify `app.py` with your dataset paths, image sizes, batch sizes, and model configurations.
   - Execute the script to train the model and evaluate its performance.

   ```bash
   python app.py
   ```

4. **Model Evaluation and Visualization**:

   - After running the script, view the generated plots for accuracy, loss, AUC, and precision metrics.
   - Examine the classification report to understand model performance on the test set.

## Example Usage

```bash
python app.py
```

## Results and Performance

- The model achieved an accuracy of X% on the test set with precision, recall, and F1-score reported for each class.
- Training history plots show improvement in metrics over epochs with proper handling of overfitting and learning rate adjustment.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration and initial code structure derived from practical deep learning applications.
- TensorFlow and Keras documentation and community for their valuable resources.
