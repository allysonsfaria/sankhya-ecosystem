---
id: "37880269064599"
titulo: "Como acompanhar os contratos com pendência de reajuste"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:37Z"
rotulos: ["Configuração", "Relatórios", "Contrato", "Agendamento", "Financeiro"]
---

# Como acompanhar os contratos com pendência de reajuste

| Categoria |
| --- |
| [O que é e como funciona essa operação?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNAH5WZ6093GN3K69V3P62C) |
| [Quais problemas resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNAKBAZ2BSVKN5QR46TMDQJ) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNAKGSNAY2MC56EY7K1GJHQ) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNAKQ6BTN4E0XGJZCSP31F4) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNANKMH40AEHGA7BRBA53ZV) |
| [Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNANVWD3R8NZM4PTD2D3WJB) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880269064599-Como-acompanhar-os-contratos-com-pend%C3%AAncia-de-reajuste#h_01KFNAP1GF79Y9BNWJP9CT4585) |

## Acompanhamento dos contratos com pendências de reajuste

#### O que é e como funciona essa operação?

O acompanhamento de contratos com pendência de reajuste é feito por meio de um agendador, que envia alertas quando a data base de reajuste do contrato foi ultrapassada e o reajuste ainda não foi realizado.

Você define a frequência de verificação (por exemplo, semanal ou mensal), e o sistema gera uma notificação com a lista dos contratos que precisam ser reajustados. Assim, a equipe responsável pode acompanhar e tomar as providências necessárias, sem precisar consultar contrato por contrato.

Esse agendamento serve apenas como um lembrete automático para garantir que os reajustes sejam feitos no prazo correto.

#### Quais problemas resolve?

- Esquecimento de reajustes contratuais, principalmente em contratos longos
- Falta de um controle centralizado sobre quais contratos já deveriam ter sido reajustados
- Retrabalho manual para identificar contratos vencidos
- Risco de continuar faturando com valores antigos, gerando perdas financeiras

#### Quais os riscos de não utilizar?

Sem esse acompanhamento, a empresa pode continuar faturando contratos com valores desatualizados, o que compromete a receita e reduz a margem de lucro.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103919992)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: A Axis realiza reajustes anuais em seus contratos de manutenção. Com o crescimento da base de clientes, a responsável pelo setor passou a ter dificuldade em acompanhar manualmente quais contratos já deveriam ter sido reajustados.

Para resolver isso, a empresa decidiu configurar um agendador de pendência de reajuste, que envia automaticamente um alerta com a lista dos contratos que já ultrapassaram a data base definida e ainda não foram atualizados.

**Tarefas**: Sua tarefa é configurar o agendamento para monitorar os contratos com pendência de reajuste.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Configurações para agendador de notificações:**

- Acesse a tela **Preferências**
  Menu: Configurações » Avançado
- Busque pelo parâmetro **“NOTPENREACON - Notificar pendências de reajuste de contratos”** e deixe-o “ligado”.
  Este parâmetro habilita a opção **“Configurar Notificações de Reajuste”** na tela de **“Contratos”** através dessa opção é possível realizar um agendamento para verificação de contratos que precisam ser reajustados e a partir daí é feita a notificação na própria tela.

2. **Criação do agendador para notificação das pendências de reajuste:**

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos
- Clique no botão outras opções **(...)** » **Configurar Notificações de Reajuste**
- **No pop-up aberto preencha:**
- **1ª execução -** 07:00
- **Meses -** Marque todos
- Selecione a opção **Diário** para execução diariamente
- Salve as informações
- Caso existam contratos com pendência de reajuste, será apresentado na tela um ícone de notificação.

#### Correção e Repetição

- Garanta que todos os campos foram preenchidos corretamente para a execução do agendador.
