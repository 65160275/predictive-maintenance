import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

time = []
amp = []

file = open("../dataset/A_Cooling Pump OAH 02_M1H_1480_Sep24.txt")

for line in file:
    parts = line.split()

    try:
        numbers = [float(x) for x in parts]
    except:
        continue

    for i in range(0, len(numbers), 2):
        if i+1 < len(numbers):
            time.append(numbers[i])
            amp.append(numbers[i+1])

plt.plot(time, amp)

plt.xlabel("Time (ms)")
plt.ylabel("Amplitude (G)")
plt.title("Cooling Pump Vibration")

plt.grid(True)

print("Peak vibration:", max(amp))
print("Min vibration:", min(amp))

plt.show()