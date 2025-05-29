#!/usr/bin/python3.10

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a HIGH priority task. Prioritize it soon!")
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a MEDIUM priority task with a deadline. Schedule time for it today.")
            else:
                print(f"Reminder: '{task}' is a MEDIUM priority task. Complete it this week.")
        case 'low':
            if time_bound == 'yes':
                print(f"Note: '{task}' is a LOW priority task but has a deadline. Fit it in if possible.")
            else:
                print(f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level. Please use high/medium/low.")

if __name__ == "__main__":
    daily_reminder()
