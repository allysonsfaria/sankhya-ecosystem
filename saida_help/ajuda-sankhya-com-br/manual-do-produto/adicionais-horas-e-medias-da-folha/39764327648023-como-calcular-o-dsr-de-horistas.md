---
id: "39764327648023"
titulo: "Como calcular o DSR de horistas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39764327648023-Como-calcular-o-DSR-de-horistas"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Adicionais, Horas e Médias da Folha"
atualizado_em: "2026-10-02T15:37:27Z"
rotulos: ["Configuração", "Cálculo", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Pessoal+", "DSR", "DRS horista", "Tipo de Remuneração", "Cálculo DSR", "Horista"]
---

# Como calcular o DSR de horistas

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Cálculos
**ID da Tela:** `br.com.sankhya.rh.CalculoIndFolha`

---

## Descrição e Usabilidade

O **DSR (Descanso Semanal Remunerado)** é o valor pago ao colaborador referente aos dias de descanso obrigatório, como **domingos, folgas semanais e feriados**, sem que haja prejuízo na sua remuneração.

Para colaboradores **horistas**, esse cálculo é importante porque a remuneração é baseada nas **horas efetivamente trabalhadas**. Ainda assim, a legislação garante que o empregado também receba pelos dias de descanso, desde que tenha cumprido corretamente sua jornada na semana.

Este artigo explica a lógica do cálculo, mostra como realizar o lançamento em cada cenário e orienta como validar a memória de cálculo quando o DSR não aparece separado na folha.

### 1. Descrição da Funcionalidade

O cálculo do DSR para horistas considera as horas trabalhadas no período e os dias de descanso da semana.

**📘 Exemplo prático do DSR do horista**

Imagine um colaborador horista com:

- **Valor da hora:** R$ 10,00
- **Horas trabalhadas na semana:** 44 horas
- **Dias úteis trabalhados:** 6 dias
- **DSR da semana:** 1 dia

A lógica do cálculo pode seguir a fórmula:

> (Valor das horas trabalhadas ÷ dias úteis) × dias de descanso

Aplicando ao exemplo:

> (R$ 440,00 ÷ 6) × 1 = **R$ 73,33**

Esse é o valor correspondente ao DSR da semana.

Dependendo da estrutura configurada na folha, esse valor poderá:

- **demonstrado separadamente na folha**, por meio de evento específico;
- **incorporado ao salário hora**, sem linha exclusiva no demonstrativo.

### 2. Pré-requisitos

Antes de validar o cálculo, confira:

- **Tipo de salário** do colaborador configurado como **Horista**;
- Carga horária corretamente preenchida no cadastro do colaborador;
- Evento de salário hora;
- Movimento utilizado no cálculo:
  - **Salário hora variável**, ou
  - **Salário Horas – Fixo**.
- Fórmula padrão sem personalizações.

### 3. Jornada de Uso

Após validar as configurações, siga o cenário correspondente à necessidade da empresa.

#### **(1)** Lançamento com Salário Hora Variável

Utilize quando a empresa deseja que o DSR seja **demonstrado separadamente na folha**.

1. Inative o evento de **Salário Horas - Fixo**.
2. Acesse a tela **Lançamento de Movimento** (Pessoal+ > Rotinas Folha).
   1. Aplique os filtros pertinentes e localize o **colaborador**.
   2. Inclua o **Evento** de **Salário hora variável**.
   3. Informe a quantidade de horas trabalhadas no campo **Índice**.
   4. **Salve** o movimento.

      ![Imagem 1: Salve o movimento.](https://ajuda.sankhya.com.br/hc/article_attachments/39774451635223)
3. Vá a tela **Cálculos** (Pessoal+ > Rotinas Folha) e execute o cálculo da folha.

   [GIF animado: Imagem 2: Vá a tela Cálculos (Pessoal+ > Rotinas Folha) e execute o cálculo da folha.](https://ajuda.sankhya.com.br/hc/article_attachments/39774418933527)

   Ao finalizar o cálculo, a folha apresentará:

   - **Evento Salário Hora Variável**;
   - **Evento DSR Salário Horas.**

   Nesse cenário, o DSR será exibido em linha própria para conferência.

#### **(2)** Lançamento com Salário Hora Fixo

Utilize este cenário quando o salário do horista já segue uma fórmula fixa da empresa e o DSR deve permanecer incorporado ao salário.

1. Acesse o **cadastro do colaborador** e confirme o**Tipo de Salário** como **Horista**.
2. Valide a configuração do evento de salário padrão.
3. **Não** realize **Lançamento do Movimento**.
4. Execute o cálculo da folha normalmente.

   [GIF animado: Imagem 3: Execute o cálculo da folha normalmente.](https://ajuda.sankhya.com.br/hc/article_attachments/39766700913815)

   Nesse cenário, o sistema:

   - calcula o salário pelas horas previstas;
   - incorpora o DSR dentro do próprio evento do salário;
   - **não apresenta o Evento DSR SALÁRIO HORAS separadamente**.

     A composição poderá ser validada na memória (LOG) de cálculo pela variável:

     `&DIASTRA`

     O DSR está sendo pago, apenas sem linha exclusiva na folha.

### 4. Pontos de Atenção

⚠️ **O sistema não possui uma configuração nativa pdrão** que atenda todos os cenários de cálculo de DSR para colaboradores horistas.

O comportamento padrão hoje é:

- **Salário Horas – Fixo → DSR embutido no salário**
- **Salário Hora Variável → DSR em evento separado**

Se a empresa precisar de uma regra diferente da nativa, como:

- destacar o DSR no cenário fixo;
- separar por sindicato;
- seguir regra do ponto;
- aplicar cálculo específico por escala;

será necessária **personalização de eventos e fórmulas**.

Essa atividade deve ser conduzida por **consultoria especializada**, que poderá inclusive reaproveitar regras já definidas no sistema de ponto para compor a lógica do evento.

### 5. Dicas de Usabilidade

💡 Sempre que houver dúvida sobre "DSR não calculado", valide primeiro:

- se houve lançamento do movimento `SALARIO HORA VARIAVEL`;
- se o cenário utilizado é salário fixo;
- se a memória do cálculo (LOG) contém a variável `&DIASTRA`.

Na maioria dos casos, o chamado ocorre porque espera-se visualizar o DSR separado, mas a empresa utiliza salário hora fixo.

💡 Se a necessidade for **demonstrar o DSR separado do salário hora em cenário fixo**, será necessário:

- criar **evento personalizado**;
- ajustar **fórmula personalizada**;
- reutilizar regras do ponto para cálculo dos descansos;
- validar incidências com consultoria.

Esse tipo de ajuste deve ser conduzido por um **consultor especializado**.

## Artigos Relacionados

- [Cálculo da Folha Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/39311261533335)
- [Lançamento de Atrasos para Desconto de DSR](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119)
- [Cadastro de Carga Horária](https://ajuda.sankhya.com.br/hc/pt-br/articles/38911679393175)
