# ASCII Webcam

This project converts your webcam feed into live ASCII art directly in your terminal!

## Project Description

`ascii_webcam.py` is a Python script that captures video from your webcam, processes each frame, and renders it as ASCII characters in the console. It provides a fun, retro way to view your webcam feed and includes several options for customization.

## Features

*   **Real-time ASCII Conversion:** See your webcam feed transformed into ASCII art live.
*   **Customizable ASCII Characters:** Choose your own set of characters for the gradient or use the defaults.
*   **Invert Brightness:** Option to invert the brightness mapping (e.g., dark pixels become light characters or vice-versa).
*   **Adjustable Output Width:** Control the number of ASCII characters used horizontally (`ASCII_COLS`).
*   **Aspect Ratio Scaling:** Fine-tune the aspect ratio of the ASCII output to match your terminal font (`ASCII_SCALE`).
*   **FPS Control:** Set a target Frames Per Second (`TARGET_FPS`) for the conversion.
*   **Webcam Resolution:** Specify a desired resolution for webcam capture.
*   **Performance Monitoring:** Displays actual FPS (optional, can be uncommented in the code).

## Requirements

*   Python 3.x
*   OpenCV (`cv2`): For webcam access and image processing.
    *   Installation: `pip install opencv-python`
*   Pillow (PIL): For image manipulation.
    *   Installation: `pip install Pillow`
*   NumPy: For efficient array calculations.
    *   Installation: `pip install numpy`

You can install all required libraries with:
`pip install opencv-python Pillow numpy`

## How to Run

1.  Ensure you have a webcam connected and the required libraries installed.
2.  Clone this repository or download the `ascii_webcam.py` script.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the script.
5.  Run the script using Python:

    ```bash
    python ascii_webcam.py
    ```

## Configuration

You can customize the behavior of the ASCII webcam by modifying the parameters at the beginning of the `main()` function in the `ascii_webcam.py` script:

*   `WEBCAM_INDEX` (default: `0`): The index of your webcam. If `0` doesn't work, try `1`, `2`, etc.
*   `ASCII_COLS` (default: `150`): Number of ASCII characters horizontally. Higher values give more detail but can slow down performance and might require a wider terminal.
*   `ASCII_SCALE` (default: `0.50`): Adjusts the aspect ratio. Terminal characters are often taller than they are wide. Values between `0.45` and `0.55` are common. Experiment for best results with your terminal font.
*   `CUSTOM_ASCII_CHARS` (default: `"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,. \`"`): A string of characters ordered from darkest to lightest used for rendering. You can provide your own custom gradient. If set to `None` or an empty string, default gradients will be used based on `INVERT_BRIGHTNESS`.
*   `INVERT_BRIGHTNESS` (default: `True`):
    *   `True`: Darker image areas are represented by lighter ASCII characters, and brighter areas by darker characters (useful for light terminal themes or if the default gradient is light-to-dark).
    *   `False`: Traditional mapping - darker image areas are represented by darker ASCII characters.
*   `TARGET_FPS` (default: `30`): Desired frames per second for the ASCII conversion. Performance depends on your system and the chosen `ASCII_COLS` and resolution.
*   `WEBCAM_RESOLUTION` (default: `(640, 480)`): Set a specific resolution (width, height) for the webcam. Lower resolutions generally result in faster processing. Set to `None` to use the webcam's default resolution.

## Controls

*   **`q`**: Press 'q' while the ASCII video feed window is active (or your terminal is focused) to quit the application.

## Troubleshooting

*   **Webcam Not Found/Error Opening Webcam:**
    *   Ensure your webcam is properly connected and not being used by another application.
    *   Try changing the `WEBCAM_INDEX` in the script.
    *   Verify that OpenCV can access your webcam using a simpler test script if issues persist.
*   **Low FPS:**
    *   Decrease `ASCII_COLS`.
    *   Decrease `WEBCAM_RESOLUTION`.
    *   Ensure your system is not under heavy load.
*   **Output Looks Squished or Stretched:**
    *   Adjust `ASCII_SCALE` to better match your terminal's font aspect ratio.

## License

This project is open-source. Feel free to modify and distribute it. (No specific license file provided, you might consider adding one like MIT).
```
