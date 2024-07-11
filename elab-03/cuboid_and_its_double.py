def compute_rectangle_area(first_side, second_side):
    return first_side * second_side


def compute_surface_area(width, height, length):
    return width * height * 2 + width * length * 2 + height * length * 2


def compute_volume(w, l, h):
    return w * l * h


w = float(input("Enter width: "))
l = float(input("Enter length: "))
h = float(input("Enter height: "))
print(f"For [{w:.2f} x {l:.2f} x {h:.2f}] cuboid:")
print(f"Surface area = {compute_surface_area(w,h,l):.3f}")
print(f"Volume = {compute_volume(w,h,l):.3f}")

w *= 2
l *= 2
h *= 2

print("")
print("After doubling each side,")
print(f"For [{w:.2f} x {l:.2f} x {h:.2f}] cuboid:")
print(f"Surface area = {compute_surface_area(w,h,l):.3f}")
print(f"Volume = {compute_volume(w,h,l):.3f}")
