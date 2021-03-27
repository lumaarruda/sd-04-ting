from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)['nome_do_arquivo'] == path_file:
            return

    data = txt_importer(path_file)

    result = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data,
    }

    instance.enqueue(result)
    return print(result, file=sys.stdout)
