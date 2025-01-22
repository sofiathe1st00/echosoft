# EchoSoft

EchoSoft is a Python application designed to customize and enhance the Windows graphical user interface for improved usability. It allows users to change their desktop wallpaper and set a custom work area for the desktop.

## Features

- **Set Wallpaper**: Change your desktop wallpaper to any image file.
- **Set Work Area**: Customize the work area of your desktop, effectively changing the usable space available for application windows.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Ensure you have Python 3 installed on your Windows machine.
2. Clone this repository or download the `echosoft.py` file.

## Usage

Open a terminal or command prompt and navigate to the directory containing `echosoft.py`. Use the following commands to interact with the application:

### Set Wallpaper

To change your desktop wallpaper, use the command:

```bash
python echosoft.py set-wallpaper <file_path>
```

Replace `<file_path>` with the path to your desired image file.

### Set Work Area

To set a custom work area, use the command:

```bash
python echosoft.py set-workarea <left> <top> <right> <bottom>
```

Replace `<left>`, `<top>`, `<right>`, and `<bottom>` with integer values representing the coordinates of your desired work area.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.