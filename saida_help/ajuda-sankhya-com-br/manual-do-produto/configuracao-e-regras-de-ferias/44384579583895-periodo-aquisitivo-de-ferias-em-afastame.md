---
id: "44384579583895"
titulo: "Período aquisitivo de férias em afastamento por serviço militar ou cárcere"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44384579583895-Per%C3%ADodo-aquisitivo-de-f%C3%A9rias-em-afastamento-por-servi%C3%A7o-militar-ou-c%C3%A1rcere"
trilha: "Manual do Produto > Pessoas+ > Férias > Configuração e Regras de Férias"
atualizado_em: "2026-10-20T14:38:51Z"
rotulos: ["Ocorrências", "br.com.sankhya.rh.LancamentoOcorrencias"]
---

# Período aquisitivo de férias em afastamento por serviço militar ou cárcere

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Ocorrências
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

### O que é e para que serve

Quando o colaborador se afasta para **prestação de serviço militar** ou por **cárcere** (prisão), o contrato de trabalho fica suspenso. Durante esse intervalo, o colaborador **não adquire tempo para férias**.

Nesses casos, o Pessoas+ **suspende a contagem do período aquisitivo**: os meses em que o colaborador ficou afastado não são contados, e a data final do período aquisitivo é **prorrogada** pela mesma quantidade de meses. Ao retornar, o colaborador continua a contagem de onde parou até completar os 12 meses de trabalho.

O período aquisitivo **não é quitado** e o colaborador **não perde o direito às férias**, independentemente da duração do afastamento.

Use este artigo para configurar a ocorrência, lançar o afastamento, registrar o retorno e conferir o período aquisitivo prorrogado.

| **⚠️** **Atenção**  Este comportamento é diferente da **Quitação de férias por afastamento** (Art. 133 da CLT), aplicada a afastamentos por doença, acidente de trabalho ou aposentadoria por invalidez superiores a 180 dias. Na quitação, o período aquisitivo é encerrado e um novo período é iniciado após o retorno. No serviço militar e no cárcere, o mesmo período aquisitivo é mantido e apenas tem sua data final prorrogada. |
| --- |

### Antes de começar

Confira se:

- a ocorrência utilizada no afastamento está cadastrada na aba **Cadastro** da tela **Ocorrências** (Pessoal+ > Rotinas Folha) com:
  - **Tipo de afastamento:** **Serviço militar** ou **Cárcere**;
  - **Motivo de afastamento do eSocial:** **29 – Serviço militar** ou **11 – Cárcere**, correspondente ao tipo de afastamento;
- a opção **Suspende contagem de avos para férias** está marcada na regra de cálculo vinculada à empresa, na tela **Regra de Cálculo** (Pessoal+ > Cadastros), aba **Propriedades** > sub-aba **Força maior**. Essa opção vem marcada por padrão;
- o colaborador tem um período aquisitivo de férias em aberto.

### Jornada de Uso

#### Lançar o afastamento

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha), aba **Lançamento**.
2. Lance a ocorrência de serviço militar ou cárcere para o colaborador, informando a **Data de Início**.
3. Enquanto o colaborador estiver afastado, **não preencha a Data de término**.

   | **⚠️** **Atenção**  A ocorrência de serviço militar ou cárcere **não deve ser lançada com a Data de término**. A **Data de término** deve ser informada somente no retorno do colaborador, na edição da ocorrência. É nesse momento que o sistema prorroga o período aquisitivo. |
   | --- |

#### Registrar o retorno do colaborador

1. Quando o colaborador retornar, edite a ocorrência de afastamento.
2. Informe a **Data de término** correspondente ao último dia de afastamento e confirme.

Ao confirmar a **Data de término**, o sistema:

- conta quantos meses o afastamento ocupou dentro do período aquisitivo;
- recalcula a data final do período aquisitivo em aberto mais recente do colaborador: **data inicial do período + 12 meses + meses afastados − 1 dia**;
- atualiza a data prevista para as férias para o dia seguinte à nova data final.

A prorrogação acontece **no momento em que a Data de término é confirmada**. Não é necessário aguardar o colaborador completar os 12 meses de trabalho após o retorno.

#### Conferir o período aquisitivo

