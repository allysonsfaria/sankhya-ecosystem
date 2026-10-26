---
id: "4410963788951"
titulo: "Eventos Formulários Formatados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:11:07Z"
rotulos: ["Configuração", "Eventos", "sankhyaflow", "formulários", "eventos formulários formatados", "flow", "Altera prioridade e envia e-mails automáticos", "Algoritmos executados em formulários formatados", "Uso de Java/Procedure para automação e integrações", "Java", "Sankhya Om", "Automação", "Formulários Formatados"]
---

# Eventos Formulários Formatados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313359491735) Versão: a partir da 3.2
```

---

O Evento de Formulários Formatados, poderá definir que um algoritmo associado a um determinado Formulário Formatado seja executado, isto é, quando esse tipo de Formulário estiver configurado com um ou mais Eventos, uma ação pode acontecer conforme a regra de negócio estabelecida no algoritmo.

Esses eventos, quando configurados, permitem automações e/ou integrações com outros módulos do Sankhya Om. Permitem também, o uso de algoritmos em Java ou em Procedure, definidos para executar em qualquer momento que o Formulário Formatado for utilizado, sendo este, na inserção de um registro do formulário, na exclusão de uma linha do formulário, entre outros.

Baseado nisso, considere como exemplo, quando você utilizar um mesmo Formulário Formatado de Cadastro de Produto que é usado no processo de Pedido de Compra e Cadastro de Produto, quando houver uma alteração, ou inclusão de um novo registro no Formulário, um Evento dispara uma mensagem no Sankhya-Om aos interessados do processo.

Dessa forma, nesse artigo trataremos do nosso [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#casodeuso), da [Configuração de um Evento Formulário Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#configura%C3%A7%C3%A3odeumeventoformul%C3%A1rioformatado), das [Demais informações e tópico de Procedure](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#demaisinforma%C3%A7oesetopicodeprocedure), além dos [Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#resultados).

---

#### Caso de Uso

A empresa Alpha Ltda é uma corretora de seguros que possui um processo interno chamado **"Manutenção Corretiva de Equipamentos"**.

Nesse processo, a equipe de manutenção irá solicitar uma manutenção para análise do equipamento e, dessa análise, pode surgir a necessidade de compra de uma nova peça para o reparo do equipamento e após a compra, o fluxo deve seguir para o técnico responsável realizar o conserto, e em seguida, será direcionado para o solicitante realizar a avaliação do atendimento, como representado na imagem abaixo:

![Imagem 2: Nesse processo, a equipe de manutenção irá solicitar uma manutenção para análise do equipamento e, dessa análise, pode…](https://ajuda.sankhya.com.br/hc/article_attachments/4410941539351)

| **Processo de Manutenção Corretivo de Equipamentos** |
| --- |

Como a empresa Alpha já possuía um processo de **"Compra de materiais"** modelado e em produção, o modelador o definiu como um subprocesso do processo de Manutenção Corretiva de Equipamento, reutilizando todo o processo de compra de materiais, visto que, ambos compartilham o mesmo Formulário Formatado chamado, **"Solicitação de Produto"**.

Quando o técnico optar por solicitar peças para o conserto do equipamento no processo de **"Manutenção"**, os dados preenchidos pelo usuário na tarefa **"Analisar equipamento"** serão carregados automaticamente no formulário para representar a Solicitação de Produto no subprocesso de **"Solicitação de Compra"**, como você pode observar na imagem abaixo:

![Imagem 3: Quando o técnico optar por solicitar peças para o conserto do equipamento no processo de "Manutenção" , os dados…](https://ajuda.sankhya.com.br/hc/article_attachments/4410949931031)

| **Subprocesso de Solicitação de compra** |
| --- |

Todo o processo, incluindo seu subprocesso, possui um campo no Formulário Formatado Solicitação de Produto chamado **"Priorização"** do chamado, localizado no formulário **"AD\_ADTWFSOLPROD"**; o campo possui três valores, sendo estes, **"P1"** o nível mais rápido, ou seja, precisa ser atendido com máxima urgência, até o nível **"P3"**, sendo ele o de menor urgência.

Todo atendimento é classificado em função da priorização e quando alterada essa priorização, ao longo do atendimento os gestores do processo recebem essa informação por e-mail. Uma vez que, quando o subprocesso for concluído, o fluxo seguirá para o técnico consertar o equipamento. Nessa tarefa, iremos disponibilizar o número do pedido de compra para a consulta e localização o produto junto à área responsável.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)

#### Configuração de um Evento Formulário Formatado

No caso de uso aqui exposto, o algoritimo utilizado será feito em Java, então, o primeiro passo para montar seu projeto Java, é baixar a biblioteca de extensões, jape e modelcore, que possui extensões para trabalhar com personalizações no Sankhya-Om. Para o acesso e download da extensão, siga os seguintes passos:

1. Abra a tela [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados);
2. Localize o Formulário de sua preferência;
3. Vá até à Aba [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados#abaeventos);
4. Nessa aba, no campo **"Tipo"**, selecione a opção **"Rotina Java"** para que a opção **"Baixar biblioteca de extensões"** fique disponível.

Após o download da biblioteca, faça a criação de um Projeto Java. Neste exemplo, será utilizada a IDE Eclipse. Sendo assim, ao abrir o arquivo baixado, siga os passos a seguir:

1. Clique em **"New"**;
2. Em seguida, nomeie seu projeto como **"Java Project"** e clique no botão **"Next"**;
3. Quando o pop-up **"Java Settings"** for aberto, acesse a aba **"Libraries"**;
4. Adicione os arquivos **"SankhyaW-extensions"**, **"jape-4.9b59.jar"** e **"mge-modelcore.jar"**.

[GIF animado: Imagem 4: Adicione os arquivos "SankhyaW-extensions" , "jape-4.9b59.jar" e "mge-modelcore.jar" .](https://ajuda.sankhya.com.br/hc/article_attachments/4410946339735)

![Imagem 5: Os arquivos aqui mencionados, encontram-se neste link .](https://ajuda.sankhya.com.br/hc/article_attachments/16092826091543) Os arquivos aqui mencionados, encontram-se [neste link](https://drive.google.com/drive/folders/1nzJCrTjcvWKkZpkKw9ZHRwaWx2L4XBog).

É necessário criar uma Classe Java, implementando a interface **"EventoProgamavelJava"**. Visto que, cada método possui uma utilização distinta, os métodos relacionados a esta interface são carregados. Observe:

- **afterDelete:** Antes de deletar um registro o algoritmo escrito será executado.
- **afterInsert:** Antes de inserir um registro o algoritmo escrito será executado.
- **afterUpdate:** Antes de atualizar um registro o algoritmo escrito será executado.
- **beforeCommit:** Antes de oficializar a transação no banco de dados o algoritmo escrito será executado.
- **beforeDelete:** Depois de deletar um registro o algoritmo escrito será executado.
- **beforeInsert:** Depois de inserir um registro o algoritmo escrito será executado.
- **beforeUpdate:** Depois de atualizar um registro o algoritmo escrito será executado.

**Observação:** nos Tipos de Eventos before(Commit, Delete, Insert, Update), também é possível acessar um registro antigo, utilizando o método:

| ``` oldVo //ou também// event.getOldVo(); ``` |
| --- |

