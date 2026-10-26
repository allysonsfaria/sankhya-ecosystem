---
id: "360042626014"
titulo: "Operação com ICMS-ST sem informação do CEST.(NT2015/003)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626014-Opera%C3%A7%C3%A3o-com-ICMS-ST-sem-informa%C3%A7%C3%A3o-do-CEST-NT2015-003"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:21Z"
rotulos: ["ERRONF", "#PUBLIFER", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "806", "Falta de Informação do CEST em ICMS-ST", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "CEST"]
---

# Operação com ICMS-ST sem informação do CEST.(NT2015/003)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16510468478359) MENSAGEM:**

[806 - Rejeição]: Operação com ICMS-ST sem informação do CEST.(NT2015/003)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16510455058071) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 3: Verifique na tela "Preferências" , buscando pela chave "UFNFESEMCEST" se o seu estado está informado neste parâmetro.…](https://ajuda.sankhya.com.br/hc/article_attachments/16510455060375) Verifique na tela **"Preferências"**, buscando pela **chave "UFNFESEMCEST"** se o seu estado está informado neste parâmetro. Se estiver informado, esta é a principal causa de não estar sendo gerada informação de CEST no XML desta NF-e. Retire então o seu estado do texto e salve esta preferência. Caso não esteja informado nenhum estado, verifique o próximo passo desta solução.

![Imagem 4: Acesse: Configurações » Cadastros » Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/16510468487831) Acesse: Configurações » Cadastros » Produtos

**Aba:** Impostos

- Campo: "**Código Especificador ST"**:' [**Preencher o campo, com o valor correspondente a Tabela**]
- Caso a empresa trabalhe com "**Impostos por Empresa"**, acesse a aba: **"Impostos/Informações por Empresa"** no cadastro de Produto e preencha o campo "**Código Especificador ST**:" de acordo com a empresa da nota.
- Quando a Substituição Tributária for realizada na compra, no cadastro do produto o campo Tipo de Substituição precisa estar preenchido como Revenda com Substituição Tributária (ST na Compra).

![Imagem 5: Após o ajuste, redigite os itens na nota ou fature o pedido novamente. Gere o lote da NF-e e a mesma será autorizada.](https://ajuda.sankhya.com.br/hc/article_attachments/16510468493719) Após o ajuste, redigite os itens na nota ou fature o pedido novamente. Gere o lote da NF-e e a mesma será autorizada.

**![Imagem 6: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/16510455072151) OBSERVAÇÕES:**

![Imagem 7: Caso não localize esse campo na tela de cadastro de produtos, acesse a opção " Configuração da tela" » Configurações.…](https://ajuda.sankhya.com.br/hc/article_attachments/16510455060375) Caso não localize esse campo na tela de cadastro de produtos, acesse a opção "**Configuração da tela"** » Configurações. Digite "Cód" dentro de 'Campos Disponíveis' » Selecione o campo "**Código Especificador ST"** e arraste para o lado direito 'Campos Selecionados', através da seta "adicionar campo".

![Imagem 8: Caso não tenha a informação do CEST correspondente aos produtos será necessário acesso a Tabela do Código Especificador…](https://ajuda.sankhya.com.br/hc/article_attachments/16510468487831) Caso não tenha a informação do CEST correspondente aos produtos será necessário acesso a Tabela do Código Especificador da Substituição Tributária disponível no link <https://www.codigocest.com.br/>. Caso não encontre o código que necessita, poderá verificar com sua contabilidade.

![Imagem 9: ( NT2015/003 ) - Nota técnica](https://ajuda.sankhya.com.br/hc/article_attachments/16510468493719) ([NT2015/003](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=pLuHNFf7xvE=)) - Nota técnica

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16510455073815) CAUSA:**

Quando for emitida uma NF-e de operação sem a informação do Código Especificador da Substituição Tributária (CEST), e o CST ou o CSOSN de ICMS for um da lista abaixo, será retornado a rejeição.

| **CST** | **DESCRIÇÃO** |
| --- | --- |
| 10 | Tributada com cobrança de ICMS por substituição tributária. |
| 30 | Isenta ou não tributada com cobrança de ICMS por substituição tributária. |
| 60 | ICMS cobrado anteriormente por substituição tributária. |
| 70 | Com redução de base de cálculo e cobrança de ICMS por substituição tributária. |
| 90 | Outros, desde que com a TAG vICMSST |

Para empresas optantes pelo Simples Nacional:

| **CSOSN** | **DESCRIÇÃO** |
| --- | --- |
| 201 | Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por substituição tributária. |
| 202 | Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por substituição tributária. |
| 203 | Isenção de ICMS do Simples Nacional para a faixa de receita, com cobrança do ICMS por substituição tributária. |
| 500 | ICMS cobrado anteriormente por substituição tributária ou por antecipação. |
| 900 | Outros, desde que com a TAG vICMSST. |
