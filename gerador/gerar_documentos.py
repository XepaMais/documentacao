# Xepa+ | Gera os 7 documentos .docx no padrão do dossiê.
# Uso: python gerar_documentos.py   (saída em word/)
import os
from docx_base import Doc, BASE, RAIZ
from md_base import MdDoc

OUT = os.path.join(RAIZ, 'word')
os.makedirs(OUT, exist_ok=True)


# =====================================================================
def doc00(D=Doc):
    d = D('Apresentação do projeto')

    d.h1('1. O que é o Xepa+')
    d.p('O Xepa+ é uma plataforma digital que conecta feirantes a consumidores interessados em comprar frutas, verduras e legumes que sobraram ao final das feiras livres por preços mais acessíveis. A proposta busca reduzir o desperdício de alimentos, diminuir as perdas financeiras dos feirantes e facilitar o acesso da população a produtos frescos com preços menores.')
    d.p('A plataforma permite divulgar produtos, apresentar ofertas, aproximar consumidores dos feirantes e facilitar a localização de feiras com alimentos disponíveis. O projeto também considera recursos para cadastro de produtos, carrinho, pedidos, pagamento, mapa de feiras, receitas, área financeira e funcionalidades relacionadas à inteligência artificial.')
    d.vazio()
    d.tabela(['Pilar', 'O que significa'], [
        ['Menos desperdício', 'Novo destino para alimentos ainda próprios para consumo.'],
        ['Menos perdas', 'Mais uma chance de venda para o feirante.'],
        ['Mais acesso', 'Alimentos frescos com preços menores.'],
    ], [1, 3])
    d.h2('1.1 Motivação')
    d.p('A base principal para a criação do Xepa+ veio da realidade de Fabiane Carneiro e Aroaldo Sandes, feirantes da Zona Norte de São Paulo. A rotina dos dois mostrou à equipe o que acontece no encerramento da feira: alimentos ainda próprios para consumo que não encontram comprador a tempo e acabam vendidos com grande desconto, doados, levados para casa ou descartados.')
    d.p('A pesquisa de campo confirmou que a situação se repete: 95% dos feirantes que responderam têm sobras às vezes ou frequentemente, e 86% dos consumidores já deixaram de comprar frutas, verduras ou legumes por causa do preço.')
    d.h2('1.2 Missão, visão e valores')
    d.p('Missão: reduzir o desperdício de alimentos, dando um novo destino às frutas, verduras e legumes que sobram após as feiras livres, conectando feirantes a consumidores e tornando esses alimentos mais acessíveis.')
    d.vazio()
    d.p('Visão: ser referência no aproveitamento de alimentos pós-feira, promovendo um modelo de negócio sustentável, acessível e eficiente, que gere valor para consumidores, feirantes e parceiros.')
    d.vazio()
    d.p('Valores:')
    d.lista(['Sustentabilidade.', 'Acessibilidade.', 'Transparência.', 'Compromisso social.'])

    d.h1('2. Contexto e problema')
    d.p('Ao final das feiras livres, muitos feirantes ainda possuem frutas, verduras e legumes que não foram vendidos. Mesmo quando esses alimentos continuam próprios para consumo, parte deles pode acabar sendo descartada por falta de compradores ou de alternativas para a comercialização. O principal problema é a dificuldade de comercializar rapidamente os alimentos que sobram no final das feiras, mesmo quando ainda podem ser consumidos.')
    d.p('Essa situação representa uma oportunidade de reduzir as perdas financeiras dos comerciantes e facilitar o acesso da população a alimentos mais baratos. O Xepa+ surge para conectar essas duas necessidades por meio de uma plataforma digital que permite divulgar produtos, apresentar ofertas e aproximar consumidores dos feirantes.')
    d.h2('2.1 Dados sobre desperdício e acesso a alimentos')
    d.tabela(['Indicador', 'Dado', 'Fonte'], [
        ['Desperdício no mundo', '1,05 bilhão de toneladas de alimentos desperdiçadas em 2022, cerca de 19% do disponível ao consumidor.', 'UNEP (2024)'],
        ['Insegurança alimentar no Brasil', 'Cerca de 24% dos domicílios tinham algum grau de insegurança alimentar em 2024; 7,7% em nível moderado ou grave.', 'IBGE, PNAD Contínua (2025)'],
        ['Feiras livres em São Paulo', '975 feiras e mais de 12 mil feirantes, que movimentam cerca de R$ 2 bilhões por ano.', 'Prefeitura de São Paulo (2025)'],
        ['Desperdício nas feiras de SP', 'De 14,9 mil a 18,4 mil toneladas de resíduos comestíveis por ano.', 'Unesp e Universidade de Borås (2022)'],
        ['Região do piloto', '27 feiras livres na subprefeitura Freguesia/Brasilândia.', 'Lista oficial de feiras da Prefeitura'],
    ], [2247, 4321, 1926])

    d.h1('3. Público-alvo')
    d.p('O Xepa+ atende dois públicos principais: feirantes que precisam vender os produtos excedentes e consumidores que buscam economizar nas compras de alimentos.')
    d.vazio()
    d.p('Feirantes: comerciantes que vendem frutas, verduras e legumes em feiras livres e que podem permanecer com produtos não vendidos ao final do expediente. Parte dos feirantes pode ter pouca familiaridade com ferramentas digitais e preocupação com taxas de utilização. Por isso, a experiência deve ser simples, com funcionalidades fáceis de entender e utilizar.')
    d.vazio()
    d.p('Consumidores: pessoas que procuram frutas, verduras e legumes por preços acessíveis e que desejam encontrar ofertas em feiras próximas.')

    d.h1('4. A solução')
    d.p('Para feirantes que ficam com frutas, verduras e legumes ao final da feira e para consumidores que desejam economizar, o Xepa+ é uma plataforma digital que conecta as duas pontas: o feirante divulga e vende o que sobrou, e o consumidor encontra feiras próximas e compra esses alimentos por preços mais acessíveis.')
    d.vazio()
    d.tabela(['Quem', 'O que faz'], [
        ['Feirante', 'Cadastra a xepa com foto, preço e janela de retirada.'],
        ['Xepa+', 'Mostra as ofertas no catálogo e no mapa das feiras.'],
        ['Consumidor', 'Encontra a oferta, paga pelo app e reserva.'],
    ], [1, 3])
    d.h2('4.1 Plataforma')
    d.p('O Xepa+ é um site responsivo que conecta feirantes e consumidores em poucos cliques. A página inicial apresenta a proposta e mostra como a plataforma funciona, e o mapa das feiras encontra as feiras mais próximas a partir do CEP.')
    d.p('Na área do consumidor, é possível encontrar feiras próximas, ver as ofertas da hora da xepa, montar o carrinho, pagar com Pix, retirar o pedido na barraca com o código de retirada, conversar com o feirante e acompanhar o próprio impacto.')
    d.p('Na área do feirante, é possível cadastrar xepas e publicar as ofertas do dia, registrar as feiras onde trabalha, acompanhar os pedidos e confirmar a entrega, conversar com os clientes e controlar lucros, despesas e planilhas no financeiro.')
    d.h2('4.2 Xep.AI (Xepinha)')
    d.p('A Xepinha é a assistente virtual do Xepa+, criada para tornar a experiência mais simples, prática e divertida. Representada por uma pera, ela tira dúvidas na hora sobre pedidos, planos e o uso da plataforma e ajuda o feirante no dia a dia da banca, orientando o cadastro de xepas e a organização do financeiro. Foi criada com a API Gemini e está disponível nos planos Broto e Colheita.')
    d.figura('xepinha.jpeg', 'Xepinha, mascote da Xep.AI', 45)
    d.h2('4.3 Diferenciais')
    d.lista([
        'Foco nas feiras livres e no feirante como vendedor.',
        'Cestas com conteúdo informado, sem o modelo de sacola surpresa.',
        'Modelo de entrada sem mensalidade, com planos pagos opcionais.',
        'Benefício duplo: renda para o feirante e economia para o consumidor, alinhados à redução do desperdício.',
    ])
    d.h2('4.4 Tecnologias')
    d.p('Front-end em React, JavaScript, HTML e CSS; back-end em Java com Spring Boot; banco de dados MySQL; integração por API REST; hospedagem na Amazon EC2 (AWS); API Gemini na Xep.AI; Figma para os protótipos e Git e GitHub para o versionamento.')

    d.h1('5. Objetivos de Desenvolvimento Sustentável')
    d.p('O Xepa+ está alinhado a três Objetivos de Desenvolvimento Sustentável (ODS) estabelecidos pela Organização das Nações Unidas (ONU). A escolha está relacionada à proposta da plataforma de reduzir o desperdício de alimentos, valorizar o trabalho dos feirantes e incentivar o aproveitamento de produtos que ainda podem ser consumidos.')
    d.vazio()
    d.tabela(['ODS', 'Como o Xepa+ contribui'], [
        ['ODS 2 – Fome Zero e Agricultura Sustentável', 'Facilita o acesso a frutas, verduras e legumes por preços mais acessíveis, aproveitando alimentos que sobraram ao final das feiras livres.'],
        ['ODS 8 – Trabalho Decente e Crescimento Econômico', 'Apoia os pequenos comerciantes com um canal digital para divulgar produtos, reduzir perdas financeiras e gerar oportunidades de renda.'],
        ['ODS 12 – Consumo e Produção Responsáveis', 'Reduz o desperdício de alimentos ao aproveitar os produtos que sobram após as feiras e incentiva o consumo consciente.'],
    ], [1.4, 3])

    d.h1('6. Modelo de negócio e plano de ação')
    d.p('O Xepa+ adotará um modelo híbrido de monetização, combinando mensalidades opcionais e comissões sobre as vendas realizadas pela plataforma. Quanto maior o plano contratado, menor será a comissão cobrada por venda e maior será a quantidade de ferramentas disponíveis.')
    d.vazio()
    d.tabela(['Plano', 'Mensalidade', 'Comissão por venda'], [
        ['Semente', 'R$ 0,00', '15%'],
        ['Broto', 'R$ 29,90', '8%'],
        ['Colheita', 'R$ 59,90', '5%'],
    ], [1.4, 1, 1])
    d.h2('6.1 Plano de ação')
    d.tabela(['Fase', 'Quando e onde', 'Ações'], [
        ['Lançamento', 'Piloto de 4 semanas, na Brasilândia e na Freguesia do Ó', 'Disponibilizar o plano gratuito para atrair feirantes, validar a experiência de compra, testar pedidos e retiradas e observar a adesão.'],
        ['Crescimento', '2027, na cidade de São Paulo', 'Divulgar os planos Broto e Colheita, lançar o aplicativo para Android e iOS e avaliar as vendas e a adesão aos planos pagos.'],
        ['Expansão', 'De 2028 a 2030, em novos estados', 'Levar o Xepa+ às feiras livres de novos estados, oferecer entrega por motoboy e permitir a venda de produtos frescos além das xepas.'],
    ], [1, 1.6, 2.6])

    d.h1('7. Conclusão')
    d.p('O Xepa+ nasceu de um problema comum nas feiras livres: ao fim do dia, muitos alimentos ainda bons para consumo sobram nas barracas e acabam vendidos com prejuízo ou jogados fora. A plataforma liga o feirante que precisa vender essas xepas ao consumidor que quer comprar alimentos frescos por um preço menor. Assim, o que seria desperdício vira renda para quem vende e economia para quem compra.')
    d.p('O projeto mostra que é possível começar com pouco investimento e crescer de forma planejada. O primeiro passo é validar o modelo com os feirantes, conquistar consumidores e controlar os custos. A partir disso, a plataforma pode ganhar o aplicativo, a entrega por motoboy e a venda de produtos frescos além das xepas.')
    d.p('Mais do que uma plataforma de vendas, o Xepa+ é uma proposta de impacto social e ambiental. A plataforma valoriza o trabalho do feirante, aproxima as pessoas das feiras do bairro e combate o desperdício de alimentos.')
    return d


