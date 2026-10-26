---
id: "9033387763607"
titulo: "O código NCM do produto xxx é inválido.  O mesmo deve possuir 8 dígitos. Atualize com o código NCM correto no cadastro do produto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9033387763607-O-c%C3%B3digo-NCM-do-produto-xxx-%C3%A9-inv%C3%A1lido-O-mesmo-deve-possuir-8-d%C3%ADgitos-Atualize-com-o-c%C3%B3digo-NCM-correto-no-cadastro-do-produto"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:11:20Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NCM", "CORE_E04463", "Código NCM inválido", "Ajuste no cadastro de produtos", "Serviço: NCM deve estar em branco", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# O código NCM do produto xxx é inválido.  O mesmo deve possuir 8 dígitos. Atualize com o código NCM correto no cadastro do produto

**MENSAGEM:**
[CORE\_E04463]: O código NCM do produto xxx é inválido. O mesmo deve possuir 8 dígitos. Atualize com o código NCM correto no cadastro do produto.

**SITUAÇÃO:**

- Ao gerar o ajuste de estoque;
- Ao tentar processar uma nota pelo portal de importação de XML;
- Ao tentar confirmar um pedido de serviço que não possui NCM;
- Ao tentar utilizar um NCM em uma nota fiscal, o sistema retorna a mensagem "NCM não existe ou não pode ser usado aqui";
- Durante o cadastro de produtos, o NCM desejado não aparece na pesquisa.

**SOLUÇÃO:**

Acesse o cadastro de **produtos** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos)  e ajuste o campo NCM corretamente.

![Imagem 1: Acesse o cadastro de produtos (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) e ajuste o campo NCM…](https://ajuda.sankhya.com.br/hc/article_attachments/16668190912535)

**IMPORTANTE:**

Caso seja um serviço, verifique se o campo NCM está preenchido. Pois, o mesmo deverá estar em branco. Para isso, é siga uma das opções abaixo:

- Cadastre o NCM 000 no cadastro de NCM e vincule o ao Serviço ou;
- Informe a primeira letra dos tipos de utilização de produtos do campo **"Usado como"** da aba **"Geral",** do Cadastro de Produtos que não passarão pela validação de NCM,

![Imagem 2: Informe a primeira letra dos tipos de utilização de produtos do campo "Usado como" da aba "Geral", do Cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/16668190929815)

- Sendo estes cadastrados na tela **"Cadastro NCM"**. Por padrão, os tipos **"Imobilizado", "Outros insumos", "Serviço"** e **"Consumo"** já estão cadastrados, caso deseje é possível incluir ou retirar as letras conforme necessidade.

![Imagem 3: Sendo estes cadastrados na tela "Cadastro NCM" . Por padrão, os tipos "Imobilizado", "Outros insumos", "Serviço" e…](https://ajuda.sankhya.com.br/hc/article_attachments/9372278116759)

**CAUSA:**

Código NCM inexistente, preenchido com quantidade de dígitos incorreta ou utilização de um NCM não vigente.
