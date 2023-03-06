import easygui

tech_days = easygui.enterbox("Enter the days you used technology with a space between each one.").lower()
days_list = len(tech_days.split())
if days_list <= 3:
    easygui.msgbox(f"You had {7-days_list} tech free days.", "Goal achieved")

else:
    easygui.msgbox(f"You had {7-days_list} tech free days.", "Goal not achieved")
