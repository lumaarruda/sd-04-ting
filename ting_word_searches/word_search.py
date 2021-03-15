def exists_word(word, instance):
    # data = [{
    #     "palavra": "",
    #     "arquivo": "",
    #     "ocorrencias": [
    #         {
    #             "linha": 1
    #         },
    #         {
    #             "linha": 2
    #         }
    #     ]
    # }]
    data = [{
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }]

    # data_exists_word = list()
    for index in range(len(instance)):
        folder = instance.search(index)
        print("\nFOLDER:", folder)

        # Arquivo
        data[0]["arquivo"] = folder["nome_do_arquivo"]

        # Ocorrências
        for index, line in enumerate(folder["linhas_do_arquivo"]):
            # print("\nINDEX:", index)
            # print("LINE:", line)
            if word in line:
                data[0]["ocorrencias"].append(
                    {
                        "linha": index + 1
                    }
                )

    # print("\n DATA:", data)
    if len(data[0]["ocorrencias"]) < 1:
        return []
    else:
        return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# --- Teste ---
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue

# print("\n--- Process ---")
# project = Queue()
# process("statics/nome_pedro.txt", project)
# print("\n\n--- Exists_Word ---")
# word = exists_word("Pedro", project)
