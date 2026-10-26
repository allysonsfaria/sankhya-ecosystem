---
id: "4406748820503"
titulo: "Importação automática de marcações de relógios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4406748820503-Importa%C3%A7%C3%A3o-autom%C3%A1tica-de-marca%C3%A7%C3%B5es-de-rel%C3%B3gios"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:00Z"
rotulos: ["Configuração", "Agendamento", "Importação", "Importação Automática de Batidas de Ponto", "Henry", "Relógios"]
---

# Importação automática de marcações de relógios

(1)** Relógios:** Henry, modelos Hexa e Prisma SF

O Sistema passa a ter a funcionalidade de realizar importações automáticas e periódicas das batidas dos relógios de ponto, permitindo ao cliente escolher se deseja que as coletas sejam realizadas conforme o critério temporal que lhe for conveniente.

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16373079423383) OBSERVAÇÃO:**

A princípio somente empresas que utilizam REPs da Henry, modelos Hexa e Prisma SF. Demais fabricantes estão em análise para demanda.

#### Passo a passo da Instalação:

**![Imagem 2: Cadastro do(s) Equipamento(s):](https://ajuda.sankhya.com.br/hc/article_attachments/16373079429655) Cadastro do(s) Equipamento(s):**

![Imagem 3: Cadastro do(s) Equipamento(s):](https://ajuda.sankhya.com.br/hc/article_attachments/4406756344215)

**Código:** código de identificação do REP. Pode ser gerado automaticamente ou inserido pelo usuário, de acordo com a opção do menu do botão direito;
**Empresa:** neste campo selecione a empresa responsável que receberá os apontamentos provenientes do relógio;
**Marca e modelo:** são os modelos de relógio homologados pelo MTE/Inmetro. **Importante:** somente o modelo Henry, modelos Hexa e Prisma SF estão disponíveis  para seleção;
**Nro de Fabricação:** código de fabricação do REP, devendo ser preenchido de acordo com o manual do fornecedor;
**Ativo:** define se a configuração está ativa conforme dados de preenchimento, se desmarcada a opção, não será realizada a comunicação com relógio;
**Endereço de IP / Porta TCP:** dados de configuração de preenchimento pelo responsável pelo TI;

**NSR Prox Coleta:** número sequencial correspondente à última coleta realizada, para este campo inicialmente será preenchido com valor referente a última importação.

#### Habilita Horário de Verão?

Com esta opção marcada, deverá agendar as datas em que ocorrerá a mudança de horários. Com a opção desmarcada permanece com o horário independente da mudança se houver, sendo alterada apenas pelo envio de Data/Hora.

#### Requer Autenticação?

Opção de validação para controle e criptografia do REP. Dados disponíveis na instalação do REP.

**Coletar Eventos:** com esta opção o usuário obtém no momento os apontamentos. ‘coletar agora’
**Enviar Data/Hora:** com esta opção é possível consolidar o horário do servidor com REP. Atualizando o horário atual com o equipamento.

**![Imagem 4: Cadastro da frequência no Agendador de comunicação:](https://ajuda.sankhya.com.br/hc/article_attachments/16373079433623) Cadastro da frequência no Agendador de comunicação:**

![Imagem 5: Cadastro da frequência no Agendador de comunicação:](https://ajuda.sankhya.com.br/hc/article_attachments/4406750216215)

**Tarefa:** código sequencial gerado pelo sistema;
**Descrição da Tarefa:** descrição correspondente a tarefa/agendador de acordo com critério do usuário
Email do responsável;
**Frequência:** campo que deverá ser configurado o momento em que serão executadas as tarefas;
**Horários:** neste campo configura o horário da tarefa;
**Data da próxima Execução:** data que ocorrerá a próxima execução;
**Data da** **última** **Execução:** data da última execução da tarefa;

**Equipamentos incluídos no Agendamento:** consolida ou não em um mesmo agendador os equipamentos configurados de empresas diversas;
**Tarefas do Agendamento:** configura se será exercida a opção de coleta de marcações e envio de data e horas.

**![Imagem 6: Baixar o Tarefas.exe, e configurar de forma que inicie automaticamente:](https://ajuda.sankhya.com.br/hc/article_attachments/16373079440407) Baixar o Tarefas.exe, e configurar de forma que inicie automaticamente:**

![Imagem 7: Baixar o Tarefas.exe, e configurar de forma que inicie automaticamente:](https://ajuda.sankhya.com.br/hc/article_attachments/4406901050647)

Este aplicativo gerencia tarefas que são agendadas nos aplicativos MGE.

Objetivo do EXE em sintonia com a Rotina implementada de automação dos apontamentos é executar as tarefas previamente agendadas  no menu; **Avançado > Agendadores > Agendador** **para comunicação com REPs.**

O Tarefas.exe é um aplicativo que deverá estar em execução para processamento das rotinas agendadas (AGENDADORES). Deve ser instalado no servidor e ficar sempre em execução, pois será feita a verificação de agendamento a cada ‘X’ minutos, de acordo com a definição do “Intervalo de Execução”. Tal aplicação pode ser baixada pelo Sankhya Place.

Na Rotina: ao clicar em Coletar eventos é apresentada a mensagem informando a ação: Em caso de Sucesso.  “ Sucesso! / Erros”  (em caso de erro apresenta mensagem).
