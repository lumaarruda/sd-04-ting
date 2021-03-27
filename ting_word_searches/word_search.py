def exists_word(word, instance):
    """Aqui irá sua implementação"""
    for x, y in enumerate(instance):
        if word in y["linhas_do_arquivo"][0]:
            search_res = [
                {
                    "palavra": f"{word}",
                    "arquivo": f'{y["nome_do_arquivo"]}',
                    "ocorrencias": [{"linha": x + 1}],
                }
            ]
        return search_res
    else:
        return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
