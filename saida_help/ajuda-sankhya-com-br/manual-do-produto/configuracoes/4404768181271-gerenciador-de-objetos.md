---
id: "4404768181271"
titulo: "Gerenciador de Objetos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:01:40Z"
rotulos: ["Produtos", "Configuração", "Segurança", "Oracle", "br.com.sankhya.gerenciadorDeObjetos", "Performance", "Gerenciador de Objetos no Sankhya Om: Otimização e Controle", "PL-SQL"]
---

# Gerenciador de Objetos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311107981847) Módulo: Configurações > Avançado       ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311107982743) Versão disponível: A partir da 4.9
```

---

![Imagem 3: O recurso de incluir regras pela tela Gerenciador de Objetos foi descontinuado por questões de segurança. Inicialmente…](https://ajuda.sankhya.com.br/hc/article_attachments/22034143154071) O recurso de incluir regras pela tela **Gerenciador de Objetos** foi descontinuado por questões de segurança. Inicialmente a tela continuará disponível para acompanhamento das regras já criadas.

O Gerenciador de Objetos é uma ferramenta desenvolvida em Oracle no Sankhya Om com o propósito de otimizar a criação, gerenciamento e manipulação dos objetos, utilizando as melhores práticas na construção, proporcionando ganho de performance e integridade.

Através do Gerenciador de Objetos, será possível realizar a criação de regras de negócio e identificação de regras personalizadas, possibilitando a celeridade na localização de adversidades, centralização das informações e avaliação da performance dos objetos pela telemetria.

Além disso, ressaltamos os seguintes benefícios:

- **Cloud Friendly:** O Gerenciador de Objetos é incorporado no Sankhya Om, tornando-se desnecessário uma ferramenta de banco de dados para realizar a criação/manutenção das regras de negócios.
- **Telemetria de objetos:** Neste dashboard será possível visualizar a quantidade de execuções, o tempo de processamento utilizado por cada objeto e um indicador apresentando quais objetos estão afetando a performance do sistema.
- **Rastreabilidade de alterações:** O usuário consegue mapear todas as alterações realizadas nos objetos para melhorar o diagnóstico de problemas, identificando as responsabilidades.
- **Facilidade na ativação desativação de regras:** Este recurso irá ajudar a ter mais simplicidade na hora de ativar ou desativar as regras de negócios personalizadas.

![Imagem 4: Por questões de compliance e segurança, a inclusão de regras foi descontinuada. Porém, caso necessário, direcione a…](https://ajuda.sankhya.com.br/hc/article_attachments/22034143154071) Por questões de compliance e segurança, a inclusão de regras foi descontinuada. Porém, caso necessário, direcione a inserção do recurso ao DBA responsável da sua empresa.

---

Nesse artigo trataremos sobre os seguintes tópicos:

| [![Imagem 5: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311107984151)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#configurandoagradedatela) | [![Imagem 6: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118796311)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#cria%C3%A7%C3%A3odeobjetos) | [![Imagem 7: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118798999)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#preenchimentodocamporegra) |
| --- | --- | --- |
|  |  |  |
| [![Imagem 8: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118799895)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#altera%C3%A7%C3%A3odeobjetos) | [![Imagem 9: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118801943)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#dashboardtelemetriadeobjetos) | [![Imagem 10: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118803223)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#configuraraordemdeexecu%C3%A7%C3%A3odosobjetos) |
|  |  |  |
| [![Imagem 11: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118804631)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#parametrizartelemetria) | [![Imagem 12: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118805527)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#d%C3%BAvidasfrequentes) | [![Imagem 13: Nesse artigo trataremos sobre os seguintes tópicos:](https://ajuda.sankhya.com.br/hc/article_attachments/42311118810391)](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#resolu%C3%A7%C3%A3odeproblemas) |

| **Clique nas imagens acima para saber mais** |
| --- |

---

#### Configurando a Grade da Tela

As colunas apresentadas na tela Gerenciador de Objetos podem ser personalizadas conforme sua necessidade. Abaixo, siga os passos necessários para essas personalizações:

Acesse o ícone **"Modo Formulário"** e selecione **"Configurar grade"**; assim, a tela para configuração será aberta. As movimentações podem ser feitas através das setas, podendo mover as colunas que estão em **"Colunas disponíveis"** para **"Colunas selecionadas"**, a fim de serem apresentadas ou não na grade e também, sendo possível selecionar a ordem dessas colunas.

Após realizar as alterações, basta clicar no botão **"Salvar"**:

[GIF animado: Imagem 14: Após realizar as alterações, basta clicar no botão "Salvar" :](https://ajuda.sankhya.com.br/hc/article_attachments/4404769294231)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Criação de Objetos

Para criar novas regras de negócios personalizadas, siga os procedimentos abaixo:

Clique no botão ![Imagem 15: Clique no botão "Cadastrar Regras de customização" . Após isso, a tela de cadastro será aberta para preenchimento das…](https://ajuda.sankhya.com.br/hc/article_attachments/16428100941463) **"Cadastrar Regras de customização"**. Após isso, a tela de cadastro será aberta para preenchimento das informações necessárias:

[GIF animado: Imagem 16: Clique no botão "Cadastrar Regras de customização" . Após isso, a tela de cadastro será aberta para preenchimento das…](https://ajuda.sankhya.com.br/hc/article_attachments/4404776505751)

Trouxemos uma descrição para te orientar no preenchimento dos campos:

No campo **"Tabela Relacionada"**, selecione a tabela correspondente na qual será criada a regra de negócio.

Informe no campo **"Nome Regra"**, o nome do objeto no banco de dados, por exemplo: **"STP\_VALIDA\_PROD"**.

Quando a marcação **"Ativo"** estiver habilitada, quer dizer que a regra será executada; se não estiver marcada, não haverá a execução da regra.

O campo **"Status Publicação"** é preenchido automaticamente, sendo possível identificar se o objeto foi publicado ou publicado com erro.

No campo **"Grupo"** você poderá selecionar ou criar agrupadores para um conjunto de regras de negócio para facilitar a identificação. Exemplo: Fiscal, Contabilidade, Produção, Comercial, entre outros.

Para utilizar um grupo já criado, basta acessar a lupa ao lado:

[GIF animado: Imagem 17: Para utilizar um grupo já criado, basta acessar a lupa ao lado:](https://ajuda.sankhya.com.br/hc/article_attachments/4404777581591)

**Observação:** para criar um novo grupo, basta digitar o nome dele no campo. Assim, após a criação do objeto, o novo grupo será inserido na lista de grupos disponibilizados no painel de filtros rápidos:

[GIF animado: Imagem 18: Observação: para criar um novo grupo, basta digitar o nome dele no campo. Assim, após a criação do objeto, o novo grupo…](https://ajuda.sankhya.com.br/hc/article_attachments/4404770733591)

Na aba **"Dados do Objeto"** preencha as seguintes informações:

No campo **"Descrição"**, informe o funcionamento da regra de negócio, qual será o impacto no sistema, qual será o objetivo da regra de negócio, etc.

A marcação **"Insert"** fará com que a regra seja executada no momento de inserção da tabela selecionada.

Já a marcação **"Update"**, quando habilitada, fará com que a regra seja executada no momento de atualização da tabela selecionada.

A marcação **"Delete"** irá executar a regra no momento em que um registro for removido da tabela selecionada.

No campo **"Momento de Execução"**, selecione o momento em que o objeto será executado (**"Before"** ou **"After"**). Se será antes ou após os eventos de Insert, Update ou Delete serem aplicados na tabela.

O campo **"Tipo"** possui duas opções, sendo **"Nativo"** para os objetos originários do ERP e **"Personalizada"** para os objetos criados.

Atualmente, o Gerenciador de Objetos tem a **"Abrangência"** apenas para objetos **"for each row"**. O gatilho é chamado uma vez para cada linha que a operação modifica.

No campo **"Documentação"**, você poderá anexar um documento detalhando a funcionalidade do objeto.

Por fim, no campo **"Regra"**, deve ser inserida a regra de negócio do cliente que foi desenvolvida em PL-SQL. Caso hajam dúvidas sobre o preenchimento desse campo, acesse o tópico [Preenchimento do campo Regra](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#preenchimentodocamporegra).

Após o preenchimento dos campos necessários, clique no botão ![Imagem 19: Após o preenchimento dos campos necessários, clique no botão "Salvar" .](https://ajuda.sankhya.com.br/hc/article_attachments/16428144052119) **"Salvar"**.

Após salvar o objeto, será aberto um pop-up para informar o motivo da criação. Ao salvar o motivo, o objeto passará por uma validação que poderá ou não apresentar erro. Caso não apresente erro, o objeto será publicado no banco de dados e estará pronto para ser executado, conforme as regras definidas, obedecendo o momento de execução e os eventos de Insert, Update e Delete.

Dando continuidade, na aba **"Histórico de Alterações"** podemos verificar as informações relacionadas à criação e todas as alterações realizadas no objeto:

![Imagem 20: Dando continuidade, na aba "Histórico de Alterações" podemos verificar as informações relacionadas à criação e todas as…](https://ajuda.sankhya.com.br/hc/article_attachments/4404800466839)

No campo **"Data"** você poderá selecionar os períodos que deseja ou selecionar os períodos configurados no sistema.

Na aba **"Telemetria"** podemos visualizar a quantidade de vezes que a regra de negócio foi disparada, o tempo total e o tempo médio de execução da regra:

![Imagem 21: Na aba "Telemetria" podemos visualizar a quantidade de vezes que a regra de negócio foi disparada, o tempo total e o…](https://ajuda.sankhya.com.br/hc/article_attachments/4404800503191)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Preenchimento do campo Regra

A estrutura criada para comportar a regra é composta por uma package e duas triggers por tabela. As triggers são responsáveis por executar a regra antes ou após uma modificação de um registro da tabela.

Você terá acesso para criação de uma procedure com um comportamento similar de uma trigger, sendo possível acessar o New e Old porém, com uma sintaxe um pouco diferente. Utilizaremos o exemplo de um objeto sendo criado na tabela TGFPRO (Tabela de Produtos) para acessar as informações de New e Old da TGFPRO:

PKG\_DSP\_TGFPRO.NEW\_CODPROD
PKG\_DSP\_TGFPRO.OLD\_CODPROD

**Observação:** para cada tabela que possua uma regra cadastrada, o sistema irá gerar um pacote contendo os campos da tabela com a informação de New e Old. A estrutura será sempre PKG\_DSP\_”NOME DA TABELA”.”TEMPO”\_”NOME DO CAMPO” (PKG\_DSP\_TGFPRO.NEW\_ATIVO).

O pacote também auxiliará as informações do momento de execução, sendo três eventos:

- PKG\_DSP\_TGFPRO.EVENTO := 'INSERTING';
- PKG\_DSP\_TGFPRO.EVENTO := 'UPDATING';
- PKG\_DSP\_TGFPRO.EVENTO := 'DELETING';

![Imagem 22: Não poderão ser utilizados campos dos tipos CLOB e BLOB . A imagem abaixo demonstra um exemplo de como utilizar:](https://ajuda.sankhya.com.br/hc/article_attachments/16428159521303) Não poderão ser utilizados campos dos tipos CLOB e BLOB. A imagem abaixo demonstra um exemplo de como utilizar:

![Imagem 23: Não poderão ser utilizados campos dos tipos CLOB e BLOB . A imagem abaixo demonstra um exemplo de como utilizar:](https://ajuda.sankhya.com.br/hc/article_attachments/4404786531351)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Alteração de Objetos

Para realizar alterações das regras de negócio nos objetos, realize os procedimentos abaixo:

1. Selecione o objeto que deseja editar com um duplo clique;
2. Realize as alterações desejadas e clique no botão Salvar;
3. Após salvar o objeto, será aberto um pop-up para informar o motivo das alterações; clique no botão Salvar;
4. Para consultar as alterações realizadas no objeto, clique na aba **"Histórico de Alterações"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Dashboard Telemetria de Objetos

Nesse dashboard podemos visualizar a quantidade de execuções, o tempo de processamento utilizado por cada objeto e um indicador apresentando quais objetos estão afetando a performance do sistema. Para acessá-lo, inicialmente, clique no botão **"Telemetria"** localizado no alto da tela e, logo depois, na tela que se abre (**"Telemetria de Objetos"**), selecione os filtros que deseja:

![Imagem 24: Nesse dashboard podemos visualizar a quantidade de execuções, o tempo de processamento utilizado por cada objeto e um…](https://ajuda.sankhya.com.br/hc/article_attachments/4404801362455)

Assim, será apresentada a lista de objetos com alguns indicadores, conforme as métricas abaixo:

- **Farol Verde:** Tempo médio de execução entre 0 e 0,4999 seg.
- **Farol Amarelo:** Tempo médio de execução entre 0,5000 e 0,9999 seg.
- **Farol Vermelho:** Tempo médio de execução acima de 1 seg.
- **Linha Vermelha:** Tempo médio de execução acima de 5 seg.

![Imagem 25: Linha Vermelha : Tempo médio de execução acima de 5 seg.](https://ajuda.sankhya.com.br/hc/article_attachments/4404801306775)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Configurar a Ordem de Execução dos Objetos

A ordem de execução dos objetos é realizada conforme a ordem de criação/alteração deles. Nesse campo, foi disponibilizada uma tela para que você possa selecionar a ordem de acordo com sua necessidade.

Então, clique no botão ![Imagem 26: Então, clique no botão "Outras Opções..." e selecione a opção "Criar ordem de execução" .](https://ajuda.sankhya.com.br/hc/article_attachments/16428231030679) **"Outras Opções..."** e selecione a opção **"Criar ordem de execução"**.

A seleção da ordem é feita através das setas. Assim, após selecionar a ordem desejada, clique em **"Salvar Ordem"**:

[GIF animado: Imagem 27: A seleção da ordem é feita através das setas. Assim, após selecionar a ordem desejada, clique em "Salvar Ordem" :](https://ajuda.sankhya.com.br/hc/article_attachments/4404787523863)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Parametrizar Telemetria

Aqui também podemos configurar a quantidade de dias em que a telemetria será armazenada, considerando que o período mínimo é de 7 dias e o máximo de 90 dias:

[GIF animado: Imagem 28: Aqui também podemos configurar a quantidade de dias em que a telemetria será armazenada, considerando que o período…](https://ajuda.sankhya.com.br/hc/article_attachments/4404787788823)

Para realizar essa, clique no botão Outras Opções... e selecione a opção **"Parametrizar telemetria"**. Após isso, informe a quantidade de dias que a telemetria será armazenada e clique em **"Salvar"**:

[GIF animado: Imagem 29: Para realizar essa, clique no botão Outras Opções... e selecione a opção "Parametrizar telemetria" . Após isso, informe…](https://ajuda.sankhya.com.br/hc/article_attachments/4404787691799)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Dúvidas frequentes

![Imagem 30: Quais os tipos de objetos aceitos pelo Gerenciador de Objetos ?](https://ajuda.sankhya.com.br/hc/article_attachments/16428231033239) Quais os tipos de objetos aceitos pelo Gerenciador de Objetos?

São aceitas as regras do negócios do tipo trigger, ou seja, são procedures com comportamento de trigger, sendo que não é possível criar functions e views pelo Gerenciador de Objetos.

![Imagem 31: As regras de negócios atuais serão transferidas automaticamente para o Gerenciador de Objetos ?](https://ajuda.sankhya.com.br/hc/article_attachments/16428292077335) As regras de negócios atuais serão transferidas automaticamente para o Gerenciador de Objetos?

Não, as transferências deverão ser realizadas manualmente.

![Imagem 32: Preciso transferir todas as minhas regras de negócios atuais?](https://ajuda.sankhya.com.br/hc/article_attachments/16428292080023) Preciso transferir todas as minhas regras de negócios atuais?

Não, as transferências ficam a critério do cliente. Porém os benefícios oferecidos pela ferramenta só poderão ser avaliados se os objetos estiverem na tela do Gerenciador de Objetos, como por exemplo, telemetria de objetos e histórico de alterações.

![Imagem 33: Para qual tipo de banco é aplicado o Gerenciador de Objetos ?](https://ajuda.sankhya.com.br/hc/article_attachments/16428292082199) Para qual tipo de banco é aplicado o Gerenciador de Objetos?

Atualmente, é aplicado apenas para o banco de dados Oracle.

![Imagem 34: Como utilizar NEW e OLD no Gerenciador de Objetos ?](https://ajuda.sankhya.com.br/hc/article_attachments/16428292084631) Como utilizar NEW e OLD no Gerenciador de Objetos?

Para melhor exemplificação utilizaremos a tabela TGFFIN, de forma que, para criar regras através do banco de dados e utilizar NEW e OLD de uma trigger, o executante aplica :NEW ou :OLD.

Assim, na ferramenta do Gerenciador de Objetos a sintaxe é alterada para PKG\_DSP\_TGFFIN.NEW\_. Observe o exemplo abaixo:

O comando :NEW.CODPARC será alterado para: PKG\_DSP\_TGFFIN.NEW\_CODPARC
O comando :OLD.CODPARC será alterado para: PKG\_DSP\_TGFFIN.OLD\_CODPARC

![Imagem 35: Como utilizar Evento no Gerenciador de Objetos ?](https://ajuda.sankhya.com.br/hc/article_attachments/16428292087319) Como utilizar Evento no Gerenciador de Objetos?

Para este, considere a tabela TGFFIN para exemplificação:

A informação do evento vai sempre estar dentro da PKG\_DSP\_TGFFIN.EVENTO, essa variável sempre contém uma das seguintes informações: INSERTING, UPDATING ou DELETING. A ordem de execução dos objetos é realizada conforme a ordem de criação/alteração dos mesmos. Para fazer essa seleção conforme a sua necessidade, acesse o botão **"Outras opções"** e selecione **"Criar ordem de execução"** e por meio das setas, selecione a ordem desejada e clique em **"Salvar Ordem"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)

#### Resolução de problemas

Caso identifique problemas na tela do Gerenciador de Objetos ou na compilação dos objetos e não consiga resolvê-los, estes deverão ser direcionados para a equipe de suporte Service Desk da Sankhya.
Os demais problemas relacionados às regras de negócios e os códigos SQL, são de responsabilidade do cliente ou do responsável pela criação do objeto.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4404768181271-Gerenciador-de-Objetos#top)
