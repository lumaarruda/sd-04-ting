def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        entry = instance.search(i)
        occurrences = []
        for index, line in enumerate(entry['linhas_do_arquivo']):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})
        if occurrences == []:
            return occurrences
        result.append({
            "arquivo": entry['nome_do_arquivo'],
            "ocorrencias": occurrences,
            "palavra": word
        })
    return result


def search_on_instance(word, instance, add_content=False):
    files_found = []
    for file_info in instance:
        occurrences = exists_word(word, file_info, add_content)

        if occurrences:
            files_found.append(
                {
                    "palavra": word,
                    "arquivo": file_info["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return files_found


def search_by_word(word, instance):
    return search_on_instance(word, instance, True)

