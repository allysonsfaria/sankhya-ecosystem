---
id: "360042726354"
titulo: "Saiba mais sobre: tag <vICMSDeson> e a rejeição:  Não informado valor do ICMS desonerado ou o Motivo de desoneração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042726354-Saiba-mais-sobre-tag-vICMSDeson-e-a-rejei%C3%A7%C3%A3o-N%C3%A3o-informado-valor-do-ICMS-desonerado-ou-o-Motivo-de-desonera%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-11T18:03:45Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "XML", "SEFAZ", "ICMS", "Impostos", "934", "ICMSDeson", "cBenef", "motDesICMS", "Rejeição 934: Falta de Valor ou Motivo do ICMS Desonerado"]
---

# Saiba mais sobre: tag <vICMSDeson> e a rejeição:  Não informado valor do ICMS desonerado ou o Motivo de desoneração

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16513693039127) MENSAGEM:**

[934 - Rejeição]: Não informado valor do ICMS desonerado ou o Motivo de desoneração.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513693042327) SOLUÇÃO:**

Para correção, siga os passos abaixo:

Quando trabalharmos com Beneficio Fiscal, tag <cBenef>, será obrigatório informar o  valor do ICMS desonerado, tag <ICMSDeson>, e o motivo de desoneração, tag <motDesICMS>.

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16513693043479) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

  Selecione o Estado de Origem » Estado de Destino,

- Preencha o CST de Tributação
- Preencha o campo **"Alíquota" e "%ICMS FCP Interno"**
- Preencha corretamente o campo **"Cód. Mot. Desoneração ICMS".**
- No tópico 'Repassar para o Cliente' se informado 'Cód. Mot. Desoneração ICMS', preencha conforme a necessidade.

![Imagem 4: No tópico 'Repassar para o Cliente' se informado 'Cód. Mot. Desoneração ICMS', preencha conforme a necessidade.](https://ajuda.sankhya.com.br/hc/article_attachments/14636501508759)

![Imagem 5: Acesse: Configurações » Cadastros » Produtos » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16513693045271) Acesse: Configurações » Cadastros » Produtos » Produtos

Aba **"Impostos":**

Campo: **"Cód. de Benefício Fiscal na UF":** Informe o respectivo Código, o mesmo deverá ser disponibilizado pela Contabilidade.

![Imagem 6: Campo: "Cód. de Benefício Fiscal na UF": Informe o respectivo Código, o mesmo deverá ser disponibilizado pela…](https://ajuda.sankhya.com.br/hc/article_attachments/14636588142487)

![Imagem 7: Após os ajustes, gere o Lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16513693047959) Após os ajustes, gere o Lote novamente.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16513693049495) CAUSA:**

Quando realizada operação com CST (Tributação):

20 - Com redução de base de cálculo
30 - Isenta ou não tributada e com cobrança do ICMS por substituição tributária
40 - Isenta
41 - Não tributada
50 - Suspensão
51 - Diferimento
60 - ICMS cobrado anteriormente por substituição tributária
70 - Com redução de base de cálculo e cobrança do ICMS por substituição tributária
90 - Outras

E a tag**<vICMSDeson>** e **<motDesICMScBenef>** não forem preenchidas.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513693056023) OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota técnica
