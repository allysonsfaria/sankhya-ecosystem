---
id: "22864139891223"
titulo: "Gestão de Licenças"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:42:35Z"
rotulos: ["Configuração", "Licenças", "Administração do Servidor", "Administração", "br.com.sankhya.sasserver.ger.lic", "INITSASONLINE", "Aquisição de licenças", "Gestão de licenças", "Gerenciar licenças", "Sankhya Om", "SAS"]
---

# Gestão de Licenças

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310528796951) Módulo: Configurações > Avançado              ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42310508165527) Versão disponível: A partir da 4.26
```

---

Por meio desta tela, o administrador da aplicação consiguirá analisar o consumo de licenças de seu ambiente, com detalhes de consumo por grupos, módulos e informações de cada usuário que está consumindo licenças.

![Imagem 3: Para utilizar essa tela é necessário que o Sankhya Om esteja se comunicando com a nova versão do SAS ( Serviço de…](https://ajuda.sankhya.com.br/hc/article_attachments/22864379051799) Para utilizar essa tela é necessário que o Sankhya Om esteja se comunicando com a nova versão do SAS (Serviço de Acesso ao Sistema). Essa comunicação é feita através da ativação do parâmetro **"Alternar as versões do SAS - INITSASONLINE"** na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834). Caso ele não esteja disponível na referida tela, poderá ser criado manualmente seguindo as seguintes regras:

**Chave:** INITSASONLINE

**Descrição:** Ativa a nova versão do SAS

**Módulos do Sistema:** Configurações

**Menu:** Diversas

**Aba:** Diversas

**Tipo:** Lógico

**Ligado/Desligado:** Ligado

Após ativar o uso da nova versão do SAS é possível acessar a tela Gestão de Licenças. Por padrão, o usuário SUP tem acesso a essa tela. Para os outros usuários é necessário conceder acesso através da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854) no **Sankhya Om**.

![Imagem 4: Após ativar o uso da nova versão do SAS é possível acessar a tela Gestão de Licenças . Por padrão, o usuário SUP tem…](https://ajuda.sankhya.com.br/hc/article_attachments/22864600389783)

**Nota:** essa tela também pode ser acessada por meio da [Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833). Neste caso, acesse a opção **"Administração"** localizada no menu do seu perfil e, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833-Administra%C3%A7%C3%A3o-do-Servidor#abageral), acione o botão ![Imagem 5: Nota: essa tela também pode ser acessada por meio da Administração do Servidor . Neste caso, acesse a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/22864646669207)**"Gerenciar Sessões"** para exibir o pop-up **"Gerenciador de Sessões"**, assim, clique no botão ![Imagem 6: Nota: essa tela também pode ser acessada por meio da Administração do Servidor . Neste caso, acesse a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/22864695755159) **"Gerenciar Licenças"** e este o redirecionará a referida tela.

[GIF animado: Imagem 7: Nota: essa tela também pode ser acessada por meio da Administração do Servidor . Neste caso, acesse a opção…](https://ajuda.sankhya.com.br/hc/article_attachments/22864986641303)

Essa tela divide-se em três grids, clique nos links abaixo para conferir as especificidades de cada um deles:

| [Consumo de licenças](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as#Consumodelicen%C3%A7as) | [Produtos do grupo](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as#Produtosdogrupo) |
| --- | --- |
| [Detalhes de consumo do grupo selecionado](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as#Detalhesdeconsumodogruposelecionado) |  |

### Consumo de licenças

Exibe a quantidade de licenças contratadas, a quantidade de licenças em uso e a quantidade de licenças disponíveis naquele mesmo momento. Cada linha desse grid representa um grupo de licenças, geralmente representado por alguma letra do alfabeto.

Se alguma linha estiver destacada na cor vermelha, significa que todas as licenças daquele grupo já estão sendo utilizadas.

![Imagem 8: Se alguma linha estiver destacada na cor vermelha, significa que todas as licenças daquele grupo já estão sendo…](https://ajuda.sankhya.com.br/hc/article_attachments/22865507149079)

Esse grid conta com um campo de filtro para que o administrador possa refinar sua pesquisa para algum módulo específico que ele queira analisar o consumo, para isso, basta selecioná-lo no campo **"Produto"**.

Além disso, todas as informações exibidas pela tela Gestão de Licenças mostram como está o consumo de licenças de acordo com o horário em que a tela foi aberta. Pode-se dizer que, no momento em que o administrador abre essa tela, o sistema tira uma 'fotografia' de todo o consumo de licenças e exibe nos grids.

O consumo de licenças do Sankhya é baseado na abertura de telas por parte do usuário, isso significa que, se o administrador ficar com essa tela aberta por muito tempo, as informações exibidas podem não mais estar refletindo a verdade, pois durante esse período, os usuários podem ter fechado telas e aberto outras telas, alterando a quantidade de licenças que estão sendo consumidas. Sendo assim, o administrador deve utilizar o botão ![Imagem 9: O consumo de licenças do Sankhya é baseado na abertura de telas por parte do usuário, isso significa que, se o…](https://ajuda.sankhya.com.br/hc/article_attachments/22866582841239) **"Atualizar"** para recarregar as informações mais recentes na tela.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as#top)

### Produtos do grupo

Este grid apresenta a relação de módulos/produtos associados ao grupo selecionado no grid anterior. A medida que o usuário navega pelo grid Consumo de licenças, os respectivos produtos de cada grupo são exibidos nesse espaço.

[GIF animado: Imagem 10: Este grid apresenta a relação de módulos/produtos associados ao grupo selecionado no grid anterior. A medida que o…](https://ajuda.sankhya.com.br/hc/article_attachments/22865551467287)

Vale lembrar que o "grupo" é a maneira utilizada para separar os módulos de acordo com o Tipo de Licença, como, por exemplo, as licenças simultâneas e licenças específicas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as#top)

### Detalhes de consumo do grupo selecionado

Neste grid serão exibidas as informações dos usuários que estão consumindo licenças do grupo selecionado no grid Consumo de licença. 

![Imagem 11: Neste grid serão exibidas as informações dos usuários que estão consumindo licenças do grupo selecionado no grid…](https://ajuda.sankhya.com.br/hc/article_attachments/22865599629975)

**Observação:** o Consumo de licenças ocorre apenas quando os usuários abrem telas do sistema. Desse modo, esse grid vai exibir somente os usuários que estão, de fato, consumindo alguma licença. Usuários que estejam, eventualmente, logados na aplicação mas sem usar nenhuma tela, não serão exibidos nessa tela. Para ver todos os usuários que estão logados na aplicação, utilize o Gerenciador de Sessões na tela Administração do Servidor.

#### Ver detalhes do usuário

Através do botão ![Imagem 12: Através do botão "Ver detalhes do usuário" , o administrador pode visualizar mais informações sobre o que cada usuário…](https://ajuda.sankhya.com.br/hc/article_attachments/22865800886295) **"Ver detalhes do usuário"**, o administrador pode visualizar mais informações sobre o que cada usuário está consumindo de licenças, inclusive as telas abertas naquele momento. 

Ao clicar neste botão será aberto o pop-up **"Detalhes de consumo do grupo selecionado"** com as informações detalhadas do usuário, separadas em dois grids:

![Imagem 13: Ao clicar neste botão será aberto o pop-up "Detalhes de consumo do grupo selecionado" com as informações detalhadas do…](https://ajuda.sankhya.com.br/hc/article_attachments/22865988362647)

- **Licenças em consumo pelo usuário:** exibe quantas licenças o usuário está consumindo. Caso o usuário esteja conectado em dois ou mais navegadores ao mesmo tempo, esse grid mostrará uma linha para cada sessão (uma linha para cada navegador que o usuário fez login e consumiu licenças);
- **Telas em execução:** apresenta as telas que o usuário está utilizando naquele momento, assim como, o módulo ao qual aquela tela está associada.

#### Finalizar licenças do usuário

Por meio do botão ![Imagem 14: Por meio do botão "Finalizar licenças do usuário" , o administrador pode finalizar as licenças dos usuários que estão…](https://ajuda.sankhya.com.br/hc/article_attachments/22866126380567) **"Finalizar licenças do usuário"**, o administrador pode finalizar as licenças dos usuários que estão consumindo licenças naquele momento.

Ao clicar nesse botão, será exibido um pop-up para confirmar se o administrador realmente deseja finalizar as licenças do usuário. É possível finalizar as licenças de mais de um usuário ao mesmo tempo, basta selecionar vários usuários no grid.

Se confirmar a execução, todas as licenças que estiverem sendo utilizadas pelo usuário selecionado no grid serão finalizadas e devolvidas aos seus respectivos grupos. Além disso, no momento em que a licença do usuário for finalizada, as telas que ele estava utilizando vão exibir uma mensagem informando que aquela licença não está mais disponível:

**"A licença para o uso dessa tela não está mais disponível. Procure o administrador do Sankhya ou tente abrir essa tela novamente mais tarde.**

**OBS: Dados não salvos podem ter sido perdidos."**

O usuário que teve a sua licença finalizada não conseguirá utilizar as telas que já estavam abertas, pois as licenças associadas a elas foram finalizadas pelo administrador do sistema.

**Nota:** apesar das licenças desse usuário terem sido finalizadas, ele continua logado no sistema, podendo abrir novas telas se houver licenças disponíveis.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/22864139891223-Gest%C3%A3o-de-Licen%C3%A7as#top)
