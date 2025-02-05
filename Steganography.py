import cv2
import numpy as np
import streamlit as st
import hashlib
from io import BytesIO
from PIL import Image

class SecureImageSteganography:
    def __init__(self):
        pass

    def hash_password(self, password):
        """Generate secure and consistent hash for password"""
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def validate_image_capacity(self, img, msg_length):
        """Check if image can accommodate the message"""
        max_capacity = img.shape[0] * img.shape[1] * 3
        return msg_length < max_capacity

    def encrypt_message(self, img, msg, password):
        """Encrypt the message and store it in the image"""
        encrypted_img = img.copy()
        hashed_password = self.hash_password(password).encode('utf-8')  # Store hash as UTF-8 encoded bytes
        msg_bytes = msg.encode('utf-8')
        msg_length = len(msg_bytes)

        if not self.validate_image_capacity(img, msg_length + len(hashed_password) + 5):
            raise ValueError("Message too large for the image")

        length_bytes = msg_length.to_bytes(4, byteorder='big')
        n, m, z = 0, 0, 0

        # Encode hashed password
        for byte in hashed_password:
            encrypted_img[n, m, z] = byte
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m == img.shape[1]:
                    m = 0
                    n += 1

        # Delimiter
        encrypted_img[n, m, z] = 255
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == img.shape[1]:
                m = 0
                n += 1

        # Encode length bytes
        for byte in length_bytes:
            encrypted_img[n, m, z] = byte
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m == img.shape[1]:
                    m = 0
                    n += 1

        # Another delimiter
        encrypted_img[n, m, z] = 255
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == img.shape[1]:
                m = 0
                n += 1

        # Encode actual message
        for byte in msg_bytes:
            encrypted_img[n, m, z] = byte
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m == img.shape[1]:
                    m = 0
                    n += 1

        return encrypted_img

    def decrypt_message(self, img, input_password):
        """Decrypt message from the image"""
        try:
            n, m, z = 0, 0, 0
            retrieved_hash_bytes = bytearray()

            while True:
                pixel_value = img[n, m, z]
                if pixel_value == 255:  # Delimiter
                    break
                retrieved_hash_bytes.append(pixel_value)
                z = (z + 1) % 3
                if z == 0:
                    m += 1
                    if m == img.shape[1]:
                        m = 0
                        n += 1

            retrieved_hash = retrieved_hash_bytes.decode('utf-8')
            input_hash = self.hash_password(input_password)

            if input_hash != retrieved_hash:
                return "Error: Incorrect Password"

            # Move past the delimiter
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m == img.shape[1]:
                    m = 0
                    n += 1

            length_bytes = bytearray()
            for _ in range(4):
                length_bytes.append(img[n, m, z])
                z = (z + 1) % 3
                if z == 0:
                    m += 1
                    if m == img.shape[1]:
                        m = 0
                        n += 1

            msg_length = int.from_bytes(length_bytes, byteorder='big')
            if msg_length <= 0:
                return "Error: Invalid message length"

            # Move past the delimiter
            z = (z + 1) % 3
            if z == 0:
                m += 1
                if m == img.shape[1]:
                    m = 0
                    n += 1

            msg_bytes = bytearray()
            for _ in range(msg_length):
                msg_bytes.append(img[n, m, z])
                z = (z + 1) % 3
                if z == 0:
                    m += 1
                    if m == img.shape[1]:
                        m = 0
                        n += 1

            return msg_bytes.decode('utf-8')
        except Exception as e:
            return f"Decryption Error: {str(e)}"

# Streamlit GUI
st.title("🔒 Secure Data Hiding in Images Using Steganography🔒 ")
st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an operation", ["Encrypt", "Decrypt"])

steg = SecureImageSteganography()

if option == "Encrypt":
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    message = st.text_area("Enter the message to hide")
    password = st.text_input("Enter password", type="password")
    if uploaded_image and message and password:
        image = np.array(Image.open(uploaded_image))
        encrypted_image = steg.encrypt_message(image, message, password)
        encrypted_pil = Image.fromarray(encrypted_image)
        buf = BytesIO()
        encrypted_pil.save(buf, format="PNG")
        st.download_button("Download Encrypted Image", buf.getvalue(), file_name="encrypted.png", mime="image/png")

if option == "Decrypt":
    uploaded_image = st.file_uploader("Upload an encrypted image", type=["png", "jpg", "jpeg"])
    password = st.text_input("Enter password", type="password")
    if uploaded_image and password:
        image = np.array(Image.open(uploaded_image))
        decrypted_message = steg.decrypt_message(image, password)
        st.text_area("Decrypted Message", decrypted_message, disabled=True)
