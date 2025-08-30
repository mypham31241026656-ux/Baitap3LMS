
# 32. Write a Python program to check whether a list contains a sublist.

def check_sublist(main_list, sub_list):
        found = False
        for i in range(len(main_list)-len(sub_list)+1):
            if main_list[i:i+len(sub_list)] == sub_list:
                found = True
                break

        if found:
            print("The sublist is in the list", sub_list)
        else:
            print("The sublist is not in the list", sub_list)

main_list = [4,9,3,6,8,3,4,9,8,11,1,1]
sub_list = [9,3,6]
check_sublist(main_list, sub_list)
