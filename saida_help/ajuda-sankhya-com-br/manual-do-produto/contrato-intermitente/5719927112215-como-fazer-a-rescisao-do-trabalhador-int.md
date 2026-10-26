---
id: "5719927112215"
titulo: "Como fazer a rescisão do trabalhador intermitente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente"
trilha: "Manual do Produto > Pessoas+ > Contratos Especiais > Contrato Intermitente"
atualizado_em: "2026-10-02T15:23:56Z"
rotulos: ["eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Aviso Prévio", "Rescisão", "Contrato Intermitente", "Pessoal+", "Rescisão de Contrato de Trabalho Intermitente"]
---

# Como fazer a rescisão do trabalhador intermitente

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Cálculos
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

### Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KKQ61TWZF6NP2ZB3CYVAX0QF)

[1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KKKRJ30QS80RY27NE1E2PHEA)
[2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KKQ6HPS31B9JWK9CR6A70WEZ)
[3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KKKRJ31QG33A75RPF3PTJDVV)
[4. Ponto de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KKQBHMEQN9F9ZRD0P9JSXDDC)

[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KZ6PRAZP912HNKZMWPR3T0BC)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215-Como-fazer-a-rescis%C3%A3o-do-trabalhador-intermitente#h_01KKQBHMFT3BR62H0HS07AVY74)

---

## Descrição e Usabilidade

A rescisão do **trabalhador intermitente** possui particularidades em relação aos demais contratos de trabalho, especialmente quanto ao **cálculo do aviso prévio indenizado**, à apuração das verbas rescisórias e à existência ou não de **convocações no período da rescisão**.

Quando a rescisão ocorre por iniciativa do empregador, o aviso-prévio é sempre indenizado e calculado com base na média da remuneração recebida pelo trabalhador nos últimos 12 meses ou desde a admissão, quando o contrato possuir período inferior.

O sistema também contempla cenários em que não há remuneração decorrente de convocações no período utilizado para o cálculo, gerando automaticamente os eventos demonstrativos necessários para a emissão dos documentos rescisórios e envio das informações ao eSocial.

### 1. Descrição da Funcionalidade

A rescisão do contrato intermitente está fundamentada principalmente em:

- **Consolidação das Leis do Trabalho – Art. 452-A**
- **Portaria MTP nº 671/2021 – Art. 37**

Conforme previsto na legislação, o cálculo do aviso-prévio indenizado considera a **média das remunerações recebidas** pelo trabalhador no período de referência.

Dessa forma, caso os descontos superem os proventos da rescisão, o sistema limita a compensação para evitar saldo devedor ao trabalhador, conforme previsto no § 5º do art. 477 da CLT.

“Art. 477- Na extinção do contrato de trabalho, o empregador deverá proceder à anotação na Carteira de Trabalho e Previdência Social, comunicar a dispensa aos órgãos competentes e realizar o pagamento das verbas rescisórias no prazo e na forma estabelecidos neste artigo.

§5º Qualquer compensação no pagamento de que trata o parágrafo anterior não poderá exceder o equivalente a um mês de remuneração do empregado.”

### 2. Pré-requisitos

Antes de calcular a rescisão de um trabalhador intermitente, é importante verificar:

- se **todas as folhas das convocações foram calculadas e fechadas**;
- se os valores foram registrados na **tabela histórica do trabalhador**;
- se os **acumulados do ano estão atualizados**.

Essas informações são necessárias para garantir o correto cálculo das **médias utilizadas na rescisão**.

### 3. Jornada de Uso

O cálculo da rescisão do trabalhador intermitente depende da correta parametrização dos eventos e das fórmulas utilizadas pelo sistema. Além disso, o comportamento do cálculo varia conforme o tipo de desligamento e a existência de convocações no período de referência.

#### ![Imagem 1: Eventos e fórmulas da rescisão comum a todos os tipos](https://ajuda.sankhya.com.br/hc/article_attachments/42315079811863) Eventos e fórmulas da rescisão comum a todos os tipos

É necessário parametrizar os [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911) que participarão do cálculo da rescisão do intermitente quando há convocação na referência, conforme exemplos abaixo:

**(1)** **Evento saldo salário**

