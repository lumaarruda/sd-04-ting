import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)

        with open(path_file, "r") as file:
            text = []
            lines = file.readlines()

            for line in lines:
                text.append(line.strip())
            return text

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
