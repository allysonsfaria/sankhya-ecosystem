---
id: "14971395326615"
titulo: "Qual processo preciso fazer para gerar a tarefa de retorno de expedição após cancelamento?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14971395326615-Qual-processo-preciso-fazer-para-gerar-a-tarefa-de-retorno-de-expedi%C3%A7%C3%A3o-ap%C3%B3s-cancelamento"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-07T13:56:31Z"
rotulos: ["Produtos", "Configuração", "WMS", "Movimentação Financeira", "Estoque", "Retorno de Mercadorias Após Cancelamento de Expedição", "Artigo atualizado KCS", "WMS - KCS"]
---

# Qual processo preciso fazer para gerar a tarefa de retorno de expedição após cancelamento?

Quando a separação é cancelada após o processo de **"Separação"** já ter sido iniciado ou concluído. Ao clicar em outras opções na tela **"Expedição de Mercadorias" (**WMS » Rotinas » Expedição de Mercadorias), e selecionar as opções 'Cancelar Separação' ou 'Cancelar separações desta OC', o sistema altera a situação para "Cancelada-Possui Retorno Merc.". Quando o cancelamento é feito com a situação da separação como 'Conferência validada', a tarefa de retorno de expedição é gerada automaticamente pelo sistema. Entretanto, caso o cancelamento seja feito em uma situação diferente, será necessário verificar a situação na tela **"Gerência do WMS"** WMS » Gerência » Gerência do WMS.

[GIF animado: Imagem 1: Quando a separação é cancelada após o processo de "Separação" já ter sido iniciado ou concluído. Ao clicar em outras…](https://ajuda.sankhya.com.br/hc/article_attachments/15142695275415)

Para realizar o retorno das mercadorias, o sistema deve gerar as tarefas após o cancelamento, apresentando a mensagem no coletor: "A separação X foi cancelada. Leve os produtos para endereço de retorno".

Caso a tarefa não seja gerada automaticamente, siga os procedimentos abaixo:

**(1)** Acesse a tela **"Gerência do WMS"**, altere o filtro Tipos de tarefa para "Expedição Cancelada" e verifique o campo **"Situação Cancelamento Sep."** e identifique a separação que foi cancelada

[GIF animado: Imagem 2: (1) Acesse a tela "Gerência do WMS" , altere o filtro Tipos de tarefa para "Expedição Cancelada" e verifique o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/15142695280919)

**(2)** Realize a tarefa indicada no campo **"Situação Cancelamento Sep."**, informando o endereço vinculado a separação podendo ser uma doca de saída ou um endereço checkout para ser gerada a tarefa dependendo do tipo de separação.

**(3)**  Após a geração da tarefa de retorno de expedição, execute-a no coletor a partir da tarefa **"Armazenagem"** para os produtos que participavam das separações canceladas, garantindo a acuracidade do estoque.

**(4)** Após a regularização, os produtos estarão disponíveis para novas separações.

Observação: Caso após a realização do processo descrito, a tarefa de retorno de expedição não seja gerada, contacte o suporte para que seja analisado o cenário informando a separação e o momento exato do cancelamento.
