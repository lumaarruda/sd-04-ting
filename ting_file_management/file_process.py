from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    importer = txt_importer(path_file)
    process_archive = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(importer),
        "linhas_do_arquivo": importer
    }

    instance.enqueue(process_archive)
    print(process_archive)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
