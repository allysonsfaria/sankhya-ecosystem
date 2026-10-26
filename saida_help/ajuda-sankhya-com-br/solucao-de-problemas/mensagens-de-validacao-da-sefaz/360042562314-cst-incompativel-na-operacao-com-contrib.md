---
id: "360042562314"
titulo: "CST incompatível na operação com Contribuinte Isento de Inscrição Estadual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042562314-CST-incompat%C3%ADvel-na-opera%C3%A7%C3%A3o-com-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:46Z"
rotulos: ["ERRONF", "#PUBLIFER", "#RevisadoClaudio", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "Impostos", "529", "CST incompatível na operação com Contribuinte Isento de Inscrição Estadual", "CST 50/51 e isenção IE", "Ajuste CST com contador"]
---

# CST incompatível na operação com Contribuinte Isento de Inscrição Estadual

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16460353342999) MENSAGEM:**

[529 - Rejeição]: CST incompatível na operação com Contribuinte Isento de Inscrição Estadual [nItem:1].

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16460321948439) SOLUÇÃO:**

![Imagem 3: Caso o parceiro destinatário seja "Contribuinte Isento de Inscrição Estadual" verifique com o Contador da empresa o CST…](https://ajuda.sankhya.com.br/hc/article_attachments/16460353348759) Caso o parceiro destinatário seja "Contribuinte Isento de Inscrição Estadual" verifique com o Contador da empresa o CST de ICMS adequado. Visto que a SEFAZ não permitirá os CST'S 50 ou 51.

- Em caso de dúvidas sobre como proceder com o ajuste dessa tributação, verifique o artigo "[Como identificar qual a alíquota/exceção de ICMS utilizada no lançamento?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043050753)". Ressaltamos a importância desse ajuste ser realizado por um usuário certificado na utilização do sistema.

![Imagem 4: Após realizar os ajustes para CST adequado a operação, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16460321953047) Após realizar os ajustes para CST adequado a operação, redigite o cabeçalho da nota e gere um novo lote.

![Imagem 5: Para os casos nos quais a tributação de fato seja 50 ou 51, acesse o cadastro do parceiro (Caminho de acesso:…](https://ajuda.sankhya.com.br/hc/article_attachments/16460353354263) Para os casos nos quais a tributação de fato seja 50 ou 51, acesse o cadastro do parceiro (Caminho de acesso: Configurações » Cadastros » Parceiros) e revise as configurações do campo "**Classificação ICMS"** da aba "**Fiscal"**.

- Para ICMS com Suspensão ou Diferimento, somente é permitido destinatário identificado como "Contribuinte do ICMS" (indIEDest = 1). Dessa forma, informe o destinatário da NF-e como Contribuinte do ICMS e sua respectiva Inscrição Estadual.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16460321955863) IMPORTANTE:**

Caso a emissão ocorra em **ambiente homologação,** atente-se ao parâmetro 'UFNFECOMIEHOM: "UFs que exigem Insc. Estad. em homologação"': insira o Estado do destinatário na lista, separando por vírgula dos demais Estados já presentes no parâmetro. Assim, a tag IE será gerada mesmo em ambiente de homologação.

![Imagem 7: Caso a emissão ocorra em ambiente homologação, atente-se ao parâmetro 'UFNFECOMIEHOM: "UFs que exigem Insc. Estad. em…](https://ajuda.sankhya.com.br/hc/article_attachments/11991040257559)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16460321959319) CAUSA:**

Quando for emitida uma NF-e com Identificação do Destinatário (<indIEDest>) igual a '2 - Contribuinte Isento de Inscrição Estadual' e o CST do ICMS for "50 - Suspensão na cobrança do ICMS" ou "51 - Diferimento na cobrança do ICMS", será retornada a rejeição.

Exceções:

- A regra de validação não se aplica para o CST = 50 (Suspensão), nas operações com CFOP de conserto ou reparo (CFOP 1915, 1916, 2915, 2916, 5915, 5916, 6915 e 6916) ou de remessa para demonstração dentro do Estado (CFOP 1912, 1913, 5912 e 5913);
- A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016;
- A critério da UF, a regra de validação não se aplica para CST = 51 (Diferimento) em operações internas (idDest = 1) quando o destinatário for Pessoa Jurídica.
- A regra não se aplica na emissão da NFA-e nas operações internas.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16460353369239) OBSERVAÇÃO:**

([NT2016/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=zfWxcJtOf98=)) - Nota técnica.
