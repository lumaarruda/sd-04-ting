def exists_word(word, instance):
    print(instance)
    for x in instance:

        if word in x["linhas_do_arquivo"]:
            return x
        else:
            return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
