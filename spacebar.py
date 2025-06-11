#!/usr/bin/env python3
"""
spacebar_left_click.py

Listens for the spacebar key press and simulates a left mouse click at the current cursor position on macOS, using pynput.

Requirements:
    • pynput  (for global hotkey listening and mouse control)

Install with:
    pip install pynput

Usage:
    • Run this script.
    • Press SPACE to trigger a left click.
    • Press ESC to exit the script.
"""
from pynput import keyboard, mouse
from pynput.keyboard import Key

# Create mouse controller
mouse_ctrl = mouse.Controller()

def on_press(key):
    """Callback for key press: SPACE = left click, ESC = exit."""
    if key == Key.space:
        mouse_ctrl.click(mouse.Button.left, 1)
    elif key == Key.esc:
        # Stop listener
        return False


def main():
    print("[INFO] Press SPACE to click. Press ESC to exit.")
    # Start listening for keyboard events
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