# =====================================================================
def doc01(D=Doc):
    d = D('Identidade visual')

    d.h1('1. Logo')
    d.p('A identidade visual do Xepa+ é inspirada na feira e utiliza uma paleta que combina verde, laranja, verde-amarelado, amarelo, cinza-escuro e branco. Ela é aplicada às páginas e aos componentes da plataforma, aos materiais de divulgação e à apresentação, contribuindo para a padronização das telas e para a consistência da experiência de navegação.')
    d.p('A logo une a cesta de compras aos alimentos que seriam desperdiçados e transmite três ideias: reaproveitamento, economia e sustentabilidade. O símbolo reforça o propósito da plataforma de dar um novo destino aos alimentos da xepa.')
    d.figura('logo-origem.png', 'Como nasceu a logo', 110)
    d.h2('1.1 Variações da logo')
    d.p('A logo tem duas variações: a verde, usada sobre fundos claros, e a branca, usada sobre fundo verde.')
    d.figura('variacoes-logo.png', 'Variações da logo', 140)
    d.tabela(['Variação', 'Onde usar'], [
        ['Verde', 'Fundos claros: site, documentos, redes sociais e materiais impressos.'],
        ['Branca', 'Fundo verde ou escuro: apresentação, capas e peças da marca.'],
    ], [1, 3])

    d.h1('2. Naming')
    d.p('O nome une a palavra “xepa”, que identifica os alimentos que permanecem nas feiras ao final do expediente, ao sinal “+”, que representa transformação e benefício.')
    d.vazio()
    d.p('Por que o nome funciona:')
    d.lista([
        'É uma palavra que o feirante e o freguês já usam: “hora da xepa”.',
        'É curto, fácil de falar e de lembrar.',
        'O “+” mostra que a xepa vale mais: mais alimento, mais renda e mais economia.',
    ])
    d.h2('2.1 Como escrever o nome')
    d.tabela(['Forma', 'Uso', 'Observação'], [
        ['Xepa+', 'Correto', 'X maiúsculo e “+” junto da palavra, sem espaço.'],
        ['o Xepa+', 'Correto', 'Em texto corrido, o nome é tratado no masculino: “o Xepa+ conecta…”.'],
        ['Xepa +, XepaMais, xepa mais', 'Evitar', '“XepaMais” e “xepamais” ficam só em endereços: site, GitHub e redes.'],
    ], [2, 1, 4])
    d.h2('2.2 Família de nomes')
    d.tabela(['Nome', 'O que é'], [
        ['Xep.AI (Xepinha)', 'Assistente virtual da plataforma, representada por uma pera.'],
        ['Semente, Broto e Colheita', 'Planos do feirante, que seguem o ciclo da planta: começar sem mensalidade, crescer e colher mais resultados.'],
        ['Hora da xepa', 'Ofertas do fim da feira na área do consumidor.'],
    ], [1, 2])
    d.h2('2.3 Mascote')
    d.p('A Xepinha é a assistente virtual do Xepa+, criada para tornar a experiência mais simples, prática e divertida. Representada por uma pera, segue o mesmo estilo de frutas da identidade visual.')
    d.figura('xepinha.jpeg', 'Xepinha, mascote da Xep.AI', 45)

    d.h1('3. Fontes')
    d.p('A fonte Poppins foi escolhida por seu estilo moderno, geométrico e de boa legibilidade. Junto com a paleta inspirada na feira, ela deixa a comunicação moderna, acolhedora e fácil de reconhecer, e é usada nos títulos e textos da plataforma e da apresentação.')
    d.vazio()
    d.tabela(['Uso', 'Fonte', 'Licença'], [
        ['Títulos', 'Poppins SemiBold e Bold', 'SIL Open Font License 1.1'],
        ['Corpo de texto', 'Poppins Regular e Medium', 'SIL Open Font License 1.1'],
        ['Destaques do site', 'Cal Sans', 'SIL Open Font License 1.1'],
        ['Código', 'JetBrains Mono', 'SIL Open Font License 1.1'],
    ], [1, 1.4, 1.4])
    d.figura('tipografia-poppins.png', 'Tipografia Poppins', 120)
    d.h2('3.1 Licenças')
    d.p('As três fontes usam a SIL Open Font License 1.1, que permite o uso gratuito em projetos pessoais e comerciais, a incorporação em sites, aplicativos e PDFs e a modificação. Não é permitido vender a fonte sozinha.')
    d.p('Todas estão disponíveis no Google Fonts. Fontes de apoio quando a principal não carregar: Arial (texto) e Consolas (código).')

    d.h1('4. Paleta de cores')
    d.p('A paleta é inspirada na feira: o verde das folhas, o laranja das frutas e do toldo, o amarelo e o verde-amarelado dos legumes, com cinza-escuro e branco para leitura.')
    d.vazio()
    cores = [('27693E', 'Verde', '39, 105, 62', 'Cor principal: cabeçalho, botões e títulos.'),
             ('F76019', 'Laranja', '247, 96, 25', 'Destaques, chamadas e botões de ação.'),
             ('9CB806', 'Verde-amarelado', '156, 184, 6', 'Detalhes, etiquetas e item ativo do menu.'),
             ('FFC927', 'Amarelo', '255, 201, 39', 'Apoio em ilustrações e destaques.'),
             ('161414', 'Cinza-escuro', '22, 20, 20', 'Textos.'),
             ('FFFFFF', 'Branco', '255, 255, 255', 'Fundos e textos sobre cores escuras.')]
    d.tabela(['Cor', 'Nome', 'HEX', 'RGB', 'Uso principal'],
             [['', n, '#' + h, rgb, u] for h, n, rgb, u in cores],
             [0.6, 1.4, 1, 1.2, 3], primeira_coluna=False,
             cores={(i, 0): c[0] for i, c in enumerate(cores)})
    d.h2('4.1 Contraste e acessibilidade')
    d.tabela(['Combinação', 'Contraste', 'Uso (WCAG 2.1)'], [
        ['Cinza-escuro sobre branco', '18,4 : 1', 'Qualquer texto.'],
        ['Branco sobre verde (e verde sobre branco)', '6,6 : 1', 'Qualquer texto (AA).'],
        ['Cinza-escuro sobre amarelo', '11,9 : 1', 'Qualquer texto.'],
        ['Cinza-escuro sobre verde-amarelado', '8,1 : 1', 'Qualquer texto.'],
        ['Cinza-escuro sobre laranja', '5,8 : 1', 'Qualquer texto (AA).'],
        ['Branco sobre laranja', '3,2 : 1', 'Só texto grande e em negrito.'],
        ['Branco sobre amarelo ou verde-amarelado', 'até 2,3 : 1', 'Não usar para texto.'],
    ], [2.2, 1, 2])

    d.h1('5. Guia de identidade visual')
    d.p('A identidade visual é aplicada às páginas e aos componentes da plataforma, aos materiais de divulgação, ao dossiê e à apresentação, garantindo telas padronizadas e uma experiência de navegação consistente.')
    d.h2('5.1 Elementos gráficos')
    d.lista([
        'Toldo listrado em verde e laranja, que lembra as barracas da feira, no topo da capa.',
        'Frutas na base da capa, sobre fundo claro.',
        'Títulos em verde, em caixa alta, com linha laranja abaixo.',
        'Tabelas com cabeçalho verde e linhas em verde-claro.',
    ])
    d.h2('5.2 Aplicações')
    d.tabela(['Peça', 'Como aplicar'], [
        ['Site', 'Fundo branco, cabeçalho verde, botões laranja e logo verde.'],
        ['Redes sociais', 'Instagram, Facebook e TikTok com fotos de alimentos, logo e paleta da marca.'],
        ['Panfletos e cartazes', 'Logo, slogan e QR Code para o agregador de links.'],
        ['Dossiê e apresentação', 'Capa com toldo e frutas, títulos verdes com linha laranja e tabelas com cabeçalho verde.'],
    ], [1, 3])
    d.h2('5.3 Uso da logo')
    d.lista([
        'Usar a logo verde em fundo claro e a branca em fundo verde.',
        'Não esticar, girar ou trocar as cores da logo.',
        'Não aplicar a logo sobre fotos sem contraste.',
    ])
    d.h2('5.4 Acessibilidade')
    d.p('Parte do público tem pouca familiaridade com ferramentas digitais. Por isso, o site conta com o widget de acessibilidade UserWay, rótulos nos formulários, textos alternativos nas imagens, atributos ARIA, layout responsivo e vídeos que respeitam a preferência por menos movimento.')

    d.h1('6. Slogan e tom de voz')
    d.p('Slogan: “Mais alimento, menos desperdício.”')
    d.h2('6.1 Tom de voz')
    d.p('O Xepa+ fala como a feira: perto, animado e direto. Usa as expressões que o feirante grita na banca e que o freguês já conhece, sem perder a clareza sobre preço, retirada e pagamento.')
    d.vazio()
    d.tabela(['Característica', 'Como aparece'], [
        ['Popular', 'Palavras do dia a dia da feira: freguês, banca, xepa, fresquinho.'],
        ['Acolhedor', 'Trata todo mundo com simpatia, como o feirante que conhece o cliente.'],
        ['Claro', 'Frases curtas. Preço, horário e regras sempre explicados.'],
        ['Transparente', 'Sem sacola surpresa: diz o que vem, a validade e a condição.'],
    ], [1, 3])
    d.h2('6.2 Falas da feira')
    d.p('Expressões populares das feiras livres que entram na comunicação da marca:')
    d.vazio()
    d.tabela(['Fala da feira', 'Como o Xepa+ usa'], [
        ['“Olha a xepa!”', 'Aviso de oferta nova: “Olha a xepa! A banca do José acabou de soltar ofertas perto de você.”'],
        ['“Chegou a hora da xepa!”', 'Título da vitrine de ofertas do fim da feira.'],
        ['“Pode chegar, freguesa!”', 'Boas-vindas na página inicial e no primeiro acesso.'],
        ['“Tá barato, tá baratinho!”', 'Chamada de posts com desconto em destaque.'],
        ['“Leva que é fresquinho!”', 'Cartão de oferta com validade e condição do produto.'],
        ['“Prova que é doce!”', 'Receitas sugeridas para usar o que foi comprado.'],
        ['“É três por dez!”', 'Cestas e combos.'],
        ['“É a última, vai levar?”', 'Aviso de estoque baixo.'],
        ['“Fim de feira, preço de xepa”', 'Frase de panfletos e cartazes nas feiras.'],
        ['“Freguês de sempre”', 'Mensagem de recompra e avaliação da banca.'],
    ], [1.3, 3])
    d.h2('6.3 Aplicação no dia a dia')
    d.tabela(['Situação', 'Assim', 'Assim não'], [
        ['Botão de compra', 'Quero essa xepa', 'Adicionar item ao carrinho de compras'],
        ['Pedido pronto', 'Tá separado! Retire na banca até 13h com o seu código.', 'Status do pedido alterado.'],
        ['Sem ofertas', 'A feira ainda não fechou por aqui. Volta na hora da xepa!', 'Nenhum resultado encontrado.'],
        ['Feirante', 'Sobrou? Cadastra a xepa em poucos toques.', 'Realize o cadastro dos produtos excedentes.'],
        ['Cancelamento', 'O produto acabou na banca. Seu dinheiro volta inteiro.', 'Pedido cancelado.'],
    ], [1, 2, 2])
    d.p('As falas populares trazem alegria, mas informações de preço, taxas, retirada, cancelamento e dados pessoais são sempre escritas de forma clara e completa.')
    return d


