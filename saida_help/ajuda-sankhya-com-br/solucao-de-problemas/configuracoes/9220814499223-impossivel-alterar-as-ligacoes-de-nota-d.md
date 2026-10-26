---
id: "9220814499223"
titulo: "Impossível alterar as ligações de nota de devolução aprovada/confirmada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9220814499223-Imposs%C3%ADvel-alterar-as-liga%C3%A7%C3%B5es-de-nota-de-devolu%C3%A7%C3%A3o-aprovada-confirmada"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:19Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Devolução", "CORE_E02731", "NFS-e", "Restrição em Alterar Ligações de Notas", "Erro"]
---

# Impossível alterar as ligações de nota de devolução aprovada/confirmada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19067770723095) MENSAGEM:**

[CORE\_E02731] Impossível alterar as ligações de nota de devolução aprovada/confirmada.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19067757166871) SITUAÇÃO:**

Ao tentar fazer a ligação de nota de devolução com a nota de venda através da opção "Documentos relacionados" na grade de itens do portal.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19067770744983) CAUSA:**

Sempre que o usuário tentar inserir um novo item no pop-up de documentos relacionados (TGFVAR) na Central o sistema faz uma validação e caso não entre na regra do sistema a mensagem é apresentada.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19067770753815) SOLUÇÃO:**

Para resolução desse erro devem ser feitas as validações para o pop-up de Documentos Relacionados.

Sempre que o usuário tentar inserir um novo item no pop-up de documentos, relacionados (TGFVAR) na Central, é executada uma regra e somente por meio da validação desta é que será possível efetivar o comando. Caso as informações presentes não obedeçam a regra, a mensagem de erro é apresentada. Vale destacar que essa regra verifica: 

- Se o tipo do documento é uma Devolução de Venda ou uma Devolução de Compra;
- Se é uma NF-e Aprovada ou uma NFS-e Aprovada ou não é uma NF-e confirmada.

Assim, faça a verificação dos dados e observe se eles obedecem a regra do tipo de documento e da NF. Para tal, confira abaixo com detalhes, um checklist das características de cada tipo de NF avaliados pela regra e faça suas validações:

**#O que quer dizer NF-e Aprovada:**
- Campo NF-e da TOP igual a (N - Normal, C - Complementar, A - Ajuste, D - Devolução)
- Campo NF-e na empresa deve ser diferente de 0, ou seja, igual a 1 - Produção ou 2 - Homologação
- Campo Modelo de Documento da TOP igual a 55-Nota Fiscal Eletrônica ou 65-Nota Fiscal Eletrônica de Venda a Consumidor
- Campo Status NF-e da nota igual a A - Aprovada

**#O que quer dizer NFS-e Aprovada:**
- Campo NFS-e da TOP igual a N - Normal
- Campo NFS-e na empresa deve ser igual a 1 - Produção ou 2 - Homologação
- Campo Status NFS-e da nota igual a A - Aprovada

**#O que quer dizer uma Não NF-e confirmada:**
Não é uma NF-e, ou seja:

- O campo NF-e da TOP é diferente de (N - Normal, C - Complementar, A - Ajuste, D - Devolução) **OU;**
- Campo NF-e na empresa é diferente de 1 - Produção e de 2 - Homologação **OU;**
- Campo Modelo de Documento da TOP é diferente de 55-Nota Fiscal Eletrônica e de 65-Nota Fiscal
Eletrônica de Venda a Consumidor **E;**
Não é uma NFS-e, ou seja:
- Campo NFS-e da TOP é diferente de N - Normal **OU;**
- Campo NFS-e na empresa é diferente de 1 - Produção e de 2 - Homologação **E;**
- Status da nota é igual a L - Confirmada.
