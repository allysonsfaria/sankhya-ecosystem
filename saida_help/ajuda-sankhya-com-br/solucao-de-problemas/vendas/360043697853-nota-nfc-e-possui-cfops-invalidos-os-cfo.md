---
id: "360043697853"
titulo: "Nota NFC-e possui CFOPs inválidos. Os CFOPs válidos são (5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043697853-Nota-NFC-e-possui-CFOPs-inv%C3%A1lidos-Os-CFOPs-v%C3%A1lidos-s%C3%A3o-5101-5102-5115-5401-5403-5405-5656-5933"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:42Z"
rotulos: ["#criadoRoger", "CORE_E02536", "Configuração", "SEFAZ", "TOP", "CFOP", "CORE_E02526", "NFC-e com CFOP inválido", "Modelo 65 apenas para saídas estaduais", "Use NF-e (modelo 55) para operações interestaduais", "Erro"]
---

# Nota NFC-e possui CFOPs inválidos. Os CFOPs válidos são (5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16163328536343) MENSAGEM:**

[CORE\_E02526] Nota NFC-e possui CFOPs inválidos os cfops validos são 5101 5102 5103 5104 5115 5405 5456 5667 5933

[CORE\_E02536] Nota NFC-e possui CFOPs inválidos. Os CFOPs válidos são (5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16163328539671) SOLUÇÃO:**

![Imagem 3: Caso trate-se de "entrada" de uma nota, a inclusão de um documento com Modelo 65 não será aceita:](https://ajuda.sankhya.com.br/hc/article_attachments/16163328553495) Caso trate-se de "entrada" de uma nota, a inclusão de um documento com Modelo 65 não será aceita:

**(2)** O modelo 65 - Nota Fiscal Eletrônica de Venda a Consumidor é **específico e exclusivo para saída de mercadoria para uso e consumo**. Esse modelo não é contemplado para escrituração da entrada na nota fiscal destinada a uso e consumo. O sistema validará qualquer inclusão a partir do lançamento no qual será informado o modelo, mesmo marcando a opção para não atualizar Livro Fiscal.

**(2)** Para que o sistema confirme o lançamento desse documento deverá ser o modelo 01 ou 55 para obtê-lo em seu Controle Gerencial. Sugerimos que seja solicitado ao fornecedor uma nota fiscal eletrônica (modelo 55).

![Imagem 4: Para notas de saída, atente-se primeiramente na utilização de um parceiro com endereço com a mesma UF (Estado) da…](https://ajuda.sankhya.com.br/hc/article_attachments/16163343248279) Para notas de saída, atente-se primeiramente na utilização de um parceiro com endereço com a mesma UF (Estado) da Empresa Emitente.

**(2)** Em Operações acobertadas por NFC-e, é **permitido apenas que sejam Estaduais** (idDest = 1). Para Operações Interestaduais ou com o Exterior, opte pela emissão de uma NF-e (modelo 55). Para corrigir a NFC-e, deve-se informar a Operação como Estadual.

![Imagem 5: Caso não trate-se de uma operação Estadual, sintonize com o contador e avalie a possibilidade de emissão de uma NF-e…](https://ajuda.sankhya.com.br/hc/article_attachments/16163343250199) Caso não trate-se de uma operação Estadual, sintonize com o contador e avalie a possibilidade de emissão de uma NF-e (Modelo 55).

![Imagem 6: Se tratar-se de uma NFC-e, certifique-se que as configurações de CFOP foram realizadas corretamente:](https://ajuda.sankhya.com.br/hc/article_attachments/16163343265943) Se tratar-se de uma NFC-e, certifique-se que as configurações de CFOP foram realizadas corretamente:

**(2)** Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba: **"Livro Fiscal"**, campo **"CFOP's para Dentro do Estado":** CFOP'S iniciadas com 5.

![Imagem 7: (2) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba: "Livro Fiscal" , campo "CFOP's para Dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/14707160938647)

![Imagem 8: Se necessário ajustes na TOP, inutilize a NFC-e rejeitada e proceda com uma nova emissão.](https://ajuda.sankhya.com.br/hc/article_attachments/16163328568599) Se necessário ajustes na TOP, inutilize a NFC-e rejeitada e proceda com uma nova emissão.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16163343273623) CAUSA:**

Ao emitir e/ou lançar no sistema notas fiscal com modelo do documento 65 a mensagem poderá ser apresentada se o CFOP utilizado for diferente de: 5101, 5102, 5115, 5401, 5403, 5405, 5656, 5933.