1. Acesse a tela **Requisições** (Pessoal+ > Rotinas Folha) > **Férias**.
2. Abra a aba **Aquisitivos** e confira a nova data final do período aquisitivo.

A contagem é feita em **meses (avos)**, e não em dias:

- cada mês completo de afastamento suspende um mês do período aquisitivo;
- frações de mês **com mais de 14 dias** são contadas como um mês completo;
- frações de mês **com até 14 dias** não são contadas.

Por isso, a nova data final do período aquisitivo pode ser alguns dias diferente de uma contagem feita dia a dia.

**Exemplo:**

| Situação | Data |
| --- | --- |
| Período aquisitivo original | 01/02/2025 a 31/01/2026 |
| Afastamento por serviço militar | 01/06/2025 a 30/11/2025 (6 meses) |
| Retorno do colaborador | 01/12/2025 |
| **Período aquisitivo após o retorno** | **01/02/2025 a 31/07/2026** |
| **Data prevista para as férias** | **01/08/2026** |

O colaborador trabalhou 4 meses antes do afastamento (fevereiro a maio de 2025) e completa os 8 meses restantes depois do retorno (dezembro de 2025 a julho de 2026), somando os 12 meses de trabalho exigidos.

#### Calcular rescisão e provisão de férias

A suspensão também é considerada nos cálculos de rescisão e de provisão de férias:

- **Férias vencidas:** se o período aquisitivo ainda estiver com 12 meses, o sistema prorroga a data final pelos meses de serviço militar ou cárcere antes de verificar se as férias estão vencidas.
- **Férias proporcionais:** os meses de serviço militar e de cárcere são descontados dos avos de férias proporcionais.

### Pontos de Atenção

- O **Tipo de afastamento** e o **Motivo de afastamento do eSocial** precisam estar coerentes (Serviço militar com motivo 29; Cárcere com motivo 11). Se apenas um deles estiver configurado, o período aquisitivo não é prorrogado.
- Se a opção **Suspende contagem de avos para férias** estiver desmarcada na regra de cálculo da empresa, o período aquisitivo não é prorrogado e o tempo de afastamento é contado normalmente.
- A ocorrência não deve ser lançada com a **Data de término**. Informe-a somente no retorno do colaborador, editando a ocorrência.
- Se a **Data de término** for alterada depois, o sistema recalcula a data final do período aquisitivo a partir da data inicial do período, considerando a nova duração do afastamento.
- O sistema **não verifica** o prazo de 90 dias para retorno após a baixa do serviço militar, previsto no **Art. 132 da CLT**. Se o colaborador não retornar dentro desse prazo, o tratamento do período aquisitivo anterior ao afastamento deve ser avaliado e ajustado manualmente.

### Perguntas frequentes

**O colaborador perde as férias se ficar mais de 180 dias afastado por serviço militar ou cárcere?**

Não. A perda do direito às férias por afastamento superior a 180 dias (Art. 133 da CLT) não se aplica a esses casos. O período aquisitivo é mantido e apenas tem a data final prorrogada pelos meses afastados.

**O período aquisitivo ficou com mais de 12 meses. Está correto?**

Sim. A data final é prorrogada pela quantidade de meses de afastamento, então o período aquisitivo passa a ter mais de 12 meses entre a data inicial e a data final. Os meses efetivamente trabalhados continuam somando 12.

**Informei a Data de término e o período aquisitivo não mudou. O que verificar?**

Verifique se:

- a ocorrência foi lançada sem a **Data de término** e a data foi informada depois, na edição;
- o **Tipo de afastamento** é **Serviço militar** ou **Cárcere** e o **Motivo de afastamento do eSocial** é **29** ou **11**, respectivamente;
- a opção **Suspende contagem de avos para férias** está marcada na regra de cálculo da empresa;
- o afastamento durou mais de 14 dias, já que frações menores não são contadas como mês.

**Por que a nova data final não corresponde exatamente aos dias de afastamento?**

Porque a contagem é feita em meses. Frações de mês com mais de 14 dias contam como mês completo, e frações com até 14 dias não são contadas.

### Artigos relacionados

- [Quitação de férias por afastamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/31144991936151)
- [Cadastro de Ocorrências da Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494)
- [Lançamento de Ocorrências para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/42603052607255)
- [Configuração das Regras de Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39936375428503)
