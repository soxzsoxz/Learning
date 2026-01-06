import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
prices = [3200000, 3150000, 3300000, 3450000, 3380000]

# --- ส่วนตกแต่ง ---
# plot(แกนX, แกนY, marker='o' คือจุดกลมๆ, color='green' สีเขียว, linestyle='--' เส้นประ)
plt.plot(days, prices, marker='o', color='green', linestyle='--', label='BTC Price')

plt.title("Bitcoin Price History (Simulated)") # ชื่อกราฟ
plt.xlabel("Day")          # ชื่อแกน X
plt.ylabel("Price (THB)")  # ชื่อแกน Y
plt.grid(True)             # ตีตารางตารางหมากรุก (Grid) ให้อ่านง่าย
plt.legend()               # โชว์ป้ายกำกับเส้น (Label)

plt.show()