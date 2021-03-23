def exists_word(word, instance):
    if not len(instance.queue):
        return []
    result_list = list()
    for file in instance.queue:
        lines_that_occurs = list()
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word in line:
                lines_that_occurs.append({ "linha": index + 1})
        if len(lines_that_occurs):
            result_file = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines_that_occurs
            }
            result_list.append(result_file)
    
    return result_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
