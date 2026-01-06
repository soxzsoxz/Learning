import requests
import pandas as pd
import matplotlib.pyplot as plt # เรียกมาเพื่อใช้คำสั่ง show()

url = "https://api.coingecko.com/api/v3/coins/tether-gold/market_chart?vs_currency=thb&days=90" # ขอ 30 วันเลย
response = requests.get(url)
data = response.json()
raw_data = data['prices']

df = pd.DataFrame(raw_data, columns=['Timestamp', 'Price'])

df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')

min_price = df['Price'].min()
print(f"ราคาต่ำสุด: {min_price:,.2f} บาท")

df.set_index('Date', inplace=True)

df['Price'].plot(color='red', figsize=(10, 5), title='Gold Price (90 Days)')
plt.ylabel("Price (THB)")
plt.grid()
plt.show()