# Lemon Quality Classification 🍋

This project is a Python-based utility to organize and process image data for identifying **fresh** vs. **affected** lemons. It is structured to be compatible with popular Deep Learning frameworks like TensorFlow, Keras, or PyTorch.

## 📂 Project Structure

The dataset is organized into training and validation sets, further categorized by the health of the fruit:

```text
.
├── data/
│   ├── train/
│   │   ├── fresh/       # Images of healthy lemons
│   │   └── affected/    # Images of damaged/moldy lemons
│   └── validation/
│       ├── fresh/       # Validation images for healthy lemons
│       └── affected/    # Validation images for damaged lemons
├── script.py            # Main script for data processing
└── README.md            # Project documentation
