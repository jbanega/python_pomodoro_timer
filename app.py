import tkinter as tk
from tkinter import ttk
from collections import deque
from frames import Timer, Settings
from frames import set_dpi_awareness


COLOUR_PRIMARY = "#333333"              #dark charcoal
COLOUR_SECONDARY = "#555555"            #davy's gray
COLOUR_LIGHT_BACKGROUND = "#EEEEEE"     #bright gray
COLOUR_LIGHT_TEXT = "#E5E5E5"           #grey
COLOUR_DARK_TEXT = "#333333"            #dark charcoal


class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resizable(False, False)


        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Timer.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_PRIMARY)

        style.configure(
            "TimerText.TLabel",
            background=COLOUR_LIGHT_BACKGROUND,
            foreground=COLOUR_DARK_TEXT,
            font="Calibri 38"
        )

        style.configure(
            "LightText.TLabel",
            background=COLOUR_PRIMARY,
            foreground=COLOUR_LIGHT_TEXT
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOUR_SECONDARY,
            foreground=COLOUR_LIGHT_TEXT
        )

        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        )

        self["background"] = COLOUR_PRIMARY



        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)

        self.timer_order = ["Pomodoro", "Short break", "Pomodoro", "Short break", "Pomodoro", "Long break"]
        self.timer_scheduled = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)


        self.frames = dict()


        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NESW")

        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NESW")


        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame


        self.show_frame(Timer)
    

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


set_dpi_awareness()

app = PomodoroTimer()

app.mainloop()