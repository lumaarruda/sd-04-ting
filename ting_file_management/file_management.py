import sys

# How to import:
# 1- se (if) o arquivo não terminar com a extensão desejada, devolve erro.
# 2- tentar (try) abrir o arquivo (via filepath) e o ler.
# 3-    Armazenar essa leitura em uma variável (content)
# 4-    Tratar exceção (except) de arquivo não encontrado (filenotfounderror).
# 5-    Utilizar pipe stderr para as mensagens de erro.
# 6- senão (else) (significa que termina com a extensão desejada)
#                       no caso, split("/n")


def txt_importer(path_file):
    
