---
id: "25370872910359"
titulo: "O valor do campo cProd informado não é valido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25370872910359-O-valor-do-campo-cProd-informado-n%C3%A3o-%C3%A9-valido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:45:54Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "CFOP", "O valor do campo cProd informado não é valido", "Erro"]
---

# O valor do campo cProd informado não é valido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25370872898839) **MENSAGEM:**

O valor do campo cProd (Código do produto ou serviço. Preencher com CFOP caso se trate de itens não relacionados com mercadorias/produto e que o contribuinte não possua codificação própria
Formato ”CFOP9999”.) informado não é valido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25370879765911)SOLUÇÃO:**

![Imagem 3: Como essa mensagem não traz o item com erro, habilite o parâmetro " Imprimir os XMLs processados pelo SanNFe no…](https://ajuda.sankhya.com.br/hc/article_attachments/25479204022167) Como essa mensagem não traz o item com erro, habilite o parâmetro "**Imprimir os XMLs processados pelo SanNFe no log?-DEBUGXML"** e analise o trecho DEBUG\_XML\_REQUEST do server log, que pode ser extraído da tela **administração do Servidor** (Configurações » Avançado » Administração do Servidor) , como mostrado na imagem abaixo.

![Imagem 4: Como essa mensagem não traz o item com erro, habilite o parâmetro " Imprimir os XMLs processados pelo SanNFe no…](https://ajuda.sankhya.com.br/hc/article_attachments/27904479869847)

![Imagem 5: Como essa mensagem não traz o item com erro, habilite o parâmetro " Imprimir os XMLs processados pelo SanNFe no…](https://ajuda.sankhya.com.br/hc/article_attachments/27904473941015)

![Imagem 6: Localizando o trecho que menciona o Cprod, verifique se a informação listada após a palavra Value existe no cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/25479204029079) Localizando o trecho que menciona o Cprod, verifique se a informação listada após a palavra Value existe no cadastro de produtos do sistema.

![Imagem 7: Abra o cadastro do produto e verifique no campo referência (mostrado abaixo com um exemplo de erro), se existe espaço…](https://ajuda.sankhya.com.br/hc/article_attachments/30091859652247) Abra o cadastro do produto e verifique no campo referência (mostrado abaixo com um exemplo de erro), se existe espaço em branco ou caracteres especiais a frente do código. Caso exista estes itens, faça a exclusão dos mesmos.

![Imagem 8: Abra o cadastro do produto e verifique no campo referência (mostrado abaixo com um exemplo de erro), se existe espaço…](https://ajuda.sankhya.com.br/hc/article_attachments/27904473947543)

![Imagem 9: Após o ajuste, redigite o item na Central e faça a geração do lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/25481771178519) Após o ajuste, redigite o item na Central e faça a geração do lote novamente.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25370879771415)CAUSA:**

Acontece quando é gerado no XML um valor inválido para o campo cProd, espaços em branco indevidos também podem causar essa rejeição.  Alguns exemplos de caracteres especiais que pode ajudar na análise.

Conforme Gif abaixo, se vê como que através do Notepad++ é possível fazer essa análise.  Utilize o filtro **[^0-9A-Za-z\t\n\r\<\>\|\$\?\ \"\=\:\/\-\+\%\@\\*\#\(\)\;\_,.]** dentro da opção 'Localizar', mencionando modo de pesquisa **'expressão regular'**:

[GIF animado: Imagem 11: Conforme Gif abaixo, se vê como que através do Notepad++ é possível fazer essa análise. Utilize o filtro…](https://ajuda.sankhya.com.br/hc/article_attachments/25370872908183)

Outros caracteres que podem ser identificados.

Todo conteúdo de um XML passa por uma análise do “parser” específico da linguagem. Alguns caracteres afetam o funcionamento deste “parser”, não podendo aparecer no texto de uma forma não controlada.

Os caracteres que afetam o “parser” são:

• > (sinal de maior),

• < (sinal de menor),

• & (e-comercial),

• “ (aspas),

• ‘ (sinal de apóstrofo).

**Observação:** importante verificar se o cliente não usa nenhum campo com referência personalizada para geração no XML, podendo gerar o erro também.
