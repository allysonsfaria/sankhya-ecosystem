---
id: "38988468841623"
titulo: "Como calcular a folha do trabalhador intermitente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623-Como-calcular-a-folha-do-trabalhador-intermitente"
trilha: "Manual do Produto > Pessoas+ > Contratos Especiais > Contrato Intermitente"
atualizado_em: "2026-10-02T15:22:53Z"
rotulos: ["INSS", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "FGTS", "Pessoal+", "IRRF", "Contrato de trabalho Intermitente", "111 - Empregado - Contrato de trabalho intermitente", "S-1210 – Pagamentos de rendimentos do trabalho", "FPRELATHOLINT", "Trabalhador Intermitente"]
---

# Como calcular a folha do trabalhador intermitente

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Cálculos
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

## Descrição e Usabilidade

O cálculo da folha do trabalhador intermitente é realizado **ao final de cada período de prestação de serviço**, considerando as horas ou dias efetivamente trabalhados na convocação.

Essa modalidade de contratação foi regulamentada pela **Lei nº 13.467/2017 (Reforma Trabalhista)** e permite que o trabalhador preste serviços **de forma não contínua**, sendo convocado apenas quando há necessidade da empresa.

No sistema, o cálculo considera automaticamente as informações da **convocação registrada**, incluindo período trabalhado e carga horária, para apurar os valores proporcionais que devem ser pagos ao trabalhador.

### 1. Descrição da Funcionalidade

O cálculo da folha intermitente permite apurar a remuneração do trabalhador considerando as convocações realizadas e confirmadas.

Ao final de cada convocação, o trabalhador recebe proporcionalmente:

- salário referente às horas ou dias trabalhados;
- férias proporcionais + adicional de 1/3;
- 13º salário proporcional;
- repouso semanal remunerado (DSR);
- adicionais legais, quando houver (hora extra, adicional noturno, insalubridade ou periculosidade).

Também são aplicados os encargos obrigatórios:

- **FGTS**, depositado sobre a remuneração;
- **INSS e IRRF**, descontados conforme a legislação vigente.

Diferentemente do contrato tradicional, o trabalhador intermitente recebe **todos esses valores proporcionalmente ao final de cada período de trabalho**.

### 2. Pré-requisitos

Antes de realizar o cálculo da folha intermitente, verifique se:

- O **funcionário intermitente está cadastrado no sistema**.
- A **convocação de trabalho foi registrada na referência**.
- O **aceite e o comparecimento da convocação foram confirmados**.

### 3. Jornada de Uso

