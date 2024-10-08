# import math

# type: ignore # print(dir(math))
# print(math.sqrt(16))
# print(math.ceil(0.9))
# print(math.pi)
# print(math.sin(0))


# import datetime
# Get the current date and time
# current_date = datetime.datetime.now()
# Format the current date as a string in the format YYYY-MM-DD
# string_date = current_date.strftime("%Y-%m-%d")
# print(string_date)


# import datetime
# Example date string
# date_string = "2024-07-24"
# Parsing the date string with the specified format
# x = datetime.datetime.strptime(date_string, "%Y-%m-%d")
# print(x)

# from datetime import datetime

# current_date = datetime.now()
# specific_date = datetime(2023, 12, 24)

# difference = current_date - specific_date

# print("Current date:", current_date)
# print("Specific date:", specific_date)
# print("Difference in days:", difference.days)

# from datetime import datetime, timedelta

# current_date = datetime.now()
# days_to_subtract = 10

# new_date = current_date - timedelta(days=days_to_subtract)
# print("Current date:", current_date)
# print("New date:", new_date)

# from datetime import datetime, timedelta

# current_date = datetime.now()
# hours_to_subtract = 10

# new_date = current_date - timedelta(hours=hours_to_subtract)

# print("Current date and time:", current_date)
# print("New date and time after subtracting 10 hours:", new_date)


# import datetime

# jobs = [
#     {'title': 'python developer', 'salary': 1000, 'exp_date': '2021-03-01'},
#     {'title': 'java developer', 'salary': 2000, 'exp_date': '2024-08-02'},
#     {'title': 'c# developer', 'salary': 3000, 'exp_date': '2022-06-03'},
#     {'title': 'c++ developer', 'salary': 4000, 'exp_date': '2025-07-04'},
# ]

# current_date = datetime.datetime.now()

# def expired():
#     for job in jobs:
#         exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#         if exp_date < current_date:
#             print(f"Job: {job['title']}, exp_time: {job['exp_date']}")

# def non_expired():
#     for job in jobs:
#         exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#         if exp_date > current_date:
#             print(f"Job: {job['title']}, exp_time: {job['exp_date']}")

# def main():
#     print("Expired Jobs:")
#     expired()
#     print("Non-Expired Jobs:")
#     non_expired()

# main()



# products []
# 0-20 - Warning
# product < 6: new
# product 6 - 12 : moderate
# product > 2 : old

# import datetime

# fruits = [
#     {'Fruits': 'Apple', 'price': 100, 'date': '2024-01-01'},
#     {'Fruits': 'Banana', 'price': 200, 'date': '2021-08-02'},
#     {'Fruits': 'Mango', 'price': 300, 'date': '2024-07-22'},
#     {'Fruits': 'Orange', 'price': 400, 'date': '2022-02-12'},
# ]

# current_date = datetime.datetime.now()

# for fruit in fruits:
#     date = datetime.datetime.strptime(fruit['date'], "%Y-%m-%d")
#     duration = current_date - date
#     days = duration.days
#     months = duration.days / 30
#     if days < 20:
#         print(f"{fruit['Fruits']}: Warning your product is reaching 20 days.")
#     elif months < 6:
#         print(f"{fruit['Fruits']}: Your product is new.")
#     elif months < 12:
#         print(f"{fruit['Fruits']}: Your product is mild.")
#     elif months > 24:
#         print(f"{fruit['Fruits']}: Your product is old.")
#     else:
#         print(f"{fruit['Fruits']}: Your product is not valid.")


