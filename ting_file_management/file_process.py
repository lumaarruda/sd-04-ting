import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_data = txt_importer(path_file)

    file_info = {
       "nome_do_arquivo": path_file,
       "qtd_linhas": len(file_data),
       "linhas_do_arquivo": file_data
    }
    if instance.enqueue(file_info):
        return print(file_info, file=sys.stdout)

    return None


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
