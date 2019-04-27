import json
import file_writing

from cryptography.fernet import Fernet




# Sets everything up to close the program
def close_unipass(account_dict):
    # Encrypts my data when I am done
    data = json.dumps(account_dict)

    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(bytes(data, 'utf-8'))

    file_writing.encrypt_function('password_manager.encrypted', 'wb', encrypted)
    file_writing.json_function('E:key.json', 'w', key.decode())