# =====================================================================
def doc02(D=Doc):
    d = D('Proposta de valor e mercado')

    d.h1('1. Proposta de valor')
    d.p('Para feirantes que ficam com frutas, verduras e legumes ao final da feira e para consumidores que desejam economizar, o Xepa+ é uma plataforma digital que conecta as duas pontas: o feirante divulga e vende o que sobrou, e o consumidor encontra feiras próximas e compra esses alimentos por preços mais acessíveis.')
    d.h2('1.1 Como o Xepa+ atende cada público')
    d.tabela(['Elemento', 'Feirantes', 'Consumidores'], [
        ['Público', 'Comerciantes de frutas, verduras e legumes com sobras ao final do expediente.', 'Pessoas que procuram esses alimentos por preços acessíveis.'],
        ['Problema', 'Dificuldade de encontrar compradores e de divulgar as sobras rapidamente.', 'Preço alto e falta de uma forma simples de encontrar a xepa.'],
        ['Evidências', '95% têm sobras às vezes ou frequentemente; 50% citam a falta de compradores; 80% responderam “sim” ou “talvez” à plataforma.', '86% já deixaram de comprar por causa do preço; 86% priorizam qualidade e frescor; todos responderam “sim” ou “talvez” à cesta de xepa.'],
        ['Solução', 'Cadastro de produtos, cestas e feiras, pedidos e recursos financeiros conforme o plano.', 'Ofertas, mapa de feiras, carrinho, pagamento, informações de retirada e receitas.'],
        ['Benefício', 'Menos perdas e desperdício, novos clientes e início sem mensalidade.', 'Economia, alimentos frescos e aproveitamento do que poderia ser descartado.'],
        ['Validação', 'Acompanhar adesão, atualização de ofertas, vendas e aceitação das comissões no piloto.', 'Acompanhar compra real, preço aceito, satisfação com a qualidade e recompra no piloto.'],
    ], [1, 2, 2])
    d.h2('1.2 Diferenciais')
    d.lista([
        'Foco nas feiras livres e no feirante como vendedor.',
        'Cestas com conteúdo informado, sem o modelo de sacola surpresa.',
        'Modelo de entrada sem mensalidade, com planos pagos opcionais.',
        'Benefício duplo: renda para o feirante e economia para o consumidor, alinhados à redução do desperdício.',
    ])

    d.h1('2. Personas')
    d.p('As duas personas representam as necessidades que o Xepa+ busca atender: consumidores que desejam economizar e feirantes que precisam vender os produtos excedentes.')
    d.vazio()
    d.p('Consumidora: Mariana tem 34 anos, é trabalhadora autônoma e busca economizar nas compras de alimentos. Frequenta feiras livres, pesquisa preços e utiliza o celular para encontrar ofertas. Seu objetivo é comprar frutas, verduras e legumes por valores acessíveis, mas enfrenta dificuldades para localizar feiras com produtos disponíveis na xepa.')
    d.vazio()
    d.p('Feirante: José tem 47 anos e trabalha em feiras livres, onde vende frutas, verduras e legumes. Ao final do dia, costuma ter produtos que não foram vendidos e que ainda podem ser consumidos. Sua principal dificuldade é encontrar compradores para esses alimentos e divulgar rapidamente as ofertas.')
    d.h2('2.1 Necessidades')
    d.tabela(['Persona', 'Necessidades'], [
        ['Mariana (consumidora)', 'Economizar nas compras.\nEncontrar produtos disponíveis na xepa.\nConsultar preços e ofertas.\nLocalizar feiras próximas.\nTer informações claras sobre retirada e pedidos.\nEncontrar alimentos em condições adequadas para consumo.'],
        ['José (feirante)', 'Comercializar rapidamente os alimentos excedentes.\nReduzir as perdas financeiras.\nDivulgar ofertas para mais consumidores.\nUtilizar uma plataforma simples e acessível.\nEntender os custos e as taxas cobradas pelo serviço.'],
    ], [1, 3])

    d.h1('3. Pesquisa de mercado')
    d.p('Dados de fontes públicas mostram que o problema não é isolado:')
    d.vazio()
    d.tabela(['Indicador', 'Dado', 'Fonte'], [
        ['Desperdício no mundo', '1,05 bilhão de toneladas de alimentos desperdiçadas em 2022, cerca de 19% do disponível ao consumidor.', 'UNEP (2024)'],
        ['Insegurança alimentar no Brasil', 'Cerca de 24% dos domicílios tinham algum grau de insegurança alimentar em 2024; 7,7% em nível moderado ou grave.', 'IBGE, PNAD Contínua (2025)'],
        ['Feiras livres em São Paulo', '975 feiras e mais de 12 mil feirantes, que movimentam cerca de R$ 2 bilhões por ano.', 'Prefeitura de São Paulo (2025)'],
        ['Desperdício nas feiras de SP', 'De 14,9 mil a 18,4 mil toneladas de resíduos comestíveis por ano.', 'Unesp e Universidade de Borås (2022)'],
        ['Região do piloto', '27 feiras livres na subprefeitura Freguesia/Brasilândia.', 'Lista oficial de feiras da Prefeitura'],
    ], [2247, 4321, 1926])
    d.h2('3.1 Pesquisa de campo')
    d.p('A pesquisa de campo foi realizada por meio de dois questionários on-line, um respondido por feirantes (20 respostas) e outro pelo público geral (29 respostas). Os percentuais descrevem apenas quem respondeu: as amostras são pequenas e concentradas, portanto, não representam todos os feirantes e consumidores da cidade.')
    d.h2('3.2 Pesquisa com feirantes')
    d.tabela(['Pergunta', 'Respostas'], [
        ['Perfil da amostra', '20 respostas · 95% da Zona Norte · 90% trabalham em feiras há mais de 10 anos · 70% têm de 29 a 49 anos.'],
        ['Frequência das sobras', 'Sim, às vezes: 65% · Sim, frequentemente: 30% · Raramente: 5%'],
        ['Destino das sobras', 'Faz doações: 45% · Tenta vender por um preço menor: 40% · Leva para casa: 20% · Utiliza de outra forma: 15%'],
        ['Dificuldades no fim da feira', 'Falta de compradores: 50% · Não tem dificuldades: 25% · Dificuldade para encontrar compradores interessados: 10% · Pouco tempo para vender: 10% · Clientes não querem comprar no fim: 5% · Produtos estragam rapidamente: 5%'],
        ['Interesse na plataforma', 'Sim: 40% · Talvez, dependendo de como funciona: 40% · Não: 20%'],
    ], [1, 3])
    d.h2('3.3 Pesquisa com consumidores')
    d.tabela(['Pergunta', 'Respostas'], [
        ['Perfil da amostra', '29 respostas · 48% têm de 18 a 28 anos · 55% moram na Zona Sul de SP.'],
        ['Frequência em feiras livres', 'Raramente: 45% · Sim, às vezes: 45% · Sim, frequentemente: 7% · Nunca: 3%'],
        ['Onde costumam comprar', 'Supermercados: 59% · Feiras livres: 48% · Hortifrutis: 38% · Sacolões: 34% · Mercados de bairro: 28%'],
        ['O que pesa na decisão', 'Qualidade e frescor: 86% · Preço: 69% · Aparência: 55% · Promoções: 24% · Variedade: 21% · Praticidade: 14% · Proximidade: 14%'],
        ['Já deixou de comprar pelo preço?', 'Sim, algumas vezes: 62% · Sim, frequentemente: 24% · Raramente: 10% · Nunca: 3%'],
        ['Compraria uma cesta de xepa?', 'Sim: 79% · Talvez, dependendo do preço: 21%'],
    ], [1, 3])
    d.p('Perguntas de múltipla escolha são contabilizadas por participante e podem somar mais de 100%.')

    d.h1('4. Concorrentes diretos e indiretos')
    d.p('A análise reúne soluções semelhantes para identificar padrões de interface, funcionalidades, tecnologias e oportunidades para o Xepa+. As informações vêm de páginas oficiais, lojas de aplicativos e reportagens, consultadas em novembro de 2026. As tecnologias internas dessas empresas não são públicas; por isso, foram registrados apenas os canais e os recursos tecnológicos divulgados.')
    d.h2('4.1 Concorrentes diretos')
    d.tabela(['Concorrente', 'Solução', 'Limitação'], [
        ['Food To Save', 'Venda de alimentos excedentes com desconto', 'Foco em restaurantes, mercados e hortifrutis'],
        ['Too Good To Go', 'Sacolas surpresa com alimentos excedentes', 'Não é focado em feiras livres'],
        ['Cheap Food', 'Venda de excedentes por preços menores', 'Não possui foco específico em feiras'],
        ['SuperOpa', 'Venda de produtos com desconto', 'Mais voltado ao varejo'],
    ], [1, 1.6, 1.6])
    d.h2('4.2 Concorrentes indiretos')
    d.tabela(['Solução', 'Como funciona', 'Limitação'], [
        ['Comida Invisível', 'Destina excedentes para instituições', 'Não atende diretamente o consumidor'],
        ['Sesc Mesa Brasil', 'Recebe e distribui alimentos para instituições', 'Não funciona como marketplace'],
        ['WhatsApp do feirante', 'Venda direta para clientes conhecidos', 'Processo manual e pouco organizado'],
        ['Venda no fim da feira', 'Produtos vendidos com desconto', 'Depende da presença física do consumidor'],
        ['Trocas e vendas locais', 'Negociação entre moradores', 'Baixa organização e previsibilidade'],
    ], [1, 1.6, 1.6])
    d.h2('4.3 Tabela comparativa')
    d.tabela(['Característica', 'Food To Save', 'Too Good To Go', 'Comida Invisível', 'Xepa+'], [
        ['Foco em feiras', 'Não', 'Não', 'Não', 'Sim'],
        ['Venda ao consumidor', 'Sim', 'Sim', 'Não', 'Sim'],
        ['Produtos excedentes', 'Sim', 'Sim', 'Sim', 'Sim'],
        ['Busca por localização', 'Sim', 'Sim', 'Sim', 'Sim'],
        ['Cesta surpresa', 'Sim', 'Sim', 'Não', 'Não; o conteúdo é informado'],
        ['Receitas para o consumidor', 'Não', 'Não', 'Não', 'Sim'],
        ['Feirante como vendedor', 'Não', 'Não', 'Não', 'Sim'],
    ], [1.6, 1, 1, 1, 1.2])

    d.h1('5. Análise de UI/UX, funcionalidades e tecnologias')
    d.tabela(['Solução', 'Interface e experiência', 'Funcionalidades', 'Tecnologia e canais'], [
        ['Food To Save', 'Passo a passo ilustrado, mapa de parceiros e escolha da sacola por categoria e porção.', 'Sacola surpresa, retirada ou entrega, pagamento no app, cupons e calculadora de CO2.', 'Aplicativo Android e iOS, portal web de usuários e portal de parceiros.'],
        ['Too Good To Go', 'Lista por distância, preço, avaliação e relevância, com confirmação da retirada no próprio app.', 'Sacola surpresa, janela de retirada e pagamento no app.', 'Aplicativo móvel com localização; plataforma para empresas.'],
        ['Cheap Food', 'Catálogo de ofertas com verificação da região de entrega após o cadastro.', 'Desconto conforme a validade, entrega ou retirada, inclusive itens de higiene.', 'Aplicativo com integração ao ERP de distribuidores e uso de IA na precificação.'],
        ['Comida Invisível', 'Fluxo voltado a doadores e ONGs, com informações de cada doação.', 'Doação de excedentes, apoio de nutricionistas e cursos.', 'Web e aplicativo, com geolocalização e rastreabilidade de dados.'],
        ['Sesc Mesa Brasil', 'Comunicação institucional, sem compra pelo consumidor.', 'Banco de alimentos e ações educativas para instituições.', 'Rede física de unidades; o site é institucional.'],
    ], [1, 1.6, 1.6, 1.6])
    d.h2('5.1 Pontos fortes, pontos fracos e oportunidades')
    d.tabela(['Solução', 'Pontos fortes', 'Pontos fracos', 'Oportunidade para o Xepa+'], [
        ['Food To Save', 'Mais de 10 mil estabelecimentos no app, descontos de até 70% e nota 4,8 na App Store.', 'Conteúdo surpresa e relatos de usuários sobre qualidade e falta de validade.', 'Informar o conteúdo e a validade de cada cesta.'],
        ['Too Good To Go', 'Marca internacional, presente em cerca de 20 países, e retirada simples.', 'Não foi localizada confirmação de operação no Brasil; não é focado em feiras.', 'Adotar como referência a janela de retirada.'],
        ['Cheap Food', 'Descontos de até 70% e mais de 30 cidades, segundo reportagens de 2020 e 2021.', 'Depende de distribuidores e varejo, sem foco em alimentos frescos de feira.', 'Atender o feirante que não possui ERP, com cadastro simples.'],
        ['Comida Invisível', 'Impacto social, rastreabilidade e apoio técnico.', 'Não vende ao consumidor final.', 'Complementar a doação com uma alternativa de renda; 45% dos feirantes já doam.'],
        ['Sesc Mesa Brasil', 'Maior rede privada de bancos de alimentos da América Latina, segundo o Sesc.', 'Atende instituições e não funciona como marketplace.', 'Considerar parceria para destinar o que não for vendido.'],
        ['WhatsApp e fim de feira', 'Sem custo e com contato direto com o cliente.', 'Processo manual e dependente da presença do consumidor.', 'Alcançar compradores que não estão na banca no encerramento.'],
    ], [1, 1.6, 1.6, 1.6])

    d.h1('6. Referências e oportunidades')
    d.h2('6.1 Padrões identificados')
    d.lista([
        'Mapa ou lista por proximidade para encontrar ofertas.',
        'Desconto em destaque e explicação do funcionamento em poucos passos.',
        'Pagamento no aplicativo e retirada no local como fluxo principal.',
        'Indicadores de impacto ambiental para reforçar o propósito do serviço.',
    ])
    d.h2('6.2 Oportunidades para o Xepa+')
    d.lista([
        'Ocupar o espaço das feiras livres, em que o feirante é o vendedor principal.',
        'Substituir a surpresa pela transparência sobre conteúdo, validade e condição dos alimentos.',
        'Oferecer cadastro simples e ajuda presencial aos feirantes.',
        'Unir compra, mapa de feiras, receitas e acompanhamento de impacto em uma só experiência.',
        'Permitir avaliações de bancas, recurso solicitado por usuários de soluções semelhantes.',
    ])

    d.h1('7. Consolidação dos dados')
    d.p('O cruzamento entre dados públicos, pesquisa de campo e análise de concorrentes mostra o que o Xepa+ precisa entregar:')
    d.vazio()
    d.tabela(['O que os dados mostram', 'Fonte', 'Decisão para o Xepa+'], [
        ['95% dos feirantes têm sobras e 50% citam falta de compradores no fim da feira.', 'Pesquisa com feirantes', 'Divulgar as ofertas para quem não está na banca no encerramento.'],
        ['Pouco tempo para vender e produtos que estragam.', 'Pesquisa com feirantes', 'Cadastro de xepa rápido e janela de retirada definida pelo feirante.'],
        ['40% responderam “talvez, dependendo de como funciona”.', 'Pesquisa com feirantes', 'Explicar cadastro, retirada, pagamento e taxas; abordagem presencial e Xepinha.'],
        ['45% dos feirantes já fazem doações.', 'Pesquisa com feirantes', 'Complementar a doação com renda e avaliar parceria com bancos de alimentos.'],
        ['86% já deixaram de comprar por causa do preço.', 'Pesquisa com consumidores', 'Comunicar claramente a economia em relação ao preço usual.'],
        ['86% priorizam qualidade e frescor.', 'Pesquisa com consumidores', 'Informar conteúdo, validade e condição; avaliação das bancas.'],
        ['Falta de tempo e horários incompatíveis com a feira.', 'Pesquisa com consumidores', 'Mapa por CEP, pagamento antecipado e retirada com código.'],
        ['Concorrentes não atendem feiras nem o feirante como vendedor.', 'Análise de concorrentes', 'Posicionar o Xepa+ como a plataforma da xepa das feiras livres.'],
        ['975 feiras e mais de 12 mil feirantes em São Paulo.', 'Prefeitura de SP', 'Começar pelo piloto na Zona Norte e crescer pela cidade.'],
    ], [2, 1.2, 2.2])
    d.p('A aceitação declarada na pesquisa é um sinal de interesse, ainda não uma comprovação de compra real. Por isso, a proposta será testada com vendas-piloto, acompanhando conversão, preço aceito, composição preferida das cestas e recompra.')
    return d


