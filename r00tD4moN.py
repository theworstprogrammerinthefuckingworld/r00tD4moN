#!/usr/bin/env python3
# ⬆ shebang de python
#librerias ⬇; 
import pyfiglet                 # pyfiglet para crear el banner en este caso 'hackpanel' , se instala con "pip install pyfiglet"
from termcolor import colored   # termcolor para poner colores a los textos , se  instala con "pip install termcolor"
import argparse                 # crea el penu de ayuda 
import sys                      # Proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python y el entorno del sistema.
import subprocess               # Permite crear nuevos procesos

def crear_panel_de_ayuda_banner(texto, fuente, color):
    banner = pyfiglet.figlet_format(texto, font=fuente)
    colored_banner = colored(banner, color)
    return colored_banner

def ejecutar_scan(ip):
    comando = ['nmap', '-sS', '-sV', '-Pn', '-p-', '-sC', '-Vv', '-vvv', '--min-rate', '5000', '-oN', 'escaneo_de_nmap{ip}.txt', ip] 
    try:
        _resultado_del_comnado_ = subprocess.run(comando, capture_output=True, text=True, check=True)
        print(_resultado_del_comnado_.stdout)  
    except subprocess.CalledProcessError as e:
        print(f'Error al ejecutar el escaneo: {e}')
        print(e.stderr)

def ejecutar_fuzzing(url):
    diccionario = '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt'
    comando = ['wfuzz', '-c', '--hc', '404', '-t', '200', '-w', diccionario, url + '/FUZZ']
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print(resultado.stdout)  
    except subprocess.CalledProcessError as e:
        print(f'Error al ejecutar el fuzzing: {e}')
        print(e.stderr)


def __panel_deayuda__():
    texto  = 'HackPanel'
    fuente = 'bloody'
    color  = 'red'
    banner = crear_panel_de_ayuda_banner(texto, fuente, color)
    print(banner)

   
    parser = argparse.ArgumentParser(
        description='↪ HELP PANEL',
        formatter_class=argparse.RawTextHelpFormatter
    )

    
    parser.add_argument('--scan',                        help='[INFO] Opción para un escaneo silencioso de una dirección IP con nmap')
    parser.add_argument('--fuzzing',                     help='[INFO] Opción para hacer fuzzing web con la herramienta wfuzz')
    parser.add_argument('--scanWP' ,                     help='[INFO] Opción para escanear WordPress con wpscan (sin la API)')
    parser.add_argument('--sql'    ,                     help='[INFO] Opción para ejecutar una SQL-injection con sqlmap')
    parser.add_argument('--smb'    ,                     help='[INFO] Opción para listar archivos compartidos de SMB')
    parser.add_argument('--url'    ,                     help='[INFO] Opción de URL')
    parser.add_argument('--rpc'    ,                     help='[INFO] Opción para enumerar archivos con el protocolo RPC')
    parser.add_argument('-pb'  ,'--password-brute-force',help='[INFO] Opción de fuerza bruta para atacar logins')
    parser.add_argument('-u'   , '--user'              , help='[INFO] Proporcionar credenciales de usuario compatible con diccionarios')
    parser.add_argument('-p'   , '--password'          , help='[INFO] Proporcionar credenciales de contraseña compatible con diccionarios')
    parser.add_argument('-d'   , '--dictionary'        , help='[INFO] Parámetro de diccionario')

    parser.add_argument('ip', type=str, help='[INFO] Parámetro para la IP o dirección') # arg importante

    if len(sys.argv) == 1:                                                              # Verificar si no se proporcionaron argumentos
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    print(f'IP: {args.ip}')                                                             # valores de los argumentos
    if args.scan:
        print(f'Scan: {args.scan}')
    if args.fuzzing:
        print(f'Fuzzing: {args.fuzzing}')
    if args.scanWP:
        print(f'ScanWP: {args.scanWP}')
    if args.password_brute_force:
        print(f'Password Brute Force: {args.password_brute_force}')
    if args.sql:
        print(f'SQL Injection: {args.sql}')
    if args.smb:
        print(f'SMB: {args.smb}')
    if args.user:
        print(f'User: {args.user}')
    if args.password:
        print(f'Password: {args.password}')
    if args.url:
        print(f'URL: {args.url}')
    if args.rpc:
        print(f'RPC: {args.rpc}')
    if args.dictionary:
        print(f'Dictionary: {args.dictionary}')

if __name__ == '__main__':
    __panel_deayuda__()
