---
id: "360054073253"
titulo: "Nota (XXXX) referenciada no XML da devolução não foi encontrada no sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360054073253-Nota-XXXX-referenciada-no-XML-da-devolu%C3%A7%C3%A3o-n%C3%A3o-foi-encontrada-no-sistema"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T15:28:41Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "XML", "Importação", "TOP", "#formatadoroger", "CORE_E02899", "Problema na Importação de XML: Solução e Causa", "XML de devolução", "Erro"]
---

# Nota (XXXX) referenciada no XML da devolução não foi encontrada no sistema

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/15916195789463) MENSAGEM**:

[CORE\_E02899] Nota (XXXX) referenciada no XML da devolução não foi encontrada no sistema.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15916201794583) CAUSA:**

Quando o XML importado possui a tag **<refNFe>** preenchida com a chave de um documento que não se encontra lançado no sistema, será retornado a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15916201796375) SOLUÇÃO:**

Para realizar a importação de XML de notas que não possuem seu documento referenciado (tag **<refNFe>)** lançado no sistema, é necessário utilizar um 'Tipo de Operação' que possua a opção **'Desconsidera Nfe de orig. referenciada? (Importação de XML)'** MARCADA.

![Imagem 4: Acesse o cadastro da TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP):](https://ajuda.sankhya.com.br/hc/article_attachments/15916201798423) Acesse o cadastro da TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP):

- Aba: NF-e/NFC-e
- Opção: Desconsidera Nfe de orig. referenciada? (Importação de XML): = [marcado]

![Imagem 5: Opção: Desconsidera Nfe de orig. referenciada? (Importação de XML): = (marcado)](https://ajuda.sankhya.com.br/hc/article_attachments/15916149768599)

![Imagem 6: Após ajustado basta processar o arquivo novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/15916195800343) Após ajustado basta processar o arquivo novamente.
