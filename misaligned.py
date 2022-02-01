major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
color_code_manual=[]

# getting pair number by passing major and minor color
def get_pair_no_from_colors(major_color,minor_color):
    major_index = major_colors.index(major_color)
    minor_index = minor_colors.index(minor_color)
    return major_index * len(minor_colors) + minor_index + 1

def print_color_map(major_colors,minor_colors):   
    for i, major_col in enumerate(major_colors):
        for j, minor_col in enumerate(minor_colors):
         color_code_manual.append([i * 5 + j + 1 ,major_col,minor_col])   
    return color_code_manual
            
def format_color_code_manual(pair_number,major_color,minor_color):
    return f'{pair_number}|{major_color}|{minor_color}'
    

        
result=print_color_map(major_colors,minor_colors)
assert (get_pair_no_from_colors('White','Blue')==1)
assert (get_pair_no_from_colors('White','Orange')==2)
assert (result[0]==[1,'White' ,'Blue'])
assert ('White' in result[0])
assert ('Blue' in result[0])
assert (result[24]==[25, 'Violet', 'Slate'])
print("All is well (maybe!)\n")

