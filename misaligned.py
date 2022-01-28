
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
 
 
color_code_manual=[]
def print_color_map(major_colors,minor_colors):   
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            color_code_manual.append(f'{i * 5 + j}| {major} | {minor}')
            length_major_minor_colors(major_colors,minor_colors)
    return color_code_manual
            
    
    
def length_major_minor_colors(major_colors,minor_colors):  
        return len(major_colors) * len(minor_colors)
        
result=print_color_map(major_colors,minor_colors)
assert (result[0]=='1| White | Blue')
assert (result[24]=='25| Violet | Slate')
print("All is well (maybe!)\n")

