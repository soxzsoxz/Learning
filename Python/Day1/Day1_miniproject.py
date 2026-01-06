inventory = [{"name": "Coke", "qty": 10}, {"name": "Lays", "qty": 5}]

while True:
    print("\n--- Inventory Management ---")
    print(f"1. Show Items (ดูสินค้า)")
    print(f"2. Add Item (เพิ่มสินค้า)")
    print(f"3. Remove Item (ลบสินค้า)")
    print(f"4.Exit (ออกจากโปรแกรม)")
    print("----------------------------")
    
    order = input("Please select an option (กรุณาเลือกตัวเลือก): ")

    if order == "1":
        for item in inventory:
            print(f" - {item['name']} (จำนวน: {item['qty']})")
    elif order == "2":
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
    elif order == "3":
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
    elif order == "4":
        print("Exiting program (ออกจากโปรแกรม)...")
        break
    else:
        print("Invalid option (ตัวเลือกไม่ถูกต้อง).")