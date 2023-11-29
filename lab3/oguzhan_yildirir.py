# # TASK 1
# organisation = input("Enter a organisation name: ")

# words = organisation.split(" ")

# for word in words:
#     print(word[0])

# # TASK 2
# def day_of_week(year, month, day):
#     days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    
#     # Mike & Keith Algorithm
#     if month < 3:
#         month += 12
#         year -= 1

#     k = year % 100
#     j = year // 100

#     day_index = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7

#     return days[day_index]

# day = int(input("Day (1-31): "))
# month = int(input("Month (1-12): "))
# year = int(input("Year: "))


# result = day_of_week(year, month, day)
# print("The day of the week for", month, "/", day, "/", year, ":", result)

# # TASK 3
# import sys

# print("Please enter numbers seperated by space")
# userInput = input()

# numbers = userInput.split(" ")

# uniqueNumbers = []

# for number in numbers:
#     try:
#         intNumber = int(number)
#         if intNumber not in uniqueNumbers:
#             uniqueNumbers.append(intNumber)
#     except:
#         print("bad data")
#         sys.exit()
    
# print(uniqueNumbers)