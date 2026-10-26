---
id: "42733668636183"
titulo: "Processo Adequação da NF-e à NT 2019.001 v1.64 (Crédito Presumido)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42733668636183-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2019-001-v1-64-Cr%C3%A9dito-Presumido"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
rotulos: ["Nota Técnica 2019.001 v1.64"]
---

# Processo Adequação da NF-e à NT 2019.001 v1.64 (Crédito Presumido)

**Caminhos de Acesso:**

- Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e
- Alíquotas de ICMS › aba Geral

---

## O que é e para que serve

A **Nota Técnica 2019.001 v1.64** gera o grupo de crédito presumido de ICMS (gCred) no XML da NF-e a partir do cadastro de Alíquotas de ICMS. Ela não calcula o benefício fiscal em si — apenas transporta para o XML o que já está configurado no cadastro do benefício.

## O que foi alterado

Com a NT ativa e os campos **Cód. do Benefício**, **Percentual do Crédito Presumido** e **Valor do Crédito Presumido** preenchidos na aba Geral da tela Alíquotas de ICMS, o grupo gCred e suas tags são gerados no XML: a tag <cCredPresumido> usa o valor do campo Código do Benefício, a tag <pCredPresumido> usa o valor do campo Percentual do Crédito Presumido, e a tag <vCredPresumido> usa o valor do campo Valor do Crédito Presumido.

## Pontos de atenção

O grupo gCred só é gerado se os três campos do benefício estiverem preenchidos no cadastro de Alíquotas de ICMS — faltando algum deles, o grupo não aparece no XML.
