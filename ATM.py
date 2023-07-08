def shiko_bilancin(bilanci):
    print(f"Bilanci aktual i llogarisë tuaj është: {bilanci}€")


def terhiq_parate(bilanci):
    shuma = float(input("Shkruani shumën për të tërhequr: "))
    if shuma <= bilanci:
        bilanci -= shuma
        print(f"Terheqja u krye me sukses. Bilanci i mbetur: {bilanci}€")
    else:
        print("Fonde të pamjaftueshme. Terheqja u anulua.")


def depozito_parate(bilanci):
    shuma = float(input("Shkruani shumën për të depozituar: "))
    bilanci += shuma
    print(f"Depozita u krye me sukses. Bilanci i përditësuar: {bilanci}€")


def atm():
    emri = input("Shkruani emrin tuaj: ")
    bilanci = 1000.0

    while True:
        print("\nZgjidhni një opsion:")
        print("1. Shikoni gjendjen e llogarisë")
        print("2. Tërheqja e parave")
        print("3. Depozitoni para të gatshme")
        print("4. Dilni")

        opsioni = input("Zgjedh nje numër:  ")

        if opsioni == "1":
            shiko_bilancin(bilanci)
        elif opsioni == "2":
            terhiq_parate(bilanci)
        elif opsioni == "3":
            depozito_parate(bilanci)
        elif opsioni == "4":
            print("Ju e keni mbyllur me sukses programin. Mirupafshim!")
            break
        else:
            print("Zgjedhje e pavlefshme. Ju lutemi, provoni përsëri.")


atm()
