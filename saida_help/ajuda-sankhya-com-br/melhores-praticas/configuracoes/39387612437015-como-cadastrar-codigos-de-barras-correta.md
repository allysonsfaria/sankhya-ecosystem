---
id: "39387612437015"
titulo: "Como cadastrar códigos de barras corretamente no cadastro de produtos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39387612437015-Como-cadastrar-c%C3%B3digos-de-barras-corretamente-no-cadastro-de-produtos"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-08-17T01:29:01Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Código de Barras", "Cadastro", "Artigo criado KCS", "CVE - KCS"]
---

# Como cadastrar códigos de barras corretamente no cadastro de produtos?

No cadastro de produtos do sistema Sankhya, existem **três locais diferentes** onde é possível registrar códigos de barras: o campo **"Referência"** (Tabela TGFPRO), a aba **"Código de Barras"** ( Tabela TGFBAR) e a seção **"Unidades Alternativas"** (Tabela TGFVOA). Esta multiplicidade de opções pode gerar dúvidas sobre qual local utilizar e causar inconsistências no processo de consulta de produtos.

Um problema comum relatado é que os **códigos EAN** cadastrados na aba de **"Unidades Alternativas"** não são reconhecidos na rotina de **"Consulta de Produtos"** nem no lançamento de itens na nota fiscal através do atalho **"Ctrl + B"**, o que impacta diretamente a operação.

### Locais disponíveis para cadastro de códigos

O sistema oferece três opções para registro de códigos de barras, cada uma com sua finalidade específica:

**Campo "Referência" (TGFPRO):** localizado no cadastro principal do produto, este campo armazena o código de referência do produto, que pode ser utilizado como identificador alternativo.

**Aba "Código de Barras" (TGFBAR):** esta aba permite o cadastro de múltiplos códigos de barras para o mesmo produto, sendo o local mais indicado para registrar códigos EAN e outros códigos de identificação.

**Seção "Unidades Alternativas" (TGFVOA):** utilizada para cadastrar unidades de medida alternativas do produto, esta seção também permite o registro de códigos de barras específicos para cada unidade alternativa.

### Comportamento na consulta de produtos

A **"Consulta de Produtos"** (Comercial Consulta Consulta de Produtos) e o **"Lançamento de Itens"** (Comercial Movimentação Central de Vendas) via **"Ctrl + B"** priorizam a busca pelos códigos cadastrados na aba **"Código de Barras"** (TGFBAR) e no campo **"Referência"** (TGFPRO). Os códigos registrados exclusivamente na seção de **"Unidades Alternativas"** (TGFVOA) podem não ser reconhecidos automaticamente nestas rotinas.

Este comportamento ocorre porque as rotinas de consulta foram desenvolvidas para buscar prioritariamente nos locais padrão de cadastro de códigos, não incluindo automaticamente a tabela de unidades alternativas no processo de pesquisa.

### Recomendações para cadastro correto

Para garantir que os códigos de barras sejam reconhecidos em todas as rotinas do sistema, siga estas orientações:

**(1)** Acesse o cadastro de **"Produtos"** (Comercial - Arquivo - Cadastros - Produtos) e localize o produto desejado.

**(2)** Utilize a aba **"Código de Barras"** (TGFBAR) como local principal para cadastrar todos os códigos EAN e códigos de barras do produto.

**(3)** Cadastre o código de barras principal também no campo **"Referência"** (TGFPRO) do produto, se necessário.

**(4)** Reserve a seção **"Unidades Alternativas"** (TGFVOA) apenas para códigos específicos de unidades de medida diferentes da unidade padrão do produto.

**(5)** Teste a consulta do produto utilizando o atalho **"Ctrl + B"** para verificar se o código está sendo reconhecido corretamente.

Seguindo estas práticas, você garante que os códigos de barras sejam reconhecidos em todas as rotinas do sistema, evitando inconsistências no processo operacional.
