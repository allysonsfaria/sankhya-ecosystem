---
id: "44012613528599"
titulo: "[TMS] - Componente Carga Tributária Destacado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012613528599--TMS-Componente-Carga-Tribut%C3%A1ria-Destacado"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:34:24Z"
rotulos: ["sync_hc", "lincros", "lincros_13433424", "sync_hash_36fc006abffd"]
---

# [TMS] - Componente Carga Tributária Destacado

**Menu:** N/A

**Objetivo**: Como adicionar o componente de carga tributária destacado

**Considerações**:

- Carga Tributária Destacado é um componente padrão, criado para atender a necessidade de destacar os impostos para as transportadoras cujo valor dos componentes não consideram como parte da sua composição os custos de PIS e COFINS, esses são acrescidos ao total, juntamente com o ICMS ou ISS;

Abaixo segue o passo a passo:

Para utilizar este componente é necessário:

- Possuir os componentes PIS e COFINS cadastrados e informados nas Generalidades da Tabela de Fretes;
- No caso de cálculo de ISS, para que seja somado o componente Carga tributária destacado no total do frete, é necessário informar nas Generalidades da Tabela de Fretes o componente ICMS destacado;

**Obs**.: O componente Carga Tributária Destacado, utiliza o valor do frete, considerando que o valor dos componentes não contém na composição o PIS e COFINS, aonde é posteriormente feita a aplicação do percentual de impostos (PIS, COFINS, ICMS ou ISS).

## Exemplo

- Valor inicial do frete sem o ICMS: R$ 1.000,00 (este valor compreende todos os componentes de frete, exceto impostos)
- Realizar a inclusão dos impostos (soma de todos os %), conforme demonstração abaixo:

12% de ICMS / 7,60% COFINS / 1,65 % PIS
TOTAL 21, 25 % = 0,7875 (100% - 21,25% = 0,7875%)

- O valor final do frete é o índice sobre o valor do custo -> R$ 1.269,84 ( R$ 1.000,00 / 0,7875)

## Valor dos impostos

ICMS: 12% = R$ 152,38 (1.269,84 x 12%)
COFINS: 7,60% = R$ 96,51 (1.269,84 x 7,60%)
PIS: 1,65% = 20,95 (1.269,84 x1,65%)
TOTAL: 21,25% = R$ 269,84

Valor do frete sem impostos => R$ 1.269,84 – 269,84 = R$ 1.000,00

## Exemplo da tela do pré-conhecimento com o componente carga tributária destacado

![Imagem 1: Exemplo da tela do pré-conhecimento com o componente carga tributária destacado](https://ajuda.sankhya.com.br/hc/article_attachments/44012624813335)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
