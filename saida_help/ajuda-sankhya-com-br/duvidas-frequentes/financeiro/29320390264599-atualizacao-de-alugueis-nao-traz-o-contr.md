---
id: "29320390264599"
titulo: "Atualização de Aluguéis não traz o Contrato"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29320390264599-Atualiza%C3%A7%C3%A3o-de-Alugu%C3%A9is-n%C3%A3o-traz-o-Contrato"
trilha: "Dúvidas Frequentes > Financeiro"
atualizado_em: "2026-07-22T14:37:15Z"
rotulos: ["Configuração", "Contrato", "Movimentação Financeira", "Atualização", "Financeiro", "Atualização de Aluguéis não traz o Contrato", "Renovação de contratos", "Prorrogar alugueis", "Efetivar reajuste", "Gerar alugueis"]
---

# Atualização de Aluguéis não traz o Contrato

**(1)**Ao clicar em **"Vincular Contratos"**, na aba **"Contratos de Locação",** da tela **"Atualização de Aluguéis"**, o contrato referente ao parceiro desejado não está sendo apresentado. Para isso, siga os passos abaixo:

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29320417259415) SOLUÇÃO:**

![Imagem 2: Acesse o título na "Movimentação Financeira" , referente ao contrato ativo, marque a opção "Bloqueada" e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/29320417260695) Acesse o título na **"Movimentação Financeira"**, referente ao contrato ativo, marque a opção **"Bloqueada"** e salve.

Essa opção quando ativada faz com que o contrato fique disponível por uma questão bem simples. Contratos não podem sofrer atualizações enquanto o período não se concluir, então o campo Bloqueada indica que o contrato deve sofrer alguma atualização ou até mesmo sofreu alguma atualização jurídica.

**(1)** O parâmetro **"TIMGERALBLQ - Ger. aluguis passives de reajuste bloq."** pode influenciar no caso, pois quando ativado, mantém a opção "Bloqueada" marcada ao gerar contratos.

As opções para desbloquear a parcela são as seguintes:

**(2)** Pela rotina de **"Efetivar Reajuste"**, acessível na tela de **"Atualização de Aluguéis"**;

**(2)** Pela rotina de **"Renovação de Contratos"**, utilizando o botão **"Efetivar"** (na tela Renovação de Contratos).

**(2)**Pela rotina de **"Gerar Aluguéis"**, encontrada na tela de **"Contrato de Locação"**, na aba **"Negociações"**, opção **"Gerar Aluguéis"**.

**(2)**Pela rotina de **"Prorrogar Aluguéis"**, também localizada na tela de Contrato de Locação, na aba Negociações, opção **"Prorrogar Negociação"**.

Essa última rotina desbloqueará todas as parcelas vinculadas à negociação selecionada na aba, desde que a Data de Vencimento Inicial do financeiro seja menor que a Data do Próximo Reajuste do contrato de locação.
