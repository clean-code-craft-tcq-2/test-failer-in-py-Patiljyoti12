major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
color_code_manual=[]

def get_pair_number_from_colors(major_colors,minor_colors):   
    for i, major_col in enumerate(major_colors):
        for j, minor_col in enumerate(minor_colors):
         color_code_manual.append([i * 5 + j + 1 ,major_col,minor_col])   
    return color_code_manual
            
    
    

        
result=get_pair_number_from_colors(major_colors,minor_colors)
assert (result[0]==[1,'White' ,'Blue'])
assert ('White' in color_code_manual[0])
assert ('Blue' in color_code_manual[0])
assert (result[24]==[25, 'Violet', 'Slate'])
print("All is well (maybe!)\n")

