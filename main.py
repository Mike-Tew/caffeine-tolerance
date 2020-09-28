from tkinter import Tk, Label, Frame, LabelFrame, Button, Entry, END

# ---------------------- TESTING ALGORITHMN ---------------------
caffeine_list = [1280, 1280, 1680, 240, 320, 560, 960, 1360, 160, 120]

print(sum(caffeine_list[-7:]) / 7)
print(caffeine_list[-7:])

my_num = 1000

for index in range(0, 10):
    # print(f"Day {index}: {my_num}")
    my_num = my_num * 0.9 - 50

caffeine_tolerance = f"{round(my_num)}mg"
print(caffeine_tolerance)


# ------------------------------------------------------------------

caffeine_level = 0

def add_caffeine(num):
    global caffeine_level

    print(num)
    caffeine_level += int(num)
    print(type(caffeine_level))
    print(caffeine_level)
    caffeine_entry.delete(0, END)
    caffeine_entry.insert(0, caffeine_level)

def _exit():
    root.destroy()

root = Tk()
root.title("Caffeine Tracker")

title_label = Label(root, text="CAFFEINE TOLERANCE", font=("Helvetica 16 bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=[5, 0])

# ---------------- BAR GRAPH FRAME -----------------
bar_frame = Frame(root, padx=10, pady=5)
bar_frame.grid(row=1, column=0)

bar_frame_label = Label(bar_frame, text="Bar Graph")
bar_frame_label.grid(row=0, column=0)

# ----------------- INFORMATION FRAME -------------------
info_frame = Frame(root, padx=10, pady=5)
info_frame.grid(row=1, column=1)

tolerance_label = Label(info_frame, text="Your tolerance is:", font=("Helvetica 10 bold"))
tolerance_label.grid(row=0, column=0)

info_frame_label = Label(info_frame, text=caffeine_tolerance)
info_frame_label.grid(row=1, column=0)

todays_caffeine_label = Label(info_frame, text="Add today's caffeine:", font=("Helvetica 10 bold"))
todays_caffeine_label.grid(row=2, column=0)
caffeine_entry = Entry(info_frame, width=10)
caffeine_entry.grid(row=3, column=0)

# ---------------- ADD CAFFEINE FRAME -------------------
add_frame = LabelFrame(root, text="Add Caffeine", padx=10, pady=5)
add_frame.grid(row=1, column=2, padx=20)

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

exit_button = Button(root, text="EXIT", width=20, font=("Helvetica 16 bold"), command=_exit)
exit_button.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

root.mainloop()
