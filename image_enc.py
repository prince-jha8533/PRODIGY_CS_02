import os
from PIL import Image


def encrypt_decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image = image.convert("RGB")

    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            new_r = r ^ key
            new_g = g ^ key
            new_b = b ^ key
            pixels[x, y] = (new_r, new_g, new_b)

    image.save(output_path, format="PNG")
    print(f"Image saved to {output_path}")


def ensure_png_extension(path):
    """Force output filename to end with .png (lossless), regardless of user input."""
    base, ext = os.path.splitext(path)
    if ext.lower() != ".png":
        new_path = base + ".png"
        print(f"Note: Output must be lossless. Saving as '{new_path}' instead of '{path}'.")
        return new_path
    return path


def get_valid_key():
    """Prompt until a valid integer key between 0 and 255 is entered."""
    try:
        key = int(input("Enter a key value (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError
        return key
    except ValueError:
        print("Key must be an integer between 0 and 255.")
        return None


def main():
    print("=== Image Encryption Tool (Pixel Manipulation) ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid choice. Please enter 1 or 2.")
        return

    input_path = input("Enter path of the input image: ").strip()
    output_path = input("Enter path to save the output image: ").strip()
    output_path = ensure_png_extension(output_path)

    key = get_valid_key()
    if key is None:
        return

    try:
        encrypt_decrypt_image(input_path, output_path, key)
        action = "encrypted" if choice == "1" else "decrypted"
        print(f"Image {action} successfully!")
    except FileNotFoundError:
        print("Error: Input image not found. Check the path and try again.")


if __name__ == "__main__":
    main()