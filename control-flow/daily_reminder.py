#!/usr/bin/python3.10

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # ===== Match-Case Section (Explicit for Tests) =====
    match priority:
        case 'high':
            if time_bound == 'yes':
                reminder = f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!"
            else:
                reminder = f"Reminder: '{task}' is a HIGH priority task. Prioritize it soon!"
        case 'medium':
            if time_bound == 'yes':
                reminder = f"Reminder: '{task}' is a MEDIUM priority task with a deadline. Schedule time for it today."
            else:
                reminder = f"Reminder: '{task}' is a MEDIUM priority task. Complete it this week."
        case 'low':
            if time_bound == 'yes':
                reminder = f"Note: '{task}' is a LOW priority task but has a deadline. Fit it in if possible."
            else:
                reminder = f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time."
        case _:
            reminder = "Invalid priority level. Please use high/medium/low."
    # ===== End Match-Case Section =====

    print("\n" + reminder)

if __name__ == "__main__":
    daily_reminder()
