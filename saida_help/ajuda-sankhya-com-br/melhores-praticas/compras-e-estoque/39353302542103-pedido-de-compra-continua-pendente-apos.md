---
id: "39353302542103"
titulo: "Pedido de compra continua pendente após a entrada da nota no Portal de Importação do XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353302542103-Pedido-de-compra-continua-pendente-ap%C3%B3s-a-entrada-da-nota-no-Portal-de-Importa%C3%A7%C3%A3o-do-XML"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-10-21T16:32:10Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Importação", "TOP", "Artigo criado KCS", "CVE - KCS"]
---

# Pedido de compra continua pendente após a entrada da nota no Portal de Importação do XML

Quando itens de um pedido de compras permanecem pendentes mesmo após a entrada da nota fiscal no sistema, é necessário verificar as configurações da **"TOP"** (Tipo de Operação) utilizada na nota de compra e o processo de importação do XML.

Este artigo orienta sobre como identificar e corrigir situações em que produtos não são baixados automaticamente do pedido durante o processo de entrada de notas fiscais, especialmente quando utilizado o **"Portal de Importação de XML"** (Comercial » Rotinas » Portal de Importação de XML).

### Identificação do problema

A divergência ocorre quando a **"TOP"** utilizada na nota de compra (a mesma informada no **"Portal de Importação de XML"**) está com o campo **"Exigir Pedido"** definido como **"Não Exigir"**. Nesta configuração, o sistema aceita a nota sem nenhuma ligação com o pedido e, no **"Portal de Importação de XML"**, a etapa de ligação com o pedido é ignorada. Sem essa ligação, os itens do pedido continuam pendentes.

Além disso, produtos incluídos em um pedido que já foi faturado, total ou parcialmente, ficam pendentes no **"Portal de Compras"** (Comercial » Consulta » Portal de Compras), porque não fizeram parte da nota já lançada.

### Verificação da configuração da TOP

Para evitar este tipo de situação, verifique a configuração da **"TOP"** utilizada na nota de compra:

**(1)**  Acesse a tela **"Tipos de Operação"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).
**(2)**  Localize a **"TOP"** utilizada na nota de compra e verifique o campo **"Exigir Pedido"**.
**(3)**  Selecione a opção adequada ao processo de compras da empresa: **"Exigir completo"** (todos os itens da nota precisam estar ligados a um pedido) ou **"Exigir algum item"** (basta um item ligado; os demais podem entrar sem ligação). Evite a opção **"Não Exigir"** quando houver necessidade de controle rigoroso dos itens.

**Importante:** com **"Exigir completo"** ou **"Exigir algum item"**, o sistema não aceita notas de compra sem pedido nessa **"TOP"**. Se a empresa também faz compras sem pedido, utilize outra **"TOP"** para elas. A alteração vale para as próximas notas: as notas já lançadas continuam sem ligação com o pedido.

### Cuidados com o Portal de Importação de XML

Ao utilizar o **"Portal de Importação de XML"**, confira a aba **"Pedidos"** antes de processar a nota. Ela mostra, para cada produto, os pedidos de compra confirmados e com saldo pendente da mesma empresa e do mesmo fornecedor. Quando o XML traz o número do pedido, a ligação já vem preenchida; nos demais casos, informe a quantidade na coluna **"Vinculado"** ou use o botão **"Ligar pedidos mais antigos"**.

Verifique também, no menu de opções do portal, em **"Preferências para importação de NF-e"**, se a opção **"Validar controle adicional"** está como **"Validar"**. Com **"Não validar"**, o portal também não faz a ligação com o pedido.

### Resolução de itens pendentes

Caso identifique itens pendentes que deveriam ter sido baixados na entrada da nota fiscal, verifique se a nota foi corretamente vinculada ao pedido de compras e se todos os itens foram incluídos no documento de entrada.

O **"Portal de Compras"** não vincula um pedido a uma nota já lançada. Se os itens já foram recebidos e precisam sair da lista de pendentes, selecione o pedido (ou apenas os itens) no **"Portal de Compras"** e use a opção **"Marcar como não pendente"**. Essa opção encerra todo o saldo pendente dos itens marcados e não liga o pedido à nota. Por isso, marque apenas os itens que realmente foram recebidos.
