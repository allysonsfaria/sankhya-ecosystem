---
id: "360044602514"
titulo: "Substituição de PA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602514-Substitui%C3%A7%C3%A3o-de-PA"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:51:43Z"
rotulos: ["Produtos", "AJUDA DO SKW", "Configuração", "Ordem de Produção", "Estoque", "Produção", "Substituir Produto (PA)", "Núm. Lote", "Percentual MP", "Substituição de PA", "Tamanho de Lote", "Substituição de PA manual", "Proporcionalização dos apontamentos anteriores", "Use o botão \"Substituir Produto (PA)\" na Ordem de Produção", "Troca parcial ou total do PA na Ordem de Produção"]
---

# Substituição de PA

O recurso de **"Substituição de PA"** permite a substituição parcial ou completa do PA da Ordem de Produção por outro, desde que o novo PA pertença ao mesmo [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314) do PA original da Ordem.

Uma consequência da Substituição de PA é a edição dos apontamentos já existentes. Esta edição é a proporcionalização que visa fazer com que aquilo que foi apontado no passado se adeque ao novo estado da Ordem.

Abaixo trouxemos um exemplo de uso:

Uma indústria química possui a mesma mistura base para vários produtos diferentes. A diferença, nessa situação, é o frasco envasado. Os produtos são: Shampoo 200 ml, Shampoo 300 ml e Shampoo 400 ml. O fornecedor de embalagens se atrasou, ocasionando que as embalagens do Shampoo de 200 ml da Ordem não chegassem a tempo.

**Substituição total:** para não manter a linha de envase inutilizável, o chefe de produção opta por produzir Shampoo de 400 ml e Shampoo 300 ml. Ordem original de 100 UN do Shampoo 200 ml que consumiu 20 KL de Mistura. Agora, produziu-se:

- 40 UN Shampoo 300 ml consumindo 60% de MP's ou 12 KL de Mistura;
- 15 UN Shampoo 400 ml consumindo 40% de MP's ou 6 KL de Mistura.

**Substituição parcial:** a indústria possui algumas das embalagens de 200 ml; então a Ordem de 100 UN agora será para 50 UN do Shampoo de 200 ml, consumindo os mesmos 20 KL de mistura, mas que deve ser proporcionalizado entre o PA original e os novos PA's:

- 50 UN Shampoo 200 ml consumindo 50% de MP's ou 10 KL de Mistura (consequência da nova quantidade representar 50% da quantidade original);
- 20 UN Shampoo 300 ml consumindo 60% de MP's ou 6 KL de Mistura (% em cima do restante de MP's);
- 10 UN Shampoo 400 ml consumindo 40% de MPs ou 4 KL de Mistura (% em cima do restante de MP's).

**Execução**

Para a execução deste procedimento, acesse a Ordem de Produção que você deseja substituir o PA por meio da tela tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o), aba [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o#abaprodutos), botão **"Substituir Produto (PA)"**.

![Imagem 1: Para a execução deste procedimento, acesse a Ordem de Produção que você deseja substituir o PA por meio da tela tela…](https://ajuda.sankhya.com.br/hc/article_attachments/8878276391575)

Ao acioná-lo, será aberto um pop-up para que sejam realizadas as configurações:

![Imagem 2: Ao acioná-lo, será aberto um pop-up para que sejam realizadas as configurações:](https://ajuda.sankhya.com.br/hc/article_attachments/8878280596119)

**Produto e Controle:** no topo da tela que é aberta, temos o produto/controle que sofrerá a substituição.

**Nova quantidade:** neste campo, especifique a nova quantidade do PA original da ordem. Caso seja uma substituição total, informe "0" (zero) neste campo.

Logo abaixo, temos alguns campos onde definimos os vários PA's que substituirão o PA original.

**Produto (PA):** neste campo, selecione o novo PA da Ordem. Serão apresentados apenas aqueles produtos que podem ser produzidos no processo do PA original ligado à Ordem.

**Controle:** quando o produto em questão possuir controle adicional de estoque do tipo lista, este campo será apresentado para que seja feita a especificação do controle do produto.

**Tamanho de Lote:** informe neste campo o tamanho de lote para o novo produto.

**Percentual MP:** neste campo, você deve especificar o Percentual de MP que o PA em questão irá receber do PA original da Ordem, quando já existir apontamentos para este. O sistema realiza a edição dos apontamentos existentes, de forma que o novo PA receba esse % das MP's já apontadas anteriormente para a quantidade substituída do PA original.

**Núm. Lote:** especifique aqui, o número de lote do novo PA. Caso a configuração do processo esteja definida para automático, o sistema seguirá essa regra.

**Importante:** caso a OP em questão tenha realizado apontamentos parciais, é preciso rever estes apontamentos, pois o sistema edita o apontamento de PA considerando a proporção do mesmo apontada, por exemplo:

OP para produção de 100UN Shampoo de 200 ml. A quantidade já apontada de PA é de 100 UN do Shampoo de 200 ml (50% da Ordem). Ao substituir o Shampoo de 200 ml com a nova quantidade igual a 100 UN e adicionar 50 UN do Shampoo de 400 ml, o apontamento existente ficará da seguinte forma:

- 50 UN Shampoo 200 ml (50% do tamanho de lote do produto);
- 25 UN Shampoo 400 ml (50% do tamanho de lote do produto).
