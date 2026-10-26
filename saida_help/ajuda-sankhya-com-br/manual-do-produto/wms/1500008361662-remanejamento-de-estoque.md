---
id: "1500008361662"
titulo: "Remanejamento de estoque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008361662-Remanejamento-de-estoque"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:12:41Z"
rotulos: ["Configuração", "WMS", "br.com.sankhya.wms.rot.remanejamentoestoque", "Rotinas", "Estoque", "Remanejamento de Estoque", "Movimentação", "Remanejamento de Estoque no WMS"]
---

# Remanejamento de estoque

Para um melhor aproveitamento do espaço físico de um armazém, é necessário realizar um remanejamento do estoque nos endereços de pulmão, ou seja, executar uma análise visando identificar quais produtos não estão ocupando o espaço total do endereço.

A tela Remanejamento de Estoque, localizada no menu **"WMS > Rotinas"** de nosso sistema, permite que seja feita a referida análise e retornadas as melhores oportunidades de modificação do estoque. Os produtos selecionados devem ser transferidos para outros endereços que sejam de menor tamanho ou que estejam ocupados com produtos compatíveis (podem ser armazenados juntos).

![Imagem 1: A tela Remanejamento de Estoque , localizada no menu "WMS > Rotinas" de nosso sistema, permite que seja feita a…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012642221)

Para que você consiga fazer o Remanejamento de Estoque com sucesso, realize primeiramente as configurações descritas abaixo:

1. Na tela [Endereço de Arm](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento)[azenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), cadastre os endereços de picking e pulmão que receberão os produtos;
2. Na tela de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-), cadastre devidamente os produtos que terão seu saldo de estoque trabalhado e se atente para a aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms), onde você deverá incluir o endereço de picking que o produto será alocado;

Realizadas as configurações acima, você já pode iniciar o processo de remanejamento de estoque, informando obrigatoriamente a **"Empresa"** do remanejamento e, caso necessário, preenchendo os campos **"Faixa de endereço"**, **"Produto"**, **"Grupo de produto"** e/ou **"Marca"**.

Através do Painel de Filtros, você ainda pode definir nas **"Preferências da Geração de Tarefas"** qual será a **"Estratégia"** de preenchimento dos endereços, se **"Pela proximidade do picking"**, fazendo com que o sistema verifique quais os endereços mais próximos do picking do produto ou se será **"Pela capacidade do pulmão"**, de forma que o pulmão que possuir a maior capacidade livre receba as de menor quantidade.

Ainda nas Preferências da Geração de Tarefas, através da marcação **"Abastecer picking no remanejamento"** você define se o picking do produto suporta um reabastecimento; sendo assim, será gerada uma movimentação de reabastecimento no lugar de um movimento entre pulmões.

Após realizar os filtros desejados, clique no botão **"Aplicar"**  para que sejam exibidos os produtos e endereços que atendem o(s) filtro(s) configurado(s):

[GIF animado: Imagem 2: Após realizar os filtros desejados, clique no botão "Aplicar" para que sejam exibidos os produtos e endereços que…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012647061)

Selecionados os produtos, clique no botão **"Gerar Remanejamento"** para realizar a geração das tarefas de remanejamento. Assim, teremos na tela a relação dos produtos indicados e seus respectivos endereços de destino:

[GIF animado: Imagem 3: Selecionados os produtos, clique no botão "Gerar Remanejamento" para realizar a geração das tarefas de remanejamento.…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012295062)

Na nova tela que é aberta, analise se as informações estão corretas e clique no botão **"Confirmar Tarefas"**:

