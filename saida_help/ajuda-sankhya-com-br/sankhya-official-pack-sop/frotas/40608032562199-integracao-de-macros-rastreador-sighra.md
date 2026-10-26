---
id: "40608032562199"
titulo: "Integração de Macros - Rastreador SIGhRA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40608032562199-Integra%C3%A7%C3%A3o-de-Macros-Rastreador-SIGhRA"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T13:27:15Z"
rotulos: ["Configuração", "Transporte", "Integração", "Macros", "Integração de Macros", "Rastreador SIGhRA", "Veículos ao rastreador", "Macros integradas", "Logs de chamadas á API", "Configurações Gestão Frotas", "SIGhRA", "Gestão de Frotas"]
---

# Integração de Macros - Rastreador SIGhRA

A integração de Macros SIGhRA estende a integração já existente de Posições do Rastreador, trazendo agora as macros — mensagens estruturadas enviadas pelo motorista no equipamento embarcado (Início de Jornada, Refeição, Chegada ao Cliente, Pernoite, etc.) — e gravando cada ocorrência em uma tabela dedicada para consulta, relatórios e dashboards.

A leitura é incremental: a cada execução do job, o sistema guarda o último identificador de macro processado e usa esse ponteiro como ponto de partida na rodada seguinte. Resultado: zero perda de macros entre execuções, mesmo após reinicializações ou janelas de manutenção.

### O que esta rotina garante

- **Histórico completo** das macros enviadas pelos motoristas, garantindo que nenhum evento seja perdido entre as execuções.
- **Rastreabilidade das configurações** de origem em cada registro, bem como do veículo e motorista vinculados.
- **Maior resiliência a futuras evoluções** da API SIGhRA, permitindo que a tabela suporte diferentes formatos de dados sem necessidade de ajustes adicionais.
- **Possibilidade de auditoria** das chamadas realizadas à API (request e response), facilitando a investigação e análise de possíveis problemas.

### Pré-Requisitos

#### Cadastre a integração SIGhRA na tela Configurações Gestão Frotas.

##### **(1)** Acesse a tela ''Configurações Gestão Frotas'' (Logística » Gestão de Frotas » Configurações Gestão Frotas), vá até a aba ''Rastreadores'' e realize a inclusão ou edição da configuração desejada:

| Campo | O que informar |
| --- | --- |
| **Tipo** | SIGhRA. |
| **Usuário** | Usuário fornecido pela SIGhRA. |
| **Senha** | Senha fornecida pela SIGhRA. |
| **URL (Opcional)** | URL base do Web Service. Em branco, será utilizado o servidor padrão. |
| **Porta (Opcional)** | Porta do Web Service. Em branco, será utilizada a porta `9091`. |
| **Ativo** | Informe **Sim** para que o job considere esta configuração. |
| **Registra Log** | Informe **Sim** para gravar o request/response da chamada SOAP na tela **Logs de Integração**, facilitando investigações e análises de problemas. |

| Sem a opção **Ativo = Sim** e o preenchimento dos campos **Usuário** e **Senha**, a configuração será ignorada pelo job. |
| --- |

#### Vincule os veículos ao rastreador.

##### **(1)** Na tela ''Cadastro de Veículos'' (Configurações → Cadastros → Veículos), cada veículo que será monitorado deve possuir as configurações necessárias devidamente preenchidas:

| Campo | O que informar |
| --- | --- |
| **Tipo do Rastreador** | SGR (SIGhRA). |
| **ID Rastreador** | Identificador do veículo na plataforma SIGhRA. |

| O ID Rastreador pode ser preenchido automaticamente pela rotina Atualizar IDs do Sighra (executada junto da integração de posições) ou manualmente pelo cadastro. |
| --- |

Sem o vínculo configurado, a macro continuará sendo gravada, porém sem a identificação do código do veículo e do motorista no Sankhya. Ainda assim, os dados brutos retornados pela API — como placa, frota e CPF do motorista — permanecerão registrados normalmente.

#### Ajuste a frequência de execução do job (opcional).

Por padrão, a rotina está configurada para ser executada a cada 1 minuto. Para alterar essa frequência

**(1)** Acesse a tela **''Parâmetros do Sistema''** (Configurações » Parâmetros do Sistema).

