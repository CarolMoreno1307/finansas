from cryptography.fernet import Fernet
import os
import time
from dotenv import load_dotenv
import sys

# Cargar variables de entorno
BASE_DIR = os.path.dirname(__file__)
dotenv_path = os.path.join(BASE_DIR, "config", ".env")
load_dotenv(dotenv_path, override=True)

print(f' - - - BIENVENIDO AL ENCRIPTADOR  - - -\n\nIntroduce las credenciales que deseas encriptar y la llave maestra del encriptador.\nLas credenciales encriptadas serán almacenadas en el archivo config/.env.\n\n')
usuario = input('Ingresa el usuario: ')
contrasena = input('Ingresa la contraseña: ')

# Obtener llave desde variables de entorno
llave = os.getenv('LLAVE_MAESTRA')
if not llave:
    print("ERROR: No se pudo cargar LLAVE_MAESTRA desde config/.env")
    sys.exit(1)

key = llave.encode('utf-8')                           #Llave única para encriptado y desencriptado
objeto_cifrado = Fernet(key)                          #Crear objeto para la encripción

user_encriptado = objeto_cifrado.encrypt(str.encode(usuario))
pass_encriptado = objeto_cifrado.encrypt(str.encode(contrasena))

# Crear directorio config si no existe
os.makedirs('config', exist_ok=True)

# Guardar en config/.env
with open('config/.env', 'w') as f:
    f.write(f'USER={user_encriptado.decode()}\n')
    f.write(f'PASSWORD={pass_encriptado.decode()}\n')
    f.write(f'LLAVE_MAESTRA={llave}\n')

print(f'Usuario encriptado guardado en config/.env')
print(f'Contraseña encriptada guardada en config/.env')

print(f'\n\n - - - HASTA LUEGO  - - -\n')
time.sleep(3)
