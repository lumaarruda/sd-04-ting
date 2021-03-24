import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    rows = txt_importer(path_file)

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(rows),
        "linhas_do_arquivo": rows
    }

    instance.enqueue(file_data)
    sys.stdout.write(f"{file_data}\n")
    return file_data


def remove(instance):
    """Aqui irá sua implementação"""
    if remove is None:
        sys.stdout.write("Não há elementos\n")
    else:
        file = instance.search(0)
        path = file["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(
            f"Arquivo {path} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        find_data = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
    else:
        print(find_data)

