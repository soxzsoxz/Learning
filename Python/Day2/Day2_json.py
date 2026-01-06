import json
import os # เอาไว้เช็คว่ามีไฟล์อยู่จริงไหม

inventory = []

def showmenu():
    print("\n--- Inventory Management ---")
    print(f"1. Show Items (ดูสินค้า)")
    print(f"2. Add Item (เพิ่มสินค้า)")
    print(f"3. Remove Item (ลบสินค้า)")
    print(f"4.Exit (ออกจากโปรแกรม)")
    print("----------------------------")
    
# 1. หาที่อยู่ของไฟล์โค้ดปัจจุบัน (Day2)
current_folder = os.path.dirname(os.path.abspath(__file__))

# 2. เอามาต่อกับชื่อไฟล์ json
DB_FILE = os.path.join(current_folder, "inventory.json")

def save_data():
    """บันทึกข้อมูลจากตัวแปร inventory ลงไฟล์"""
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=4, ensure_ascii=False)
        print("💾 Saved data successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")

def load_data():
    """โหลดข้อมูลจากไฟล์กลับเข้าตัวแปร inventory"""
    global inventory # บอกว่าจะแก้ตัวแปร inventory ที่อยู่ข้างนอก
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                inventory = json.load(f)
            print(f"📂 Loaded {len(inventory)} items from file.")
        except Exception as e:
            print(f"Error loading data: {e}")
            inventory = [] # ถ้าโหลดพัง ให้เริ่มใหม่ด้วยลิสต์ว่าง
    else:
        print("⚠️ No save file found. Starting with empty inventory.")
        inventory = []

def show_items():
    for item in inventory:
        print(f" - {item['name']} (จำนวน: {item['qty']})")

def add_item():
    print("--- Add New Item ---")
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
        
    found = False
        
    for item in inventory:
    # --- แก้จุดที่ 1: แปลงเป็นตัวเล็กทั้งคู่ก่อนเทียบ ---
    # ไม่ว่าจะพิมพ์ Coke, coke, COKE ก็จะกลายเป็น "coke" == "coke"
        if item["name"].lower() == name.lower():
            item["qty"] += qty
            found = True
            print(f"Updated {item['name']}: total is now {item['qty']}")
            break
        
    if not found:
        # --- แถมให้ จุดที่ 2: บันทึกให้สวยงาม ---
        # แปลงให้ตัวแรกเป็นพิมพ์ใหญ่เสมอ (เช่น "coke" -> "Coke")
        pretty_name = name.capitalize() 
            
        new_item = {"name": pretty_name, "qty": qty}
        inventory.append(new_item)
        print(f"Added new item: {pretty_name}")
    
def remove_item():
    print("--- Remove Item (เบิกของ) ---")
    name = input("Enter item name to remove: ")
        
    for item in inventory:
        if item["name"].lower() == name.lower():
            # 1. เจอของแล้ว ถามต่อว่าจะเบิกเท่าไหร่
            qty_to_remove = int(input(f"Found {item['name']} ({item['qty']}). Amount to remove: "))
                
            # 2. เช็คสต็อก (Validation)
            if qty_to_remove <= item["qty"]:
                item["qty"] -= qty_to_remove # ลบจำนวนออก
                print(f"Success! Removed {qty_to_remove}. Remaining: {item['qty']}")
                    
                # (Optional) ลูกเล่น: ถ้าเหลือ 0 ให้ลบ key ทิ้งไปเลย
                if item["qty"] == 0:
                    inventory.remove(item)
                    print(f"Stock is empty. Removed {item['name']} from list.")
                else:
                    print(f"Error: Not enough stock! (Have only {item['qty']})")
                
                break # เจอแล้ว หยุดลูป
        else:
            print("Item not found (ไม่พบสินค้า).")
            
# --- Main Program ---

# 1. โหลดข้อมูลเก่าก่อนเริ่มโปรแกรม
load_data() 

while True:
    showmenu()
    choice = input("Select : ")
    
    if choice == "1":
        show_items()
    elif choice == "2":
        add_item()
        save_data() # <--- บันทึกทันทีที่เพิ่มของ
    elif choice == "3":
        remove_item()
        save_data() # <--- บันทึกทันทีที่ลบของ
    elif choice == "4":
        print(f"Bye!")
        break