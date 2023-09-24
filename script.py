import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CookieClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        self.cookies = 0
        self.click_multiplier = 1

        self.cookie_image = Image.open("cookie.png")
        self.cookie_image = ImageTk.PhotoImage(self.cookie_image)

        self.cookie_button = tk.Button(
            root, image=self.cookie_image, command=self.click_cookie)
        self.cookie_button.pack(pady=10)

        self.info_label = tk.Label(
            root, text=f"Cookies: {self.cookies}\nClick Multiplier: {self.click_multiplier}")
        self.info_label.pack(pady=10)

        self.upgrade_button = tk.Button(
            root, text="Buy Click Upgrade (Cost: 10 cookies)", command=self.buy_upgrade)
        self.upgrade_button.pack(pady=10)

    def click_cookie(self):
        self.cookies += self.click_multiplier
        self.update_info_label()

    def buy_upgrade(self):
        if self.cookies >= 10:
            self.cookies -= 10
            self.click_multiplier += 1
            self.update_info_label()
        else:
            messagebox.showerror(
                "Error", "Not enough cookies to buy a Click Upgrade.")

    def update_info_label(self):
        self.info_label.config(
            text=f"Cookies: {self.cookies}\nClick Multiplier: {self.click_multiplier}")


def main():
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
