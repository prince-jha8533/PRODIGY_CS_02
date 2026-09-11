# 🔐 Image Encryption Tool

A simple Python-based **Image Encryption and Decryption Tool** that uses **pixel-level manipulation with XOR operations**.

The tool allows users to encrypt an image using a numeric key between **0 and 255** and decrypt it using the **same key**. The processed image is saved in **PNG format** to preserve lossless image data.

---

## 📌 Features

* 🔒 Encrypt images using XOR-based pixel manipulation
* 🔓 Decrypt encrypted images using the same key
* 🖼️ Supports common image formats readable by Pillow
* 🎨 Processes RGB pixel values individually
* 🔢 User-defined encryption key from `0–255`
* 💾 Automatically saves output as PNG
* ⚡ Simple command-line interface
* 🐍 Built with Python and Pillow

---

## 🧠 How It Works

The program reads an image and converts it to **RGB format**.

Each pixel contains three color channels:

```text
Pixel = (R, G, B)
```

The program applies an XOR operation between each color channel and the user-provided key:

```text
New R = R XOR Key
New G = G XOR Key
New B = B XOR Key
```

This operation is performed for every pixel in the image.

### Why XOR?

XOR has a useful property:

```text
A XOR K XOR K = A
```

Therefore, applying the **same key twice** restores the original pixel values.

For example:

```text
Original Pixel
(120, 200, 50)

       ↓ XOR Key

Encrypted Pixel
(..., ..., ...)

       ↓ XOR Same Key

Original Pixel
(120, 200, 50)
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Pillow (PIL)**
* `os` module

---

## 📂 Project Structure

```text
Image-Encryption-Tool/
│
├── image_enc.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/prince-jha8533/Image-Encryption-Tool.git
```

### 2. Navigate to the project directory

```bash
cd Image-Encryption-Tool
```

### 3. Install the required dependency

```bash
pip install Pillow
```

---

## ▶️ Usage

Run the program:

```bash
python image_enc.py
```

You will see:

```text
=== Image Encryption Tool (Pixel Manipulation) ===
1. Encrypt Image
2. Decrypt Image
```

Choose:

```text
1
```

for encryption or:

```text
2
```

for decryption.

Then provide:

```text
Enter path of the input image:
Enter path to save the output image:
Enter a key value (0-255):
```

### Example

```text
=== Image Encryption Tool (Pixel Manipulation) ===
1. Encrypt Image
2. Decrypt Image
Enter your choice (1 or 2): 1

Enter path of the input image: image.jpg
Enter path to save the output image: encrypted.png
Enter a key value (0-255): 123

Image encrypted successfully!
```

---

## 🔓 Decrypting an Image

To decrypt the image, select option `2` and use the **same key** that was used during encryption.

Example:

```text
Enter your choice (1 or 2): 2
Enter path of the input image: encrypted.png
Enter path to save the output image: decrypted.png
Enter a key value (0-255): 123

Image decrypted successfully!
```

> ⚠️ The encryption key must be the same for successful decryption.

---

## 🔑 Key Validation

The program accepts only integer keys between:

```text
0–255
```

Invalid values are rejected by the program.

---

## 💾 Output Format

The program saves processed images as:

```text
PNG
```

If a different extension is provided, the program changes the output filename to `.png` because PNG is lossless.

Example:

```text
encrypted.jpg
```

becomes:

```text
encrypted.png
```
