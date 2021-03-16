from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    txt = txt_importer(path_file)
    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    instance.enqueue(info)


def remove(instance):
    instance.dequeue()


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
