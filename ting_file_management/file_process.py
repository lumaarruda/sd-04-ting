def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return

    lines_file = txt_importer(path_file)
    new_file = format(path_file, lines_file)
    instance.enqueue(new_file)
    print(new_file, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
