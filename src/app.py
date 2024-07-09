# #!/usr/bin/env python3
import argparse
import sys
import os
from businessModel import trim_white_margins

def info():
    """Display information message and exit."""
    print("This script trims white margins from an image.")
    print("Usage:")
    print("  python main_script.py <input_image_path> [--output_image_path <path>] [--color <color>] [--color-type <type>] [--tolerance <value>] [--info]")
    print("\nOptions:")
    print("input_image_path:       Full path of the input image;")
    print("--output_image_path:    Full path of the output image;")
    print("--color:                Color that must be cropped;")
    print("--color-type:           Type rgb, hex (hexadecimal);")
    print("--tollerance:           Tollerance on color;")
    print("--info                  Show this information message and exit.")
    pass

def hex_to_rgb(hex_color):
    """Convert hex color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def parse_color(color, color_type):
    """Parse color input to RGB format."""
    if color_type.lower() == 'rgb':
        color = color.replace(' ', '').split(',')
        if len(color) != 3:
            raise ValueError("RGB color should have three components")
        return tuple(int(c) for c in color)
    elif color_type.lower() == 'hex':
        return hex_to_rgb(color)
    else:
        raise ValueError("Unsupported color type. Use 'rgb' or 'hex'.")
    
def generate_output_path(input_path:str) -> str:
    """Generate the output image path by appending '_cr' before the extension."""
    print("generate_output_path")
    base, ext = os.path.splitext(input_path)
    return f"{base}_cr{ext}"

def main():
    parser = argparse.ArgumentParser(description="Trim white margins from an image.")
    parser.add_argument('input_image_path', type=str, help='Path to the input image')
    parser.add_argument('--output_image_path', type=str, help='Path to save the trimmed image')
    parser.add_argument('--color', type=str, default='255,255,255', help='Color of the margins to be trimmed (default-white: (255, 255, 255))')
    parser.add_argument('--color-type', type=str, default='rgb', help='Color type (default: rgb)')
    parser.add_argument('--tolerance', type=int, default=30, help='Tolerance for trimming the margins (default: 30)')
    parser.add_argument('--info', action='store_true', help="Show this information message and exit.")

    args = parser.parse_args()

    if args.info:
        info()
    
    input_image_path =  str(args.input_image_path)
    file,input_image_path_ext = os.path.splitext(input_image_path)
    input_image_path_ext = input_image_path_ext.replace('.','')
    if ((input_image_path_ext is None) or (input_image_path_ext == "" ) or
        input_image_path_ext not in ('bmp','dib','jpeg','jpg','jpe','jp2','png','pbm','pgm','ppm','sr','ras','tiff','tif')):
        raise Exception('Image extension not compatible')
    
    output_image_path = str(args.output_image_path)
    if (args.output_image_path is None or str(args.output_image_path) == ""):
        output_image_path = generate_output_path(input_image_path) 
    
    try:
        color_rgb = parse_color(args.color, args.color_type)
    except ValueError as e:
        print(f"Error parsing color: {e}")
        sys.exit(1)

    # Call the trim function
    trim_white_margins(input_image_path, output_image_path, color=color_rgb, tolerance=args.tolerance)

if __name__ == "__main__":
    main()
