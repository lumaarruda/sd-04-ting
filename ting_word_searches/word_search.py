def search_in_lines(word, file_info, add_content):
    occurrences = []
    for index in range(len(file_info["linhas_do_arquivo"])):
        line = file_info["linhas_do_arquivo"][index]
        if word.lower() in line.lower():
            occur = {"linha": index + 1}
            if add_content:
                occur["conteudo"] = line
            occurrences.append(occur)
    return occurrences


def exists_word(word, instance):
    """Aqui irá sua implementação"""


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
