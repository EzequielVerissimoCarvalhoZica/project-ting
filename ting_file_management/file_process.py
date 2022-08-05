from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
