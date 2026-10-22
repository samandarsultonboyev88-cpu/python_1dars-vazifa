ism = input("Ism: ")
familiya = input("Familiya: ")

username = f"{ism[:3].lower()}_{familiya[:3].lower()}"

print(f"Username: {username}")