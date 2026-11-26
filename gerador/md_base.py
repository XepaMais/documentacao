# Xepa+ | Versão Markdown dos documentos (mesmo conteúdo dos .docx), no padrão dos .md do repositório.
import re

CABECALHO = '''<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-texto-branca.png">
    <img src="assets/logo-texto-colorida.png" alt="Logo do Xepa+" width="280">
  </picture>
</p>
'''


def _celula(texto):
    linhas = []
    for linha in str(texto).split('\n'):
        m = re.fullmatch(r'(https?://\S+|mailto:\S+)(?:\s+\|\s+(.+))?', linha.strip())
        if m:
            url, rotulo = m.group(1), m.group(2) or m.group(1).replace('mailto:', '')
            linhas.append(f'[{rotulo}]({url})')
        else:
            linhas.append(linha.replace('|', '\\|'))
    return '<br>'.join(linhas)


class MdDoc:
    def __init__(self, titulo):
        self.titulo = titulo
        self.fig = 0
        self.partes = []
        self.h1s = 0

    def h1(self, texto):
        if self.h1s:
            self.partes.append('<br>')
        self.h1s += 1
        self.partes.append(f'# {texto}')

    def h2(self, texto, nova_pagina=False):
        self.partes.append(f'## {texto}')

    def p(self, texto):
        self.partes.append(texto)

    def vazio(self):
        pass

    def lista(self, itens):
        self.partes.append('\n'.join(f'- {i}' for i in itens))

    def codigo(self, linhas):
        self.partes.append('```text\n' + linhas + '\n```')

    def tabela(self, cab, linhas, larg=None, primeira_coluna=True, cores=None):
        if cores:  # coluna de amostra de cor não existe em Markdown: remove
            cab = cab[1:]
            linhas = [ln[1:] for ln in linhas]
        out = ['| ' + ' | '.join(cab) + ' |', '|' + '|'.join([' :--- '] * len(cab)) + '|']
        for ln in linhas:
            cels = [_celula(c) for c in ln]
            if primeira_coluna and cels[0]:
                cels[0] = f'**{cels[0]}**'
            out.append('| ' + ' | '.join(cels) + ' |')
        self.partes.append('\n'.join(out))

    def figura(self, arquivo, legenda, largura_mm=120):
        self.fig += 1
        px = int(largura_mm * 4.5)
        self.partes.append(f'<p align="center">\n  <img src="assets/{arquivo}" alt="{legenda}" width="{px}">\n</p>\n\n'
                           f'<p align="center"><sub>Figura {self.fig} – {legenda}</sub></p>')

    def texto(self, titulo_visivel=True, rodape=''):
        topo = CABECALHO + '\n' + (f'# {self.titulo}\n\n<br>\n\n' if titulo_visivel else '')
        corpo = '\n\n'.join(self.partes)
        return topo + corpo + ('\n\n' + rodape if rodape else '') + '\n'
