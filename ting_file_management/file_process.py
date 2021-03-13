from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    doc = txt_importer(path_file)
    if not instance.enqueue(path_file):
        return
    print(
        f"""'nome_do_arquivo': '{path_file}',
        'qtd_linhas': {len(doc)},
        'linhas_do_arquivo': {doc}""",
        file=sys.stdout,
    )


def remove(instance):
    """Aqui irá sua implementação"""
    file_removed = instance.dequeue()
    if file_removed:
        print(f"Arquivo {file_removed} removido com sucesso", file=sys.stdout)
    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        path_file = instance.search(position)
        text = txt_importer(path_file)
        print(
            f"""'nome_do_arquivo': '{path_file}',
        'qtd_linhas': {len(text)},
        'linhas_do_arquivo': {text}""",
            file=sys.stdout,
        )
    except IndexError:
        print("Posição inválida", file=sys.stderr)
