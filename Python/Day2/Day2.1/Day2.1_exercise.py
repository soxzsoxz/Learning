import requests
import time

def get_bitcoin_price():
    """ดึงราคา Bitcoin ทั้ง THB และ USD ในครั้งเดียว"""
    # สังเกตตรง vs_currencies=thb,usd (ขอทีเดียว 2 หน่วย)
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=thb,usd"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            # --- จุดที่แก้: เจาะเข้าไปเอาข้อมูลให้ถูกชั้น ---
            # data คือ {'bitcoin': {'thb': 3xxxxxx, 'usd': 9xxxx}}
            price_thb = data['bitcoin']['thb']
            price_usd = data['bitcoin']['usd']
            
            # ส่งค่ากลับไป 2 ตัวพร้อมกัน (Tuple)
            return price_thb, price_usd
        else:
            print("Server Error:", response.status_code)
            return None, None
    except Exception as e:
        print(f"Internet Error: {e}")
        return None, None

# --- Main Loop ---
print("🚀 เริ่มต้นดึงราคา Bitcoin Real-time (กด Ctrl+C เพื่อหยุด)...")

while True:
    # รับค่า 2 ตัวที่ส่งกลับมา
    thb, usd = get_bitcoin_price()
    
    if thb and usd:
        # \033[92m คือรหัสสีเขียว (ให้ดูเท่ๆ), \033[0m คือล้างสี
        print(f"💰 BTC: \033[92m{thb:,.0f} THB\033[0m | \033[94m{usd:,.2f} USD\033[0m")
    else:
        print("❌ เกิดข้อผิดพลาด")
    
    time.sleep(5) # รอ 5 วินาที