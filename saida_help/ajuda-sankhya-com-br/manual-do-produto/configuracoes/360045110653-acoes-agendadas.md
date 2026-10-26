---
id: "360045110653"
titulo: "Ações Agendadas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-28T14:17:02Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Ações Agendadas", "br.com.sankhya.acoesagendadas", "Ações Agendadas manual", "Agendamento", "Ações Agendadas para Execução Automática", "Java", "Quartz"]
---

# Ações Agendadas

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310927172375) Módulo: Configurações > Cadastros
```

---

Por meio desta tela são cadastradas as ações que serão executadas em intervalos periódicos de tempo. Esse comportamento está fundamentado no funcionamento do quartz (Agendador), que é uma infraestrutura preparada para configurar o agendamento de tarefas. As expressões podem ser configuradas como intervalos de tempo, segundos, minutos, horas ou ainda como expressões do quartz.

| Funcionalidades da tela |
| --- |
| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#abageral) |
| [Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#botolog...) |
| [Aba Configurar expressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#abaconfigurarexpresso) |
| [Ações Agendadas - Exemplo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#aesagendadas-exemplo) |

![Imagem 2: Ações Agendadas - Exemplo](https://ajuda.sankhya.com.br/hc/article_attachments/5546020264343)

Para a configuração de uma Ação Agendada, inicialmente é necesário realizar o preenchimento do campo **"Nro. único"**, que pode ser alimentado de forma manual ou automática; essa definição é feita através do botão ![Imagem 3: Para a configuração de uma Ação Agendada , inicialmente é necesário realizar o preenchimento do campo "Nro. único" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/16343566072983) **"Configurações da Tela"**, opção **"Numeração"** localizado no lado superior direito da tela.

A marcação **"Ativo"** irá determinar se a ação está ou não operante. Sendo que, quando habilitada, logo a frente, será apresentada a descrição **"A ação está ativa"**, e quando desabilitada, ficará com a descrição **"A ação está desativada"**.

### Aba Geral

Neste aba, realize a configuração do fundamento da ação. Devem ser informados os seguintes campos:

No campo **"Nome"**, informe o nome da ação que está sendo criada; este nome será apresentado no log de execução da ação.

Preencha em **"Descrição"**, a definição da ação que quando informada, também será exibida no log de execução da ação.

Determine o **"Tipo de ação"** a ser configurada. Esta poderá ser:

- **Proc. Banco de dados:** por esta opção, o nome da procedure criada na base, que será executada conforme o agendamento;
- **Java:** ao selecionar essa opção, cadastre um módulo JAVA na tela [Módulo Java](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110573), com um arquivo.jar que contenha uma classe que implemente a interface ScheduledAction do arquico Cuckoo.jar, disponível na api\_outros.

Indique em **"Cód. módulo"**, o código do módulo Java cadastrado que será carregado a classe Java executada conforme o agendamento.

Selecione no campo **"Ação"**, a ação de acordo com o módulo que ela pertence, ou seja,  a scheduledAction que contenha a ação que deseja desempenhar. Quando procedure, o nome da procedure.

Caso a ação necessite de uma sessão do sistema para desempenhar sua tarefa, informe no campo **"Usuário Logado"**, o usuário com o qual será feito o login. Nesse caso, devem ser levadas em consideração as permissões do usuário ser informado conforme a ação a ser desempenhada.

Indique no campo **"Fonte de dados"**, a fonte de dados registrada no sistema, na qual serão efetuadas as modificações da ação; sendo procedure, a base onde irá rodar esta procedure.

Quando a marcação **"Transação automática"** for realizada, indica que a ação irá utilizar transação automática de banco de dados; se desmarcada, não irá utilizar.

**Observação:** ao criar uma ação agendada, o sistema poderá realizar uma consulta ao Serasa com um CNPJ, CPF ou Prospect automaticamente para um parceiro, de acordo com a personalização a ser definida.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#top)

### Aba Configurar expressão

Nessa aba, defina as configurações acerca da frequência em que as ações criadas serão executadas.

![Imagem 4: Nessa aba, defina as configurações acerca da frequência em que as ações criadas serão executadas.](https://ajuda.sankhya.com.br/hc/article_attachments/5546083955095)

Sabendo disso, configure os seguintes campos:

Em **"Tipo de gatilho"**, será estipulado a forma como será tratada a sequência de execução das ações. Existem duas opções:

- **Intervalo de tempo:** defina um intervalo homogêneo de segundos, minutos ou horas para ser executada a ação;
- **Expressão CRON:** É a maneira de configuração que permite um ajuste mais fino do intervalo de tempo, possibilitando a inserção manual no campo uma expressão do cron.

O campo **"Expressão de gatilho"** é preenchido a medida que os intervalos dispostos em forma de Lista de opções (segundos, minutos, horas, dias, meses, dias da semana) forem definidos.

Ainda sobre a Lista de Opções, tem-se as seguintes considerações:

Cada lista de opções equivale a um dos caracteres gerados no campo **"Expressão de gatilho"**, ao passo que qualquer modificação em uma das listas ou suas opções, irá refletir em uma atualização no referido campo. Assim, observe:

- O caractere **'\*'** (asterisco) significa **"todos"**. No caso, uma lista vazia gera um asterisco e significa que o agendamento irá rodar em todos os valores para aquela determinada lista de opções;
- É possível especificar um **"dia"** ou **"dia da semana"** para a execução, mas não os dois simultaneamente, pois tal configuração poderia ser inconsistente;
- O caractere **'?'** (interrogação) significa **"não importa"**, ele pode ser utilizado para dias ou dias da semana. Dessa forma, quando selecionado um ou mais dias para executar o agendamento, obrigatoriamente o dia da semana será preenchido com interrogação no campo Expressão do gatilho. Caso sejam selecionados dias da semana, os dias serão configurados com interrogação no campo "Expressão do gatilho";
- Caso a marcação **"Intervalo?"** não esteja realizada, mas vários valores na lista foram selecionados, serão incluídos no campo os valores selecionados separados por vírgulas, indicando que o agendamento será executado para cada valor selecionado;
- Quando a marcação Intervalo? for habilitada em alguma das listas, e esta estiver com mais de um valor selecionado, o valor gerado será substituído pelo primeiro e o último valor selecionados separados por um hífen ( - ) no campo Expressão do gatilho, o que indicará que o agendamento será executado para todos os valores contidos no intervalo;
- O botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992976830615)**"Limpar"** de uma determinada lista, irá limpar a seleção da lista e troca o valor referente a mesma por um asterisco, indicando que o agendamento será executado para todos os valores desse intervalo;

**Nota:** o botão Limpar será apresentado somente na versão flex dessa tela.

- Já o botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992976831511)**"Limpar listas"** limpa a seleção de todas as listas, o que possibilita o reinício da seleção dos valores desejados para a configuração;

- O botão ![botão](https://ajuda.sankhya.com.br/hc/article_attachments/15992961976087)**"Validar Expressão"** analisará a expressão e caso ocorra algum erro, irá exibi-lo na tela, e quando não houver erro, o sistema exibirá o horário da próxima execução.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#top)

### Botão Outras Opções

Localizado no lado superior central da tela, é possível visualizar o botão ![Imagem 8: Localizado no lado superior central da tela, é possível visualizar o botão Outras Opções... que possibilita a geração…](https://ajuda.sankhya.com.br/hc/article_attachments/23536982434583) Outras Opções... que possibilita a geração do log dos jobs. Ele possui duas opções, sendo elas:

- **Ações ativas:** essa opção exibirá um pop-up denominado **"Lista de jobs cadastrados"**, na qual será apresentado o log relacionado às ações ativas.
- **Ações em execução no momento:** por meio dessa opção, o pop-up **"Lista de jobs em execução"** será aberto onde conterá o log das ações em execução no momento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#top)

### Ações Agendadas - Exemplo

Ao utilizar a [Configuração do Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110273-Configura%C3%A7%C3%A3o-Arquivo-de-Remessa), é possível gerar o arquivo de configuração de forma automática a partir de [Ações Agendadas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108753-Configura%C3%A7%C3%A3o-Arquivo-Remessa#aesagendadas). Isso é feito em um ambiente de desenvolvimento Java. Assim, considere o exemplo abaixo:

```
     package br.com.sankhya.servicedesk;
