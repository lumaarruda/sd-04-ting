def exists_word(word, instance):
    """Aqui irá sua implementação"""

    obj_file = [{
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }]

    for element in range(len(instance)):
        file = instance.search(element)
        # print('teste', file)

        obj_file[0]["arquivo"] = file["nome_do_arquivo"]
        # obj_file["ocorrencias"] = list()
        # obj_file["palavra"] = word
        for index, row in enumerate(file["linhas_do_arquivo"]):
            if word in row:
                obj_file[0]["ocorrencias"].append({"Linha": index + 1})

        if len(obj_file[0]["ocorrencias"]) < 1:
            return []
        else:
            return obj_file


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
