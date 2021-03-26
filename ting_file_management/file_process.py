import sys
from ting_file_management.file_management import txt_importer


def format_file(path_file, lines):
    return {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    lines = txt_importer(path_file)
    new_file = format_file(path_file, lines)
    instance.enqueue(new_file)
    print(new_file, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