# =====================================================================
def doc03(D=Doc):
    d = D('Tecnologias')

    d.h1('1. Banco de dados')
    d.p('O banco de dados do Xepa+ foi implementado em MySQL 8 pelo script xepaDB 1.0 e é acessado pelo back-end em Java com Spring Boot, por meio de uma API REST. O banco possui 25 tabelas, organizadas em cinco grupos: contas e acesso, feiras e ofertas, compra, comunicação, e receitas e financeiro.')
    d.h2('1.1 Estratégia de dados')
    d.lista([
        'Dados de conta: identificação, contato e perfil de acesso de consumidores e feirantes.',
        'Dados de operação: feiras, xepas, pedidos, pagamentos e conversas.',
        'Dados de gestão: gastos por categoria, vendas e plano de cada feirante.',
        'Indicadores: volume de vendas, comissões, recompra, produtos mais vendidos e alimentos aproveitados.',
        'Proteção: senhas com hash, acesso por perfil, coleta apenas do necessário e atendimento à LGPD.',
        'Dados de pagamento: o Xepa+ guarda apenas o método, o valor e o status, sem armazenar dados de cartão.',
        'Integridade: o controle de versão da xepa impede que a mesma unidade seja vendida duas vezes, e o preço de cada item fica registrado no momento da compra.',
    ])
    d.h2('1.2 Tabelas do banco de dados')
    L = [2247, 4321, 1926]
    d.tabela(['Tabela', 'Principais campos', 'Finalidade'], [
        ['tb_conta', 'id_conta (PK), nome_conta, cpf_conta, email_conta, senha_conta (hash), telefone_conta, ativo, data_cadastro', 'Contas de acesso de todos os usuários'],
        ['tb_consumidor', 'id_consumidor (PK), id_conta (FK)', 'Perfil de consumidor da conta'],
        ['tb_feirante', 'id_feirante (PK), id_conta (FK), id_plano (FK), nome_fantasia, cnpj_feirante, ccm_feirante, matricula_feirante, grupo_comercio', 'Dados comerciais do feirante'],
        ['tb_colaborador', 'id_colaborador (PK), id_conta (FK)', 'Equipe do Xepa+ que administra a plataforma'],
        ['tb_plano', 'id_plano (PK), id_colaborador (FK), nome_plano, descricao_plano, valor_plano, ativo', 'Planos Semente, Broto e Colheita'],
        ['tb_dispositivo_sessao', 'id_dispositivo (PK), id_conta (FK), nome_aparelho, token_hash, expira_em, ultimo_acesso, revogado', 'Aparelhos conectados e sessões'],
        ['tb_feira', 'id_feira (PK), nome_feira, endereco_feira, cep_feira, cidade_feira, uf_feira, dia_semana, horario_inicio, horario_fim, latitude, longitude', 'Feiras exibidas no mapa'],
        ['tb_feirante_feira', 'id_feirante (PK, FK), id_feira (PK, FK)', 'Feiras em que cada feirante trabalha'],
        ['tb_categoria', 'id_categoria (PK), nome_categoria', 'Categorias de produtos'],
        ['tb_produto', 'id_produto (PK), id_feirante (FK), id_categoria (FK), nome_produto, descricao_produto, imagem_produto, unidade_medida, preco_referencia, ativo', 'Catálogo de produtos do feirante'],
        ['tb_xepa', 'id_xepa (PK), id_produto (FK), id_feira (FK), quantidade_xepa, preco_xepa, validade_xepa, data_retirada, horario_retirada_inicio, horario_retirada_fim, status_xepa, versao', 'Ofertas à venda e janela de retirada'],
        ['tb_carrinho', 'id_carrinho (PK), id_consumidor (FK), data_criacao', 'Carrinho do consumidor'],
        ['tb_item_carrinho', 'id_item_carrinho (PK), id_carrinho (FK), id_xepa (FK), quantidade_item', 'Itens do carrinho'],
        ['tb_pedido', 'id_pedido (PK), id_consumidor (FK), id_feirante (FK), data_pedido, status_pedido, valor_total, codigo_retirada', 'Pedidos, um por feirante'],
        ['tb_item_pedido', 'id_item_pedido (PK), id_pedido (FK), id_xepa (FK), quantidade_item, preco_unitario', 'Itens e preço no momento da compra'],
        ['tb_tipo_pagamento', 'id_tipo_pagamento (PK), metodo_pagamento', 'Pix, cartão de crédito, cartão de débito e dinheiro'],
        ['tb_pagamento', 'id_pagamento (PK), id_pedido (FK), id_tipo_pagamento (FK), valor_pagamento, status_pagamento, id_transacao_gateway, data_pagamento', 'Tentativas e situação do pagamento'],
        ['tb_avaliacao', 'id_avaliacao (PK), id_pedido (FK), id_consumidor (FK), id_feirante (FK), nota, comentario', 'Avaliação do pedido (nota de 1 a 5)'],
        ['tb_chat', 'id_chat (PK), id_consumidor (FK), id_feirante (FK), data_inicio', 'Conversa entre consumidor e feirante'],
        ['tb_mensagem', 'id_mensagem (PK), id_chat (FK), id_conta (FK), texto_mensagem, data_envio, lida', 'Mensagens de cada conversa'],
        ['tb_mensagem_ia', 'id_mensagem_ia (PK), id_conta (FK), papel, texto_mensagem_ia, data_envio', 'Conversas com a Xep.AI'],
        ['tb_receita_culinaria', 'id_receita (PK), titulo_receita, imagem_receita, modo_preparo, tempo_preparo', 'Receitas sugeridas ao consumidor'],
        ['tb_ingrediente_receita', 'id_ingrediente (PK), id_receita (FK), id_categoria (FK), nome_ingrediente, quantidade_ingrediente', 'Ingredientes ligados às categorias de xepa'],
        ['tb_categoria_gasto', 'id_categoria_gasto (PK), nome_categoria_gasto, descricao_categoria_gasto', 'Tipos de gasto do feirante'],
        ['tb_gasto', 'id_gasto (PK), id_feirante (FK), id_categoria_gasto (FK), valor_gasto, data_gasto, descricao_gasto', 'Despesas do feirante'],
    ], L)
    d.h2('1.3 Relacionamentos')
    d.lista([
        'Uma conta pode ter um perfil de consumidor, um de feirante e um de colaborador, cada um em relação 1:1.',
        'Uma conta possui vários dispositivos de sessão.',
        'Um colaborador cadastra vários planos, e um plano pode ser contratado por vários feirantes.',
        'Um feirante trabalha em várias feiras e uma feira reúne vários feirantes, relação registrada em tb_feirante_feira.',
        'Um feirante cadastra vários produtos; cada produto pertence a uma categoria e pode gerar várias xepas, cada uma ligada a uma feira.',
        'Cada consumidor tem um carrinho com vários itens; no checkout, o carrinho é dividido em um pedido por feirante.',
        'Um pedido possui vários itens, um ou mais pagamentos e, no máximo, uma avaliação.',
        'Um chat liga um consumidor a um feirante e possui várias mensagens; as conversas com a Xep.AI ficam ligadas à conta.',
        'Uma receita possui vários ingredientes, que podem estar ligados a uma categoria de produto.',
        'Um feirante registra vários gastos, cada um em uma categoria de gasto.',
    ])
    d.h2('1.4 Diagrama do banco de dados')
    d.figura('diagrama-banco-contas-feiras-ofertas.png', 'Diagrama do banco: contas, feiras e ofertas', 140)
    d.figura('diagrama-banco-compra-pagamento.png', 'Diagrama do banco: compra e pagamento', 140)
    d.figura('diagrama-banco-comunicacao-receitas-financeiro.png', 'Diagrama do banco: comunicação, receitas e financeiro', 140)

    d.h1('2. Back-end em Java')
    d.p('A API do Xepa+ é escrita em Java 17 com Spring Boot e organizada em camadas. Cada requisição do front-end entra por um controller, passa pelas regras de negócio no service e chega ao banco por meio dos repositórios do Spring Data JPA. O front-end não acessa o banco diretamente.')
    d.h2('2.1 Arquitetura em camadas')
    d.tabela(['Camada', 'Responsabilidade', 'Exemplos'], [
        ['Front-end (React)', 'Telas do consumidor e do feirante; envia requisições HTTP com JSON.', 'Área do consumidor e área do feirante'],
        ['Controller', 'Recebe a requisição, valida a entrada e devolve a resposta.', 'AuthController, FeiraController, FinanceiroController'],
        ['Service', 'Regras de negócio e transações (@Transactional).', 'AuthService, FeiraService, FinanceiroService'],
        ['Repository', 'Consultas ao banco com Spring Data JPA.', 'ContaRepository, FeiranteRepository, FeiraRepository'],
        ['Entidades e MySQL', 'Classes @Entity mapeadas para as tabelas tb_* do banco.', 'Conta, Feirante, Feira, Produto, Xepa, Pedido'],
    ], [1.2, 2.2, 2])
    d.h2('2.2 Tecnologias do back-end')
    d.tabela(['Tecnologia', 'Para que é usada'], [
        ['Java 17', 'Linguagem da aplicação do servidor.'],
        ['Spring Boot', 'Inicialização e configuração da API.'],
        ['Spring Web MVC', 'Criação dos endpoints HTTP/REST.'],
        ['Spring Data JPA e Hibernate', 'Persistência e consultas às entidades do banco.'],
        ['MySQL Connector/J', 'Comunicação JDBC com o MySQL.'],
        ['Lombok', 'Geração de getters e setters nas entidades.'],
        ['Maven Wrapper', 'Build, dependências e execução do projeto.'],
        ['PBKDF2 com HMAC-SHA-256', 'Hash das senhas antes de gravar no banco.'],
        ['JUnit e H2', 'Testes automatizados da API com banco em memória.'],
    ], [1, 2])
    d.h2('2.3 Estrutura de pacotes')
    d.codigo('br.com.xepamais.api\n'
             '├── ApiApplication          // inicia a API\n'
             '├── auth                    // cadastro, login e hash de senha\n'
             '│   └── dto                 // requisições e respostas de cadastro e login\n'
             '├── feira                   // feiras próximas e feiras do feirante\n'
             '├── financeiro              // lucros, gastos, resumo, histórico e planilha CSV\n'
             '├── admin                   // painel da equipe Xepa+\n'
             '├── config                  // CORS para o front-end\n'
             '└── database\n'
             '    ├── model               // entidades JPA\n'
             '    └── repository          // interfaces Spring Data JPA')
    d.h2('2.4 Exemplo de entidade')
    d.codigo('@Entity\n'
             '@Table(name = "tb_xepa")\n'
             '@Getter @Setter\n'
             'public class Xepa {\n'
             '    @Id\n'
             '    @GeneratedValue(strategy = GenerationType.IDENTITY)\n'
             '    @Column(name = "id_xepa")\n'
             '    private Integer id;\n'
             '\n'
             '    @ManyToOne\n'
             '    @JoinColumn(name = "id_produto", nullable = false)\n'
             '    private Produto produto;\n'
             '\n'
             '    @ManyToOne\n'
             '    @JoinColumn(name = "id_feira", nullable = false)\n'
             '    private Feira feira;\n'
             '\n'
             '    @Column(name = "preco_xepa", precision = 10, scale = 2)\n'
             '    private BigDecimal preco;\n'
             '\n'
             '    @Version   // impede vender a mesma unidade duas vezes\n'
             '    private Integer versao;\n'
             '}')
    d.h2('2.5 Regras de integridade')
    d.tabela(['Regra', 'Como funciona'], [
        ['Controle de versão da xepa', 'O campo versao com @Version faz o Hibernate recusar duas compras simultâneas da mesma unidade.'],
        ['Preço no momento da compra', 'preco_unitario em tb_item_pedido guarda o preço no momento da compra.'],
        ['Um pedido por feirante', 'No checkout, o carrinho é dividido em pedidos separados, cada um com seu código de retirada.'],
        ['Transações', 'Cadastro e operações financeiras rodam em @Transactional: ou tudo é gravado, ou nada.'],
        ['Senhas', 'Nunca voltam nas respostas da API; ficam só como hash PBKDF2.'],
        ['Pagamento', 'Só método, valor, status e id da transação do gateway; nenhum dado de cartão.'],
    ], [1, 2])
    d.p('O pedido passa pelas situações: aguardando pagamento, pago, pronto para retirada, retirado ou cancelado.')

    d.h1('3. Endpoints REST planejados')
    d.tabela(['Método', 'Endpoint', 'Finalidade', 'Acesso'], [
        ['POST', '/api/auth/cadastro', 'Criar conta', 'Público'],
        ['POST', '/api/auth/login', 'Entrar', 'Público'],
        ['GET, PUT', '/api/usuarios/me', 'Consultar e editar perfil', 'Logado'],
        ['GET', '/api/planos', 'Listar planos', 'Público'],
        ['PUT', '/api/feirantes/me/plano', 'Alterar o plano', 'Feirante'],
        ['GET', '/api/feiras', 'Listar feiras do mapa', 'Público'],
        ['POST, PUT, DELETE', '/api/feirantes/me/feiras', 'Gerenciar suas feiras', 'Feirante'],
        ['GET', '/api/xepas', 'Listar ofertas', 'Público'],
        ['POST', '/api/xepas', 'Cadastrar oferta', 'Feirante'],
        ['GET', '/api/xepas/{id}', 'Consultar oferta', 'Público'],
        ['PUT, DELETE', '/api/xepas/{id}', 'Alterar ou remover oferta', 'Feirante'],
        ['GET, POST', '/api/pedidos', 'Consultar e criar pedidos', 'Consumidor'],
        ['GET', '/api/feirantes/me/vendas', 'Consultar vendas', 'Feirante'],
        ['PATCH', '/api/pedidos/{id}/status', 'Atualizar situação', 'Feirante'],
        ['POST', '/api/pedidos/{id}/pagamento', 'Registrar pagamento', 'Consumidor'],
        ['GET, POST', '/api/financeiro/gastos', 'Consultar e registrar gastos', 'Feirante'],
        ['GET, POST', '/api/financeiro/lancamentos', 'Consultar e registrar rendas', 'Feirante'],
        ['GET', '/api/financeiro/resumo', 'Consultar indicadores', 'Feirante'],
        ['GET', '/api/conversas', 'Listar conversas', 'Logado'],
        ['GET, POST', '/api/conversas/{id}/mensagens', 'Ler e enviar mensagens', 'Logado'],
        ['POST', '/api/ia/mensagens', 'Conversar com a Xep.AI', 'Feirante'],
    ], [1.1, 2.4, 2, 1])
    d.p('Ajustes previstos: incluir a comissão de cada plano (15%, 8% e 5%) e o valor da comissão no pedido, criar tabelas de rendas do feirante, itens da cesta, consentimento da LGPD e recuperação de senha.')
    d.h2('3.1 Dados iniciais (seed)')
    d.p('O script já insere os meios de pagamento, as categorias de produtos e as categorias de gastos. As 975 feiras virão da lista oficial da Prefeitura de São Paulo, já usada no mapa do site, e os feirantes, consumidores, xepas e pedidos serão fictícios, simulando o piloto na Brasilândia e na Freguesia do Ó.')
    d.h2('3.2 Hospedagem da API')
    d.p('A API e o MySQL rodam em uma instância Amazon EC2 (t3.small) com disco EBS de 30 GB, IP fixo e snapshots para backup. A aplicação é empacotada pelo Maven e executada como serviço no servidor, com as credenciais do banco em variáveis de ambiente.')

    d.h1('4. Requisitos técnicos da plataforma')
    d.p('O desenvolvimento do Xepa+ considera os recursos necessários para disponibilizar a plataforma na internet, manter suas funcionalidades e permitir futuras melhorias.')
    d.vazio()
    d.tabela(['Área', 'Requisitos'], [
        ['Desenvolvimento', 'Front-end: React, JavaScript, HTML e CSS.\nBack-end: Java com Spring Boot.\nAPIs: integração entre front-end e back-end por endpoints REST.\nArquitetura: código organizado, modularizado e reutilizável.'],
        ['Banco de dados', 'MySQL.\nPersistência: armazenamento e recuperação dos dados entre sessões.\nModelagem: tabelas, chaves primárias, chaves estrangeiras e relacionamentos.\nSeed: dados de teste para simular situações reais.'],
        ['Infraestrutura e hospedagem', 'Hospedagem: Amazon EC2 (AWS), servidor em nuvem compatível com React, Java e MySQL.\nDomínio: endereço personalizado para acessar o Xepa+.\nArmazenamento: espaço para banco de dados, imagens e arquivos.\nBackups: cópias de segurança para recuperação dos dados.\nPublicação: aplicação disponível na internet.'],
        ['Integrações', 'Pagamentos: possibilidade de integração com Pix e outros meios de pagamento.\nMapas: localização das feiras e dos feirantes.\nServiços externos: integração com APIs necessárias às funcionalidades da plataforma.\nInteligência artificial: API Gemini, utilizada na criação da Xep.AI (Xepinha).'],
        ['Testes e qualidade', 'Testes funcionais: validação das principais funcionalidades.\nTratamento de erros: mensagens adequadas para falhas de conexão e operações.\nValidação de dados: verificação das informações enviadas pelos usuários.\nDesempenho: consultas eficientes e planejamento para crescimento da plataforma.'],
        ['Documentação e versionamento', 'Git e GitHub: controle de versões e armazenamento do código-fonte.\nFigma: protótipos e design das telas antes do desenvolvimento.\nREADME: instruções de instalação, execução e tecnologias utilizadas.\nDocumentação técnica: arquitetura, banco de dados e endpoints.\nDossiê: registro dos conceitos, funcionalidades e decisões do projeto.'],
        ['Apresentação do projeto', 'Agregador de links: página com acesso à plataforma, ao GitHub e às redes sociais.\nQR Code: acesso direto ao agregador de links.\nDemonstração: sistema publicado e funcional durante a apresentação.'],
    ], [1, 3])

    d.h1('5. Segurança, privacidade e acessibilidade')
    d.h2('5.1 Segurança')
    d.lista([
        'Autenticação: login e controle de acesso por perfil.',
        'Proteção de dados: armazenamento seguro de credenciais e informações pessoais.',
        'Senhas e tokens de sessão são guardados como hash, e o site usa HTTPS.',
        'O Xepa+ não armazena dados de cartão.',
    ])
    d.h2('5.2 Privacidade e LGPD')
    d.p('O Xepa+ segue a Lei nº 13.709/2018 (LGPD), coletando apenas os dados necessários e informando a finalidade de cada um.')
    d.vazio()
    d.tabela(['Dado', 'Finalidade', 'Base legal'], [
        ['Nome, e-mail, telefone, CPF e senha (hash)', 'Criar a conta, dar acesso e permitir o pagamento via Pix', 'Execução de contrato'],
        ['Dados do feirante (nome fantasia, CNPJ, matrícula)', 'Identificar o feirante e verificar se atua de forma regular', 'Execução de contrato e legítimo interesse'],
        ['Pedidos e pagamentos', 'Processar a compra, calcular a comissão e cumprir obrigações fiscais', 'Execução de contrato e obrigação legal'],
        ['Mensagens do chat e da Xep.AI', 'Comunicação sobre pedidos e respostas ao feirante', 'Execução de contrato'],
        ['Aparelhos e sessões', 'Manter o acesso seguro e permitir desconectar aparelhos', 'Legítimo interesse'],
        ['E-mail para novidades', 'Marketing', 'Consentimento (opcional)'],
    ], [1.6, 2, 1.4])
    d.p('No cadastro, o usuário marca a caixa “Li e aceito os Termos de Uso e a Política de Privacidade”.')
    d.h2('5.3 Acessibilidade')
    d.p('Parte do público tem pouca familiaridade com ferramentas digitais. Por isso, o site já conta com o widget de acessibilidade UserWay, rótulos nos formulários, textos alternativos nas imagens, atributos ARIA, layout responsivo e vídeos que respeitam a preferência por menos movimento.')
    return d


