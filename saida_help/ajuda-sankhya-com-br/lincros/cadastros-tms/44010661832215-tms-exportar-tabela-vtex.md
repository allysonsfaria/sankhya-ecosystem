---
id: "44010661832215"
titulo: "[TMS] - Exportar tabela VTEX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010661832215--TMS-Exportar-tabela-VTEX"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:43:23Z"
rotulos: ["sync_hc", "lincros", "lincros_13438862", "sync_hash_5161de98d28d"]
---

# [TMS] - Exportar tabela VTEX

Este é um artigo complementar. Para saber mais sobre a integração Lincros com VTEX acesse [este artigo](https://intercom.help/ajudalincros/pt-BR/articles/13434455-tms-integracao-vtex).

## Objetivo:

Este artigo tem como objetivo instruir como exportar uma tabela de fretes no modelo VTEX.

## Pré-requisitos:

Possuir habilitada a funcionalidade da Integração VTEX.

Possuir a integração com a VTEX configurada.

Possuir tabela de frete cadastrada.

## Localização:

Cadastros Gerais > Transportadoras > Negociações > Transportadora

---

## Instruções:

Para exportar a tabela de frete Vtex, selecione a tabela de frete desejada (1), clique na seta ao lado de "exportar" (2) e em seguida selecione a opção Vtex (3).

![Imagem 1: Para exportar a tabela de frete Vtex, selecione a tabela de frete desejada (1), clique na seta ao lado de "exportar"…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1964968962/8bb3826fa38d76076e5d80af7a40/4488A39BFADBE48344D714EA2482CE0B?expires=1791331200&signature=425902de02103e29c1d27a55b69d077535ac0023a6801627fde3b12ca69475ee&req=dSkhEsB4lYhZW%2FMW3nq%2BgeUP5YVsiiWrt4SFR1A7%2BDCSUSJ5H7z2QPIH%2BZLw%0ApfLuHFCsHEuzVzxrL1fSaOtACfI%3D%0A)

Informe o e-mail para recebimento da tabela e clique em "sim"

![Imagem 2: Informe o e-mail para recebimento da tabela e clique em "sim"](https://ajuda.sankhya.com.br/hc/article_attachments/44010662181783)

Você receberá a tabela no seu e-mail.

Na tabela Vtex somente são consideradas as faixas de peso nominal e de peso excedente, e somente o componente Frete peso. Caso hajam outras faixas e/ou outros componentes na tabela, eles são desconsiderados na exportação, gerando o arquivo somente com os dados de peso.

![Imagem 3: Na tabela Vtex somente são consideradas as faixas de peso nominal e de peso excedente, e somente o componente Frete…](https://ajuda.sankhya.com.br/hc/article_attachments/44010666218391)

---

## Correspondências dos campos:

- **ZipCodeStart** - faixa inicial do CEP - deve ter 8 caracteres.
- **ZipCodeEnd** - faixa final do CEP - deve ter 8 caracteres. As faixas de início e fim de CEP são correspondentes ao endereço de destino da faixa da tabela. As faixas de destino serão quebradas respeitando os CEP de restrição da rota.
- **PolygonName** - geolocalização, só necessário se a faixa inicial e final de CEP não forem informados, padrão envia como zero.
- **WeightStart** - peso inicial - peso em gramas - deve ter 6 casas decimais.
- **WeightEnd** - peso final - peso em gramas - deve ter 6 casas decimais.
- **AbsoluteMoneyCost** - valor fixo de frete que deverá ser cobrado - deve ter 6 casas decimais. (Faixa: Peso Nominal / Componente: Frete peso / Valor: Valor mínimo ou valor fixo)

![Imagem 4: AbsoluteMoneyCost - valor fixo de frete que deverá ser cobrado - deve ter 6 casas decimais. (Faixa: Peso Nominal /…](https://ajuda.sankhya.com.br/hc/article_attachments/44010662465943)

- **PricePercent** - Ad valorem (Percentual em cima do valor da nota) - deve ter 6 casas decimais. (Faixa: Valor mercadoria / Componente: Ad valorem / Valor: Percentual %)

![Imagem 5: PricePercent - Ad valorem (Percentual em cima do valor da nota) - deve ter 6 casas decimais. (Faixa: Valor mercadoria /…](https://ajuda.sankhya.com.br/hc/article_attachments/44010666499479)

- **PriceByExtraWeight** - cálculo conforme peso - deve ter 6 casas decimais. (Faixa: Peso excedente / Componente: Frete peso / Valor: Valor fixo)

![Imagem 6: PriceByExtraWeight - cálculo conforme peso - deve ter 6 casas decimais. (Faixa: Peso excedente / Componente: Frete peso…](https://ajuda.sankhya.com.br/hc/article_attachments/44010708205079)

- **MaxVolume** - volume máximo - por padrão utilização o valor: 1000000,000000
- **TimeCost** - Tempo de entrega do pedido pela transportadora, no formato DD.HH:MM:SS. (Campo destinado ao prazo de entrega)
- **Country** - País onde a entrega será realizada, preenchido com o código ISO de 3 dígitos.
- **MinimumValueInsurance** - Valor adicional de seguro, configurado com um valor absoluto, em número decimal.

---

Após a exportação é necessário realizar a [importação dela na plataforma VTEX](https://intercom.help/ajudalincros/pt-BR/articles/13432582-tms-cadastrar-tabela-tms-na-plataforma-vtex).

Depois de importada a tabela na Plataforma Vtex, é possível atualizar os valores sem precisar exportar a tabela do TMS e importá-la na VTEX, configurando e utilizando a função [Atualizar tabela VTEX](https://intercom.help/ajudalincros/pt-BR/articles/13438855-tms-atualizar-tabela-vtex).

## Informações importantes sobre os pesos nominais da tabela de frete:

- Todo peso nominal é multiplicado por 1000 para pegar o valor em gramas (e atender a exigência da vtex).
- Para os pesos nominais acima de 100 mil kg, o valor é convertido para o limite máximo de 7 dígitos, resultando: 9.999.999.
- Para os pesos nominais entre 10.000kg e 100.000kg é apresentado um e-mail com erro de exportação e inserido nos logs a mensagem: Peso nominal incompatível
- Para os pesos nominais até 9.999kg, é realizada a conversão para gramas normalmente.
