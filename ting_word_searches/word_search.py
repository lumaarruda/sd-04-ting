import re


def exists_word(word, instance):
    queue = instance._queue
    count = 0
    match = []
    occurrences = []

    for file in queue:
        for i in file["linhas_do_arquivo"]:
            if re.findall(word, i, re.IGNORECASE):
                count += 1
                occurrences.append({"linha": count})

        if len(occurrences):
            match.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences})

    return match


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
