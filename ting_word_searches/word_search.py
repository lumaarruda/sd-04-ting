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


def search_on_instance(word, instance, add_content=False):
    found = []
    for file_info in instance:
        occurrences = search_in_lines(word, file_info, add_content)

    if occurrences:
        found.append(
                {
                    "palavra": word,
                    "arquivo": file_info["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return found


def exists_word(word, instance):
    return search_on_instance(word, instance)


def search_by_word(word, instance):
    return search_on_instance(word, instance, True)
