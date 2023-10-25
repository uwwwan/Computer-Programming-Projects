import calendar
from colorama import Fore, Style


def display_calendar(yy, mm, subject_name, subject_schedule, highlighted_days):
    cal = calendar.monthcalendar(yy, mm)
    print(calendar.month_name[mm], yy)
    print("Mon Tue Wed Thu Fri Sat Sun")

    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end="  ")
            elif calendar.weekday(yy, mm, day) in highlighted_days:
                print(f"{Fore.BLUE}{day:2}{Style.RESET_ALL}", end="  ")
            else:
                print(f"{day:2}", end="  ")

    print(f"{Fore.LIGHTYELLOW_EX}{subject_name}{Style.RESET_ALL}\n{subject_schedule}")


while True:
    print("==========================================")
    print("""       ✨✨WELCOME TO OUR CODE✨✨
              ✨✨GROUP 2✨✨""")
    print("==========================================")
    bb = input("Enter a block: ")

    if bb == "2":
        yy = int(input("Enter a year: "))
        mm = int(input("Enter a month: "))
        subject_code = input("Enter a subject: ")
        print("==========================================")
        print("""       ✨✨WELCOME TO OUR CODE✨✨
              ✨✨GROUP 2✨✨""")
        print("==========================================")

        if subject_code.lower() in ["ite366", "ite-366"]:
            subject_name = "ITE 366 - Introduction to Computing (Including IT Fundamentals)"
            subject_schedule = "Date: Monday, Friday\nTime: 09:00 AM - 05:00 PM"
            highlighted_days = [0]
            display_calendar(yy, mm, subject_name, subject_schedule, highlighted_days)

        elif subject_code.lower() in ["ite260", "ite-260"]:
            subject_name = "ITE 260 - Computer Programming 1"
            subject_schedule = "Date: Tuesday, Friday\nTime: 08:30 AM - 04:00 PM"
            highlighted_days = [1, 4]
            display_calendar(yy, mm, subject_name, subject_schedule, highlighted_days)

        elif subject_code.lower() in ["ped030", "ped-030"]:
            subject_name = "PED 030 - Physical Activities Toward Health and Fitness (PATHFit 1): Movement Competency Training"
            subject_schedule = "Date: Saturday\nTime: 07:00 AM - 09:00 AM"
            highlighted_days = [5]
            display_calendar(yy, mm, subject_name, subject_schedule, highlighted_days)

        elif subject_code.lower() in ["gen002", "gen-002"]:
            subject_name = "GEN 002 - Understanding the Self"
            subject_schedule = "Date: Wednesday, Saturday\nTime: 09:00 AM - 04:00 PM"
            highlighted_days = [2, 5]
            display_calendar(yy, mm, subject_name, subject_schedule, highlighted_days)

        elif subject_code.lower() in ["nst021", "nst-021"]:
            subject_name = "NST 021 - National Service Training Program 1"
            subject_schedule = "Date: Monday, Thursday\nTime: 04:00 PM - 05:30 PM"""
            highlighted_days = [0, 3]
            display_calendar(yy, mm, subject_name, subject_schedule, highlighted_days)



        else:
            print(f"{Fore.RED}Subject not found{Style.RESET_ALL}")
    elif bb != "2":
        print(f"{Fore.RED}Invalid Block{Style.RESET_ALL}")

    ii = input("Do you want to continue? Yes / No: ").lower()

    if ii not in ["yes", "y"]:
        break