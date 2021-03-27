import sys
from .file_management import txt_importer


def process(path_file, instance):
    for item in range(len(instance)):
        if path_file == instance.search(item)["nome_do_arquivo"]:
            return

    txt_imported = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_imported),
        "linhas_do_arquivo": txt_imported,
    }

    sys.stdout.write(f"{data}")
    instance.enqueue(data)


def remove(instance):
    removed_file = instance.dequeue()
    if not removed_file:
        return print("Não há elementos")
    print(f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
