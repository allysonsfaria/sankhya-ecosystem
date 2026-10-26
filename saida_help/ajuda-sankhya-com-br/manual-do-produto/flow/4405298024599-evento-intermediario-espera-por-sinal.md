---
id: "4405298024599"
titulo: "Evento intermediário espera por sinal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298024599-Evento-intermedi%C3%A1rio-espera-por-sinal"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:09:43Z"
rotulos: ["Configuração", "Eventos", "Movimentação Financeira", "Financeiro", "sankhyaflow", "Evento intermediário espera por sinal", "Evento Intermediário: Interrompe fluxo até sinal", "Exemplo: Adiantamento de viagens"]
---

# Evento intermediário espera por sinal

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313306990359) Versão: a partir da 4.3
```

---

O Evento intermediário espera por sinal interrompe o fluxo do processo até a chegada de um sinal.

Ao integrar o processo com outras rotinas do ERP, como, por exemplo, em uma empresa de desenvolvimento de software existe um processo de correção de erros do sistema, em que, após a correção ser realizada, ela deverá ser oficializada em um pacote para ser disponibilizado ao cliente, que é realizada por um outro software. Nesse momento, o processo é interrompido até que a correção seja oficializada nesse pacote.

Assim, quando as tarefas são concluídas nessa segunda aplicação, um sinal é enviado ao SankhyaFlow para continuar o processo.

Outro exemplo são os processos que precisam aguardar a baixa de um título financeiro para dar continuidade na sua execução.

Para demonstrar essa funcionalidade, iremos utilizar como caso de uso o processo de [Adiantamento de viagens](https://drive.google.com/file/d/1RA3c5e-tg_rcHX3LhI_xnspczoYbiv2T/view):

![Imagem 2: Para demonstrar essa funcionalidade, iremos utilizar como caso de uso o processo de Adiantamento de viagens :](https://ajuda.sankhya.com.br/hc/article_attachments/4405303344663)

| **Processo de Adiantamento de viagens** |
| --- |

Esse processo permite que qualquer colaborador solicite um adiantamento de viagem para a empresa, que poderá ser aprovado ou reprovado pelo seu líder imediato.

Caso seja aprovado, dois títulos serão gerados automaticamente: receita e despesa. O título de despesa representa o desembolso financeiro que a empresa fará ao colaborador, através de uma transferência bancária, dinheiro, etc, e o título de receita será utilizado para basear a compensação financeira após o acerto de despesas.

Em seguida, o solicitante receberá um e-mail informando que sua solicitação foi aprovada e que em breve o dinheiro será disponibilizado. Nesse momento o processo é interrompido até que o financeiro faça a baixa do título de despesa. Quando for executada essa baixa, um sinal é enviado ao SankhyaFlow para continuar o processo.

---

No decorrer dessa documentação, demonstraremos como inserir o evento no processo e como personalizá-lo.

Para inserir o evento no processo, basta selecionar uma tarefa qualquer no diagrama do processo; assim, será apresentada uma caixa com várias opções, dentre elas, selecione **"Adicionar evento intermediário"** ou busque pelo elemento **"Criar evento intermediário"** dentro da paleta localizada no lado esquerdo:

[GIF animado: Imagem 3: Para inserir o evento no processo, basta selecionar uma tarefa qualquer no diagrama do processo; assim, será…](https://ajuda.sankhya.com.br/hc/article_attachments/4405298406551)

| **Inserção de Evento intermediário espera por sinal no processo** |
| --- |

Em seguida, com o evento selecionado, clique no ícone **"Alterar tipo"**  e selecione o **"Evento intermediário espera por sinal"**:

[GIF animado: Imagem 4: Em seguida, com o evento selecionado, clique no ícone "Alterar tipo" e selecione o "Evento intermediário espera por…](https://ajuda.sankhya.com.br/hc/article_attachments/4405298453527)

| **Inserção de Evento intermediário espera por sinal no processo** |
| --- |

Ao inserir esse evento no processo, você deve informar o **"Nome do Sinal"** pois o utilizaremos em sua personalização.

![Imagem 5: Ao inserir esse evento no processo, você deve informar o "Nome do Sinal" pois o utilizaremos em sua personalização.](https://ajuda.sankhya.com.br/hc/article_attachments/4405298467223)

| **Inserção Nome do Sinal** |
| --- |

**Observação:** o elemento sinal deve possuir um nome único, pertencente àquela abertura de processo em específico, para que possa enviar o sinal correto e dar continuidade ao fluxo certo.

A personalização do evento precisa implementar a chamada do método **sendSignal**, pertencente ao pacote **br.com.sankhya.workflow.api.SankhyaFlow**, que pode ser obtido a partir dessa [biblioteca](https://drive.google.com/file/d/1ZUS04jMHlmZ9gHRUkehgtUJiE2FAIP08/view?usp=sharing).

**Nota:** o Evento de sinal pode ser implementado através de uma personalização (Rotina Java) no Sankhya Om (evento programado, botão de ação, etc).

Abaixo, segue o exemplo de um evento programado para o nosso caso de uso, onde a baixa do título de despesa do adiantamento envia o sinal **"baixouTítulo"** ao processo:

| ``` import br.com.sankhya.extensions.eventoprogramavel.EventoProgramavelJava; import br.com.sankhya.jape.event.PersistenceEvent; import br.com.sankhya.jape.event.TransactionContext; import br.com.sankhya.jape.sql.NativeSql; import br.com.sankhya.jape.vo.DynamicVO; //Biblioteca de APIs do SankhyaFlow import br.com.sankhya.workflow.api.SankhyaFlow; import java.math.BigDecimal; import java.sql.ResultSet; import java.sql.Timestamp; import java.util.ArrayList; import java.util.List; public class SinalBaixarTitulo implements EventoProgramavelJava { public void afterDelete(PersistenceEvent arg0) throws Exception {} public void afterInsert(PersistenceEvent event) throws Exception {} public void afterUpdate(PersistenceEvent event) throws Exception { DynamicVO financeiro = (DynamicVO)event.getVo(); BigDecimal nufin = financeiro.asBigDecimal("NUFIN"); Timestamp dhbaixa = financeiro.asTimestamp("DHBAIXA"); if (dhbaixa != null) { List<String> idIstPrn = new ArrayList<String>(); NativeSql query = null; try { query = new NativeSql(event.getJdbcWrapper()); query.appendSql("SELECT IDINSTPRN FROM AD_SOLICITACAOADIANTAMENTO WHERE NUFIN_AD_D = :NUFIN"); query.setNamedParameter("NUFIN", nufin); ResultSet rs = query.executeQuery(); while (rs.next()) idIstPrn.add(rs.getBigDecimal("IDINSTPRN").toString());  } finally { NativeSql.releaseResources(query); }  String[] instancias = idIstPrn.<String>toArray(new String[0]); //Método 'sendSignal' passando o nome do sinal e as instâncias de processo SankhyaFlow.sendSignal("baixouTitulo", instancias); }  } public void beforeCommit(TransactionContext arg0) throws Exception {} public void beforeDelete(PersistenceEvent arg0) throws Exception {} public void beforeInsert(PersistenceEvent arg0) throws Exception {} public void beforeUpdate(PersistenceEvent arg0) throws Exception {} } ``` |
| --- |

Após a implementação da personalização, é gerado o módulo Java e então, ele é vinculado na aba Eventos da tabela TGFFIN.

![Imagem 6: A(s) instância(s) do processo de Adiantamento de viagem será(ão) automaticamente interrompida(s) no momento que chegar…](https://ajuda.sankhya.com.br/hc/article_attachments/16092588076183) A(s) instância(s) do processo de Adiantamento de viagem será(ão) automaticamente interrompida(s) no momento que chegar no evento de sinal **"Aguardar baixa de título"** e somente será retomado quando o financeiro executar a baixa dos títulos de despesas.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405298024599-Evento-intermedi%C3%A1rio-espera-por-sinal#top)
