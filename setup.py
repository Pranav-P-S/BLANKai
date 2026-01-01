from setuptools import setup, find_packages

setup(
    name="blankai",
    version="0.1.0",
    description="Alzheimer's Dataset Image Classification using TensorFlow",
    author="Pranav P S",
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.10.0",
        "numpy>=1.23.0",
        "matplotlib>=3.6.0",
        "scikit-learn>=1.2.0",
        "seaborn>=0.12.0",
        "Pillow>=9.0.0",
        "streamlit>=1.20.0",
    ],
    python_requires=">=3.8",
)
