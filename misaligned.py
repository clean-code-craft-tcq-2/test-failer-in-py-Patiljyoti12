
def print_color_map():
    all_color_pair_numbers=[]
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            all_color_pair_numbers.append(f'{i * 5 + j}')
    return len(major_colors) * len(minor_colors),all_color_pair_number


all_color_pair_number,result = print_color_map()
assert(result == 25)
assert('2' in all_color_pair_number[1])
print("All is well (maybe!)\n")
