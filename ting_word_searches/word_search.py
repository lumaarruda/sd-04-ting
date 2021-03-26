def serch_each_line(word, file):
    ocorrencias = []
    for index in range(file["qtd_linhas"]):
        line = file["linhas_do_arquivo"][index]
        if word.lower() in line.lower():
            ocorrencias.append({"linha": index + 1})

    return ocorrencias


def exists_word(word, instance):
    files_with_word = []
    for file in instance:
        ocorrencias = serch_each_line(word, file)
        if ocorrencias:
            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )
        print("bbbbbbbbbbbbbbbbbbbb", files_with_word)
    return files_with_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
