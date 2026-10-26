---
id: "360043696753"
titulo: "Rotina de ajuste dos totais dos impostos (NOMETABELA). Problemas no cálculo do valor de 'NOMEIMPOSTO'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043696753-Rotina-de-ajuste-dos-totais-dos-impostos-NOMETABELA-Problemas-no-c%C3%A1lculo-do-valor-de-NOMEIMPOSTO"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-10T16:58:23Z"
rotulos: ["#criadoRoger", "CORE_E04474", "Configuração", "IPI", "ICMS", "Impostos", "Nota Fiscal", "CORE_E04473", "Problemas no cálculo de impostos (ex.: ICMS IPI)", "Verifique e ajuste impostos e despesas acessórias", "Ajuste proporção de impostos em Tipos de Operação (TOP)", "Passos para resolver", "Comercial"]
---

# Rotina de ajuste dos totais dos impostos (NOMETABELA). Problemas no cálculo do valor de 'NOMEIMPOSTO'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16165773348759) MENSAGEM:**

[CORE\_E04474] Rotina de ajuste dos totais dos impostos (NOMETABELA). Problemas no cálculo da base de 'NOMEIMPOSTO'

[CORE\_E04473] Rotina de ajuste dos totais dos impostos (NOMETABELA). Problemas no cálculo do valor de 'NOMEIMPOSTO'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16165773353239) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Identifique quais os impostos devem incidir na nota (ICMS, IPI, ISS, ICMS-ST, etc).](https://ajuda.sankhya.com.br/hc/article_attachments/16165773355671) Identifique quais os impostos devem incidir na nota **(ICMS, IPI, ISS, ICMS-ST, etc).**

- Efetue o cálculo da soma dos impostos dos itens e verifique se é igual ao total descriminado no rodapé da nota.
- Certifique-se sobre a existência de despesas acessórias inclusas ao total do documento, bem como sua incidência ou não na base de cálculo dos impostos.

![Imagem 4: Caso necessário proporcionalizar as despesas acessórias entre os itens para o cálculo do impostos, pode se efetuar de…](https://ajuda.sankhya.com.br/hc/article_attachments/16165789326743) Caso necessário proporcionalizar as despesas acessórias entre os itens para o cálculo do impostos, pode se efetuar de forma automática, configurando a TOP, quais impostos serão proporcionalizados, marcando apenas as que desejam.

Para isso configure:

- Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
- Aba: **Desp. Acessórias**
- De acordo com a necessidade do documento, efetue a marcação do(s) imposto(s) no qual deseja proporcionalizar para os itens

![Imagem 5: De acordo com a necessidade do documento, efetue a marcação do(s) imposto(s) no qual deseja proporcionalizar para os…](https://ajuda.sankhya.com.br/hc/article_attachments/14708420651031)

![Imagem 6: Realizados os ajustes acima, refaça o lançamento/faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16165773360023) Realizados os ajustes acima, refaça o lançamento/faturamento.

### **(1)** Exemplo de análise para correção do erro: CORE\_E04473

(2)**Valores da mensagem:**

Rotina de ajuste dos totais dos impostos (TGFCAB).
Problemas no cálculo do valor de ICMS.
Valor do ICMS na nota = R$8.447,66.
Valor do ICMS na tabela de impostos = R$8.446,45.
Verifique

(2)**Dados do Lançamento:**

Total dos Produtos 136.856,70
IPI 10% (para apenas um produto) 668,85
Vlr. Frete: 4.125,82
ICMS do Frete: 246,05 (nos totais da nota)
--> IPI incide na base de ICMS

(2)**Valores na Mensagem de Erro:**

Valor do ICMS da nota = 8.447,66
Valor do ICMS na DIN = 8.446,45

**- Diferença 1,21**

(2)**Valores nas Tabelas**

Ver total de ICMS nos totais da nota (na tabela TGFCAB): 8.447,66
Ver total de ICMS na grade de itens, outras opções: Consultar/Alterar Dados do Imposto do Item (na tabela TGFDIN): 8.201,61

**Diferença 246,05. A diferença até aqui é o ICMS do frete**

(2)**Despesas Acessórias da TOP**

ICMS proporcional para frete: marcado
IPI proporcional para frete: desmarcado

(2)**Validando o Cálculo**

Vlr.Produto | Alíq.ICMS

103.768,20  |  4%
    6.688,50  | 12%  ---> IPI base 6.688,50 | 10%  (Base de ICMS 7.357,35)
  26.400,00  | 12%
-------------
136.856,70

(2)**Proporção:**

**(3)**Encontre o percentual que representa cada produto referente ao valor total dos produtos (sem considerar o vlr de IPI) » (Vlr. total de cada produto / Vlr. total dos produtos) \* 100

Produto 1 =  103.768,20 » 75,82%
Produto 2 =      6.688,50 »   4,89% 
Produto 3 =    26.400,00 » 19,29% 
--------------------------------------
Vlr Total Prod. 136.856,70  [100%]

**(3)**Encontre o valor proporcional do frete para cada produto (aplicar o percentual encontrado ao valor do frete) e aplique a alíquota de ICMS à este resultado:

Valor do Frete: 4.125,82

75,82%  -> 3.128,20  | 4%  === 125,13
4,89%     -> 201,75    | 12% ===  24,21
19,29%   -> 795,87    | 12% ===  95,50
--------------------------------------------
Total ICMS do frete                     244,84

**244,84 ICMS do frete correto**

**246,05 ICMS do frete calculado pelo sistema**

**246,05 - 244,84 = 1,21**

(2)**Conclusão do Exemplo:**

Como o valor do IPI deve incidir sobre a base de ICMS a TOP deve estar configurada para proporcionalizar também o IPI para frete.

**Observações:**

- Valor do Imposto no Total da Nota maior que na tabela de impostos (TGFDIN) » Alguma despesa acessória que não foi proporcionalizada
- Valor do Imposto no Total da Nota menor que na tabela de impostos (TGFDIN) » Possivelmente houve desconto que não foi distribuído entre os itens

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16165789334295) CAUSA:**

Ocorre quando há despesas acessórias no lançamento ('Frete, Seguro, Destaque, Juro, Embalagem') e a TOP não estava configurada para proporcionalizar os impostos para estas despesas. Pode ocorrer também quando há desconto informado no total da nota que não foi distribuído entre os itens.
