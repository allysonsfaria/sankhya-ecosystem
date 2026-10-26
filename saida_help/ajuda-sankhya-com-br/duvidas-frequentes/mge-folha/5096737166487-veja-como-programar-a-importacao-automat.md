---
id: "5096737166487"
titulo: "Veja como programar a Importação automática de marcações dos relógios de ponto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5096737166487-Veja-como-programar-a-Importa%C3%A7%C3%A3o-autom%C3%A1tica-de-marca%C3%A7%C3%B5es-dos-rel%C3%B3gios-de-ponto"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:36Z"
rotulos: ["Configuração", "Agendamento", "Importação", "não apagar", "Agende frequências e horários no sistema.", "Cadastre equipamentos e configure dados.", "Instale e mantenha Tarefas.exe em execução.", "Relógio de Ponto", "Henry"]
---

# Veja como programar a Importação automática de marcações dos relógios de ponto

**Relógios:** Henry, modelos Hexa e Prisma SF

O Sistema passa a ter a funcionalidade de realizar importações automáticas e periódicas das batidas dos relógios de ponto, permitindo ao cliente escolher se deseja que as coletas sejam realizadas de acordo com o critério temporal que lhe for conveniente.

**Observação:** a priori somente empresas que utilizam REPs da Henry, modelos Hexa e Prisma SF. Demais fabricantes estão em análise para demanda.

Passo a passo da Instalação:

![Imagem 1: Cadastre o(s) Equipamento(s):](https://ajuda.sankhya.com.br/hc/article_attachments/16347885334295) Cadastre o(s) Equipamento(s):

![Imagem 2: Cadastre o(s) Equipamento(s):](https://ajuda.sankhya.com.br/hc/article_attachments/5100644035479)

(1)** Código:** código de identificação do REP. Pode ser gerado automaticamente ou inserido pelo usuário, de acordo com a opção do menu do botão direito.

(1)** Empresa:** neste campo, selecione a empresa responsável que receberá os apontamentos provenientes do relógio.

(1)** Marca e modelo:** são os modelos de relógio homologados pelo MTE/Inmetro.

**Importante:** somente o modelo Henry, modelos Hexa e Prisma SF está disponível para seleção.

(1)** Nro de Fabricação:** código de fabricação do REP, deve ser preenchido de acordo com o manual do fornecedor.

(1)** Ativo:** defina se a configuração está ativa conforme dados de preenchimento, se desmarcada a opção, não será realizada a comunicação com relógio

(1)** Endereço de IP / Porta TCP:** dados de configuração de preenchimento pelo responsável pelo TI.

(1)** NSR Prox Coleta:** número sequencial correspondente à última coleta realizada, para este campo inicialmente será preenchido com valor referente a última importação.

(1)** Habilita Horário de Verão?:** com esta opção marcada, agende as datas em que ocorrerá a mudança de horários. Com a opção desmarcada permaneça com o horário independente da mudança se houver, sendo alterada apenas pelo envio de Data/Hora.

(1)** Requer Autenticação?:**opção de validação para controle e criptografia do REP. Dados disponíveis na instalação do REP.

(1)** Coletar Eventos:** com esta opção o usuário obtém no momento os apontamentos. ‘coletar agora’;

**Enviar Data/Hora:** com esta opção é possível consolidar o horário do servidor com REP. atualizando o horário atual com o equipamento.

![Imagem 3: Cadastro da frequência no Agendador de comunicação:](https://ajuda.sankhya.com.br/hc/article_attachments/16348175768855) Cadastro da frequência no Agendador de comunicação:

![Imagem 4: Cadastro da frequência no Agendador de comunicação:](https://ajuda.sankhya.com.br/hc/article_attachments/5100927348631)

(1)** Tarefa:** código sequencial gerado pelo sistema;

(1)** Descrição da Tarefa:** descrição correspondente a tarefa/agendador de acordo com critério do usuário;

(1)** Email do responsável;**

(1)** Frequência:** campo que deverá ser configurado no momento em que serão executadas as tarefas;

(1)** Horários:** neste campo configure o horário da tarefa;

(1)** Data da próxima Execução:** data que ocorrerá a próxima execução;

(1)** Data da ùltima Execução:** data da última execução da tarefa;

(1)** Equipamentos incluídos no Agendamento:** Consolida ou não em um mesmo agendador os equipamentos configurados de empresas diversas;

(1)** Tarefas do Agendamento:** Configura se será exercido a opção de coleta de marcações e envio de data e horas.

![Imagem 5: Baixe o Tarefas.exe e configure de forma que inicie automaticamente:](https://ajuda.sankhya.com.br/hc/article_attachments/16348192749847) Baixe o Tarefas.exe e configure de forma que inicie automaticamente:

![Imagem 6: Baixe o Tarefas.exe e configure de forma que inicie automaticamente:](https://ajuda.sankhya.com.br/hc/article_attachments/5100986566935)

Este aplicativo **gerencia** tarefas que são agendadas nos aplicativos MGE.

Objetivo do EXE em sintonia com a Rotina implementada de automação dos apontamentos é executar as tarefas previamente agendadas no **menu**; Avançado > Agendadores > Agendador para comunicação com REPs.

O Tarefas.exe é um aplicativo que deverá estar em execução para processamento das rotinas agendadas (AGENDADORES). Deve ser **instalado** **no** **servidor** e ficar **sempre** **em** **execução**, pois fará verificação de agendamento a cada ‘X’ minutos, de acordo com a definição do “**Intervalo** **de** **Execução**”.

Na Rotina, ao clicar em Coletar eventos é apresentado mensagem informando a ação: “ Sucesso! / Erros” (em caso de sucesso ou erro apresenta mensagem).
