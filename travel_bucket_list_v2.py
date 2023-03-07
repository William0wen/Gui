import easygui

# pre-setting variables
places_list_ = []
change_places = []
place_to_remove = ""
choice = "No"
repeat = "Yes"

# Loop to gather starting info
while len(places_list_) != 5:
    # enter five places
    places = easygui.enterbox("Enter the five places you want to visit"
                              "\neach separated by a comma only (no space)", "Favourite places")
    # convert string into a list
    places_list_ = places.split(",")
    if len(places_list_) != 5:
        easygui.msgbox(f"Sorry, you must enter exactly 5 places and you entered {len(places_list_)} places", f"{len(places_list_)}/5 places")

# Main loop
while choice == "No":
    repeat = "Yes"
    output = "\n*  ".join(places_list_)
    # print list
    easygui.msgbox("My bucket list:"
                   f"\n\n* {output}", "Bucket list")

    choice = easygui.buttonbox("Do you want to change any of the places?", choices=["Yes", "No"])
    if choice == "No":
        easygui.msgbox("Ok.")
    else:
        while repeat == "Yes":
            # replace one string with another
            change = easygui.enterbox("Enter the name of the place you want to change followed by the new place"
                                      "\neach separated by a comma only (no space)", "Change Place")
            change_places = change.split(",")
            place_to_remove = change_places[0]
            new_place = change_places[1]

            if place_to_remove not in places_list_:
                easygui.msgbox("The place you want to remove is not in your list.")
            else:
                index = places_list_.index(place_to_remove)
                places_list_[index] = new_place
                repeat = ""
                choice = "No"
