from ting_file_management.file_management import txt_importer
# from ting_file_management.queue import Queue
import sys


lidos = set()
# fila = Queue()


def process(path_file, instance):
    result = {
        'nome_do_arquivo': '',
        'qtd_linhas': '',
        'linhas_do_arquivo': ''
        }
    dados = txt_importer(path_file)

    if path_file not in lidos:
        result['nome_do_arquivo'] = path_file
        result['qtd_linhas'] = len(dados)
        result['linhas_do_arquivo'] = dados
        lidos.add(path_file)
        instance.enqueue(result)
        return print(result, file=sys.stdout)
    else:
        pass


def remove(instance):
    removido = instance.dequeue()
    if removido:
        print("Arquivo statics/arquivo_teste.txt removido com sucesso",
              file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# if len(instance) == 0:
#         return print('Não há elementos', file=sys.stdout)
#     else:
#         instance.dequeue()
#        return print("Arquivo statics/arquivo_teste.txt removido com sucesso",
#                      file=sys.stdout)
