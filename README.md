# Clipboard Keyboard v1.0.1

A utility application that simulates keyboard input to bypass problematic clipboard paste operations in certain applications.

## Important Note

**This application requires administrator privileges to function properly.** The keyboard simulation functionality requires elevated permissions to work correctly. Please ensure you run the application as administrator.

## Overview

Clipboard Keyboard is a Python-based tool that helps users input text in applications where standard clipboard paste operations don't work as expected. Instead of using the clipboard, it simulates actual keyboard input, ensuring consistent text entry across all applications.

## Features

- Text input through typing or pasting
- Simulates keyboard input for reliable text entry
- 5-second countdown timer before sending text
- Font customization options
- Control character removal
- Plain text paste support (Ctrl+V)
- Clean, user-friendly interface

## Installation

### For Users

1. Download the latest release (v1.0.0) from the releases page
2. Extract the ZIP file
3. Right-click on `ClipKeyboard.exe` and select "Run as administrator"

### For Developers

1. Ensure you have Python 3.x installed
2. Clone this repository:
   
   ```bash
   git clone https://github.com/yourusername/clipboard-keyboard.git
   cd clipboard-keyboard
   ```
3. Install required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

## Building from Source

To build the executable from source:

1. Ensure you have Python 3.x installed
2. Clone the repository and install dependencies as shown above
3. Run the build script:
   
   ```bash
   build.bat
   ```
   
   Or manually:
   
   ```bash
   python build.py
   ```
4. The executable will be created in the `dist` directory

## Project Structure

```
clipboard-keyboard/
├── dist/              # Distribution files (created during build)
├── build.py           # Python build script
├── build.bat          # Windows build script
├── ClipKeyboard.py    # Main application
├── LICENSE.txt        # License file
├── README.md          # This file
└── requirements.txt   # Python dependencies
```

## Usage

1. Run the application:
   
   ```bash
   python ClipKeyboard.py
   ```
   
   Or if using the executable:
   
   ```bash
   ClipKeyboard.exe
   ```
2. Type or paste your text into the main window
3. Click "Send as Keystrokes"
4. You have 5 seconds to switch to your target application
5. The text will be automatically typed out

### Additional Features

- **Set Font**: Customize the text display font and size
- **Clear**: Clear the text area
- **Remove Control Chars**: Strip control characters from the text
- **Plain Text Paste**: Use Ctrl+V to paste text without formatting

## Requirements

- Windows operating system
- Python 3.x (for development)
- **Administrator privileges** (required for keyboard simulation)

## Security Note

This application requires administrator privileges to function properly, as it needs to simulate keyboard input at the system level. This is a security requirement for Windows applications that need to interact with system-level input devices.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or feedback, please open an issue in the repository.
