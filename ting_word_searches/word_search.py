def search_on_line(word, file_info, should_add_content):
    data = []
    for index in range(len(file_info["linhas_do_arquivo"])):
        line = file_info["linhas_do_arquivo"][index]
        if word.lower() in line.lower():
            occur = {"linha": index + 1}
            if should_add_content:
                occur["conteudo"] = line
            data.append(occur)
    return data


def search_on_instance(word, instance, should_add_content=False):
    files_found = []
    for file_info in instance:
        occurrences = search_on_line(word, file_info, should_add_content)

        if occurrences:
            files_found.append(
                {
                    "palavra": word,
                    "arquivo": file_info["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return files_found


def exists_word(word, instance):
    return search_on_instance(word, instance)


def search_by_word(word, instance):
    return search_on_instance(word, instance, True)

# def exists_word(word, instance):
    #     result = []
#     for i in range(len(instance)):
#         entry = instance.search(i)
#         occurrences = []
#         for index, line in enumerate(entry['linhas_do_arquivo']):
#             if word.lower() in line.lower():
#                 occurrences.append({"linha": index + 1})
#         if occurrences == []:
#             return occurrences
#         result.append({
#             "arquivo": entry['nome_do_arquivo'],
#             "ocorrencias": occurrences,
#             "palavra": word
#         })
#     return result
