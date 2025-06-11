import streamlit as st
from PIL import Image
#import tensorflow as tf
import numpy as np

# Set the background color and theme colors
main_background_color = 'white'
theme_color = '#6C8DBF'  # Bluish shade
clicking_color = 'red'
other_color = '#50C878'  # Greenish-blue

# Set the page background color and font style
st.markdown(f"""
    <style>
        body {{
            background-color: {main_background_color};
            color: black;
            font-family: 'Times New Roman', Times, serif;
        }}
        .sidebar .sidebar-content {{
            background-color: {theme_color};
        }}
        .css-2trqyj {{
            color: {clicking_color};
        }}
        .css-1vmm3a3 {{
            color: {other_color};
        }}
    </style>
""", unsafe_allow_html=True)

# Streamlit App Title with Serpents Symbol
st.title("🐍🐍 Doc B - AI Image Analyzer 🐍🐍")

# Load the pre-trained model
#model = tf.keras.models.load_model('scratch_alzheimer_pre_process')

# Function to Analyze MRI Image


"""def analyze_image(image):

    prediction = model.predict(np.array([image]))

    # Get the predicted label
    predicted_label = np.argmax(prediction)

    # Display the uploaded image
    st.image(image, caption="Uploaded MRI Image", use_column_width=True)

    # Display the prediction label
    labels = ['MildDemented', 'ModerateDemented', 'NonDemented',
              'VeryMildDemented']  # Replace with actual labels
    st.write(f"Predicted Label: {labels[predicted_label]}")
"""

# Streamlit Sidebar
st.sidebar.title("🐍🐍 Doc B - Instructions 🐍🐍")
st.sidebar.write("Please upload an MRI image for analysis.")

# Upload MRI Image
uploaded_file = st.sidebar.file_uploader(
    "Choose an MRI image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display Uploaded Image
    image = Image.open(uploaded_file)
    st.sidebar.image(image, caption="Uploaded Image", use_column_width=True)

    # Analyze Button
    if st.sidebar.button("Analyze MRI Image"):
        # Call the function to analyze the image
        analyze_image(image)

# Drag and Drop Support
st.sidebar.markdown("### OR")
uploaded_file_drag_and_drop = st.file_uploader(
    "Drag and drop an MRI image here...", type=["jpg", "jpeg", "png"])

if uploaded_file_drag_and_drop is not None:
    # Display Uploaded Image
    image_drag_and_drop = Image.open(uploaded_file_drag_and_drop)
    st.sidebar.image(image_drag_and_drop,
                     caption="Uploaded Image", use_column_width=True)

    # Analyze Button for Drag and Drop
    if st.sidebar.button("Analyze MRI Image (Drag and Drop)"):
        # Call the function to analyze the image
        analyze_image(image_drag_and_drop)
