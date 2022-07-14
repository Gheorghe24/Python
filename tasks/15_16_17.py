# 15. Write a Python program to get the volume of a sphere with radius 6.

volume = 6 ** 3
print(f"Volume of sphere with radius 6 is equal to {volume}")

# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. 

n = int(input())
if n > 17 :
    print(abs(n - 17) * 2)
else :
    print(abs(n - 17))

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000. 

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

