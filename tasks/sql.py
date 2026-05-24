import sqlite3

db = sqlite3.connect("applciton.db")
cr = db.cursor()

# تفعيل الجدول تلقائياً للتأكد من وجوده
cr.execute("""CREATE TABLE IF NOT EXISTS gym(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    emill TEXT,
    age INTEGER NOT NULL
)""")

the_massge = """
what do you want ?
"S"=>show all skills
"A"=>add new skill
"D"=>delete A skill
"U"=>update skill progress
"Q"=>Quit App
choose option : """

def show_skill():
    cr.execute("SELECT * FROM gym")
    data = cr.fetchall()
    if len(data) > 0:
        for d in data:
            # تم إزالة حرف الـ s الزائد ليكون تنسيق الطباعة نظيفاً
            print(f"user_id = {d[0]} , name = {d[1]} , emiil = {d[2]} , age = {d[3]}")
    else:
        print("Error: Please enter data")

def add_skill():
    sk = input("enter your name please : ").strip().capitalize()
    em = input("and your meill please : ").strip()
    try:
        ag = int(input("and your age: ").strip())
    except ValueError:
        print("❌ Error: Age must be a number!")
        return
    cr.execute("INSERT INTO gym (name,emill,age) VALUES (?, ?, ?)", (sk, em, ag))
    print("thank you, added successfully")

def delete_skill():
    cr.execute("SELECT user_id, name FROM gym")
    data = cr.fetchall()    
    if len(data) == 0:
        print("📭 The table is completely empty!")
        return 
    for d in data:
        print(f"user_id => '{d[0]}' ", end=" ")
        print(f"name => '{d[1]}'")
    try:
        sk = int(input("delete client from user_id : ").strip())
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        return 
    
    existing_ids = [x[0] for x in data]
    if sk not in existing_ids:
        print(f"❌ Error: User ID {sk} is not found!")
    else:
        cr.execute("DELETE FROM gym WHERE user_id = ?", (sk,))
        print(f"🗑️ Client with ID {sk} deleted successfully!")

def update_skill():
    cr.execute("SELECT user_id FROM gym")
    data = cr.fetchall()
    if len(data) == 0:
        print("📭 The table is completely empty! No data to update.")
        return
    try:
        user_id = int(input("Enter the user_id you want to update: ").strip())
    except ValueError:
        print("❌ Error: Please enter a valid number")
        return
    ex = [x[0] for x in data]
    if user_id not in ex:
        print(f"❌ Error: User ID {user_id} is not found!")
        return
    sk = input("write your name please : ").strip().capitalize()
    em = input("write your meill please : ").strip()
    try:
        ag = int(input("write your age: ").strip())
    except ValueError:
        print("❌ Error: Age must be a number!")
        return
    cr.execute("UPDATE gym SET name=?, emill=?, age=? WHERE user_id=? ", (sk, em, ag, user_id))
    print("thank you, updated successfully")

commands_list = ['s', 'a', 'd', 'u', 'q']

while True:
    user_input = input(the_massge).strip().lower()
    if user_input in commands_list:
        print(f"cominds found {user_input}")
        
        if user_input == "s":
            show_skill()
            # شيلنا الـ commit هنا لأن الـ SELECT مش بيغير في الداتا
        elif user_input == "a":
            add_skill()
            db.commit()
        elif user_input == "d":
            delete_skill()
            db.commit()
        elif user_input == "u":
            update_skill()
            db.commit()
        else:
            print("app is close")
            db.close()
            break
    else:
        print(f"this comind {user_input} is not found")