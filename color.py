color = input("enter the colors seperate by comas:")
color_list=color.split(',')
print(color_list)

print("first color:", color_list[0])
print("last color:",color_list[-1])
color_list2 = ["red", "orange","black","white"]


print("color-list1 not contained in color-list2 are : ")
diff = list(set(color_list) - set(color_list2))
print(diff)
color_int_list=[]
for color in color_list:
    # for color in color_list:
    color_int_list.append(len(color))
    print(f" list of interger corresponding to each color:{color_int_list}")
