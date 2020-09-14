caffeine_list = [1400, 1400, 160, 880, 680, 1280, 1000, 1480, 80, 480]

# print(sum(caffeine_list[-7:]) / 7)
# print(caffeine_list[-7:])

my_num = 1000

for index in range(1, 10):
    my_num = my_num * 0.9 - 50
    print(f"Day {index}: {my_num}")