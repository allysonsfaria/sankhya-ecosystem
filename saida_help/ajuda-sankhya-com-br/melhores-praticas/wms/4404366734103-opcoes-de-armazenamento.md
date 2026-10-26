---
id: "4404366734103"
titulo: "Opções de armazenamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404366734103-Op%C3%A7%C3%B5es-de-armazenamento"
trilha: "Melhores Práticas > WMS"
atualizado_em: "2026-07-22T15:23:20Z"
rotulos: ["Configuração", "WMS", "Estoque", "#publicadoHyago", "Tarefas de armazenagem geradas automaticamente", "Armazenagem Seletiva e Expresso", "Processo sequencial e otimizado", "Squad WMS", "Armazenagem"]
---

# Opções de armazenamento

Com a situação do Recebimento **“Aguardando Armazenagem”** é possível fazer a geração da tarefas de armazenamento pela Rotina: Tarefas de Recebimento. Tarefas que são geradas obedecendo os algoritmos de armazenagem configurados na Rotina: Configurações de Armazenagem. A configuração da regra é de acordo com o processo do cliente e outros fatores que podem influenciar qual a melhor forma de gerar as tarefas, hoje existem três algoritmos: Picking, Completar Endereço e Endereços Vazios.

Geradas as tarefas de Recebimento/Armazenagem as mesmas podem ser executadas pelos operadores e para isso o WMS dispõe de algumas funcionalidades:

(1)** Armazenagem Seletiva:** a "Armazenagem seletiva" permite que o usuário faça a escolha de qual tarefa será armazenada primeiro, de acordo com a "doca" e com o "produto".

(1)** Armazenagem:** tarefa utiliza para guardar os produtos dentro do armazém. Armazenagem convencional, tendo que executar item a item, Armazena, volta na Doca pega outro Produto armazena e assim até finalizar toda armazenagem. Bipado, após concluir a armazenagem de um produto, o sistema voltará à tela para informar o produto novamente e tudo recomeçará. Se não houver tarefas para o "produto" e "doca" informada, será exibida uma mensagem comunicando ao usuário que não há tarefas. Se por algum motivo o coletor travar no meio de um processo de armazenagem, onde o usuário esteja definindo o destino da tarefa, ao entrar no coletor novamente, informar a "tarefa" e "equipamento" e clicar em "Tarefa" o sistema exibirá uma mensagem de tarefas pendentes, para o usuário decidir se irá ou não executar a tarefa.

(1)** Armazenamento Expresso:** Essa tarefa permite que o operador faça a coleta de todos os produtos da nota e execute o armazenamento de maneira sequencial, evitando que o operador armazene um produto e tenha que retornar a doca para pegar outro produto. Na utilização da rotina de "Armazenagem Expressa", o coletor de dados não irá guardar os dados localmente; este processamento ficará a cargo do servidor. Conta-se também com uma paginação de dados nas telas de "Produtos Coletados" e "Produtos Disponíveis do Armazenamento Expresso". Na tela de informação do lote, utiliza-se ufaixa dma marcação para selecionar os lotes; nos casos em que existem muitos lotes, visando facilitar a localização do lote desejado, pode-se fazer uso do parâmetro **"Informar lote manualmente no armazenam. expresso? -** **WMSDIGLOTARMEXP"**, que quando ativado, ao invés de escolher-se o lote no armazenamento expresso pela marcação, tem-se um campo para digitação do mesmo.
