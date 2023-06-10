import json

file_path = "data.json"

def load_registered_users():
        try:
            with open(file_path, "r") as file:
                registered_users = json.load(file)
        except FileNotFoundError:
            registered_users = []

        return registered_users

def save_registered_users(registered_users):
    with open(file_path, "w") as file:
        json.dump(registered_users, file)

def check_id(sender_id):
    registered_users = load_registered_users()  # Carregar os usuários registrados do arquivo JSON

    if sender_id not in registered_users:
        registered_users.append(sender_id)
        save_registered_users(registered_users)  # Salvar os usuários registrados no arquivo JSON
        return False # se o user não existir vai retornar False
    else:
        return True # se o user ja existir vai retornar True
