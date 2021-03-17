import sys
from ting_file_management.file_management import txt_importer


def format(name, lines):
    return {
        "nome_do_arquivo": name,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }


def process(path_file, instance):
    text_data = txt_importer(path_file)
    for item in range(instance.__len__()):
        if instance.search(item)['nome_do_arquivo'] == path_file:
            return

    dict_return = format(path_file, text_data)
    instance.enqueue(dict_return)
    print(dict_return, file=sys.stdout)


def remove(instance):
    file_name = instance.search(0)['nome_do_arquivo']
    instance.dequeue()
    if (instance.__len__() == 0):
        return print('Não há elementos', file=sys.stdout)
    return print(f'Arquivo {file_name} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
