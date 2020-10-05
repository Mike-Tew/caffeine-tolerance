from tkinter import Tk, Label, Frame, LabelFrame, Button, Entry, END

# ---------------------- TESTING ALGORITHMN ---------------------
caffeine_list = [1280, 1280, 1680, 240, 320, 560, 960, 1360, 160, 120]

# print(sum(caffeine_list[-7:]) / 7)
# print(caffeine_list[-7:])

tolerance = sum(caffeine_list[-7:]) / 7
print(tolerance)

for index in range(0, 10):
    print(f"Day {index}: {tolerance}")
    tolerance = tolerance * 0.9 - 50

caffeine_tolerance = f"{round(tolerance)}mg"
print(caffeine_tolerance)


# ------------------------------------------------------------------
caffeine_level = 0


def add_caffeine(num):
    global caffeine_level
    caffeine_level += int(num)
    caffeine_entry.delete(0, END)
    caffeine_entry.insert(0, caffeine_level)


def _exit():
    root.destroy()


root = Tk()
root.title("Caffeine Tracker")

title_label = Label(
    root,
    width=34,
    height=2,
    text="CAFFEINE TOLERANCE",
    font=("Helvetica 16 bold"),
    bg="#bfbfbf",
)
title_label.grid(row=0, column=0, columnspan=4, pady=[0, 20])

# ---------------- BAR GRAPH FRAME -----------------
bar_frame = Frame(root)
bar_frame.grid(row=1, column=0, padx=[60, 0])

red_bar = Label(bar_frame, width=4, height=2, bg="#DF0020")
red_bar.grid(row=0, column=0)
orange_bar = Label(bar_frame, width=4, height=2, bg="#FF9300")
orange_bar.grid(row=1, column=0)
yellow_bar = Label(bar_frame, width=4, height=2, bg="#FFE500")
yellow_bar.grid(row=2, column=0)
green_bar = Label(bar_frame, width=4, height=2, bg="#00A000")
green_bar.grid(row=3, column=0)
blue_bar = Label(bar_frame, width=4, height=2, bg="#0000FF")
blue_bar.grid(row=4, column=0)

# ---------------- CAFFEINE LINE FRAME ----------------
line_frame = Frame(root)
line_frame.grid(row=1, column=1, padx=[0, 30])

line_label = Label(line_frame, text="<", font=("Helvetica 15 bold"))
line_label.grid(row=0, column=0, pady=[0, 20])

# ----------------- INFORMATION FRAME -------------------
info_frame = Frame(root, padx=10)
info_frame.grid(row=1, column=2, ipady=1)

tolerance_label = Label(
    info_frame, text="Your tolerance is:", font=("Helvetica 10 bold")
)
tolerance_label.grid(row=0, column=0)

info_frame_label = Label(info_frame, text=f"{round(tolerance)}mg", font=("15"))
info_frame_label.grid(row=1, column=0)

color_label = Label(info_frame, font=("Helvetica 12 bold"))
color_label.grid(row=2, column=0, pady=10)

todays_caffeine_label = Label(
    info_frame, text="Add today's caffeine:", font=("Helvetica 10 bold")
)
todays_caffeine_label.grid(row=3, column=0, pady=[10, 0])
caffeine_entry = Entry(info_frame, width=4, justify="right")
caffeine_entry.grid(row=4, column=0)
mg_label = Label(info_frame, text="mg")
mg_label.grid(row=4, column=0, sticky="e", padx=30)

add_caffeine_button = Button(info_frame, text="ADD", width=10)
add_caffeine_button.grid(row=5, column=0, pady=10)

if tolerance < 50:
    line_label.grid(pady=[175, 0])
    color_label.config(fg="#0000FF", text="NONE")
elif tolerance < 200:
    line_label.grid(pady=[140, 0])
    color_label.config(fg="#0000FF", text="MINIMAL")
elif tolerance < 400:
    line_label.grid(pady=[70, 0])
    color_label.config(fg="#00A000", text="LOW")
elif tolerance < 600:
    line_label.grid(pady=[0, 0])
    color_label.config(fg="#FFE500", bg="black", text="MODERATE")
elif tolerance < 800:
    line_label.grid(pady=[0, 70])
    color_label.config(fg="#FF9300", text="HIGH")
elif tolerance < 1000:
    line_label.grid(pady=[0, 140])
    color_label.config(fg="#DF0020", text="VERY HIGH")
else:
    line_label.grid(pady=[0, 175])
    color_label.config(fg="#DF0020", text="VERY HIGH")

# ---------------- ADD CAFFEINE FRAME -------------------
add_frame = LabelFrame(root, text="Add Caffeine", padx=10)
add_frame.grid(row=1, column=3, padx=20)

coffee_label = Label(add_frame, text="Coffee")
coffee_label.grid(row=0, column=0)
coffee_button = Button(add_frame, text="ADD", command=lambda: add_caffeine(80))
coffee_button.grid(row=0, column=1, pady=2)

tea_label = Label(add_frame, text="Tea")
tea_label.grid(row=1, column=0)
tea_button = Button(add_frame, text="ADD", command=lambda: add_caffeine(40))
tea_button.grid(row=1, column=1, pady=2)

red_bull_label = Label(add_frame, text="Red Bull")
red_bull_label.grid(row=2, column=0)
red_bull_button = Button(add_frame, text="ADD", command=lambda: add_caffeine(80))
red_bull_button.grid(row=2, column=1, pady=2)

monster_label = Label(add_frame, text="Monster")
monster_label.grid(row=3, column=0)
monster_button = Button(add_frame, text="ADD", command=lambda: add_caffeine(160))
monster_button.grid(row=3, column=1, pady=2)

espresso_label = Label(add_frame, text="Espresso")
espresso_label.grid(row=4, column=0)
espresso_button = Button(add_frame, text="ADD", command=lambda: add_caffeine(60))
espresso_button.grid(row=4, column=1, pady=2)

five_hour_label = Label(add_frame, text="5-hour")
five_hour_label.grid(row=5, column=0)
five_hour_button = Button(add_frame, text="ADD", command=lambda: add_caffeine(200))
five_hour_button.grid(row=5, column=1, pady=2)

exit_button = Button(
    root, text="EXIT", width=20, font=("Helvetica 16 bold"), command=_exit
)
exit_button.grid(row=2, column=0, padx=10, pady=10, columnspan=4)

root.mainloop()
