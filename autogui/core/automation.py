import pyautogui

def click(x, y):
    pyautogui.click(x, y)

def type_text(text):
    pyautogui.write(text)

def main():
    # Example usage
    click(100, 100)
    type_text("Hello, world!")

if __name__ == "__main__":
    main()
