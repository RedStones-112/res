import matplotlib.pyplot as plt
A = 20
speed = 0
a = 5
min_a = 0
max_a = 20
goal = 420
tick = 0.1
t = 0
stop_time = 0
def stop_range(speed,a):

    time = speed/a
    stop_distance = 0
    i = 0
    while i != speed:
        stop_distance += speed
        i+=0.5
    return stop_distance

while A < goal:
    t += tick
    if goal-A <= stop_range(speed,a):
        a = -5
    else:
        a = 5
    speed += a*tick
    if speed > max_a:
        speed = max_a
    elif speed < min_a:
        speed = min_a
    else:
        pass
    A = A+speed

plt.plot()
plt.show()