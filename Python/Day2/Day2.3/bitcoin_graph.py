import requests
import matplotlib.pyplot as plt
from datetime import datetime  # <--- 1. เพิ่มตัวช่วยเรื่องเวลา

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=thb&days=7"
response = requests.get(url)
data = response.json()

raw_data = data['prices'] 

times = []
prices = []

for item in raw_data:
    # item[0] คือเวลา (หน่วย Millisecond)
    # item[1] คือราคา
    
    # <--- 2. แปลงเวลาตรงนี้ ---
    timestamp_ms = item[0] 
    # ต้องหาร 1000 เพราะ CoinGecko ให้มาเป็น "มิลลิวินาที" แต่ Python ใช้ "วินาที"
    date_obj = datetime.fromtimestamp(timestamp_ms / 1000) 
    
    times.append(date_obj) # เก็บแบบเป็นวันที่ (Object) เลย กราฟจะได้ฉลาด
    prices.append(item[1])

# --- วาดกราฟ ---
plt.figure(figsize=(10, 6)) # <--- ปรับขนาดกราฟให้กว้างขึ้นหน่อย (กว้าง 10 สูง 6)

plt.plot(times, prices, color='orange', label='BTC Price')

plt.title("Bitcoin Price History (Last 7 Days)")
plt.ylabel("Price (THB)")
plt.xlabel("Date & Time")
plt.grid(True)
plt.legend()

# <--- 3. จัดระเบียบแกน X ให้ตัวหนังสือเอียงๆ จะได้ไม่ทับกัน ---
plt.xticks(rotation=45) 
plt.tight_layout() # จัดขอบให้อัตโนมัติ

plt.show()