---
id: "15082837906327"
titulo: "Configurações necessárias para correto funcionamento do evento 68 e uso no Portal de Importação de XML "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15082837906327-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-correto-funcionamento-do-evento-68-e-uso-no-Portal-de-Importa%C3%A7%C3%A3o-de-XML"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:57:33Z"
rotulos: ["Configuração", "Eventos", "XML", "Importação", "TOP", "Preferências", "Configurações para o Evento 68 e Uso no Portal de Importação de XML"]
---

# Configurações necessárias para correto funcionamento do evento 68 e uso no Portal de Importação de XML 

**(1)** Na tela **["Preferências"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias)** (Caminho de acesso: Configurações » Avançado » Preferências), localize o parâmetro **"Campo p/ validação valor unit. evento 68? - CAMVLRUNITEVT68".** Este é o responsável pela validação do evento em questão. Ou seja, configure o parâmetro informando no mesmo os campos calculados na tabela **"TGFITE"** pertinentes aos referidos valores, como por exemplo, os campos **"VLRUNIT"** e **"VLRUNITLIQ"** sempre separados por ";".

![Imagem 1: (1) Na tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências ), localize o parâmetro "Campo…](https://ajuda.sankhya.com.br/attachments/token/yhbqKRTHCymcvOLweclZCQbuj/?name=image.png)

Na mesma tela (Preferências) ligue/ative o parâmetro **"Usar liberação de limites por alçada? - USALIBLIM".**

Acesse a tela **["Tipos de Operação - TOP"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), localize a aba **"Conf. do evento 68"** (Variação do valor unitário entre origem e destino). Efetuando a marcação "**Validar variações do vlr. unit. orig./dest."**, define-se que no momento da confirmação de um item de uma nota de venda, havendo variação entre o valor unitário do pedido e o valor unitário da nota de destino.

**![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16591490028951) OBSERVAÇÃO:**

Também configure os campos **"Validar diferença para"**, **"% Tolerância na variação do Vlr. unitário:"**, **"Valor para validar o evento 68:",** presentes na mesma aba.

![Imagem 3: Também configure os campos "Validar diferença para" , "% Tolerância na variação do Vlr. unitário:" , "Valor para…](https://ajuda.sankhya.com.br/attachments/token/FYkIf6hDkc605c0S8s8Q4a8h4/?name=image.png)

Ainda na tela Tipos de Operação, o Tipo de Operação utilizado deve estar com o campo**"Exigir pedido"** diferente de **"Não exigir"**; (tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abavalidaes)).

Na tela [**"Usuários"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios) (Caminho de acesso: Configurações » Controle de Acesso » Usuários) configure o evento**"68 - Variação do vlr. unit. orig./dest."** para o usuário liberador(botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Limites para Liberação"**);

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16591493008023) SOLUÇÃO:**

Após configuração caso o XML importado possua algum item com o valor unitário diferente do valor unitário do pedido de compra ligado à nota de compra importada, será acionada a divergência de importação do XML, ou seja, a Divergência de valor unitário entre pedido e nota sendo apresentada a seguinte mensagem:
 
**"Aguardando liberação para variação do vlr.unitário acima do permitido. Divergência de valor unitário entre pedido e nota."**
