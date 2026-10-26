---
id: "29660326768919"
titulo: "Veja como configurar o cálculo FCP/ST Interno para pedidos de vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29660326768919-Veja-como-configurar-o-c%C3%A1lculo-FCP-ST-Interno-para-pedidos-de-vendas"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-09-15T18:38:01Z"
rotulos: ["Configuração", "NF-e", "ICMS", "Impostos", "TOP", "Tributação", "Cálculo FCP/ST Interno - Para Pedidos de Vendas", "ICMS FCP Interno", "ST FCP Interno/Coeficiente FECOP", "FCP"]
---

# Veja como configurar o cálculo FCP/ST Interno para pedidos de vendas

#### Para que o  cálculo do FCP/ST Interno aconteça, configure os seguintes cadastros:

![Imagem 1: Acesse a tela Alíquotas de ICMS (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS), vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/29806884360855) Acesse a tela **Alíquotas de ICMS** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS), vá até a aba **"Substituição Tributária"** e preencha o campo **"ST FCP Interno/Coeficiente FECOP".** 

![Imagem 2: Acesse a tela Alíquotas de ICMS (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS), vá até a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/29806884363671)

![Imagem 3: Acesse a tela Alíquotas de ICMS (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS) , aba "Geral",…](https://ajuda.sankhya.com.br/hc/article_attachments/29806884365719) Acesse a tela **Alíquotas de ICMS** (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS), aba **"Geral",** informe o campo **"ICMS FCP Interno"** e preencha o campo **"Tributação"** com uma das opções abaixo:

00 - Tributada integralmente;
10 - Tributada e com cobrança do ICMS por ST;
20 - Com redução de base de cálculo;
51 - Com diferimento;
70 - Com redução de base de cálculo e cobrança do ICMS por ST;
90 - Outras.

![Imagem 4: 00 - Tributada integralmente; 10 - Tributada e com cobrança do ICMS por ST; 20 - Com redução de base de cálculo; 51 -…](https://ajuda.sankhya.com.br/hc/article_attachments/29806862083735)

![Imagem 5: Acesse a tela Tipos de Operação - TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba "Impostos" e…](https://ajuda.sankhya.com.br/hc/article_attachments/29806884369303) Acesse a tela **Tipos de Operação - TOP** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba **"Impostos"** e marque o flegue **"Calcular FCP (ICMS/ST) Interno?".**

![Imagem 6: Acesse a tela Tipos de Operação - TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba "Impostos" e…](https://ajuda.sankhya.com.br/hc/article_attachments/29806862088215)

**Nota:** A empresa precisa estar configurada para NF-e 4.00.

![Imagem 7: Nota: A empresa precisa estar configurada para NF-e 4.00.](https://ajuda.sankhya.com.br/hc/article_attachments/31605247910551)

**Porém** se no campo citado acima (print) estiver como **Versão NFe 4.0 e NFCe 3.10** o modelo de documento da TOP, deve estar como **55.**

Com essas configurações, o sistema irá processar os cálculos do FCP ST, aplicando as regras/cálculos usados no cálculo do ST normal.
