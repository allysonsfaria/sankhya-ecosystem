---
id: "35807135993751"
titulo: "Ajuste no cálculo não atualiza valores do Crédito do Trabalhador - MGE"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35807135993751-Ajuste-no-c%C3%A1lculo-n%C3%A3o-atualiza-valores-do-Cr%C3%A9dito-do-Trabalhador-MGE"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:07Z"
rotulos: ["Configuração", "Eventos", "MGE", "Crédito", "Preferências", "Financeiro", "FPEVERECAUTO", "Ajuste no cálculo", "não atualiza valores do Crédito do Trabalhador", "Cód. Eventos com Recálculo Automático"]
---

# Ajuste no cálculo não atualiza valores do Crédito do Trabalhador - MGE

**SITUAÇÃO:**

Ao realizar um ajuste de cálculo, seja para corrigir valores ou incluir eventos que compõem a base do Crédito do Trabalhador, o valor referente ao Desconto do Crédito do Trabalhador e/ou à Parcela não descontada do Crédito do Trabalhador não é atualizado automaticamente após o ajuste.

**SOLUÇÃO:**

**(1)**  Selecione a opção: **Avançado » Preferências » Todas Preferências**.

![Imagem 1: (1) Selecione a opção: Avançado » Preferências » Todas Preferências .](https://ajuda.sankhya.com.br/hc/article_attachments/36257348851991)

**(2)** Adicione o código **''FPEVERECAUTO''** Cód. Eventos com Recálculo Automático, para corrigir o cálculo dos eventos vinculados ao Desconto do Crédito do Trabalhador e à Parcela não descontada do Crédito do Trabalhador.

![Imagem 2: (2) Adicione o código ''FPEVERECAUTO'' Cód. Eventos com Recálculo Automático, para corrigir o cálculo dos eventos…](https://ajuda.sankhya.com.br/hc/article_attachments/36257348853143)![Imagem 3: (2) Adicione o código ''FPEVERECAUTO'' Cód. Eventos com Recálculo Automático, para corrigir o cálculo dos eventos…](https://ajuda.sankhya.com.br/hc/article_attachments/36257348856215)

**CAUSA:**

O comportamento ocorre sempre que o código '**'FPEVERECAUTO''** – Cód. Eventos com Recálculo Automático. não está incluído na sessão **''Preferência''**.
