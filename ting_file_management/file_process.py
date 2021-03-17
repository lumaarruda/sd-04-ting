from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return
    linhas_do_arquivo = txt_importer(path_file)
    new_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(linhas_do_arquivo),
        "linhas_do_arquivo": linhas_do_arquivo,
    }
    instance.enqueue(new_file)
    instance.last_file()


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
