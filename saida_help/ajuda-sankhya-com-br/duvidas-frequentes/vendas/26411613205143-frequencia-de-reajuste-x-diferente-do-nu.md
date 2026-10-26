---
id: "26411613205143"
titulo: "Frequência de reajuste (X) diferente do número de índices (Y) encontrados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26411613205143-Frequ%C3%AAncia-de-reajuste-X-diferente-do-n%C3%BAmero-de-%C3%ADndices-Y-encontrados"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:42:11Z"
rotulos: ["Configuração", "Fiscal", "Contrato", "Moeda", "Passos para resolver", "Razão do erro", "Detalhe do erro", "SVC_E01016", "Frequência de reajuste (X) diferente do número de índices (Y) encontrados", "Erro"]
---

# Frequência de reajuste (X) diferente do número de índices (Y) encontrados

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26411598503575) **MENSAGEM:**

[SVC\_E01016] Frequência de reajuste (X) diferente do número de índices (Y) encontrados

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26440278210071) **SITUAÇÃO:**

Ao realizar um reajuste pela tela **"[Reajuste de Contratos Ativos"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113573-Reajuste-de-Contratos-Ativos)** (Caminho: Contratos e Serviços » Rotinas » Reajuste de Contratos Ativos) é exibido o erro citado acima

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26411598505239)SOLUÇÃO:**

O erro é apresentado pois o sistema não encontra os índices de acordo com a frequência de reajuste do contrato. Veja abaixo o passo a passo para solução:

![Imagem 4: Acesse a tela 'Configurações » Cadastros » Valores de Moedas' e filtre pela mesma moeda usada no contrato em questão;](https://ajuda.sankhya.com.br/hc/article_attachments/26411598507287) Acesse a tela 'Configurações » Cadastros » Valores de Moedas' e filtre pela mesma moeda usada no contrato em questão;

![Imagem 5: Acesse a aba "Cotação de Moeda" e verifique se o número de índices bate com o número de frequência do contrato.](https://ajuda.sankhya.com.br/hc/article_attachments/26411598509207) Acesse a aba **"Cotação de Moeda"** e verifique se o número de índices bate com o número de frequência do contrato.

Segue abaixo um exemplo:

Estamos no mês de setembro de 2024 e o contrato ativo possui a frequência de 12 meses. Na tela **"Valores de Moedas"** existe o cadastro de índices apenas até dezembro de 2023. Neste caso, o sistema apresenta a mensagem ("Frequência de reajuste (12) diferente do número de índices (4) encontrados") ao tentar reajustar, sendo necessário o cadastro dos 8 índices restantes de 2024.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26411613192727)CAUSA:**

O erro é apresentado pois o sistema não encontra os índices de acordo com a frequência de reajuste do contrato.
