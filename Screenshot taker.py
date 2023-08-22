import pyautogui
from tkinter import Tk, Button, Label

# Create a tkinter window
win = Tk()
win.title("LoopGlitch Screenshoter")

# Callback function to take a screenshot
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')  # Save the screenshot as 'screenshot.png' in the current directory
    status_label.config(text="Screenshot saved as 'screenshotbyGOKUL.png'")

# Create a label for instructions
instructions_label = Label(win, text="Click the button to take a screenshot.")
instructions_label.pack(pady=10)

# Create a button to trigger the screenshot
screenshot_button = Button(win, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=5)

# Create a label to display status
status_label = Label(win, text="", fg="green")
status_label.pack(pady=5)

# Start the tkinter event loop
win.mainloop()