**(2)** Localize o parâmetro **Expressão de Execução JOB Integração de Macros SIGhRA** (`TCFEXPJOBMACSGR`).

**(3)** Ajuste a expressão cron conforme a necessidade da operação.

| A definição de um intervalo curto considera o limite de 1000 macros por chamada imposto pela API SIGhRA. Em frotas de grande porte, esse volume pode ser atingido rapidamente, especialmente fora do horário comercial. Por isso, intervalos muito longos entre as execuções podem ocasionar atraso na integração e no recebimento das macros pelo sistema. |
| --- |

### Como acompanhar as macros integradas

#### Consulta direta na tabela

As macros integradas ficam disponíveis na tabela **TCFMACROSVEI**, podendo ser consultadas via **DBExplorer** ou utilizadas em relatórios e dashboards personalizados.

Cada registro disponibiliza informações como:

- **Identificação do veículo:** placa, frota, código do veículo no Sankhya e tipo de rastreador.
- **Identificação do motorista:** CPF, nome, código no Sankhya, ID do cliente e login utilizado na plataforma do rastreador.
- **Data, hora e localização:** data/hora do envio realizado pelo motorista, data/hora de recepção no servidor SIGhRA, latitude, longitude, cidade, estado, logradouro e ponto de referência.
- **Conteúdo da macro:** número, nome, tipo, formulário preenchido pelo motorista, hodômetro, velocidade e status da ignição.
- **Auditoria da integração:** data/hora da integração no Sankhya e referência à configuração SIGhRA responsável pela origem do registro.

#### Logs de chamadas á API

Quando a configuração estiver com a opção **Registra Log = Sim**, cada chamada realizada à API SIGhRA terá o request (envelope SOAP enviado) e o response (XML recebido) gravados na tela **Logs de Integração** (`TMSLOGINTEGRACAO`), permitindo consultas e análises filtradas pela configuração do rastreador.

### Como rotina funciona - Fluxo Resumido

A cada 1 minuto
       ↓
Job de Macros SIGhRA dispara
       ↓
Lê todas as configurações SIGhRA ativas
       ↓
Para cada configuração:
       ↓
Chama API obterMacros passando o último ID já integrado
       ↓
Registra Log?
  ├── Sim → Salva request/response em Logs de Integração
  └── Não
       ↓
Lê a lista de macros retornada (até 1000 por chamada)
       ↓
Para cada macro:
  ├── Resolve veículo e motorista pelo ID do rastreador
  │       ↓
  │   Grava registro em TCFMACROSVEI
  │
  └── Atualiza o último ID integrado na configuração
       ↓
Próxima macro

### Como o ponteiro do último ID funciona

##### A API SIGhRA retorna até 1000 macros por chamada, ordenadas pelo identificador interno:

| Situação | O que a API retorna |
| --- | --- |
| **Primeira execução (sem ponteiro salvo)** | Macros do dia atual. |
| **Execuções seguintes** | Apenas macros novas desde o último ID integrado, limitadas a 1000 registros por chamada. |

Se a frota acumular mais de 1000 macros entre execuções (ex.: após uma janela de indisponibilidade longa), as próximas execuções vão drenando o backlog automaticamente — sem perda.

### Pontos de verificação em caso de falhas

| Sintoma | O que verificar |
| --- | --- |
| **Macros não aparecem em** `TCFMACROSVEI` | Verifique se a configuração SIGhRA está marcada como **Ativa** e se o usuário e senha informados estão corretos. |
| **O job não executa no horário esperado** | Confira a expressão cron configurada em **Parâmetros do Sistema**. |
| **Macros chegam sem o campo Cód. Veículo preenchido** | Valide se o veículo está cadastrado com **Tipo do Rastreador = SGR** e com o **ID Rastreador** correto. |
| **Erro intermitente de comunicação com a SIGhRA** | Habilite a opção **Registra Log** na configuração e consulte o request/response na tela **Logs de Integração**. |
| **Macros muito antigas sendo integradas** | Indica que o sistema está processando um backlog após período de indisponibilidade. Esse comportamento é esperado e tende a se normalizar após alguns ciclos de execução. |
