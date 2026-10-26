---
id: "16252269468695"
titulo: "Erro 130 - É necessário existir informação cadastral do empregador para o período"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16252269468695-Erro-130-%C3%89-necess%C3%A1rio-existir-informa%C3%A7%C3%A3o-cadastral-do-empregador-para-o-per%C3%ADodo"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:17:29Z"
rotulos: ["Configuração", "Eventos", "Fiscal", "eSocial", "Central do eSocial", "Preencher data de início válida", "Envio sem data correta", "Falta de informação cadastral", "Erro"]
---

# Erro 130 - É necessário existir informação cadastral do empregador para o período

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16252282924055)  MENSAGEM:**

Erro 130 - É necessário existir informação cadastral do empregador para o período.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16503748323223) SITUAÇÃO:**

Erro ao enviar o S-1005 de uma empresa nova.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16503712599703) SOLUÇÃO:**

Necessário antes de liberar o evento para transmissão, clicar em cima do evento S-1005 e preencher o campo "Início Validade" (ou atalho CTRL + SHIFT + F9 abre pop-up para preencher a data).

**MGE**

Pode preencher  com a validade vigente da referência, exemplo 01/07/2023. Depois liberar o evento para transmissão e o evento será enviado com sucesso.

![Imagem 4: MGE Pode preencher com a validade vigente da referência, exemplo 01/07/2023. Depois liberar o evento para transmissão e…](https://ajuda.sankhya.com.br/hc/article_attachments/16424239329687)

**Pessoal +**

Acesse a Central do eSocial e realize uma nova geração dos eventos
Antes de liberar para envio, desmarque a opção de "Utilizar a data de início padrão do sistema".

![Imagem 5: Acesse a Central do eSocial e realize uma nova geração dos eventos Antes de liberar para envio, desmarque a opção de…](https://ajuda.sankhya.com.br/hc/article_attachments/16676355286807)

Após isso clique para enviar dados
Será aberto um pop-up para preenchimento da data
Preencha com a data da referência atual a qual seu novo evento terá validade e envie.

![Imagem 6: Após isso clique para enviar dados Será aberto um pop-up para preenchimento da data Preencha com a data da referência…](https://ajuda.sankhya.com.br/hc/article_attachments/16676362165399)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16252278288663) CAUSA:**

Como se trata de uma filial, tem que enviar com data de validade de acordo com a vigência da empresa.
