from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    data = list()

    for index in range(len(instance)):
        content = instance.search(index)
        find_lines = list()

        for index, line in enumerate(content["linhas_do_arquivo"]):
            line_lower = line.lower()
            if line_lower.find(word.lower()) == -1:
                continue
            else:
                find_lines.append({"linha": index + 1})

        if len(find_lines) > 0:
            data.append({
                "palavra": word,
                "arquivo": content["nome_do_arquivo"],
                "ocorrencias": find_lines
            })

    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
