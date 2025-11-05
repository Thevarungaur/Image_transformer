import streamlit as st

st.set_page_config(
    page_title="Mathematics Behind Transformations",
    page_icon="🧮",
    layout="wide"
)

# Title and Intro
st.markdown("""
<h2 style='text-align:center; color:#003366;'> Mathematics Behind Image Transformations</h2>
<p style='text-align:center; color:gray;'>

</p>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 1. Grayscale Conversion
# =========================
st.subheader(" 1. Grayscale Conversion")

st.write("""
Every color image consists of three intensity channels — **Red (R)**, **Green (G)**, and **Blue (B)**.  
However, the human eye does not perceive all three colors with the same sensitivity.  
We are most responsive to **green light**, moderately to **red**, and least to **blue**.  

To represent brightness accurately, grayscale conversion applies a **weighted sum** of the RGB components:
""")

st.latex(r"Y = 0.299R + 0.587G + 0.114B")

st.write("""
These weights come from the **luminance standard (ITU-R BT.601)**, designed to model how humans perceive brightness.  
The resulting grayscale image maintains the overall brightness and contrast of the original without retaining color.
""")

st.info("The value of Y represents the brightness of a pixel — a single number that captures how light or dark it appears to our eyes.")

st.markdown("---")

# =========================
# 2. Rotation
# =========================
st.subheader(" 2. Rotation")

st.write("""
Rotation changes the orientation of an image around a chosen point, typically the origin or center.  
For a pixel located at \((x, y)\), its new position after a rotation by angle \(θ\) is found using a rotation matrix:
""")

st.latex(r"""
\begin{bmatrix}
x' \\ 
y'
\end{bmatrix}
=
\begin{bmatrix}
\cos \theta & -\sin \theta \\ 
\sin \theta & \cos \theta
\end{bmatrix}
\begin{bmatrix}
x \\ 
y
\end{bmatrix}
""")

st.write("""
This formula comes directly from trigonometric relations in a coordinate system.  
Each point moves along a circular path around the origin while preserving its distance from it — meaning the shape and size of the image remain unchanged.
""")

st.info("Rotation is a rigid transformation — it changes orientation without altering dimensions or proportions.")

st.markdown("---")

# =========================
# 3. Scaling
# =========================
st.subheader(" 3. Scaling")

st.write("""
Scaling adjusts the size of an image by stretching or shrinking it along the horizontal and vertical directions.  
Mathematically, this is achieved by multiplying pixel coordinates with scaling factors \(S_x\) and \(S_y\):
""")

st.latex(r"""
\begin{bmatrix}
x' \\ 
y'
\end{bmatrix}
=
\begin{bmatrix}
S_x & 0 \\ 
0 & S_y
\end{bmatrix}
\begin{bmatrix}
x \\ 
y
\end{bmatrix}
""")

st.write("""
- When \(S_x\) and \(S_y\) are greater than 1, the image enlarges.  
- When they are less than 1, the image shrinks.  
- Unequal values for \(S_x\) and \(S_y\) cause stretching in one direction.

Scaling changes distances between points but keeps straight lines straight — making it a **linear transformation**.
""")

st.info("Scaling modifies the size of an image while keeping its geometry intact.")

st.markdown("---")

# =========================
# 4. Translation
# =========================
st.subheader("↔ 4. Translation")

st.write("""
Translation repositions an image by moving every pixel the same distance along the X and Y axes.  
In matrix form, translation can be represented using **homogeneous coordinates**:
""")

st.latex(r"""
\begin{bmatrix}
x' \\ 
y'
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & T_x \\ 
0 & 1 & T_y \\ 
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\ 
y \\ 
1
\end{bmatrix}
""")

st.write("""
Here, \(T_x\) and \(T_y\) are translation distances along the X and Y directions.  
The inclusion of an additional coordinate (the constant 1) allows translation to be expressed using the same matrix form as rotation and scaling, ensuring consistency across geometric operations.
""")

st.info("Translation is a simple shift — it moves the image without changing its size, angle, or proportions.")

st.markdown("---")

# =========================
# 5. Unified Linear Algebra Concept
# =========================
st.subheader("💡 Unified View: Transformations as Matrix Operations")

st.write("""
All geometric transformations can be expressed using a **single mathematical framework**:
""")

st.latex(r"P' = M \times P")

st.write("""
- \(P = [x, y, 1]^T\) represents the coordinates of a pixel in homogeneous form.  
- \(M\) is the transformation matrix (which could represent rotation, scaling, or translation).  
- \(P'\) gives the pixel’s new position after the transformation.  

This unified approach allows multiple transformations to be combined through **matrix multiplication**, a fundamental technique in computer graphics and vision.
""")

st.success("Every image manipulation — from rotation to zooming — is built upon linear algebra and matrix operations that map one coordinate system to another.")


