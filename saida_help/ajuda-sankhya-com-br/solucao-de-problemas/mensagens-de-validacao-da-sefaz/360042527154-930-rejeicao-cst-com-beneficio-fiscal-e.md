---
id: "360042527154"
titulo: "930 Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal [nItem: nnn]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042527154-930-Rejei%C3%A7%C3%A3o-CST-com-benef%C3%ADcio-fiscal-e-n%C3%A3o-informado-o-c%C3%B3digo-de-benef%C3%ADcio-fiscal-nItem-nnn"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-10-20T19:09:42Z"
rotulos: ["ERRONF", "Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "930", "CST sem benefício fiscal", "Informe cód. de benefício", "Ajuste na tela Produtos", "Rejeição 930", "930 Rejeição"]
---

# 930 Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal [nItem: nnn]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16457540457367) MENSAGEM:**

930 Rejeição: CST com benefício fiscal e não informado o código de benefício fiscal.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457491358999) SOLUÇÃO:**

Para correção, siga os passos abaixo:
Quando trabalharmos com Desoneração do ICMS, tag <motDesICMS>, será obrigatória a informação do 'Cód. de Benefício Fiscal na UF', para isso:

![Imagem 3: Acesse a tela " Produtos" : (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos )](https://ajuda.sankhya.com.br/hc/article_attachments/16457540461335) Acesse a tela "[**Produtos"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) : (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)

- Aba "**Impostos"**
- Campo "**Cód. de Benefício Fiscal na UF"**: informe o respectivo Código, o mesmo deverá ser disponibilizado pela Contabilidade.

![Imagem 4: Campo " Cód. de Benefício Fiscal na UF" : informe o respectivo Código, o mesmo deverá ser disponibilizado pela…](https://ajuda.sankhya.com.br/hc/article_attachments/14448334486807)

Se o código for preenchido após o lançamento do produto na Nota, exclua o item na nota e faça novamente o lançamento, para puxar o código.

![Imagem 5: Acesse a tela " Empresa ": (Caminho de acesso: Comercial » Preferências » Empresa )](https://ajuda.sankhya.com.br/hc/article_attachments/16457491365271) Acesse a tela "[**Empresa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)": (Caminho de acesso: Comercial » Preferências » Empresa)

- Aba: "**NFe/ NFC-e"**
- Campos: "**Considere Benefícios ao incluir/alterar item da nota"=** [Marcado], "**Atualização Cód. Beneficio no Faturamento pelo Produto**"=Sempre Atualizar

![Imagem 6: Campos: " Considere Benefícios ao incluir/alterar item da nota"= (Marcado), " Atualização Cód. Beneficio no Faturamento…](https://ajuda.sankhya.com.br/hc/article_attachments/14448431436439)

![Imagem 7: Após os ajustes, gerar o Lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16457540466583) Após os ajustes, gerar o Lote novamente.

![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16457540468887) **CAUSA:**

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

E a tag **<cBenef>** não for preenchida.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16457491373975) OBSERVAÇÃO:**

([NT2019/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=RD1XRVxKLtI=)) - Nota Técnica.