import java.math.BigDecimal;
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import org.cuckoo.core.ScheduledAction;
import org.cuckoo.core.ScheduledActionContext;
import com.sun.jmx.snmp.Timestamp;
import br.com.sankhya.extensions.actionbutton.AcaoRotinaJava;
import br.com.sankhya.extensions.actionbutton.ContextoAcao;
import br.com.sankhya.jape.dao.JdbcWrapper;
import br.com.sankhya.modelcore.PlatformService;
import br.com.sankhya.modelcore.PlatformServiceFactory;
import br.com.sankhya.modelcore.PlatformServiceFactory.ServiceDescriptor;
import br.com.sankhya.modelcore.util.EntityFacadeFactory;
public class ScheduleGeraEDI implements ScheduledAction {
       public void onTime(ScheduledActionContext contexto) {
                     try{
                           //Para que seja possível preencher os parâmetros sem a interface com o usuário
                                       //criamos uma colection e preenchemos essa colection com cada
parâmetro de cada
                            //"registro" (chamo de registro a configuração de linha do arquivo).
                      Collection<Map<String, Object>> params = new ArrayList<Map<String, Object>>();
                                     //O primeiro "registro" é o 1.02.00, ele usa duas variáveis: "DATA INICIO"
e "DATA FINAL"
                            params.add(buildParam(10200, "DATA INICIO", "01/04/2016"));
                            params.add(buildParam(10200, "DATA FINAL", "30/04/2016"));
                                         //O segundo "registro" é o 1.03.00, esse usa "DATData Inicial" e
 "DATData Inicial"
                            params.add(buildParam(10300, "DATData Inicial", "01/04/2016"));
                            params.add(buildParam(10300, "DATData Final", "30/04/2016"));
                            //e segue...
                            params.add(buildParam(10400, "DATData Inicial", "01/04/2016"));
                            params.add(buildParam(10400, "DATData Final", "30/04/2016"));
                            params.add(buildParam(10500, "DATData Inicial", "01/04/2016"));
                            params.add(buildParam(10500, "DATData Final", "30/04/2016"));
                            params.add(buildParam(10600, "DATData Inicial", "01/04/2016"));
                            params.add(buildParam(10600, "DATData Final", "30/04/2016"));
                                                                                                        PlatformService ps =
                            PlatformServiceFactory.getInstance().lookupService(
                            "@core:edi.comercial.service");
                            ps.set("codLayout", new BigDecimal(10000));
                            ps.set("parametros", params);
                            ps.set("caminhoRepositorio", "IntercambioEletronico/relatorio10000");
                            ps.set("emails", "hamir@hamir.com.br,jose@jose.com.br");
                            /*Descomente se for usar FTP
                            ps.set("caminhoFTP", "arquivos/edi/relatorio10000");
                            ps.set("enderecoFTP", "ftp://meuftp.com.br");
                            ps.set("usuarioFTP", "hamir");
                            ps.set("senhaFTP", "123456");
                             */
                              ps.execute();
                            } catch (Exception e){
                            RuntimeException re = new RuntimeException(e);
                            throw re;
                     }
                 }
               //Esse método serve só pra agilizar a criação da Map, pois como cada parâmetro
               //precisa de 3 informações, ficaria extenso escrever linha a linha
              private Map<String, Object> buildParam(long codigo, String nome, Object valor)
              {
                     Map<String, Object> param = new HashMap<String, Object>();
                     param.put("codigo", new BigDecimal(codigo));
                     param.put("nome", nome);
                     param.put("valor", valor);
                     return param;
                }
}
```

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110653-A%C3%A7%C3%B5es-Agendadas#top)
