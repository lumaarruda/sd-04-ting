import re


def exists_word(word, instance):
    list = []
    count = 0

    for i in range(len(instance)):
        seach_intance = instance.search(i)
        list_of_ocorrence = []
        count += 1
        for line in seach_intance["linhas_do_arquivo"]:
            if re.search(word, line, re.IGNORECASE):
                list_of_ocorrence.append({
                    "linha": count,
                })
                list.append({
                    "palavra": f"{word}",
                    "arquivo": seach_intance["nome_do_arquivo"],
                    "ocorrencias": list_of_ocorrence,
                })

    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
