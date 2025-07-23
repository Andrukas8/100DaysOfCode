def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    else:
        return (f_name + " " + l_name).title()


print(format_name("vaLerA", "mAgniToFonchIk"))
print(format_name("", "mAgniToFonchIk"))
