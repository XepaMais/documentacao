# Xepa+ | Monta documentos .docx a partir do modelo do dossiê (modelo/dossie-modelo.docx).
# Mantém capa, estilos, cabeçalho (número da página) e rodapé do dossiê; troca só o conteúdo.
import os, re
from xml.sax.saxutils import escape
from docx import Document
from docx.shared import Mm
from docx.oxml import parse_xml
from docx.oxml.ns import qn, nsdecls
from docx.opc.constants import RELATIONSHIP_TYPE as RT

BASE = os.path.dirname(os.path.abspath(__file__))
MODELO = os.path.join(BASE, 'modelo', 'dossie-modelo.docx')
RAIZ = os.path.dirname(BASE)
IMG = os.path.join(RAIZ, 'assets')
W = nsdecls('w')

CAP_RPR = '<w:b/><w:color w:val="27693E"/><w:sz w:val="20"/><w:szCs w:val="20"/>'
CAPA_RPR = '<w:b/><w:caps/><w:color w:val="27693E"/><w:sz w:val="44"/><w:szCs w:val="44"/>'
COD_RPR = '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="17"/><w:szCs w:val="17"/>'
CELL_PPR = '<w:ind w:firstLine="0"/><w:jc w:val="left"/>'


def _runs(texto, rpr=''):
    """Converte texto com **negrito** em runs do Word."""
    out = []
    for i, parte in enumerate(re.split(r'\*\*', texto)):
        if not parte:
            continue
        r = rpr + ('<w:b/>' if i % 2 else '')
        out.append(f'<w:r><w:rPr>{r}</w:rPr><w:t xml:space="preserve">{escape(parte)}</w:t></w:r>')
    return ''.join(out)


