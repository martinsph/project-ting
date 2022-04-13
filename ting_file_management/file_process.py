import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    content = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    print(content)
    instance.enqueue(content)


def remove(instance):
    if len(instance) != 0:
        path_file = instance.dequeue()
        print(f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        sys.stderr.write("Posição inválida")
