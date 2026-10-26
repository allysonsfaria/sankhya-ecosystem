---
id: "360043061853"
titulo: "Informado idEstrangeiro e Operação não é com consumidor final (NT2015/002)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043061853-Informado-idEstrangeiro-e-Opera%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-com-consumidor-final-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:09:10Z"
rotulos: ["ERRONF", "Configuração", "Parceiro", "NF-e", "SEFAZ", "CFOP", "721", "idEstrangeiro usado em operações não destinadas ao exterior", "Rejeição [721] - idEstrangeiro e operação incorreta", "Ajuste classificação do parceiro e CFOP; preencha idEstrangeiro para operações internacionais", "Identificação de Estrangeiro"]
---

# Informado idEstrangeiro e Operação não é com consumidor final (NT2015/002)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16474094598167) MENSAGEM:**

[721- Rejeição]: Informado idEstrangeiro e Operação não é com consumidor final (NT2015/002)

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474094598807) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Caso seja realizada uma operação para o Exterior, o parceiro da NF-e deve estar classificado como 'Consumidor Final Não…](https://ajuda.sankhya.com.br/hc/article_attachments/16474094599959) Caso seja realizada uma operação para o Exterior, o parceiro da NF-e deve estar classificado como 'Consumidor Final Não Contribuinte' e o CFOP deve iniciar-se com 7.

- Cadastro do Parceiro, aba "**Fiscal"**, campo "**Classificação ICMS"**= 'Consumidor Final Não Contribuinte'
- Cadastro da "[**TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)" (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), aba "**Livro Fiscal"**, em ' CFOP's para Fora do Estado': verifique com Contador o CFOP a ser utilizado, respeitando a regra de iniciar em 7.

![Imagem 4: Na tela " Parceiros " (Caminho de acesso: Configuração » Cadastro » Parceiro ), aba " Identificação" , o campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/16474094600727) Na tela "**[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494)"** (Caminho de acesso: Configuração » Cadastro » Parceiro), aba "**Identificação"**, o campo "**Identificação de Estrangeiro"** deve ser preenchido:

![Imagem 5: Na tela " Parceiros " (Caminho de acesso: Configuração » Cadastro » Parceiro ), aba " Identificação" , o campo "…](https://ajuda.sankhya.com.br/hc/article_attachments/14494307142551)

A informação neste campo tem a finalidade de informar na geração da NF-e a tag <idEstrangeiro> no caso de operação com o exterior, ou para comprador estrangeiro. Assim, informa-se o número do passaporte ou outro documento legal que identifique a pessoa estrangeira; este campo pode permanecer vazio para outras situações. A informação aqui inserida, deve conter no mínimo 5 e no máximo 20 caracteres/números.

Para mais informações sobre configurações relacionadas a parceiro estrangeiro, verificar o artigo: [Como cadastrar Parceiro ESTRANGEIRO ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474)

(1)** Caso não trate-se de uma Operação para o Exterior:**

![Imagem 6: Se for realizada uma Operação Nacional (Estadual/Interestadual), analise:](https://ajuda.sankhya.com.br/hc/article_attachments/16474094599959) Se for realizada uma Operação Nacional (Estadual/Interestadual), analise:

- Campo "**Identificação de Estrangeiro"** não deverá estar preenchido;
- CFOP não iniciará em 7;
- Endereço do Parceiro da NF-e, a UF que está sendo utilizada não poderá ser simbolizada por EX.

![Imagem 7: Após os ajustes, realize um novo lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16474094600727) Após os ajustes, realize um novo lançamento.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16474094602263) CAUSA:**

Quando for emitida uma NF-e com Destinatário do Exterior, onde o Destino da Mercadoria ocorre dentro do Brasil, podendo ser uma Operação Estadual ou Interestadual e a Operação não for igual a "1 - Consumidor Final", será retornado a rejeição.

**![Imagem 9: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16474094603031) OBSERVAÇÃO:**

([NT](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=)[2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hDS5co/qWOc=)) - Nota Técnica.
