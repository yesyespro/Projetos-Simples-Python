from colorama import Fore
import sys
from os import system

if __name__ == "__main__":
    system("clear"); # Limpando a tela
    if len(sys.argv) <= 2:
        file=sys.argv[1]
        print(file)