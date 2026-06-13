weather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in weather:
    if i == 0:
        sunny += 1
    else:
        rainy += 1
    
    if sunny > rainy:
        print("The weather is sunny")
    elif rainy > sunny:
        print("The weather is rainy")
    else:
        print("The weather is neither sunny nor rainy")