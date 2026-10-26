---
id: "7869194336407"
titulo: "Geração ISS Agendamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Apuração e Livros Fiscais > Escrituração dos livros"
atualizado_em: "2026-09-28T11:41:08Z"
rotulos: ["ISS", "Configuração", "Livros Fiscais", "Agendamento", "br.com.sankhya.mgeliv.geracao.iss.agendamento", "Prefeituras", "Horários e Frequência: Defina datas e periodicidade", "Agendamento: Configuração e ativação", "Parâmetros: Informe empresas; escolha tipo de nota e filtros"]
---

# Geração ISS Agendamento

| ```  Módulo: Livros Fiscais > Arquivos          Versão disponível: A partir da 4.14 ``` |
| --- |

---

Através dessa tela, você tem a função de agendamento para a geração das notas para o livro de ISS Serviços Tomados e Serviços Prestados, automaticamente, conforme as parametrizações feitas.

O agendamento respeita o parâmetro LIVISSPAGINADO. Com ele habilitado, a geração agendada também é executada de forma paginada.

Acesse os links a seguir para saber mais sobre essa tela:

| [Preenchimentos iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#preenchimentosiniciais) | [Aba Horários](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#abahorrios) |
| --- | --- |
| [Aba Frequência Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#abafrenqunciaagendamento) | [Aba Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#abapar%C3%A2metros) |
| [Aba Histórico](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#abahist%C3%B3rico) | [Botão Executar Agora](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#bot%C3%A3oexecutaragora) |

### Preenchimentos iniciais

![Imagem 1: Preenchimentos iniciais](https://ajuda.sankhya.com.br/hc/article_attachments/7869738212119)

O campo**"Nro. agendamento"**é de numeração automática.

Informe no campo **"Descrição agendamento"** um nome para identificar o agendamento que está sendo cadastrado. Esse campo é de preenchimento obrigatório.

O campo **"Status Última Execução"** é atualizado automaticamente com o status da última execução do agendamento.

A marcação **"Ativo"** define se o agendador está ou não disponível.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#top)

### Aba Horários

![Imagem 2: Aba Horários](https://ajuda.sankhya.com.br/hc/article_attachments/7870092143255)

No campo **"Próxima execução em"** você agenda a data e hora da próxima execução, podendo ser inclusive para forçar uma execução imediata.

Na **"Data Final de execução"** informe uma data e hora limite para execução do agendamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#top)

### Aba Frequência Agendamento

Nessa aba você define quando será a **"1ª execução"** e a frequência em que o agendador será executado, sendo **"Diário"**, **"Semanal"** ou **"Mensal"**.

**Importante:** deve ser definido ao menos um horário e mês para execução.

![Imagem 3: Importante: deve ser definido ao menos um horário e mês para execução.](https://ajuda.sankhya.com.br/hc/article_attachments/7870237355287)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#top)

### Aba Parâmetros

![Imagem 4: Aba Parâmetros](https://ajuda.sankhya.com.br/hc/article_attachments/7870255025559)

Inicialmente, você deve informar a **"Empresa"** e a **"Empresa Destinatária"**, ou seja, a empresa pela qual realizou a emissão das notas.

Se a marcação **"Gerar notas com ISS zerado"** estiver habilitada, o sistema buscará as notas que possuem a configuração para serem geradas no livro, ainda que elas não tenham item de serviço. Sendo assim, as notas que ainda não foram geradas, irão para o livro com apenas um item e os campos **"Base"**, **"Alíquota"** e **"Valor ISS"** zerados.

**Seção Ações**

Nessa seção, determine os conjuntos de dados relacionados às notas que serão gerados, podendo definir dentre as seguintes marcações:

- **Gerar Notas:** Serão geradas todas as informações referentes às notas dentro do período estabelecido.
- **Gerar Canceladas:** Com essa marcação feita, serão consideradas apenas as notas canceladas dentro do período definido.
- **Gerar Financeiro:** Será considerado para geração apenas o financeiro das notas contidas no período estabelecido.
- **Gerar Redução Z:** Serão gerados os fechamentos fiscais diários de um ECF (Emissor de Cupom Fiscal), visto que este trabalha com base em movimentações diárias.

![Imagem 5: Você deve escolher pelo menos uma ação para efetuar a geração dos registros.](https://ajuda.sankhya.com.br/hc/article_attachments/16313902760471) Você deve escolher pelo menos uma ação para efetuar a geração dos registros.

**Observação:** quando as marcações **"Gerar Notas"** e **"Gerar Canceladas"** estão efetuadas, **"Aquisições"** e/ou **"Prestações"** também devem estar realizadas.

**Seção Filtros**

Nessa seção você deve determinar qual operação será considerada para geração dos dados. Você pode marcar uma ou ambas as opções:

- **Aquisições:** Serão considerados apenas os serviços adquiridos (entrada);
- **Prestações:** É feita a busca pelos serviços fornecidos (saída).

**Seção Data Inicial**

Nessa seção você escolhe se a data inicial será por **"Ult. Execução"**, **"Hoje"**, **"1º dia do mês"** ou **"Ult. dia do mês"** e ainda os **"Dias p/ somar na data inicial"**.

**Seção Data Final**

Nessa seção você informa se a data final será **"Hoje"** ou **"Ult. dia do mês"** bem como os **"Dias p/ somar na data final"**.

**Seção Histórico**

Através dessa seção você define quantos dias deseja manter as informações do histórico.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#top)

### Aba Histórico

Aqui, você pode acompanhar o histórico com as informações básicas de execução dos reajustes realizados a partir dos agendamentos programados.

![Imagem 6: Aqui, você pode acompanhar o histórico com as informações básicas de execução dos reajustes realizados a partir dos…](https://ajuda.sankhya.com.br/hc/article_attachments/7870342047383)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#top)

### Botão Executar Agora

Ao acionar o botão **"Executar Agora"** será apresentado o pop-up abaixo para que seja processada a geração do livro ISS:

[GIF animado: Imagem 7: Ao acionar o botão "Executar Agora" será apresentado o pop-up abaixo para que seja processada a geração do livro ISS:](https://ajuda.sankhya.com.br/hc/article_attachments/7887712161175)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/7869194336407-Gera%C3%A7%C3%A3o-ISS-Agendamento#top)

---

**![Imagem 8: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16313919113111) Acesse também:**

[Geração ISS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607514-Gera%C3%A7%C3%A3o-ISS)