# =====================================================================
def doc04(D=Doc):
    d = D('Jornada do usuário')

    d.h1('1. Visão geral')
    d.p('O Xepa+ é um site responsivo que conecta feirantes e consumidores em poucos cliques. A jornada de cada público foi desenhada a partir das personas e da pesquisa de campo.')
    d.vazio()
    d.tabela(['Quem', 'O que faz'], [
        ['Feirante', 'Cadastra a xepa com foto, preço e janela de retirada.'],
        ['Xepa+', 'Mostra as ofertas no catálogo e no mapa das feiras.'],
        ['Consumidor', 'Encontra a oferta, paga pelo site e retira na banca.'],
    ], [1, 3])
    d.h2('1.1 Um dia de feira')
    d.tabela(['Momento', 'O que acontece'], [
        ['Durante a feira', 'O feirante vende normalmente na banca.'],
        ['Perto do fim', 'O feirante vê o que vai sobrar e cadastra a xepa no Xepa+.'],
        ['Hora da xepa', 'O consumidor encontra a oferta, compra e paga pelo Pix.'],
        ['Retirada', 'O consumidor retira na banca com o código, dentro da janela.'],
    ], [1, 3])
    d.h2('1.2 Pedidos, retirada e cancelamento')
    d.lista([
        'O pedido passa pelas situações: aguardando pagamento, pago, pronto para retirada, retirado ou cancelado.',
        'O consumidor retira na barraca, na janela definida pelo feirante, apresentando o código de retirada.',
        'Se o produto não estiver disponível ou não corresponder ao anunciado, o pedido é cancelado com estorno integral.',
        'Pedidos não retirados: o consumidor tem uma tolerância de 30 minutos após o fim da janela de retirada e recebe um lembrete pelo chat.',
        'Se o consumidor avisar pelo chat antes do fim da janela, o feirante pode combinar um novo horário no mesmo dia, enquanto estiver na feira.',
        'Encerrada a tolerância, o pedido é cancelado por não retirada e o feirante fica livre para vender os produtos na banca.',
        'Como os alimentos ficaram reservados e são perecíveis, o pedido não retirado não tem estorno; o feirante recebe o valor da venda, descontada a comissão do plano.',
        'Após três pedidos não retirados em 30 dias, a conta do consumidor fica impedida de fazer novos pedidos por 7 dias.',
    ])

    d.h1('2. Jornada da consumidora')
    d.p('Mariana, 34 anos, trabalhadora autônoma. Pesquisa preços e usa o celular para achar ofertas, mas não sabe onde encontrar a xepa.')
    d.vazio()
    d.tabela(['Etapa', 'O que ela faz', 'Tela no Xepa+', 'Como se sente', 'Oportunidade'], [
        ['1. Descobre', 'Vê um post no Instagram ou um panfleto com QR Code na feira.', 'Página inicial', 'Curiosa', 'Mostrar em poucos passos como funciona e quanto se economiza.'],
        ['2. Cadastra', 'Cria a conta com nome, e-mail, telefone, CPF e senha e aceita os Termos.', 'Criar conta e aceite dos termos', 'Desconfiada', 'Formulário curto, explicando por que cada dado é pedido (LGPD).'],
        ['3. Encontra', 'Informa o CEP e vê as feiras próximas e as ofertas da hora da xepa.', 'Mapa das feiras e início', 'Animada', 'Avisar quando uma banca próxima publicar xepa.'],
        ['4. Escolhe', 'Confere foto, preço, validade, condição e janela de retirada.', 'Detalhe do produto', 'Confiante', 'Conteúdo informado, sem sacola surpresa; avaliações da banca.'],
        ['5. Paga', 'Monta o carrinho e paga com Pix; o carrinho vira um pedido por feirante.', 'Carrinho e pagamento', 'Atenta', 'Deixar claro o total, a economia e o código de retirada.'],
        ['6. Retira', 'Vai até a banca na janela e mostra o código. Se atrasar, avisa pelo chat.', 'Meus pedidos e chat com o feirante', 'Satisfeita', 'Lembrete antes do fim da janela e tolerância de 30 minutos.'],
        ['7. Volta', 'Avalia a banca, vê receitas para usar a xepa e acompanha o próprio impacto.', 'Avaliação, receitas e impacto', 'Engajada', 'Incentivar a recompra e mostrar quanto alimento deixou de ir para o lixo.'],
    ], [1, 1.8, 1.4, 1, 1.8])

    d.h1('3. Jornada do feirante')
    d.p('José, 47 anos, feirante. No fim do dia tem produtos bons, mas não consegue encontrar compradores nem divulgar as ofertas a tempo.')
    d.vazio()
    d.tabela(['Etapa', 'O que ele faz', 'Tela no Xepa+', 'Como se sente', 'Oportunidade'], [
        ['1. Conhece', 'A equipe visita a feira, apresenta o projeto e mostra a plataforma no celular.', 'Página inicial', 'Desconfiado', 'Explicar cadastro, retirada, pagamento e taxas.'],
        ['2. Cadastra', 'Cria a conta com nome fantasia, CNPJ, CCM e matrícula e começa no plano Semente.', 'Criar conta do feirante e planos', 'Inseguro', 'Ajuda presencial no primeiro cadastro e início sem mensalidade.'],
        ['3. Organiza', 'Registra as feiras onde trabalha e os produtos da banca.', 'Adicionar feira e adicionar produtos', 'Mais seguro', 'Feiras já vêm da lista oficial da Prefeitura.'],
        ['4. Publica', 'Perto do fim da feira, cadastra a xepa com foto, quantidade, preço, validade e janela de retirada.', 'Adicionar produtos e histórico de produtos', 'Esperançoso', 'Publicar em poucos toques; a Xepinha orienta o cadastro.'],
        ['5. Vende', 'Recebe pedidos pagos e conversa com os clientes pelo chat.', 'Histórico de vendas e chat', 'Animado', 'Avisar cada pedido novo e mostrar o que está para retirar.'],
        ['6. Entrega', 'Confere o código do cliente e confirma a entrega na banca.', 'Confirmar entrega', 'Aliviado', 'A regra de não retirada protege o feirante.'],
        ['7. Cresce', 'Controla lucros, despesas e planilhas e avalia mudar para o Broto ou o Colheita.', 'Financeiro, planilhas, planos e Xep.AI', 'No controle', 'Mostrar a partir de quanto vendido cada plano fica mais barato.'],
    ], [1, 1.8, 1.4, 1, 1.8])

    d.h1('4. Telas de cada área')
    d.h2('4.1 Área do consumidor')
    d.p('Na área do consumidor, é possível encontrar feiras próximas, ver as ofertas da hora da xepa, montar o carrinho, pagar com Pix, retirar o pedido na barraca com o código de retirada, conversar com o feirante e acompanhar o próprio impacto.')
    d.vazio()
    d.tabela(['Tela', 'Para quê'], [
        ['Início', 'Ofertas da hora da xepa e feiras perto.'],
        ['Mapa de feiras', 'Feiras mais próximas a partir do CEP.'],
        ['Carrinho', 'Itens separados por feirante.'],
        ['Pagamento', 'Pagamento com Pix.'],
        ['Meus pedidos', 'Situação e código de retirada.'],
        ['Chat', 'Conversa com o feirante.'],
        ['Receitas', 'Ideias para usar a xepa.'],
        ['Impacto', 'Alimentos que deixaram de ir para o lixo.'],
    ], [1, 3])
    d.h2('4.2 Área do feirante')
    d.p('Na área do feirante, é possível cadastrar xepas e publicar as ofertas do dia, registrar as feiras onde trabalha, acompanhar os pedidos e confirmar a entrega, conversar com os clientes e controlar lucros, despesas e planilhas no financeiro.')
    d.vazio()
    d.tabela(['Tela', 'Para quê'], [
        ['Adicionar feira', 'Feiras onde trabalha.'],
        ['Adicionar produtos', 'Publicar as xepas do dia.'],
        ['Histórico de produtos', 'Editar e remover ofertas.'],
        ['Histórico de vendas', 'Pedidos e confirmação de entrega.'],
        ['Financeiro', 'Lucros, despesas e indicadores.'],
        ['Chat', 'Conversa com os clientes.'],
        ['Xep.AI', 'Dúvidas e ajuda no dia a dia (planos Broto e Colheita).'],
        ['Planos', 'Semente, Broto e Colheita.'],
    ], [1, 3])
    return d


# =====================================================================
def doc05(D=Doc):
    d = D('Links do projeto')
    d.h1('Links do projeto')
    d.tabela(['Item', 'Link'], [
        ['Site do Xepa+', 'https://xepamais.com.br/'],
        ['GitHub', 'https://github.com/XepaMais'],
        ['Figma', 'https://www.figma.com/design/5Nw6zLHUqIYhwYY50plLAZ/XEPA-?node-id=0-1&p=f&t=vl4HczMBfvlPGG1F-0 | Protótipo do Xepa+ no Figma'],
        ['Trello', 'https://trello.com/b/JAWsBfvE/inclusive'],
        ['Drive', 'https://drive.google.com/drive/folders/1CCV-396h58LKcWAGL3VJ0c5VaQ9GcCdR?usp=sharing'],
        ['Agregador de links', 'https://linktr.ee/xepa.mais'],
        ['Instagram', 'https://www.instagram.com/xepa_mais | @xepa_mais'],
        ['LinkedIn', 'https://linkedin.com/company/xepamais'],
        ['E-mail', 'mailto:xepamais8@gmail.com'],
        ['Pesquisa com feirantes', 'https://docs.google.com/forms/d/e/1FAIpQLScBpA0H-gxJ4zD2XmqOz_ab7Er4VnKzmdYcxqHZhlsvhKEkYQ/viewform | Formulário dos feirantes'],
        ['Pesquisa de consumo', 'https://docs.google.com/forms/d/e/1FAIpQLSdDhmJwShsM5SFmZPVTlWPbm0Z6rWXmDHxJuD8IZ6asRmkGmA/viewform | Formulário dos consumidores'],
    ], [1, 2.4])
    return d


