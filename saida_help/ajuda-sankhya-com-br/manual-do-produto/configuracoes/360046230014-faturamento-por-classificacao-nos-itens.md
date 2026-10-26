---
id: "360046230014"
titulo: "Faturamento por classificação nos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046230014-Faturamento-por-classifica%C3%A7%C3%A3o-nos-itens"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:59:56Z"
rotulos: ["SQL", "Configuração", "Faturamento", "TOP", "Itens", "Tipos de Operação - TOP", "Separação por critério de itens", "Separação de Itens no Faturamento"]
---

# Faturamento por classificação nos itens

Será possível que você realize a separação de itens em diferentes documentos através da rotina de faturamento. Para isto, é necessário que o parâmetro **"Tipo separação faturamento - TIPOSEPFAT"** encontre-se com a opção **"Separação por critério de itens"** selecionada.

**Observação:** esta funcionalidade poderá ser acessada pelo [Cadastro de Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba **"Separação para faturamento"**:

![Imagem 1: Observação: esta funcionalidade poderá ser acessada pelo Cadastro de Tipos de Operação - TOP , aba "Separação para…](https://ajuda.sankhya.com.br/hc/article_attachments/360067011113)

Você deverá realizar a configuração na TOP de origem, informando os seguintes dados:

No campo **"Empresa"**, define-se para qual empresa ocorrerá a separação.

Você deverá inserir no campo **"Tipo de Operação separação"** o tipo de operação de destino para os itens separados.

No campo **"Série separação"** você informará a série utilizada para o documento gerado.

Quando você selecionar a marcação **"Confirmar nota ao faturar?"**, fará com que o documento gerado seja confirmado após o faturamento.

No campo **"Critério p/ separação de itens"** você definirá qual critério será utilizado para separação de itens. Para isto, deve-se utilizar uma expressão SQL, a qual será inserida no contexto do faturamento, na query base para faturamento ou ainda, você poderá informar o nome do campo da tabela de itens, da seguinte forma: TIPENTREGA='E'.

**Observação:** a opção de confirmação refere-se apenas aos documentos separados no faturamento; para que todos os documentos gerados no faturamento sejam confirmados, você deverá gerar critérios suficientes para todos os itens que compõe a nota. Caso existam itens na nota que não se enquadrem em nenhum dos critérios definidos, eles serão faturados porém, a nota de destino não será confirmada.

O campo **"Tipo entrega"**, existente na tabela de itens, precisará ser adicionado no [layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634) do Pedido de Venda, onde o vendedor deverá classificar o tipo de entrega. O faturamento que gera diversas notas, apenas será realizado caso preencha esta informação no Pedido de Venda.
