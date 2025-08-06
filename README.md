# Image Resampling with Linear Interpolation

This project performs image resampling using custom linear interpolation methods in Python. It converts an input image to grayscale, downsamples it to 70% of its original dimensions, and then resamples it back to the original size — all without using image processing libraries like OpenCV.

---

## 🚀 Features

- Convert image to grayscale (8bpp format)
- Resample image to 0.7x using **linear interpolation**
- Resample back to original dimensions
- Compute average of squared pixel differences between original and restored image
- Only uses `Pillow` and `NumPy` (for loading/saving and arrays)


