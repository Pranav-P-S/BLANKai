import tensorflow as tf
from . import config

def conv_block(filters, kernel_size=3, activation='relu', padding='same'):
    """
    Creates a separable convolution block with BatchNormalization and MaxPooling.
    
    Args:
        filters (int): Number of filters for the convolution layers.
        kernel_size (int): Size of the convolution kernel.
        activation (str): Activation function.
        padding (str): Padding strategy.
        
    Returns:
        tf.keras.Sequential: A sequential model representing the block.
    """
    block = tf.keras.Sequential([
        tf.keras.layers.SeparableConv2D(filters, kernel_size, activation=activation, padding=padding),
        tf.keras.layers.SeparableConv2D(filters, kernel_size, activation=activation, padding=padding),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D()
    ])
    
    return block

def dense_block(units, dropout_rate, activation='relu'):
    """
    Creates a dense block with BatchNormalization and Dropout.
    
    Args:
        units (int): Number of neurons in the dense layer.
        dropout_rate (float): Dropout rate.
        activation (str): Activation function.
        
    Returns:
        tf.keras.Sequential: A sequential model representing the block.
    """
    block = tf.keras.Sequential([
        tf.keras.layers.Dense(units, activation=activation),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(dropout_rate)
    ])
    
    return block

def build_model():
    """
    Builds the complete CNN model for Alzheimer's MRI classification.
    
    Returns:
        tf.keras.Model: The compiled Keras model.
    """
    input_shape = (*config.IMAGE_SIZE, 3)
    
    model = tf.keras.Sequential([
        tf.keras.Input(shape=input_shape),
        
        # Initial Conv Layer
        tf.keras.layers.Conv2D(16, 3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(16, 3, activation='relu', padding='same'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPool2D(),
        
        # Convolution Blocks
        conv_block(32),
        tf.keras.layers.BatchNormalization(),
        conv_block(64),
        tf.keras.layers.BatchNormalization(),
        
        conv_block(128),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.2),
        
        conv_block(256),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.2),
        
        # Dense Layers
        tf.keras.layers.Flatten(),
        dense_block(256, 0.7),
        dense_block(128, 0.5),
        dense_block(64, 0.3),
        
        # Output Layer
        tf.keras.layers.Dense(config.NUM_CLASSES, activation='softmax')
    ])
    
    return model
