# with open(r'C:\Users\р\OneDrive\Desktop\new_text.txt') as new_text:
#     pass

colors_list = []
with open(r'C:\\Users\\р\\OneDrive\\Desktop\\new_text.txt') as new_text:
    for color in new_text:
        colors_list.append(color.strip('\n'))
        # '.strip' - обрезает символ указанный в параметре для строк
print(colors_list)
