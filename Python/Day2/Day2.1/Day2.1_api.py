import requests
import time # เอาไว้หน่วงเวลา

def get_price(coin_id):
    """ฟังก์ชันไปดึงราคาเหรียญ (หน่วยบาท)"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=thb"
    
    try:
        response = requests.get(url, timeout=10) # รอสูงสุด 10 วิ
        if response.status_code == 200:
            data = response.json()
            # data หน้าตาแบบนี้: {'bitcoin': {'thb': 3500000}}
            price = data[coin_id]['thb']
            return price
        else:
            print("Error connecting to server.")
            return None
    except Exception as e:
        print(f"Internet Error: {e}")
        return None

# --- Main Loop ---
while True:
    print("\n--- 💰 Crypto Price Checker 💰 ---")
    coin = input("ป้อนชื่อเหรียญ (เช่น bitcoin, ethereum, dogecoin) หรือพิมพ์ q เพื่อออก: ").lower()
    
    if coin == 'q':
        print("Goodbye!")
        break
        
    print(f"กำลังดึงราคา {coin}...")
    price = get_price(coin)
    
    if price:
        # จัดรูปแบบตัวเลขใส่ลูกน้ำ (Format Currency)
        print(f"✅ ราคาปัจจุบัน: {price:,.2f} THB")
    else:
        print("❌ ไม่พบเหรียญนี้ หรือระบบมีปัญหา")