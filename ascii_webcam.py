import cv2
from PIL import Image
import numpy as np
import os
import time # Import time for measuring frame processing

def create_ascii_frame(image, cols, scale, invert_chars=False, gradient_chars=None):
    """
    Converts an image frame to ASCII art.
    Args:
        image (PIL.Image): The PIL Image object (should be grayscale).
        cols (int): Number of ASCII characters horizontally.
        scale (float): Aspect ratio adjustment.
        invert_chars (bool): If True, use a gradient from dark to light characters.
                             If False, use light to dark.
        gradient_chars (str or None): Custom ASCII character gradient.
                                      If None, default gradients are used.
    Returns:
        str: The ASCII art representation of the image.
    """
    # Define ASCII characters for different brightness levels
    # Default characters: from darkest to lightest
    DEFAULT_ASCII_CHARS_DARK_TO_LIGHT = '@%#*+=-:. '
    # Inverted characters: from lightest to darkest (for inverted brightness mapping)
    DEFAULT_ASCII_CHARS_LIGHT_TO_DARK = ' .:-=+*#%@'

    if gradient_chars:
        ASCII_CHARS = gradient_chars
    elif invert_chars:
        ASCII_CHARS = DEFAULT_ASCII_CHARS_LIGHT_TO_DARK
    else:
        ASCII_CHARS = DEFAULT_ASCII_CHARS_DARK_TO_LIGHT

    # Ensure the image is grayscale for consistent processing
    if image.mode != "L":
        image = image.convert("L")

    width, height = image.size
    
    # Calculate cell dimensions. We want cells to be roughly square in terms of pixel area
    # that gets averaged, then scale the character height to match terminal aspect ratio.
    cell_width = width / cols
    cell_height = cell_width * scale # Apply scale here to directly influence aspect ratio

    rows = int(height / cell_height)

    # Basic error check for impossible dimensions
    if cols <= 0 or rows <= 0:
        # print("Error: Calculated columns or rows are zero or negative. Adjust ASCII_COLS or ASCII_SCALE.")
        return ""

    ascii_frame = []
    # Use array operations for faster pixel averaging
    image_array = np.array(image)

    for i in range(rows):
        y1 = int(i * cell_height)
        y2 = int((i + 1) * cell_height)
        # Ensure y2 doesn't go out of bounds
        y2 = min(y2, height)
        if y1 >= y2: # Skip if cell height is zero or negative
            continue
        
        row_chars = []
        for j in range(cols):
            x1 = int(j * cell_width)
            x2 = int((j + 1) * cell_width)
            # Ensure x2 doesn't go out of bounds
            x2 = min(x2, width)
            if x1 >= x2: # Skip if cell width is zero or negative
                continue

            # Extract the cell using NumPy slicing for speed
            cell_pixels = image_array[y1:y2, x1:x2]
            
            # Calculate average pixel value. Handle empty cells if bounds are off.
            if cell_pixels.size > 0:
                avg_pixel = np.mean(cell_pixels)
            else:
                avg_pixel = 0 # Default to darkest if cell is empty

            # Map the average pixel value to an ASCII character
            # Scale 0-255 to 0 to len(ASCII_CHARS)-1
            char_index = int((avg_pixel / 255) * (len(ASCII_CHARS) - 1))
            char_index = max(0, min(char_index, len(ASCII_CHARS) - 1)) # Clamp values
            row_chars.append(ASCII_CHARS[char_index])
            
        ascii_frame.append("".join(row_chars))

    return "\n".join(ascii_frame)

