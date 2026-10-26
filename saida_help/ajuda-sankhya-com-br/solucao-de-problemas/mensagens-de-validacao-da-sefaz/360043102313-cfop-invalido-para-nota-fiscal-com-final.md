---
id: "360043102313"
titulo: "CFOP inválido para Nota Fiscal com finalidade de devolução de mercadoria(NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102313-CFOP-inv%C3%A1lido-para-Nota-Fiscal-com-finalidade-de-devolu%C3%A7%C3%A3o-de-mercadoria-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:26Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "CFOP", "Devolução", "327", "327 - Rejeição", "CFOP inválido devolução", "Ajuste CFOP conforme tabela"]
---

# CFOP inválido para Nota Fiscal com finalidade de devolução de mercadoria(NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16506433957783) MENSAGEM:**

[327 - Rejeição]: CFOP inválido para Nota Fiscal com finalidade de devolução de mercadoria.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16506405357335) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Se realmente tratar-se de uma nota de DEVOLUÇÃO, ajuste o CFOP para um dos listados na tabela ilustrada ao final desse…](https://ajuda.sankhya.com.br/hc/article_attachments/16506433962519) Se realmente tratar-se de uma nota de **DEVOLUÇÃO,** ajuste o CFOP para um dos listados na tabela ilustrada ao final desse artigo, sintonizando com seu contador o mais adequado.

- O ajuste deve ser realizado no cadastro do Tipo de Operação, aba Livro Fiscal, campos de CFOP'S.

![Imagem 4: Caso não se trate de uma NF-e de Devolução, sendo um retorno de remessa, por exemplo, ajuste o campo "NF-e" do cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/16506433966231) Caso não se trate de uma NF-e de Devolução, sendo um retorno de remessa, por exemplo, ajuste o campo **"NF-e"** do cadastro da TOPTela **"[Tipos de Operação -TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)"** (Caminho de acesso: Comercial » Arquivo » Cadastros/Financeiro » Arquivos » Cadastros) » aba: "**NF-e/NFC-e"** para diferente de **"Devolução":**

![Imagem 5: Caso não se trate de uma NF-e de Devolução, sendo um retorno de remessa, por exemplo, ajuste o campo "NF-e" do cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/14605415961111)

Ou, verifique se já existe uma TOP de devolução com finalidade diferente dessa, que atenda sua necessidade.

![Imagem 6: Após ajustes na TOP, inutilize/exclua a nota e realize um novo faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16506405366935) Após ajustes na TOP, inutilize/exclua a nota e realize um novo faturamento.

Importante: O sistema irá gerar <finNFe> = 4, desde que o CFOP utilizado na operação esteja dentro do parâmetro **"CFOPDEVOLUCAO".**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16506405386007) CAUSA:**

A operação é considerada uma Devolução de Mercadoria através da tag  <finNFe>4</finNFe>, onde a SEFAZ realiza comparação de CFOP x Finalidade.

(1)** Exceção a regra:**

Aceitar os CFOP 1.949 e 2.949 na devolução de venda para não Contribuinte. Para estes CFOP verificar a condição: finNFe = 4 (devolução) e indIEDest = 9 (não Contribuinte).

**![Imagem 8: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16506405390615) OBSERVAÇÕES:**

![Imagem 9: ( NT2015/002 ) - Nota Técnica:](https://ajuda.sankhya.com.br/hc/article_attachments/16506433962519) ([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota Técnica:

![Imagem 10: Tabela CFOP's com Finalidade Devolução.](https://ajuda.sankhya.com.br/hc/article_attachments/16506433966231) Tabela CFOP's com Finalidade Devolução.

![Imagem 11: Tabela CFOP's com Finalidade Devolução.](https://ajuda.sankhya.com.br/hc/article_attachments/360060880733)
