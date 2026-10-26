---
id: "360044228333"
titulo: "Cálculo da Data de Vencimento, utilizando TEF no Fast Service"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044228333-C%C3%A1lculo-da-Data-de-Vencimento-utilizando-TEF-no-Fast-Service"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:59:51Z"
rotulos: ["#RevisadoJR", "Configuração", "Fast Service", "Vencimento", "TEF", "Financeiro", "Sem TEF dois métodos", "Data venda + prazo", "TEF vencimento cálculo"]
---

# Cálculo da Data de Vencimento, utilizando TEF no Fast Service

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198756048151) SITUAÇÃO:**

Comportamento do sistema quanto ao cálculo de Vencimento de Títulos quando utilizando sistema TEF no Fast Service.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198756050327) SOLUÇÃO:**

Para podermos levar em consideração a questão de Data de Vencimento, primeiro temos que saber se a empresa utiliza TEF ou não no Fast Service.

(1)** SITUAÇÃO¹ - Caso empresa utilize TEF:**
Caso o mesmo utilize TEF no Fast Service e a venda tenha sido feito no PDV, o cálculo da Data de Vencimento, não seguirá nenhuma linha de configuração. Para vendas de TEF discado/dedicado, o cálculo desta data é feita internamente nos fontes do Fast Service, seguindo o calculo de 30 (trinta) X Nr. de Parcelas.

**(2)** **EXEMPLO:**
![Imagem 3: (2) EXEMPLO: Venda feita por Cartão, parcelado em apenas 1x no dia 08/08/2018, gerará um financeiro com Data de…](https://ajuda.sankhya.com.br/hc/article_attachments/16198756058519) Venda feita por Cartão, parcelado em apenas 1x no dia 08/08/2018, gerará um financeiro com Data de Vencimento igual a 08/09/2018.

![Imagem 4: Venda feita por Cartão, parcelado em 3x no dia 08/08/2018, gerará 3 linhas de financeiro com Data de Vencimento,…](https://ajuda.sankhya.com.br/hc/article_attachments/16198756060951) Venda feita por Cartão, parcelado em 3x no dia 08/08/2018, gerará 3 linhas de financeiro com Data de Vencimento, respectivamente igual a:

**(3)**1- 08/09/2018
**(3)**2- 08/10/2018
**(3)**3- 08/11/2018

(1)**SITUAÇÃO² - Caso Empresa NÃO utilize TEF:**
Caso o mesmo não utilize TEF no Fast Service, existem 2 formas de calcular a Data de Vencimento do Titulo.

**![Imagem 5: Caso a venda esteja sendo feita da tela de Financeiro 'Botões' ou 'Simplificado':](https://ajuda.sankhya.com.br/hc/article_attachments/16198756058519) Caso a venda esteja sendo feita da tela de Financeiro 'Botões' ou 'Simplificado':**

A Data de Vencimento ficará como **Data da Venda** + **Prazo do Tipo de Titulo**. O Fast Service irá capturar o valor inserido neste campo e acrescentará a data de atual da venda para o cálculo do Vencimento.

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198756064151) OBSERVAÇÃO:**

Até a data desta nota, o sistema não captura nenhuma data informada no Tipo de Negociação, isto porque no Fast Service não há relação obrigatória entre Tipo de Negociação x Tipo de Titulo.

![Imagem 7: Até a data desta nota, o sistema não captura nenhuma data informada no Tipo de Negociação, isto porque no Fast Service…](https://ajuda.sankhya.com.br/hc/article_attachments/12809557528087)

**![Imagem 8: Caso o parceiro utilize a tela de financeiro 'Parcelas', o sistema poderá operar de 2 formas:](https://ajuda.sankhya.com.br/hc/article_attachments/16198756060951) Caso o parceiro utilize a tela de financeiro 'Parcelas', o sistema poderá operar de 2 formas:**

**(3)**Caso seja digitado no campo **"Vencto 1ª Parcela"** ou deixado o campo **"Qtd. Parcelas"** igual a 0 (zero), o sistema seguirá a mesma hierarquia dita acima: 'ata da Venda + Prazo do Tipo de Titulo.

**(3)**Caso contrário, irá capturar o valor digitado no campo Vencto 1ª Parcelas x Qtd. Parcelas e calcular o vencimentos dos títulos.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16198756064151) OBSERVAÇÃO:**

Lembrando que o sistema efetua os cálculos para os tipos de títulos Cartão de Crédito/Débito ou Voucher.

![Imagem 10: CAUSA: Ocorre quando as configurações e a adequação sobre o comportamento da aplicação sobre os cálculos não estão…](https://ajuda.sankhya.com.br/hc/article_attachments/16198756066711) **CAUSA:**
Ocorre quando as configurações e a adequação sobre o comportamento da aplicação sobre os cálculos não estão claras para o usuário.
