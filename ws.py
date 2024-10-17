import string
import time
from colorama import init, Fore, Style

# Inicializa Colorama
init(autoreset=True)

# Definir los colores del arcoíris
rainbow_colors = [
    Fore.RED, Fore.YELLOW, Fore.GREEN,
    Fore.BLUE, Fore.MAGENTA, Fore.CYAN
]

def mostrar_busqueda(palabra):
    abecedario = string.ascii_lowercase

    for letra in palabra:
        print("Buscando la letra:")
        
        # Mostrar el abecedario letra por letra
        for letra_abecedario in abecedario:
            if letra_abecedario == letra:
                print(Fore.GREEN + letra_abecedario + Style.RESET_ALL, end=' ', flush=True)  
                tiempo_despues = 0.05  
            else:
                print(letra_abecedario, end=' ', flush=True)
                tiempo_despues = 0.1  
            time.sleep(tiempo_despues)  
        print()  
        
        time.sleep(1)  

        print("\n" + "-" * 30 + "\n")  

    print("Escribiendo la palabra completa...")
    for i, letra in enumerate(palabra):
        color = rainbow_colors[i % len(rainbow_colors)]  
        print(color + letra + Style.RESET_ALL, end='', flush=True)
        time.sleep(0.2)  
    print()  
if __name__ == "__main__":
    palabra_usuario = input("Introduce una palabra: ").lower()
    print("Iniciando la búsqueda...\n")
    mostrar_busqueda(palabra_usuario)
