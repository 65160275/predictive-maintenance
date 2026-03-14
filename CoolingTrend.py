import matplotlib.pyplot as plt

def get_peak(file_name):

    time = []
    amp = []

    file = open(file_name)

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

    return max(amp)


# หา Peak vibration
jun = get_peak("dataset/A_Cooling Pump OAH 02_M1H_1480_Jun24.txt")
sep = get_peak("dataset/A_Cooling Pump OAH 02_M1H_1480_Sep24.txt")
oct = get_peak("dataset/A_Cooling Pump OAH 02_M1H_1480_Oct24.txt")

print("Jun:", jun)
print("Sep:", sep)
print("Oct:", oct)


# Trend graph
months = ["Jun", "Sep", "Oct"]
values = [jun, sep, oct]

plt.plot(months, values, marker='o')

plt.xlabel("Month")
plt.ylabel("Peak Vibration (G)")
plt.title("Cooling Pump Vibration Trend")

plt.grid(True)

plt.show()