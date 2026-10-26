---
id: "7893973086743"
titulo: "Integração Máxima e Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7893973086743-Integra%C3%A7%C3%A3o-M%C3%A1xima-e-Sankhya"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:12:51Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Integração", "Integração Completa: Sankhya e Máxima", "Máxima", "ERP"]
---

# Integração Máxima e Sankhya

A integração do sistema Sankhya com a Máxima tem o propósito de vincular as seguintes funcionalidades:

#### Pré-venda

**(1)** Pré-venda que gera pedido de venda para entrega futura pela matriz e seus centros de distribuição;

**(1)** A força de vendas gera o pedido e o ERP fatura em uma NF-e.

#### Pronta entrega

**(1)** Imediata, estoque fica no veículo;

**(1)** O Pronta Entrega emite a NF-e em contingência;

**(1)** O Pronta Entrega envia a NF-e emitida em contingência para o ERP;

**(1)** O ERP apenas busca a autorização na SEFAZ da NF-e emitida em contingência.

#### Roteirização dos pedidos

**(1)** Montagem de Carga e Roteirização das Entregas;

**(1)** O ERP envia os pedidos ao Roteirizador;

**(1)** O Roteirizador irá agrupar e ordenar as cargas;

**(1)** O Roteirizador devolve ao ERP as cargas montadas.

#### Matriz de Responsabilidade:

![Imagem 1: A instalação da extensão Máxima agora é feita pelo Sankhya Place . Para isto basta procurar pelo texto Integração…](https://ajuda.sankhya.com.br/hc/article_attachments/16542406818327) A instalação da extensão Máxima agora é feita pelo **Sankhya Place**. Para isto basta procurar pelo texto **Integração Máxima.**

![Imagem 2: O ambiente pode ser de Testes ou de Produção .](https://ajuda.sankhya.com.br/hc/article_attachments/16542398129047) O ambiente pode ser de **Testes** ou de **Produção**.

![Imagem 3: A decisão é do cliente, de fazer primeiro em ambiente de testes ou direto em ambiente de produção.](https://ajuda.sankhya.com.br/hc/article_attachments/16542406828055) A decisão é do **cliente,** de fazer primeiro em ambiente de testes ou direto em ambiente de produção.

![Imagem 4: Se decidirem fazer primeiro em ambiente de testes, depois de validado devem replicar todas as configurações da extensão…](https://ajuda.sankhya.com.br/hc/article_attachments/16542398135447) Se decidirem fazer primeiro em ambiente de testes, depois de validado devem replicar todas as configurações da extensão e de seus cadastros no ambiente produção.

![Imagem 5: Após o envio de dados, a Máxima ficará responsável por validar a coerência dos dados recebidos. Para isso, a Máxima…](https://ajuda.sankhya.com.br/hc/article_attachments/16542398137751)Após o envio de dados, a Máxima ficará responsável por validar a coerência dos dados recebidos. Para isso, a Máxima disponibiliza um relatório ( planilha ) no qual informa os campos que estão com ligações incoerentes.

![Imagem 6: A Máxima deve disponibilizar documentação explicativa que facilite o entendimento da planilha de validação de dados que…](https://ajuda.sankhya.com.br/hc/article_attachments/16542398140311) A Máxima deve disponibilizar documentação explicativa que facilite o entendimento da planilha de validação de dados que a Máxima fornece ao cliente para que seja feito a adequação de inconsistências nos cadastros do ERP.

![Imagem 7: Para resolver estes problemas de inconsistências de dados mencionados no item 8, o CLIENTE ou Máxima devem fazer os…](https://ajuda.sankhya.com.br/hc/article_attachments/16542406836887) Para resolver estes problemas de inconsistências de dados mencionados no item 8, o CLIENTE ou Máxima devem fazer os ajustes nos cadastros para solucionar a incoerência das informações. Após estes ajustes, estas informações devem ser enviadas novamente à Máxima.

![Imagem 8: Após o envio de todos os cadastros e tudo validado pela Máxima, já será possível gerar pedidos no ambiente da Máxima.](https://ajuda.sankhya.com.br/hc/article_attachments/16542398144535) Após o envio de todos os cadastros e tudo validado pela Máxima, já será possível gerar pedidos no ambiente da Máxima.

![Imagem 9: A Máxima deve disponibilizar o ambiente e treinar o cliente sobre como usar sua Plataforma Web e App Mobile.](https://ajuda.sankhya.com.br/hc/article_attachments/16542406840727) A Máxima deve disponibilizar o ambiente e treinar o **cliente** sobre como usar sua **Plataforma Web e App Mobile.**

**Observações Importantes:**

**(1)** Considerando a Matriz de Responsabilidade citada acima, caso queira acessar o **material complementar de instalação, acesse o manual anexado ao final desse artigo**. 

**(1)** Também encontra-se em anexo ao final desse artigo, os arquivos **Maxima.ext,** que é a extensão que necessita ser instalada, e o **MaximaAction.jar**que é a ação agendada para configurar as execuções automáticas. 

**(1)** Para acessar o manual de instalação de extensões, [clique aqui.](https://developer.sankhya.com.br/docs/instala%C3%A7%C3%A3o-de-extens%C3%A3o)

**Anexos:**
