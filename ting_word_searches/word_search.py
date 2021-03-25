def search_on_line(word, file_info, add_content):
    result = []
    for index in range(len(file_info["linhas_do_arquivo"])):
        file_lines = file_info["linhas_do_arquivo"][index]
        if word.lower() in file_lines.lower():
            word_occurrence = {"linha": index + 1}
            if add_content:
                word_occurrence["conteudo"] = file_lines
            result.append(word_occurrence)
    return result


def search_on_instance(word, instance, add_content=False):
    files_found = []
    for file_info in instance:
        word_occurrence = search_on_line(word, file_info, add_content)

        if word_occurrence:
            files_found.append(
                {
                    "palavra": word,
                    "arquivo": file_info["nome_do_arquivo"],
                    "ocorrencias": word_occurrence,
                }
            )

    return files_found


def exists_word(word, instance):
    return search_on_instance(word, instance)


def search_by_word(word, instance):
    return search_on_instance(word, instance, True)