![Imagem 2: (1) Evento saldo salário](https://ajuda.sankhya.com.br/hc/article_attachments/40417209262615)

####

**(1)** **Evento DSR saldo salário**

![Imagem 3: (1) Evento DSR saldo salário](https://ajuda.sankhya.com.br/hc/article_attachments/40417238340887)

Os **eventos de férias, média de férias e 1/3 constitucional, 13º salário (normal e média)** e respectivas médias devem possuir como **regra de cálculo as folhas Normal, Rescisão e Intermitente**, pois poderão participar de qualquer uma dessas apurações.

Como os eventos de férias e 13º salário são os mesmos na folha normal, os eventos de saldo salário e DSR do saldo salário ficarão depois destes, porém não altera a apuração dos tributos.

As outras parametrizações seguem conforme legislação vigente para cada tipo e na ausência, conforme entendimento da empresa.

As fórmulas relacionadas ao contrato intermitente devem seguir o **padrão disponibilizado na base modelo da Sankhya**.

#### ![Imagem 4: Tipos de Rescisão](https://ajuda.sankhya.com.br/hc/article_attachments/42315079813655) Tipos de Rescisão

#####

##### 2.1. Rescisão sem justa causa iniciativa do empregador

Nesse tipo de desligamento:

- o **aviso prévio é sempre indenizado**;
- não existe aviso prévio trabalhado para o contrato intermitente.

O cálculo do aviso prévio é realizado considerando:

1. a **remuneração total recebida nos últimos 12 meses** (ou desde a admissão);
2. a divisão pelo **número de meses trabalhados**;
3. o resultado dividido por **30 dias**;
4. multiplicação pelo **número de dias do aviso prévio**.

Quando o trabalhador **não possuir remunerações decorrentes de convocações nos últimos 12 meses** (ou desde a admissão, quando esse período for inferior), o sistema não enccontrará valores para compor a média utilizada no cálculo do aviso-prévio indenizado e das demais verbas rescisórias.

Nessa situação, ao processar a rescisão por **iniciativa do empregador sem justa causa**, o sistema gera automaticamente o demonstrativo **Folha Intermitente sem Valor**, registrando que não houve valores de remuneração a serem considerados no período de apuração.

**(3)Evento 262- Aviso prévio indenizado intermitente**

[GIF animado: Imagem 5: (3) Evento 262- Aviso prévio indenizado intermitente](https://ajuda.sankhya.com.br/hc/article_attachments/40417238343063)

**Fórmula**

| 262 - IF(QueFuncionario.CODCATEGESOCIAL <> 111, 0, IF((&TIPFOL = 'R') AND (&AVISO =     'S') AND (&CAUAFA = 60), ((&BaseMediaInterm / IF(&MesesMediaInterm > 0,   &MesesMediaInterm, 1)) / 30) \* &Diaavi, 0)) |
| --- |

**(3)Evento 263- férias API intermitente**

[GIF animado: Imagem 6: (3) Evento 263- férias API intermitente](https://ajuda.sankhya.com.br/hc/article_attachments/40417238343831)

**Fórmula**

| 263- IF(QueFuncionario.CODCATEGESOCIAL <> 111, 0, IF((&TIPFOL = 'R') AND (&AVISO =   'S') AND (&CAUAFA = 60), (&E262 / 12) \* &MESPROPAPFER, 0)) |
| --- |

**(3)Evento 264- 13º API intermitente**

[GIF animado: Imagem 7: (3) Evento 264- 13º API intermitente](https://ajuda.sankhya.com.br/hc/article_attachments/40417209272215)

**Fórmula**

| 264- IF(QueFuncionario.CODCATEGESOCIAL <> 111, 0, IF((&TIPFOL = 'R') AND (&AVISO =   'S') AND (&CAUAFA = 60), (&E262 / 12) \* &MESPROPAP, 0)) |
| --- |

**(3)Evento 265- ⅓ de férias API intermitente**

[GIF animado: Imagem 8: (3) Evento 265- ⅓ de férias API intermitente](https://ajuda.sankhya.com.br/hc/article_attachments/40417209273111)

**Fórmula**

| 265 - IF(QueFuncionario.CODCATEGESOCIAL <> 111, 0, IF((&TIPFOL = 'R') AND (&AVISO =   'S') AND (&CAUAFA = 60), (&E263 / 3), 0)) |
| --- |

| (4)** Exemplo de cálculo com convocação na referência aviso prévio:**   - **Aviso Prévio**  ![Imagem 9: Aviso Prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315079822615)  - **Cálculo**   ![Imagem 10: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079823639)  ![Imagem 11: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079825175)  ![Imagem 12: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049363991)  ![Imagem 13: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079830039)   - **TRCT**   ![Imagem 14: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315049365655)  ![Imagem 15: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315079832471) |
| --- |

---

| (4)** Exemplo de cálculo sem convocação na referência aviso prévio:**   - **Aviso Prévio**   ![Imagem 16: Aviso Prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315049368471)   - **Cálculo**   ![Imagem 17: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049370135)  ![Imagem 18: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079837719)  ![Imagem 19: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049372055)   - **TRCT**   ![Imagem 20: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315079839639)  ![Imagem 21: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315049375767) |
| --- |

##### 2.2 Rescisão a pedido do trabalhador

Quando o trabalhador solicita o desligamento e não existe convocação na referência da rescisão, não há remuneração suficiente para compensar eventual desconto de aviso-prévio. Nessa situação, o sistema gera apenas um evento demonstrativo para possibilitar a comunicação ao eSocial e a emissão dos documentos rescisórios.

(3)**Cadastro do evento demonstrativo**

A) Evento - FOLHA INTERMITENTE SEM VALOR

![Imagem 22: A) Evento - FOLHA INTERMITENTE SEM VALOR](https://ajuda.sankhya.com.br/hc/article_attachments/5723613885591)

![Imagem 23: A) Evento - FOLHA INTERMITENTE SEM VALOR](https://ajuda.sankhya.com.br/hc/article_attachments/5723596392855)

![Imagem 24: A) Evento - FOLHA INTERMITENTE SEM VALOR](https://ajuda.sankhya.com.br/hc/article_attachments/5723648591255)

#### Imagem 25: A) Evento - FOLHA INTERMITENTE SEM VALOR

**Fórmula**

| IF ((QueFuncionario.CODCATEGESOCIAL = 111), IF((&TIPFOL = 'R') AND (&RESCISAODEFINITIVA = 'S') AND ((&TIPOAVISO = 3 AND &CODMOTDESLIGESOCIAL = '07') OR (&TIPOAVISO = 2 AND &CODMOTDESLIGESOCIAL = '2' AND &MESESMEDIAINTERM <= 0)), 0.01, (&TOTPROV - &TOTDESC)),0) |
| --- |

| **⚠️** **Atenção**  O evento **120 – Folha Intermitente sem Valor** possui finalidade exclusivamente demonstrativa. Ele não gera pagamento ao trabalhador e é utilizado apenas para permitir a emissão dos documentos rescisórios e a comunicação do desligamento ao eSocial quando não existirem valores financeiros na rescisão. |
| --- |

| (4)** Exemplo de cálculo sem convocação na referência aviso prévio:**   - **Aviso Prévio**   ![Imagem 26: Aviso Prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315049378071)   - **Cálculo**   ![Imagem 27: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049378967)   - **TRCT**   ![Imagem 28: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315049379095)  ![Imagem 29: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315079847447) |
| --- |

---

| (4)** Exemplo de cálculo com convocação na referência:**  Esse tipo de rescisão acontecerá quando o trabalhador intermitente pede a rescisão do seu contrato de trabalho e há convocação no mês da rescisão. Como não há provento suficiente para abater a indenização do aviso prévio em favor da empresa, é feita a rescisão apenas com os eventos pagos na folha do intermitente para comunicar o eSocial e também para geração dos documentos da rescisão, conforme exemplo:   - **Aviso prévio**   ![Imagem 30: Aviso prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315049382167)   - **Cálculo**   ![Imagem 31: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079848215)  ![Imagem 32: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049383063)  ![Imagem 33: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079849751)   - **TRCT**   ![Imagem 34: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315049384087)  ![Imagem 35: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315079850647) |
| --- |

##### 2.3 Rescisão com justa causa do trabalhador intermitente

No desligamento do colaborador intermitente, as verbas seguem a regra do pagamento mensal, considerando os dias de convocação. São pagos saldo salário, DSR, férias, média e ⅓ de férias, além do 13º salário e suas médias, se houver.

Como férias e 13º salário são pagos proporcionalmente ao trabalhador intermitente durante a execução do contrato, essas verbas somente serão geradas na rescisão quando houver valores decorrentes de convocação na referência.

Se não houver convocação, é gerado apenas um evento demonstrativo para emitir o TRCT e comunicar o eSocial, já que o aviso prévio não se aplica nesse caso.

| (4)** Exemplo de cálculo sem convocação na referência:**   - **Aviso prévio**   ![Imagem 36: Aviso prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315049386007)   - **Cálculo**   ![Imagem 37: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049386391)   - **TRCT**   ![Imagem 38: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315079853207) |
| --- |

---

| **Exemplo cálculo com convocação na referência**   - **Aviso prévio**   ![Imagem 39: Aviso prévio](https://ajuda.sankhya.com.br/hc/article_attachments/42315079854231)   - **Cálculo**   ![Imagem 40: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049388951)  ![Imagem 41: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315049389719)  ![Imagem 42: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/42315079857559)   - **TRCT**   ![Imagem 43: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315049392023)  ![Imagem 44: TRCT](https://ajuda.sankhya.com.br/hc/article_attachments/42315049393815) |
| --- |

**(3)** Próximas etapas:

- **liberar a folha para o eSocial**;
- **enviar os eventos de desligamento ao eSocial (S-2299)**;
- **realizar as integrações financeira e contábil**, quando aplicável;
- **disponibilizar o TRCT e o holerite de rescisão ao trabalhador**.

### 4. Pontos de Atenção

- O aviso prévio no contrato intermitente **é sempre indenizado quando a iniciativa é do empregador**.
- O cálculo do aviso prévio utiliza **a média da remuneração dos últimos 12 meses**.
- A geração do demonstrativo **Folha Intermitente sem Valor** ocorre apenas quando o trabalhador não possui remunerações decorrentes de convocações no período considerado para o cálculo da rescisão. Essa situação não caracteriza erro de processamento.
- Não pode existir **rescisão com saldo negativo para o trabalhador**.
- É fundamental que **todas as folhas de convocação estejam calculadas e fechadas antes da rescisão**.
- Quando não houver convocação no mês da rescisão, será necessário utilizar **evento demonstrativo para registrar o desligamento**.

## Perguntas Frequentes (FAQ)

**1. O aviso-prévio no contrato intermitente pode ser trabalhado?**

Não. Na rescisão sem justa causa por iniciativa do empregador, o aviso-prévio do trabalhador intermitente é sempre indenizado, conforme previsto para essa modalidade de contratação.

**2. Como o sistema calcula o aviso-prévio indenizado?**

O cálculo considera a remuneração recebida pelo trabalhador nos últimos 12 meses anteriores à rescisão ou, se o contrato possuir menos de 12 meses, desde a data de admissão.

**3. O que acontece se o trabalhador não tiver recebido remuneração nos últimos 12 meses?**

Quando não houver convocações com remuneração no período considerado para o cálculo, o sistema gera automaticamente o demonstrativo **Folha Intermitente sem Valor**.

Esse comportamento é esperado e indica apenas que não existem valores para compor a média das verbas rescisórias.

**4. O evento 120 – Folha Intermitente sem Valor gera pagamento ao trabalhador?**

Não. O evento 120 possui finalidade exclusivamente demonstrativa. Ele é utilizado para registrar que não houve remuneração no período considerado para o cálculo da rescisão, sem gerar valores financeiros.

**5. O demonstrativo "Folha Intermitente sem Valor" indica erro no cálculo?**

Não. O demonstrativo é gerado automaticamente quando o trabalhador não possui remuneração decorrente de convocações no período utilizado para o cálculo da rescisão. Nessa situação, o comportamento do sistema é esperado.

**6. É necessário lançar manualmente o evento 120?**

Não. O evento é gerado automaticamente pelo sistema quando as condições para sua utilização são atendidas. Não é necessário realizar lançamentos manuais.

**7. O demonstrativo "Folha Intermitente sem Valor" é enviado ao eSocial?**

Sim. O demonstrativo permite que o sistema gere corretamente as informações necessárias para comunicação da rescisão ao eSocial, mesmo quando não houver valores financeiros decorrentes de convocações no período considerado para o cálculo.

## Artigos Relacionados

- [Contrato de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38961120003095)
- [Cadastro do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38962184136215)
- [Convocação de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38968450402455)
- [Aceite e Comparecimento da Convocação Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38986155986071)
- [Cálculo da Folha do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623)
- [Férias do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39012829384599)
