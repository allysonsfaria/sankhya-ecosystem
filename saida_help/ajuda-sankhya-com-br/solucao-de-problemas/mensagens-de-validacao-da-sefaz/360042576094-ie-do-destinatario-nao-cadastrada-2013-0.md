---
id: "360042576094"
titulo: "IE do destinatário não cadastrada(2013/005)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042576094-IE-do-destinat%C3%A1rio-n%C3%A3o-cadastrada-2013-005"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:20Z"
rotulos: ["ERRONF", "ERROMDFE", "Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "233", "Consulte Inscrição Estadual no SINTEGRA", "Ajuste IE e Classificação de ICMS na tela \"Parceiros\"", "Gere novo lote e verifique situação cadastral", "Erro"]
---

# IE do destinatário não cadastrada(2013/005)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16474436254871) MENSAGEM:**

[233 - Rejeição]: IE do destinatário não cadastrada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474482601111) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Consulte o CNPJ do destinatário no SINTEGRA para verificar qual Inscrição Estadual está vinculada ao seu CNPJ.](https://ajuda.sankhya.com.br/hc/article_attachments/16474482602391) Consulte o CNPJ do destinatário no SINTEGRA para verificar qual Inscrição Estadual está vinculada ao seu CNPJ.

<http://www.sintegra.gov.br/>

Através do link acima, selecione o Estado do respectivo parceiro destinatário e realize a consulta de seu CNPJ. Veja o exemplo abaixo para um parceiro de Minas Gerais:

[GIF animado: Imagem 4: Através do link acima, selecione o Estado do respectivo parceiro destinatário e realize a consulta de seu CNPJ. Veja o…](https://ajuda.sankhya.com.br/hc/article_attachments/360088807753)

![Imagem 5: Confira se a IE informada corresponde a Inscrição inserida no cadastro do parceiro:](https://ajuda.sankhya.com.br/hc/article_attachments/16474436260759) Confira se a IE informada corresponde a Inscrição inserida no cadastro do parceiro:

- Tela "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso: Configurações » Cadastros) » Aba "**Identificação"**:

![Imagem 6: Tela " Parceiros " (Caminho de acesso: Configurações » Cadastros ) » Aba " Identificação" :](https://ajuda.sankhya.com.br/hc/article_attachments/14500103249687)

![Imagem 7: Caso a Inscrição esteja correta, na consulta ao site do Sintegra verifique se o campo '" Situação Cadastral"…](https://ajuda.sankhya.com.br/hc/article_attachments/16474436262551) Caso a Inscrição esteja correta, na consulta ao site do Sintegra verifique se o campo '"**Situação Cadastral"** encontra-se com a situação '**Habilitado - ATIVO**'. Caso esteja inativo, sintonize junto ao parceiro, se necessário retire essa informação e ajuste a 'Classificação de ICMS' vinculada em seu cadastro:

- Tela 'Parceiros' (Caminho de acesso: Configurações » Cadastros) » Aba "**Fiscal**" » Campo **"Classificação de ICMS"**

![Imagem 8: Realizado os ajustes acima, redigite o cabeçalho da nota e gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16474436264983) Realizado os ajustes acima, redigite o cabeçalho da nota e gere um novo lote.

**![Imagem 9: IMPORTANTE :](https://ajuda.sankhya.com.br/hc/article_attachments/16474482606487) IMPORTANTE:**

Para destinatários do '**Distrito Federal**', ao realizar a consulta no Sintegra, verifique se existem informações para o campo '**CF/DF' (Cadastro Fiscal do Distrito Federal).**Caso exista, preencha essa informação no campo 'Inscrição Estadual'.

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474436267287) CAUSA:**

A rejeição será retornada quando uma NF-e  (modelo 55) for transmitida e a I.E. cadastrada no sistema for inválida, ou então, não estiver devidamente cadastrada na SEFAZ Estadual.

Geralmente o XML gerado, a tag (IndIEDest = 2) para Isento ou Não Contribuinte(IndIEDest = 9), porém a I.E está ativa no Estado UF do parceiro.

**![Imagem 11: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474482612119) OBSERVAÇÃO:**

O sistema Sankhya possui a função de estruturar o XML conforme os dados cadastrados, para o envio a SEFAZ. Caberá a mesma a recepção desta nota e o retorno.

**(2)** ([NT](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)[2013/005](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=%20tq7zNwy6jo=)) - Nota Técnica.
