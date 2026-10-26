---
id: "360044597954"
titulo: "Fluxo de Processos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597954-Fluxo-de-Processos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:55Z"
rotulos: ["manual", "Configuração", "Fluxo", "Tela", "Fluxo de Processos", "Lançador", "Menu do Sistema", "Novo Fluxo", "Processo", "br.com.sankhya.core.cad.fluxoprocessos", "Fluxo de Processos manual", "Fluxo de Processos: Criando e Visualizando Processos de Forma Estruturada", "Sankhya-Om"]
---

# Fluxo de Processos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310659043735) Módulo: Configurações > Avançado
```

---

A tela Fluxo de Processos permite ao usuário criar fluxos demonstrativos de processos usados no Sankhya-Om.

Ao criar um fluxo, você adicionará as telas que serão usadas nele e interligará as mesmas para demonstrar o processo.

Ao finalizar o processo o usuário poderá adicionar o mesmo como uma tela no sistema, utilizando para isto a tela de **"Menu do Sistema"**.

A tela de configuração de fluxo de processo é acessada pelo menu **"Configurações> Avançado> Fluxo de Processos"**.

Assim, o sistema apresentará nesta tela uma grade com todos os fluxos já configurados, para consultá-los, você poderá apenas dar um duplo clique sobre estes.

![Imagem 2: Assim, o sistema apresentará nesta tela uma grade com todos os fluxos já configurados, para consultá-los, você poderá…](https://ajuda.sankhya.com.br/hc/article_attachments/360086065634)

Para criar um novo fluxo, clique no botão ![Imagem 3: Para criar um novo fluxo, clique no botão " Novo " , nomear o Fluxo pelo campo " Descrição " e adicione as telas e os…](https://ajuda.sankhya.com.br/hc/article_attachments/16275381162007) **"Novo"**, nomear o Fluxo pelo campo **"Descrição"** e adicione as telas e os processos externos envolvidos neste fluxo através dos elementos ![Imagem 4: Para criar um novo fluxo, clique no botão " Novo " , nomear o Fluxo pelo campo " Descrição " e adicione as telas e os…](https://ajuda.sankhya.com.br/hc/article_attachments/360087440793) **"Inserir tela"** e ![Imagem 5: Para criar um novo fluxo, clique no botão " Novo " , nomear o Fluxo pelo campo " Descrição " e adicione as telas e os…](https://ajuda.sankhya.com.br/hc/article_attachments/360087440973) **"Inserir Processo Externo"**.

Assim que o botão Inserir tela for acionado, o sistema abrirá a janela **"Selecione uma tela"** apresentando todas as telas disponíveis ao usuário logado, para que este possa selecionar aquelas que irão compor o novo fluxo.

Você poderá navegar na árvore ou digitar no campo pesquisa desta janela o nome específico da tela que desejar adicionar ao fluxo.

Ao selecionar a tela, dê um duplo clique sobre ela ou pressionar o botão **"OK"** da janela, pra que a mesma seja inserida ao layout do fluxo.

Depois de inserida nesta rotina a tela poderá ser arrastada através do mouse e posicionada de acordo com a vontade do usuário.

A inserção do processo **"Inserir Processo Externo"**, teremos uma imagem com texto que representa um processo externo para o qual não há uma tela no sistema para suprir, ao clicar no botão de adição de processo externo aparecerá uma janela requisitando que seja digitada uma descrição para o elemento, a descrição é obrigatória e o elemento tem ligações livres com qualquer elemento, tanto para recebimento quanto para saída.

[GIF animado: Imagem 6: A inserção do processo "Inserir Processo Externo" , teremos uma imagem com texto que representa um processo externo…](https://ajuda.sankhya.com.br/hc/article_attachments/360086069194)

Definidas as telas que farão parte do fluxo você irá definir o fluxo propriamente dito. Para isso dispomos dos seguintes elementos:

![Imagem 7: : O íc one "Adicionar início" representa o início do fluxo , só pode haver um por diagrama e nenhum outro elemento pode…](https://ajuda.sankhya.com.br/hc/article_attachments/360087321173): O ícone **"Adicionar início"** representa o início do fluxo, só pode haver um por diagrama e nenhum outro elemento pode se ligar a ele, enquanto ele pode se ligar a múltiplos elementos.

![Imagem 8: : O í cone "Adicionar Fim" exibido representa o fim do fluxo , assim como o elemento de início só pode haver um por…](https://ajuda.sankhya.com.br/hc/article_attachments/360086136094): O ícone **"Adicionar Fim"** exibido representa o fim do fluxo, assim como o elemento de início só pode haver um por fluxo, contudo o fim do fluxo pode receber múltiplas ligações, mas não pode se ligar a nada.

![Imagem 9: : Trata-se de uma caixa de texto. O texto é especificado ao clicar no botão no menu para adicionar um comentário e é de…](https://ajuda.sankhya.com.br/hc/article_attachments/360086141034): Trata-se de uma caixa de texto. O texto é especificado ao clicar no botão no menu para adicionar um comentário e é de dígito obrigatório, um comentário só pode ter uma ligação partindo dele para um elemento e não pode receber ligações, é possível editar um comentário dando dois cliques rápidos com o mouse, também é possível redimensionar os comentários nas bordas inferior e lateral direita.

![Imagem 10: : O ícone exibido aqui representará a opção "Inserir Bifurcação" , sendo que este é o elemento que divide o fluxo de…](https://ajuda.sankhya.com.br/hc/article_attachments/360086148014): O ícone exibido aqui representará a opção **"Inserir Bifurcação"**, sendo que este é o elemento que divide o fluxo de acordo com uma condição que pode ser expressa por meio de um comentário, podendo receber múltiplas ligações, mais apenas duas saídas serão permitidas, uma para o caso verdadeiro (S) e outra para o caso falso (N). Para criar uma ligação saindo de S ou N dê um clique sobre a letra.

![Imagem 11: : O ícone tido como "Adicionar junção" será o elemento de junção de processos, pode receber múltiplas ligações, mais só…](https://ajuda.sankhya.com.br/hc/article_attachments/360086144914): O ícone tido como **"Adicionar junção"** será o elemento de junção de processos, pode receber múltiplas ligações, mais só há uma ligação de saída.

**![Imagem 12: : Por meio do "Zoom" será possível aumentar ou diminuir o fluxo movendo o cursor para a direita e a esquerda,…](https://ajuda.sankhya.com.br/hc/article_attachments/8927193490967):** Por meio do **"Zoom"** será possível aumentar ou diminuir o fluxo movendo o cursor para a direita e a esquerda, respectivamente.

Ao passar o cursor do mouse por cima de uma tela ou processo externo adicionado ao fluxo, aparecerá um menu que permitirá que você remova por meio do botão ![Imagem 13: Ao passar o cursor do mouse por cima de uma tela ou processo externo adicionado ao fluxo, aparecerá um menu que…](https://ajuda.sankhya.com.br/hc/article_attachments/16967929925143)**"Remover"**  ou  **"Criar ligação"**  desta tela a outras telas e elementos do fluxo, através de uma seta de ligação.

Para criar estas ligações basta clicar sobre a opção Criar ligação de um elemento e levar a seta de ligação até o outro elemento desejado, dando um clique sobre este elemento para que a ligação seja formada.

**Nota:** a seta de ligação fará uma ligação entre um elemento e outro, por isto se houver no layout apenas um elemento e você acionar a seta de ligação por engano, bastará clicar na tecla **"Esc"** para que a seta desapareça, liberando o cursor do mouse, para que então o usuário possa adicionar outro elemento e definir o fluxo.

Ao clicar sobre a seta de ligação ![Imagem 14: Ao clicar sobre a seta de ligação , aparecerá outro menu que permitirá o usuário: " Remover " , " Editar nome " ou "…](https://ajuda.sankhya.com.br/hc/article_attachments/8929187965847), aparecerá outro menu que permitirá o usuário: ![Imagem 15: Ao clicar sobre a seta de ligação , aparecerá outro menu que permitirá o usuário: " Remover " , " Editar nome " ou "…](https://ajuda.sankhya.com.br/hc/article_attachments/16967929925143) **"Remover"**, **"Editar nome"** ou **"Bidirecionar"** a ligação.

[GIF animado: Imagem 16: Ao clicar sobre a seta de ligação , aparecerá outro menu que permitirá o usuário: " Remover " , " Editar nome " ou "…](https://ajuda.sankhya.com.br/hc/article_attachments/360087356093)

Pode-se utilizar os elementos de Junção e Bifurcação para deixarmos o fluxo mais completo.

[GIF animado: Imagem 17: Pode-se utilizar os elementos de Junção e Bifurcação para deixarmos o fluxo mais completo.](https://sankhyasd.zendesk.com/hc/article_attachments/360056834853/embim251.gif)

Ao finalizar o processo, você poderá adicionar o mesmo como uma tela do sistema, para isto deverá acessar a tela do menu **"Configurações> Avançado> Menu do Sistema"**, onde será criado um **"Lançador"** para o processo que foi definido na tela de Fluxo de Processo.

Na tela Menu do Sistema, selecione a pasta do módulo ao qual deseja vincular o fluxo, e em seguida clique no botão **"Criar Novo Item"**.

Neste momento o sistema abrirá a janela **"Criando novo item em: "xxxx""**, onde o usuário:

- Definirá no campo **"Descrição"** o nome do item de menu;
- Informará no campo **"Tipo"** que se trata de um **"Lançador"**;
- E no campo **"Tipo de Lançador"** informará que se trata de um **"Fluxo de processo"**.

Ao clicar no botão **"Próximo"** o sistema exibirá os fluxos criados na tela de **"Fluxo de Processo"** e bastará que o usuário selecione o fluxo que deseja lançar naquele item.

[GIF animado: Imagem 18: Ao clicar no botão " Próximo " o sistema exibirá os fluxos criados na tela de "Fluxo de Processo" e bastará que o…](https://ajuda.sankhya.com.br/hc/article_attachments/360087431253)

Clicando em **"Concluir"** o usuário estará finalizando a criação do lançador.

Para visualizar a nova tela, bastará pesquisar pelo nome utilizando o campo de pesquisa de telas do Sankhya-Om, a tela já estará disponível.

É possível encontrar a tela também na árvore ou lista de telas do módulo no qual a tela foi criada, bastará clicar no ícone do módulo que está localizado no Desktop do Sankhya-Om.

![Imagem 19: É possível encontrar a tela também na árvore ou lista de telas do módulo no qual a tela foi criada, bastará clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/360087436433)

Após abrir a tela, veremos o fluxo da mesma forma que definimos na tela ‘Fluxo de Processo’, porém aqui não teremos o painel de controle, e o usuário poderá alterar o layout do fluxo apenas temporariamente.

Ao passar o cursor do mouse sobre os elementos Tela e Processo Externo, o sistema apresentará a mensagem **"Clique para abrir a tela"** ou **"Alterar Processo"**, desta forma, pode-se dar um clique sobre a tela para acessá-la ou dar um clique sobre o processo externo para marcá-lo como **"executado"**.

Para iniciar o fluxo o usuário posicionará o cursor do mouse sobre o elemento que está sendo ligado pelo elemento de Início e, se for uma ‘tela’, com um clique abrirá a mesma para executar a tarefa, se for um ‘processo externo’ deverá realizá-lo e depois clicar para marcar como executado.

Feito isto, o sistema considerará que a primeira tela ou processo foi executado e irá marcá-lo com um sinal verde em forma de "V".

O usuário dará sequência ao processo abrindo a próxima tela e realizando sua tarefa ou realizando o próximo processo externo do fluxo, e assim por diante até finalizar todo o processo.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597954-Fluxo-de-Processos#top)
