---
id: "39353397688215"
titulo: "Erro de Estoque Insuficiente ao Faturar Pedido de Venda."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353397688215-Erro-de-Estoque-Insuficiente-ao-Faturar-Pedido-de-Venda"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-08-01T01:24:53Z"
rotulos: ["Configuração", "Faturamento", "TOP", "Vendas", "Estoque", "Erro", "Artigo criado KCS", "CVE - KCS", "Comercial"]
---

# Erro de Estoque Insuficiente ao Faturar Pedido de Venda.

**MENSAGEM**

Estoque insuficiente para o produto XXX no local XXX

**SITUAÇÃO**

Ao tentar faturar um pedido de venda já conferido, o sistema apresenta mensagem de estoque insuficiente, mesmo quando há saldo físico disponível. Esta situação ocorre frequentemente quando:

- O pedido utiliza reserva de estoque
- A **"TOP"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) está configurada para adiar atualização de estoque
- Há produtos com controle de lote na conferência
- O estoque disponível está negativo devido a excesso de reservas

**SOLUÇÃO**

Para resolver o erro de estoque insuficiente, siga os passos abaixo:

**(1)**  Verifique o saldo real do produto acessando a tela **"Gerência de Produtos"** (Comercial Consultas Gerência de Produtos). Confirme se há estoque físico disponível no local indicado na mensagem de erro.

**(2)**  Verifique as configurações da **"TOP"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) do pedido de venda. Certifique-se de que:

- A opção **"Reserva de Estoque"** está configurada adequadamente
- A opção **"Detalhamento de Lote na Conferência"** está compatível com o controle de lote dos produtos
- A configuração de **"Atualização de Estoque"** não está em conflito com a conferência

**(3)**  Se o produto possui controle de lote, verifique se os lotes foram informados corretamente na conferência do pedido. Acesse o pedido de venda e confirme se os lotes estão devidamente apontados.

**(4)**  Verifique se há excesso de reservas que estejam comprometendo o estoque disponível. Acesse **"Consulta de Reservas"** (Comercial Consultas Consulta de Reservas) e analise as reservas ativas para o produto em questão.

 **(5)** Caso utilize a funcionalidade **"Faturar pelo Estoque"** no **"Portal de Vendas"** (Comercial Portal de Vendas), verifique se a configuração da **"Nota Fiscal"** está definida para atualizar o estoque apenas após confirmação. Esta funcionalidade deve desconsiderar a reserva e validar apenas o saldo físico.

**(6)** Se necessário, realize um ajuste de estoque para corrigir divergências entre o saldo físico e o saldo no sistema. Utilize uma TOP de ajuste, devidamente configurada para a ação.

**Obs: Sempre utilize a base de homologação para realizar as correções, e posteriormente replique para produção, isso evita divergências e cenários não previstos.**
