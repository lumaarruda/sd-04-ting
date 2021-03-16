def exists_word(word, instance):
    output = list()
    obj = dict()
    for item in instance.elements:
        obj["palavra"] = word
        obj["arquivo"] = item["nome_do_arquivo"]
        obj["ocorrencias"] = list()
        for index, line in enumerate(item["linhas_do_arquivo"]):
            if word not in line:
                return output
            else:
                obj["ocorrencias"].append({"linha": index + 1})
    output.append(obj)
    return output


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