[GIF animado: Imagem 4: Na nova tela que é aberta, analise se as informações estão corretas e clique no botão "Confirmar Tarefas" :](https://ajuda.sankhya.com.br/hc/article_attachments/1500012295102)

**Observação:** se o processo ocorrer de maneira correta, será apresentada a mensagem **"Tarefas geradas com sucesso!"**, assim como demonstramos acima; caso contrário, se for localizado algum impedimento na confirmação, a mensagem **"Problemas na confirmação das tarefas, verifique!"** será exibida e, logo em seguida, teremos a mensagem **"Erro na geração das tarefas. Não existe endereço de movimentação vertical disponível para o Endereço: XXXXX."** para que sejam feitas as devidas correções.

Finalizando a geração das tarefas, acesse a tela [Gerência do WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120453-Ger%C3%AAncia-do-WMS), escolha o tipo de tarefa **"Transferência"** e confirme se a geração da tarefa ocorreu corretamente:

[GIF animado: Imagem 5: Finalizando a geração das tarefas, acesse a tela Gerência do WMS , escolha o tipo de tarefa "Transferência" e confirme…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012647421)

Após isso, acesse o Coletor SuperWaba com o usuário responsável pela função de **"Transferência"**, informe o **"Cód. Equipamento"** e clique no botão **"Tarefa"**. Informe o **"Endereço de Origem"**, o **"Produto"** e **"Endereço de Destino"**:

[GIF animado: Imagem 6: Após isso, acesse o Coletor SuperWaba com o usuário responsável pela função de "Transferência" , informe o "Cód.…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012310682)

**Nota:** caso não existam mais tarefas em aberto, será exibida a mensagem **"Não há tarefas em aberto/adequadas para o usuário/Equipamento"** ao final do processo.

Após finalizar todos os passos que descrevemos acima, na tela [Estoque / Endereçamento WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120393-Estoque-Endere%C3%A7amento-WMS) você poderá filtrar o Produto e confirmar se ele foi remanejado para o endereço correto.

---

**![Imagem 7: Observações importantes a respeito da rotina de Remanejamento de Estoque :](https://ajuda.sankhya.com.br/hc/article_attachments/16979109348631) Observações importantes a respeito da rotina de Remanejamento de Estoque:**

- As tarefas de Remanejamento serão geradas como reabastecimento para o picking caso o estoque dele seja maior do que zero. Assim, encontrando-se o endereço de picking com o estoque zerado, o Remanejamento será feito entre endereços de pulmão, seguindo a Estratégia realizada na [Preferências da Geração de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008361662-Remanejamento-de-estoque#prefer%C3%AAnciasdagera%C3%A7%C3%A3odetarefas), seja Pela proximidade do picking ou Pela capacidade do pulmão.
- Quando as movimentações de transferência forem realizadas através das telas [Registro de Avarias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120333-Registro-de-Avarias), Remanejamento de Estoque ou [Transferência entre Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107213-Transfer%C3%AAncia-entre-Endere%C3%A7os), ao realizar a execução da tarefa, você deverá informar a **"Data de Validade"** e/ou **"Data de Fabricação"** do produto que será movimentado. Dessa forma, o sistema irá validar se as datas informadas constam no endereço de origem da tarefa. Se a data informada estiver incorreta, será apresentada a mensagem abaixo:

[GIF animado: Imagem 8: Quando as movimentações de transferência forem realizadas através das telas Registro de Avarias , Remanejamento de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500012663501)

- Caso você tente realizar um Remanejamento e o endereço de destino esteja marcado como **"Lote Único"** (tela [Endereços de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#abageral)), será possível realizar a transferências se ambos os endereços possuírem o mesmo produto e lote. Assim, a transferência não poderá acontecer entre endereços de lotes distintos, pois eles não podem ser alocados no mesmo endereço. O mesmo ocorrerá para a Transferência entre Endereços.
- Ao gerar as tarefas de remanejamento, se forem encontrados endereços que não suportem a quantidade a ser transferida, será apresentada a seguinte mensagem:

  **"A capacidade do endereço X não suporta a quantidade a ser movimentada do Produto Y. Verifique as configurações de Metro Cúbico e Peso Máximo".**

---