# =====================================================================
def doc06(D=Doc):
    d = D('Financeiro')

    d.h1('1. Modelo de monetização')
    d.p('O Xepa+ adotará um modelo híbrido de monetização, combinando mensalidades opcionais e comissões sobre as vendas realizadas pela plataforma. O objetivo é facilitar a entrada de pequenos feirantes, oferecendo recursos adicionais para aqueles que desejam aumentar suas vendas, divulgar seus produtos e acompanhar o desempenho do negócio.')
    d.p('O modelo será dividido em três planos: Semente, Broto e Colheita. Quanto maior o plano contratado, menor será a comissão cobrada por venda e maior será a quantidade de ferramentas disponíveis.')
    d.h2('1.1 Descrição dos planos')
    d.p('Plano Semente – R$ 0/mês, comissão de 15% por venda. Para pequenos feirantes e novos vendedores que desejam começar sem pagar mensalidade.')
    d.lista(['Cadastro da banca e do feirante.', 'Cadastro e atualização de produtos.', 'Cadastro das feiras e locais de retirada.',
             'Divulgação dos produtos na plataforma.', 'Recebimento e acompanhamento de pedidos.', 'Acesso às conversas com clientes.'])
    d.vazio()
    d.p('Plano Broto – R$ 29,90/mês, comissão de 8% por venda. Para feirantes com vendas recorrentes que desejam aumentar a visibilidade e acompanhar melhor as vendas.')
    d.lista(['Todos os recursos do plano Semente.', 'Acesso básico ao financeiro.', 'Registro e acompanhamento de receitas e gastos.',
             'Consulta de informações financeiras básicas.', 'Acesso à Xep.AI.', 'Suporte pelo chat.'])
    d.vazio()
    d.p('Plano Colheita – R$ 59,90/mês, comissão de 5% por venda. Para feirantes que desejam expandir o negócio e precisam de controle financeiro completo.')
    d.lista(['Todos os recursos do plano Broto.', 'Acesso completo ao financeiro.', 'Acompanhamento de receitas, gastos e compras.',
             'Visualização de indicadores financeiros e capital de giro.', 'Possibilidade de destacar produtos e cestas.', 'Suporte prioritário pelo chat.'])
    d.h2('1.2 Comparação dos planos')
    d.tabela(['Funcionalidade', 'Semente', 'Broto', 'Colheita'], [
        ['Mensalidade', 'R$ 0,00', 'R$ 29,90', 'R$ 59,90'],
        ['Comissão por venda', '15%', '8%', '5%'],
        ['Cadastro de produtos e feiras', 'Sim', 'Sim', 'Sim'],
        ['Divulgação na plataforma', 'Sim', 'Sim', 'Sim'],
        ['Conversas com clientes', 'Sim', 'Sim', 'Sim'],
        ['Financeiro', '—', 'Básico', 'Completo'],
        ['Xep.AI', '—', 'Sim', 'Sim'],
        ['Destaque de produtos e cestas', '—', '—', 'Sim'],
        ['Suporte pelo chat', '—', 'Sim', 'Prioritário'],
    ], [2, 1, 1, 1])
    d.h2('1.3 Simulação de comissão por venda')
    d.p('A tabela abaixo demonstra quanto o Xepa+ recebe em cada venda, sem considerar outros custos.')
    d.vazio()
    d.tabela(['Valor da venda', 'Semente – 15%', 'Broto – 8%', 'Colheita – 5%'], [
        ['R$ 10,00', 'R$ 1,50', 'R$ 0,80', 'R$ 0,50'], ['R$ 15,00', 'R$ 2,25', 'R$ 1,20', 'R$ 0,75'],
        ['R$ 20,00', 'R$ 3,00', 'R$ 1,60', 'R$ 1,00'], ['R$ 25,00', 'R$ 3,75', 'R$ 2,00', 'R$ 1,25'],
        ['R$ 30,00', 'R$ 4,50', 'R$ 2,40', 'R$ 1,50'], ['R$ 40,00', 'R$ 6,00', 'R$ 3,20', 'R$ 2,00'],
        ['R$ 50,00', 'R$ 7,50', 'R$ 4,00', 'R$ 2,50'],
    ])
    d.h2('1.4 Simulação mensal para o feirante')
    d.p('Considere um feirante que realiza R$ 1.000,00 em vendas mensais pelo Xepa+.')
    d.vazio()
    d.tabela(['Descrição', 'Semente', 'Broto', 'Colheita'], [
        ['Vendas mensais', 'R$ 1.000,00', 'R$ 1.000,00', 'R$ 1.000,00'],
        ['Mensalidade', 'R$ 0,00', 'R$ 29,90', 'R$ 59,90'],
        ['Comissão', 'R$ 150,00', 'R$ 80,00', 'R$ 50,00'],
        ['Custo total do Xepa+', 'R$ 150,00', 'R$ 109,90', 'R$ 109,90'],
        ['Valor restante', 'R$ 850,00', 'R$ 890,10', 'R$ 890,10'],
    ])
    d.lista(['Broto passa a ser mais barato que o Semente vendendo acima de R$ 427,14.',
             'Colheita passa a ser mais barato que o Semente vendendo acima de R$ 599,00.',
             'Colheita passa a ser mais barato que o Broto vendendo acima de R$ 1.000,00.'])

    d.h1('2. Estimativa de vendas e receita')
    d.p('A projeção financeira considera uma hipótese de 100 feirantes cadastrados, com vendas médias de R$ 1.000,00 por mês para cada feirante, distribuídos em 60% no plano Semente, 30% no Broto e 10% no Colheita.')
    d.vazio()
    d.tabela(['Plano', 'Vendas dos feirantes', 'Comissão', 'Receita de comissão', 'Receita de mensalidades', 'Receita mensal total'], [
        ['Semente', 'R$ 60.000,00', '15%', 'R$ 9.000,00', 'R$ 0,00', 'R$ 9.000,00'],
        ['Broto', 'R$ 30.000,00', '8%', 'R$ 2.400,00', 'R$ 897,00', 'R$ 3.297,00'],
        ['Colheita', 'R$ 10.000,00', '5%', 'R$ 500,00', 'R$ 599,00', 'R$ 1.099,00'],
        ['Total', 'R$ 100.000,00', '—', 'R$ 11.900,00', 'R$ 1.496,00', 'R$ 13.396,00'],
    ])
    d.p('O volume total de vendas (GMV) não corresponde à receita do Xepa+. A receita bruta estimada não representa lucro: ainda é necessário descontar os custos de tecnologia, suporte, marketing, impostos, taxas de pagamento, reembolsos e demais despesas operacionais.')

    d.h1('3. Custos de desenvolvimento')
    d.p('Atualmente, o desenvolvimento do Xepa+ está sendo realizado pela própria equipe do projeto, sem contratação externa. Para a continuidade, a evolução e a manutenção da plataforma no futuro, considera-se a contratação de uma equipe enxuta, com quatro profissionais.')
    d.vazio()
    d.tabela(['Cargo', 'Salário mensal', 'Salário 3 meses', 'Salário 1 ano'], [
        ['Gestor de Produto e Operações', 'R$ 5.000,00', 'R$ 15.000,00', 'R$ 60.000,00'],
        ['Desenvolvedor Full Stack Pleno (PJ)', 'R$ 6.200,00', 'R$ 18.600,00', 'R$ 74.400,00'],
        ['Estagiário de Marketing e Design', 'R$ 2.000,00', 'R$ 6.000,00', 'R$ 24.000,00'],
        ['Assistente de Atendimento e Operações', 'R$ 2.000,00', 'R$ 6.000,00', 'R$ 24.000,00'],
        ['Total mensal', 'R$ 15.200,00', 'R$ 45.600,00', 'R$ 182.400,00'],
    ], [2, 1, 1, 1])
    d.h2('3.1 Custos de manutenção')
    d.tabela(['Descrição', 'Custo mensal'], [
        ['Desenvolvimento inicial pela equipe', 'R$ 0,00'],
        ['Manutenção técnica', 'R$ 500,00'],
        ['Atendimento e operações', 'R$ 300,00'],
        ['Total mensal estimado', 'R$ 800,00'],
    ], [2, 1])

    d.h1('4. Custos de hospedagem e domínio')
    d.p('A hospedagem do Xepa+ será feita na Amazon Web Services (AWS), por meio do Amazon EC2, um servidor virtual na nuvem que fica ligado 24 horas por dia. Nele ficam a API em Java com Spring Boot, o banco de dados MySQL e o front-end em React. A cobrança é feita em dólar e só pelo que for usado.')
    d.vazio()
    d.tabela(['Item', 'Finalidade', 'Custo'], [
        ['Instância EC2 t3.small', 'Servidor da API em Java com Spring Boot e do banco de dados MySQL.', 'US$ 25,00/mês'],
        ['IP público (IPv4)', 'Endereço fixo de acesso ao servidor.', 'US$ 3,65/mês'],
        ['Disco EBS (30 GB)', 'Armazenamento do sistema, da aplicação e do banco de dados.', 'US$ 4,60/mês'],
        ['Backup (snapshots)', 'Cópias de segurança do disco.', 'US$ 2,00/mês'],
        ['Amazon S3', 'Armazenamento das fotos dos produtos.', 'US$ 1,00/mês'],
        ['Amazon CloudFront', 'Entrega rápida das fotos aos usuários.', 'Gratuito'],
        ['Amazon SES', 'Envio de e-mails da plataforma.', 'US$ 0,50/mês'],
        ['Amazon CloudWatch', 'Logs e alertas de funcionamento.', 'US$ 0 a 2,00/mês'],
        ['Tráfego de saída', 'Dados enviados aos usuários, dentro da faixa gratuita.', 'Gratuito'],
        ['Total AWS (base)', 'Valor considerado no orçamento do Xepa+ (cerca de US$ 37 a 40).', 'R$ 200,00/mês'],
    ], [2247, 4321, 1926])
    d.h2('4.1 Domínio e custo total')
    d.p('O domínio será comprado por meio do serviço de registro de domínio .com.br, pelo valor de R$ 40,00 por um ano, com possibilidade de renovação por períodos adicionais, conforme as condições do serviço.')
    d.vazio()
    d.tabela(['Período', 'Hospedagem (AWS)', 'Domínio', 'Total'], [
        ['Mensal', 'R$ 200,00', '—', 'R$ 200,00'],
        ['Anual', 'R$ 2.400,00', 'R$ 40,00', 'R$ 2.440,00'],
    ])
    d.p('Como a cobrança da AWS é feita em dólar, o valor mensal pode variar conforme o câmbio e o uso. Por isso, a equipe acompanhará os gastos pelo painel de custos da AWS, com alertas de orçamento.')
    d.h2('4.2 Ferramentas gratuitas para desenvolvimento')
    d.tabela(['Ferramenta', 'Utilização', 'Observações'], [
        ['Figma', 'Design de interfaces', 'Prototipação e design das interfaces antes do desenvolvimento.'],
        ['React', 'Interfaces do front-end', 'É necessário um ambiente para publicar a aplicação.'],
        ['Java/JDK', 'Back-end', 'Escolher distribuição e versão com licença adequada.'],
        ['Spring Boot', 'APIs e regras de negócio', 'Exige configuração, testes e execução no servidor.'],
        ['MySQL Community', 'Usuários, produtos e pedidos', 'Requer administração, segurança, atualizações e backups.'],
        ['Git e GitHub', 'Controle de versão e repositório', 'Não substitui a hospedagem de produção.'],
        ['API de mapas', 'Localização das feiras', 'Gratuita, conforme a opção de serviço utilizada.'],
    ], [1, 1.4, 2.4])

    d.h1('5. Marketing')
    d.p('A estratégia inicial de divulgação considera canais digitais e ações presenciais para alcançar feirantes e consumidores.')
    d.lista(['Redes sociais: Instagram, Facebook e TikTok para divulgar a plataforma, apresentar ofertas e publicar conteúdos sobre o aproveitamento de alimentos.',
             'Panfletos e cartazes: materiais impressos em feiras livres, com QR Code para a plataforma.',
             'Abordagem presencial: visitas às feiras para apresentar o projeto, demonstrar a plataforma pelo celular e ajudar no primeiro cadastro.'])
    d.vazio()
    d.tabela(['Item', 'Custo estimado mensal'], [
        ['Anúncios em redes sociais', 'R$ 165,00'], ['Canva Pro', 'R$ 35,00'], ['Panfletos e cartazes', 'R$ 150,00'],
        ['Deslocamentos', 'R$ 120,00'], ['Materiais diversos', 'R$ 50,00'], ['Total', 'R$ 520,00'],
    ], [2, 1])

    d.h1('6. Investimento necessário')
    d.h2('6.1 Cenário inicial: equipe própria')
    d.tabela(['Item', 'Mensal', '3 meses', '1 ano'], [
        ['Hospedagem (AWS)', 'R$ 200,00', 'R$ 600,00', 'R$ 2.400,00'],
        ['Domínio', '—', '—', 'R$ 40,00'],
        ['Marketing', 'R$ 520,00', 'R$ 1.560,00', 'R$ 6.240,00'],
        ['Manutenção e operações', 'R$ 800,00', 'R$ 2.400,00', 'R$ 9.600,00'],
        ['Desenvolvimento inicial', 'R$ 0,00', 'R$ 0,00', 'R$ 0,00'],
        ['Subtotal', 'R$ 1.520,00', 'R$ 4.560,00', 'R$ 18.280,00'],
        ['Reserva para imprevistos (10%)', 'R$ 152,00', 'R$ 456,00', 'R$ 1.828,00'],
        ['Total', 'R$ 1.672,00', 'R$ 5.016,00', 'R$ 20.108,00'],
    ], [2, 1, 1, 1])
    d.h2('6.2 Cenário com equipe contratada')
    d.tabela(['Item', 'Mensal', '3 meses', '1 ano'], [
        ['Hospedagem (AWS)', 'R$ 200,00', 'R$ 600,00', 'R$ 2.400,00'],
        ['Domínio', '—', '—', 'R$ 40,00'],
        ['Marketing', 'R$ 520,00', 'R$ 1.560,00', 'R$ 6.240,00'],
        ['Manutenção e operações', 'R$ 800,00', 'R$ 2.400,00', 'R$ 9.600,00'],
        ['Salários da equipe (4 profissionais)', 'R$ 15.200,00', 'R$ 45.600,00', 'R$ 182.400,00'],
        ['Subtotal', 'R$ 16.720,00', 'R$ 50.160,00', 'R$ 200.680,00'],
        ['Reserva para imprevistos (10%)', 'R$ 1.672,00', 'R$ 5.016,00', 'R$ 20.068,00'],
        ['Total', 'R$ 18.392,00', 'R$ 55.176,00', 'R$ 220.748,00'],
    ], [2, 1, 1, 1])
    d.p('O investimento definido para iniciar a operação é de R$ 20.108,00 no primeiro ano, sendo R$ 5.016,00 para os três primeiros meses de validação.')
    d.p('Com a equipe contratada, o custo anual é de R$ 220.748,00, distribuído entre desenvolvimento (33,7%), gestão (27,2%), atendimento e operações (15,2%), marketing e design (13,7%), reserva para imprevistos (9,1%) e infraestrutura na AWS (1,1%). Considerando a receita média de R$ 133,96 por feirante por mês (R$ 13.396,00 divididos por 100 feirantes), essa equipe passa a se pagar a partir de cerca de 138 feirantes ativos.')

    d.h1('7. Projeção financeira para 1, 5 e 10 anos')
    d.p('As projeções consideram vendas médias de R$ 1.000,00 por mês para cada feirante e a distribuição de 60% dos participantes no plano Semente, 30% no Broto e 10% no Colheita.')
    d.vazio()
    d.tabela(['Indicador', '1 ano', '5 anos', '10 anos'], [
        ['Feirantes cadastrados', '100', '1.000', '5.000'],
        ['Volume mensal de vendas (GMV)', 'R$ 100.000,00', 'R$ 1.000.000,00', 'R$ 5.000.000,00'],
        ['Receita bruta mensal estimada', 'R$ 13.396,00', 'R$ 133.960,00', 'R$ 669.800,00'],
        ['Receita bruta anual estimada', 'R$ 160.752,00', 'R$ 1.607.520,00', 'R$ 8.037.600,00'],
    ], [2, 1, 1, 1])
    d.h2('7.1 Receita bruta anual por plano')
    d.tabela(['Plano', '1 ano', '5 anos', '10 anos'], [
        ['Semente (60%)', 'R$ 108.000,00', 'R$ 1.080.000,00', 'R$ 5.400.000,00'],
        ['Broto (30%)', 'R$ 39.564,00', 'R$ 395.640,00', 'R$ 1.978.200,00'],
        ['Colheita (10%)', 'R$ 13.188,00', 'R$ 131.880,00', 'R$ 659.400,00'],
    ], [2, 1, 1, 1])
    d.h2('7.2 Metas de cada fase')
    d.tabela(['Fase', 'Lançamento', 'Crescimento', 'Expansão'], [
        ['Onde', 'Brasilândia e Freguesia do Ó', 'Cidade de São Paulo (2027)', 'Novos estados (até 2030)'],
        ['Meta 1', '10 feirantes ativos vendendo toda semana', '100 feirantes cadastrados', '1.000 feirantes até 2028 (regional)'],
        ['Meta 2', '30 pedidos concluídos no piloto', '138 feirantes: ponto de equilíbrio da equipe', '5.000 feirantes até 2030 (nacional)'],
        ['Meta 3', '90% dos pedidos retirados na barraca', 'R$ 13,4 mil de receita bruta por mês com 100 feirantes', 'R$ 8 mi de receita bruta por ano em 2030'],
    ], [0.8, 1.4, 1.4, 1.4])

    d.h1('8. Projeção de crescimento')
    d.p('O crescimento do Xepa+ está organizado em três horizontes, de 2027 a 2030: a consolidação em São Paulo, a expansão regional e a chegada às feiras livres de todo o Brasil.')
    d.h2('8.1 2027 – São Paulo')
    d.p('Meta: 100 feirantes cadastrados.')
    d.lista(['Iniciar a operação em São Paulo.', 'Desenvolver e validar a plataforma.',
             'Lançar o aplicativo Xepa+ para Android e iOS, levando as xepas da feira para a palma da mão.',
             'Estabelecer contato com feiras e feirantes.', 'Atrair os primeiros consumidores.',
             'Testar os planos de monetização.', 'Avaliar vendas, custos e satisfação dos usuários.'])
    d.h2('8.2 Até 2028 – expansão regional')
    d.p('Meta: 1.000 feirantes cadastrados.')
    d.lista(['Expandir para cidades próximas e outras regiões do estado de São Paulo.',
             'Ampliar o contato com associações e produtores.', 'Fortalecer as estratégias de marketing e retenção.',
             'Aprimorar relatórios e recursos de controle de estoque.', 'Fortalecer a equipe de tecnologia e suporte.'])
    d.h2('8.3 Até 2030 – expansão nacional')
    d.p('Meta: 5.000 feirantes cadastrados.')
    d.lista(['Levar o Xepa+ às feiras livres de outros estados brasileiros.', 'Atender capitais e outras cidades.',
             'Desenvolver parcerias em âmbito nacional.', 'Oferecer entrega por motoboy, levando as compras até a casa do cliente.',
             'Permitir que os feirantes vendam também seus produtos frescos, além das xepas.',
             'Tornar-se referência no aproveitamento de alimentos e no comércio de feiras.'])
    d.h2('8.4 Estratégias para alcançar as metas')
    d.tabela(['Área', 'Estratégia'], [
        ['Marketing', 'Utilizar redes sociais, feiras e comunidades locais.'],
        ['Relacionamento', 'Desenvolver contato com feirantes, associações e produtores.'],
        ['Tecnologia', 'Melhorar a plataforma com base nas necessidades dos usuários.'],
        ['Fidelização', 'Oferecer uma experiência simples, preços acessíveis e condições para compras recorrentes.'],
        ['Sustentabilidade', 'Acompanhar os alimentos comercializados que poderiam ser desperdiçados.'],
        ['Financeiro', 'Monitorar receitas, despesas, comissões e crescimento mensal.'],
    ], [1, 3])
    d.p('A expectativa é validar o modelo no primeiro ano, consolidar a operação regional em cinco anos e ampliar a atuação para outras regiões do país em dez anos. A expansão deverá ocorrer gradualmente, considerando os resultados, a capacidade tecnológica e a adesão de feirantes e consumidores.')
    return d


