def exists_word(word, instance):
    line_list = []
    result = []
    for index in range(len(instance)):
        file_checked = instance.search(index)
        if word in file_checked:
            line_list.append({"linha": index + 1})
            result.append({
                "palavra": word,
                "arquivo": file_checked["nome_do_arquivo"],
                "ocorrencias": line_list
            }.rstrip("\n"))
    return result


def search_by_word(word, instance):
    line_list = []
    result = []
    for index in range(len(instance)):
        file_checked = instance.search(index)
        if word in file_checked:
            line_list.append({
                "linha": index + 1,
                "conteudo": file_checked["linhas_do_arquivo"]})
            result.append({
                "palavra": word,
                "arquivo": file_checked["nome_do_arquivo"],
                "ocorrencias": line_list
            }.rstrip("\n"))
    return result
