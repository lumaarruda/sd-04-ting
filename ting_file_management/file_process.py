from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    lines_file = txt_importer(path_file)
    new_file = format(path_file, lines_file)
    instance.enqueue(new_file)
    print(new_file, file=sys.stdout)


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()
        return print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")
    return print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