# =====================================================================
def doc08(D=Doc):
    d = D('Pesquisas')
    R = ['Resposta', 'Participantes']
    LR = [3, 1]

    d.h1('1. Pesquisa de mercado')
    d.p('Dados de fontes públicas mostram que o problema do desperdício de alimentos e do acesso a frutas, verduras e legumes não é isolado:')
    d.vazio()
    d.tabela(['Indicador', 'Dado', 'Fonte'], [
        ['Desperdício no mundo', '1,05 bilhão de toneladas de alimentos desperdiçadas em 2022, cerca de 19% do disponível ao consumidor.', 'UNEP (2024)'],
        ['Insegurança alimentar no Brasil', 'Cerca de 24% dos domicílios tinham algum grau de insegurança alimentar em 2024; 7,7% em nível moderado ou grave.', 'IBGE, PNAD Contínua (2025)'],
        ['Feiras livres em São Paulo', '975 feiras e mais de 12 mil feirantes, que movimentam cerca de R$ 2 bilhões por ano.', 'Prefeitura de São Paulo (2025)'],
        ['Desperdício nas feiras de SP', 'De 14,9 mil a 18,4 mil toneladas de resíduos comestíveis por ano.', 'Unesp e Universidade de Borås (2022)'],
        ['Região do piloto', '27 feiras livres na subprefeitura Freguesia/Brasilândia.', 'Lista oficial de feiras da Prefeitura'],
    ], [2247, 4321, 1926])

    d.h1('2. Pesquisa de campo')
    d.p('A pesquisa de campo foi realizada por meio de dois questionários on-line, um respondido por feirantes e outro pelo público geral, para entender as sobras no fim da feira, os hábitos de compra e o interesse na proposta do Xepa+. Os percentuais descrevem apenas quem respondeu: as amostras são pequenas e concentradas, portanto, não representam todos os feirantes e consumidores da cidade.')
    d.h2('2.1 Questionários aplicados')
    d.tabela(['Questionário', 'Link'], [
        ['Pesquisa com Feirantes', 'https://docs.google.com/forms/d/e/1FAIpQLScBpA0H-gxJ4zD2XmqOz_ab7Er4VnKzmdYcxqHZhlsvhKEkYQ/viewform | Formulário dos feirantes'],
        ['Pesquisa de Consumo e Hábitos de Compra', 'https://docs.google.com/forms/d/e/1FAIpQLSdDhmJwShsM5SFmZPVTlWPbm0Z6rWXmDHxJuD8IZ6asRmkGmA/viewform | Formulário dos consumidores'],
    ], [1.4, 2])
    d.tabela(['Pesquisa', 'Respostas', 'Perfil da amostra'], [
        ['Feirantes', '20', 'Quase todas da Zona Norte de São Paulo, com forte presença de feirantes experientes.'],
        ['Consumidores', '29', 'Concentração de pessoas jovens e residentes na Zona Sul de São Paulo.'],
    ], [1, 0.7, 3])

    d.h1('3. Pesquisa com feirantes')
    d.p('A amostra reúne 20 respostas, quase todas da Zona Norte de São Paulo, com forte presença de feirantes experientes. Os percentuais descrevem apenas quem respondeu ao formulário; não representam, por si só, todos os feirantes da cidade. Perguntas com múltiplas escolhas são contabilizadas por participante e podem somar mais de 100%.')
    d.p('As respostas apontam uma oportunidade para facilitar a venda dos produtos que restam ao final da feira. 19 de 20 participantes (95%) disseram que sobras ocorrem às vezes ou frequentemente. 8 demonstraram interesse direto em divulgar os produtos por uma plataforma digital, e outros 8 responderam “talvez, dependendo de como funciona”.')
    d.p('O principal obstáculo citado foi encontrar compradores no fim da feira. Reduzir preços, levar alimentos para casa e fazer doações aparecem como respostas práticas às sobras. As respostas condicionais sugerem que a adesão pode depender de uma proposta simples e de regras de funcionamento claras.')
    d.h2('3.1 Perfil da amostra')
    d.tabela(['Pergunta', 'Respostas'], [
        ['Faixa etária', '29 a 49 anos: 14 (70%)\n50 anos ou mais: 3 (15%)\n18 a 28 anos: 3 (15%)'],
        ['Tempo de trabalho como feirante', 'Mais de 10 anos: 18 (90%)\nDe 6 a 10 anos: 1 (5%)\nDe 1 a 5 anos: 1 (5%)'],
        ['Região de trabalho', 'Zona Norte (SP): 19 (95%)\nRegião Metropolitana (SP): 1 (5%)'],
    ], [1.4, 2])
    d.h2('3.2 Produtos mencionados')
    d.p('A pergunta permitia respostas com mais de um produto. Os itens foram contabilizados como menções individuais.')
    d.vazio()
    d.tabela(['Produto', 'Menções'], [
        ['Legumes', '7 (35%)'], ['Verduras', '6 (30%)'], ['Frutas', '4 (20%)'], ['Temperos', '3 (15%)'],
        ['Pastel', '2 (10%)'], ['Carne / Frango / Peixe', '1 (5%)'], ['Tapioca', '1 (5%)'],
    ], LR)
    d.h2('3.3 Frequência das sobras')
    d.tabela(R, [['Sim, às vezes', '13 (65%)'], ['Sim, frequentemente', '6 (30%)'], ['Raramente', '1 (5%)']], LR)
    d.h2('3.4 O que acontece com os alimentos que sobram')
    d.p('Pergunta de múltipla escolha; uma mesma pessoa podia selecionar mais de um destino.')
    d.vazio()
    d.tabela(R, [
        ['Faço doações', '9 (45%)'], ['Tento vender por um preço menor', '8 (40%)'], ['Levo para casa', '4 (20%)'],
        ['Utilizo de outra forma', '3 (15%)'],
        ['Como é pescados alguns doações e outros conseguimos o resfriamento para trabalhar dia seguinte', '1 (5%)'],
    ], LR)
    d.h2('3.5 Dificuldades para vender no final da feira')
    d.tabela(R, [
        ['Falta de compradores no final da feira', '10 (50%)'], ['Não tenho dificuldades', '5 (25%)'],
        ['Dificuldade para encontrar compradores interessados', '2 (10%)'], ['Pouco tempo para vender antes de encerrar', '2 (10%)'],
        ['Clientes não querem comprar os produtos no final da feira', '1 (5%)'], ['Os produtos estragam rapidamente', '1 (5%)'],
    ], LR)
    d.h2('3.6 Interesse em divulgar sobras por uma plataforma digital')
    d.tabela(['Resposta', 'Participantes', 'Leitura'], [
        ['Sim', '8 (40%)', 'Interesse declarado'],
        ['Talvez, dependendo de como funciona', '8 (40%)', 'Interesse condicionado à proposta'],
        ['Não', '4 (20%)', 'Sem interesse declarado'],
    ], [2, 1, 1.6])
    d.h2('3.7 O que as respostas sugerem')
    d.lista([
        'A comunicação precisa alcançar compradores que ainda não estão na banca no encerramento da feira.',
        'A agilidade importa: pouco tempo para vender e produtos que estragam foram citados como barreiras.',
        'O grupo que respondeu “talvez” quer entender como a ferramenta funcionaria. Vale explicar cadastro, atualização de disponibilidade, retirada e pagamento.',
        'As respostas mostram práticas variadas para as sobras: desconto, doação, consumo próprio e reaproveitamento. A plataforma pode complementar essas práticas.',
    ])
    d.h2('3.8 Respostas abertas: temas recorrentes')
    d.p('Nas justificativas sobre o que dificulta a venda, os participantes citaram falta de dinheiro entre consumidores, pouco tempo para comprar, preferência por produtos mais escolhidos e perda de qualidade dos produtos no fim da feira. São percepções individuais e foram resumidas sem alterar o sentido.')

    d.h1('4. Pesquisa com consumidores')
    d.p('A pesquisa reuniu 29 respostas. A amostra tem concentração de pessoas jovens e residentes na Zona Sul de São Paulo. Portanto, os resultados descrevem apenas os participantes e não devem ser generalizados para toda a cidade. Questões de múltipla escolha foram contabilizadas por menção de cada pessoa; suas porcentagens podem ultrapassar 100%.')
    d.p('A frequência às feiras está dividida: 15 participantes (52%) vão às vezes ou frequentemente, enquanto 14 (48%) vão raramente ou nunca. Supermercados e feiras aparecem juntos aos demais canais de compra, sugerindo que muitas pessoas alternam entre locais.')
    d.p('O preço pesa no acesso a frutas, verduras e legumes: 25 de 29 pessoas (86%) disseram que já deixaram de comprar esses alimentos por causa do preço, pelo menos algumas vezes. Ao mesmo tempo, 23 responderam “sim” e 6 “talvez, dependendo do preço” à possibilidade de comprar uma cesta de xepa mais acessível.')
    d.p('A oportunidade para o Xepa+ está em combinar preço atrativo com confiança na qualidade e frescor, além de tornar a compra e a retirada convenientes. A aceitação declarada é um sinal de interesse, ainda não uma comprovação de compra real.')
    d.h2('4.1 Perfil da amostra')
    d.tabela(['Pergunta', 'Respostas'], [
        ['Faixa etária', '18 a 28 anos: 14 (48%)\n29 a 49 anos: 10 (34%)\n50 anos ou mais: 5 (17%)'],
        ['Região de moradia', 'Zona Sul (SP): 16 (55%)\nZona Leste (SP): 4 (14%)\nZona Norte (SP): 4 (14%)\nZona Oeste (SP): 4 (14%)\nSalto SP: 1 (3%)'],
    ], [1.4, 2])
    d.h2('4.2 Frequência com que costuma ir a feiras livres')
    d.tabela(R, [['Raramente', '13 (45%)'], ['Sim, às vezes', '13 (45%)'], ['Sim, frequentemente', '2 (7%)'], ['Nunca', '1 (3%)']], LR)
    d.h2('4.3 Frequência de compra de frutas, verduras e legumes')
    d.tabela(R, [['Uma vez por semana', '13 (45%)'], ['Mais de uma vez por semana', '6 (21%)'], ['A cada 15 dias', '4 (14%)'],
                 ['Uma vez por mês', '4 (14%)'], ['Raramente', '2 (7%)']], LR)
    d.h2('4.4 Onde costumam comprar')
    d.p('Respostas de múltipla escolha; cada local foi contado por participante.')
    d.vazio()
    d.tabela(R, [['Supermercados', '17 (59%)'], ['Feiras livres', '14 (48%)'], ['Hortifrutis', '11 (38%)'],
                 ['Sacolões', '10 (34%)'], ['Mercados de bairro', '8 (28%)'], ['Não compro', '1 (3%)']], LR)
    d.h2('4.5 Fatores que influenciam a decisão de compra')
    d.p('Respostas de múltipla escolha.')
    d.vazio()
    d.tabela(R, [['Qualidade e frescor', '25 (86%)'], ['Preço', '20 (69%)'], ['Aparência dos alimentos', '16 (55%)'],
                 ['Promoções', '7 (24%)'], ['Variedade', '6 (21%)'], ['Praticidade', '4 (14%)'], ['Proximidade do local', '4 (14%)']], LR)
    d.h2('4.6 Já deixou de comprar hortifrúti por causa do preço?')
    d.tabela(R, [['Sim, algumas vezes', '18 (62%)'], ['Sim, frequentemente', '7 (24%)'], ['Raramente', '3 (10%)'], ['Nunca', '1 (3%)']], LR)
    d.h2('4.7 Compraria uma cesta de xepa por preço mais acessível?')
    d.tabela(R, [['Sim', '23 (79%)'], ['Talvez, dependendo do preço', '6 (21%)']], LR)
    d.p('Os 23 “sim” e 6 “talvez, dependendo do preço” indicam abertura para experimentar a proposta entre as pessoas que responderam. O preço é decisivo também para o grupo que respondeu “talvez”, então vale testar faixas de preço e tamanhos de cesta.')
    d.h2('4.8 Implicações práticas')
    d.lista([
        'Comunicar claramente a economia em relação ao preço usual.',
        'Informar conteúdo e condição dos produtos para sustentar confiança em qualidade e frescor.',
        'Facilitar localização, horário e retirada: falta de tempo e incompatibilidade de horários aparecem entre os motivos citados para não frequentar feiras.',
        'Testar a proposta com vendas-piloto e acompanhar conversão, preço aceito, composição preferida e recompra.',
    ])
    return d


