from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    imported_text = txt_importer(path_file)
    line = 0
    for line in imported_text:
        line += 1
    data = {
         "nome_do_arquivo": path_file,
         "qtd_linhas": line,
         "linhas_do_arquivo": imported_text,
    }

    instance.enqueue(data)


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()['nome_do_arquivo']
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
    except IndexError:
        sys.stderr.write("Posição inválida")
