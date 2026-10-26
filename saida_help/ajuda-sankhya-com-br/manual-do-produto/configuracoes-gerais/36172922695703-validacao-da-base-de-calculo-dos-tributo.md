---
id: "36172922695703"
titulo: "Validação da Base de cálculo dos tributos IBS e CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36172922695703-Valida%C3%A7%C3%A3o-da-Base-de-c%C3%A1lculo-dos-tributos-IBS-e-CBS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Configurações gerais"
atualizado_em: "2026-10-05T16:43:47Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Impostos", "Tributos IBS e CBS", "Validação da Base de Cálculo", "IBS", "CBS", "Valor da Base de Cálculo", "IBS e CBS (vBC)", "Reforma Tributária", "Artigo atualizado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS"]
---

# Validação da Base de cálculo dos tributos IBS e CBS

A **"Nota Técnica 2025.002-RTC"**, publicada como parte da implementação da **"Reforma Tributária"**, introduziu novas validações referentes ao cálculo do **"IBS"** e **"CBS"** nas Notas Fiscais eletrônicas (NF-e).

Entre elas, destaca-se a validação do  **"Valor da Base de Cálculo do IBS/CBS (gIBSCBS/vBC)"**

## Descrição da Validação e Composição da Base

A SEFAZ passou a validar se o **"Valor da Base de Cálculo do IBS e CBS (vBC)"** informado no item da NF-e corresponde exatamente ao somatório dos campos que o compõem, conforme a fórmula:

```
vBC = vProd + vServ + vFrete + vSeg + vOutro + vII - vDesc - vPis - vCofins - vICMS
- vICMSUFDest - vFCP - vFCPUFDest - vICMSMono - vISSQN* + vIS
```

```
Exceção 1: Não subtrair o valor do PIS por Substituição Tributária (PIST/vPIS) quando
compor o valor total da NF-e (se indSomaPISST=1);

Exceção 2: Não subtrair o valor do COFINS por Substituição Tributária
(COFINSST/vCOFINS) quando compor o valor total da NF-e (se
indSomaCOFINSST=1).
```

## Como interpretar (sem juridiquês)

### ➕ Entram na base:

- Produto (**vProd**)
- Serviço (**vServ**)
- Frete (**vFrete**)
- Seguro (**vSeg**)
- Outras despesas (**vOutro**)
- Imposto de Importação (**vII**)
- IBS/CBS por dentro (**vIS**)

### ➖ Saem da base:

- Descontos (**vDesc**)
- PIS / COFINS
- ICMS (incluindo DIFAL e FCP)
- ICMS monofásico
- ISSQN (durante transição também sai)

O PLP 68/2024 determina a exclusão da base de cálculo do montante do próprio IBS e da CBS, do IPI, dos descontos incondicionais, e de reembolsos ou ressarcimentos recebidos por valores pagos relativos a operações por conta e ordem ou em nome de terceiros, desde que a documentação fiscal relativa a essas operações seja emitida em nome do terceiro. Durante o período de transição, de 1º de janeiro de 2026 a 31 de dezembro de 2032, também são excluídos da base de cálculo do IBS e da CBS o montante do ISS, ICMS, PIS e COFINS.

[Fonte GOV](https://www.gov.br/fazenda/pt-br/acesso-a-informacao/acoes-e-programas/reforma-tributaria/regulamentacao-da-reforma-tributaria/lei-geral-do-ibs-da-cbs-e-do-imposto-seletivo/resumos-tecnicos/plp-68-2024_resumo-ibs-e-cbs-sobre-operacoes.pdf)

##### REJEIÇÃO POR INCONSISTÊNCIA

Caso o valor informado no campo **"vBC"** não obedeça à fórmula acima, a NF-e pode ser rejeitada com a mensagem:

**"Rejeição: Valor da Base de Cálculo do IBS e CBS difere do somatório dos valores que a compõem [nItem: 999]"**

## O que a SEFAZ está fazendo nessa regra

Ela pega **todos esses campos do XML do item** e recalcula:

vBC=vProd+vServ+vFrete+vSeg+vOutro+vII−vDesc−vPIS−vCOFINS−vICMS−vICMSUFDest−vFCP−vFCPUFDest−vICMSMono−vISSQN+vISvBC = vProd + vServ + vFrete + vSeg + vOutro + vII - vDesc - vPIS - vCOFINS - vICMS - vICMSUFDest - vFCP - vFCPUFDest - vICMSMono - vISSQN + vISvBC=vProd+vServ+vFrete+vSeg+vOutro+vII−vDesc−vPIS−vCOFINS−vICMS−vICMSUFDest−vFCP−vFCPUFDest−vICMSMono−vISSQN+vIS

👉 Depois compara com o seu `<vBC>` informado
👉 Se não bater **exatamente** → rejeição 1104
