---
id: "360043864114"
titulo: "Como enviar as tags <xPed> e <nItemPed> no XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043864114-Como-enviar-as-tags-xPed-e-nItemPed-no-XML"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:24Z"
rotulos: ["#PUBLIFER", "Configuração", "NF-e", "Central de Vendas", "XML", "SEFAZ", "Tags <xPed> e <nItemPed> no XML", "Enviar tags", "Geração das tags XML"]
---

# Como enviar as tags <xPed> e <nItemPed> no XML

**Número Pedido:** Este campo poderá ser preenchido manualmente, tanto no 'cabeçalho', quanto nos itens da nota. Caso não esteja preenchido manualmente, ele poderá ser gerado de forma automática, considerando a ligação pedido/nota (TGFVAR):

Atente-se as configurações necessárias para enviar as  tags <xPed> e <nItemPed> no XML:

![Imagem 1: Acesse a tela 'Configurador de Layout da Nota' (Comercial » Configuração) e s elecione o layout utilizado para a…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233773975) Acesse a tela **'Configurador de Layout da Nota'** (Comercial » Configuração) e selecione o layout utilizado para a respectiva 'Venda'.

![Imagem 2: Para inserção do campo ' Número pedido ' no cabeçalho da nota, selecione em 'Campos Disponíveis' o campo 'Número…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233778199) Para inserção do campo '**Número pedido**' no cabeçalho da nota, selecione em 'Campos Disponíveis' o campo 'Número Pedido' e arraste o mesmo para o quadrante cabeçalho.

![Imagem 3: Salve o ajuste. Ao realizar o lançamento na Central de 'Vendas', preencha o campo 'Número Pedido' conforme necessário.…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233785367) Salve o ajuste. Ao realizar o lançamento na Central de 'Vendas', preencha o campo 'Número Pedido' conforme necessário. Caso o lançamento tenha sido iniciado antes do ajuste, feche a tela, ao abrir novamente o campo será apresentado.

Ao utilizar a inserção dessas informações através do cabeçalho, apenas a tag <xPed> será gerada (não gera a tag <nItemPed>). Valide a geração da tag conforme exemplo abaixo:

![Imagem 4: Ao utilizar a inserção dessas informações através do cabeçalho, apenas a tag <xPed> será gerada (não gera a tag…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233787159)

![Imagem 5: Caso o lançamento possua mais de um item, aconselha-se que essa informação seja preenchida na grade de itens. As…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233792791) Caso o lançamento possua mais de um item, aconselha-se que essa informação seja preenchida na grade de itens. As informações inseridas nos itens irão sobrepor a informação do cabeçalho. Para tal, acesse o configurador de layout da nota e realize a inserção dos campos '**Número Pedido' e 'Sequência no Pedido'**dentro de "Itens".

![Imagem 6: Salve o ajuste. Ao realizar o lançamento na Central de 'Vendas', preencha os campos para cada um dos itens, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233800855) Salve o ajuste. Ao realizar o lançamento na Central de 'Vendas', preencha os campos para cada um dos itens, conforme necessário. Caso o lançamento tenha sido iniciado antes do ajuste, feche a tela, ao abrir novamente os campos serão apresentados.

![Imagem 7: Salve o ajuste. Ao realizar o lançamento na Central de 'Vendas', preencha os campos para cada um dos itens, conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/18857233808791)

Ao gerar o XML valide a geração das tags conforme exemplo abaixo:

![Imagem 8: Ao gerar o XML valide a geração das tags conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18857223818135)

**Observações:**

- O sistema sempre irá considerar **primeiramente o campo referente aos itens**, ou seja, se ele estiver aqui preenchido, então, será este valor que será gerado na tag <xPed> do XML. Só irá para a tag do XML o valor informado no campo do **cabeçalho da nota**, se o do item estiver vazio.
- Se não estiver preenchido no cabeçalho e nem nos itens, o sistema irá buscar o pedido de origem e a sequência de origem pela TGFVAR (tabela de ligação do pedido/nota).
- Se não estiver preenchido nenhum dos campos de número de pedido e não existir ligação na TGFVAR, o sistema **não vai gerar a tag**.
- Para que essas informações sejam apresentadas no DANFE, será necessário acessar a tela 'Empresa' (Comercial >> Preferências >> Empresa),botão  Outras Opções >> Complemento para Itens da Nota (Web) >> Itens da Nota >> Adicionar os campos "Seq. No pedido" e "Número Pedido".
- De acordo com o **Manual de Integração do Contribuinte - SEFAZ**, em sua versão atual e com data do referido artigo, informa que a tag 'xPed' recebe 1 a 15 caracteres e a tag 'nItemPed' recebe até 6 caracteres.