# =====================================================================
MEMBROS = [
    ('Fernanda Ribeiro', 'Fernanda Ribeiro Pinto', 'Documentarista', 'Financeiro',
     'Área financeira da plataforma e desenvolvimento full stack. É responsável, junto com o Igor, pela hospedagem, pelas rotas, pelo domínio e pela integração entre o back-end e o front-end.',
     'f3rnandarib3iro@gmail.com', 'fernanda.rpinto@senacsp.edu.br', '(11) 99221-5045',
     'https://www.linkedin.com/in/f3f3h/', 'https://github.com/f3f3h'),
    ('Gabriel Carneiro', 'Gabriel Carneiro Sandes', 'Product Owner', 'Marketing',
     'Contato com os feirantes, visitas às feiras e gravação de conteúdo. Também atua no pitch e no desenvolvimento full stack.',
     'gabrielcarneiro780@gmail.com', 'gabriel.csandes@senacsp.edu.br', '(11) 95972-0652',
     'https://www.linkedin.com/in/gabriel-carneiro-5459b6303/', 'https://github.com/carneirogabri'),
    ('Hadson de Jesus', 'Hadson Ferreira de Jesus', 'Desenvolvedor', 'Vendas',
     'API de mapa das feiras e desenvolvimento full stack.',
     'fhadson@gmail.com', 'hadson.fjesus@senacsp.edu.br', '(11) 95630-8263',
     'https://www.linkedin.com/in/hadson-ferreira-068088271/', 'https://github.com/fhadson'),
    ('Henrique Mazza', 'Henrique Rodrigues Mazza do Valle', 'Desenvolvedor', 'IA',
     'Desenvolvimento da Xepinha, a assistente com inteligência artificial, e elaboração do banco de dados MySQL.',
     'henriquerodriguesmazza@gmail.com', 'henrique.rmvalle@senacsp.edu.br', '(11) 91350-3388',
     'https://www.linkedin.com/in/henriquemazzavalle/', None),
    ('Igor Aguiar', 'Igor Aguiar Rodrigues', 'Desenvolvedor', 'Dados',
     'Página de receitas e desenvolvimento full stack. É responsável, junto com a Fernanda, pela hospedagem, pelas rotas, pelo domínio e pela integração entre o back-end e o front-end.',
     'igoraguiar0101@gmail.com', 'igor.arodrigues3@senacsp.edu.br', '(11) 94642-0627',
     'https://www.linkedin.com/in/igor-aguiar-ab193132b/', 'https://github.com/Igordevice'),
    ('Jamilly Moreira', 'Jamilly Moreira de Jesus', 'Scrum Master', 'Vendas',
     'Organização do projeto, controle de prazos e distribuição das responsabilidades. Também apresenta o pitch.',
     'jamillymoreira963@gmail.com', 'jamilly.mjesus@senacsp.edu.br', '(11) 91351-3383',
     'https://www.linkedin.com/in/jamillymoreira/', 'https://github.com/milly-m-dev'),
    ('Matheus Barros', 'Matheus de Souza Barros', 'Desenvolvedor', 'Dados',
     'Dados e desenvolvimento full stack.',
     'sjmatheus07@gmail.com', 'matheus.sbarros14@senacsp.edu.br', '(11) 95069-7883',
     'https://www.linkedin.com/in/matheus-barros-13b652330/', 'https://github.com/MatheusSouzaBarros'),
    ('Murilo Verissimo', 'Murilo Verissimo Pereira', 'Desenvolvedor', 'Marketing',
     'Marketing e gestão do Instagram, além da elaboração do banco de dados MySQL.',
     'muriloverissimo2008@gmail.com', 'murilo.vpereira1@senacsp.edu.br', '(11) 98102-9405',
     'https://www.linkedin.com/in/murilo-verissimo-44a958372/', 'https://github.com/verissimoMuh'),
]


def doc07(D=Doc):
    d = D('Integrantes')
    d.h1('1. Equipe e divisão de responsabilidades')
    d.p('A equipe do Xepa+ é composta por oito integrantes, com funções relacionadas à organização do projeto, documentação, finanças, marketing, vendas, desenvolvimento, inteligência artificial e dados. Além das responsabilidades específicas, todos os integrantes participaram do desenvolvimento front-end utilizando React e Figma e da elaboração do pitch.')
    d.vazio()
    d.tabela(['Integrante', 'Cargo primário', 'Cargo secundário'],
             [[m[0], m[2], m[3]] for m in MEMBROS], [2, 1.5, 1.5])
    d.figura('equipe.png', 'Equipe do Xepa+', 140)

    d.h1('2. Informações dos integrantes')
    for i, m in enumerate(MEMBROS):
        nome, completo, c1, c2, resp, email, inst, tel, lin, git = m
        d.h2(nome, nova_pagina=(i > 0 and i % 2 == 0))  # 2 integrantes por página
        linhas = [
            ['Nome completo', completo],
            ['Cargo primário', c1],
            ['Cargo secundário', c2],
            ['Responsabilidades', resp],
            ['E-mail', f'mailto:{email}'],
            ['E-mail institucional', f'mailto:{inst}'],
            ['Telefone', tel],
            ['LinkedIn', lin],
        ]
        if git:
            linhas.append(['GitHub', git])
        d.tabela(['Campo', 'Informação'], linhas, [1, 3])
    return d


DOCS = [  # (arquivo, função, arquivo .md no repositório) — mesma ordem da pasta do Drive
    ('01-apresentacao-do-projeto', doc00, 'README.md'),
    ('02-integrantes', doc07, '02-integrantes.md'),
    ('03-links-do-projeto', doc05, '03-links-do-projeto.md'),
    ('04-identidade-visual', doc01, '04-identidade-visual.md'),
    ('05-pesquisas', doc08, '05-pesquisas.md'),
    ('06-proposta-de-valor-e-mercado', doc02, '06-proposta-de-valor-e-mercado.md'),
    ('07-jornada-do-usuario', doc04, '07-jornada-do-usuario.md'),
    ('08-financeiro', doc06, '08-financeiro.md'),
    ('09-tecnologias', doc03, '09-tecnologias.md'),
]


def _titulo(fn):
    return fn(MdDoc).titulo


def _documentacao():
    linhas = ['| Documento | Word | PDF |', '| :--- | :--- | :--- |']
    for i, (nome, fn, md) in enumerate(DOCS):
        doc = f'**{i + 1}. {_titulo(fn)}**' if md == 'README.md' else f'**{i + 1}.** [{_titulo(fn)}]({md})'
        linhas.append(f'| {doc} | [{nome}.docx](word/{nome}.docx) | [{nome}.pdf](pdf/{nome}.pdf) |')
    return '\n'.join(linhas)


def _rodape(i):
    links = []
    if i > 0:
        nome, fn, md = DOCS[i - 1]
        links.append(f'<a href="{md}">← {i}. {_titulo(fn)}</a>')
    if i < len(DOCS) - 1:
        nome, fn, md = DOCS[i + 1]
        links.append(f'<a href="{md}">{i + 2}. {_titulo(fn)} →</a>')
    return '<br>\n\n---\n\n<p align="center">' + ' · '.join(links) + '</p>'


if __name__ == '__main__':
    import sys
    filtro = sys.argv[1:]  # ex.: python gerar_documentos.py 05  (gera só os que começam com 05)
    for i, (nome, fn, md) in enumerate(DOCS):
        if filtro and not any(nome.startswith(f) for f in filtro):
            continue
        fn().salvar(os.path.join(OUT, nome + '.docx'))
        m = fn(MdDoc)
        if md == 'README.md':
            rodape = ('<br>\n\n# Documentação\n\nOs documentos seguem a mesma ordem da pasta do Drive. '
                      'Cada um tem versão em Markdown, Word e PDF.\n\n' + _documentacao() + '\n\n' + _rodape(i))
            texto = m.texto(titulo_visivel=False, rodape=rodape)
        else:
            texto = m.texto(rodape=_rodape(i))
        with open(os.path.join(RAIZ, md), 'w', encoding='utf-8', newline='\n') as f:
            f.write(texto)
        print('ok', nome)
