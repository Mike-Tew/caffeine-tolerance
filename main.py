from tkinter import Tk, Label, Frame, LabelFrame, Button

root = Tk()
root.title("Caffeine Tracker")

title_label = Label(root, text="CAFFEINE TOLERANCE", font=("Helvetica 16 bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=[5, 0])

# ---------------- BAR GRAPH FRAME -----------------
bar_frame = Frame(root, padx=10, pady=5)
bar_frame.grid(row=1, column=0)

bar_frame_label = Label(bar_frame, text="Tolerance")
bar_frame_label.grid(row=0, column=0)

# ----------------- INFORMATION FRAME -------------------
info_frame = Frame(root, padx=10, pady=5)
info_frame.grid(row=1, column=1)

info_frame_label = Label(info_frame, text="Info")
info_frame_label.grid(row=0, column=0)

# ---------------- ADD CAFFEINE FRAME -------------------
add_frame = LabelFrame(root, text="Add Caffeine", padx=10, pady=5)
add_frame.grid(row=1, column=2, padx=20)

coffee_label = Label(add_frame, text="Coffee")
coffee_label.grid(row=0, column=0)
coffee_button = Button(add_frame, text="ADD")
coffee_button.grid(row=0, column=1)

tea_label = Label(add_frame, text="Tea")
tea_label.grid(row=1, column=0)
tea_button = Button(add_frame, text="ADD")
tea_button.grid(row=1, column=1)

red_bull_label = Label(add_frame, text="Red Bull")
red_bull_label.grid(row=2, column=0)
red_bull_button = Button(add_frame, text="ADD")
red_bull_button.grid(row=2, column=1)

monster_label = Label(add_frame, text="Monster")
monster_label.grid(row=3, column=0)
monster_button = Button(add_frame, text="ADD")
monster_button.grid(row=3, column=1)

espresso_label = Label(add_frame, text="Espresso")
espresso_label.grid(row=4, column=0)
espresso_button = Button(add_frame, text="ADD")
espresso_button.grid(row=4, column=1)

root.mainloop()

# caffeine_list = [1400, 1400, 160, 880, 680, 1280, 1000, 1480, 80, 480]

# # print(sum(caffeine_list[-7:]) / 7)
# # print(caffeine_list[-7:])

# my_num = 1000

# for index in range(0, 11):
#     print(f"Day {index}: {my_num}")
#     my_num = my_num * 0.9 - 50