# ASCII Art Converter

This Python script converts images into ASCII art.

## How it Works

The script takes an input image file, resizes it, and converts each pixel to a corresponding ASCII character based on its brightness level. The brightness level determines which ASCII character is used, creating a visual representation of the image in ASCII form.

## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/nanadotam/ascii-art-converter.git

2. Navigate to the project directory:
cd img-to-ascii

3. Run the script with the following command, providing the necessary arguments:
python3 img-to-ascii.py <image_path> <image_type> <output_file> <scale>

Replace `<image_path>` with the path to the input image file, `<image_type>` with the image file type (e.g., jpg, png), `<output_file>` with the desired name for the output ASCII art file, and `<scale>` with the scaling factor (an integer value).

For example:
python3 img-to-ascii.py mona_lisa.jpg jpg mona_lisa_ascii.txt 3


This command will convert the "mona_lisa.jpg" image to ASCII art, scale it down by a factor of 3, and save the output to "mona_lisa_ascii.txt".

## Dependencies

- Python 3
- Pillow (Python Imaging Library)

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.