Algumas outras interfaces serão também importadas ao algoritmo, confira abaixo, o algoritmo completo:

| ``` import  br.com.sankhya.extensions.eventoprogramavel.EventoProgramavelJava;  import java.math.BigDecimal; import java.sql.ResultSet; import br.com.sankhya.jape.EntityFacade; import br.com.sankhya.jape.dao.JdbcWrapper; import br.com.sankhya.jape.sql.NativeSql; import br.com.sankhya.jape.vo.DynamicVO; import br.com.sankhya.jape.event.PersistenceEvent; import br.com.sankhya.jape.event.TransactionContext; import br.com.sankhya.modelcore.actionbutton.ProgrammableUtils; import br.com.sankhya.modelcore.util.EntityFacadeFactory;  public class eventoDeEmail implements EventoProgramavelJava {      public void afterDelete(PersistenceEvent arg0) throws Exception {}     public void afterInsert(PersistenceEvent event) throws Exception {}     public void afterUpdate(PersistenceEvent event) throws Exception {         if (event.getModifingFields().isModifing("PRIORIZACAO")) {              //declarando variáveis              DynamicVO vo = (DynamicVO) event.getVo ();             String prio = vo.asString("PRIORIZACAO");             String shadow_prio = vo.asString("SHADOW_PRIORIZACAO");             BigDecimal peca = vo.asBigDecimal("CODPROD");             BigDecimal id = vo.asBigDecimal("IDINSTPRN");                String nomePeca = null;             String assunto = "Uma priorização de pedido foi alterada.";             String email = "email@sankhya.com.br";                   JdbcWrapper jdbc = null;             NativeSql sql = null;              EntityFacade entityFacade =  EntityFacadeFactory.getDWFFacade();             jdbc = entityFacade.getJdbcWrapper();              //consultando para obter o nome da peça             sql = new NativeSql(jdbc);             sql.appendSql (" SELECT ");             sql.appendSql ("     DESCRPROD ");             sql.appendSql (" FROM ");             sql.appendSql ("     TGFPRO ");             sql.appendSql (" WHERE ");             sql.appendSql ("CODPROD = :CODPROD");              sql.setNamedParameter("CODPROD", peca);              ResultSet rset = sql.executeQuery();              if (rset.next()) {                 nomePeca = rset.getString("DESCRPROD");             }              //montando a mensagem de email             StringBuffer msgbuff = new StringBuffer();             msgbuff.append (" Priorização do pedido ");             msgbuff.append (id);             msgbuff.append (" da peça ");             msgbuff.append (nomePeca);             msgbuff.append (" foi alterado de ");             msgbuff.append (shadow_prio);             msgbuff.append (" para ");             msgbuff.append (prio);              //método que dispara o email             ProgrammableUtils.eMail(entityFacade, assunto,  msgbuff.toString(), email);         }     }       public void beforeCommit(TransactionContext arg0) throws Exception  {}     public void beforeDelete (PersistenceEvent arg0) throws Exception {}     public void beforeInsert (PersistenceEvent arg0) throws Exception {}     public void beforeUpdate (PersistenceEvent arg0) throws Exception {} } ``` |
| --- |

