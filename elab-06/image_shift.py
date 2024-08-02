h = int(input("Enter horizontal shift size: "))
v = int(input("Enter vertical shift size: "))
print("Enter image:")
image = []

while 1:
    img = input()
    if img == "-1":
        break
    image.append(img)

newImage = []
width = len(image[0])
height = len(image)

for i in range(v):
    newImage.append("0" * width)

for i in range(height - v):
    newImage.append(image[i])

image = newImage.copy()
newImage = []

for i in range(height):
    newImage.append("0" * h + image[i][: width - h])

print("After shift:")
for x in newImage:
    print(x)
