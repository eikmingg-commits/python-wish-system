print("Unknown Entity: what do you desire for mortal?")
print("1. Wealth")
print("2. Influence")
print("3. Wisdom")
print("4. Immortality")
print("5. Women")

choice = input("Choose your desire (1-5): ")

if choice == '1':
    print("hmp... the usual. very well, wealth shall be yours.")  
elif choice == '2':
    print("so be it, influence shall be yours.")
elif choice == '3':
    print("granted, wisdom shall be yours.")
elif choice == '4':
    print("as you wish, immortality shall be yours.")
elif choice == '5':
    print("hmp.. very well.")

else:
    secret_choice = input("Are you sure you want to choose nothing? (yes/no): ").lower()
    if secret_choice == 'yes':
        print("the ultimate wish... to have no desires at all.")
    else:
        print("choose wisely next time.")