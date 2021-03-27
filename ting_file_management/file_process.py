from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file_read = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,  # Nome do arquivo recém adicionado
        "qtd_linhas": len(file_read),  # Qtde de linhas existentes no arquivo
        "linhas_do_arquivo": file_read  # linhas retornadas pela função do req2
    }

    instance.enqueue(result)
    print(result, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
