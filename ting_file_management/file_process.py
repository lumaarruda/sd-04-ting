from ting_file_management.file_management import txt_importer
import sys


def stdout_file(file_info):
    print(f"""'nome_do_arquivo': '{file_info["nome_do_arquivo"]}',
        'qtd_linhas': {len(file_info["linhas_do_arquivo"])},
        'linhas_do_arquivo': {file_info["linhas_do_arquivo"]}""", file=sys.stdout)


def process(path_file, instance):
    text = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(text),
        "linhas_do_arquivo": text
    }
    if instance.enqueue(file_info):
        stdout_file(file_info)


def remove(instance):
    file_removed = instance.dequeue()
    if file_removed:
        print(f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso", file=sys.stdout)
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        stdout_file(file_info)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
