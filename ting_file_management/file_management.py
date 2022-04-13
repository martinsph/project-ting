import sys


def txt_importer(path_file):
    if not path_file.lower().endswith(".txt"):
        error_msg = "Formato inválido\n"
        return sys.stderr.write(error_msg)

    try:
        with open(path_file, "r") as file:
            return file.read().split("\n")

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
