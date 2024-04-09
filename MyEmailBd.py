import sqlite3 


connect = sqlite3.connect("emails.db")
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS emails(
    email TEXT,
    NAME TEXT,
    SURNAME TEXT,
    BirthDay TEXT,
    password TEXT,
    create_date TEXT
)
            """)

def SearchUsers(email):
    connect = sqlite3.connect("emails.db")
    cur = connect.cursor()
    
    cur.execute("SELECT * FROM emails WHERE email = ?", (email,))
    result = cur.fetchall()
    if len(result) <= 0:
        return False
    else:
        return True


def AddEmail():
    choice = input("Вы уверены что хотите добавить почту (y/n): ")
    if choice == "y":
        connect = sqlite3.connect("emails.db")
        cur = connect.cursor()
        email = input("Введите email: ")
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        birthday = input("Введите дату рождения(ДМГ): ")
        password = input("Введите пароль от почты: ")
        data_create = input("Введите дату создания (ДМГ): ")
        cur.execute("INSERT INTO emails VALUES(?,?,?,?,?,?)",(email,name,surname,birthday,password,data_create))
        connect.commit()
        connect.close()
        return True
    else:
        return False
    
    

    
def DeleteMail():
    connect = sqlite3.connect("emails.db")
    cur = connect.cursor()
    
    email = input("Введите маил который хотите удалить: ")
    if SearchUsers(email) == True:
        cur.execute(f"DELETE FROM emails WHERE email='{email}'")
        connect.commit()
        connect.close()
        return True
    else:
        return False
    
def ChangeMail():
    email = input("Введите маил который хотите изменить: ")
    if email!= None and SearchUsers(email) == True:
        connect = sqlite3.connect("emails.db")
        cur = connect.cursor()
        choice = int(input("Выберите что хотите изменить 1)Почта\n2)Имя\n3)Фамилия\n4)Дата рождения\n5)Пароль\n6)Дата создания\nНапишите цифру, которую хотите выбрать:"))
        if choice == 1:
            ChangeEmail = input("Введите емаил на который хотите поменять")
            cur.execute("UPDATE emails SET email =? WHERE email =?", (ChangeEmail, email))
            connect.commit()
            connect.close()
            return True
        if choice == 2:
            ChangeName = input("Введите имя на которое хотите сменить")
            cur.execute("UPDATE emails SET name =? WHERE email =?", (ChangeName, email))
            connect.commit()
            connect.close()
            return True
        if choice == 3:
            ChangeSurName = input("Введите фамилию на которое хотите сменить")
            cur.execute("UPDATE emails SET surname =? WHERE email =?", (ChangeSurName, email))
            connect.commit()
            connect.close()
            return True
        if choice == 4:
            ChangeBirthDay = input("Введите Дату рождения на которое хотите сменить")
            cur.execute("UPDATE emails SET BirthDay =? WHERE email =?", (ChangeBirthDay, email))
            connect.commit()
            connect.close()
            return True
        if choice == 5:
            ChangePass = input("Введите пароль на которое хотите сменить")
            cur.execute("UPDATE emails SET password =? WHERE email =?", (ChangePass, email))
            connect.commit()
            connect.close()
            return True
        if choice == 6:
            ChangeCreateDate = input("Введите дату создания на которое хотитеь сменить")
            cur.execute("UPDATE emails SET create_date =? WHERE email =?", (ChangeCreateDate, email))
            connect.commit()
            connect.close()
            return True
    else:
        return False


def InputEmail():
    connect = sqlite3.connect("emails.db")
    cur = connect.cursor()
    cur.execute("SELECT * FROM emails")
    rows = cur.fetchall()
    
    for row in rows:
        print(f"Почта: {row[0]} ||| Имя: {row[1]} ||| Фамилия: {row[2]} ||| Дата рождения: {row[3]} ||| Пароль: {row[4]} ||| Дата создания: {row[5]}")
            
    connect.close()
def main():
    print("Привет. Это База Данных твоих почт. Выбери действие:")
    while True:
        choice = input("1)Добавить почту\n2)Удалить Почту\n3)Вывести почты\n4)Изменить почту\n5)Выход\n")
        if choice == '1':
            AddEmail()
        elif choice == '2':
            DeleteMail()
        elif choice == '3':
            InputEmail()
        elif choice == '4':
            ChangeMail()
        elif choice == '5':
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")
main()
    
    
