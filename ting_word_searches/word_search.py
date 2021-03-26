def exists_word(word, instance):
    data = {"palavra": word, "arquivo": "", "ocorrencias": []}

    for item in range(len(instance)):
        file = instance.search(item)
        data["arquivo"] = file["nome_do_arquivo"]
        for index, line in enumerate(file["linhas_do_arquivo"]):
            # print("line =>", line)
            # print("index =>", index)
            if word in line:
                data["ocorrencias"].append({"linha": index + 1})
    if len(data["ocorrencias"]) == 0:
        return []

    return [data]


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
