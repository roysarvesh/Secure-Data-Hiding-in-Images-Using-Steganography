Secure Data Hiding in Images Using Steganography

SecureImageStego is a Python-based steganography tool that allows users to hide and retrieve secret messages inside images using a password-protected encryption mechanism. The project is built with OpenCV, NumPy, and Streamlit, providing a simple and intuitive graphical user interface (GUI) for encoding and decoding messages securely.

Features

Encrypt Messages: Hide text messages inside an image with a password.

Password Protection: Uses SHA-256 hashing to secure stored messages.

Capacity Check: Ensures the image has enough space for data embedding.

Decrypt Messages: Retrieve hidden messages only with the correct password.

Streamlit GUI: A user-friendly web interface for easy operation.

Supports PNG & JPG Images

Installation & Setup

Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Steps to Install

Clone the repository:

git clone https://github.com/your-username/Secure-Image-Stego.git
cd Secure-Image-Stego

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Usage

Encrypting a Message:

Upload an image (PNG/JPG).

Enter the message you want to hide and a secure password.

The image will be processed and you can download the new encoded image.

Decrypting a Message:

Upload the encoded image.

Enter the correct password.

Retrieve the hidden message.

How It Works

The message is converted into UTF-8 encoded bytes.

A SHA-256 hash of the password is stored in the image.

The message bytes are embedded into pixel values in a secure and structured manner.

During decryption, the password is verified, and the hidden message is extracted only if it matches.

Security Measures

SHA-256 hashing ensures that the password is never stored in plaintext.

Error handling prevents decryption with an incorrect password.

Capacity validation ensures that images are large enough for embedding.


License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

Contact

For any issues or suggestions, feel free to reach out via GitHub Issues.

