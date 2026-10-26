---
id: "15696666423319"
titulo: "Rendimentos Recebidos Acumuladamente (RRA): como calcular"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-09-27T17:44:18Z"
rotulos: ["Configuração", "Impostos", "ID: br.com.sankhya.rh.ReajusteSalarial", "eSocial", "Entendendo o RRA", "Pessoal+", "ID: br.com.sankhya.rh.CadastroEventos", "IRRF", "RRA", "RRA (Rendimentos Recebidos Acumuladamente)", "Diferença de RRA"]
---

# Rendimentos Recebidos Acumuladamente (RRA): como calcular

**Módulo:** Pessoal+

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular#h_01HP244YG5F2SKXTN6Q8ETF83R)
[Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular#h_01HP244YG505PMR16C5Z9HK28P)
[Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular#h_01HP244YG6MWCS90R41D0MTTNJ)
[Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular#h_01KQW3DSXEW159MHCX61P99DYS)
[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular#h_01KQW3DSXMFMA6A297DR4VTFYE)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319-Rendimentos-Recebidos-Acumuladamente-RRA-como-calcular#h_01KQW3DSXYJY3Y3DKTEJJWQKEE)

---

###

### Descrição e Usabilidade

O **RRA (Rendimentos Recebidos Acumuladamente)** corresponde a valores pagos ao trabalhador que se referem a **anos anteriores ao ano do pagamento**.

Por se tratarem de rendimentos de períodos passados, esses valores têm um **tratamento tributário diferente**, sendo o imposto calculado de forma separada e mais vantajosa para o trabalhador, sendo:

- Tributados **no mês do pagamento**;
- Calculados **separadamente da folha mensal**;
- Com aplicação de uma **tabela de IRRF ajustada pela quantidade de meses**.

⚠️ Isso evita tributação indevida e torna o cálculo mais justo para o trabalhador.

O RRA é aplicado quando há pagamento retroativo, como:

- Dissídio coletivo com efeito em meses anteriores;
- Diferenças salariais;
- Verbas reconhecidas judicialmente;
- Ajustes de remuneração pagos fora da competência original.

**Exemplo prático**

Pagamento realizado em **maio/2026**, referente a diferenças de:

- Outubro/2025
- Novembro/2025
- Dezembro/2025
- 13º salário de 2025
- Janeiro/2026
- Fevereiro/2026
- Março/2026
- Abril/2026

✔️ **Resultado**: esses valores são tratados como RRA e **tributados separadamente**, considerando **4 meses de referência**.

O **envio ao eSocial** segue regras específicas:

- **perApur (S-1210):** mês do pagamento
- **perRef:** períodos anteriores (RRA)

Eventos utilizados:

- **S-1200** → Remuneração
- **S-2299** → Rescisão
- **S-2399** → Trabalhador sem vínculo

⚠️ Quando houver diferença de **13º salário** de ano anterior:

- O **perRef** deve ser informado como **dezembro**;
- O 13º salário conta como **1 mês** na quantidade de meses {qtdMesesRRA} de RRA, conforme dispõe o art. 37 da Instrução Normativa n.º 1.500/2014.

| **XML envio do S-1200** | **XML envio do S-1210** |
| --- | --- |
| ![xml](https://ajuda.sankhya.com.br/hc/article_attachments/42315209097239) | ![XML](https://ajuda.sankhya.com.br/hc/article_attachments/42315193213591) |

### Pré-requisitos

#### **(3)**Configurações necessárias no sistema

**(1)** **Cadastro do Sindicato**

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.Sindicato

---

Na tela [Sindicato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953) (Pessoal+ > Cadastros), informe a [Convenção Coletiva, Acordo Coletivo ou Sentença Normativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953-Sindicato#AbaConven%C3%A7%C3%A3ocoletiva,AcordocoletivoouSenten%C3%A7aNormativa) que determinará o pagamento das verbas.

![Convenção](https://ajuda.sankhya.com.br/hc/article_attachments/15935906687767)

Quando:

- A **Data Base** e a **Data Assinatura** forem de anos diferentes, automaticamente o sistema exige o preenchimento da sub-aba **Rendimentos Recebidos Acumuladamente - RRA**.

![aba](https://ajuda.sankhya.com.br/hc/article_attachments/15742838694039)

Nela, configure o campo **Tipo de Processo** com a opção **Judicial** ou **Administrativo**.

Depois, preencha o campo **Número do Processo para eSocial** conforme a opção selecionada no campo **Tipo de Processo**. Isto é:

- se o **Tipo de Processo** for **Judicial**, o campo será de preenchimento obrigatório com 20 caracteres numéricos;
- caso seja **Administrativo**, será opcional seu preenchimento com 17 ou 21 caracteres numéricos.

Registre o nome do processo no campo **Descrição dos Rendimentos Recebidos Acumuladamente - RRA**.

Informe o **Valor das Despesas de Custas Judiciais** e o **Valor das Despesas com Advogado(s)** somente se o Tipo de Processo for Judicial.

![Rendimentos](https://ajuda.sankhya.com.br/hc/article_attachments/15743271510551)

⚠️ A aba **Advogados** é opcional e só pode ser preenchida após o cadastro prévio dos advogados na tela [Advogados e Escritórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/12601978387479) (Pessoal+ > Cadastros).

![aba](https://ajuda.sankhya.com.br/hc/article_attachments/15743828381079)

**(2)** **Cadastro de Eventos**

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.CadastroEventos

---

Agora acesse a tela [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911) (Pessoal+ > Cadastros), para cadastrar todos os eventos de diferença de RRA.

- **Diferença de RRA**: soma dos valores a receber de anos anteriores.
- **Diferença de 13º salário RRA**: soma dos 13º salários a receber de anos anteriores.
- **INSS RRA**: soma dos descontos de INSS sobre essas diferenças para cálculo do IRRF - RRA.
- **INSS 13º salário RRA**: desconto de INSS sobre 13º salário das diferenças para cálculo do IRRF - RRA.
- **Base IRRF RRA**: soma dos valores sujeitos ao IRRF - RRA, incluindo INSS e 13º salário.
- **IRRF RRA**: valor do IRRF a descontar sobre as diferenças, incluindo 13º salário.

**1.** Na aba **Avançado**, configure o campo **IRRF** com a opção **IRRF RRA**, sinalizando assim que aquele evento compõe a Base de IRRF-RRA. A marcação **Evento de RRA** será ativada automaticamente.

![aba](https://ajuda.sankhya.com.br/hc/article_attachments/15935946507927)

**2.** Na aba **eSocial**, campo **Incidência p/ IRRF** selecione a incidência 15 - Rendimentos Recebidos
Acumuladamente - RRA.

**(3)**  **Vínculo com eventos recalculados**

Após criar os eventos de diferença, vincule-os aos eventos que precisam do cálculo de diferença de RRA.

1. Acesse cada evento marcado como **Tem seus valores recalculados** na aba **Avançado**;
2. Preencha os campos **Evento de Diferença** e **Evento de Diferença - RRA** com os eventos cadastrados.
   O sistema usa o campo **Evento de Diferença** para diferenças do ano corrente e o campo **Evento de Diferença - RRA** para anos anteriores e 13º salário.

![vincular](https://ajuda.sankhya.com.br/hc/article_attachments/15936042184983)

⚠️ Esse vínculo é essencial. Sem ele, o sistema **bloqueia o cálculo da folha de dissídio**.

Eventos que exigem esse vínculo, por exemplo:

- 1 - Salário Base
- 11 - Periculosidade
- 50 - Hora Extra 50%
- 53 - Hora Extra 100%
- 90 - DSR- Horas Extras 50%
- 93 - DSR- Horas Extras 100%
- 650 - Adiant Quinzenal- Percentual
- 651 - Desc Adiantamento Quinzenal
- 653 - Tempo de Serviço
- 9010 - INSS

### Jornada de Uso

A seguir, a jornada para calcular e pagar o RRA no sistema:

**(1)** [**Realizar o Reajuste Salarial**](https://ajuda.sankhya.com.br/hc/pt-br/articles/40242689587095)

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=4abnntGExTY)

**(2)** **Calcular a Folha de Dissídio**

Vá para a tela de **Cálculos** e processe a folha do tipo **Dissídio**. O sistema calculará automaticamente os valores de RRA com base nas configurações realizadas.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=DHmseKaav2I)

**(3)** **Conferir os Valores**

Utilize o **Gerenciador de Folhas** para verificar os valores calculados. Os proventos de RRA (salário e 13º) e os descontos (INSS e IRRF) serão exibidos em eventos separados.

![Gerenciador](https://ajuda.sankhya.com.br/hc/article_attachments/15935679814679)

**Proventos**

- As diferenças aparecem agrupadas no **evento de RRA**;
- São exibidos:

  - Valor de origem;
  - Índice aplicado;
  - Referência original.

[GIF animado: Imagem 10: Referência original.](https://ajuda.sankhya.com.br/hc/article_attachments/15819580482455)

**Descontos**

- As diferenças aparecem no **evento INSS-RRA**;
- Também é exibido o **valor total de IRRF-RRA**, calculado sobre todos os eventos de RRA, inclusive 13º salário.

[GIF animado: Imagem 11: Também é exibido o valor total de IRRF-RRA , calculado sobre todos os eventos de RRA, inclusive 13º salário.](https://ajuda.sankhya.com.br/hc/article_attachments/15819711919127)

A tributação do RRA segue o **art. 37 da IN RFB n.º 1.500/2014**.

Na prática:

- a tabela mensal do IRRF é **multiplicada pela quantidade de meses de RRA**;
- o **13º salário conta como 1 mês adicional**, quando existir.

📌 Exemplo:

- Outubro, novembro, dezembro + 13º salário = **4 meses**;
- A tabela do IRRF é multiplicada por **4**.

![Imagem 12: A tabela do IRRF é multiplicada por 4 .](https://ajuda.sankhya.com.br/hc/article_attachments/15935219258519)

**Tabela RRA- Multiplicação IRRF**

```
  Baixe essa tabela, por meio do link RRA- Multiplicação Tabela IRRF.
```

Na aba [LOG](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031-C%C3%A1lculos#AbaLOG), existe a variável "QMESRRA" que armazena a quantidade de meses considerados. 

![Log](https://ajuda.sankhya.com.br/hc/article_attachments/15821443817879)

Nessa aba também é possível identificar os valores considerados no cálculo:

- Base de IRRF;
- Alíquota aplicada;
- Parcela a deduzir;
- Total de meses de RRA.

![Log](https://ajuda.sankhya.com.br/hc/article_attachments/15935275760151)

Variáveis e funções utilizadas:

- **&QMESRRA** → quantidade de meses de RRA
- **&INSSRRA** → valor de INSS sobre RRA
- **FTFRRA()** → cálculo do IRRF ajustado

**(4)** **Enviar ao eSocial**

Após conferir e fechar a folha, libere os dados para o eSocial. Os valores de RRA serão enviados nos eventos **S-1200** (Remuneração) e **S-1210** (Pagamento), dentro do grupo `infoPerAnt`, conforme o leiaute exigido.

### Pontos de Atenção

- A funcionalidade de RRA só deve ser utilizada para rendimentos cujo pagamento ocorre em um ano-calendário **posterior** ao da competência original.
- A vinculação do **Evento de Diferença - RRA** nos eventos originais (passo 2 dos pré-requisitos) é **crítica**. Sem essa configuração, o sistema bloqueará o cálculo da folha de dissídio e exibirá um alerta com a lista de eventos pendentes de ajuste.
- Conforme o Manual do eSocial, o 13º salário pago como RRA conta como **um mês adicional** para a apuração do IRRF.
- A rotina de RRA funciona apenas com **eventos originais** que impactam o IRRF.
- Eventos sem vínculo com RRA bloqueiam o cálculo.
- A tabela de IRRF é sempre multiplicada pelos meses.
- O cálculo é separado da folha mensal.
- As informações do processo (judicial ou administrativo) cadastradas no Sindicato são enviadas ao eSocial e devem estar corretas.

### Perguntas Frequentes (FAQ)

**1. Por que o IRRF do RRA é menor?**

Porque a tabela é multiplicada pelos meses, reduzindo a carga tributária.

**2. O RRA entra junto com a folha mensal?**

Não. Ele é calculado separadamente.

**3. O sistema calcula automaticamente os meses?**

Sim, através da variável **&QMESRRA**.

**4. Posso usar qualquer evento no RRA?**

Não. Apenas eventos com incidência **IRRF RRA**.

**5. O que acontece se não vincular o evento de diferença?**

O sistema bloqueia o cálculo da folha de dissídio.

### Artigos Relacionados

- [Cadastro de Convenção Coletiva](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953-Sindicato#AbaConven%C3%A7%C3%A3ocoletiva,AcordocoletivoouSenten%C3%A7aNormativa)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Reajuste Salarial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424998383767)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
