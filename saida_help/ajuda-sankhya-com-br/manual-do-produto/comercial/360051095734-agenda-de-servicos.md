---
id: "360051095734"
titulo: "Agenda de Serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-01T01:37:42Z"
rotulos: ["Configuração", "Parceiro", "Faturamento", "ACEITACGCBRANCO", "br.com.sankhya.com.mov.agenda.servicos", "VISUSUAGE", "HISTAGETMKT", "PAREXECASSESSOR", "Agenda de Serviços", "Funcionalidades: Agendamento Faturamento Indicadores", "Configurações Necessárias: Usuários Acessos Preferências da Empresa", "Comercial"]
---

# Agenda de Serviços

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312182785303) Módulo: Comercial > Rotinas
```

---

Por meio da Agenda de Serviços, pode-se realizar operações básicas de agendamento de serviços e faturamento dos serviços no **Sankhya Om**. Com isso, será possível colher informações para indicadores que apoiarão a tomada de decisões da organização.

| Funcionalidades da tela: | |
| --- | --- |
| [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#cadastrodeusurios) | [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#controledeacessos) |
| [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#prefernciasdaempresa) | [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#cadastrodeparceiros) |
| [Cadastro de Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#cadastrodevendedorescompradores) | [Cadastro de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#cadastrodeservios) |
| [Parâmetros que influenciam na rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#par%C3%A2metrosqueinfluenciamnarotina) |  |

---

![Imagem 2: Parâmetros que influenciam na rotina](https://ajuda.sankhya.com.br/hc/article_attachments/1500007627022)

### Cadastro de Usuários

A utilização da Agenda de Serviços tem seu uso vinculado ao usuário e à empresa a qual ele pertence. O agendamento de serviços poderá ser realizado apenas para a empresa do usuário logado. Esse vínculo é realizado por meio da tela [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios), na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), campo **"Empresa"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)

### Controle de Acessos

Para completa utilização da Agenda de Serviços, alguns acessos especiais precisam ser liberados na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos). Nessa configuração, as ações de **"Incluir"**, **"Alterar"** e **"Excluir"** se referem ao agendamento.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)

### Preferências da Empresa

Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa) acesse a aba **"Agenda de Serviços"**; as configurações aqui realizadas serão utilizadas diretamente pela Agenda.

Os campos **"Hora inicial"** e **"Hora final"** se referem ao horário de funcionamento da empresa. Para excluir os dias de descanso da agenda (sábado e domingo, por exemplo), deve-se configurar a carga horária padrão dos funcionários. Os valores possuem um valor padrão, mas podem ser alterados.

A informação inserida no campo **"Modelo de notas e pedidos"** considera um modelo cadastrado na tela [Modelo de Notas e Pedidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051706514-Modelo-de-Notas-e-Pedidos) para o faturamento do atendimento do serviço. Nesse ponto, é importante configurar todos os dados que serão utilizados para preenchimento do cabeçalho da nota. Não é possível faturar o serviço se este campo não for preenchido.

O **"Cód. perfil"** é definido para que na Agenda seja possível agendar eventos somente de parceiros/clientes que possuam o mesmo perfil da empresa.

No campo **"Minutos p/ módulo"** determine o período de intervalo da agenda, de modo que, por exemplo:, se o módulo for de 15 minutos, a hora na Agenda de Serviços será dividia em quatro blocos de 15 minutos.

Essa informação exerce influência também no cálculo da quantidade de módulos de um serviço onde, no agendamento, o sistema utiliza o campo **"Tempo Estimado"** do [Cadastro de Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), dividido pela quantidade de minutos configurados nesse campo; caso existam casas decimais, o arredondamento será feito para cima, assim compõe-se a quantidade de módulos do serviço. Por exemplo:

O módulo é de 30 minutos e o tempo estimado do serviço é 45 minutos, portanto, o sistema irá considerar 2 módulos.

Informe em **"Limite de dias p/ histórico"** a quantidade de dias que será feita a busca pelo histórico na Agenda. O período de busca considera a data atual com limite no valor estipulado neste campo.

Quando a marcação **"CPF obrigatório"** for ligada, será definido que, ao criar um cliente através da tela de [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento), o CPF será obrigatório. Caso essa marcação esteja desligada, o sistema verificará o parâmetro **"Aceita CGC/CPF de Parceiro em branco? - ACEITACGCBRANCO"**. Essa validação também é feita no momento de geração da fatura para o cliente, onde será verificado se este possui ou não CPF.

A seção **"Configuração de cores p/ eventos"** determina como cada evento será exibido na tela principal da Agenda. Ela é inicialmente preenchida com cores padrão, porém pode ser modificada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)

### Cadastro de Parceiros

Na tela [Cadastro Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) configure o **"Perfil Principal"** de cada parceiro, sendo importante a informação de que serão apresentados na Agenda apenas os parceiros que possuírem o mesmo Perfil Principal configurado na tela Preferências da Empresa, aba Agenda de Serviços, campo Cód. perfil.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)

### Cadastro de Vendedores/Compradores

A configuração efetuada nessa tela, é a que define quais são os responsáveis pela execução dos serviços agendados.

Para estarem disponíveis, deve ser informada na aba **"Geral"** a **"Empresa"** e, na tela Cadastro de Parceiros, aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abaidentificao), o campo **"Executante"** ou **"Assessor"** também devem ser preenchidos.

**Observação:** através do parâmetro **"Parceiro utiliza executante ou assessor? - PAREXECASSESSOR"** é possível alterar a descrição do campo tipo Executante para Assessor.

![Imagem 3: Atente-se também para a carga horária do executante, pois isso limitará os horários de agendamento e atendimento dos…](https://ajuda.sankhya.com.br/hc/article_attachments/21002689199511) Atente-se também para a carga horária do executante, pois isso limitará os horários de agendamento e atendimento dos serviços, por exemplo, 44 horas semanais com folgas aos domingos e segundas-feiras.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)

### Cadastro de Serviços

Nessa tela, na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o#abageral), realize a definição do **"Tempo estimado"** para a execução do serviço. O tempo aqui informado irá impactar na quantidade de módulos reservados no agendamento. Considere o seguinte exemplo:

Se o módulo é 30 minutos, e o tempo estimado do serviço é de 15 minutos, o sistema irá reservar um módulo.

Na aba **"Agenda de Serviços"**, a marcação **"Fixar na Agenda"** não deve estar efetuada caso o serviço possua algum impedimento e não possa ser realizado conforme os períodos de um evento fixo. Em casos, por exemplo, em que o serviço só pode ser executado por um profissional específico que colabora na empresa uma vez ao mês; neste caso a opção deve estar desmarcada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)

### Parâmetros que influenciam na rotina

**Abrir Telemarketing a partir da Agenda de Serviço - HISTAGETMKT:**com esse parâmetro ligado, será disponibilizado o botão ![Imagem 4: Abrir Telemarketing a partir da Agenda de Serviço - HISTAGETMKT: com esse parâmetro ligado, será disponibilizado o…](https://ajuda.sankhya.com.br/hc/article_attachments/21002689205399) **"Histórico Telemarketing"**, ao criar um novo evento nessa tela quando há um Parceiro e Serviço cadastrados. Por meio desse botão, é possível consultar o histórico de atendimentos de determinado Parceiro na tela [Telemarketing](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604514).

**Visualizar Ag. Serviço de usuários de outras emp. - VISUSUAGE:** quando ligado, pode-se visualizar a agenda dos [Vendedores/Compradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111133-Vendedores-Compradores) de outras empresas, independente da **"Empresa"** e **"Vendedor"** vinculados na tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874). Assim, na tela [Preferencias da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), as configurações dos campos **"Hora inicial"**, **"Hora final"**, **"Cód. Perfil"** e **"Minutos por Módulos"** sofrerão determinadas alterações, sendo elas:

- Os campos Hora inicial e Hora final utilizarão a menor hora inicial e a maior hora final para serem exibidas na Agenda de Serviços;
- O Cód. Perfil será ignorado no momento da busca do parceiro de um novo evento, ou seja, todos os parceiros clientes serão carregados;
- O campo Minutos por Módulos da Empresa também será ignorado, e o menor tempo previsto será apresentado, sendo ele, de 15 minutos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051095734-Agenda-de-Servi%C3%A7os#top)
