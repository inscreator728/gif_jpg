from PIL import Image
import os

def convert_images(input_folder, output_folder, output_format):
    """
    Convert all image files in the input_folder to the specified output_format (JPG or PNG) and save them to the output_folder.

    Args:
        input_folder (str): Path to the folder containing image files.
        output_folder (str): Path to the folder where converted files will be saved.
        output_format (str): Desired output format, either 'JPG' or 'PNG'.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List of common image extensions supported by PIL
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    image_files = [f for f in os.listdir(input_folder) if os.path.splitext(f)[1].lower() in image_extensions]

    if not image_files:
        print("No image files found in the input folder.")
        return

    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        base_name = os.path.splitext(image_file)[0]
        
        # Set output path based on chosen format
        if output_format == 'JPG':
            output_path = os.path.join(output_folder, base_name + '.jpg')
        elif output_format == 'PNG':
            output_path = os.path.join(output_folder, base_name + '.png')

        try:
            with Image.open(input_path) as img:
                if output_format == 'JPG':
                    # Convert to RGB for JPG (removes transparency)
                    img_converted = img.convert('RGB')
                    img_converted.save(output_path, 'JPEG')
                elif output_format == 'PNG':
                    # Save as-is to preserve transparency if present
                    img.save(output_path, 'PNG')
                print(f"Converted: {image_file} -> {os.path.basename(output_path)}")
        except Exception as e:
            print(f"Error converting {image_file}: {e}")

if __name__ == "__main__":
    print("Welcome to the Image Converter!")
    input_folder = input("Enter the path to the folder containing image files: ").strip()
    output_folder = input("Enter the path to the folder where converted files should be saved: ").strip()

    # Get and validate output format
    while True:
        output_format = input("Enter the desired output format (JPG or PNG): ").strip().upper()
        if output_format in ['JPG', 'PNG']:
            break
        print("Invalid format. Please enter 'JPG' or 'PNG'.")

    convert_images(input_folder, output_folder, output_format)
    print("Conversion process completed!")
