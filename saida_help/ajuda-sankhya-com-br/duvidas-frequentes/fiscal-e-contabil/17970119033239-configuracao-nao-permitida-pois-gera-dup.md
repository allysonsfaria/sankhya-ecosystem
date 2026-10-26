---
id: "17970119033239"
titulo: "Configuração não permitida, pois gera duplicidade da retenção dos impostos no financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17970119033239-Configura%C3%A7%C3%A3o-n%C3%A3o-permitida-pois-gera-duplicidade-da-reten%C3%A7%C3%A3o-dos-impostos-no-financeiro"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:52:58Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Impostos", "Financeiro", "CORE_ E05957", "Base incorreta de imposto", "Parcelamento causa duplicidade", "Altere para valor do pagamento"]
---

# Configuração não permitida, pois gera duplicidade da retenção dos impostos no financeiro

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17970112485783) **MENSAGEM:**

[CORE\_ E05957] Configuração não permitida, pois gera duplicidade da retenção dos impostos no financeiro.
Configuração: Nas configurações para cálculo de Outros Impostos o valor do campo [Base do Imposto no Financeiro] está como [Valor do documento], em casos de mais de uma parcela ou baixa parcial gera duplicidade.

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17970129180055) **SITUAÇÃO:**

Ao lançar uma Nota, onde temos duas ou mais parcelas, e há retenção de impostos, o sistema não está permite confirmar.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17971333324311)**SOLUÇÃO:**

O sistema irá utilizar como base de cálculo para a retenção do imposto o valor da nota e nesse caso específico, devido a utilização do tipo de negociação parcelado, não é possível utiliza-lo, pois assim gera-se duplicidade de retenção nas parcelas. 
 
Altere o campo 'Base de Calculo de Imposto' para 'Valor do Pagamento', assim ele ira calcular o imposto e realizar a retenção de maneira separada para cada parcela

![Imagem 4: O sistema irá utilizar como base de cálculo para a retenção do imposto o valor da nota e nesse caso específico, devido…](https://ajuda.sankhya.com.br/hc/article_attachments/17971333350551)

Ficando assim no financeiro de cada parcela.

![Imagem 5: Ficando assim no financeiro de cada parcela.](https://ajuda.sankhya.com.br/hc/article_attachments/17971361566231)
