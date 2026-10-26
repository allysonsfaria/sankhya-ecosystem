---
id: "37880048070295"
titulo: "Como calcular e faturar os serviços de forma proporcional à ativação/cancelamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:42Z"
rotulos: ["Configuração", "Faturamento", "Contrato", "Financeiro", "NFS-e", "Pro-rata"]
---

# Como calcular e faturar os serviços de forma proporcional à ativação/cancelamento

| Categoria |
| --- |
| [O que é e como funciona essa operação?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9A12Q78E8F1WHYGVFQWTK) |
| [Quais problemas resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9AD0K2AN034S792HFN4SQ) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9AJ48Z06Z9KPVYBSVG6G5) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9AQZ64Y391FC8XZTQBTF8) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9B4421SQ8Y9ZWMF8J50WR) |
| [Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9BAQTC3HC7XEJ8HNKD47X) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880048070295-Como-calcular-e-faturar-os-servi%C3%A7os-de-forma-proporcional-%C3%A0-ativa%C3%A7%C3%A3o-cancelamento#h_01KFN9BJ66T1MJS2J0HVP5YVCE) |

## Cálculo de faturamento dos serviços de forma proporcional (Pro-rata)

#### O que é e como funciona essa operação?

O faturamento proporcional, também conhecido como pro-rata, é utilizado quando um contrato não permanece ativo durante o mês inteiro. Isso acontece, por exemplo, quando o serviço começa no meio do mês ou é cancelado antes do fim.

Em vez de cobrar o valor cheio, o sistema calcula apenas pelos dias em que o serviço esteve ativo dentro daquela referência. Esse processo garante que o cliente pague de forma justa e que a empresa registre a receita correta.

#### Quais problemas resolve?

- Cobrança integral de um mês mesmo quando o serviço foi iniciado ou encerrado no meio do período.
- Inconsistência entre a prestação real do serviço e o valor faturado, gerando dúvidas ou reclamações.
- Dificuldade no controle de contratos com variações de data, como ativações tardias ou cancelamentos antecipados.
- Erros na conciliação financeira, por valores faturados acima ou abaixo do efetivamente prestado.

#### Quais os riscos de não utilizar?

Cobrar o valor cheio em meses com ativação ou cancelamento parcial pode gerar insatisfação do cliente e questionamentos sobre a cobrança. Sem o cálculo proporcional, há risco de lançamentos incorretos no financeiro, afetando relatórios e o controle da receita.

Além disso, ocorre desalinhamento entre o serviço prestado e o valor faturado, o que compromete a confiabilidade das informações.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103868872)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: A Axis LTDA firmou um novo contrato de manutenção com o cliente Comercial Viana, com valor mensal de R$ 3.000,00. O contrato foi assinado no mesmo mês do primeiro contrato, porém, no dia 13, e a prestação do serviço começou imediatamente após a ativação. Esse contrato tem uma característica diferente do primeiro, o tipo de pagamento utilizado é vencido, ou seja, o pagamento ocorre sempre no próximo mês referente a prestação de serviço.

Como o serviço não foi prestado durante todo o mês, o faturamento deve considerar apenas os dias efetivos de serviço na referência de ativação. Por isso, será necessário realizar o faturamento proporcional, conhecido como pro-rata.

**Tarefas**: Sua tarefa é registrar o contrato com a data real de início e realizar o faturamento da referência de forma proporcional, de acordo com o período de ativação.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Configurações para faturamento parcial (pro-rata):**

- Acesse a tela **Preferências**
  Menu: Configurações » Avançado
- Busque pelo parâmetro **“FATCONTPRORATA - Utiliza faturamento de contratos pro rata?”** e deixe-o “ligado”.

2. **Registro do contrato que será usado na operação:**

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos
- Registre um novo contrato para o parceiro Comercial Viana, você pode duplicar o contrato anterior também como feito em outras atividades, porém sempre se atentando às alterações que são necessárias, data do contrato, referência de próximo faturamento, como citado anteriormente.
- Na aba **Geral**, marque a flag **Faturamento pro rata?**
- Na aba **Propriedades**, no campo **Tipo de pagamento,** informe **“vencido”.**
- Na aba **Produtos/Serviços**, sub-aba **Ocorrências**, a data de ativação do produto será dia 13 do mês de registro do contrato.
- Lembre-se de preencher o campo **Qtd. Prevista** na aba **Geral** do serviço.

3. **Faturamento do contrato:**

- Acesse a tela **Faturamento de Contratos**
  Menu: Contratos e Serviços » Rotinas
- Nos **Filtros Personalizados**, utilize o campo **Parceiro** para buscar o cliente Comercial Viana.
- Marque a flag **Considerar Contatos/Perfil/Serviço**
- Nos **Parâmetros Obrigatórios**, preencha as seguintes informações:

**Tipo de Operação** - VENDA NFS-E

**Tipo de Título -** 1

**Tipo de Negociação -** 16

**Observação Padrão -** 0

**Data para Faturamento -** Primeiro dia do próximo mês em relação a data do contrato

**Mês para Referência -** O mês para referência se trata do mês que ocorrerá o pagamento, sendo assim, mesma data usada no campo anterior

**Série -** NF

- Clique em **Aplicar**
- Confira se o valor foi calculado corretamente considerando os dias em que houve a prestação de serviços, a fórmula utilizada pelo sistema é: **valor do contrato /30 \* dias de serviço prestado no mês**
- Realize o faturamento do contrato como visto em aulas anteriores

#### Correção e Repetição

- Se o valor do faturamento não for calculado proporcionalmente, revise os seguintes pontos no contrato: se a flag "Faturamento pro rata?" foi marcada e se a data de ativação foi registrada corretamente.
- Caso a opção de faturamento pro rata não seja apresentada, revise as configurações do script fornecido.
