from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        data = instance.search(index)

        if data["nome_do_arquivo"] == path_file:
            return None

    contents = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(contents),
        "linhas_do_arquivo": contents,
    }

    instance.enqueue(data)
    print(data)


def remove(instance: Queue):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)

    else:
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance: Queue, position):
    if not 0 <= position < len(instance):
        print("Posição inválida", file=sys.stderr)
    else:
        data = instance.search(position)
        print(data)
