import matplotlib.pyplot as plt # เรียกใช้โดยตั้งชื่อเล่นว่า plt

# 1. เตรียมข้อมูล (Data Preparation)
# แกน X: วัน
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# แกน Y: ราคา (สมมติ)
prices = [3200000, 3150000, 3300000, 3450000, 3380000]

# 2. สั่งวาดกราฟ (Plotting)
print("กำลังวาดกราฟ... (หน้าต่างกราฟจะเด้งขึ้นมา)")
plt.plot(days, prices)

# 3. โชว์ผลงาน
plt.show()