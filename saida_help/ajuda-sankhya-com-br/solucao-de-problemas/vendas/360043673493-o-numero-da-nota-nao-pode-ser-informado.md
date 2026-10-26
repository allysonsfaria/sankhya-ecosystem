---
id: "360043673493"
titulo: "O número da nota não pode ser informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673493-O-n%C3%BAmero-da-nota-n%C3%A3o-pode-ser-informado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:39Z"
rotulos: ["Configuração", "NF-e", "Nota Fiscal", "TOP", "CORE_E01856", "Número de nota inválido", "Numeração automática ativada", "Ajuste a configuração ou deixe o campo em branco", "Erro"]
---

# O número da nota não pode ser informado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16143673758103) MENSAGEM:**

[CORE\_E01856]  O número da nota não pode ser informado.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16143673759895) SOLUÇÃO:**

A mensagem será apresentada quando inserido informações no campo **"Nro.Nota"** e a TOP utilizada configurada para **"Numeração automática"**.

![Imagem 3: Trata-se de um lançamento emissão própria, onde a sequência de numeração deverá ser gerada pelo sistema?](https://ajuda.sankhya.com.br/hc/article_attachments/16143673761943) Trata-se de um lançamento emissão própria, onde a sequência de numeração deverá ser gerada pelo sistema?

**(2)** Nesse caso apague a informação inserida em Nro.Nota, visto que esse número será preenchido automaticamente pelo sistema na confirmação.

![Imagem 4: Trata-se de um lançamento de terceiros, onde o Nro.Nota deverá ser preenchido conforme nota enviada pelo parceiro?](https://ajuda.sankhya.com.br/hc/article_attachments/16143673768599) Trata-se de um lançamento de terceiros, onde o Nro.Nota deverá ser preenchido conforme nota enviada pelo parceiro?

**(2)** Nesse caso, sintonize com o implantador da empresa, se está sendo utilizado o 'Tipo de Operação' correto. Em caso positivo, reporte ao mesmo a necessidade de ajuste do campo abaixo, para que o sistema permita a inserção de informações para Nro.Nota:

Tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho de acesso: Comercial » Arquivo » Cadastros), aba **"Impressão"**, campo "**Numeração somente automática":** desmarcado:

![Imagem 5: Tela " Tipos de Operação - TOP " (Caminho de acesso: Comercial » Arquivo » Cadastros) , aba "Impressão" , campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/14662400399127)

![Imagem 6: Realizado o ajuste acima, feche a Central e realize um novo lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16143666280855) Realizado o ajuste acima, feche a Central e realize um novo lançamento.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16143666282263) CAUSA:**

A mensagem será apresentada quando inserido informações no campo Nro.Nota e a TOP utilizada está configurada para Numeração automática.
