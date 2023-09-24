import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import time


class CookieClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookie Clicker")
        self.cookies = 0
        self.click_multiplier = 1
        self.auto_clickers = 0
        self.auto_clicker_cost = 50
        self.auto_clicker_increment = 1
        self.total_multiplier = 1

        self.cookie_image = Image.open("cookie.png")
        self.cookie_image = ImageTk.PhotoImage(self.cookie_image)

        self.cookie_button = tk.Button(
            root, image=self.cookie_image, command=self.click_cookie)
        self.cookie_button.pack(pady=10)

        self.info_label = tk.Label(
            root, text=f"Cookies: {self.format_number(self.cookies)}\nTotal Multiplier: {self.format_multiplier(self.total_multiplier)}\nAuto-clickers: {self.auto_clickers}")
        self.info_label.pack(pady=10)

        self.upgrade_label = tk.Label(root, text="Buy Click Upgrades:")
        self.upgrade_label.pack(pady=5)

        self.upgrade_levels = [0, 0, 0, 0]  # Keep track of upgrade levels

        for i in range(4):
            upgrade_button = tk.Button(root, text=f"Upgrade x{i+2} (Cost: {self.format_number(self.calculate_upgrade_cost(i))} cookies)",
                                       command=lambda i=i: self.buy_upgrade(i))
            upgrade_button.pack()

        self.auto_clicker_label = tk.Label(
            root, text=f"Auto-clickers (Cost: {self.format_number(self.auto_clicker_cost)} cookies)")
        self.auto_clicker_label.pack()

        self.buy_auto_clicker_button = tk.Button(
            root, text="Buy Auto-clicker", command=self.buy_auto_clicker)
        self.buy_auto_clicker_button.pack(pady=10)

        self.use_max_cookies_button = tk.Button(
            root, text="Use Max Cookies", command=self.use_max_cookies)
        self.use_max_cookies_button.pack(pady=10)

        self.auto_clicker_thread = None
        self.auto_clicker_active = False
        self.auto_clicker_clicks = 0

    def format_number(self, num):
        if num >= 10**9:  # Billion or more
            return f"{num // 10**9}B"
        elif num >= 10**6:  # Million or more
            return f"{num // 10**6}M"
        else:
            return f"{num:,}"

    def format_multiplier(self, num):
        if num >= 10**9:  # Billion or more
            return f"{num // 10**9}Bx"
        elif num >= 10**6:  # Million or more
            return f"{num // 10**6}Mx"
        else:
            return f"{num}x"

    def click_cookie(self):
        self.cookies += self.click_multiplier
        self.update_info_label()

    def buy_upgrade(self, level):
        cost = self.calculate_upgrade_cost(level)
        if self.cookies >= cost:
            self.cookies -= cost
            self.upgrade_levels[level] += 1
            self.click_multiplier = sum(
                [(i + 2) * level_count for i, level_count in enumerate(self.upgrade_levels)])
            self.total_multiplier = self.click_multiplier * \
                (self.auto_clickers + 1)
            self.update_info_label()
        else:
            messagebox.showerror(
                "Error", "Not enough cookies to buy this upgrade.")

    def buy_auto_clicker(self):
        if self.cookies >= self.auto_clicker_cost:
            self.cookies -= self.auto_clicker_cost
            self.auto_clickers += 1
            self.auto_clicker_cost += self.auto_clicker_increment
            self.total_multiplier = self.click_multiplier * \
                (self.auto_clickers + 1)
            self.update_info_label()

            if not self.auto_clicker_active:
                self.auto_clicker_active = True
                self.auto_clicker_thread = threading.Thread(
                    target=self.auto_clicker)
                self.auto_clicker_thread.start()
        else:
            messagebox.showerror(
                "Error", "Not enough cookies to buy the Auto-clicker.")

    def auto_clicker(self):
        while self.auto_clicker_active:
            self.cookies += self.auto_clickers * self.click_multiplier
            self.auto_clicker_clicks += self.auto_clickers
            self.update_info_label()
            time.sleep(1)

    def use_max_cookies(self):
        remaining_cookies = self.cookies
        # Start with the current total multiplier
        max_multiplier = self.total_multiplier

        for i in range(4):
            cost = self.calculate_upgrade_cost(i)
            while remaining_cookies >= cost:
                self.cookies -= cost
                self.upgrade_levels[i] += 1
                max_multiplier += (i + 2)
                remaining_cookies -= cost
                cost = self.calculate_upgrade_cost(i)

        while remaining_cookies >= self.auto_clicker_cost:
            self.cookies -= self.auto_clicker_cost
            self.auto_clickers += 1
            max_multiplier += 1
            remaining_cookies -= self.auto_clicker_cost
            self.auto_clicker_cost += self.auto_clicker_increment

        self.total_multiplier = max_multiplier
        self.update_info_label()
        messagebox.showinfo(
            "Info", f"Converted {self.format_number(self.cookies)} cookies into a total multiplier of {self.format_multiplier(max_multiplier)}.")

    def calculate_upgrade_cost(self, level):
        # Upgrade cost formula
        return 10 * (level + 2) ** (self.upgrade_levels[level] + 1)

    def update_info_label(self):
        self.info_label.config(
            text=f"Cookies: {self.format_number(self.cookies)}\nTotal Multiplier: {self.format_multiplier(self.total_multiplier)}\nAuto-clickers: {self.auto_clickers} (Clicks: {self.auto_clicker_clicks})")
        for i in range(4):
            self.root.nametowidget(self.upgrade_label.winfo_parent()).config(
                i, text=f"Upgrade x{i+2} (Cost: {self.format_number(self.calculate_upgrade_cost(i))} cookies)")


def main():
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
