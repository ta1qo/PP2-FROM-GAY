from math import tan, radians

n, l = int(input("Input number of sides: ")), int(input("Input the length of a side: "))
perimeter = n * l
alpha = tan(radians(180/n))   # radians Преобразует угол x, заданный в градусах, в радианы
apothem = l / (2*alpha)
Area = perimeter*apothem / 2
print('The area of the polygon is:', int(Area))
