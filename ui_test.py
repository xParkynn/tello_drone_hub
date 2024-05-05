import tkinter as tk
from Xlib.display import Display as xlib_display


def get_geometry():
    display = xlib_display(':0')
    main_monitor = display.screen().root.xrandr_get_monitors().monitors[0]
    width = main_monitor.width_in_pixels
    height = main_monitor.height_in_pixels
    return "".join([str(width-width//192), "x", str(height)])






if __name__ == "__main__":
    app = tk.Tk()
    app.title("Drohnenhub")

    app.resizable(width=True, height=True)
    app.geometry(get_geometry())

    label = tk.Label(app, text="Test")
    label.pack()

    app.mainloop()

