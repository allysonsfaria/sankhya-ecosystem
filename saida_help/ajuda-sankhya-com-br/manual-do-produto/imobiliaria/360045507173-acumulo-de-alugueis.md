---
id: "360045507173"
titulo: "Acúmulo de Aluguéis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:09:14Z"
rotulos: ["Contrato", "Locação", "Financeiro", "Renegociação", "br.com.sankhya.tim.mov.acumulo", "Renegociar parcelas vencidas", "Informar contrato e datas", "Gerar e efetivar novas parcelas", "Imobiliária"]
---

# Acúmulo de Aluguéis

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311387109143) Módulo: Imobiliária > Rotinas > locação       ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311403406999) Versão disponível: a partir da 3.31
```

---

Esta tela tem a finalidade de acumular todas as parcelas vencidas do [Contrato de Locação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o) e renegociar, conforme sua necessidade.

Acesse os links abaixo para facilitar sua navegação nas funcionalidades desta tela:

| [Aba Parcelas Origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#abaparcelasorigem) |  | [Aba Novas Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#abanovasparcelas) |
| --- | --- | --- |
| [Outras Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#outrasinforma%C3%A7%C3%B5es) |  |  |

                 

![Imagem 3: Outras Informações](https://ajuda.sankhya.com.br/hc/article_attachments/360088546533)

Primeiramente, informe um Contrato de Locação que possua parcelas vencidas e, após isto, insira a **"Dt. Base"** e a **"Dt. Venc"** destas parcelas.

## Aba Parcelas Origem

Esta aba carregará todas as parcelas vencidas do Contrato de Locação, quando você acionar a opção **"Vincular Parcelas"** do botão **"Outras Opções..."** no topo da tela.

[GIF animado: Imagem 4: Esta aba carregará todas as parcelas vencidas do Contrato de Locação , quando você acionar a opção "Vincular Parcelas"…](https://ajuda.sankhya.com.br/hc/article_attachments/360087408894)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#top)

## Aba Novas Parcelas

Após preencher todos os campos conforme a nova negociação e efetivar, estas serão lançadas na aba **"Novas Parcelas"** e também no Contrato de Locação, aba [Negociações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#abanegocia%C3%A7%C3%B5es), sub-aba [Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117213-Contrato-de-Loca%C3%A7%C3%A3o#sub-abaparcelas).

![Imagem 5: Após preencher todos os campos conforme a nova negociação e efetivar, estas serão lançadas na aba "Novas Parcelas" e…](https://ajuda.sankhya.com.br/hc/article_attachments/360087409214)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#top)

## Outras Informações

A tela de Acúmulo de Aluguéis é utilizada para a renegociação de parcelas de um Contrato de Locação, conforme falamos inicialmente, e funciona de acordo com os seguintes passos:

- Primeiramente, o contrato alvo para o acúmulo deve possuir uma negociação com parcelas em aberto geradas;
- Ao informar o número do contrato na tela, aparecerão os acúmulos desse contrato; caso não exista nenhum, basta que você insira um novo registro, informando a data de vencimento e a data base do acúmulo;
- Após a criação do acúmulo, faça a busca das parcelas desejadas através do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15501397513367) **"Outras Opções..."**, opção **"Vincular Parcelas"**. Após selecionar as parcelas desejadas, elas serão carregadas para a aba [Parcelas Origem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#abaparcelasorigem), apresentando o total devido, multa, juros e etc;
- Depois de inserir as parcelas de origem, gere as novas parcelas. Na aba [Novas Parcelas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#abanovasparcelas), elas podem ser geradas uma à uma (criando um novo registro e informando a data de vencimento da parcela e o valor) ou todas de uma vez, preenchendo os campos **"Qtd"** e **"Vcto"** e clicando no botão **"Gerar"**;
- Quando as novas parcelas estiverem geradas, efetive o acúmulo através do botão Outras Opções..., opção **"Efetivar"** e, após efetivadas, as parcelas de origem serão excluídas do contrato e as novas serão acrescentadas.

A fórmula de cálculo de juros é a seguinte:

indiceJuros = (atrasoDias / 30 \* timpercjurosloc) / 100
valorJuros = valorAluguel \* indiceJuros

E a fórmula do cálculo de correção:

valorIndiceAcumulado = timcodmmon acumulado de acordo com atrasoDias.
valorCorrMon = valorAluguel \* valorIndiceAcumulado

**Observação:** Nos cálculos, a data do vencimento é incluída na atualização e a data do novo vencimento não é incluída, visto que faz parte da negociação do acúmulo.

A fórmula do cálculo de multa é a seguinte:

- Se o atrasoDias for maior do que a timmultandias: percentualDeMulta = timmultadialoc \* timmultandias
- Se não: percentualDeMulta = timmultadialoc \* atrasoDias

valorMulta = valorAluguel / 100 \* percentualDeMulta.

**Nota:** o pró-rata leva em consideração sempre 30 dias do mês, exceto o mês de fevereiro que poderá ser 28 ou 29 dias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045507173-Ac%C3%BAmulo-de-Alugu%C3%A9is#top)
