---
id: "360044286313"
titulo: "Melhores Práticas para Ressuprimento e Dimensionamento de Endereços no WMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044286313-Melhores-Pr%C3%A1ticas-para-Ressuprimento-e-Dimensionamento-de-Endere%C3%A7os-no-WMS"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-07-22T15:59:05Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "WMS", "Ressuprimento", "Estoque", "Dimensionar estoques corretamente", "Otimizar reabastecimento picking", "Configurar estoque máximo", "Logística"]
---

# Melhores Práticas para Ressuprimento e Dimensionamento de Endereços no WMS

(1)** Dimensionamentos de Endereços (Picking/Pulmão)**

**Dimensionar para Ressuprir de forma correta atendendo a Demanda**

Analisando a Cadeia de Suprimentos nos tempos de hoje, o cenário adequado para definição da demanda de um produto seria receber os produtos dos fornecedores e expedir conforme a demanda de Pedidos, isso em cenário de demanda controlável/exata. Dentro dos setores de Planejamento das empresas existem algumas ferramentas que são utilizadas para fazer o levantamento dessas demandas sejam elas diárias, mensais ou por período que dê a empresa números exatos ou aproximados das demandas de um determinado produto. Existem produtos que é maior o desafio de medir e ter números em "mãos", devido sua nacionalidade, processo de manufaturas e etc.

Mediante isso, dentro da Logística existe o desafio de manter estes produtos sempre abastecidos em seus endereços de armazenagem, tanto nos endereços de Picking (apanha) e endereços de Pulmão (armazenagem). Para isso, usamos os parâmetros baseados nas demandas para, assim, definir estoque mínimo (quantidade determinada previamente para que ocorra o acionamento da solicitação do pedido de compra, que as vezes é confundido com "Estoque de Segurança", também denominado "Ponto de Ressuprimento) e também estoque Máximo. Com estes parâmetros atualizados, o risco de ocorrer corte dentro do Armazém é reduzido de forma significativa, tornando a operação tanto de Recebimento quanto de Armazenagem mais eficiente e eficaz.

Dentro do CD (Centro de Distribuição), não é incomum ver alguns sistemas e mecanismos que ajudam a operação a reduzir em 50% o tempo de operação. Alguns dos sistemas são: carrosséis, linhas de separação. O principal fator normalmente dito para esse excesso de capacidade é de responder rapidamente às demandas dos clientes. Entretanto, a maioria dos pedidos poderia ser planejada dentro de uma janela de serviço. O segredo é nivelar a carga da distribuição com o planejamento em ondas, pedidos em lote e áreas de separação do armazém. A separação de pedidos é uma das mais importantes atividades do fluxo de materiais porque consome uma grande parcela de recursos (tempo do ciclo do pedido, distância, mão-de-obra, etc), e é a penúltima atividade do fluxo de materiais do armazém.

Com base nas informações e conceitos vistos acima, alguns pontos no momento da implantação do WMS são importantes para que a operação fique com seu processo sem interrupções por falta de estoque em endereços de pulmão.

**(2)** As configurações indicadas para endereços de Picking é que sempre seja configurado com a menor unidade de medida (geralmente a padrão).

**(2)** Endereços de Pulmão com caixas masters, consequentemente os abastecimentos serão feitos em CX.

**(2)** Para que o sistema faça o reabastecimento de forma eficiente e que atenda uma alta demanda da OC, é necessário definir o giro do produto, lembrando que menos abastecimentos, menos desgastes dos equipamentos e maior número de separações executadas, geralmente os reabastecimentos atende uma demanda de 3 dias ou mais (depende do Giro e o dimensionamento do picking).

![Imagem 1: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16201687819031) **IMPORTANTE:**

Hoje o sistema já possui mecanismo onde o reabastecimento não mais extrapola o estoque máximo do picking no envio da OC para Expedição.

(1)** Por que não extrapolar o estoque máximo do picking?**

Isso evita que as ruas se tornem "endereços de Pulmão", muitas vezes prejudicando a movimentação dos separadores nas ruas.

Com o estoque do picking preenchido no Máximo (bem dimensionado) vai suprimir toda a demanda, vai garantir as ruas livres para movimentação, mantendo o Armazém organizado e com a operação íntegra de erros devido a dificuldade de movimentação.

Regra padrão para Reabastecimento Corretivo: atender demanda da OC + quantidade do estoque máximo do picking.

Exemplo: Demanda da OC 50UN

Estoque Max: 50UN

Estoque atual:0

Envio da OC>>>Geração do reabastecimento com 100UN - 50 pra atender a demanda + 50 pra manter o picking completo (lembrando que esses outros 50 vai ficar na rua).

No novo cenário o sistema vai descer no Pulmão apenas as 50 UN e caso a tarefa não chegue a uma quantidade exata na conversão de unidades, o sistema faz o arredondamento pra maior ou pra menor, isso pra sempre descer caixa completa do pulmão e evitar que sejam abertas as caixas e consequente manter frações no pulmão, ocupando um endereço com uma pequena quantidade de produto, tornando este endereço ocioso.

**(2)** Uma boa dica é 1 hora/tempo que for necessário antes de começar as operações de "Separação", o Gerente de Logística ou responsável pelo armazém fazer o levantamento de necessidade de "Reabastecimento" dos endereços de Picking. Isso pode ser feito por nossa Rotina: Ressuprimento Preventivo.

O Ressuprimento Preventivo é um importante procedimento envolvido na rotina de um armazém, que permite a verificação e o abastecimento de todos os seus endereços antes do início das separações de mercadoria. Assim, aprimorando o processo, o gestor de armazenagem poderá comandar reabastecimentos preventivos anteriormente ao começo da operação de separação de produtos.

Previsões adequadas otimizam os equipamentos, a capacidade da mão de obra e atendem as necessidades do cliente.

**![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201660381847) OBSERVAÇÃO:**

Importante que todos os Pickings estejam com estoque Máximo configurado, pois o sistema vai usar como parâmetro para analisar a necessidade de Reabastecimento.

(1)** Onde Configurar o Estoque Máximo dos Picking?**

Configurações » Cadastros » Produtos » Produtos

Aba: **WMS**.

ou

WMS » Cadastros » Endereço de Armazenamento

Aba: **Produtos**.

**Lembrando que configurando em um local, os dados serão visualizados no outro local. Pois, o cadastro é na mesma tabela.**
