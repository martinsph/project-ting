def exists_word(word, instance):
    report = list()

    for index in range(len(instance)):
        occurrences = list()
        path_file = instance.search(index)["nome_do_arquivo"]
        lines = instance.search(index)

        for line, contents in enumerate(lines["linhas_do_arquivo"]):
            line_number_counter = line + 1
            if word.lower() in contents.lower():
                occurrences.append({"linha": line_number_counter})

    if len(occurrences):
        word_report = {
                "palavra": word,
                "arquivo": path_file,
                "ocorrencias": occurrences,
            }
        report.append(word_report)

    return report


def search_by_word(word, instance):
    report = list()

    for index in range(len(instance)):
        occurrences = list()
        path_file = instance.search(index)["nome_do_arquivo"]
        lines = instance.search(index)

        for line, contents in enumerate(lines["linhas_do_arquivo"]):
            line_number_counter = line + 1
            if word.lower() in contents.lower():
                occurrences.append({
                    "linha": line_number_counter,
                    "conteudo": contents
                    })

    if len(occurrences):
        word_report = {
                "palavra": word,
                "arquivo": path_file,
                "ocorrencias": occurrences,
            }
        report.append(word_report)

    return report
