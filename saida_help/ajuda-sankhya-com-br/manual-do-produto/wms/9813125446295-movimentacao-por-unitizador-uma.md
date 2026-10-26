---
id: "9813125446295"
titulo: "Movimentação por Unitizador (UMA)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:17:23Z"
rotulos: ["Configuração", "WMS", "Estoque", "Endereço de Armazenamento", "Picking", "UMA", "Movimentação", "Otimize operações logísticas em armazéns", "Agrupe produtos para melhor gestão e produtividade", "Habilite e configure UMAs no sistema para operações logísticas", "Logística"]
---

# Movimentação por Unitizador (UMA)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311658462743) Versão disponível: A partir da 4.15
```

---

Armazéns com grande fluxo de operações e mercadorias exigem um controle de entradas e saídas exaustivo, por isso, é fundamental a existência de mecanismos otimizados de movimentação que acelere os processos internos da operação logística.

Nesse sentido, o processo de Movimentação por Unitizador (UMA - Unidade de Movimentação e Armazenagem) irá otimizar a movimentação e o controle dos produtos por meio de agrupamentos dentro do armazém, contribuindo positivamente com a produtividade dos operadores e com a gestão das mercadorias e endereços.

Para entender como funciona este processo em cada rotina, acesse os links abaixo:

| [Parametrizações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Parametriza%C3%A7%C3%B5esIniciais) |  | [Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Recebimento) |
| --- | --- | --- |
| [Armazenagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Armazenagem) |  | [Reabastecimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Reabastecimento) |
| [Registro de Ocorrência](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#RegistrodeOcorr%C3%AAncia) |  | [Transferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Transfer%C3%AAncia) |
| [Movimentação Pró Ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Movimenta%C3%A7%C3%A3oPr%C3%B3Ativa) |  | [Remanejamento de UMA](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#RemanejamentodeUMA) |
| [Expedição - Picking](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Expedi%C3%A7%C3%A3o-Picking) |  | [Inventário de endereço com UMA](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#Invent%C3%A1riodeendere%C3%A7ocomUMA) |

### Parametrizações Iniciais

Para iniciar o processo de movimentação por UMA, o uso do unitizador deverá ser habilitado no Sankhya Om para as rotinas de **"Recebimento"**, **"Armazenagem"**, **"Movimentação"**, **"Expedição"** e **"Inventário"**. 

Primeiramente, ative o parâmetro **"Movimentação por unitizador (UMA)? - WMSMOVUNIUMA"** na tela [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias).

**Observação:** enquanto houver saldo de estoque em pelo menos uma UMA ou qualquer histórico de movimentação por UMA registrado no banco de dados, não será possível desligar este parâmetro. Caso tente, será exibida a seguinte mensagem:

**"O parâmetro WMSMOVUNIUMA não pode ser alterado, pois existe estoque registrado no WMS."**

Porém, será possível realizar uma recontagem de registro de conferência de uma UMA e seu respectivo endereço independente do parâmetro acima ser ligado ou não. Desse modo, com ele desligado, informe uma UMA fictícia com letras maiúsculas para que o coletor TotalCross possa validar a recontagem, por exemplo, insira no campo UMA, os caracteres UMA123.

Depois, configure na tela [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento), aba [Unitizador (UMA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313#AbaUnitizador(UMA)), a quantidade de UMAs que será permitida para cada endereço analítico.

![Imagem 2: Depois, configure na tela Endereço de Armazenamento , aba Unitizador (UMA) , a quantidade de UMAs que será permitida…](https://ajuda.sankhya.com.br/hc/article_attachments/9837068987927)

Em seguida, você deverá criar a máscara do código UMA para as mesmas rotinas citadas acima no parâmetro **"Máscara de Endereço UMA WMS. - MASCUMAWMS"**, considerando que, o referido código terá um prefixo e um sufixo totalizando no máximo 20 caracteres alfanuméricos, conforme o exemplo abaixo:

Prefixo (Fixo): **UMA**

Sufixo (Fixo): **W**

Máscara entre Prefixo e Sufixo: **Até 16 caracteres numéricos.**

Exemplo: **UMA0000000000000000W**

Logo após, configure na tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108573-Relat%C3%B3rios-Formatados-) o modelo padrão de etiqueta das UMAs a ser usado para impressão e informe o código deste no parâmetro **"Define o tipo de modelo do relatório UMA - RELUMAETIQUETA"** e, em seguida, defina no parâmetro **"Impressora padrão para UMA. - IMPRESSORAUMA"** a impressora padrão para realizar a impressão das etiquetas. Este modelo poderá ser alterado de acordo com a necessidade do usuário. 

![Imagem 3: Logo após, configure na tela Relatórios Formatados o modelo padrão de etiqueta das UMAs a ser usado para impressão e…](https://ajuda.sankhya.com.br/hc/article_attachments/9837192063511)

Feito isso, determine a impressora que será utilizada para impressão das etiquetas. 

**Observação:** ao tentar imprimir uma etiqueta no coletor, caso ele não localize uma impressora configurada, será exibida a mensagem abaixo:

**"Não foi localizada uma impressora configurada para realizar esta impressão."**

Verifique na tela [Configurações por Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595354-Configura%C3%A7%C3%B5es-por-Usu%C3%A1rio) se você tem a permissão para acessar a função de Impressão UMA no coletor, bem como, o acesso às demais rotinas. 

![Imagem 4: Verifique na tela Configurações por Usuários se você tem a permissão para acessar a função de Impressão UMA no coletor,…](https://ajuda.sankhya.com.br/hc/article_attachments/9813407662103)

Depois, você irá gerar as etiquetas no coletor de uma UMA vazia ou reimprimir de uma UMA já existente para serem utilizadas nas rotinas de Recebimento, Armazenagem, Movimentação e Inventário. 

Para isso, acesse o coletor e acione o botão **"Impressão UMA"** e, em seguida, informe a quantidade de UMAs que deseja imprimir no campo **"Quantas UMAs deseja gerar?"** e clique em **"Imprimir"**.

![Imagem 5: Para isso, acesse o coletor e acione o botão "Impressão UMA" e, em seguida, informe a quantidade de UMAs que deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/9858803185943) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 7: Para isso, acesse o coletor e acione o botão "Impressão UMA" e, em seguida, informe a quantidade de UMAs que deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/9858823370263) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 9: Para isso, acesse o coletor e acione o botão "Impressão UMA" e, em seguida, informe a quantidade de UMAs que deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/9858867426967)

Lembrando que, caso não tenha cadastrado um modelo de etiqueta anteriormente, será emitida uma mensagem de alerta informando que é necessário fazer este cadastro para prosseguir com a impressão.

![Imagem 10: O sistema irá gerar as etiquetas conforme a seguinte regra:](https://ajuda.sankhya.com.br/hc/article_attachments/16922211333271) O sistema irá gerar as etiquetas conforme a seguinte regra:

O número único inicial deve ser igual ao último da UMA gerada anteriormente + 1, e o número único final deve ser igual ao último número da UMA gerada + a quantidade de UMAs que se deseja gerar. Logo, a primeira UMA será a de número 1.

**Exemplo 1:** Considerando que esta é a primeira vez que as UMAs serão geradas no sistema, vamos iniciar o uso de unitizadores com a criação de 5 novas UMAs. Então a contagem começa com o número 1 (UMA000001W) e o número final 5 (UMA000005W).

**Exemplo 2:** Se o usuário quiser criar mais 10 novas UMAs, o sistema irá considerar o último número gerado anteriormente (5) e iniciar a nova geração com o número 6 (UMA000006W).

Se desejar reimprimir uma etiqueta, clique na opção **"Reimprimir UMA"**, informe o código da UMA que deseja imprimir novamente no campo **"Qual UMA deseja reimprimir?"** e acione o botão **"Reimprimir UMA"**.

![Imagem 11: Se desejar reimprimir uma etiqueta, clique na opção "Reimprimir UMA" , informe o código da UMA que deseja imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/9859086176151) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 13: Se desejar reimprimir uma etiqueta, clique na opção "Reimprimir UMA" , informe o código da UMA que deseja imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/9859009723671) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 15: Se desejar reimprimir uma etiqueta, clique na opção "Reimprimir UMA" , informe o código da UMA que deseja imprimir…](https://ajuda.sankhya.com.br/hc/article_attachments/9858867426967)

Na tela [Gestão de UMA](https://ajuda.sankhya.com.br/hc/pt-br/articles/9811987930135) você poderá consultar e acompanhar todas as UMAs cadastradas e seus respectivos produtos armazenados nos endereços em tempo real.

![Imagem 16: Na tela Gestão de UMA você poderá consultar e acompanhar todas as UMAs cadastradas e seus respectivos produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/9837997425687)

Com as definições acima efetuadas, você poderá iniciar o processo de Recebimento no coletor de dados.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Recebimento

Após inserção dos dados da nota na [Central de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras), acesse a tela [Portal de Compras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953) e no **"Botão Outras Opções..."** clique na opção [Enviar para o WMS (Recebimento)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598054-Portal-de-Compras-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es#enviarparaowmsrecebimento), e então, um usuário de conferência deve acessar o registro de conferência do coletor e preenchê-lo com a mesma doca cadastrada ao enviar o WMS anteriormente, para assim, informar as UMAs que deseja atribuir aos produtos durante a conferência de Recebimento. 

Em seguida, no coletor de dados, clique na opção **"Conferência"**, em seguida no **"Registro de Conferência"** e informe no campo **"Qual a Doca"** o endereço da Doca em que se encontra os produtos que irá conferir.

**Importante:** a quantidade máxima de UMAs que podem ser utilizadas em uma conferência de entrada ficará limitada conforme determinado no Endereço de Armazenamento, aba Unitizador UMA.

**Observação:** quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar o botão [Recontar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#recontar), será criada uma tarefa de recontagem da(s) UMA(s) na doca e no endereço de destino. Desse modo, ao acessar o coletor TotalCross você pode conferir o **"Endereço"**, a **"UMA"** e o **"Produto"** que será recontado. 

![Imagem 17: Observação: quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar…](https://ajuda.sankhya.com.br/hc/article_attachments/9859181693207)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 19: Observação: quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar…](https://ajuda.sankhya.com.br/hc/article_attachments/9859183942807)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 21: Observação: quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar…](https://ajuda.sankhya.com.br/hc/article_attachments/9859127641111)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 23: Observação: quando o produto estiver em uma ou mais UMAs na doca e ainda possuir tarefas abertas e fechadas, ao acionar…](https://ajuda.sankhya.com.br/hc/article_attachments/9859187840279)

Caso informe uma Doca que não exista ou que não possua conferência pendente, serão apresentadas as seguintes mensagens respectivamente: 

**“Nenhuma Doca cadastrada para o código de barras do endereço ‘3.100.913’.”**

**“Nenhum recebimento encontrado para a Doca ‘‘3.100.913’.”**

Após confirmar a Doca, informe o código da **"UMA"** e clique em **"Continuar"**.

Em seguida, escolha que tipo de estratégia será utilizada para que o sistema possa validar se a quantidade de produtos alocados na UMA excederá a norma de paletização. Essa estratégia deverá estar cadastrada na tela [Cadastro de Tipos de Unitizador](https://ajuda.sankhya.com.br/hc/pt-br/articles/13660826815383) que, será apresentada somente com a habilitação dos parâmetros **"Valida capacidade da UMA no WMS? - VALCAPUMAWMS"** e **"Movimentação por unitizador (UMA)? - WMSMOVUNIUMA"**.

Assim, no campo **"Qual a estratégia UMA?"** são disponibilizadas as seguintes opções:

- **Norma de Paletização:**

          ![Imagem 24: Norma de Paletização:](https://ajuda.sankhya.com.br/hc/article_attachments/13666297931287) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 26: Norma de Paletização:](https://ajuda.sankhya.com.br/hc/article_attachments/13666337710615)

Acionando essa opção, a validação será realizada pela norma de paletização cadastrada para o Produto na seção Norma de Paletização (Lastro x Camada) da aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abawms). Desse modo, ao registrar o Produto, a **"Paletização"** será exibida no canto superior direito da tela e o total da soma dos produtos da UMA será apresentado no campo **"Total conferido"**. Sendo que, para os demais produtos, o sistema buscará o lastro e as camadas da Empresa x Produto ou do Produto. Sendo a empresa prioritária.  

Caso seja inserida uma quantidade superior ao limitado na norma, a seguinte mensagem será exibida:

**"A última contagem será desconsiderada. O total máximo suportado é de XXXXX UN, e o total conferido é de XXXX UN. Conferência deve ser refeita realocando a quantidade excedente em outra U.M.A."**

Se no Produto, o Lastro ou a Camada não estiver configurada, mas possuir (M³ e Peso>0), uma mensagem será exibida pedindo que o produto em questão seja alocado para uma UMA com estratégia do tipo Capacidade m³/Kg.

Já, se no Produto nenhum desses itens estiverem configurados, será apresentada uma mensagem solicitando que o referido produto seja alocado para uma UMA com estratégia do tipo Sem controle.

Não será permitido misturar produtos diferentes na mesma UMA. Caso tente conferir um Produto diferente, será mostrada a seguinte mensagem:

**"A conferência deste item não pode ser registrada, porque já existe outro item em andamento na conferência com norma/palete. Este item deve ser alocado em uma nova UMA."**

- **Capacidade M²/Kg:**

          ![Imagem 27: Capacidade M²/Kg:](https://ajuda.sankhya.com.br/hc/article_attachments/13666658332183) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 29: Capacidade M²/Kg:](https://ajuda.sankhya.com.br/hc/article_attachments/13666351591319)

Essa opção só poderá ser usada quando possuir algum Produto no Recebimento que tenha os dados de medidas configurados, sendo assim, ao acioná-la será exibida a tela para seleção dos **"Dados do produto"**. 

No campo **"Selecione o tipo de U.M.A."** deverá ser indicado o unitizador que irá alocar os produtos. Lembrando que, esse unitizador deve estar ativo no [Cadastro de Tipos de Unitizador](https://ajuda.sankhya.com.br/hc/pt-br/articles/13660826815383). 

A **"Capacidade"** da UMA será mostrada no canto superior direito dessa tela. Sabendo que uma UMA pode ter vários produtos, o sistema irá somar o peso de todos eles para comparar com o peso do unitizador e exibirá esse resultado no campo **"Total conferido"**.

Caso o peso alocado exceda o peso cadastrado no Unitizador, a seguinte mensagem será apresentada: 

**"A contagem de XXX UN será desconsiderada. O peso máximo suportado é de XXX Kg, e o peso proposto total na U.M.A é de XXX Kg. Produto deve ser alocado a quantidade excedente em outra U.M.A."**

Nesse contexto, ao registrar o Produto durante a conferência, podem ocorrer duas situações, observe:

1 - Se no cadastro do Produto não possuir dados de medidas (Peso ou M³) preenchidos e nem norma de paletização, o sistema exibirá a mensagem abaixo:

**"A conferência deste item não pode ser registrada, porque não existe configuração de volumetria ou peso para o produto informado. Este item deve ser alocado em uma UMA com estratégia do tipo ‘Sem Controle'"**

2 - Caso no cadastro do Produto não tenha dados de medidas (Peso ou M³) cadastrados, mas tenha norma de paletização, a seguinte mensagem será apresentada:

**"A conferência deste item não pode ser registrada, porque não existe configuração de volumetria ou peso para o produto informado. Este item deve ser alocado em uma UMA com estratégia do tipo ‘Norma de Paletização'"**

A cada vez que uma UMA for fechada, o sistema retornará para a tela de escolha da estratégia.

- **Sem Controle:**

   ![Imagem 30: Sem Controle:](https://ajuda.sankhya.com.br/hc/article_attachments/13666934394647) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 32: Sem Controle:](https://ajuda.sankhya.com.br/hc/article_attachments/9859187840279)

Escolhendo essa opção, a validação não ocorrerá porque não será possível ser contabilizada, já que os Produtos não possuirão norma de paletização e/ou não terão dados de medidas (Peso ou M³) cadastrados.

Todavia, se o Produto estiver com uma dessas configurações realizadas, então, ao ser informado nessa estratégia, a mensagem abaixo será apresentada:

**"Este produto não pode ser utilizado na estratégia ‘Sem controle’ porque possui configurações para norma palete ou volumetria."**   

Neste momento, o sistema irá validar se a UMA está vazia:

- Se estiver, os campos **"Produto"** e **"Quantidade"** serão habilitados para preenchimento e poderá avançar com a conferência. Se o produto for controlado por **"Lote"** e/ou **"Data de Validade"** ou **"Data de Fabricação"**, estes campos também serão apresentados para preenchimento.
- Caso não esteja vazia, o coletor exibirá uma mensagem solicitando que seja informada outra UMA, pois essa já está sendo utilizada atualmente.

**Observação:** se o conferente estiver com alguma UMA aberta e decidir **"Voltar"** para a tela anterior, os produtos conferidos nesta UMA serão desconsiderados.

Preenchidos todos os campos, acione o botão **"Confirmar"** para que possa realizar a conferência física. Ao bipar os produtos, o sistema realizará as seguintes validações: 

- Se o produto possui cadastro no sistema. Se não, será exibida a mensagem:

**“Não há produto cadastrado para este código de barras ‘9999999999999’.”**

- Se o mesmo consta na nota em conferência. Caso não conste, será apresentada a mensagem:

**“Produto 99 não informado na nota.”**

- Se o Lote corresponde ao esperado;
- Se a Data de Validade e/ou Fabricação está de acordo com os limites cadastrados de Shelf Life.

Após essas validações, o coletor ainda irá validar as quantidades dos produtos, confrontando com as quantidades negociadas na Nota de Compra. Dessa forma, se a quantidade inserida na UMA em conferência mais a quantidade já conferida em outras UMAs for:

- Menor ou igual à quantidade da nota fiscal, será exibida uma mensagem informando que o Produto foi conferido com sucesso;
- Maior que a quantidade da nota fiscal, o sistema irá validar o status do parâmetro **"Permitir contar a maior no Registro de Conferência -PERMCONTREGCON".**
- Se estiver ligado, será apresentada uma mensagem informando que o Produto foi conferido com sucesso;
- Se estiver desligado, um alerta será exibido com a seguinte mensagem:

**“A quantidade do produto excedeu a quantidade negociada. Continuar com a divergência? Sim/Não.”**

- Se clicar em **"Sim"**, o sistema acatará como conferida a quantidade informada, mesmo que esteja maior que o previsto;
- Ao clicar em **"Não"**, a conferência do produto deverá ser realizada novamente.

![Imagem 33: Caso queira desistir da conferência depois de ter informado a UMAS, acione o botão "Cancelar'' , que apresentará uma…](https://ajuda.sankhya.com.br/hc/article_attachments/16922211333271) Caso queira desistir da conferência depois de ter informado a UMAS, acione o botão **"Cancelar''**, que apresentará uma mensagem solicitando a confirmação da ação: 

**“Deseja mesmo cancelar a conferência da UMA ‘XXX’? Sim/Não”**.

- Clicando em **"Sim"**, a conferência dos produtos em andamento da UMA em aberto será desconsiderada e o coletor exibirá a mensagem **“Conferência da UMA XXX cancelada com sucesso”**;

Esta UMA em questão poderá ser utilizada em outro momento, visto que, não foi registrado nenhum produto nela.

- Ao clicar em **"Não"**, permanecerá na tela de Conferência.

O sistema irá cancelar a conferência apenas da UMA em aberto. Ou seja, as UMAs fechadas não serão canceladas via coletor. Isso só será possível através da tela Recebimento de Mercadorias, botão [Outras Opções…](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#bot%C3%A3ooutrasop%C3%A7%C3%B5es...), opção **"Cancelar Recebimento"**.

Já em caso de cancelamento do Recebimento, todas as UMAs utilizadas poderão ser reaproveitadas em outro processo, visto que, estarão vazias.

Você poderá atribuir à UMA quantos produtos desejar. Quando quiser fechá-la, clique no respectivo botão. Assim, o sistema irá se comportar da seguinte maneira:

- Exibirá uma mensagem avisando que a UMA foi registrada com sucesso;
- Habilitará o campo UMA novamente, para que o conferente informe a nova UMA a ser criada;
- Habilitará também o botão **"Finalizar"**, caso a conferência dos produtos tenha sido concluída.

Após a conclusão da conferência de todos os produtos dentro das UMAs, clique no botão Finalizar e será exibida uma tela com o resumo do Recebimento realizado:

![Imagem 34: Após a conclusão da conferência de todos os produtos dentro das UMAs, clique no botão Finalizar e será exibida uma tela…](https://ajuda.sankhya.com.br/hc/article_attachments/9859223792791) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 36: Após a conclusão da conferência de todos os produtos dentro das UMAs, clique no botão Finalizar e será exibida uma tela…](https://ajuda.sankhya.com.br/hc/article_attachments/9859224845463)

- Se a quantidade de itens conferidos for igual à quantidade de itens previstos, a mensagem a ser exibida será:

**“Registro de Conferência apto para ser finalizado.”**

- Caso a quantidade de itens conferidos for menor que a quantidade de itens previstos, então o coletor apresentará a mensagem:

**“Este recebimento possui X item(ns) pendente(s) de conferência. Ao acionar o botão ‘Finalizar Conferência’, este(s) produto(s) será(ão) tratado(s) com divergência de falta.”**

Quando a conferência estiver apta para ser finalizada, pressione o botão **“Finalizar conferência”**; dessa forma, as UMAs serão enviadas para validação do sistema e a tela de conclusão será exibida confirmando o sucesso da conferência.

**Importante:** a formação da UMA é livre, ou seja, não está condicionada à paletização dos produtos nem à quantidade do produto presente na nota em conferência.

---

#### Registrar Avaria

Durante a conferência, caso existam produtos avariados, não será possível registrá-los na UMA que contenha produtos não avariados. Assim, para registrar estes produtos, clique no botão **"Registrar Avaria"**. 

![Imagem 37: Durante a conferência, caso existam produtos avariados, não será possível registrá-los na UMA que contenha produtos não…](https://ajuda.sankhya.com.br/hc/article_attachments/9859292033175) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 39: Durante a conferência, caso existam produtos avariados, não será possível registrá-los na UMA que contenha produtos não…](https://ajuda.sankhya.com.br/hc/article_attachments/9859293819287) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 41: Durante a conferência, caso existam produtos avariados, não será possível registrá-los na UMA que contenha produtos não…](https://ajuda.sankhya.com.br/hc/article_attachments/9859295599895)

No campo **"UMA avariada"** você deve inserir uma UMA válida, onde colocará os produtos avariados e **"Confirmar"**. Em seguida, os campos **"Produto"** e **"Quantidade"** serão habilitados para preenchimento. Caso os produtos sejam controlados por Lote, Data de Validade e/ou Data de Fabricação, estes campos também serão exibidos.

**Observação:** as mesmas validações utilizadas pelo sistema nas UMAs não avariadas serão aplicadas aqui.

Após concluir a contagem de avarias e clicar em **"Fechar UMA com avaria"**, o sistema solicitará a confirmação desta ação por meio da mensagem: 

**“Deseja realmente fechar a UMA Avaria?’ Sim/Não’.”**

- Se **"Sim"**, retornará para a tela de Conferência;
- Se **"Não"**, permanecerá na tela de Registro de avaria.

Ao retornar para a tela de Conferência, o conferente encontrará o processo exatamente no ponto onde estava quando clicou em Registrar Avaria. Ou seja:

- Se havia uma UMA em aberto, esta continua em aberto ainda;
- Se não havia nenhuma UMA em aberto, a conferência poderá ser finalizada ou poderá informar uma nova UMA e seguir com o processo de conferência.

**Importante:** as UMAs criadas dentro do fluxo do botão Registrar Avaria deverão atualizar a quantidade avariada dos produtos conforme for registrado na UMA.

---

#### Análise de divergências

Realizada a conferência, acesse a tela [Recebimento de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias) para que o recebimento seja processado e as possíveis divergências sejam tratadas. 

Após a busca da conferência, o processamento é feito através do botão [Outras Opções…](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#bot%C3%A3ooutrasop%C3%A7%C3%B5es...), opção **"Processar Recebimento"**, dessa forma, se houver alguma divergência, como falta, sobra ou avaria, o pop-up [Divergências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613034-Recebimento-de-Mercadorias#divergncia) será exibido para correção da mesma.

![Imagem 42: Após a busca da conferência, o processamento é feito através do botão Outras Opções… , opção " Processar Recebimento" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/9851372220951)

Em relação às faltas, se existir algum produto na nota que não tenha sido conferido, ou seja, havendo falta total de algum produto, não será possível gerar recontagem para o mesmo. Contudo, a recontagem poderá ser gerada normalmente em caso de falta parcial ou sobra.

A quantidade avariada apresentada no pop-up deve ser considerada de acordo com o que foi informado na UMA com avaria.

---

#### Recontagem de conferência de entrada

Para recontar os produtos atribuídos à uma UMA a fim de corrigir ou validar a quantidade contada durante a conferência de entrada, acesse a opção **"Recontagem"**, em seguida, **"Registro de Conferência"** e informe o endereço da Doca. O coletor irá mostrar os detalhes da recontagem que precisa ser realizada.

![Imagem 43: Para recontar os produtos atribuídos à uma UMA a fim de corrigir ou validar a quantidade contada durante a conferência…](https://ajuda.sankhya.com.br/hc/article_attachments/9859401057431) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 45: Para recontar os produtos atribuídos à uma UMA a fim de corrigir ou validar a quantidade contada durante a conferência…](https://ajuda.sankhya.com.br/hc/article_attachments/9859402310167) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535) ![Imagem 47: Para recontar os produtos atribuídos à uma UMA a fim de corrigir ou validar a quantidade contada durante a conferência…](https://ajuda.sankhya.com.br/hc/article_attachments/9859396730903)

**Nota:** o campo **"Qtd. itens recontados"** será exibido apenas se houver dois ou mais produtos a serem recontados na mesma UMA. 

Em seguida, preencha a UMA, o Produto e a Quantidade de itens que serão recontados e clique no botão **"Confirmar"**, neste momento será apresentada uma mensagem informando que o referido produto foi recontado com sucesso.

Se houver outro produto a ser recontado dentro da mesma UMA, o card será atualizado com os detalhes da próxima Recontagem. Caso contrário, será exibida a tela de conclusão de recontagem. Lembrando que, não será obrigatória a geração de tarefas de Recontagem de todos os produtos contidos em uma UMA, portanto, poderá recontar quantos produtos desejar. 

Clicando em **"Próxima tarefa"**, o coletor buscará a próxima tarefa de Recontagem. Se não houver, será apresentada a mensagem abaixo:

**“Não há tarefas em aberto/ adequadas para o usuário/ equipamento.”**

**Observação:** é possível cancelar a Recontagem a qualquer momento. Ao clicar no botão **"Cancelar"**, os dados recontados da UMA cuja tarefa está em execução serão perdidos e a tarefa permanecerá pendente. Além disso, durante a recontagem, também é possível Registrar Avaria através do respectivo botão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Armazenagem

Quando a UMA é fechada no Registro de Conferência, a tarefa de Armazenagem dessa UMA poderá ser gerada, com exceção das UMAs criadas no fluxo de Registro de avarias. 

**Nota:** só é possível gerar tarefas das UMAs criadas através do fluxo Registro de Avaria caso a tratativa da divergência seja **"Aceitar Avaria"**.

---

#### Geração das Tarefas de Armazenamento

Após clicar em Fechar UMA, se o parâmetro **"Registro de conferência c/ armazenagem automática - REGCONFARMAUTO"** estiver ligado, o sistema irá gerar as tarefas de Armazenagem de forma automática para os produtos registrados na UMA, atualizando a situação do Recebimento para **"Enviado para Armazenagem".** Porém, se o parâmetro estiver desligado, o responsável pela geração das tarefas de Armazenagem deve realizá-la na tela [Tarefas de Recebimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613334-Tarefas-de-Recebimento).

Concluída a geração das tarefas, o sistema bloqueia os endereços de Destino; assim, se houver divergências, elas serão tratadas sem correr o risco do produto ser movimentado. Esse processo pode ser alterado através da marcação **"Inibe bloqueio do endereço no registro de conferência"** localizada na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) das Preferências da Empresa.

Por fim, após todas as tarefas de Armazenagem serem realizadas, processe o recebimento e libere a Doca para que os endereços que foram bloqueados durante o processo de Armazenagem sejam desbloqueados.

É importante ressaltar que todas as movimentações relacionadas à Armazenagem e retorno de Expedição serão permitidas, conforme abaixo:

![Imagem 48: É importante ressaltar que todas as movimentações relacionadas à Armazenagem e retorno de Expedição serão permitidas,…](https://ajuda.sankhya.com.br/hc/article_attachments/9851975336599)

---

#### Função Armazenagem

Por meio do coletor, além de receber as tarefas de Armazenagem de Produtos, você poderá receber também as tarefas de armazenamento de UMAs a partir da função **"Armazenagem"**.

![Imagem 49: Por meio do coletor, além de receber as tarefas de Armazenagem de Produtos , você poderá receber também as tarefas de…](https://ajuda.sankhya.com.br/hc/article_attachments/9859471605911)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 51: Por meio do coletor, além de receber as tarefas de Armazenagem de Produtos , você poderá receber também as tarefas de…](https://ajuda.sankhya.com.br/hc/article_attachments/9859472866583)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 53: Por meio do coletor, além de receber as tarefas de Armazenagem de Produtos , você poderá receber também as tarefas de…](https://ajuda.sankhya.com.br/hc/article_attachments/9859473796119)

Na execução das tarefas de Armazenagem da UMA, não será necessário informar o código dos produtos contidos na mesma, sendo assim, você deverá fazer apenas a leitura da UMA.

Depois de acionar o botão Armazenagem, a tela do coletor  irá mostrar a Doca de Origem e a UMA que será armazenada para que você possa confirmá-la lendo o seu código no campo disponível.

Em seguida, o endereço de Destino desta UMA será indicado e você deverá confirmar a entrega bipando o código do referido endereço.

Após confirmação da entrega da UMA no destino, o sistema atualizará todo o estoque pertinente à movimentação.

---

#### Função Armazenagem Expressa

Ao optar pela **"Armazenagem Expressa"** e tendo o parâmetro **"Permite definir endereço armazenamento expresso? - WMSDEFENDARMEXP"** ativado, você terá autonomia para definir o endereço de Destino da UMA de acordo com as seguintes condições:

- Se o endereço de Origem utilizar UMA, após informar a Doca, indique a UMA que deseja coletar e acione o botão **"Coletar UMA"**. Nesta primeira etapa, você poderá coletar quantas UMAs desejar.
- Porém, se o endereço de Origem não utilizar UMA, então nesta primeira etapa você deverá seguir conforme já existe no coletor.
- Na segunda etapa, independente do endereço de Destino utilizar ou não uma UMA, você deverá confirmar a entrega dela no endereço de Destino, não sendo necessário informar o(s) produto(s).

**Observação:** caso o Destino não utilize UMA, ao confirmar a entrega o sistema irá "explodir" no endereço os produtos contidos na UMA movimentada.

- Em caso de movimentação de Produto e o endereço de Destino utilizar UMA, na segunda etapa, confirme a entrega dele no referido endereço de Destino e informe a UMA que conterá este produto.

![Imagem 54: Quando a Doca informada utilizar UMA:](https://ajuda.sankhya.com.br/hc/article_attachments/16922211333271) Quando a Doca informada utilizar UMA:

- O botão **"Disponíveis"** exibirá a lista de cards com as UMAs disponíveis e seus respectivos endereços de Destino.
- O botão **"Coletados"** irá apresentar a lista de cards com as UMAs já coletadas e seus respectivos endereços de Destino.

Após a entrega da UMA ou do Produto no Destino, clique no botão **"Salvar Armazenagem"**, a mensagem de confirmação da Armazenagem será apresentada logo em seguida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Reabastecimento

Com o objetivo de otimizar o fluxo de movimentações do armazém, você pode fazer o Reabastecimento de todos os produtos contidos em uma UMA com uma única movimentação.

         ![Imagem 55: Com o objetivo de otimizar o fluxo de movimentações do armazém, você pode fazer o Reabastecimento de todos os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/9852595246359) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 57: Com o objetivo de otimizar o fluxo de movimentações do armazém, você pode fazer o Reabastecimento de todos os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/9852640581271) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 59: Com o objetivo de otimizar o fluxo de movimentações do armazém, você pode fazer o Reabastecimento de todos os produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/9852631224087)

**Notas:**

- As tarefas de Reabastecimento devem ser geradas de acordo com as regras já existentes.
- O endereço de Origem do Reabastecimento pode ou não utilizar UMA.
- Para reabastecer pickings (endereço de destino) que utilizam UMAs, deve haver pelo menos uma UMA vinculada ao endereço de picking após o Reabastecimento ser concluído. Do contrário, a UMA perderá a validade no momento em que o Reabastecimento for confirmado.
- Se tanto o endereço de Origem quanto o endereço de Destino não utilizarem UMA, o Reabastecimento deve ser feito conforme fluxo já existente.

No coletor, é possível realizar o reabastecimento integral das UMAs, bem como, o reabastecimento parcial:

- #### Reabastecimento integral de UMAs

Nas tarefas de Reabastecimento integral, ou seja, onde a quantidade total de todos os produtos da UMA de um endereço é reabastecida, serão consideradas as seguintes regras:

![Imagem 60: Quando o endereço de Origem utilizar uma UMA e o endereço de Destino utilizar ou não uma UMA:](https://ajuda.sankhya.com.br/hc/article_attachments/16922455553815) Quando o endereço de Origem utilizar uma UMA e o endereço de Destino utilizar ou não uma UMA:

- Na primeira etapa, o coletor irá trazer o endereço de Origem e a UMA a ser coletada. Neste momento, você deverá confirmá-la lendo o seu código no campo disponível.
- Em seguida, o endereço de Destino desta UMA será indicado, confirme a entrega bipando o código do referido endereço.

**Observação:** caso o endereço de Destino não utilize UMA, ao confirmar a entrega o sistema irá "explodir" nele os produtos contidos na UMA movimentada.

![Imagem 61: Se o endereço de Origem não utiliza UMA, mas o endereço de Destino utilizar:](https://ajuda.sankhya.com.br/hc/article_attachments/16922455562775) Se o endereço de Origem não utiliza UMA, mas o endereço de Destino utilizar:

- Na primeira etapa, o coletor exibirá o endereço de Origem e o Produto a ser reabastecido. Assim, você deverá confirmar estes dados (como já acontece atualmente).
- Logo após, o coletor irá indicar o endereço de Destino. Na sequência, preencha os campos Endereço e UMA e confirme o endereço de entrega, bem como, da UMA onde irá inserir o Produto. Essa UMA pode ser alguma já existente no endereço ou uma vazia. O botão **"Confirmar"** será habilitado somente depois que os dados forem preenchidos.

![Imagem 62: Quando o endereço de Destino do reabastecimento for um picking que utiliza UMA e já houver outra UMA neste endereço, o…](https://ajuda.sankhya.com.br/hc/article_attachments/16922455569303) Quando o endereço de Destino do reabastecimento for um picking que utiliza UMA e  já houver outra UMA neste endereço, o mesmo se manterá ativo e passará a possuir duas UMAs. Se não houver nenhuma UMA no endereço de Destino, a UMA reabastecida será a única disponível no endereço neste momento.

Confirmada a entrega da UMA no Destino, o sistema atualizará os estoques pertinentes à movimentação.

- #### Reabastecimento parcial de UMAs

No Reabastecimento parcial faz-se o reabastecimento parcial de produtos contidos em uma UMA com uma única movimentação. Nessa tarefa serão consideradas as seguintes regras:

![Imagem 63: Quando o endereço de Origem e o endereço de Destino utilizarem UMA:](https://ajuda.sankhya.com.br/hc/article_attachments/16922455553815) Quando o endereço de Origem e o endereço de Destino utilizarem UMA:

- Na primeira etapa, o coletor irá trazer o endereço de Origem e o número da UMA que contém os produtos que irá reabastecer, assim como, o Produto e a Quantidade que você deverá pegar. Confirme a UMA, lendo o seu código no campo disponível e também o código do Produto indicado.

**Nota:** se houver mais de um Produto a ser coletado dentro da mesma UMA, não será necessário confirmá-la novamente, basta confirmar apenas o produto.

- Em seguida, o endereço de Destino será indicado. Preencha os campos Endereço e UMA e confirme o endereço de entrega, bem como, a UMA onde irá inserir os produtos. Essa UMA pode ser alguma já existente no endereço ou uma vazia. O botão Confirmar será habilitado somente depois que os dados forem preenchidos.

![Imagem 64: Em casos em que o endereço de Origem utiliza UMA, mas o endereço de Destino não utiliza:](https://ajuda.sankhya.com.br/hc/article_attachments/16922455562775) Em casos em que o endereço de Origem utiliza UMA, mas o endereço de Destino não utiliza:

- A primeira etapa funciona da mesma maneira que a citada na regra anterior.
- Na segunda etapa, o coletor irá mostrar o endereço de Destino e apenas o campo Endereço para que a entrega seja confirmada no endereço indicado.

![Imagem 65: Se o endereço de Origem não utiliza UMA, porém o endereço de Destino utiliza:](https://ajuda.sankhya.com.br/hc/article_attachments/16922455569303) Se o endereço de Origem não utiliza UMA, porém o endereço de Destino utiliza:

- Na primeira etapa, o coletor exibirá o endereço de Origem e o Produto a ser reabastecido. Assim, você deverá confirmar estes dados (como já acontece atualmente).
- Logo após, o coletor irá indicar o endereço de Destino. Na sequência, preencha os campos Endereço e UMA e confirme o endereço de entrega, bem como, da UMA onde irá inserir o Produto.

Após a confirmação da entrega da UMA no Destino, o sistema atualizará os estoques pertinentes à movimentação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Registro de Ocorrência

Ao identificar uma ocorrência no estoque, é importante informar a UMA para que a tarefa de Transferência seja gerada corretamente.

Para isso, primeiramente acione a opção **"Ocorrência"** no coletor. Em seguida, informe o **"Endereço"**, o **"Tipo"**, o **"Produto"** e a **"Quantidade"**.

O campo **"UMA"** só será obrigatório se o endereço informado previamente utilizar UMA. Caso contrário, ficará desabilitado para preenchimento.

Preencha os campos **"Lote"**, **"Data de Validade"** ou **"Data de Fabricação"** apenas se os produtos forem controlados por um deles.

![Imagem 66: Preencha os campos " Lote" , " Data de Validade" ou " Data de Fabricação" apenas se os produtos forem controlados por…](https://ajuda.sankhya.com.br/hc/article_attachments/9853224383767) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 68: Preencha os campos " Lote" , " Data de Validade" ou " Data de Fabricação" apenas se os produtos forem controlados por…](https://ajuda.sankhya.com.br/hc/article_attachments/9853276828567) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 70: Preencha os campos " Lote" , " Data de Validade" ou " Data de Fabricação" apenas se os produtos forem controlados por…](https://ajuda.sankhya.com.br/hc/article_attachments/9853235001367)

Depois de **"Enviar"** o registro da ocorrência, a tarefa de Transferência será gerada levando em consideração a UMA informada. Essa tarefa será executada pela funcionalidade Transferência do coletor.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Transferência

A tarefa de Transferência tem o objetivo de alocar melhor os produtos dentro do armazém. 

#### Transferência de UMAs (Sankhya Om)

Na tela [Transferência entre Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107213-Transfer%C3%AAncia-entre-Endere%C3%A7os) você irá gerar a tarefa de Transferência, primeiramente, filtrando a **"UMA"** que deseja transferir por meio do Painel de Filtros. 

![Imagem 71: Na tela Transferência entre Endereços você irá gerar a tarefa de Transferência , primeiramente, filtrando a " UMA" que…](https://ajuda.sankhya.com.br/hc/article_attachments/9853383053463)

Esta tela mostrará somente os produtos que possuem saldo no Endereço e na UMA com suas quantidades atuais. Lembrando que, os produtos que não pertencerem a uma UMA serão exibidos normalmente.

A coluna **"UMA"** estará preenchida se o endereço consultado estiver com a configuração ativa na aba [Unitizador (UMA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento#AbaUnitizador(UMA)) do [Endereço de Armazenamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento).

Aqui, só será possível transferir a UMA integralmente, ou seja, todos os produtos contidos na UMA serão transferidos juntos em uma única movimentação. Caso queira realizar a transferência de uma ou mais UMAs, selecione pelo menos uma linha de cada UMA.

Depois de selecionar a linha da UMA que deseja transferir, informe o **"Endereço de Destino"** no respectivo campo da linha selecionada e acione o botão **"Gerar Transferências"**.

Logo após, o sistema exibirá uma mensagem informativa, exibindo o número da UMA transferida e a quantidade de produtos envolvidos nessa operação.

![Imagem 72: Logo após, o sistema exibirá uma mensagem informativa, exibindo o número da UMA transferida e a quantidade de produtos…](https://ajuda.sankhya.com.br/hc/article_attachments/9853524669335)

**Observações:**

- Ao selecionar simultaneamente a linha de um Endereço ou Produto que possua uma UMA vinculada e outra linha que não possua, o sistema emitirá uma mensagem informando que não é possível concluir a geração das tarefas simultaneamente.
- Caso você clique em Gerar Transferências antes de informar o Endereço de Destino, será apresentada uma mensagem de alerta orientando que o campo Endereço de Destino precisa ser preenchido. Além disso, se ao clicar no botão Gerar Transferências, as configurações feitas no Endereço de Destino não permitirem que a operação seja realizada, será emitido um aviso informando sobre a possível causa.

---

#### Transferência de UMAs (Coletor)

A tarefa de Transferência gerada na tela [Transferência entre Endereços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107213-Transfer%C3%AAncia-entre-Endere%C3%A7os) será executada considerando as regras abaixo:

![Imagem 73: Quando a tarefa de Transferência possuir como Endereço de Destino um endereço especial, a quantidade da tarefa não será…](https://ajuda.sankhya.com.br/hc/article_attachments/16922455553815) Quando a tarefa de Transferência possuir como Endereço de Destino um endereço especial, a quantidade da tarefa não será necessariamente a quantidade integral da UMA ou do Produto. Se a quantidade for parcial, o sistema deverá indicar a UMA e o Produto a ser coletado no endereço de Origem, em seguida deve indicar o endereço de Destino, que pode ou não utilizar UMA. 

- Se utilizar, basta confirmar o endereço e informar a UMA destino (que pode ser alguma já existente no endereço ou uma outra que esteja vazia).
- Caso não utilize, será solicitado  somente o endereço de Destino.

![Imagem 74: Se o endereço de Origem utilizar UMA e o endereço de Destino utilizar ou não utilizar UMA:](https://ajuda.sankhya.com.br/hc/article_attachments/16922455562775) Se o endereço de Origem utilizar UMA e o endereço de Destino utilizar ou não utilizar UMA:

- Na primeira etapa, o coletor irá mostrar o endereço de Origem e a UMA a ser transferida para que você possa confirmar a UMA, lendo o seu código no campo disponível.
- Na etapa seguinte, o endereço de Destino da UMA será sugerido e você deverá confirmar a entrega bipando o código do endereço indicado.

**Observação:** caso o endereço de Destino não utilize UMA, ao confirmar a entrega o sistema irá "explodir" nele os produtos contidos na UMA movimentada.

![Imagem 75: Se tanto o endereço de Origem , quanto o endereço de Destino não utilizarem UMA, a Transferência deverá ser feita…](https://ajuda.sankhya.com.br/hc/article_attachments/16922455569303) Se tanto o endereço de Origem, quanto o endereço de Destino não utilizarem UMA, a Transferência deverá ser feita conforme fluxo já existente.

![Imagem 76: Se o endereço de Origem não utiliza UMA, porém o endereço de Destino utiliza:](https://ajuda.sankhya.com.br/hc/article_attachments/16922488966807) Se o endereço de Origem não utiliza UMA, porém o endereço de Destino utiliza:

- Na primeira etapa, o coletor exibirá o endereço de Origem, o Produto e a Quantidade a ser transferida. Assim, você deverá confirmar estes dados (como já acontece atualmente).
- Logo após, o coletor irá indicar o endereço de Destino. Na sequência, preencha os campos Endereço e UMA e confirme o endereço de entrega, bem como, da UMA onde irá inserir o Produto.

Após a confirmação da entrega da UMA no Destino, o sistema atualizará os estoques pertinentes à movimentação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Movimentação Pró-Ativa

As UMAs podem ser movimentadas dentro do armazém de uma forma mais ágil e autônoma. Para isso, acesse a opção **"Movimentação Pró-Ativa"** do coletor. Em seguida, o campo **"UMA ou Endereço"** se comportará da seguinte maneira:

- Ao inserir um Endereço, o coletor irá seguir o fluxo normal da funcionalidade para que os demais campos sejam preenchidos e os produtos coletados.
- Caso o **"Endereço"** informado não seja controlado por UMA, o campo **"UMA"** será ocultado da tela do coletor **"Total Cross"**.
- Informando uma UMA, os demais campos da tela ficarão bloqueados para edição, dessa forma, basta acionar o botão **"Continuar"** para seguir o fluxo da coleta.

Na sequência, você deverá conferir as informações da movimentação desejada, indicar o Endereço de Destino e **"Concluir"** a operação. 

![Imagem 77: Na sequência, você deverá conferir as informações da movimentação desejada, indicar o Endereço de Destino e " Concluir"…](https://ajuda.sankhya.com.br/hc/article_attachments/9854144367255) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 79: Na sequência, você deverá conferir as informações da movimentação desejada, indicar o Endereço de Destino e " Concluir"…](https://ajuda.sankhya.com.br/hc/article_attachments/9854146157335) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 81: Na sequência, você deverá conferir as informações da movimentação desejada, indicar o Endereço de Destino e " Concluir"…](https://ajuda.sankhya.com.br/hc/article_attachments/9854138733207)

Você pode acompanhar as UMAs e produtos já coletados através do botão **"Movimentações em andamento"** e, caso desejar desistir da operação, é só clicar em **"Limpar campos"**.

Considere ainda que, o Destino da UMA ou Produtos coletados podem ser controlados por UMA ou não. 

- Se sim, o sistema irá validar se o Endereço já atingiu a quantidade máxima de UMAs permitidas.

- Se o Endereço ainda não estiver com a quantidade máxima atingida, o coletor exibirá a mensagem **“UMA armazenada com sucesso.”**.
- Porém, se a armazenagem dessa UMA superar a quantidade máxima permitida no Endereço, a operação não poderá ser concluída e o coletor apresentará a seguinte mensagem:

**“A quantidade máxima de UMAs deste endereço já foi atingida. Por gentileza, escolha outro destino.”**

- Se não, após informar o Endereço de destino, os produtos serão armazenados no Destino escolhido e a UMA perderá a validade.

Com o parâmetro **"Movimentação por unitizador (UMA)? - WMSMOVUNIUMA"** ligado, o coletor irá solicitar a doca no recebimento que possui uma recontagem pendente. Assim, informe a UMA em seu referido campo para realizar a recontagem. Porém, com este desabilitado, o coletor será direcionado diretamente para a tela de **"Recontagem"** do **"Registro de Conferência"**.

---

![Imagem 82: Informações adicionais referente ao uso do parâmetro WMSMOVUNIUMA na Movimentação pró-ativa:](https://ajuda.sankhya.com.br/hc/article_attachments/18337956261399) **Informações adicionais referente ao uso do parâmetro WMSMOVUNIUMA na Movimentação pró-ativa:**

**(1)** Com o parâmetro WMSMOVUNIUMA habilitado, ao realizar movimentações com UMA's o sistema irá validar se o produto movimentado está em um endereço e/ou UMA para, então, realizar a movimentação. Então, se o produto não for reconhecido, o sistema exibirá a mensagem:

**"Não foi possível encontrar um produto com o código de barras informado xxxxxx"**

Além disso, caso o item não pertença à UMA, o sistema o informará por meio da mensagem:

**"Produto inexistente para a UMA informada"**

**(1)** No  coletor TotalCross, a cada produto movimentado, seja ele integral ou parcial, o coletor irá exibir uma mensagem o informando da efetivação da tarefa.

**(1)** A nomenclatura do campo **"Controle tipo lista"** da tela [Movimentação Pró-ativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295#Movimenta%C3%A7%C3%A3oPr%C3%B3Ativa) do Coletor TotalCross será definida conforme o inserido no campo **"Título"** do [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) (sub-aba [Controle adicional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#sub-abacontroleadicional), aba [Medidas e Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113#abamedidaseestoque)). Caso o campo Título esteja sem informação, o nome padrão Controle tipo lista será exibido no TotalCross.

**(1)** Além disso, quando um item com, ou sem controle adicional for coletado, será possível visualizar se o endereço de destino possui controle de UMA. Assim, em caso positivo, deve-se informar a UMA de destino de forma que a movimentação seja feita da origem sem UMA para um endereço controlado por UMA. Porém, se o endereço não possuir esse controle, o campo **"Quantidade"** do TotalCross será preenchido com um valor conforme à tarefa, mas este pode ser alterado desde que não seja o valor 0 ou negativo.

**(1)** Ao realizar uma movimentação entre UMA's, é importante se atentar aos seguintes critérios caso o endereço esteja vazio:

**(2)** O item não pode ser movimentado para uma UMA já armazenada utilizada em outro endereço;

- - Se utilizado o botão ![Imagem 83: Se utilizado o botão "Confirmar" , a UMA a ser movimentada poderá ser destinada ao seu novo endereço;](https://ajuda.sankhya.com.br/hc/article_attachments/18365552205463) **"Confirmar"**, a UMA a ser movimentada poderá ser destinada ao seu novo endereço;
  - A quantidade máxima de UMA's previstas no endereço deve ser respeitada;
  - Ao realizar essa movimentação, há algumas restrições, como, por exemplo, se o produto pertence a um grupo de produtos, se a sua área de armazenamento é pré-determinada, se o endereço está bloqueado, entre outros.

**(2)** Porém, se o endereço de destino estiver parcialmente ocupado, tem-se que:

- - Se utilizado o botão ![Imagem 84: Se utilizado o botão Confirmar sem informar a "UMA de destino" , então a mesma UMA de origem pode ser destinada ao novo…](https://ajuda.sankhya.com.br/hc/article_attachments/18365552205463) Confirmar sem informar a **"UMA de destino"**, então a mesma UMA de origem pode ser destinada ao novo endereço;
  - A quantidade máxima de UMA's previstas no endereço deve ser respeitada;
  - Ao realizar essa movimentação, há algumas restrições, como, por exemplo, se o produto pertence a um grupo de produtos, se a sua área de armazenamento é pré-determinada, se o endereço está bloqueado, entre outros.

**(1)** Dado que a tarefa da movimentação tenha origem na coleta de itens com UMA's parciais, o campo Quantidade será preenchido com o valor conforme a Movimentação Pró-ativa. Mas lembre-se que este não poderá ser 0 ou valores negativos.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Remanejamento de UMA

Ao selecionar a opção **"Remanejamento de UMA"**, você conseguirá retirar um ou mais itens de uma UMA (origem) e atribuí-los a uma nova UMA (destino).

Após clicar na opção citada acima, informe a **"UMA"** de Origem e avance para a próxima etapa, na qual os detalhes da UMA serão exibidos e informe qual o **"Produto"** e a **"Quantidade"** que deseja remanejar.

Se o Produto for controlado por **"Lote"** e/ou **"Data de Validade"**, estes campos também serão exibidos para preenchimento.

![Imagem 85: Se o Produto for controlado por " Lote" e/ou " Data de Validade" , estes campos também serão exibidos para…](https://ajuda.sankhya.com.br/hc/article_attachments/9854523112599) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 87: Se o Produto for controlado por " Lote" e/ou " Data de Validade" , estes campos também serão exibidos para…](https://ajuda.sankhya.com.br/hc/article_attachments/9854535697943) ![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 89: Se o Produto for controlado por " Lote" e/ou " Data de Validade" , estes campos também serão exibidos para…](https://ajuda.sankhya.com.br/hc/article_attachments/9854537420439)

Após coletar todos os produtos que deseja remanejar e clicar  em **"Finalizar"**, será exibido um pop-up confirmando a ação com a seguinte mensagem: 

**“Deseja mesmo finalizar? Sim/Não.”**

- Se Não, permanecerá na tela Produto.
- Ao clicar em Sim, você será direcionado para a etapa de Destino, onde terá que informar a **"UMA de Destino"**. Feito isso, poderá **"Confirmar"** a operação.

Caso queira remanejar apenas um produto, após informá-lo com a Quantidade desejada, clique diretamente em Finalizar, não sendo necessário clicar em **"Próximo item"**.

A UMA Destino ficará hospedada no mesmo endereço da UMA de Origem.  Se houver a necessidade de fazer alguma movimentação, utilize a função Movimentação Pró-Ativa.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Expedição - Picking

Este processo consiste em separar os produtos contidos em uma UMA que estejam em endereço de picking para atender aos pedidos dos clientes. 

Quando existem UMAs no picking, tanto a separação normal quanto a separação balcão podem ser realizadas. 

Para isso, acesse a opção **"Separação"** e, em seguida, escolha qual o tipo de separação deseja realizar dentre as opções **"Separação"** normal e **"Separação Balcão"**. Depois, informe a **"UMA"** e o **"Produto"** que deseja separar e finalize indicando o **"Endereço"** de Destino.

![Imagem 90: Para isso, acesse a opção " Separação" e, em seguida, escolha qual o tipo de separação deseja realizar dentre as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/9855361984407)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 92: Para isso, acesse a opção " Separação" e, em seguida, escolha qual o tipo de separação deseja realizar dentre as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/9855363892503)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 94: Para isso, acesse a opção " Separação" e, em seguida, escolha qual o tipo de separação deseja realizar dentre as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/9855415832215)

Além disso, neste mesmo processo ainda é possível realizar a separação fracionada dentro da UMA, ou seja, a tarefa não precisa ser gerada com a quantidade total dos produtos e nem de todos os produtos existentes nesta UMA.

Se o endereço de picking possuir mais de uma UMA, o sistema irá validar se os produtos do pedido que será separado possuem controle de **"Data de validade"**:

- Possuindo, a geração das tarefas seguirá conforme padrão já existente, priorizando a separação dos itens com vencimento mais próximo, independente se este produto está ou não na menor UMA do endereço;
- Se não, o sistema identifica qual é a UMA de menor número e a geração das tarefas irá priorizar a separação dessa UMA, até que todo saldo tenha sido consumido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)

### Inventário de endereços com UMA

Para a realização do Inventário, execute a [Geração das Tarefas de Contagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008928381-Gera%C3%A7%C3%A3o-de-Tarefas-de-Contagem) orientada ao Endereço ou ao Produto contido no endereço selecionado. Lembrando que, para dar início na geração de tarefas de contagem, primeiramente, você deve possuir um [Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500007989601-Como-realizar-o-processo-de-invent%C3%A1rio-no-WMS#invent%C3%A1rios1) cadastrado. 

- Contagem de estoque de endereços com UMA com a tarefa orientada ao Endereço

Quando a tarefa gerada for orientada ao Endereço e este utilizar UMA, ao acessar a opção **"Inventário"**, o coletor irá mostrar o Endereço que deverá ser contado inicialmente na **"Contagem de Estoque"**.

Em seguida, informe a **"UMA"** que será contada, bem como, o **"Produto"** e a **"Quantidade"**. Se o Produto for controlado por **"Lote"** e/ou **"Data de Validade"**, estes campos também serão exibidos para preenchimento.

![Imagem 95: Em seguida, informe a " UMA" que será contada, bem como, o " Produto" e a " Quantidade" . Se o Produto for controlado…](https://ajuda.sankhya.com.br/hc/article_attachments/9855768638103)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 97: Em seguida, informe a " UMA" que será contada, bem como, o " Produto" e a " Quantidade" . Se o Produto for controlado…](https://ajuda.sankhya.com.br/hc/article_attachments/9855771580055)![seta](https://ajuda.sankhya.com.br/hc/article_attachments/15619687360535)![Imagem 99: Em seguida, informe a " UMA" que será contada, bem como, o " Produto" e a " Quantidade" . Se o Produto for controlado…](https://ajuda.sankhya.com.br/hc/article_attachments/9855763291031)

Após **"Confirmar"** a contagem de todos os itens da UMA, acione o botão **"Finalizar contagem de UMA"**. Em seguida, envie a contagem feita para o Endereço indicado. Se houver tarefa de contagem para outro Endereço, o ciclo se reinicia até que todas as tarefas estejam concluídas. Em resumo, o fluxo operacional será conforme abaixo:

![Imagem 100: Após " Confirmar" a contagem de todos os itens da UMA, acione o botão " Finalizar contagem de UMA" . Em seguida, envie…](https://ajuda.sankhya.com.br/hc/article_attachments/9858700244119)

O sistema irá validar se as quantidades lógica e contada dos Produtos da UMA estão equiparadas. Se estiverem, não há necessidade de ajuste; do contrário, o estoque deverá ser ajustado nas UMAs conforme contagem, de modo que a quantidade contada e lógica sejam iguais após o ajuste feito.  Este processo, por consequência, irá validar o estoque dos endereços.

**Observações importantes:**

- Quando for inserido um Produto que logicamente não perten��a a UMA informada, o sistema irá inserir o item e a quantidade correspondente a UMA inventariada, fazendo em paralelo o [Ajuste no estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117633-Ajuste-de-Estoque-) (se necessário), conforme padrão.
- Caso não seja informado um Produto que logicamente pertença a UMA, o sistema registrará a saída do item e a quantidade da UMA inventariada, fazendo em paralelo o Ajuste no estoque (se necessário), conforme padrão nativo.
- Se no sistema o Endereço possuir uma ou mais UMAs armazenadas e nenhuma UMA for identificada fisicamente durante a contagem, no campo UMA deverá ser informada uma UMA vazia para realizar a contagem dos itens. Neste caso, a UMA inicial ficará vazia após o ajuste e a nova UMA pertencerá ao Endereço.
- Uma vez que  no Endereço do sistema não exista nenhuma UMA e por consequência não possua saldo de nenhum Produto, ou seja, está logicamente vazio, porém fisicamente existam produtos neste Endereço, uma UMA vazia deverá ser informada para realizar a contagem dos itens. Neste caso, a nova UMA só pertencerá ao Endereço após o ajuste de inventário ser realizado.

---

- Contagem de estoque de endereços com UMA com a tarefa orientada ao Produto

Ao acessar a opção Inventário com a tarefa gerada para o Produto e este utilizar UMA, o coletor irá mostrar o Endereço que deverá ser contado inicialmente e a descrição do produto na **"Contagem de Estoque"**.

Na sequência, preencha a **"UMA"**, o **"Produto"** e a **"Quantidade"** que será contada. Lembrando que, se o Produto for controlado por **"Lote"** e/ou **"Data de Validade"**, estes campos também serão exibidos para preenchimento.

Após concluir a contagem do item na UMA, clique no botão Finalizar contagem de UMA. Caso haja mais de um Lote e/ou Data de Validade do mesmo Produto dentro de uma mesma UMA, você deverá clicar primeiramente em Confirmar e repetir este ciclo até que tenha contado todos os Produtos da mesma UMA. Somente quando finalizar, clique em Finalizar contagem de UMA.

Em seguida, você poderá informar uma nova UMA que possua o Produto e seguir o fluxo de contagem ou enviar a contagem feita para o Endereço indicado. 

Se o Produto contado possuir saldo em outro Endereço, o ciclo se reinicia até que todas as tarefas estejam concluídas. Em resumo, o fluxo operacional será conforme abaixo:

![Imagem 101: Se o Produto contado possuir saldo em outro Endereço , o ciclo se reinicia até que todas as tarefas estejam concluídas.…](https://ajuda.sankhya.com.br/hc/article_attachments/9858601279511)

A validação desta contagem pelo sistema ocorrerá da mesma forma que foi citada na contagem de estoque de endereços com UMA orientada ao Endereço.

---

#### Ajuste de estoque por Inventário

O [Ajuste de Estoque por Inventário](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500009432561-Ajuste-de-Estoque-por-Invent%C3%A1rio) é realizado no Sankhya Om.

O ajuste deverá ser feito conforme padrão já existente, gerando transferência atômica dos saldos divergentes para os endereços especiais de sobra e falta, sendo que a classificação de Falta e Sobra será baseada no saldo da UMA.

![Imagem 102: O ajuste deverá ser feito conforme padrão já existente, gerando transferência atômica dos saldos divergentes para os…](https://ajuda.sankhya.com.br/hc/article_attachments/9856163934743)

Os Produtos e Quantidades serão atualizados nas UMAs após a conclusão do ajuste.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/9813125446295-Movimenta%C3%A7%C3%A3o-por-Unitizador-UMA#top)
