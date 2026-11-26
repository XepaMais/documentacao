# Gera modelo/capa-alta.jpg: a capa do modelo com a logo e a linha laranja mais no alto
# (para aparecerem na miniatura do Google Drive).
import io, os
from docx import Document
from docx.oxml.ns import qn
from PIL import Image
BASE = os.path.dirname(os.path.abspath(__file__))
d = Document(os.path.join(BASE, 'modelo', 'dossie-modelo.docx'))
blip = d.element.body[0].find('.//' + qn('a:blip'))
part = d.part.related_parts[blip.get(qn('r:embed'))]
im = Image.open(io.BytesIO(part.blob)).convert('RGB')
w, h = im.size
fundo = im.getpixel((w // 2, int(h * 0.2)))
top, bot = int(h * 0.365), int(h * 0.556)          # logo + linha laranja
novo_top = int(h * 0.175)
bloco = im.crop((0, top, w, bot))
im.paste(Image.new('RGB', (w, bot - top), fundo), (0, top))
im.paste(bloco, (0, novo_top))
im.save(os.path.join(BASE, 'modelo', 'capa-alta.jpg'), quality=92)
print(w, h, 'logo de', round(top / h, 3), 'para', round(novo_top / h, 3), '| linha agora em', round((novo_top + bot - top) / h, 3))
