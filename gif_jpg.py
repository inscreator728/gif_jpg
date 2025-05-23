from PIL import Image
import os

def convert_gif_to_jpg(input_folder, output_folder):
    """
    Convert all GIF files in the input_folder to JPG format and save them to the output_folder.

    Args:
        input_folder (str): Path to the folder containing GIF files.
        output_folder (str): Path to the folder where converted JPG files will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    gif_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.gif')]

    if not gif_files:
        print("No GIF files found in the input folder.")
        return

    for gif_file in gif_files:
        input_path = os.path.join(input_folder, gif_file)
        output_path = os.path.join(output_folder, os.path.splitext(gif_file)[0] + '.jpg')

        try:
            with Image.open(input_path) as img:
                img = img.convert('RGB')  # Convert to RGB mode for JPG
                img.save(output_path, 'JPEG')
                print(f"Converted: {gif_file} -> {os.path.basename(output_path)}")
        except Exception as e:
            print(f"Error converting {gif_file}: {e}")

if __name__ == "__main__":
    print("Welcome to the GIF to JPG converter!")
    input_folder = input("Enter the path to the folder containing GIF files: ").strip()
    output_folder = input("Enter the path to the folder where JPG files should be saved: ").strip()

    convert_gif_to_jpg(input_folder, output_folder)

    print("Conversion process completed!")
