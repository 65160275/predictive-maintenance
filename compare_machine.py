import matplotlib.pyplot as plt

months = ["Jun", "Sep", "Oct"]

# ข้อมูล vibration
jockey = [1.244, 1.531, 1.699]
cooling = [1.17, 1.20, 1.142]
compressor = [0.966, 0.786, 0.916]

# หา peak vibration
machines_peak = {
    "Jockey Pump": max(jockey),
    "Cooling Pump": max(cooling),
    "Compressor Motor": max(compressor)
}

highest_machine = max(machines_peak, key=machines_peak.get)

# หาเครื่องที่ stable
machines_range = {
    "Jockey Pump": max(jockey) - min(jockey),
    "Cooling Pump": max(cooling) - min(cooling),
    "Compressor Motor": max(compressor) - min(compressor)
}

stable_machine = min(machines_range, key=machines_range.get)

# ====== ส่วนที่คุณส่งมา ======

print("\n================ MACHINE VIBRATION DATA ================\n")

print(f"{'Machine':20}{'Jun':8}{'Sep':8}{'Oct':8}")
print("--------------------------------------------------------")

print(f"{'Jockey Pump':20}{jockey[0]:<8}{jockey[1]:<8}{jockey[2]:<8}")
print(f"{'Cooling Pump':20}{cooling[0]:<8}{cooling[1]:<8}{cooling[2]:<8}")
print(f"{'Compressor Motor':20}{compressor[0]:<8}{compressor[1]:<8}{compressor[2]:<8}")

print("\n===================== ANALYSIS =========================\n")

print("⚠ Machine at Risk      :", highest_machine)
print("✓ Stable Machine       :", stable_machine)

print("\n================== RECOMMENDATION ======================\n")

print("Inspect Machine        :", highest_machine)

print("\n==================== MACHINE STATUS ====================\n")

for machine in machines_peak:
    if machine == highest_machine:
        status = "WARNING"
    else:
        status = "NORMAL"

    print(f"{machine:22}: {status}")

# ====== กราฟ ======

plt.plot(months, jockey, marker='o', label="Jockey Pump")
plt.plot(months, cooling, marker='o', label="Cooling Pump")
plt.plot(months, compressor, marker='o', label="Compressor Motor")

plt.xlabel("Month")
plt.ylabel("Peak Vibration (G)")
plt.title("Machine Vibration Comparison")

plt.legend()
plt.grid(True)

plt.show()