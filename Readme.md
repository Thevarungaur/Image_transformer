# 🖼️ Image Transformation and Grayscale Conversion App

## 📘 About the Project

This project is an **interactive web application** built using **Streamlit**, designed to demonstrate how different **image transformations** (like rotation, scaling, translation, and flipping) work, along with **grayscale conversion**.  

The application lets you upload any image, apply transformations in real-time, and view side-by-side comparisons — all within a clean, modern, and responsive interface.  

Additionally, the app includes a **“Mathematics Behind Transformations”** section that explains the core formulas and linear algebra concepts behind each operation.

---

## 🚀 Features

- 📤 **Upload and preview images** easily  
- 🎨 **Grayscale conversion** using perceptual luminance formula  
- 🔄 **Image transformations** — Rotate, Scale, Translate, Flip  
- 🧮 **Dedicated “Mathematics Behind” page** explaining the formulas  
- 💾 **Download processed images**  
- 📱 **Responsive UI** (mobile-friendly layout)  
- ⚡ **Fast processing** powered by OpenCV and NumPy  

---

## 🧠 Mathematics Behind Operations

### 🎨 Grayscale Conversion

A color image has three channels: Red (R), Green (G), and Blue (B). To convert it to grayscale, we calculate the intensity perceived by the human eye using this weighted formula:

\[
Gray = 0.299R + 0.587G + 0.114B
\]

#### Why these weights?
- Human vision is more sensitive to green light, followed by red and then blue.  
- This formula mimics human brightness perception.  
- It’s derived from the **ITU-R BT.601** standard for video encoding.

---

### 🔁 Image Transformations

#### 1️⃣ Rotation
Each pixel \((x, y)\) is rotated around the center using a **rotation matrix**:

\[
\begin{bmatrix}
x' \\ y'
\end{bmatrix}
=
\begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}
\begin{bmatrix}
x \\ y
\end{bmatrix}
\]

Here, \( \theta \) is the rotation angle (in radians).

---

#### 2️⃣ Scaling
Scaling changes the size of the image by multiplying pixel coordinates with scale factors \( S_x \) and \( S_y \):

\[
\begin{bmatrix}
x' \\ y'
\end{bmatrix}
=
\begin{bmatrix}
S_x & 0 \\
0 & S_y
\end{bmatrix}
\begin{bmatrix}
x \\ y
\end{bmatrix}
\]

Scaling helps enlarge or shrink images while maintaining proportions.

---

#### 3️⃣ Translation
Translation moves an image by shifting pixels along X and Y axes:

\[
\begin{bmatrix}
x' \\ y'
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & T_x \\
0 & 1 & T_y
\end{bmatrix}
\begin{bmatrix}
x \\ y \\ 1
\end{bmatrix}
\]

\(T_x\) and \(T_y\) represent movement in horizontal and vertical directions.

---

#### 4️⃣ Flipping
Flipping mirrors the image horizontally, vertically, or both.  
It can be represented by multiplying coordinates with -1 along the desired axis.

---

### 💡 Unified Concept

All geometric transformations can be represented as **matrix multiplications** in **homogeneous coordinates**:

\[
P' = M \times P
\]

where \(M\) is the transformation matrix and \(P = [x, y, 1]^T\).  
This is the foundation of **computer graphics, robotics, and image processing**.

---

## 🧩 Tech Stack

- 🐍 **Python 3.10+**
- 🌐 **Streamlit** – for UI and frontend  
- 🧮 **OpenCV** – for image manipulation  
- 🔢 **NumPy** – for matrix operations  
- 🖼️ **Pillow (PIL)** – for image loading and preprocessing  

---

## 📂 Folder Structure

📦 image-transformation-app
├── app.py # Main Streamlit app file
├── pages/
│ ├── 1_Image_Editor.py # Page for transformations
│ ├── 2_Mathematics_Behind.py # Page explaining the math
├── utils/
│ └── image_ops.py # Helper functions for processing
├── requirements.txt
└── README.md


---

## ⚙️ Setup and Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/image-transformation-app.git
cd image-transformation-app

--- 

### On Windows (Git Bash / CMD)
python -m venv venv
source venv/Scripts/activate



### Install dependecies 
pip install -r requirements.txt


### 4️⃣ Run the Streamlit app

streamlit run app.py

