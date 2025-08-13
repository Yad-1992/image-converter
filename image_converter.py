# -------------------------------------------------------
# Bulk Image Converter Web App
# Author: Nirmal Sahoo
# Created: 2025
# Description: Convert multiple images to different formats and download as ZIP
# -------------------------------------------------------

import streamlit as st
from PIL import Image
import io
import zipfile
import os

# --- Visitor Counter Function ---
def update_counter():
    counter_file = "counter.txt"
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")
    with open(counter_file, "r") as f:
        count = int(f.read().strip())
    count += 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count

# Update and get visitor count
visitor_count = update_counter()

# --- Logo ---
st.image("logo.png", width=100)

# --- Title ---
st.title("🖼 Bulk Image Format Converter")
st.write(f"Welcome! You are visitor number **{visitor_count}**.")
st.write("Upload multiple images, choose output format, and download them as a ZIP file.")

# --- File uploader ---
uploaded_files = st.file_uploader(
    "Choose images", 
    type=["png", "jpg", "jpeg", "bmp", "gif", "tiff", "webp"], 
    accept_multiple_files=True
)

# --- Output format selection ---
formats = ["PNG", "JPEG", "BMP", "GIF", "TIFF", "WEBP"]
output_format = st.selectbox("Select output format", formats)

if uploaded_files:
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zipf:
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file).convert("RGB")
            output_name = os.path.splitext(uploaded_file.name)[0] + "." + output_format.lower()

            img_bytes = io.BytesIO()
            img.save(img_bytes, format=output_format)
            zipf.writestr(output_name, img_bytes.getvalue())

    st.download_button(
        label=f"Download all images as ZIP ({output_format})",
        data=zip_buffer.getvalue(),
        file_name=f"converted_images.zip",
        mime="application/zip"
    )

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Developed by **Nirmal Sahoo**")
