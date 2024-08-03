import colorgram

rgb_color = []
colors = colorgram.extract('C:\\Users\\Asus\\Desktop\\tomato2.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.r
    new_color = (r, g, b)
    rgb_color.append(new_color)
print(rgb_color)
