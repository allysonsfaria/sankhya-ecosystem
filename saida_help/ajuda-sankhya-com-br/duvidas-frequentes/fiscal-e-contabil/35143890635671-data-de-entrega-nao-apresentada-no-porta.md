---
id: "35143890635671"
titulo: "Data de entrega não apresentada no portal de importação de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35143890635671-Data-de-entrega-n%C3%A3o-apresentada-no-portal-de-importa%C3%A7%C3%A3o-de-XML"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:25:58Z"
rotulos: ["Configuração", "NF-e", "XML", "Importação", "Preferências", "data de entrega", "portal de importação XML", "Opção data previsão entrega", "importação XML", "Data de entrega não apresentada no portal de importação de XML"]
---

# Data de entrega não apresentada no portal de importação de XML

**SITUAÇÃO**

Durante o processo de **importação de XML**, na etapa de **ligação com os pedidos de compra**, o usuário não consegue visualizar a **data de previsão de entrega** dos itens no portal, dificultando o controle e acompanhamento da operação.

**SOLUÇÃO**

**(1)**  Acesse a tela **"Portal de importação de XML",** clique no botão **"Outras Opções"** e selecione a opção **"Preferências para importação de NF-e".** Nessas preferências, configure o campo **"Opção para Data de Previsão de Entrega"** com uma das opções abaixo:

    • Não ordenar pela data de previsão de entrega
    • Ordenar pela data de previsão de entrega do item da nota
    • Buscar mais de uma data de previsão de entrega para cada item da nota

![Imagem 1: • Não ordenar pela data de previsão de entrega • Ordenar pela data de previsão de entrega do item da nota • Buscar mais…](https://ajuda.sankhya.com.br/hc/article_attachments/35475226488343)

**(2)**  Certifique-se de que os **pedidos de compra** possuam a **data de previsão de entrega** preenchida **nos itens**. O sistema **não utiliza a data do cabeçalho da nota, apenas dos itens específicos.**

![Imagem 2: (2) Certifique-se de que os pedidos de compra possuam a data de previsão de entrega preenchida nos itens . O sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/35475215846039)

**Observação:** a **data de previsão de entrega** será apresentada no portal de importação de XML, mas não será transferida para a nota na central.

![Imagem 3: Observação: a data de previsão de entrega será apresentada no portal de importação de XML, mas não será transferida…](https://ajuda.sankhya.com.br/hc/article_attachments/35488113464471)

**CAUSA**

A ausência da **data de previsão de entrega** nos **itens do pedido de compra** ou a **configuração inadequada** do campo Opção para Data de Previsão de Entrega impedem que essa informação seja exibida corretamente no portal de importação de XML.
