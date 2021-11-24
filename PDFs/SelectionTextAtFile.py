# lun 22 nov 2021 19:31:17 CST

filename = "/home/alfredo/Alfredo's Files/AutoKey/note.txt"
notecontent = clipboard.get_selection()

with open(filename, "a") as file_object:
    file_object.write(notecontent+"\n\n")

