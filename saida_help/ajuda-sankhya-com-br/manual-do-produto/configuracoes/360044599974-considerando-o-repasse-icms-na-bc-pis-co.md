---
id: "360044599974"
titulo: "Considerando o Repasse ICMS na BC PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599974-Considerando-o-Repasse-ICMS-na-BC-PIS-COFINS"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-13T15:13:35Z"
rotulos: ["Configuração", "NF-e", "COFINS", "PIS", "ICMS", "Impostos", "Considerando o Repasse ICMS na BC PIS/COFINS manual", "Preferências", "Repasse ICMS na BC PIS/COFINS: Configurações e Exemplo"]
---

# Considerando o Repasse ICMS na BC PIS/COFINS

O artigo a seguir, visa esclarecer a influência da marcação **"Considera Repasse ICMS na BC PIS/COFINS?"** nos cálculos realizados no sistema. Portanto, quando ela for habilitada ficará definido que o Desconto de Redução de Base de ICMS será reduzido do valor da base de cálculo do PIS/COFINS.

Abaixo, considere um exemplo demonstrando as configurações necessárias para que o cálculo dos valores dos impostos aconteça de acordo com a marcação mencionada:

- Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), acione a marcação Considera Repasse ICMS na BC PIS/COFINS?;
- Em seguida, no [Cadastro de Alíquotas de PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600434-Al%C3%ADquotas-de-PIS) configure uma alíquota de PIS com %0,65 e o tipo **"Percentual"**;
- No [Cadastro de Alíquotas de COFINS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS) realize a configuração de uma alíquota de COFINS com % 3,00 aplicando o tipo Percentual;
- Ainda no cadastro de alíquotas, faça a configuração de uma [Alíquota de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108813-Al%C3%ADquotas-de-COFINS) com %17,00 e na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232854-Al%C3%ADquotas-de-ICMS#abageral), seção **"Repassar para o cliente"**, habilite a marcação **"ICMS"**;
- Depois, no Cadastro de [Tipos de Operação- TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), configure a TOP que será utilizada no lançamento da NF-e e na aba [Desp. Acessórias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abadespesasacessrias), todas as marcações das seções **"Seção ICMS Proporcional ao ICMS dos Itens"**, **"Seção PIS Proporcional ao PIS dos Itens"** e **"Seção COFINS Proporcional ao COFINS dos Itens"**, devem ser habilitadas.

Posteriormente, efetue o lançamento de uma NF-e com um item no valor de R$ 30,00, onde se tem um frete incluso e CIF no valor de R$ 10,00. Assim, os valores dos impostos serão ser calculados da seguinte forma:

- **ICMS Produto**

**Base ICMS:** 30,00

**Alíquota:** 17%

**Valor ICMS:** 5,10 (30,00 \* 17%)

**Valor de Desconto de Redução da Base:** 5,10

- **ICMS Frete**

**Base ICMS:** 10,00

**Alíquota:** 17 %

**Valor ICMS:** 1,70 (10 \* 17%)

**Valor de Desconto de Redução da Base:** 1,70

**Base de Cálculo ICMS:** (30+ 10) = 40,00

**Valor do ICMS:** (5,10 + 1,70) = 6,80. Este valor será desconto no valor total da nota.

**Valor da Nota:** (40 - 6,80) = 33,20

Cálculo PIS Incidência Geral

- **Base PIS**

**(+) Valor do Produto:** 30,00

**(+) Valor do Frete:** 10,00

**(-) Desc. Red. Base - Produto:** 5,10

**(-) Desc. Red. Base - Frete:** 1,70

**Base PIS:** 33,20

**Alíquota:** 0,65 %

**Valor PIS:** 0,21 (33,20 \* 0,65%)

Base COFINS Incidência Geral

- **Base COFINS**

**(+) Valor do Produto:** 30,00

**(+) Valor do Frete:** 10,00

**(-) Desc. Red. Base - Produto:** 5,10

**(-) Desc. Red. Base - Frete:** 1,70

**Base COFINS:** 33,20

**Alíquota:** 3,00 %

**Valor COFINS:** 0,99 (33,20 \* 3,00%)

Resumo dos Totais

**Valor da Nota:** 33,20

**Base ICMS da nota:** 40,00

**Valor ICMS da nota:** 6,80

**Desconto Redução de Base:** 6,80

**Base PIS Geral:** 33,20

**Valor PIS Geral:** 0,21

**Base COFINS Geral:** 33,20

**Valor COFINS Geral:** 0,99

## Parceiros com código SUFRAMA

Por padrão, quando o parceiro tem o **Código SUFRAMA** preenchido, o Desconto de Redução de Base de ICMS (**Vlr. Repasse de Redução**) não é deduzido da base de cálculo do PIS e da COFINS, mesmo com a marcação **Considera Repasse ICMS na BC PIS/COFINS?** ativa.

Para deduzir o repasse também nas vendas para parceiros SUFRAMA, como nas operações com a Zona Franca de Manaus e as Áreas de Livre Comércio:

1. Acesse **Configurações › Avançado › Preferências**, pesquise o parâmetro **COMDEDREPPCSUF** e ative-o.
2. No cadastro do parceiro, mantenha o **Código SUFRAMA** preenchido e ative a marcação **Possui Suframa para PIS/COFINS**.
3. Nas **Preferências da Empresa**, aba **Propriedades**, mantenha ativa a marcação **Considera Repasse ICMS na BC PIS/COFINS?**.
4. Nos cadastros de **Alíquotas de PIS** e **Alíquotas de COFINS**, preencha o campo **Alíquota Suframa**.

Com o parâmetro ativo, o Sankhya Om deduz o repasse da base de cálculo do PIS e da COFINS, tanto no valor do produto quanto nas despesas acessórias, como o frete. Não é preciso remover o **Código SUFRAMA** do parceiro: ele continua sendo informado no XML da NF-e, e a nota sem esse código é rejeitada pela SEFAZ (rejeição 625).

**ℹ️ Nota**

O parâmetro **COMDEDREPPCSUF** vem desativado, para manter o cálculo atual de quem já usa a marcação **Considera Repasse ICMS na BC PIS/COFINS?**. A base de cálculo da CSLL não é alterada pelo parâmetro.
