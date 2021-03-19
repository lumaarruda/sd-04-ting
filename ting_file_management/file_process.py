import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    same_file = 0
    for index in range(len(instance)):
        file = instance.search(index)
        if path_file == file["nome_do_arquivo"]:
            same_file += 1
            break

    if same_file == 0:
        lines = txt_importer(path_file)

        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }

        instance.enqueue(file_info)

        sys.stdout.write(f"{file_info}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
