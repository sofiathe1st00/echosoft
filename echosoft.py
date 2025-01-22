import ctypes
from ctypes import wintypes
import sys

# Constants
SPI_SETDESKWALLPAPER = 20
SPI_SETWORKAREA = 47

# Initialize ctypes
user32 = ctypes.WinDLL('user32', use_last_error=True)

def set_wallpaper(path):
    """Set the desktop wallpaper."""
    success = user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    if not success:
        print("Failed to set wallpaper. Ensure the path is correct.")

def set_work_area(left, top, right, bottom):
    """Set the work area for the desktop."""
    rect = wintypes.RECT(left, top, right, bottom)
    success = user32.SystemParametersInfoW(SPI_SETWORKAREA, 0, ctypes.byref(rect), 0)
    if not success:
        print("Failed to set work area.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python echosoft.py <command> [options]")
        print("Commands:")
        print("  set-wallpaper <file_path>")
        print("  set-workarea <left> <top> <right> <bottom>")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "set-wallpaper":
        if len(sys.argv) != 3:
            print("Usage: set-wallpaper <file_path>")
            sys.exit(1)
        set_wallpaper(sys.argv[2])

    elif command == "set-workarea":
        if len(sys.argv) != 6:
            print("Usage: set-workarea <left> <top> <right> <bottom>")
            sys.exit(1)
        try:
            left, top, right, bottom = map(int, sys.argv[2:6])
            set_work_area(left, top, right, bottom)
        except ValueError:
            print("Invalid input. Coordinates should be integers.")
            sys.exit(1)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()