colors = ("red", "green", "blue")

try:
    colors[0] = "yellow"
except:
    pass

print("Length:", len(colors))
print("red in tuple:", "red" in colors)
