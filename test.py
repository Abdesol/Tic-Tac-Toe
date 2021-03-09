from screeninfo import get_monitors

resolution = str(get_monitors()[0]).split(" ")

print(str(get_monitors()[1]).split(" "))
