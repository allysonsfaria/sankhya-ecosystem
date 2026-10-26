---
id: "360042534354"
titulo: "Código Município do Emitente diverge do cadastrado na UF (NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042534354-C%C3%B3digo-Munic%C3%ADpio-do-Emitente-diverge-do-cadastrado-na-UF-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:57Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Cidades", "SEFAZ", "Rejeição código município", "Consulte site IBGE", "Atualize cadastro", "Erro"]
---

# Código Município do Emitente diverge do cadastrado na UF (NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16455185092887) MENSAGEM:**

[480 - Rejeição]: Código Município do Emitente diverge do cadastrado na UF (NT2015/002)'

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455236686743) SOLUÇÃO:**

Para correção, siga os passos abaixo.

![Imagem 3: Consulte no site SINTEGRA ou da Receita Federal, o cadastro e identificação do Município da Empresa(Emitente da NF-e)](https://ajuda.sankhya.com.br/hc/article_attachments/16455185104919) Consulte no site SINTEGRA ou da Receita Federal, o cadastro e identificação do Município da Empresa(Emitente da NF-e)

Pesquise no site do IBGE <https://cidades.ibge.gov.br/>, o Código do Município e insira no campo informado acima no cadastro de Cidades.

![Imagem 4: Acesse a tela : " Cidades" (Caminho de acesso: Configurações » Cadastros » Endereços » Cidades )](https://ajuda.sankhya.com.br/hc/article_attachments/16455236689943) Acesse a tela : **"**[**Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913) (Caminho de acesso: Configurações » Cadastros » Endereços » Cidades)

Aba "**Geral**", informe no campo: "**Mun. Domicílio Fiscal"** o Código do Município correto.

![Imagem 5: Aba " Geral ", informe no c ampo: " Mun. Domicílio Fiscal" o Código do Município correto.](https://ajuda.sankhya.com.br/hc/article_attachments/14438162288023)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16455236692503) CAUSA:**

Quando for emitida uma NF-e, e o Código do Município (cMun) informado para o Emitente for diferente do Código do Município cadastrado na mesma UF para esse mesmo Emitente, será retornado a rejeição.

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455185117079) OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=v9JbkEY7evI=)) - Nota Técnica.