Após o algoritmo ser implantado conforme a regra de negócio do caso de uso, basta salvar o projeto e exportá-lo, sendo este um arquivo do tipo **".jar"**. Observe:

1. Salve o algoritmo por meio do caminho **"File"** > **"Save all"** e em seguida clique em **"Export..."**;
2. No pop-up **"JAR Export"**, você, como modelador, deve selecionar o seu projeto como um todo no painel **"Select the resources to export"**;
3. No mesmo pop-up, em **"Select the export destination"** escolha a pasta onde deseja salvar e clique em **"Finish"**.

![Imagem 6: No mesmo pop-up, em "Select the export destination" escolha a pasta onde deseja salvar e clique em "Finish" .](https://ajuda.sankhya.com.br/hc/article_attachments/4410961389847)

| **Pop-up JAR Export** |
| --- |

Após essa etapa, é necessário realizar o upload do módulo java gerado, de forma que, o arquivo irá para a base Sankhya-Om que o modelador esteja trabalhando. Assim, com o Sankhya aberto, siga os seguintes passos:

1. Primeiramente, como modelador, acesse a tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573-M%C3%B3dulo-Java);
2. Em seguida, cadastre o Módulo Adicional e preencha o campo **"Identificador"** da aba **"Geral"**;
3. Na aba **"Arquivo Módulo (Jar)"**, cadastre o arquivo módulo Arquivo Módulo (Jar), e localize o arquivo jar que foi salvo anteriormente.

Dessa forma, o módulo Java gerado com as regras de negócio deste caso de uso estará disponível para ser utilizado no Sankhya-Om, como na imagem abaixo:

![Imagem 7: Dessa forma, o módulo Java gerado com as regras de negócio deste caso de uso estará disponível para ser utilizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/4410961904919)

| **Configuração de Evento no Formulário Formatado** |
| --- |

E por fim, deve-se relacionar esse módulo Java na aba Eventos do Formulário Formatado. Observe:

