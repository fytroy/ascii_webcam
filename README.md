# ASCII Webcam - Real-time ASCII Art from your Webcam

This project captures video from your webcam, converts each frame into ASCII art in real-time, and displays it in your terminal.

## Features

*   **Real-time Conversion:** Captures webcam feed and converts it to ASCII art live.
*   **Configurable Output Width:** Adjust the number of ASCII characters per line (`ASCII_COLS`) for different levels of detail and terminal sizes.
*   **Aspect Ratio Adjustment:** Fine-tune the character aspect ratio (`ASCII_SCALE`) to match your terminal's font for a more accurate representation.
*   **Customizable Character Sets:** Define your own ASCII character gradients (`CUSTOM_ASCII_CHARS`) to achieve different visual styles.
*   **Brightness Inversion:** Option to invert brightness (`INVERT_BRIGHTNESS`), mapping dark pixels to light characters or vice-versa.
*   **FPS Control:** Set a target Frames Per Second (`TARGET_FPS`) for the ASCII video output.
*   **Webcam Resolution Setting:** Specify a desired resolution (`WEBCAM_RESOLUTION`) for the webcam input to balance performance and quality.
*   **Cross-Platform:** Clears console on both Windows (`cls`) and Unix-like systems (`clear`).

## Requirements

*   Python 3.x
*   A webcam connected to your computer.
*   The following Python libraries:
    *   OpenCV (`opencv-python`)
    *   Pillow (`Pillow`)
    *   NumPy (`numpy`)

## Installation

1.  Ensure you have Python 3 installed.
2.  Clone this repository or download the `ascii_webcam.py` script.
3.  Install the required Python libraries using pip:
    ```bash
    pip install opencv-python pillow numpy
    ```

## Usage

1.  Navigate to the directory where you saved `ascii_webcam.py`.
2.  Run the script from your terminal:
    ```bash
    python ascii_webcam.py
    ```
3.  Press 'q' to quit the application.

### Configuration

You can customize the behavior of the ASCII webcam by modifying the following variables at the beginning of the `main()` function in the `ascii_webcam.py` script:

*   `WEBCAM_INDEX`: Set this to the index of your webcam (usually 0 for the default one).
*   `ASCII_COLS`: Number of ASCII characters horizontally. Higher values give more detail but can be slower and might require a wider terminal. (e.g., 80, 120, 150).
*   `ASCII_SCALE`: Adjusts the aspect ratio of characters. Values around 0.45-0.55 often work well, but you might need to experiment based on your terminal font.
*   `CUSTOM_ASCII_CHARS`: A string of characters ordered from darkest to lightest, defining the gradient used for ASCII mapping. Several examples are provided in the script.
*   `INVERT_BRIGHTNESS`: Set to `True` to map dark image areas to light ASCII characters and vice-versa. Set to `False` for the traditional mapping (dark areas to dark characters).
*   `TARGET_FPS`: Desired frames per second for the ASCII conversion. Higher values result in smoother video but are more performance-intensive.
*   `WEBCAM_RESOLUTION`: A tuple `(width, height)` to set a specific resolution for your webcam (e.g., `(640, 480)`). Set to `None` to use the webcam's default resolution.

Adjust your terminal font size and window dimensions for the best viewing experience.

## How it Works

The script performs the following steps in a loop:

1.  **Frame Capture:** Reads a frame from the webcam using OpenCV.
2.  **Color Conversion:** Converts the captured frame (usually in BGR format) to an RGB image using Pillow.
3.  **Resizing:** The PIL image is resized to a width equal to `ASCII_COLS` and a height that maintains the original aspect ratio, adjusted by `ASCII_SCALE`. This prepares the image for efficient ASCII mapping.
4.  **Grayscale Conversion:** The resized image is converted to grayscale.
5.  **ASCII Mapping (`create_ascii_frame` function):**
    *   The grayscale image is divided into a grid of cells, where the number of columns is `ASCII_COLS`.
    *   For each cell, the average pixel brightness is calculated.
    *   This average brightness is then mapped to a character from the specified ASCII character set (e.g., `CUSTOM_ASCII_CHARS` or default sets). The mapping depends on whether `INVERT_BRIGHTNESS` is active.
6.  **Console Output:** The resulting string of ASCII characters is printed to the terminal, effectively creating one frame of the ASCII video. The console is cleared before printing each new frame to create an animation effect.

## Example Output

The output is a real-time stream of ASCII characters in your terminal that represents your webcam's view. Imagine your face, or whatever your webcam sees, drawn with letters and symbols, constantly updating!

For best results:
*   Use a monospaced font in your terminal.
*   Adjust your terminal's font size and window dimensions.
*   Experiment with the `ASCII_COLS` and `ASCII_SCALE` settings in the script.

## License

This project is open-source and available under the [MIT License](LICENSE).
(You may want to create a `LICENSE` file with the contents of the MIT License or choose another license.)
