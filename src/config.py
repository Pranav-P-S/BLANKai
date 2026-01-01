import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset paths
DATA_DIR = os.path.join(BASE_DIR, "Alzheimer_s Dataset")
TRAIN_DIR = os.path.join(DATA_DIR, "train")
TEST_DIR = os.path.join(DATA_DIR, "test")

# Model parameters
IMAGE_SIZE = (176, 208)
BATCH_SIZE = 20
EPOCHS = 50
LEARNING_RATE = 0.01
DECAY_STEPS = 20
DECAY_RATE = 0.1

# Classes
CLASSES = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
NUM_CLASSES = len(CLASSES)

# Visualization settings
THEME_COLOR = '#6C8DBF'
BACKGROUND_COLOR = 'white'
