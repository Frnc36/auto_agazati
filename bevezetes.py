def feladat1():
    print("I/A:")
    auto = input("\tAutó neve: ")
    gyartas = int(input("\tGyártási dátum: "))

    if gyartas == 2025:
        print(f"I/B:\n\tFriss gyártás")
    elif gyartas < 2000:
        print(f"I/B:\n\tÖreg autó")
    else:
        print(f"I/B:\n\tEz az {auto} átlagos korú")


