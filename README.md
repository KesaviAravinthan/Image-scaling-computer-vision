# Image Resampling using Linear Interpolation (No OpenCV)

This project implements a simple image resampling pipeline **without using any image processing libraries** like OpenCV or skimage. It includes:

- Converting an RGB image to grayscale
- Resizing the grayscale image to 70% of its original size using **bilinear interpolation**
- Resizing it back to the original size
- Calculating the **Sum of Squared Differences (SSD)** between the original and reconstructed images

---

## 🖼️ Sample Flow

```text
original image (RGB) 
       ↓
grayscale image (8-bit)
       ↓
resampled image (0.7x)
       ↓
resampled-back image (original size)
       ↓
SSD (pixel-wise difference analysis)

```
--- 
## File Strcture
```text
image-salling/
│
├── image.jpg                  # Input image (you must provide this)
├── gray_image.jpg             # Grayscale version of input
├── resized_image.jpg          # Downsampled to 70%
├── resized_back_image.jpg     # Upsampled back to original
├── main.py                    # Your script
└── README.md                  # Project documentation

```
---
## Output Details

- Grayscale Image (gray_image.jpg): Converted from original using luminance formula:
Y = 0.299*R + 0.587*G + 0.114*B

- Resized Image (resized_image.jpg): Resampled to 70% using bilinear interpolation

- Resized-Back Image (resized_back_image.jpg): Resampled back to original size

- SSD Calculation: Computes the sum and average of squared differences between original and final image.
---
## Example output printed:

```text

Converted to grayscale: Done
Original size: 800 x 600  -->  Resized: 560 x 420
Image resized: Done
Image resized: Done
The Sum of Squared Differences: 19582034.0
The average of squared differences: 53.49

```
