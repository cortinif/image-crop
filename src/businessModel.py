from PIL import Image
import numpy as np

def trim_white_margins(input_image_path, output_image_path, color=(255, 255, 255), tolerance=30):
    try:
        # Open the image
        image = Image.open(input_image_path)
        
        # Convert the image to RGBA (if it's not already in that mode)
        image = image.convert("RGBA")
        
        # Convert image to numpy array
        np_image = np.array(image)
        
        # Create a mask where pixels are close to the specified color within the given tolerance
        mask = np.all(np.abs(np_image[:, :, :3] - color) <= tolerance, axis=-1)
        
        # Find the bounding box of the non-matching regions
        coords = np.argwhere(~mask)
        
        if coords.size > 0:
            x0, y0, x1, y1 = coords[:, 1].min(), coords[:, 0].min(), coords[:, 1].max(), coords[:, 0].max()
            bbox = (x0, y0, x1 + 1, y1 + 1)
            # Crop the image to the bounding box
            cropped_image = image.crop(bbox)
            # Save the cropped image
            cropped_image.save(output_image_path)
            print(f"Image saved as {output_image_path}")
        else:
            print("No matching margins found or image is completely the specified color.")
        
    except Exception as e:
        print(f"Error: {e}")
