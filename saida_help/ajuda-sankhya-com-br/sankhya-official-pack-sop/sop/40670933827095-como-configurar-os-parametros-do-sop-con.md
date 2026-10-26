---
id: "40670933827095"
titulo: "Como configurar os parâmetros do SOP Conciladora"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40670933827095-Como-configurar-os-par%C3%A2metros-do-SOP-Conciladora"
trilha: "Sankhya Official Pack - SOP > SOP"
atualizado_em: "2026-07-22T13:27:14Z"
rotulos: ["Configuração", "Preferências", "Financeiro", "Conciliação", "API", "SOP conciliadora", "API da Conciliadora", "WebService", "CRON Jobs", "TDCCON", "Baixas e Conciliação", "Validações de Valores na Baixa", "Retroação", "Flags"]
---

# Como configurar os parâmetros do SOP Conciladora

#### Introdução

O SOP Conciliadora possui parâmetros responsáveis pela comunicação com a API da Conciliadora, execução de rotinas automáticas, validações financeiras e processamento das conciliações realizadas no sistema.

Todos os parâmetros relacionados ao produto possuem o prefixo **''TDCCON''** e podem ser localizados na tela **''Preferências''** (Configurações » Avançado » Preferências) do Sankhya.

Este artigo apresenta o objetivo de cada parâmetro, bem como orientações sobre sua utilização e impacto na integração.

#### Como acessar os parâmetros do SOP Conciliadora

**(1)** Acesse a tela ''Preferências'' (Configurações » Avançado » Preferências).

**(2)** Pesquise pelo termo **''TDCCON''**.

**(3)** Localize o parâmetro desejado.

**(4)** Realize a configuração necessária.

**(5)** Clique em **''Salvar''** para confirmar as alterações.

#####

**ATENÇÃO:**

- Recomenda-se que alterações nos parâmetros sejam realizadas apenas por usuários com conhecimento técnico da integração.
- Antes de alterar parâmetros críticos, realize validações em ambiente de homologação.
- Configurações incorretas podem impedir o envio de vendas, busca de pagamentos ou processamento das conciliações financeiras.

#### Configurações de conexão e API

**IMPORTANTE**:

- Os parâmetros desta seção são responsáveis pela comunicação com a API da Conciliadora. Alterações incorretas podem impedir o funcionamento da integração.
- Estes parâmetros configuram a **comunicação com o WebService** da Conciliadora.

| Parâmetro | Descrição | Função |
| --- | --- | --- |
| **\*TDCCONURLVENDA** | Conciliadora URL Envio de Vendas | **Não precisa ser alterado.**  URL base do WebService para envio de vendas.  (Padrão: `http://webservice.conciliadora.com.br/`). |
| **\*TDCCONHOSTVENDA** | Conciliadora Host Envio de Vendas | **Não precisa ser alterado.**  Host do serviço.  (Padrão: `webservice.conciliadora.com.br`). |
| **\*TDCCONSOAPVENDA** | Conciliadora SOAP Action Envio Vendas | **Não precisa ser alterado.**  Ação SOAP específica para o método de envio.  (Padrão: `.../XmlVendaCliente`). |
| **TDCCONTOKENAPI** | Conciliadora Token de Acesso API | **( Crítico)** Token de autenticação fornecido pela Conciliadora.  **Sem ele, a integração não funciona**. |

#### Configurações Financeiras (Baixas e Conciliação)

Os parâmetros abaixo controlam a forma como o sistema realiza baixas financeiras e conciliações bancárias.

| Parâmetro | Descrição | Função |
| --- | --- | --- |
| **TDCCONTOPBAIXA** | Conciliadora TOP Baixa Pagamentos | Código da TOP (Tipo de Operação) utilizada para realizar a **baixa dos pagamentos** conciliados. |
| **TDCCONTOPBTXAL** | Conciliadora TOP Baixa Taxa de Aluguel | Código da TOP utilizada para lançar/baixar **taxas de aluguel** de máquinas. |
| **TDCVALTIPTIT** | Ativar validacao do Tipos de Titulo (Parceiro ADM) | Se ativo, valida tipos de título específicos (geralmente para parceiro ADM). |
| **TDCCONCTIT** | Conciliar financeiros na Mov. Bancária? | Define se deve realizar a **conciliação bancária** automática após baixar o título. |
| **TDCCONSDAVLRDE** | Somar desconto/acrescimo no valor desdobramento? | Define se deve somar descontos ou acréscimos ao valor do desdobramento no momento da baixa. |

####

#### Validações de Valores na Baixa

Os parâmetros desta seção auxiliam na validação de divergências entre os valores recebidos da Conciliadora e os valores financeiros do Sankhya.

