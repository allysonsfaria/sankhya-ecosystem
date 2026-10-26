---
id: "30877925152791"
titulo: "EFD ICMS/IPI | Registro G125 - Campo 10 VL_PARC_PASS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30877925152791-EFD-ICMS-IPI-Registro-G125-Campo-10-VL-PARC-PASS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:34:31Z"
rotulos: ["Produtos", "Configuração", "Bens", "ICMS", "Impostos", "EFD", "Preferências", "EFD ICMS/IPI- Registro G125 - Campo 10 VL_PARC_PASS", "Valor da parcela de ICMS passível de apropriação", "CIAP"]
---

# EFD ICMS/IPI | Registro G125 - Campo 10 VL_PARC_PASS

Para que o sistema gere o valor do campo **"Valor da parcela de ICMS passível de apropriação"** do registro G125, o sistema realiza as seguintes validações:

Na tela **"Produtos",** aba **"Bens"** (lembrando que essa aba somente aparecerá se o produto estiver marcado como "Imobilizado, na aba "Geral"), sub-aba **"Bens",** existe a aba **"CIAP"**, nesta aba, temos os seguintes campos:

**Valor do ICMS**

**Valor crédito de ICMS dif. alíquota**

**Valor crédito ICMS por subst. tributária**

Para o preenchimento do campo citado no título, o sistema vai somar esses três campos, e dividir pela quantidade de parcelas de meses definido.

**Observação:** O campo Valor crédito de ICMS dif. alíquota só será considerado na equação se a marcação **"Desconsiderar crédito Dif.Alíquota no CIAP",** na tela **"Empresa** (Comercial » Preferências » Empresa), **estiver desabilitada:**

![Imagem 1: Valor crédito de ICMS dif. alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/30975563254039)

![Imagem 2: Valor crédito de ICMS dif. alíquota](https://ajuda.sankhya.com.br/hc/article_attachments/30975563255063)

(1)** Resultado no txt do EFD FISCAL**

R$ 1,20 + R$2,00 + R$0,87 = R$4,07

R$4,07 / 48 = R$ 0,08

![Imagem 3: R$4,07 / 48 = R$ 0,08](https://ajuda.sankhya.com.br/hc/article_attachments/30975563255831)