**(1)** O cálculo da folha intermitente pode ser realizado **de forma** [**individual**](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623-Como-calcular-a-folha-do-trabalhador-intermitente#h_01KKH8JPKCGZANC0648RKTD851) **ou** [**coletiva**](https://ajuda.sankhya.com.br/hc/pt-br/articles/38988468841623-Como-calcular-a-folha-do-trabalhador-intermitente#h_01KKH8JPN3RK8N9HGT40QBNP23).

#### **(2)**Cálculo Individual do Intermitente

[GIF animado: Imagem 1: (2) Cálculo Individual do Intermitente](https://ajuda.sankhya.com.br/hc/article_attachments/39035162225943)

1. Acesse a tela **Cálculos** (Pessoal+ > Rotinas Folha).
2. Selecione o modo **Individual**.
3. Escolha o tipo de folha **Intermitente**.
4. Informe:

   - **Referência**
   - **Data de Pagamento**
   - **Empresa**
   - **Funcionário**
5. Selecione a **Convocação** cadastrada anteriormente, o sistema preencherá automaticamente:

   - **Data de Início**
   - **Data de Fim**
   - **Sequência:** indicará quantas convocações estão sendo realizadas no mês.
6. Clique em **Próximo** ou na etapa **Calcular**.
7. Defina o modo de cálculo utilizando ou não log:

   - **Calcular sem log**
   - **Calcular com log**
   - **Calcular com log de incorporações**
8. Clique em **Calcular** para processar a folha.
9. Após o processamento, os valores calculados poderão ser analisados nas abas da tela.
10. Se os valores estiverem corretos, clique em **Confirmar Folha**.

**Observações importantes**

- É possível calcular **mais de uma folha intermitente no mesmo mês**, caso existam várias convocações.
- Caso uma convocação tenha início em um mês e término em outro, será necessário **calcular a folha em cada referência correspondente**.
- Se existir cálculo pendente de referência anterior, o sistema exibirá a mensagem:

  **"Não foi possível realizar o cálculo de intermitente na referência atual pois existem cálculos em aberto em referências anteriores."**

| **Exemplo prático de cálculo do intermitente**  Trabalhador intermitente com **salário-hora de R$ 15,00**, que foi convocado para trabalhar **32 horas em determinado período**.  **Salário:** 32h × R$ 15,00 = **R$ 480,00**  **DSR (Descanso Semanal Remunerado):** R$ 480,00 ÷ 6 = **R$ 80,00**  **Base para cálculos proporcionais:** Salário + DSR = **R$ 560,00**  **13º proporcional:** R$ 560,00 ÷ 12 = **R$ 46,67**  **Férias proporcionais:** R$ 560,00 ÷ 12 = **R$ 46,67**  **1/3 constitucional de férias:** R$ 46,67 ÷ 3 = **R$ 15,56**  **Total bruto:** **R$ 668,90**  **Descontos:**  Sobre o valor bruto incidem os descontos legais:   - **INSS:** aplicado sobre R$ 668,90, conforme a faixa da tabela vigente. - **IRRF:** quando aplicável, conforme a base de cálculo e tabela vigente.   O **valor líquido** será o total bruto **menos os descontos de INSS e IRRF**, quando houver. |
| --- |

#### **(2)**Cálculo Coletivo do Intermitente

O cálculo coletivo permite processar **vários trabalhadores intermitentes ao mesmo tempo**.

[GIF animado: Imagem 2: O cálculo coletivo permite processar vários trabalhadores intermitentes ao mesmo tempo .](https://ajuda.sankhya.com.br/hc/article_attachments/38993754899095)

1. Na tela **Cálculos**, selecione o modo **Coletivo**.
2. Escolha o tipo de folha **Intermitente**.
3. Informe a **Referência** e a **Data de Pagamento**.
4. **Empresas**
   Selecione a(s) **Empresa(s)** que realizará(ão) o pagamento.
5. **Departamentos**
   Escolha o(s) **Departamento(s)** dos funcionários convocados.
6. **Funcionários**
   Selecione os **funcionários intermitentes** que receberão o pagamento clicando em seus respectivos cards.
7. Clique em **Calcular** para processar as folhas.

Após o processamento, os resultados poderão ser conferidos e confirmados na tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folhas).

[GIF animado: Imagem 3: Após o processamento, os resultados poderão ser conferidos e confirmados na tela Gerenciador de Folhas (Pessoal+ >…](https://ajuda.sankhya.com.br/hc/article_attachments/38994172612887)

1. Ao acessar a tela, informe e **Empresa** e a **Referência**.
2. Clique em **Pesquisar** e depois sobre o card da folha para realizar a conferência.

**(2)** Após calcular todas as convocações do mês, é necessário consolidar os valores no cálculo mensal.

Esse cálculo consolida os valores das folhas intermitentes para fechamento da folha do período.

**Exemplo:** cálculo individual mensal

[GIF animado: Imagem 4: Exemplo: cálculo individual mensal](https://ajuda.sankhya.com.br/hc/article_attachments/39035273392151)

**(3)**  **Após confirmar o cálculo da folha**, é necessário realizar as seguintes etapas operacionais:

- efetuar as **integrações financeira e contábil**;
- **liberar as folhas para o eSocial**;
- realizar o envio do evento **S-1210 – Pagamentos de Rendimentos do Trabalho**;
- disponibilizar ou **enviar o holerite ao trabalhador** para conferência dos valores pagos.

  | ⚠️ A emissão do **Holerite Intermitente** pode utilizar um layout personalizado, conforme a configuração do parâmetro **Holerite Intermitente - FPRELATHOLINT**.  Quando esse parâmetro estiver preenchido com o código de um relatório cadastrado na tela **Relatórios Formatados**, o sistema utilizará o relatório personalizado informado. Caso o parâmetro não esteja preenchido, será utilizado o relatório padrão Sankhya. |
  | --- |

### 4. Pontos de Atenção

- O cálculo da folha intermitente **só deve ser realizado após o registro do aceite e comparecimento da convocação**.
- Caso existam **cálculos pendentes de referência anterior**, o sistema não permitirá calcular a referência atual.
- É possível realizar **várias folhas intermitentes dentro da mesma referência**, dependendo do número de convocações realizadas.
- Parâmetro **Usa demonstrativo por RPA autônomo/intermitente? - FPUSARPAAUTINT:**

  - quando este parâmetro estiver **ligado**, o sistema envia ao eSocial um **demonstrativo de valores (dmDev) por convocação**, através dos eventos:

    - **S-1200 – Remuneração do trabalhador**;
    - **S-1210 – Pagamentos de rendimentos do trabalho**.

    Nesse caso, cada convocação calculada gera um demonstrativo específico.
  - Quando o parâmetro estiver **desligado**, os valores enviados ao eSocial serão **consolidados na folha mensal**, ou seja, os eventos considerarão o total da remuneração do trabalhador no período.

    **Importante:** esse parâmetro **só pode ser alterado antes do envio dos eventos de remuneração ao eSocial**.
- Além do processamento da folha, a empresa também deve cumprir **obrigações legais relacionadas ao contrato intermitente**:

  - **efetuar o depósito do FGTS** sobre a remuneração do trabalhador;
  - **informar os eventos de remuneração e pagamento no eSocial**, dentro dos prazos legais;
  - **recolher os encargos patronais**, como INSS, RAT e contribuições a terceiros, quando aplicáveis.

### 5. Dicas de Usabilidade

- Sempre **confira as convocações selecionadas antes de calcular a folha**, garantindo que o período esteja correto.
- Utilize o cálculo com **log** quando for necessário analisar detalhadamente o processamento da folha.
- Após calcular todas as convocações do período, **não se esqueça de consolidar os valores no cálculo mensal**.

## Artigos Relacionados

- [Contrato de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38961120003095)
- [Cadastro do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38962184136215)
- [Convocação de Trabalho Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38968450402455)
- [Aceite e Comparecimento da Convocação Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/38986155986071)
- [Férias do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39012829384599)
- [Rescisão do Trabalhador Intermitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/5719927112215)