| Parâmetro | Descrição | Função |
| --- | --- | --- |
| **TDCCONVALVLRBRU** | Validar Vlr. Bruto na baixa? | Ativa a validação do valor bruto na baixa. Se o valor divergir, a baixa pode ser impedida. |
| **TDCCONDVALVLRBR** | Valor de desvio p/ validacao Vlr. Bruto na baixa | Margem de erro (desvio) aceitável em reais para o valor bruto (Ex: aceitar diferença de R$ 0,01). |
| **TDCCONVALPETAXA** | Calcular o valor da taxa para validar na baixa? | Se deve recalcular e validar o valor da taxa administrativa no momento da baixa. |
| **TDCCONVALTX** | Valor de desvio de taxa p/ validar na baixa | Margem de erro aceitável em reais para a validação da taxa administrativa. |
| **TDCCONDIFBRULIQ** | Considera dif/ de valor bruto e liquido na baixa? | Se deve considerar a diferença matemática entre valor bruto e líquido ao efetuar a baixa. |

####

#### Janelas de Busca e Retroação

Os parâmetros abaixo definem o período retroativo utilizado nas consultas e integrações da Conciliadora.

| Parâmetro | Descrição | Função |
| --- | --- | --- |
| **TDCDIASLIMLOG** | Determina o periodo de Logs que serao deletados | Dias para manter logs armazenados na **TDCTCCLOG** antes de limpar automaticamente. |
| **TDCCONDRAPI** | Dias retroacao p/ BUSCA na API. | Dias de retroação para buscas gerais na API da Conciliadora. |
| **TDCCONDRLOCPV** | Dias retroacao p/ BUSCA de locação ponto de venda. | Dias de retroação específicos para busca de locação de Ponto de Venda. |
| **DIASBUSCAFINPAG** | Dias retroacao BUSCA VWFINPAGAMENTO | Dias de retroação considerados na view de financeiro (**VWFINPAGAMENTO**). |
| **BUSCAFINPAGBAI** | Considerar titulos baixados BUSCA VWFINPAGAMENTO? | Se a view de financeiro deve olhar também títulos que já foram baixados (**true**/**false**). |

##

####

#### Agendamento de Tarefas (CRON Jobs)

Os parâmetros CRON controlam a execução automática das rotinas da integração. Defique a frequência e horário de execução automática dos Jobs.

**ATENÇÃO**: Recomenda-se validar cuidadosamente os horários configurados para evitar concorrência de processamento.

| Parâmetro | Descrição | Função |
| --- | --- | --- |
| **TDCCONCRONVEN** | CRON Envio de Vendas (JOB) | Horário do Job de Envio de Vendas (Padrão: 18:00). |
| **TDCCONCRONPAG** | CRON Busca Pagamento (JOB) | Horário do Job de Busca de Pagamentos (Padrão: 17:30). |
| **TDCCONCRONCAN** | CRON Busca Cancelamento (JOB) | Horário do Job de Busca de Cancelamentos (Padrão: 17:30). |
| **TDCCONCRONTAX** | CRON Busca Taxa Aluguel (JOB) | Horário do Job de Busca de Taxa de Aluguel (Padrão: 17:30). |
| **TDCCONCRONAPV** | CRON Busca Aluguel PV (JOB) | Horário do Job de Busca de Aluguel de Ponto de Venda (Padrão: 16:30). |
| **TDCCRONLIMPLOG** | CRON exclusao de logs | Horário do Job de Limpeza de Logs antigos (Padrão: 19:30). |
| **TDCCONCRONCPA** | Buscar Pagamentos (JOB)? | Horário do Job de Correção de Parceiros (Padrão: 06:00 aos Domingos). |

##

####

#### Ativação de Funcionalidades (Flags)

##### Os parâmetros abaixo permitem ativar ou desativar funcionalidades específicas da integração.

| Parâmetro | Descrição | Função |
| --- | --- | --- |
| TDCCONFILEST | Conciliadora Filtrar Estabelecimento API | Se filtra o estabelecimento na API enviando apenas dados da loja atual/logada. |
| **TDCCONUSUPDR** | Cod. Usuario Padrao da Conciliacao | Código do usuário (codusu) usado como autor das ações automáticas do sistema. |
| **TDCCONBUSCAPAG** | Buscar Pagamentos (JOB)? | Chave geral para Ativar/Desativar o processo de busca de pagamentos. |
| **TDCCONBUSCACAN** | Buscar Cancelamentos (JOB)? | Chave geral para Ativar/Desativar o processo de busca de cancelamentos. |
| **TDCCONBUSCATAX** | Buscar Taxas de aluguel (JOB)? | Chave geral para Ativar/Desativar o processo de busca de taxas. |
| **TDCCONLOTPAD** | Diferencia envio de vendas por parceiro adquirente | Diferencia o envio de vendas agrupando os lotes por parceiro adquirente. |
| **TDCCONREMZERESQ** | Utiliza zeros a esquerda no num. Estabelecimento? | Controla se deve remover/usar zeros à esquerda no código do estabelecimento para match com a adquirente. |

#### Boas práticas

- Realize alterações preferencialmente fora do horário operacional;
- Após alterar parâmetros críticos, valide a integração em ambiente de homologação;
- Monitore os logs da integração após alterações em parâmetros de API ou CRON;
- Mantenha o token da API atualizado conforme orientação da Conciliadora.
