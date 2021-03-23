git from .file_management import txt_importer


def process(path_file, instance):
    text_file = txt_importer(path_file)
    if '/' in path_file:
        path_file = path_file.split('/')[-1]
    
    return {
        'nome_do_arquivo': path_file,
        "qtd_linhas": len(text_file),
        "linhas_do_arquivo": text_file
    }


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
