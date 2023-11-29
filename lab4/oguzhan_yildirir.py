# # TASK 1
# while True:
#     print("---------------")
#     print("BMI CALCULATOR")
#     print("---------------")
#     try:
#         height = float(input("Please enter height in meters: "))
#         weight = float(input("Please enter weight in kilograms: "))
#     except:
#         print("Please enter valid weight and height")
#         pass
# 
#     bmi = weight / height ** 2
# 
#     print("\nYour BMI: ", bmi)
# 
#     if bmi < 16.00:
#         print("Starvation")
#     elif bmi >= 16.00 and bmi <= 16.99:
#         print("Emeciation")
#     elif bmi >= 17.00 and bmi <= 18.49:
#         print("Underweight")
#     elif bmi >= 18.50 and bmi <= 24.99:
#         print("Correct weight")
#     elif bmi >= 25.00 and bmi <= 29.99:
#         print("Overweight")
#     elif bmi >= 30.00 and bmi <= 34.99:
#         print("First degree obesity")
#     elif bmi >= 35.00 and bmi <= 39.99:
#         print("Second degree obesity (clinical)")
#     else:
#         print("Third degree obesity (extreme)")
# 
#     ideal_min = 18.5 * height ** 2
#     ideal_max = 24.99 * height ** 2
# 
#     print("Min ideal kg: ", ideal_min)
#     print("Max ideal kg: ", ideal_max)

# # TASK 2
# while True:
#     print("-------------")
#     print("Exponantitaion")
#     print("-------------")
#
#     try:
#         x = int(input("X: "))
#         y = int(input("Y: "))
#         if (x == 0 and y == 0):
#             print("Both of values can't be 0!")
#             pass
#     except:
#         print("Please enter valid values!")
#         pass
#
#     result = 1
#
#     for n in range(1, y+1):
#         result *= x
#
#     print(x, "^", y, "=", result)