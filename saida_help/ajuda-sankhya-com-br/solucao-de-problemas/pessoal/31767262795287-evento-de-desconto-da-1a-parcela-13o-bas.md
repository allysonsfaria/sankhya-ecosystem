---
id: "31767262795287"
titulo: "Evento de desconto da 1ª parcela 13º - base FGTS mensal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31767262795287-Evento-de-desconto-da-1%C2%AA-parcela-13%C2%BA-base-FGTS-mensal"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:43Z"
rotulos: ["Impostos", "eSocial", "Folha de Pagamento", "Rescisão", "Configuração Funcionários", "FGTS", "FGTS mensal", "evento Desc1ªParc 13ºBase FGTS Mensal (Cód. 316)", "FGTS Digital", "Manual de orientações do FGTS Digital", "incidência de FGTS", "Antecipação da 1ª parcela do 13º salário", "FGTS rescisório"]
---

# Evento de desconto da 1ª parcela 13º - base FGTS mensal

O evento **Desc1ªParc 13ºBase FGTS Mensal (Cód. 316)** foi criado para atender às regras do FGTS Digital em situações de desligamento de funcionários.

O FGTS Digital prevê que, em casos de desligamentos de empregados, quando o adiantamento da **1ª parcela do 13º salário** for **maior** do que o valor do 13º proporcional devido na rescisão, o empregador pode compensar esse valor com outras verbas da rescisão, conforme a legislação vigente.

Para que essa compensação ocorra corretamente, **a incidência de FGTS aplicada ao valor compensado não deve ser a do 13º salário (código [12])**, e sim a **mesma da remuneração mensal (código [11])**, pois essa parcela está sendo subtraída da base mensal. Caso contrário, a base de cálculo mensal não será ajustada corretamente.

---

![Imagem 1: Consulte o item 5.1.4 - do Manual de orientações do FGTS Digital :](https://ajuda.sankhya.com.br/hc/article_attachments/31768719732375) Consulte o item 5.1.4 - do [Manual de orientações do FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-23-16-12-2024.pdf):

| ![Imagem 2: Consulte o item 5.1.4 - do Manual de orientações do FGTS Digital :](https://ajuda.sankhya.com.br/hc/article_attachments/42309908147991)  ![Imagem 3: Consulte o item 5.1.4 - do Manual de orientações do FGTS Digital :](https://ajuda.sankhya.com.br/hc/article_attachments/42309861811607) |
| --- |

---

Esse evento permite que o sistema calcule corretamente a compensação do FGTS quando houver o adiantamento da 1ª parcela do 13º salário maior que o direito no momento da rescisão.

Ele subtrai essa diferença da base de incidência mensal do FGTS, como exige a norma.

**Exemplo prático**

**Antecipação da 1ª parcela do 13º salário**: R$ 1.500,00

![Imagem 4: Antecipação da 1ª parcela do 13º salário : R$ 1.500,00](https://ajuda.sankhya.com.br/hc/article_attachments/31768928305815)

**FGTS sobre a antecipação (8%)**: R$ 120,00

![Imagem 5: FGTS sobre a antecipação (8%) : R$ 120,00](https://ajuda.sankhya.com.br/hc/article_attachments/31769156570263)

Em **fevereiro/2025**, ocorre a **rescisão** do contrato do colaborador. No momento da rescisão, o valor devido de 13º salário proporcional é de **R$ 500,00**, resultando em **FGTS de R$ 40,00**.

Como já houve **antecipação de R$ 1.500,00**, o valor foi pago **a maior** em relação ao 13º proporcional.

![Imagem 6: Como já houve antecipação de R$ 1.500,00 , o valor foi pago a maior em relação ao 13º proporcional.](https://ajuda.sankhya.com.br/hc/article_attachments/31769129405463)

**Como o sistema irá calcular:**

- o evento **Desc1ªParc 13ºBase FGTS Mensal** (Cód. 316) será utilizado para ajustar o valor de FGTS que foi recolhido de forma antecipada;
- o restante da diferença continuará sendo tratado no evento Desconto 1ª Parc 13º Rescisão;
- o evento **Desc1ªParc 13ºBase FGTS Mensal** utilizará a incidência de FGTS mensal (cód. 11), garantindo o abatimento correto na base de cálculo.

![Imagem 7: o evento Desc1ªParc 13ºBase FGTS Mensal utilizará a incidência de FGTS mensal (cód. 11), garantindo o abatimento…](https://ajuda.sankhya.com.br/hc/article_attachments/31769295582871)

**Resultado da rescisão:**

![Imagem 8: Resultado da rescisão:](https://ajuda.sankhya.com.br/hc/article_attachments/31769372860439)

![Imagem 9: Resultado da rescisão:](https://ajuda.sankhya.com.br/hc/article_attachments/31769372866967)

Como **já houve recolhimento de R$ 120,00** sobre a antecipação do 13º, na rescisão, **o recolhimento complementar será de R$ 74,28**.

![Imagem 10: Como já houve recolhimento de R$ 120,00 sobre a antecipação do 13º, na rescisão, o recolhimento complementar será de R$…](https://ajuda.sankhya.com.br/hc/article_attachments/31769414798359)

Em resumo, o evento 315 foi desmembrado em dois eventos distintos para permitir o tratamento adequado do FGTS na rescisão. Portanto, o valor que seria descontado no evento 315 não muda, apenas ocorre em dois eventos separados.

Essa separação garante que o valor pago a maior na antecipação da 1ª parcela do 13º salário seja compensado corretamente, utilizando a base de FGTS mensal, e não a base do 13º. Com isso, o sistema realiza a dedução proporcional na base do FGTS rescisório, conforme determina a legislação.
