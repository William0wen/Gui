import easygui

word = easygui.enterbox("Write a nz english word with an 'ou' in it: ")
word_list = list(word)
word_list.remove("u")
easygui.msgbox(f"The american spelling of {word} is {''.join(word_list)}")
