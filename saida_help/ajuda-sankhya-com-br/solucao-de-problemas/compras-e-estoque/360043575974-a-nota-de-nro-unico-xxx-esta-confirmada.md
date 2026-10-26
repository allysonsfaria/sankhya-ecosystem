---
id: "360043575974"
titulo: "A nota de Nro. Único XXX está confirmada e não pode ser excluída pelo Portal de importação de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575974-A-nota-de-Nro-%C3%9Anico-XXX-est%C3%A1-confirmada-e-n%C3%A3o-pode-ser-exclu%C3%ADda-pelo-Portal-de-importa%C3%A7%C3%A3o-de-XML"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:14Z"
rotulos: ["CORE_E04305", "NF-e", "Portal de Vendas", "XML", "Importação", "NFS-e", "Erro ao Excluir Nota Confirmada", "Erro", "Artigo atualizado KCS", "CVE - KCS", "Docs Eletrônicos - KCS"]
---

# A nota de Nro. Único XXX está confirmada e não pode ser excluída pelo Portal de importação de XML

**MENSAGEM**

O sistema pode apresentar diferentes mensagens de erro ao tentar excluir uma nota fiscal:

- **"[CORE\_E04305] A nota de Nro. Único XXX está confirmada e não pode ser excluída pelo Portal de importação de XML".**
- **A nota é NFe/NFSe e não pode ser excluida, deve ser cancelada. (Emissão Própria).**

**SOLUÇÃO**

A solução varia conforme o tipo de vínculo que impede a exclusão:

**Cenário 1: Nota no Portal de Importação de XML**

**(1)** No **"Portal de Importação de XML"** (Comercial >> Portal de Importação de XML), selecione a opção **"Abrir Documento"** para o registro.

![Portal de importação](https://ajuda.sankhya.com.br/hc/article_attachments/14692241691543)
**(2)** Exclua o documento através da **"Central de Compras"** (Comercial >> Central de Compras).

**Cenário 2: Nota importada no Portal de Vendas (Emissão Própria).**

**(1)** Acesse a tela **"Portal de vendas"** (Comercial >> Consulta).
**(2)** As notas de **emissão própria** são inseridas no sistema já com o status **"Aprovada"**. Por esse motivo, elas não podem ser excluídas, apenas **canceladas**.

Para realizar o cancelamento, basta acessar o **Portal de Vendas**, selecionar a nota desejada e utilizar o **botão "Cancelar"**.

![Imagem 2: Para realizar o cancelamento, basta acessar o Portal de Vendas , selecionar a nota desejada e utilizar o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/41815319925271)

Obs.: Clicar no botão Doc > documentos relacionados. Se tiver documento relacionado precisa desvincular

**CAUSA**

Ao excluir um registro no **Portal de Importação de XML**, caso esse registro possua o **Nro. Único da Nota** informado, será apresentada uma mensagem questionando se deseja excluir também a nota vinculada. Caso o usuário opte por prosseguir e a nota ainda não esteja confirmada, ela será excluída. Caso contrário, a mensagem informativa será exibida.
