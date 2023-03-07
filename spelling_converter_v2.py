import easygui

repeat = "Yes"

# main loop
while repeat == "Yes":
    word = easygui.enterbox("Write a nz english word with an 'our', 'ise' or 'yse' in it: ")
    word_list = list(word)

    # Checking the string to see if the options are in it
    # and converting it to the american spelling
    if "our" in word:
        word_list.remove("u")
        easygui.msgbox(f"The american spelling of {word} is {''.join(word_list)}")
    elif "ise" in word or "yse" in word:
        amer_word = word.replace("s", "z")
        easygui.msgbox(f"The american spelling of {word} is {amer_word}")
    else:
        easygui.msgbox(f"No change in spelling for {word}")

    # repeat?
    repeat = easygui.buttonbox("Do you want to convert another word to US english?", choices=["Yes", "No"])

easygui.msgbox("Have a good day")
