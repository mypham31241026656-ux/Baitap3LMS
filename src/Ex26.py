# 26. Write a Python program to check whether two lists are circularly identical.
#giống nhau theo vòng tròn

def check_circular(list1, list2):
    if len(list1) != len(list2):
        print("Two list are not the same in circle")
    else:
        doubled = list1*2

        found = False
        for i in range (len(list1)):
            if doubled[i:i+len(list2)]==list2:
                found = True
                break
    if found:
        print("Two lists are circular identical")
    else:
        print("Two lists are not circular identical")

list1 = [6,7,8,9]
list2 = [8,9,6,7]
check_circular(list1, list2)