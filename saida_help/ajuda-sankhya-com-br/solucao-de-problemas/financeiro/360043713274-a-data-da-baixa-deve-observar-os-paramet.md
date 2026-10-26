---
id: "360043713274"
titulo: "A data da baixa deve observar os parâmetros de \"Dias para Retroação\" e \"Dias para Lançamentos Futuros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043713274-A-data-da-baixa-deve-observar-os-par%C3%A2metros-de-Dias-para-Retroa%C3%A7%C3%A3o-e-Dias-para-Lan%C3%A7amentos-Futuros"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:39Z"
rotulos: ["#PUBLIFER", "Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "Retroação e Futuro", "Ajuste Parâmetros Usuário", "Correção Data Baixa"]
---

# A data da baixa deve observar os parâmetros de "Dias para Retroação" e "Dias para Lançamentos Futuros

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16199845186327) MENSAGEM:**

A data da baixa deve observar os parâmetros de "Dias para Retroação" e "Dias para Lançamentos Futuros.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199872002071) SITUAÇÃO:**

Ao tentar realizar baixa/estorno de títulos com data retroativa ou futura, a mensagem abaixo é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16199845190807) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Configurações » Controle de Acesso » Usuários :](https://ajuda.sankhya.com.br/hc/article_attachments/16199845191703) Acesse: Configurações » Controle de Acesso » Usuários:

- Selecione o usuário responsável pela baixa.
- Botão: **"Outras Opções"**, opção **"Configurações Usuário"**

![Imagem 5: Botão: "Outras Opções" , opção "Configurações Usuário"](https://ajuda.sankhya.com.br/hc/article_attachments/14613195984407)

- Campo **"Dias para retroação da baixa":** altere o valor deste campo
- Campo **"Dias para lançamentos futuros":** altere o valor deste campo

![Imagem 6: Campo "Dias para lançamentos futuros": altere o valor deste campo](https://ajuda.sankhya.com.br/hc/article_attachments/14613258209943)

(1)** EXEMPLO:**

- No dia 28/03/19 o usuário 'FRANQUIA' precisa realizar a baixa de um título com data da baixa: 28/03/18.
- Para esse cenário temos **365 dias de retroação**.
- Nesse caso, o campo Dias para retroação da baixa do usuário deverá estar como 365 ou superior.

![Imagem 7: Após o ajuste, efetue a baixa novamente dos títulos.](https://ajuda.sankhya.com.br/hc/article_attachments/16199845197591) Após o ajuste, efetue a baixa novamente dos títulos.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16199845201559) CAUSA:**

Mensagem retornada ao tentar realizar baixa/estorno de títulos com data retroativa ou futura, diferente do período liberado para o usuário.
