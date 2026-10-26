---
id: "40078646183319"
titulo: "Como o sistema calcula a aba Provisões na tela Cálculos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40078646183319-Como-o-sistema-calcula-a-aba-Provis%C3%B5es-na-tela-C%C3%A1lculos"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Provisões de Férias e 13º Salário"
atualizado_em: "2026-10-02T15:39:03Z"
rotulos: ["Configuração", "Provisões", "Folha de Pagamento", "Férias", "13º Salário", "Pessoal+", "Cálculos da folha de pagamento", "Impactos regras de cálculo", "Provisão de férias", "Provisão de 13° salário"]
---

# Como o sistema calcula a aba Provisões na tela Cálculos

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Cálculos
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

### Descrição e Usabilidade

A aba **Provisões** apresenta os valores que a empresa precisa **provisionar contabilmente** para obrigações trabalhistas futuras, como Férias + 1/3 constitucional e 13º salário.

![Imagem 1: A aba Provisões apresenta os valores que a empresa precisa provisionar contabilmente para obrigações trabalhistas…](https://ajuda.sankhya.com.br/hc/article_attachments/40220478145943)

Esses valores representam custos já gerados pelo trabalho do colaborador, mesmo que ainda não tenham sido pagos.

⚠️ Ou seja: a aba Provisões não é apenas informativa — ela é essencial para:

- controle financeiro e contábil;
- auditorias;
- conferência de cálculos;
- previsibilidade de custos da folha.

Para apresentar os valores sugeridos nessa aba, o sistema segue este fluxo:

1. Lê a **Regra de Cálculo vinculada à empresa**;
2. Busca os valores calculados na folha;
3. Classifica as rubricas por natureza (13º, férias);
4. Aplica proporcionalizações (tempo trabalhado);
5. Calcula cada provisão separadamente;
6. Soma os valores e apresenta na aba.

#### **(3)**Provisão de 13º salário

**✔️ Fórmula base**

| Provisão de 13º = (Base de remuneração × avos) / 12 |
| --- |

**✔️ O que entra na base**

Depende da natureza das rubricas:

1. **Base de remuneração**

   Soma de todas as rubricas (eventos) com **natureza de rendimento** classificada como integrante do 13º.

- **Inclui**: salário base, horas extras, abonos/gratificações, adicionais (noturno, insalubridade) e comissões (dependendo da configuração).
- **Não inclui**: descontos (INSS, IR), FGTS e verbas com natureza "não integrante".

**2. Meses trabalhados**

- **Cálculo de avos**: o sistema **não usa fração de dias diretamente no valor final**, ele converte em **avos (meses de direito)**.

  - Trabalhou **15 dias ou mais no mês → conta 1 avo**
  - Trabalhou menos de 15 dias → não conta
- **Dias Trabalhados**: conta desde a admissão até a data do cálculo, descontando afastamentos sem direito (como faltas injustificadas).
- **Dias do Mês**: é definido na **Regra de Cálculo** como **Comercial** (sempre 30 dias) ou **Real** (28, 29, 30 ou 31 dias).

**✔️ Impacto da Regra de Cálculo**

O campo **Considera valores variáveis nas provisões** é fundamental.

- **Marcado**: o sistema usa média dos últimos 12 meses de valores variáveis (ex: comissões) para compor a base → Provisão 13º Variável = (Soma de 12 meses / 12) × Meses Trabalhados
- **Desmarcado**: usa sempre o salário fixo cadastrado.

**O que pode alterar o valor**

- Afastamentos sem direito (faltas, licenças não remuneradas).
- Férias no período.
- Pagamento de adiantamento do 13º.
- Alteração no tipo de mês (comercial X real).

**Exemplo Prático**

**Cenário**:

- Colaborador admitido em 15/01/2024
- Salário Base: R$ 3.000,00
- Mês de cálculo: Março/2024 (tipo de mês: Real - 31 dias)
- Nenhum afastamento

**Cálculo**:

1. **Período trabalhado até Março/2024**:

   - Janeiro: 17 dias (15 a 31)
   - Fevereiro: 29 dias (2024 é bissexto)
   - Março: 31 dias
   - **Total de avos (meses proporcionais)**: 3 avos (pois trabalhou mais de 15 dias em todos os meses)
2. **Provisão do 13º**:  (R$ 3.000 × 3) / 12 = R$ 750,00

#### **(3)**Provisão de Férias

✔️ **Fórmula base**

| Provisão Férias = (Salário × dias acumulados) / 30 \* 1.3333 |
| --- |

**✔️ O que entra na base**

1. **Salário Base**
   Mesmo conceito do 13º, considerando rubricas (eventos) com natureza de rendimento "integrante de Férias".
2. **Dias Acumulados**
   - **Cálculo básico**: a cada mês de trabalho, o colaborador acumula **2,5 dias** de direito a férias (30 dias / 12 meses).
   - **Considerações**: férias já gozadas reduzem o saldo acumulado e afastamentos podem reduzir o acúmulo.
3. **Abono de 1/3**
   É o direito a receber 1/3 do valor das férias em dinheiro, calculado sobre o valor da provisão.

**⚠️Regras importantes**

- 1 mês trabalhado = **2,5 dias de férias**
- 12 meses = **30 dias de direito**

**✔️ Impacto da Regra de Cálculo**

Campos que influenciam:

- **Considera valores variáveis nas provisões**;
- **Tipo de mês**;
- **Configurações de férias** (coletivas, abono) da aba **Propriedades** > **Férias**.
  - **Mantém Períodos Aquisitivos em Férias Coletivas**
    - **Marcado:** mantém ou ajusta o período automaticamente;
      → A provisão pode ser redistribuída entre períodos.
    - **Desmarcado:** congela o período aquisitivo.
      → A provisão pode ficar sem evolução no período.
  - **Calcular Licença Remunerada para funcionários com mais de 1 ano**
    - **Marcado:** complementa saldo com licença remunerada;
      → Pode gerar divisão da provisão entre períodos.
    - **Desmarcado:** considera apenas férias.
      → Pode gerar insuficiência de saldo.
  - **Quita resíduos menores ou iguais que (Dias)**

    - Elimina pequenos saldos automaticamente.

      **Impacto:**

      - evita valores residuais na provisão;
      - ajusta período aquisitivo;

    ⚠️ Fica indisponível se **Mantém Períodos Aquisitivos** estiver marcado.
  - **Abono Pecuniário proporcional ao período de gozo**
    - **Marcado:** 1/3 proporcional;
    - **Desmarcado:** 1/3 integral.

      →  Impacta diretamente o valor da provisão.
  - **Possibilidade de cálculo apenas com pagamento de abono**

    →  Pode reduzir provisão sem gerar afastamento.
  - **Calcula Férias Proporcionais por Período Aquisitivo**
    - **Marcado:** respeita período real;
    - **Desmarcado:** usa regra simplificada (1/12).
  - **Lançar Parte das Férias como Adiantamento**

    → Impacta financeiro, não o total provisionado.
  - **Feriados não computados nas férias**
    - **Marcado:** não desconta feriados → aumenta provisão;
    - **Desmarcado:** desconta → reduz impacto.

**O que pode alterar o valor**

- Férias já gozadas (parcial ou integralmente).
- Afastamentos que impactam a contagem do período aquisitivo.
- Férias em atraso (vencidas há mais de 1 ano), que podem gerar pagamento em dobro.
- Férias coletivas.
- Abono pecuniário.

**Exemplo Prático**

- **Cenário**: 
  - Colaborador com 1 ano de empresa
  - Salário Base: R$ 3.000,00
  - Acumulou 30 dias de férias
- **Cálculo**:
  1. **Provisão base**: R$ 3.000,00 (correspondente a 30 dias).
  2. **Abono (1/3)**: R$ 3.000,00 / 3 = R$ 1.000,00.
  3. **Total da provisão de férias**: R$ 3.000,00 + R$ 1.000,00 = **R$ 4.000,00**
- **Provisão:** (R$ 3.000 × 30) / 30 \* 1.3333 = R$ 3.999,99

### Pontos de Atenção

- A aba Provisões depende **exclusivamente da Regra de Cálculo da empresa**.
- Alterações na regra exigem **reprocessamento da folha**.
- Valores podem variar mês a mês (principalmente com variáveis).
- Empresa com Regime de Férias Coletivas:
  - Provisão reduz quando férias coletivas são agendadas;
  - Acúmulo pode "congelar" durante período coletivo (configurável);
  - Abono é calculado diferentemente (proporcional ao gozo).
- Empresa com Remuneração Variável:
  - Provisão usa **média móvel de 12 meses;**
  - Recalculada mensalmente;
  - Maior precisão, mas valores flutuam.
- Empresa com Sindicato específico:
  - Convenção Coletiva pode redefinir:
    - Dias de férias;
    - Adicional de férias (alguns sindicatos definem 1/4 em vez de 1/3).
- A provisão acompanha o **fechamento da competência**.
- Sem 1 avo completo, não há geração de saldo.
- Antecipações de férias não geram saldo anterior.

### Perguntas Frequentes (FAQ)

**1. Por que a provisão muda todo mês?**

Porque depende de:

- variáveis (comissões, horas extras);
- tempo trabalhado;
- eventos ocorridos no mês.

**2. O sistema usa salário fixo ou média?**

Depende do campo **Considera valores variáveis nas provisões** da Regra de Cálculo vinculada à empresa.

**3. Posso confiar nos valores da aba Provisões?**

Sim. Os valores seguem:

- legislação trabalhista;
- natureza das rubricas;
- regra de cálculo configurada.

**4. Onde vejo o detalhe do cálculo?**

Na própria tela de Cálculos ou relatórios de detalhamento da folha.

### Artigos Relacionados

- [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/39936375428503)
- [Cálculo de Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Cálculo de Férias](https://ajuda.sankhya.com.br/hc/pt-br/articles/7091805775255)
- [Cálculo de 13º Salário](https://ajuda.sankhya.com.br/hc/pt-br/articles/36494077074071)
