est_time = int(input("Estimated time : "))
recovered_time = est_time * 2.5
wk = est_time // 7

course = [0, 0, 0]  # physic, weight, fitness
physic, weight, fitness = course
for i in range(wk):
    print(f"Week{i+1}")
    physic += int(input("Physical therapy : "))
    weight += int(input("Weight training : "))
    fitness += int(input("Fitness training : "))

if physic >= recovered_time and weight >= recovered_time and fitness >= recovered_time:
    print("Buzzy has recovered in time.")
else:
    print("Buzzy has not recovered in time.")
