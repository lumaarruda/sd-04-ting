import sys
from .file_management import txt_importer


def process(path_file, instance):
    text_file = txt_importer(path_file)
    processed_file = {
        'nome_do_arquivo': path_file,
        "qtd_linhas": len(text_file),
        "linhas_do_arquivo": text_file
    }

    return print(f"{processed_file}", file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