1. Na tabela AD\_ADTWFSOLPROD do Dicionário de Dados, digite a Descrição do Evento;
2. Logo depois selecione o Tipo, sendo esta a Rotina Java;
3. Para o módulo Java ser vinculado, basta clicar no botão ![Imagem 8: Para o módulo Java ser vinculado, basta clicar no botão do campo "Módulo" para procurar o módulo Java que você…](https://ajuda.sankhya.com.br/hc/article_attachments/4410963642519) do campo **"Módulo"** para procurar o módulo Java que você adicionou anteriormente no Sankhya-Om;
4. Por último, selecione a classe em que será executada nessa ação.

![Imagem 9: Por último, selecione a classe em que será executada nessa ação.](https://ajuda.sankhya.com.br/hc/article_attachments/4411032155927)

| **Configuração de Evento no Formulário Formatado** |
| --- |

| ![Imagem 10: Configuração de Evento no Formulário Formatado](https://ajuda.sankhya.com.br/hc/article_attachments/42313349112087) | Um mesmo arquivo **".jar"** pode conter um algoritmo com várias classes e cada classe pode ser vinculada seperadamente em vários eventos ou no mesmo eventos. |
| --- | --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)

#### Demais informações e Tópicos da Procedure

Em nosso caso de uso, o Evento foi definido para seu algoritmo ser em Java, criando um módulo java e o configurando no Formulário Formatado, mas além do Java é possível criar um algoritmo para o Evento baseado em Procedure, ou seja, uma Rotina no Banco de Dados.

Para isso, basta acessar novamente a aba Eventos do Formulário Formatado no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) e no campo **"Tipo"** selecionar a opção **"Rotina no Banco de Dados"**:

![Imagem 11: Para isso, basta acessar novamente a aba Eventos do Formulário Formatado no Dicionário de Dados e no campo "Tipo"…](https://ajuda.sankhya.com.br/hc/article_attachments/4411032238615)

| **Criação de Evento com Procedure** |
| --- |

Logo depois, clique em **"Criar um template da rotina"**, sendo este a estrutura base da Procedure é criada no Banco de Dados.

A lógica do algoritmo em Procedure é a mesma da implementada em Java, baseado nos Tipos de Eventos. Assim, considere-os:

- BEFORE INSERT;
- AFTER INSERT;
- BEFORE DELETE;
- AFTER DELETE;
- BEFORE UPDATE;
- AFTER UPDATE; e
- BEFORE COMMIT.

Portanto, conforme a regra de negócio, o modelador irá escolher o tipo mais adequado para implementar a Procedure. Sendo que, nela você poderá encontrar mais detalhes para auxiliá-lo na criação do algoritmo.

[[volt](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)[ar](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top) [ao](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top) [top](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)[o]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)

#### Resultados

Conforme as configurações aqui realizadas, exibiremos os resultados nesse tópico.

Foi lançada uma requisição solicitando a Manutenção Corretiva, assim, os dados foram inseridos juntamente com a peça a ser trocada e a prioridade dela, sendo que, a prioridade para a troca desta peça é uma **"P2"**. Considere ainda que, para este exemplo, a peça em questão é uma peça para notebook. Assim, teremos:

![Imagem 12: Foi lançada uma requisição solicitando a Manutenção Corretiva , assim, os dados foram inseridos juntamente com a peça a…](https://ajuda.sankhya.com.br/hc/article_attachments/4411027636503)

| **Lançamento da Manutenção Corretiva** |
| --- |

Logo, podemos perceber que a Manutenção Corretiva seguiu para o Subprocesso de Solicitação de Compras, pois não há estoque do notebook. Na Solicitação de Compras, o usuário responsável pela análise, reclassificou a priorização para esta peça, passando de P2 para **"P1"**:

![Imagem 13: Logo, podemos perceber que a Manutenção Corretiva seguiu para o Subprocesso de Solicitação de Compras , pois não há…](https://ajuda.sankhya.com.br/hc/article_attachments/4411032397975)

| **Tarefa do SubProcesso "Analisar Solicitação de Compra"** |
| --- |

Logo, quando a prioridade foi alterada e salva, um e-mail será enviado aos gestores do processo para que estes tenham a ciência de que tal alteração ocorreu, conforme a regra de negócio definida.

[[volt](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)[ar](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top) [ao](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top) [top](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)[o]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4410963788951-Eventos-Formul%C3%A1rios-Formatados#top)
