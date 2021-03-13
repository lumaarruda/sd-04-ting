from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    bof = txt_importer(path_file)
    counterLines = 0
    for line in bof:
        counterLines += 1
    arquivo = {
         "nome_do_arquivo": path_file,
         "qtd_linhas": counterLines,
         "linhas_do_arquivo": bof,
    }
    print("arquivo", arquivo)
    instance.enqueue(arquivo)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
