import streamlit as st
from PIL import Image
from image_utils import (
    read_and_preprocess_image,
    rotate_image,
    scale_image,
    translate_image
)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Image Transformation App",
    page_icon="📸",
    layout="wide"
)

# -------------------------------
# Custom Styling
# -------------------------------
st.markdown("""
<style>
body, .main {
    background-color: #f7f9fb;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

.block-container {
    max-width: 1100px;
    margin: auto;
    padding-top: 1rem;
    padding-bottom: 2rem;
}

h1 {
    color: #003366;
    text-align: center;
    font-weight: 700;
    margin-bottom: 0.4em;
    font-size: clamp(1.6rem, 4vw, 2.4rem);
}

h2, h3 {
    color: #004080;
    font-size: clamp(1.1rem, 2.5vw, 1.5rem);
}

p {
    font-size: clamp(0.9rem, 2vw, 1rem);
}

.stFileUploader {
    border: 1px solid #ccc;
    border-radius: 12px;
    padding: 0.6em;
    background: white;
}

.caption {
    text-align: center;
    color: #555;
    font-size: 0.9em;
}

hr {
    border: 0.5px solid #dce3ec;
    margin: 1.5em 0;
}

/* Image layout */
.responsive-img {
    width: 100%;
    max-width: 360px;
    height: auto;
    border-radius: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

@media (max-width: 768px) {
    .responsive-img {
        max-width: 95%;
    }
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("Image Transformation App")

st.markdown("""
Upload an image (from your **camera or gallery**) to view it in **original vs grayscale** format  
and apply transformations — **Rotation**, **Scaling**, or **Translation** — interactively.
""")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    original_image = Image.open(uploaded_file)
    gray_image = read_and_preprocess_image(uploaded_file)

    st.subheader("Original vs Grayscale Comparison")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.image(original_image, caption="Original Image", width=360)
    with col2:
        st.image(gray_image, caption="Grayscale Image", width=360)

    with st.expander("View Partial 2D Matrix Representation"):
        st.text(gray_image[:10, :10])

    st.markdown("---")
    st.subheader("Apply a Transformation")

    transform_choice = st.selectbox("Select transformation type:", ["Rotation", "Scaling", "Translation"])

    transformed_img = None
    caption = ""

    if transform_choice == "Rotation":
        angle = st.slider("Select rotation angle (°)", -180, 180, 45)
        transformed_img = rotate_image(gray_image, angle)
        caption = f"Rotated by {angle}°"

    elif transform_choice == "Scaling":
        scale_factor = st.slider("Select scaling factor", 0.1, 3.0, 1.0, step=0.1)
        transformed_img = scale_image(gray_image, scale_factor)
        caption = f"Scaled by {scale_factor}×"

    elif transform_choice == "Translation":
        tx = st.slider("Translate along X-axis (pixels)", -200, 200, 50)
        ty = st.slider("Translate along Y-axis (pixels)", -200, 200, 50)
        transformed_img = translate_image(gray_image, tx, ty)
        caption = f"Translated by ({tx}, {ty}) pixels"

    if transformed_img is not None:
        st.markdown("---")
        st.subheader("Transformation Result")

        col3, col4 = st.columns(2, gap="large")
        with col3:
            st.image(gray_image, caption="Original Grayscale", width=360)
        with col4:
            st.image(transformed_img, caption=caption, width=360)

        st.markdown(f"<p class='caption'><b>Transformation:</b> {caption}</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Camera & System Specifications")
    st.markdown("""
    - **Camera Used:** Mobile Phone Camera  
    - **Image Format:** JPG / PNG / JPEG  
    - **Color Mode:** 8-bit Grayscale  
    """)
    st.success("✅ Transformation successfully applied.")

else:
    st.info("👆 Upload an image file to start transformations.")

st.markdown("<hr><center style='color:#777;font-size:0.85rem;'>Developed by M.Sc. Computer Science Students with ❤️</center>", unsafe_allow_html=True)
