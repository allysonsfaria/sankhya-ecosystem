---
id: "10464995777047"
titulo: "Tipo de Operação(TOP) do modelo de Pedido/Nota não pode usar configuração de impressão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10464995777047-Tipo-de-Opera%C3%A7%C3%A3o-TOP-do-modelo-de-Pedido-Nota-n%C3%A3o-pode-usar-configura%C3%A7%C3%A3o-de-impress%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-13T20:41:39Z"
rotulos: ["Configuração", "Impressão", "NF-e", "TOP", "SVC_E00473", "Resolução de Erro de Impressão em Tipo de Operação", "Erro"]
---

# Tipo de Operação(TOP) do modelo de Pedido/Nota não pode usar configuração de impressão

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18954973425175) MENSAGEM:**

[SVC\_E00473] Tipo de Operação(TOP) do modelo de Pedido/Nota não pode usar configuração de impressão.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18954978773527) SITUAÇÃO:**

Ao tentar confirmar o lançamento a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18954978777239)SOLUÇÃO:**

Verifique a configuração do campo "Imprimir", no cadastro da TOP utilizada no lançamento. Para isso, acesse a tela **Tipo de Operação TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

![Imagem 4: Verifique a configuração do campo "Imprimir", no cadastro da TOP utilizada no lançamento. Para isso, acesse a tela Tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/10464943068183)

![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/18954973438231) **IMPORTANTE:**

A opção **"Imprimir"** serve para indicar se a TOP irá ou não efetuar impressão da nota e esse campo pode ser preenchido com as seguintes opções:

- **Na Confirmação:** a impressão da nota será impressa quando efetuar a confirmação da nota nos Portais, clicando no botão Confirmar;
- **Manual:** após selecionar a nota a ser impressa, a impressão da nota será efetuada ao acionar o botão Imprimir;
- **Opcional:** o usuário será questionado se a nota será ou não impressa no momento da confirmação da nota;
- **Proibida:** a nota não será impressa. Nos Portais, se solicitar a impressão da nota o sistema emite o aviso: Documento (Número da Nota): TOP proíbe impressão de Nota/Pedido.

Ao preencher o campo **'Imprimir',** caso tenha escolhido as opções: 'Na confirmação', 'Manual' ou 'Opcional', logo em seguida, clique em 'Outras opções' e informe ou configure um controle de numeração.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18954978792343)CAUSA:**

Ocorre quando a TOP não permite impressão.
