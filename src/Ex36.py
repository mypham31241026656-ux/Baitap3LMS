# 36. Write a Python program to get a variable with an identification number or
# string. viết chương trình Python để lấy số định danh (ID) hoặc chuỗi của một biến.

x="Phạm Đào Trà My"
var_id = id(x)
print("Số định danh của biến x: ", var_id)
id_str = str(var_id)
print("ID dưới dạng chuỗi: ", id_str)
print("Kiểu dữ liệu của biến x: ", type(x))
