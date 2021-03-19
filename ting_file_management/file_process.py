import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    same_files = 0
    for index in range(len(instance)):
        element = instance.search(index)
        if path_file == element["nome_do_arquivo"]:
            same_files += 1
            break

    if same_files == 0:
        lines = txt_importer(path_file)

        processed_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines
        }

        instance.enqueue(processed_data)

        sys.stdout.write(f"{processed_data}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
