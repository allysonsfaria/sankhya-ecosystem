---
id: "36500284707223"
titulo: "Nota com Diferimento de ICMS, e proporcionalização de ICMS Para o Frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36500284707223-Nota-com-Diferimento-de-ICMS-e-proporcionaliza%C3%A7%C3%A3o-de-ICMS-Para-o-Frete"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-10-15T20:14:30Z"
rotulos: ["Configuração", "NF-e", "ICMS", "Impostos", "Preferências", "Proporcionalização de ICMS", "Diferimento do ICMS", "ICMS do Frete", "Tributação 51 - Diferimento", "ICMSFRETE"]
---

# Nota com Diferimento de ICMS, e proporcionalização de ICMS Para o Frete

##### SITUAÇÃO:

Ao emitir uma Nota de Venda sujeita à **Tributação 51 – Diferimento,** o é esperado é que o **ICMS do Frete (ICMSFRETE)** siga o mesmo critério aplicado ao **ICMS do item**, garantindo consistência entre os valores calculados na **TGFITE (itens)** e na **TGFCAB (cabeçalho)**.

No entanto, em alguns cenários, o ICMSFRETE **não considera o deferimento**, mesmo que o ICMS do item esteja correto.

Esse comportamento gera **divergência entre os valores exibidos na grade de itens e na totalização da nota (TGFDIN X TGFCAB)**, dificultando a confirmação do documento.

##### SOLUÇÃO:

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou Descrição''** pesquise pelo parâmetro **''GALQICMSFRTPROP''.**

**(3)** Abra a configuração e altere o campo **''Ligado/Desligado''** para **''Desligado''**.

![Imagem 1: (3) Abra a configuração e altere o campo ''Ligado/Desligado'' para ''Desligado'' .](https://ajuda.sankhya.com.br/hc/article_attachments/36570922200471)

**(4)** Recalcule o item da nota.

**(5)** O ICMS do Frete será ajustado e ficará coerente com os valores da TGFITE.

**CAUSA:**

O comportamento está relacionado ao parâmetro ''GALQICMSFRTPROP'' **– “Garantir alíq. de ICMS de Frete proporcional ao IPI?”**.

Quando esse parâmetro está **ligado (valor padrão)**, o sistema prioriza a proporcionalização do ICMS do frete **com base no IPI**, e não com base no diferimento do ICMS aplicado do item.

Por isso, mesmo que o item esteja com diferimento configurado corretamente, o frete continua sendo calculado **integralmente**, sem considerar o percentual de diferimento.