class Doc:
    def __init__(self, titulo):
        self.d = Document(MODELO)
        self.titulo = titulo
        self.fig = 0
        body = self.d.element.body
        self.body = body
        els = list(body)
        capa = els[0]
        fim_capa = next(e for e in els if e.tag == qn('w:p') and e.find('.//' + qn('w:sectPr')) is not None)
        for e in els:
            if e is capa or e is fim_capa or e.tag == qn('w:sectPr'):
                continue
            body.remove(e)
        # Capa com a logo mais no alto (modelo/capa-alta.jpg, gerada por capa_alta.py),
        # para a logo e o título aparecerem na miniatura do Google Drive
        blip = capa.find('.//' + qn('a:blip'))
        with open(os.path.join(BASE, 'modelo', 'capa-alta.jpg'), 'rb') as f:
            self.d.part.related_parts[blip.get(qn('r:embed'))]._blob = f.read()
        # Título no meio da capa, abaixo da linha laranja da imagem
        t = parse_xml(
            f'<w:p {W}><w:pPr><w:spacing w:before="4830" w:after="0" w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:left="-567" w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
            f'{_runs(titulo, CAPA_RPR)}</w:p>')
        capa.addnext(t)
        self.d.core_properties.title = f'Xepa+ | {titulo}'

    # ---------- elementos ----------
    def _add(self, xml):
        el = parse_xml(xml)
        self.body.insert(len(self.body) - 1, el)
        return el

    def h1(self, texto):
        self._add(f'<w:p {W}><w:pPr><w:pStyle w:val="Ttulo1"/></w:pPr>{_runs(texto)}</w:p>')

    def h2(self, texto, nova_pagina=False):
        quebra = '<w:pageBreakBefore/>' if nova_pagina else ''
        self._add(f'<w:p {W}><w:pPr><w:pStyle w:val="Ttulo2"/>{quebra}</w:pPr>{_runs(texto)}</w:p>')

    def p(self, texto):
        self._add(f'<w:p {W}><w:pPr/>{_runs(texto)}</w:p>')

    def vazio(self):
        self._add(f'<w:p {W}/>')

    def lista(self, itens):
        for it in itens:
            self._add(f'<w:p {W}><w:pPr><w:pStyle w:val="PargrafodaLista"/>'
                      f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="3"/></w:numPr></w:pPr>{_runs(it)}</w:p>')

    def codigo(self, linhas):
        for ln in linhas.split('\n'):
            self._add(f'<w:p {W}><w:pPr><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/>'
                      f'<w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/><w:jc w:val="left"/></w:pPr>'
                      f'{_runs(ln or " ", COD_RPR)}</w:p>')
        self.vazio()

    def _cell_content(self, texto):
        paras = []
        for linha in str(texto).split('\n'):
            m = re.fullmatch(r'(https?://\S+|mailto:\S+)(?:\s+\|\s+(.+))?', linha.strip())
            if m:
                url, rotulo = m.group(1), m.group(2) or m.group(1).replace('mailto:', '')
                rid = self.d.part.relate_to(url, RT.HYPERLINK, is_external=True)
                run = (f'<w:hyperlink r:id="{rid}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                       f'<w:r><w:rPr><w:color w:val="0563C1"/><w:u w:val="single"/></w:rPr>'
                       f'<w:t xml:space="preserve">{escape(rotulo)}</w:t></w:r></w:hyperlink>')
            else:
                run = _runs(linha)
            paras.append(f'<w:p><w:pPr>{CELL_PPR}</w:pPr>{run}</w:p>')
        return ''.join(paras)

    def tabela(self, cab, linhas, larg=None, primeira_coluna=True, cores=None):
        """cab: lista de títulos; linhas: lista de listas; larg: pesos das colunas;
        cores: {(linha, coluna): 'RRGGBB'} para preencher células (ex.: amostras de cor)."""
        n = len(cab)
        larg = larg or [1] * n
        tot = 8494
        ws = [int(tot * x / sum(larg)) for x in larg]
        ws[-1] = tot - sum(ws[:-1])
        cores = cores or {}

        def tc(i, txt, r=None):
            shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{cores[(r, i)]}"/>' if (r, i) in cores else ''
            return f'<w:tc><w:tcPr><w:tcW w:w="{ws[i]}" w:type="dxa"/>{shd}</w:tcPr>{self._cell_content(txt)}</w:tc>'

        xml = [f'<w:tbl {W}><w:tblPr><w:tblStyle w:val="TabeladeGrade4-nfase211"/>'
               f'<w:tblW w:w="{tot}" w:type="dxa"/><w:tblLayout w:type="fixed"/>'
               f'<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="{1 if primeira_coluna else 0}" '
               f'w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr><w:tblGrid>']
        xml += [f'<w:gridCol w:w="{w}"/>' for w in ws]
        xml.append('</w:tblGrid><w:tr><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>')
        xml += [tc(i, t) for i, t in enumerate(cab)]
        xml.append('</w:tr>')
        for r, ln in enumerate(linhas):
            xml.append('<w:tr><w:trPr><w:cantSplit/></w:trPr>')
            xml += [tc(i, t, r) for i, t in enumerate(ln)]
            xml.append('</w:tr>')
        xml.append('</w:tbl>')
        self._add(''.join(xml))
        self.vazio()

    def figura(self, arquivo, legenda, largura_mm=120):
        self.fig += 1
        self._add(
            f'<w:p {W}><w:pPr><w:keepNext/><w:spacing w:before="200" w:after="80" w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:t xml:space="preserve">Figura </w:t></w:r>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:instrText xml:space="preserve"> SEQ Figura \\* ARABIC </w:instrText></w:r>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:t>{self.fig}</w:t></w:r>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:fldChar w:fldCharType="end"/></w:r>'
            f'<w:r><w:rPr>{CAP_RPR}</w:rPr><w:t xml:space="preserve"> – {escape(legenda)}</w:t></w:r></w:p>')
        par = self.d.add_paragraph()
        par.paragraph_format.first_line_indent = 0
        par.paragraph_format.alignment = 1
        par.paragraph_format.keep_with_next = True
        par.add_run().add_picture(os.path.join(IMG, arquivo), width=Mm(largura_mm))
        self._add(f'<w:p {W}><w:pPr><w:spacing w:after="240" w:line="240" w:lineRule="auto"/>'
                  f'<w:ind w:firstLine="0"/><w:jc w:val="center"/></w:pPr>'
                  f'<w:r><w:rPr><w:color w:val="464646"/><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>'
                  f'<w:t>Fonte: elaborado pela equipe (2026).</w:t></w:r></w:p>')

    def salvar(self, caminho):
        xml = self.d.element.xml
        for rid, rel in list(self.d.part.rels.items()):
            if rel.reltype == RT.IMAGE and f'"{rid}"' not in xml:
                del self.d.part.rels[rid]
        self.d.save(caminho)
