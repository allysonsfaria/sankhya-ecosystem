---
id: "16861371221015"
titulo: "ICMS com desoneração (Suframa) e ST (CST 30) de SP/AP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16861371221015-ICMS-com-desonera%C3%A7%C3%A3o-Suframa-e-ST-CST-30-de-SP-AP"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:54:15Z"
rotulos: ["Configuração", "Fiscal", "SUFRAMA", "ICMS", "Impostos", "ST", "Desoneração ICMS cálculo ST com valor total", "Sistema não suporta essa configuração atualmente", "Use \"0 - Não específico\" e \"Considera desconto no cálculo de ST por IVA\""]
---

# ICMS com desoneração (Suframa) e ST (CST 30) de SP/AP

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16861356708375) SITUAÇÃO:**

Cliente vende para o Amapá com desoneração Suframa e precisa desonerar apenas o ICMS e calcular a ST normalmente utilizando o valor total dos itens, sem a redução do ICMS na base do ST.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16861382038807) SOLUÇÃO:**

Atualmente o sistema não está preparado para fazer o seguinte cálculo desonerando o ICMS, mas usando o valor total sem a desoneração para calculo do ST.

**![Imagem 3: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16861353469975) OBSERVAÇÃO:**

Segue abaixo uma sugestão de configuração que poderá atender a necessidade, entretanto caso não satisfaça a necessidade é preciso solicitar análise de projetos adaptativos.

Acesse a tela **Alíquotas de ICMS -** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS aba "Substituição Tributária" em "Tipo de Cálculo de ST Específico" usar a opção "0 - Não especifico (Regra Geral)", além disso utilize a configuração "Considera desconto no cálculo de ST por IVA" na tela **Parceiros -** Configurações » Cadastros » Parceiros na aba "Fiscal".

Estas configurações calculam como esperado as bases de cálculo, tanto ICMS quanto a base de ST, porém não haverá o destaque do ICMS desonerado.
