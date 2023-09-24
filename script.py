import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class CookieClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        self.cookies = 0
        self.click_multiplier = 1

        self.auto_clicker_cost = 50
        self.click_upgrade_costs = [10, 50, 100, 500]

        self.cookie_image = Image.open("cookie.png")
        self.cookie_image = ImageTk.PhotoImage(self.cookie_image)

        self.cookie_button = tk.Button(
            root, image=self.cookie_image, command=self.click_cookie)
        self.cookie_button.pack(pady=10)

        self.info_label = tk.Label(
            root, text=f"Cookies: {self.cookies}\nClick Multiplier: {self.click_multiplier}")
        self.info_label.pack(pady=10)

        self.upgrade_label = tk.Label(root, text="Buy Click Upgrades:")
        self.upgrade_label.pack(pady=5)

        for i, cost in enumerate(self.click_upgrade_costs):
            upgrade_button = tk.Button(root, text=f"Upgrade x{i+2} (Cost: {cost} cookies)",
                                       command=lambda i=i: self.buy_upgrade(i))
            upgrade_button.pack()

        self.auto_clicker_button = tk.Button(root, text=f"Buy Auto Clicker (Cost: {self.auto_clicker_cost} cookies)",
                                             command=self.buy_auto_clicker)
        self.auto_clicker_button.pack(pady=10)

        self.cookies_to_spend_label = tk.Label(
            root, text="Enter cookies to spend:")
        self.cookies_to_spend_label.pack()

        self.cookies_to_spend_entry = tk.Entry(root)
        self.cookies_to_spend_entry.pack()

        self.spend_button = tk.Button(
            root, text="Spend Cookies", command=self.spend_cookies)
        self.spend_button.pack()

        self.auto_clicker_active = False

    def click_cookie(self):
        self.cookies += self.click_multiplier
        self.update_info_label()

    def buy_upgrade(self, level):
        cost = self.click_upgrade_costs[level]
        if self.cookies >= cost:
            self.cookies -= cost
            self.click_multiplier = level + 2
            self.update_info_label()
        else:
            messagebox.showerror(
                "Error", "Not enough cookies to buy this upgrade.")

    def buy_auto_clicker(self):
        if self.cookies >= self.auto_clicker_cost:
            self.cookies -= self.auto_clicker_cost
            self.auto_clicker_active = True
            self.root.after(1000, self.auto_click)
            self.update_info_label()
        else:
            messagebox.showerror(
                "Error", "Not enough cookies to buy the Auto Clicker.")

    def auto_click(self):
        if self.auto_clicker_active:
            self.click_cookie()
            self.root.after(1000, self.auto_click)

    def spend_cookies(self):
        try:
            cookies_to_spend = int(self.cookies_to_spend_entry.get())
            if cookies_to_spend > 0 and cookies_to_spend <= self.cookies:
                self.cookies -= cookies_to_spend
                self.update_info_label()
            else:
                messagebox.showerror(
                    "Error", "Invalid amount of cookies to spend.")
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid number of cookies to spend.")

    def update_info_label(self):
        self.info_label.config(
            text=f"Cookies: {self.cookies}\nClick Multiplier: {self.click_multiplier}")
        self.auto_clicker_button.config(
            text=f"Buy Auto Clicker (Cost: {self.auto_clicker_cost} cookies)")
        for i, cost in enumerate(self.click_upgrade_costs):
            self.root.nametowidget(self.upgrade_label.winfo_parent()).config(
                i, text=f"Upgrade x{i+2} (Cost: {cost} cookies)")


def main():
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
