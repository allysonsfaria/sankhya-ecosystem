---
id: "32692165826455"
titulo: "O campo Utiliza U.M.A no cadastro de endereço não pode ser alterado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32692165826455-O-campo-Utiliza-U-M-A-no-cadastro-de-endere%C3%A7o-n%C3%A3o-pode-ser-alterado"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:30:45Z"
rotulos: ["Produtos", "Configuração", "WMS", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro"]
---

# O campo Utiliza U.M.A no cadastro de endereço não pode ser alterado

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32692165817623) **MENSAGEM:**

[CORE\_E07359] O campo Utiliza U.M.A no cadastro de endereço não pode ser alterado pois existe estoque registrado. Para alterá-lo é necessário que não haja estoque no endereço.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32692165818135)SOLUÇÃO:**

**Como verificar e alterar um endereço no WMS:**

**(1)**Acesse o caminho: WMS > Consultas > Estoque / Endereçamento WMS.

Filtre pelo endereço desejado, no campo Faixa de endereços, insira o CodEnd do endereço que deseja consultar.

**(2)** Verifique os produtos:
Confira quais produtos estão atualmente alocados nesse endereço.

**Caso precise alterar o endereço:**

**(3)** Realize a movimentação dos produtos:
Antes de alterar o endereço, é necessário remover os produtos dele, você pode fazer isso de duas formas:

**(1)** Pelo sistema:
WMS > Rotinas > Transferência entre Endereços

**(1)** Pelo coletor de dados:
Utilize a opção de transferência de endereço ou faça a movimentação proativa diretamente no equipamento.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32692165821335)CAUSA:**

Ocorre quando tentamos alterar a configuração de UMA de um endereço que já tem estoque de produtos cadastrado.
