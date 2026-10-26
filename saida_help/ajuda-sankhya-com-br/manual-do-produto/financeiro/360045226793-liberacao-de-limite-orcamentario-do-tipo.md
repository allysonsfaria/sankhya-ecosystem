---
id: "360045226793"
titulo: "Liberação de limite orçamentário do tipo Mensal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045226793-Libera%C3%A7%C3%A3o-de-limite-or%C3%A7ament%C3%A1rio-do-tipo-Mensal"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:45:37Z"
rotulos: ["Configuração", "Movimentação Financeira", "Liberação de Limites", "Financeiro", "Orçamento", "Lançamento R$1.500 (ok). R$1.200 (liberação R$200)", "Ricardo suplementa R$1.000. Cristiano suplementa R$1.200 após liberação", "Renato: R$1.000 (suplementação). Ricardo: R$2.000 (todos). Cristiano: R$3.000 (todos)"]
---

# Liberação de limite orçamentário do tipo Mensal

Abaixo, tem-se um cenário de como funcionará a solicitação de liberação de limite orçamentário para o tipo Mensal:

**(1)** **Orçamento previsto: 2.500,00**

|  | **Renato** | **Ricardo** | **Cristiano** |
| --- | --- | --- | --- |
| **Pode liberar até** | 1.000,00 | 2.000,00 | 3.000,00 |
| **Pode antecipar** | Sim | Sim | Sim |
| **Pode suplementar** | Não | Sim | Sim |
| **Pode transferir** | Não | Sim | Sim |

---

No cenário acima descrito, o usuário Renato poderá apenas suplementar. No caso, ele poderá efetuar liberações mensais de até 1.000,00 de suplementação.

Já o usuário Ricardo pode antecipar, suplementar e transferir liberações mensais de até 2.000,00.

Por último, o usuário Cristiano também poderá antecipar, suplementar e transferir, porém, liberações mensais de até 3.000,00.

Desta forma, segue abaixo o caso de uso:

**(1)** **Renato - Suplementação:**

- O vendedor lançou um documento no valor de R$1.500,00 e solicita sua confirmação;
- O sistema processa o lançamento e não solicita liberação, visto que o orçamento previsto é de R$2.500,00;
- O vendedor lança um segundo documento no valor de R$1.200,00 e solicita sua confirmação;
- O sistema processa o lançamento e solicita uma liberação no valor de R$200,00 para o usuário Renato, visto que o mesmo possui alçada para liberação;
- O usuário Ricardo verifica a liberação e efetua uma suplementação no valor solicitado;
- O vendedor solicita a confirmação do documento;
- O sistema processa o lançamento e confirma o documento, visto que houve a liberação (suplementado).

| **Usuário** | **Suplementação** | **Antecipação** | **Transferência** |
| --- | --- | --- | --- |
| Renato | 200,00 | 0,00 | 0,00 |
| Ricardo | 0,00 | 0,00 | 0,00 |
| Cristiano | 0,00 | 0,00 | 0,00 |

**(1)** **Ricardo - Suplementação:**

- O vendedor lança um documento no valor de R$1.000,00 e solicita sua confirmação;
- O sistema processa o lançamento e solicita uma liberação no valor de R$1.000,00 para o usuário Ricardo, visto que Renato, o qual possui um limite de R$1.000,00 mensais não possui alçada (200 + 1.000 = 1.200);
- Ricardo verifica a liberação e efetua a suplementação do valor solicitado;
- O vendedor solicita a confirmação do documento;
- O sistema processa o lançamento e confirma o documento, já que houve a liberação.

| **Usuário** | **Suplementação** | **Antecipação** | **Transferência** |
| --- | --- | --- | --- |
| Renato | 200,00 | 0,00 | 0,00 |
| Ricardo | 1.000,00 | 0,00 | 0,00 |
| Cristiano | 0,00 | 0,00 | 0,00 |

**(1)** **Cristiano - Suplementação:**

- O vendedor lança um documento no valor de R$1.200,00 e solicita sua confirmação;
- O sistema processa o lançamento e solicita uma liberação no valor de R$1.200,00 para Ricardo, visto que Renato ainda pode antecipar ou transferir;

Neste cenário podem existir duas situações:

![Imagem 1: Caso o vendedor escolha suplementar, o sistema reavaliará o lançamento e solicitará uma liberação ao Cristiano, visto…](https://ajuda.sankhya.com.br/hc/article_attachments/16371136682391) Caso o vendedor escolha suplementar, o sistema reavaliará o lançamento e solicitará uma liberação ao Cristiano, visto que Ricardo não possui alçada para suplementar este valor (1.000,00 + 1.200,00 = 2.000,00).

![Imagem 2: Caso não se escolha o tipo de liberação, o sistema irá solicitar a liberação para Ricardo, o qual poderá apenas…](https://ajuda.sankhya.com.br/hc/article_attachments/16371128422935) Caso não se escolha o tipo de liberação, o sistema irá solicitar a liberação para Ricardo, o qual poderá apenas antecipar ou transferir.

Seguindo a primeira situação:

- Cristiano verifica a liberação e efetua uma suplementação;
- O vendedor solicita a confirmação do documento;
- O sistema processa o lançamento e confirma o documento, já que houve a liberação.