def clear_console():
    """Clears the console screen."""
    # Use sys.stdout.write and \r for faster console updates on some systems,
    # but full clear is generally more reliable for consistent line count.
    # For speed, we'll stick to os.system for clearing.
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # --- Configuration ---
    WEBCAM_INDEX = 0  # Typically 0 for the default webcam
    
    # ASCII_COLS significantly impacts clarity and performance.
    # Higher values (e.g., 200+) give more detail but slow down significantly.
    # Aim for a value that makes sense for your terminal width.
    ASCII_COLS = 150 # Number of ASCII characters horizontally (e.g., 80, 120, 150, 200)

    # ASCII_SCALE: Adjusts the aspect ratio of characters.
    # Terminal characters are usually taller than they are wide.
    # Common values are 0.45 to 0.55. Experiment!
    ASCII_SCALE = 0.50 # A value of 0.5 is a good starting point for many terminals

    # Custom ASCII Character Gradient:
    # Experiment with different character sets for different looks.
    # Characters are ordered from darkest to lightest.
    # Example gradients:
    # " .':;l!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" (very dense)
    # " .`-_':,;=+|!/ijfvrzxcLJYXOCQZUtdbepqwmkhaoGNEF$BH@M#" (another dense one)
    # " .`-_':,;=+|!/ijfvrzxcLJYXOCQZUtdbepqwmkhaoGNEF$BH@M#" (another dense one)
    # "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,.` " (very detailed)
    CUSTOM_ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,.` "
    # CUSTOM_ASCII_CHARS = " .'`^,:;I!lTjC7xuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # A slightly shorter, but good gradient

    # Set to True to invert brightness mapping (e.g., dark pixels become light chars)
    INVERT_BRIGHTNESS = True # Set to False if you want traditional dark chars for dark pixels

    # Desired frames per second for ASCII conversion. Higher FPS means smoother video.
    # Be aware of performance limits.
    TARGET_FPS = 30 
    
    # Webcam resolution. Lower resolution generally means faster processing.
    # Set to None to use default webcam resolution.
    # Examples: (640, 480), (1280, 720)
    WEBCAM_RESOLUTION = (640, 480) 

    cap = cv2.VideoCapture(WEBCAM_INDEX)

    if not cap.isOpened():
        print(f"Error: Could not open webcam at index {WEBCAM_INDEX}.")
        print("Please check if the webcam is connected and not in use by another application.")
        return

    # Set webcam resolution if specified
    if WEBCAM_RESOLUTION:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, WEBCAM_RESOLUTION[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, WEBCAM_RESOLUTION[1])
    
    # Read actual resolution
    actual_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    actual_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Webcam opened with resolution: {actual_width}x{actual_height}")


    # Calculate delay between frames to achieve target FPS
    delay_ms = int(1000 / TARGET_FPS) if TARGET_FPS > 0 else 1

    print("\nPress 'q' to quit the ASCII video feed.")
    print("Adjust your terminal font size for best results!")
    
    frame_count = 0
    start_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame. Exiting.")
            break

        # Convert OpenCV BGR image to PIL RGB image
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # --- Dynamic Resizing for ASCII conversion ---
        # The ASCII_COLS determines the final ASCII output width.
        # We want to resize the *input* image to the `create_ascii_frame` function
        # such that its effective resolution matches the density of the ASCII output.
        # This prevents over-sampling (processing pixels that won't contribute much)
        # or under-sampling (losing detail).
        
        # Calculate target height based on desired ASCII_COLS and original aspect ratio
        original_width, original_height = pil_image.size
        
        # The "effective pixel width" for the ASCII conversion will be ASCII_COLS * cell_width.
        # Since cell_width is proportional to the original image width,
        # we can determine a target input resolution for the PIL image.
        
        # A good heuristic is to make the input image width slightly larger than ASCII_COLS
        # to ensure enough detail for the averaging. A factor of 2-3 is often suitable.
        # For better clarity, we might scale the input image to a resolution that is
        # directly proportional to the ASCII output grid.
        
        # Let's target an internal image resolution that is proportional to ASCII_COLS
        # and has enough pixel density per ASCII character cell.
        # If ASCII_COLS is 150, and each character is made from a 5x5 pixel block (for example),
        # then the internal image should be 150*5 pixels wide.
        
        # We'll use a simple scaling factor for the input image size to `create_ascii_frame`.
        # This factor balances performance and detail.
        # A factor of 1 is usually enough because `create_ascii_frame` does the cropping/averaging.
        # However, making the input image slightly larger *before* `create_ascii_frame`
        # can sometimes lead to smoother averages if there's an internal scaling going on.
        
        # For maximum clarity, the input image to create_ascii_frame should ideally have
        # a width and height that are multiples of the cell_width and cell_height it will calculate.
        # Let's simplify: the image passed to create_ascii_frame should have a width 
        # equal to ASCII_COLS and height proportional to ASCII_SCALE.
        
        target_pil_width = ASCII_COLS
        target_pil_height = int(target_pil_width * (original_height / original_width) * ASCII_SCALE)
        
        # Ensure minimum dimensions for robustness
        if target_pil_width == 0: target_pil_width = 1
        if target_pil_height == 0: target_pil_height = 1

        resized_image = pil_image.resize((target_pil_width, target_pil_height), Image.LANCZOS)
        # Image.LANCZOS (or Image.ANTIALIAS for older Pillow) is a high-quality downsampling filter.

        ascii_art = create_ascii_frame(
            resized_image, 
            ASCII_COLS, 
            ASCII_SCALE, 
            invert_chars=INVERT_BRIGHTNESS,
            gradient_chars=CUSTOM_ASCII_CHARS if CUSTOM_ASCII_CHARS else None
        )

        clear_console()
        print(ascii_art)

        # Update frame count and calculate FPS
        frame_count += 1
        elapsed_time = time.time() - start_time
        if elapsed_time > 1.0: # Update FPS every second
            actual_fps = frame_count / elapsed_time
            # print(f"\nFPS: {actual_fps:.2f} (Target: {TARGET_FPS})", end='') # Optional: print FPS
            frame_count = 0
            start_time = time.time()

        # Wait for a short period. `cv2.waitKey` is needed for OpenCV to process events.
        key = cv2.waitKey(delay_ms) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("ASCII video stream ended.")

if __name__ == "__main__":
    main()