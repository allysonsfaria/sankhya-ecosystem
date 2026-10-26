---
id: "360055358513"
titulo: "Integração entre os processos Expedição WMS x Fila de Conferência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360055358513-Integra%C3%A7%C3%A3o-entre-os-processos-Expedi%C3%A7%C3%A3o-WMS-x-Fila-de-Confer%C3%AAncia"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:16:37Z"
rotulos: ["Conferência", "WMS", "Expedição", "Preferências", "Fila de Conferência", "Checkout", "Conferência finalizada manualmente", "Integração WMS e Fila de Conferência", "Permitir múltiplas Ordens na mesma doca"]
---

# Integração entre os processos Expedição WMS x Fila de Conferência

A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos produtos, retirando-os do seu endereço de armazenamento, e os colocando no endereço de checkout, a conferência dos itens a ser realizada em seguida, pode ser executada e concluída por meio da tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia). Vejamos as características desse processo:

![Imagem 1: A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16921881168791) Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms), tem-se a marcação **"Permitir mais de uma OC na doca expedição"** que quando realizada, permite que Ordens de Carga distintas, sejam encaminhadas para uma mesma doca, mesmo que esta já esteja ocupada.

![Imagem 2: A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16921847909783) A tela Fila de Conferência conta com o campo **"Checkout"**, que diz respeito aos endereços de checkout para os quais os itens separados, são destinados.

![Imagem 3: A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16921881175191) Feita a marcação mencionada acima nas Preferências da Empresa, realizando-se o lançamento de pedidos de venda, sua separação no WMS, e os colocando no ponto de efetuar a conferência (situação no WMS como **"Aguardando Conferência"**), pode-se na tela Fila de Conferência (tanto em modo Flex, como em HTML5), filtrar os pedidos lançados, por meio do **"Número Único"**, **"Número da Nota"**, ou ainda, através do **"Checkout"** no qual os produtos se encontram após a realização da separação.

![Imagem 4: A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16921881175831) Uma vez na tela Fila de Conferência, caso seja feita a escolha de informar o endereço de checkout, ao preenchê-lo e pressionar a tecla **"Enter"**, o sistema já abre diretamente a tela de Conferência para sua realização.

![Imagem 5: A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16921847918359) Caso seja realizado o cancelamento de uma expedição, cujos produtos ainda não tenham sido separados, o sistema exclui a linha dessa separação conforme acontece atualmente. Caso a separação tenha sido realizada, e os produtos se encontrem no endereço de checkout, ao efetuar o cancelamento, e filtrar pelo pedido em questão na tela Fila de Conferência, é apresentada ao usuário a mensagem **"A separação XXX foi cancelada. Leve os produtos para o endereço de retorno."**; as tarefas de retorno de expedição são devidamente criadas, e disponibilizadas para serem executadas no coletor.

![Imagem 6: A integração do processo de Expedição do WMS com a Fila de Conferência, consiste após executar a separação dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16921847920663) Ao finalizar a conferência por meio da tela [Fila de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612074-Fila-de-Confer%C3%AAncia), uma conferência que estava como **"Aguardando conferência"**, passa diretamente para **"Concluído"**.

**Observação:** hoje a integração do WMS com a Fila de Conferência não suporta o processo de corte feito na Fila de Conferência, pois o mesmo não atualiza as tabelas do WMS.

**Importante:** este processo trabalha apenas com áreas de separação por Pedido. Conferências oriundas de área de separação por Produto e Conferências de Volumes não são apresentadas para serem realizadas na tela Fila de Conferência.

**Observação:** no final de uma conferência, a doca utilizada no processo não é liberada automaticamente; depois de todas as separações vinculadas a doca em questão terem sido concluídas, deve-se liberá-las manualmente (tela [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias) > [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474-Expedi%C3%A7%C3%A3o-de-Mercadorias#botooutrasopes) > opção **"Liberar Doca"**)
