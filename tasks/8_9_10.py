#  Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]

print(color_list[0] + " " + color_list[-1])

# Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)

print(f"The examinaton will start from : {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5
# Expected Result : 615
n = int(input())

print(3*n + n*10 + n*110)