---
id: "41296271575191"
titulo: "Como fica o DSR quando há férias no período"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41296271575191-Como-fica-o-DSR-quando-h%C3%A1-f%C3%A9rias-no-per%C3%ADodo"
trilha: "Manual do Produto > Pessoas+ > Férias > Cálculo de Férias"
atualizado_em: "2026-10-02T15:42:19Z"
rotulos: ["Cálculo", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Férias", "Cálculo de Férias", "Pessoal+", "DSR", "DIASNAOUTEISTRAB", "Cálculo dos Dias Úteis e Não Úteis no DSR quando Há Férias no Período de Apuração", "DIASUTEISTRAB"]
---

# Como fica o DSR quando há férias no período

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ › Rotinas Folha > Cálculos
**ID da tela:** br.com.sankhya.rh.CalculoIndFolha

---

### Descrição e Usabilidade

Em eventos que calculam **Descanso Semanal Remunerado (DSR)** com base nos dias úteis e não úteis do período de apuração, o sistema considera apenas os dias em que o trabalhador esteve efetivamente disponível para o trabalho.

Quando existe afastamento por férias dentro do período de apuração utilizado pela folha, os dias correspondentes às férias são desconsiderados automaticamente da contagem de dias úteis e não úteis.

Esse comportamento evita que o DSR seja calculado sobre períodos em que o colaborador já estava afastado, garantindo a apuração correta da remuneração.

#### Como o sistema realiza a apuração

O sistema inicia o cálculo considerando o calendário completo do período de apuração configurado para a empresa.

Em seguida, identifica ocorrências que impactam a disponibilidade do trabalhador, como períodos de férias, e realiza os ajustes necessários na quantidade de dias úteis e não úteis.

Dessa forma, as variáveis utilizadas nas fórmulas de cálculo refletem apenas os dias efetivamente considerados para o rateio do DSR:

| Variável | Descrição |
| --- | --- |
| DIASUTEISTRAB | Quantidade de dias úteis considerados para o cálculo |
| DIASNAOUTEISTRAB | Quantidade de dias não úteis considerados para o cálculo |

**Exemplo**

Considere a seguinte situação:

**Período de apuração da folha:** 21/03/2026 a 20/04/2026

Calendário do período:

- 25 dias úteis;
- 6 dias não úteis;
- Total de 31 dias.

O colaborador possui férias registradas no período de 09/03/2026 a 22/03/2026.

Como o período de apuração inicia em 21/03/2026, os dias abaixo ainda estavam dentro das férias do trabalhador:

| Data | Classificação |
| --- | --- |
| 21/03/2026 | Dia útil |
| 22/03/2026 | Dia não útil |

O sistema então realiza o ajuste:

| Apuração | Quantidade |
| --- | --- |
| **Dias úteis** | |
| Dias úteis do calendário | 25 |
| (-) Dias úteis em férias | 1 |
| Total de dias úteis considerados | 24 |
| **Dias não úteis** | |
| Dias não úteis do calendário | 6 |
| (-) Dias não úteis em férias | 1 |
| Total de dias não úteis considerados | 5 |

Resultado utilizado na fórmula:

- `DIASUTEISTRAB = 24`
- `DIASNAOUTEISTRAB = 5`

Total de dias considerados no cálculo: **29 dias**

#### Impacto no cálculo do DSR

Quando a fórmula do evento utiliza as variáveis de dias úteis e não úteis, o sistema empregará os valores já ajustados pelas férias.

Exemplo:

| IF(&DIASUTEISTRAB > 0,(@E\_HORASDESOBREAVISO / &DIASUTEISTRAB) \* &DIASNAOUTEISTRAB,0) |
| --- |

Nesse cenário, a fórmula utilizará:

DIASUTEISTRAB = 24
DIASNAOUTEISTRAB = 5

e não os valores originais do calendário.

### Pontos de Atenção

- A quantidade de dias úteis e não úteis utilizada pelo cálculo pode ser diferente da quantidade total existente no calendário do período de apuração.
- O sistema desconsidera automaticamente os dias de férias que coincidirem com o período utilizado na folha.
- Esse comportamento não representa erro de cálculo, mas uma regra de apuração para evitar pagamento de DSR sobre dias em que o trabalhador estava afastado.
- Ao conferir divergências nas variáveis DIASUTEISTRAB e DIASNAOUTEISTRAB, verifique primeiro se existem férias, afastamentos ou outras ocorrências que reduzam os dias disponíveis para trabalho dentro do período de apuração.
- A análise deve considerar sempre o período de apuração configurado para a empresa, e não apenas a competência da folha.
