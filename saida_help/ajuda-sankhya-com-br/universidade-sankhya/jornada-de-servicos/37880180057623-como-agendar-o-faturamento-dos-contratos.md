---
id: "37880180057623"
titulo: "Como agendar o faturamento dos contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880180057623-Como-agendar-o-faturamento-dos-contratos"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:40Z"
rotulos: ["Configuração", "Contrato", "Agendamento", "Financeiro", "NFS-e"]
---

# Como agendar o faturamento dos contratos

| Categoria |
| --- |
|  |

## Agendador de faturamento

#### O que é e como funciona essa operação?

O agendamento de faturamento é uma forma de deixar o processo automático. Em vez de entrar todo mês na tela de faturamento para gerar as notas dos contratos, você pode configurar uma programação e deixar que o sistema faça isso sozinho. Você escolhe quando e com que frequência o faturamento deve acontecer (por exemplo, todo dia 1º de cada mês), define as regras que devem ser seguidas e pronto: o sistema roda no dia e horário definidos, gera as notas e os valores a receber.

Depois, é possível acompanhar o que foi faturado, se houve algum erro e quais contratos foram incluídos no processo. Isso ajuda a garantir que tudo aconteça no prazo, com menos esforço da equipe.

#### Quais problemas essa prática resolve?

- Trabalho repetitivo de faturar contratos manualmente todo mês
- Risco de atrasos ou esquecimentos no faturamento
- Dependência de alguém estar disponível no dia certo para executar a rotina
- Falta de padronização no processo, gerando erros e retrabalho

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103874792)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: A Axis possui muitos contratos de manutenção recorrente com diferentes redes varejistas. Todo início de mês, o responsável pelo financeiro precisa acessar o sistema, aplicar filtros e faturar esses contratos manualmente, um por um.

Para ganhar tempo e evitar esquecimentos, a diretoria decidiu automatizar esse processo com um agendamento de faturamento. A tarefa será programada para rodar no dia 1º de cada mês, às 7h da manhã, gerando automaticamente as notas dos contratos que estiverem prontos para faturar.

**Tarefas**: Sua tarefa é configurar um agendador para faturar os contratos da Axis de forma automática todo mês.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Criação do agendador para faturamento de contratos:**

- Acesse a tela **Agendador para Faturamento de Contratos**
  Menu: Contratos e Serviços » Avançado
- Clique em **+ Novo registro** para iniciar o lançamento e preencha as informações abaixo no **Painel Principal**
- **Descrição agendamento -** Agendamento para faturamento
- **Ativo -** Marcado

Aba **Frequência Agendamento**

- **1ª execução -** 07:00
- **Meses -** Marque todos
- Selecione a opção **Mensal** e marque para o faturamento ocorrer sempre no dia **1** de cada mês

Aba **Filtros/Parâmetros Obrigatórios**

- **Considerar Contatos/Perfil/Serviço -** Marcado
- **Tipo de Operação -** VENDA NFS-E
- **Tipo de Título -** 1
- **Tipo de Negociação -** 16
- **Observação Padrão -** 0
- **Mês para Referência -** Mês do faturamento

Aba **Configurações**

- Utilize essa aba para definir quais as configurações devem ser consideradas no faturamento dos contratos
- Salve as informações
- Acompanhe a execução pela aba **Histórico.**

#### Correção e Repetição

- Verifique se todos os campos foram preenchidos para o faturamento ocorrer corretamente.
- Esteja sempre acompanhando os faturamentos pela aba **Histórico** para realizar correções se for necessário.
