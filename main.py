"""
    Author: Jinesh Jain
    Desc  : A simple brightness dimmer for windows created in python. 
    Github: https://github.com/JineshRV

"""


import tkinter as tk
import pywintypes
from screeninfo import get_monitors
import win32gui
import win32con


def setClickthrough(hwnd):
    try:
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)
        win32gui.SetLayeredWindowAttributes(hwnd, 0x00000010, 255, 0x00000001)
    except Exception as e:
        pass


if __name__ == "__main__":
    alphavalue = float(input("Enter transparency value (0.0 - 0.75):") or 0.5)
    while True:
        if alphavalue <= 0.75:
            break
        else:
            alphavalue = float(input("**Not greater than 0.75 : ") or 0.5)
    root = tk.Tk()
    root.config(bg="black")
    screen = get_monitors()[0]
    root.geometry(f"{screen.width}x{screen.height}")
    root.wm_attributes("-alpha", alphavalue)
    root.overrideredirect(1)
    root.attributes('-transparentcolor', '#000000', '-topmost', 1)
    setClickthrough(root.winfo_id())
    root.mainloop()
