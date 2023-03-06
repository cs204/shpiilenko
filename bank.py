bank = input("Приветствие: ")
if bank.startswith("здравствуйте"):
    print("$0")
elif bank.startswith("з"):
    print("$20")
else:
    print("$100")