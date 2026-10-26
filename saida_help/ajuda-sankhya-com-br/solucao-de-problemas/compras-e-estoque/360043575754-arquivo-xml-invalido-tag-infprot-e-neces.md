---
id: "360043575754"
titulo: "Arquivo: '.xml' inválido, tag infProt é necessário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575754-Arquivo-xml-inv%C3%A1lido-tag-infProt-%C3%A9-necess%C3%A1rio"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:20Z"
rotulos: ["#PUBLIFER", "CORE_E03192", "NF-e", "Portal de Vendas", "XML", "Importação", "SEFAZ", "Erro em Arquivo XML", "Erro"]
---

# Arquivo: '.xml' inválido, tag infProt é necessário

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16173018521111) MENSAGEM:**

[CORE\_E03192]  Arquivo: '.xml' inválido, tag infProt é necessário.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16173002023831) SOLUÇÃO:**

![Imagem 3: Situação pode ocorrer quando o arquivo XML está sendo gerado em conferência.](https://ajuda.sankhya.com.br/hc/article_attachments/16173002027159) Situação pode ocorrer quando o arquivo XML está sendo gerado em conferência.

Em nosso sistema, essa geração ocorre no caminho:

- Portal de Vendas » NF-e » Gerar XML NF-e em arquivo para conferência

![Imagem 4: Portal de Vendas » NF-e » Gerar XML NF-e em arquivo para conferência](https://ajuda.sankhya.com.br/hc/article_attachments/14690149718679)

![Imagem 5: O XML gerado conforme item 1 não gera as informações da tag <infProt>, visto que não recebeu os protocolos de aprovação…](https://ajuda.sankhya.com.br/hc/article_attachments/16173018533143) O XML gerado conforme item 1 não gera as informações da tag <infProt>, visto que não recebeu os protocolos de aprovação da SEFAZ.

Dessa forma, utilize uma das opções abaixo para geração desse arquivo:

- Portal de Vendas » NF-e » Gerar Arquivo XML de NF-e

![Imagem 6: Portal de Vendas » NF-e » Gerar Arquivo XML de NF-e](https://ajuda.sankhya.com.br/hc/article_attachments/14690174972567)

- Tela **"Gerar Arquivo XML de NFe/NFSe/SAT"** (Caminho de acesso: Comercial » Rotinas » Gerar Arquivo XML de NF-e/NFS-e/SAT)

![Imagem 7: Tela "Gerar Arquivo XML de NFe/NFSe/SAT" (Caminho de acesso: Comercial » Rotinas » Gerar Arquivo XML de NF-e/NFS-e/SAT )](https://ajuda.sankhya.com.br/hc/article_attachments/14690158241175)

![Imagem 8: Caso o XML não tenha sido gerado em nosso sistema, solicite ao seu parceiro que refaça a geração, enviando um XML…](https://ajuda.sankhya.com.br/hc/article_attachments/16173002033047) Caso o XML não tenha sido gerado em nosso sistema, solicite ao seu parceiro que refaça a geração, enviando um XML válido, constando informações referente tag mencionada.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16173018539031) CAUSA:**

Ao realizar importação de XML, quando esse não contém a tag <infProt>, a mensagem é apresentada.
