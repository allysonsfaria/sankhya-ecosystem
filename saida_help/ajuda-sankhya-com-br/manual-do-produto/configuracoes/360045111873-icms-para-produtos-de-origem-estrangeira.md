---
id: "360045111873"
titulo: "ICMS para produtos de Origem Estrangeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111873-ICMS-para-produtos-de-Origem-Estrangeira"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:58:26Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Origem", "SEFAZ", "ICMS", "Impostos", "ALIQPRODESTRAN", "Estrangeira", "ICMS para produtos de Origem Estrangeira manual", "Configuração de Alíquota de ICMS para Produtos de Origem Estrangeira"]
---

# ICMS para produtos de Origem Estrangeira

Nos lançamentos referentes à Pedidos de Venda, Pedidos de Compra, Notas de Venda ou Notas de Compra, quando os produtos negociados para fora do estado são de origem estrangeira, a alíquota de ICMS utilizada é de 4%. Salvo algumas exceções, esta é uma regra tributária, que é inclusive validada pela SEFAZ na emissão da NF-e. As configurações abaixo, visam permitir que essa alíquota de ICMS possa ser configurada sem a necessidade de cadastro de várias exceções.

O produto é considerado de origem estrangeira quando:

- Possui em seu cadastro ([Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abageral)), o campo **"Origem do produto"** com os valores **"1"**, **"2"**, **"3"** ou **"8"**, ressalta-se que, as origens **"6"** e **"7"** não entram nesse cenário.
- A operação for de saída interestadual;
- CST de código **"00"**, **"10"**, **"20"**, **"30"**, **"40"**, **"60"**, **"70"** ou **"90"** ([Cadastro de Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), campo **"Tributação"**);
- Data de emissão do pedido/nota superior a 01/01/2013;
- NF-e complementar em que a NF-e ou NF (modelo 1) referenciada possua data de emissão superior a 01/01/2013;
- Nos lançamentos de Pedidos de Compra ou Pedidos de Venda, o [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) utilizado, deve estar com a marcação **"Calcular ICMS de Origem Estrangeira"** presente na Aba Impostos, realizada; para Notas de Compra ou Notas de Venda, esta marcação não precisa ser efetuada;
- Não possuir as CFOP's 6664, 6665, 6902, 6903, 6906, 6907, 6909, 6913, 6916 e/ou 6925 (operações de Saída);
- Não possuir as CFOP's 2664, 2665, 2902, 2903, 2906, 2907, 2909, 2913, 2916 e/ou 2925 (operações de Entrada).

**Importante:** para localizar a origem do produto, o sistema verifica se houve preenchimento do campo **"Origem do produto"** na aba **"Impostos / Informações por empresa"** presente no Cadastro de Produtos; caso exista, esta informação será considerada; caso não haja, a origem a ser considerada será a do Cadastro de Produtos, aba Geral).

No Cadastro de Alíquotas de ICMS, aba Geral tem-se o campo **"Alíquota p/ Origem Estrangeira"**, campo este, essencial para este procedimento:

![Imagem 1: No Cadastro de Alíquotas de ICMS , aba Geral tem-se o campo "Alíquota p/ Origem Estrangeira" , campo este, essencial…](https://ajuda.sankhya.com.br/hc/article_attachments/360068421673)

No momento de calcular o ICMS para um item na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) ou na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), com base nas informações descritas acima, o sistema irá verificar se o mesmo é de origem estrangeira para o cálculo de ICMS. Caso o produto seja de origem estrangeira, a alíquota de ICMS calculada será a configurada para produtos de origem estrangeira.

**Importante:**  se as regras de alíquota encontradas não possuírem a alíquota para produtos de origem estrangeira preenchida, o sistema irá pegar o valor informado no parâmetro **"Alíquota Padrão Produto de Origem Estrangeira - ALIQPRODESTRAN"**; caso este parâmetro esteja nulo, o sistema irá utilizar o valor do campo **"Alíquota"** presente na aba Geral do cadastro de Alíquotas de ICMS. Vale mencionar que caso o campo Alíquota p/ origem estrangeira ou o parâmetro **ALIQPRODESTRAN** estejam com valor igual a **"0"**, o sistema irá considerar esta alíquota zerada para efetuar o cálculo do ICMS e a alíquota de ICMS utilizada será a encontrada pelo sistema em situações normais, ou seja, desconsiderando estas configurações.
