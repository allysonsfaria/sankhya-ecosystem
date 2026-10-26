---
id: "9448417531799"
titulo: "O CFOP XX não está cadastrado no sistema. Caso seja válido, o mesmo deve ser incluído no cadastro de CFOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9448417531799-O-CFOP-XX-n%C3%A3o-est%C3%A1-cadastrado-no-sistema-Caso-seja-v%C3%A1lido-o-mesmo-deve-ser-inclu%C3%ADdo-no-cadastro-de-CFOP"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:07:51Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Impostos", "TOP", "CFOP", "CORE_E01540", "Necessidade de Cadastro de CFOP no Sistema"]
---

# O CFOP XX não está cadastrado no sistema. Caso seja válido, o mesmo deve ser incluído no cadastro de CFOP

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18613663521431) MENSAGEM:**

[CORE\_E01540]  O CFOP XX não está cadastrado no sistema. Caso seja válido, o mesmo deve ser incluído no cadastro de CFOP.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613687868567) SITUAÇÃO:**

Ao lançar uma nota a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18613687874967) CAUSA:**

Poderá ocorrer quando a CFOP não está cadastrada, ou se o parceiro não é revendedor ou o produto vendido não está definido como revenda e a CFOP selecionada não condiz com essas configurações.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18613663540759) SOLUÇÃO:**

Verifique algumas configurações:

- Verifique se a classificação ICMS no cadastro do Parceiro está informado corretamente para que puxe o CFOP corretamente, caso esteja configurado corretamente, necessário seguir as próximas orientações.

![Imagem 5: Verifique se a classificação ICMS no cadastro do Parceiro está informado corretamente para que puxe o CFOP…](https://ajuda.sankhya.com.br/hc/article_attachments/18613687886871)

- Acesse a tela **CFOP** (Comercial » Arquivo » Cadastros » CFOP) e realizar o cadastro do CFOP utilizado.

Não sendo a correta, avalie se a CFOP condiz com a operação a ser realizada pois algum dos cadastros no sistema podem estar incorretos podendo ser:

Alguns campos afetam diretamente o cálculo do CFOP:

- No [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), os campos das Seções **"CFOP para FORA do Estado "**e**" CFOP para DENTRO do Estado"**;
- No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba [Impostos / Informações por empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostosinformaesporempresa) e [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaimpostos), os campos **"Uso do produto "**e **"Tipo de substituição"** respectivamente.

Por fim, verifique no cadastro de **Produtos** (Configurações » Cadastros » Produtos » Produtos) se o campo "Usado como" está definido corretamente.

![Imagem 6: Por fim, verifique no cadastro de Produtos (Configurações » Cadastros » Produtos » Produtos) se o campo "Usado como"…](https://ajuda.sankhya.com.br/hc/article_attachments/18613663547927)
