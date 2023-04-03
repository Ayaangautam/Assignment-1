import math

#sine of angles ranging from 0 to 345 in 15 increment
for i in range(0, 360, 15):
    # then print the sine and cosine of the angles
    print(i, '---', round(math.sin(i), 4), round(math.cos(i),4));
    