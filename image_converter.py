import streamlit as st
from PIL import Image
import io

st.title("🖼 Image Format Converter")
st.write("Upload an image, choose output format, and download the converted file.")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg", "bmp", "gif", "tiff", "webp"])

# Select output format
formats = ["PNG", "JPEG", "BMP", "GIF", "TIFF", "WEBP"]
output_format = st.selectbox("Select output format", formats)

if uploaded_file:
    # Open image
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Convert and save to buffer
    buf = io.BytesIO()
    img.save(buf, format=output_format)
    byte_data = buf.getvalue()

    # Download button
    st.download_button(
        label=f"Download as {output_format}",
        data=byte_data,
        file_name=f"converted.{output_format.lower()}",
        mime=f"image/{output_format.lower()}"
    )
