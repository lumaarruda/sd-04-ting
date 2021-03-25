import sys


def search_word(word, instance, add_content):
    list_files = list()
    for index in range(len(instance)):
        file_search = instance.search(index)
        list_ocurrences = list()

        conteudo = file_search["linhas_do_arquivo"]
        for linha in range(len(conteudo)):
            if word.lower() in conteudo[linha].lower():
                if add_content:
                    list_ocurrences.append({"linha": linha + 1,
                                            "conteudo": conteudo[linha]})
                else:
                    list_ocurrences.append({"linha": linha + 1})
        if len(list_ocurrences) > 0:
            list_files.append({
                "palavra": word,
                "arquivo": file_search["nome_do_arquivo"],
                "ocorrencias": list_ocurrences
            })

    return list_files


def exists_word(word, instance):
    return search_word(word, instance, False)


def search_by_word(word, instance):
    return search_word(word, instance, True)
