---
id: "39320482743191"
titulo: "Erro ao realizar transferência de imobilizado pelo Portal de Movimentação Interna"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39320482743191-Erro-ao-realizar-transfer%C3%AAncia-de-imobilizado-pelo-Portal-de-Movimenta%C3%A7%C3%A3o-Interna"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T13:56:02Z"
rotulos: ["Produtos", "Configuração", "Imobilizado", "TOP", "Erro", "Artigo criado KCS", "Fiscal/Contábil - KCS"]
---

# Erro ao realizar transferência de imobilizado pelo Portal de Movimentação Interna

**Mensagem**

Produto: XX – Divergência na quantidade de bens informada.

Ao realizar a transferência de um produto imobilizado, o sistema identificou que a quantidade de bens vinculados é diferente da quantidade de itens da nota.

**Situação**

Ao acessar o **Portal de Movimentação Interna** (**Comercial » Consulta » Portal de Movimentação Interna**) e realizar a **Transferência de Bens** de um produto imobilizado, o sistema apresenta a mensagem **"Produto: XX – Divergência na quantidade de bens informada"**.

Esse comportamento ocorre quando um ou mais produtos imobilizados da nota não possuem um bem cadastrado ou não estão devidamente vinculados na **Central de Movimentações Internas** (**Comercial » Consulta » Central de Movimentações Internas**).

**Causa**

A inconsistência ocorre quando a **TOP** utilizada está configurada com a opção **"Atualizar Bem"** habilitada e existem itens imobilizados na nota sem um bem cadastrado ou vinculado.

Como a transferência de imobilizados depende da correspondência entre a quantidade de itens da nota e a quantidade de bens vinculados, o sistema interrompe o processo e apresenta a divergência quando essa correspondência não é atendida.

**Solução**

Verifique se os itens da nota possuem bens cadastrados e vinculados corretamente.

**Caso o item já tenha o bem cadastrado:**

**(1)** Acesse a **Central de Movimentações Internas**.
**(2)** Abra a nota que apresenta a inconsistência.
**(3)** Selecione o item imobilizado que está sem o bem vinculado.
**(4)** Clique em **Outras Opções**.
**(5)** Selecione **Transferência de Bens**.
**(6)** Clique em **Adicionar**.
**(7)** Localize e selecione o bem correspondente ao produto.
**(8)** Clique em **Salvar**.

**Caso o bem ainda não esteja cadastrado:**

**(1)** Acesse **Configurações » Cadastros » Produtos » Produtos**.
**(2)** Localize o produto imobilizado.
**(3)** Acesse a aba **"Bens"**.
**(4)** Na sub aba **Bens**, clique em **Adicionar**.
**(5)** Cadastre o bem, informando os dados necessários, como o código e a empresa de origem.
**(6)** Clique em **Salvar**.
**(7)** Retorne à **Central de Movimentações Internas**.
**(8)** Vincule o bem recém-cadastrado ao item da nota utilizando a opção **Transferência de Bens**.

**Importante:** A quantidade de bens vinculados deve ser exatamente igual à quantidade de produtos imobilizados da nota. Caso exista qualquer divergência, a transferência não será concluída.
