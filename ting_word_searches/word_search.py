def exists_word(word, instance):
    data = list()

    for index_instance in range(len(instance)):
        obj_structure = {"palavra": word, "arquivo": "", "ocorrencias": []}

        folder = instance.search(index_instance)
        # print("\nFOLDER:", folder)

        # Arquivo
        obj_structure["arquivo"] = folder["nome_do_arquivo"]

        # Ocorrências
        for index, line in enumerate(folder["linhas_do_arquivo"]):
            # print("\nINDEX:", index)
            # print("LINE:", line)
            if word.lower() in line.lower():
                obj_structure["ocorrencias"].append({"linha": index + 1})

        # Terminou a busca dentro de UM arquivo
        data.append(obj_structure)

    # Checando se a palavra não foi encontrada em nenhum arquivo
    for ocurrence in data:
        if len(ocurrence["ocorrencias"]) > 0:
            return data

    return []


def search_by_word(word, instance):
    data = list()

    for index_instance in range(len(instance)):
        obj_structure = {"palavra": word, "arquivo": "", "ocorrencias": []}
        folder = instance.search(index_instance)
        print("\nFOLDER:", folder)

        # Arquivo
        obj_structure["arquivo"] = folder["nome_do_arquivo"]

        # Ocorrências
        for index, line in enumerate(folder["linhas_do_arquivo"]):
            # print("\nINDEX:", index)
            # print("LINE:", line)
            if word.lower() in line.lower():
                obj_structure["ocorrencias"].append({
                    "linha": index + 1,
                    "conteudo": line
                })

        # Terminou a busca dentro de UM arquivo
        data.append(obj_structure)

    # print("\n DATA:", data)
    for ocurrence in data:
        if len(ocurrence["ocorrencias"]) > 0:
            return data

    return []

# --- Teste ---
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue

# print("\n--- Process ---")
# project = Queue()
# # process("statics/nome_pedro.txt", project)

# # print("\n\n--- Exists_Word ---")
# # word = exists_word("Pedro", project)

# print("\n\n--- Search_By_Word ---")
# word = search_by_word("pedro", project)
