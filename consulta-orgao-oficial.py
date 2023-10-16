import requests


def baixar_arquivo(url, endereco):
    # faz a requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print(
            "Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


if __name__ == "__main__":
    baixar_arquivo('https://campomourao.atende.net/atende.php?rot=54002&aca=737&processo=visualizar&parametro=%7B%22codigo%22%3A%223848%22%2C%22hash%22%3A%22ED46EDF78B6C64568F2360E0913CB07780900ABB%22%7D&cidade=padrao', './output/arquivo.pdf')
