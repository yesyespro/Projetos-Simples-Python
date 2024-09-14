from colorama import Fore
import sys
from os import system
import os
import time

def verificar_vogais(conteudo):
    vogais= ["a","e","i","o","u"] 
    i=0
    for linha in conteudo:
        if linha in vogais: #verificando se caractere esta no array vogais
            i+=1
    return i
        


if __name__ == "__main__":
    system("clear"); 
    if len(sys.argv) <= 2:
        file=sys.argv[1]
        if not os.path.isfile(file):
            print("Por favor passe um arquivo")
            exit(1)
        #lendo arquivo e mandando pra função verificar vogais
        with open(file, 'r') as arq:
            ler=arq.read()
            retorno = verificar_vogais(ler)
        if retorno > 1:
            plural="vogais"
        else:
            plural="vogal"
        print(f"há {retorno} {plural}")
