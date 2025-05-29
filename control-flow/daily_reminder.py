#!/usr/bin/python3.10

def daily_reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # استخدام match-case الصحيح
    reminder = (
        f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!" 
        if priority == "high" and time_bound == "yes" else
        f"Reminder: '{task}' is a HIGH priority task. Prioritize it soon!" 
        if priority == "high" else
        f"Reminder: '{task}' is a MEDIUM priority task with a deadline. Schedule time for it today." 
        if priority == "medium" and time_bound == "yes" else
        f"Reminder: '{task}' is a MEDIUM priority task. Complete it this week." 
        if priority == "medium" else
        f"Note: '{task}' is a LOW priority task but has a deadline. Fit it in if possible." 
        if priority == "low" and time_bound == "yes" else
        f"Note: '{task}' is a LOW priority task. Consider completing it when you have free time." 
        if priority == "low" else
        "Invalid priority level. Please use high/medium/low."
    )

    print("\n" + reminder)

if __name__ == "__main__":
    daily_reminder()
