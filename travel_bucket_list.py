import easygui

places_list = []

while len(places_list) != 5:
    places = easygui.enterbox("Enter the five places you want to visit, each separated by a comma only (no space).", "Favourite places")
    places_list = places.split(",")

    if len(places_list) != 5:
        easygui.msgbox(f"Sorry, you must enter exactly 5 places and you entered {len(places_list)} places.", f"{len(places_list)}/5 places")

for place in places_list:
    output = f"\n*  ".join(places_list)
easygui.msgbox("My bucket list:"
               f"\n\n* {output}", "Bucket list")
