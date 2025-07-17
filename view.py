import tkinter as tk
import tkinter.ttk as ttk


class View(tk.Tk):
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    button_captions = [
        "C",
        "+/-",
        "%",
        "/",
        7,
        8,
        9,
        "*",
        4,
        5,
        6,
        "-",
        1,
        2,
        3,
        "+",
        0,
        ".",
        "=",
    ]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("PyCalculator")
        self.value_var = tk.StringVar()
        self._make_frame()
        self._make_label()
        self._make_buttons()
        self._config_buttons_style()
        self._center_window()
        self.configure(bg="black")

    def main(self):
        self.mainloop()

    def _make_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(
            side="top", fill="both", expand=True, padx=self.PAD, pady=self.PAD
        )

    def _make_label(self):
        lbl = tk.Label(
            self.main_frm,
            anchor=tk.E,
            textvariable=self.value_var,
            background="black",
            foreground="white",
            font=("Arial", 30),
        )
        lbl.pack(fill=tk.X)

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        # frm = ttk.Frame(outer_frm)
        # frm.pack()
        is_first_row = True
        button_on_row = 0
        for caption in self.button_captions:
            if is_first_row or button_on_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False
                frm = ttk.Frame(outer_frm)
                frm.pack(fill=tk.X, expand=True)
                button_on_row = 0

            if isinstance(caption, int):
                style_prefix = "N"
            elif self._is_operator(caption):
                style_prefix = "O"
            else:
                style_prefix = "M"
            style = f"{style_prefix}.TButton"
            btn = ttk.Button(
                frm,
                text=caption,
                command=(
                    lambda button=caption: self.controller.on_button_click(button)
                ),
                style=style,
            )

            if caption == "=":
                fill = tk.X
                expand = True
            else:
                fill = None
                expand = False

            btn.pack(side="left", fill=fill, expand=expand)
            button_on_row += 1

    def _is_operator(self, button_caption):
        return button_caption in ["+", "-", "*", "/", "="]

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    def _config_buttons_style(self):
        style = ttk.Style()
        style.theme_use("default")
        # print(style.theme_names())
        # print(style.theme_use())

        # Style for number button
        style.configure(
            "N.TButton",
            background="gray",
            foreground="black",
            font=("Arial", 16),
        )
        # Style for operator button
        style.configure(
            "O.TButton",
            background="orange",
            foreground="black",
            font=("Arial", 16),
        )
        # Style for other button
        style.configure(
            "M.TButton",
            foreground="black",
            background="white",
            font=("Arial", 16),
        )
