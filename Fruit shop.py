print("please name and id vared konid :")
user_name = input("please your name :")
user_id = input("please your id :")
if user_name == "amir" and user_id == "123":
    print("***welcome to mive foroshi alamut***")
    print("menu : 1. moz 2. hendone 3. ananas 4. tallebi 5. koho(daraje1 , daraje2 , daraje3)")
    menu = int(input("please select az menu :"))
else:
    print("format eshteb ast , mojadad emtehan konid")

if menu == 1:
    a = "yes"
    while a == "yes":
        mojodi_anbar = float(input("please your mojodi ?"))
        kilo = float(input("chand kilo ?"))
        gaymat = float(input("gaymat chand ?"))
        total = kilo * gaymat
        print(total)
        baghi = mojodi_anbar - kilo
        if baghi < 10:
            print("mojodi anbar kam shode ast")
            quit()

        a = input("please yes , no :")
    print("b salamat")

elif menu == 2:
    a = "yes"
    while a == "yes":
        mojodi_anbar = float(input("please your mojodi ?"))
        kilo = float(input("chand kilo ?"))
        gaymat = float(input("gaymat chand ?"))
        total = kilo * gaymat
        print(total)
        baghi = mojodi_anbar - kilo
        if baghi < 10:
            print("mojodi anbar kam shode ast")
            quit()

        a = input("please yes , no :")
    print("b salamat")

elif menu == 3:
    a = "yes"
    while a == "yes":
        mojodi_anbar = float(input("please your mojodi ?"))
        kilo = float(input("chand kilo ?"))
        gaymat = float(input("gaymat chand ?"))
        total = kilo * gaymat
        print(total)
        baghi = mojodi_anbar - kilo
        if baghi < 10:
            print("mojodi anbar kam shode ast")
            quit()

        a = input("please yes , no :")
    print("b salamat")

elif menu == 4:
    a = "yes"
    while a == "yes":
        mojodi_anbar = float(input("please your mojodi ?"))
        kilo = float(input("chand kilo ?"))
        gaymat = float(input("gaymat chand ?"))
        total = kilo * gaymat
        print(total)
        baghi = mojodi_anbar - kilo
        if baghi < 10:
            print("mojodi anbar kam shode ast")
            quit()
        a = input("please yes , no :")
    print("b salamat")

elif menu == 5:
    a = "yes"
    while a == "yes":
        print("1 . daraje1 2. daraje2 3. daraje3")
        kaho_daraje = int(input("chose kaho ?"))
        if kaho_daraje == 1:
            mojodi_anbar = float(input("please your mojodi ?"))
            kilo = float(input("chand kilo ?"))
            gaymat = float(input("gaymat chand ?"))
            total = kilo * gaymat
            print(total)
            baghi = mojodi_anbar - kilo
            if baghi < 10:
                print("mojodi anbar kam shode ast")
                quit()

            a = input("please yes , no :")

        elif kaho_daraje == 2:
            mojodi_anbar = float(input("please your mojodi ?"))
            kilo = float(input("chand kilo ?"))
            gaymat = float(input("gaymat chand ?"))
            total = kilo * gaymat
            print(total)
            baghi = mojodi_anbar - kilo
            if baghi < 10:
                print("mojodi anbar kam shode ast")
                quit()

            a = input("please yes , no :")

        elif kaho_daraje == 3:
            mojodi_anbar = float(input("please your mojodi ?"))
            kilo = float(input("chand kilo ?"))
            gaymat = float(input("gaymat chand ?"))
            total = kilo * gaymat
            print(total)
            baghi = mojodi_anbar - kilo
            if baghi < 10:
                print("mojodi anbar kam shode ast")
                quit()
            a = input("please yes , no :")

    if total > 300000:
        takhfif = total * 0.1
        nahai = total - takhfif
        print(nahai)

