# Color Detection using Python and OpenCV

## About the Project

This is a simple Color Detection project built using **Python, OpenCV, and Pandas**.

The project allows the user to click on any part of an image and detect the closest color name by comparing the clicked pixel's RGB values with the colors stored in `colors.csv`.

The detected **color name and RGB values** are displayed directly on the image.

## Technologies Used

* Python
* OpenCV
* Pandas
* CSV

## Project Files

* `color_detection.py` – Main Python program
* `colors.csv` – Color database containing color names, HEX codes, and RGB values
* `pic3.jpg` – Image used for color detection

## Installation

First, install Python on your computer.

Then install the required libraries:

```bash
pip install opencv-python pandas
```

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Make sure `color_detection.py`, `colors.csv`, and the image file are in the correct location.
4. Open the terminal in VS Code.
5. Run:

```bash
python color_detection.py
```

## How to Use

1. The image will open in a new window.
2. Click on any color in the image.
3. The program gets the RGB values of the clicked pixel.
4. It compares the RGB values with the colors in `colors.csv`.
5. The closest color name and RGB values are displayed on the image.
6. You can click on different areas to detect different colors.

## Example

When you click on a colored area, the program displays information like:

```text
Alabama Crimson
RGB: 163, 38, 56
```

## Project Purpose

This project helped me understand the basics of **Python, OpenCV, image pixels, RGB colors, mouse events, and working with CSV data using Pandas**.
