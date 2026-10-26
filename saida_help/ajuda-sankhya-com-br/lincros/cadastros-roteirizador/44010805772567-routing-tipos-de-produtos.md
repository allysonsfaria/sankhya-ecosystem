---
id: "44010805772567"
titulo: "[Routing] - Tipos de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010805772567--Routing-Tipos-de-Produtos"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T18:47:28Z"
rotulos: ["sync_hc", "lincros", "lincros_13432262", "sync_hash_24b13d762645"]
---

# [Routing] - Tipos de Produtos

**Menu:** Cadastros > Tipos de Produtos

**Objetivo:** Como realizar o cadastro de tipos de produtos

## Considerações:

- Os tipos de produtos são utilizados para associarmos o produto ao veículo, nele definimos como serão os códigos identificadores de cada tipo de produto.
- É necessário ter os campos abaixo já cadastrados no Router para iniciar o cadastramento de tipos de produtos:

- [Depósito](https://intercom.help/ajudalincros/pt-BR/articles/14443341-routing-cadastro-de-deposito)

Para o cadastro de tipos de produtos é necessário informar os seguintes campos:

1. **Depósito**: Para o cadastro de uma prioridade de pedidos é necessário vincular ele à um depósito;
2. **Descrição:** Informe uma descrição para este tipo de produto;
3. **Identificador**: Informe um código identificador para esse tipo de produto. Ex.: C de Congelados
4. **Segregação de produtos**: Aqui você vai selecionar os produtos que não poderão ser transportados juntamente com os produtos identificados acima.

## Exemplo da Tela de Tipos de Produtos

![Imagem 1: Exemplo da Tela de Tipos de Produtos](https://ajuda.sankhya.com.br/hc/article_attachments/44010805921559)

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

**Importante**: O cadastro de tipo de produto pode ser feito de forma manual ou via API. Caso não tenha sido cadastrado o tipo de produto no sistema, mas em seu arquivo .txt de pedidos tenha o código de identificação do tipo de produto, então no momento em que realizar a importação deste arquivo em Importações > Pedidos, o sistema apresentará a seguinte mensagem: Tipo de produto... não encontrado.

Caso defina como obrigatório ser informado no arquivo de importação de pedidos o Tipo de Produto, então deverá utilizar no arquivo o "valor" que for informado no campo "Identificador". É deste campo que o sistema faz validação do tipo de produto.

![Imagem 2: Caso defina como obrigatório ser informado no arquivo de importação de pedidos o Tipo de Produto, então deverá utilizar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010818441495)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
