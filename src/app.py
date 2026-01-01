import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
from . import config

# Page Configuration
st.set_page_config(
    page_title="Doc B - AI Image Analyzer",
    page_icon="🐍",
    layout="wide"
)

# Custom CSS
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {config.BACKGROUND_COLOR};
        }}
        .sidebar .sidebar-content {{
            background-color: {config.THEME_COLOR};
        }}
        h1 {{
            color: {config.THEME_COLOR};
            font-family: 'Helvetica Neue', sans-serif;
        }}
        .stButton>button {{
            color: white;
            background-color: {config.THEME_COLOR};
            border-radius: 10px;
        }}
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the trained model."""
    try:
        # Check if model exists in config path, otherwise look for default name
        if os.path.exists(config.MODEL_PATH):
            return tf.keras.models.load_model(config.MODEL_PATH)
        elif os.path.exists('scratch_alzheimer_pre_process'):
             return tf.keras.models.load_model('scratch_alzheimer_pre_process')
        else:
            return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def analyze_image(model, image):
    """Analyze the uploaded image and display results."""
    if model is None:
        st.error("Model not found. Please train the model first.")
        return

    # Preprocess image
    img = image.resize(config.IMAGE_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) / 255.0  # Rescale to 0-1

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_label = config.CLASSES[predicted_class_index]
    confidence = prediction[0][predicted_class_index]

    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="Uploaded MRI Scan", use_column_width=True)
    
    with col2:
        st.subheader("Analysis Results")
        st.write(f"**Predicted Diagnosis:** {predicted_label}")
        st.write(f"**Confidence:** {confidence:.2%}")
        
        # Display probability distribution
        st.bar_chart({label: float(pred) for label, pred in zip(config.CLASSES, prediction[0])})

def main():
    st.title("🐍🐍 Doc B - AI Image Analyzer 🐍🐍")
    st.write("Upload a brain MRI scan to detect signs of Alzheimer's disease.")

    model = load_model()
    if model is None:
        st.warning("⚠️ Model file not found. Please place 'alzheimer_model.h5' in the saved_models directory.")

    # Sidebar
    st.sidebar.title("Instructions")
    st.sidebar.info(
        "1. Upload a brain MRI image (JPG, PNG).\n"
        "2. The AI will analyze the image.\n"
        "3. View the diagnosis and confidence score."
    )

    uploaded_file = st.sidebar.file_uploader("Choose an MRI image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        if st.sidebar.button("Analyze Image"):
            with st.spinner('Analyzing...'):
                analyze_image(model, image)

if __name__ == "__main__":
    main()
