from PIL import Image

# Define ASCII characters used for mapping grayscale values
ASCII_CHARS = '@%#*+=-:. '

# Resize image and convert to grayscale
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    grayscale_image = resized_image.convert("L")
    return grayscale_image

# Convert grayscale pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        index = pixel_value // 32
        ascii_str += ASCII_CHARS[index]
    return ascii_str

# Main function
def image_to_ascii(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image)
    ascii_str = pixels_to_ascii(image)
    ascii_width = image.width

    ascii_image = ""
    for i in range(0, len(ascii_str), ascii_width):
        ascii_image += ascii_str[i:i + ascii_width] + "\n"

    print(ascii_image)

    # Save ASCII art to a file
    save_to_file = input("Do you want to save the ASCII art to a file? (Y/N): ")
    if save_to_file.upper() == "Y":
        file_name = input("Enter the file name: ")
        with open(file_name, "w") as file:
            file.write(ascii_image)
        print(f"ASCII art saved to {file_name}.")

# Usage example
image_path = "PATH_TO_PICTURE"
image_to_ascii(image_path)
