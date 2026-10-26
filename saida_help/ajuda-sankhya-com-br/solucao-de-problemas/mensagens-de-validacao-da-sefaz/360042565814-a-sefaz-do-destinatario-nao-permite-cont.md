---
id: "360042565814"
titulo: "A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual (NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042565814-A-SEFAZ-do-destinat%C3%A1rio-n%C3%A3o-permite-Contribuinte-Isento-de-Inscri%C3%A7%C3%A3o-Estadual-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-08T13:14:23Z"
rotulos: ["ERRONF", "Configuração", "Fiscal", "Parceiro", "NF-e", "SEFAZ", "Impostos", "805", "Verificar e ajustar IE do destinatário", "IE incompatível com normas estaduais", "Rejeição IE Destinatário"]
---

# A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual (NT2015/003)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16475589136535) MENSAGEM:**

[805 - Rejeição]: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual (NT2015/003)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16475589141015)SOLUÇÃO:**

Para correção, siga os passos abaixo.

![Imagem 3: Verifique no site Sintegra se o parceiro destinatário da nota possui Inscrição Estadual cadastrada.](https://ajuda.sankhya.com.br/hc/article_attachments/16475589142039)  Verifique no site [Sintegra](http://www.sintegra.gov.br/)se o parceiro destinatário da nota possui Inscrição Estadual cadastrada.

- Caso o parceiro tenha I.E., a mesma deve ser devidamente preenchida em seu cadastro, aba **"Identificação"**, campo **"I.E./RG"**.

![Imagem 4: Acesse " Parceiros" (Caminho de acesso: Configurações » Cadastros )](https://ajuda.sankhya.com.br/hc/article_attachments/16475542607383) Acesse "[**Parceiros"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)(Caminho de acesso: Configurações » Cadastros)

Aba: "**Fiscal"** » Campo: "**Classificação de ICMS"**

Ajuste conforme detalhes a seguir:

- "1 - Consumidor Final Contribuinte"/ Produtor Rural **OU**
- "9 - Consumidor Final Não Contribuinte".

![Imagem 5: Para tal, sintonize com seu parceiro e/ou contador, a classificação fiscal correta e realize os devidos ajustes.](https://ajuda.sankhya.com.br/hc/article_attachments/16475589153687) Para tal, sintonize com seu parceiro e/ou contador, a classificação fiscal correta e realize os devidos ajustes.

**![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16475542615703) IMPORTANTE:**

Nessas duas identificações, o destinatário pode possuir IE cadastrada, mas apenas em identificação como 'Consumidor Final Contribuinte' deve ser informado a IE, obrigatoriamente.

![Imagem 7: Em "Tipos de Operação - TOP" (Comercial » Arquivo » Cadastros) » Aba: "Impostos"](https://ajuda.sankhya.com.br/hc/article_attachments/16475589142039) Em **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros) » Aba: **"Impostos"**

Campo **"Classificação ICMS":** 'Usar do Parceiro'

![Imagem 8: Após os ajustes, redigite o parceiro no cabeçalho da nota e posteriormente gere o Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16475542607383) Após os ajustes, redigite o parceiro no cabeçalho da nota e posteriormente gere o Lote.

![Imagem 9: Informe no parâmetro " UFNFECOMIEHOM " a UF da empresa emitente.](https://ajuda.sankhya.com.br/hc/article_attachments/16475589153687) Informe no parâmetro "**UFNFECOMIEHOM**" a UF da empresa emitente.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16475589162519) CAUSA:**

Este erro ocorre por causa da identificação da IE (Campo: dest / indIEDest - ID: E16a) como "2 - Contribuinte Isento de Inscrição Estadual" em Estado (UF) que não permite essa identificação da IE.

Os Estados que não permitem que os destinatário tenham indicação como Contribuinte Isento são: **AM, BA, CE, GO, MG, MS, MT, PA, PE, RN e SP**.

(1)** Exemplo:**

Foi emitida uma NF-e para Destinatário localizado no CE (Ceará) com identificação para sua IE como Contribuinte Isento (indIEDest = 2). Como a Sefaz CE não permite Destinatário como Contribuinte Isento, a NF-e será rejeitada pelo motivo 805.

**![Imagem 11: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16475589169047)OBSERVAÇÕES:**

**(1)** Caso a operação seja em base de **Homologação**, verifique o parâmetro "**UFNFECOMIEHOM (UFs que exigem Insc. Estad. em homologação)"**  Caberá a SEFAZ Estadual validar ou não a I.E., caso seja validada, valide conforme orientações citadas nesse artigo.

**Obs.:** Caso a SEFAZ do estado em questão exija a Inscrição Estadual, mesmo sendo em base de homologação, configure o nome da UF no parâmetro citado acima. Exemplo:

![Imagem 12: Obs.: Caso a SEFAZ do estado em questão exija a Inscrição Estadual, mesmo sendo em base de homologação, configure o…](https://ajuda.sankhya.com.br/hc/article_attachments/14506802888599)

**(1)** (**NT2015/003**) Nota Técnica:

<http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=DRiCiO978HY=>
