---
id: "360044602754"
titulo: "Inserção de Itens nas Centrais por Referência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602754-Inser%C3%A7%C3%A3o-de-Itens-nas-Centrais-por-Refer%C3%AAncia"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:52:51Z"
rotulos: ["Produtos", "Configuração", "Central de Compras", "Central de Vendas", "Portal de Vendas", "Estoque", "Inserção de Itens nas Centrais por Referência manual", "Configuração de Parâmetro para Inserção de Itens na Nota"]
---

# Inserção de Itens nas Centrais por Referência

O parâmetro **"Código e/ou referência nos itens?** **-** **CODPROREF"** é empregado para estabelecer se nas Centrais de [Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras) | [Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594154-Central-de-Mov-Internas), os itens da nota serão inseridos por Código (Cód. do Produto) ou por Referência (Cód. Barra), essa referência pode ser a Referência principal do produto, e também pode ser a Referência da Unidade Alternativa ou do Estoque.

Para utilizar a Referência na adição de itens na central, primeiramente deve-se alterar o valor do parâmetro mencionado para **"Referência"**. Essa decisão por Código ou Referência aplica-se ao [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232294-Portal-de-Vendas) | [Compra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025389513-Portal-de-Compras) | [Mov. Internas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025394173-Portal-de-Mov-Internas), para todos os tipos de movimento.

**Importante:** quando o referido parâmetro estiver definido com a opção Referência, se fará necessária a ativação do parâmetro **"Mostrar qual o tipo de referência - MOSTRARQUALREF"**, pois este será o responsável por definir se a referência apresentada na grade Itens será tanto **"Referência do produto e Referência do fornecedor"** ou cada uma unitariamente.

É possível cadastrar Referências (Cód. De Barra) para Unidades Alternativas e também para Estoques, para utilizar essa Referência na Central para adicionar o item na nota, é necessário habilitar a opção **"Pesquisar por Cód. Barra do Estoque/Unid. Alternativa"**, esta opção se encontra no botão **"Outras opções"**, na opção **"Opções p/Controlar Pesquisas"** da grade de itens da Nota.

Tem-se como vantagem, que ao utilizar o Cód. Barra de uma unidade alternativa, o sistema automaticamente buscará a Unidade e o Controle do produto e configurará o item da nota.

Para Cód. Barra de Estoque o sistema configurará o Controle e o Local, porém, para que esse Local seja carregado, é necessário que no [Cadastro do Produto](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-), aba **"Medidas e Estoque"**, **"Sub-Aba Estoque"**, o campo **"Usa Local?"** se encontre marcado e o parâmetro **"Utiliza a coluna Local para controlar o estoque - UTILIZALOCAL"** esteja habilitado.

Quando um produto é inserido na grade de itens por Cód. Barras de Unidades Alternativas ou Estoque, quando ele é salvo, o sistema mudará a referência do produto na nota para a Referência principal que fica na aba **"Geral"** do Cadastro de Produtos. Isso ocorre porque o Cód. Barra da Unid. Alternativa ou Estoque serve apenas para configurar a Unidade, Local e Controle automaticamente para quem estiver lançando a nota.

Porém, é possível que tenhamos um produto que não tem Referência principal, e só tem Referências (Cód. Barras) para Unidades Alternativas ou Estoque, pois a Referência não é campo obrigatório, neste caso, o sistema deixará o campo referente a referência em branco e manterá a Descrição do Produto, o sistema também permitirá alterar o item na nota sem inserir a referência novamente.

**Observação:** as Centrais de Notas são customizáveis através da tela [Configurador de layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota), em primeira instância, ou seja, sem layouts personalizados, o sistema mudará automaticamente o campo **"Produto"** para **"Referência do Produto"**, porém, se o sistema estiver usando um Layout personalizado por essa tela, será necessário que o criador do layout troque na grade itens o campo Produto pelo Referência de Produto, não é recomendado manter os dois campos na grade, pois pode gerar confusão, sempre deixe somente um deles conforme definido no parâmetro **"Código e/ou referência nos itens?** **-** **CODPROREF"**.

⚠️ **Importante:** O campo **"Referência do Fornecedor"** possui uma regra de negócio específica: ele permanece disponível para utilização nas Centrais de Compras, Vendas e Mov. Internas **independentemente** de estar ou não selecionado na configuração do layout. Ou seja, habilitar ou desabilitar esse campo na tela Configurador de Layout da Nota não interfere em sua disponibilidade na Central — este é o comportamento padrão do sistema e não caracteriza uma inconsistência funcional.

![Imagem 1: Observação: as Centrais de Notas são customizáveis através da tela Configurador de layout da nota , em primeira…](https://ajuda.sankhya.com.br/hc/article_attachments/9193972783639)
