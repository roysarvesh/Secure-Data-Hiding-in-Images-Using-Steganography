🔒 Secure Data Hiding in Images Using Steganography
📌 Overview

In the digital era, secure data transmission is crucial to prevent unauthorized access. This project implements steganography to hide text messages within image pixels using a password-protected encryption mechanism. The system ensures confidentiality by hashing passwords and validating image capacity before embedding messages. A Streamlit-based GUI provides an intuitive interface for seamless encryption and decryption.
🛠️ Technologies Used

    Programming Language: Python
    Libraries: OpenCV, NumPy, Streamlit, PIL (Pillow), Hashlib
    Platform: Streamlit (GUI), Jupyter Notebook/VS Code (Development)

✨ Unique Features

✅ Password-Protected Steganography – Uses SHA-256 hashing for enhanced security.
✅ Pixel-Level Encryption – Embeds both hashed passwords and messages securely.
✅ Capacity Validation – Ensures image size can accommodate the message before embedding.
✅ User-Friendly Streamlit GUI – Simple interface for encryption & decryption.
✅ Efficient & Lightweight – Works with PNG/JPG images without significant quality loss.
📥 Installation & Setup

    Clone the Repository

git clone https://github.com/roysarvesh/Secure-Data-Hiding-in-Images-Using-Steganography.git
cd Secure-Data-Hiding-in-Images-Using-Steganography

Install Dependencies

pip install -r requirements.txt

Run the Application

    streamlit run app.py

📌 Usage
🔹 Encryption (Hiding Message)

    Upload an image (PNG/JPG/JPEG).
    Enter the secret message.
    Set a password for protection.
    Download the encrypted image.

🔹 Decryption (Retrieving Message)

    Upload the encrypted image.
    Enter the correct password.
    Retrieve the hidden message securely.

🚀 Future Scope

🔹 AES/RSA Encryption – For even stronger security.
🔹 Multi-Format Support – Extending to GIFs, BMPs, and video steganography.
🔹 AI-Based Detection Prevention – Making it resistant to steganalysis.
🔹 Cloud Integration – Secure cloud-based encrypted image storage.
🔹 Mobile Application – Developing an Android/iOS app for real-time steganography.
📜 License

This project is open-source and available under the MIT License.
📩 Contact

📌 Developer: Sarvesh Kumar Roy
📌 GitHub: https://github.com/roysarvesh/Secure-Data-Hiding-in-Images-Using-Steganography
