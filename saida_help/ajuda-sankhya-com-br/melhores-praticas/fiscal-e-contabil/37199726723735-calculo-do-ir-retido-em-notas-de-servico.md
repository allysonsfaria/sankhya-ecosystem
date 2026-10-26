---
id: "37199726723735"
titulo: "Cálculo do IR Retido em Notas de Serviço com Base Diária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37199726723735-C%C3%A1lculo-do-IR-Retido-em-Notas-de-Servi%C3%A7o-com-Base-Di%C3%A1ria"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:18:49Z"
rotulos: ["Configuração", "Impostos", "Financeiro", "IRRF", "IRRF em notas de Serviço", "Base de Cáculo Diária", "Notas de Serviço", "Cálculo do IR Retido em Notas", "Calcular com Base Diária", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Base Diária"]
---

# Cálculo do IR Retido em Notas de Serviço com Base Diária

O sistema pode não realizar o cálculo automático do Imposto de Renda (IR) ao cadastrar uma nota de serviço devido a configurações de valores mínimos ou de base de cálculo diária. Este artigo explica esse comportamento, os campos e parâmetros que influenciam o cálculo e como conferir os valores apurados.

### Compreendendo a base diária do irrf

No contexto do **IRRF em Notas de Serviço**, **base diária** não significa apenas dividir valores por dias. Na prática, existe um **valor mínimo diário de base de cálculo** que, quando atingido ou ultrapassado, ativa a retenção do imposto. Ou seja, a retenção do IRRF só ocorre se a base diária mínima for alcançada, considerando o número de dias da prestação do serviço.

### Como determinar o valor mínimo diário ou o valor mínimo do imposto

**Exemplo de cálculo do valor mínimo diário (valores de referência, apenas para ilustração):**

- Faixa mensal de isenção (exemplo): **R$ 2.259,20**
- Cálculo do valor mínimo diário:

**2.259,20 ÷ 30 = R$ 75,31 / dia**

- Nesse exemplo, **R$ 75,31** é o **valor mínimo diário** para início da retenção.

Além da base diária, existe também o **valor mínimo do imposto**: quando o valor calculado do IR retido é inferior ao mínimo para retenção (**por exemplo**, R$ 10,00, valor de referência da legislação para dispensa de retenção do IR), o sistema não destaca o imposto na nota. **Exemplo**: se o cálculo do IR resultar em R$ 8,25 e o mínimo for R$ 10,00, não haverá retenção (valores meramente ilustrativos).

### Configuração no sankhya

As configurações são realizadas na tela **“Impostos”** (Configurações » Cadastros » Impostos), no cadastro do imposto de IR retido.

![Imagem 1: Selecione a opção “Calcular com Base Diária?” .](https://ajuda.sankhya.com.br/hc/article_attachments/41143768473239) Selecione a opção **“Calcular com Base Diária?”**.

![Imagem 2: Preencha o campo “Vlr mínimo da Base Diária” com o valor mínimo da base para início da retenção.](https://ajuda.sankhya.com.br/hc/article_attachments/41143800678551) Preencha o campo **“Vlr mínimo da Base Diária”** com o valor mínimo da base para início da retenção.

![Imagem 3: Avalie a opção “Registrar cálculo quando o imposto retido for inferior ao valor mínimo?” (detalhada na seção a seguir).](https://ajuda.sankhya.com.br/hc/article_attachments/41143800678935) Avalie a opção **“Registrar cálculo quando o imposto retido for inferior ao valor mínimo?”** (detalhada na seção a seguir).

![Imagem 4: Nas abas “Parceiro” , “TOP” e “Empresa” , informe os parceiros, tipos de operação e empresas que participarão do…](https://ajuda.sankhya.com.br/hc/article_attachments/41143800679447) Nas abas **“Parceiro”**, **“TOP”** e **“Empresa”**, informe os parceiros, tipos de operação e empresas que participarão do cálculo.

![Imagem 5: Nas abas “Parceiro” , “TOP” e “Empresa” , informe os parceiros, tipos de operação e empresas que participarão do…](https://ajuda.sankhya.com.br/hc/article_attachments/37199726718231)

### Opção “Registrar cálculo quando o imposto retido for inferior ao valor mínimo?”

Com a ativação dessa opção, um registro será incluído na tabela de **Outros Impostos** do documento com o **valor de retenção zerado** caso o imposto não atinja o valor mínimo para retenção.

**IMPORTANTE:** essa funcionalidade foi projetada para garantir a geração dos **rendimentos tributáveis na EFD REINF**, mesmo que a retenção seja dispensada por ser inferior ao valor mínimo (R$ 10,00, valor de referência).

### Parâmetros que influenciam o cálculo

Além da tela de Impostos, os parâmetros abaixo (Configurações » Avançado » Preferências) influenciam a rotina. A combinação validada para o correto funcionamento do cálculo com base diária é:

- **TIPIMPCALCDIA:** Ligado;
- **CALCDIARIONOTA:** Ligado;
- **CALCDIARIOREC:** Desligado;
- **GERIMPOSTO:** Desligado.

Combinações diferentes desses parâmetros podem fazer com que a retenção ocorra em cada nota isoladamente, sem somar as bases do dia, ou com que o valor mínimo configurado não seja respeitado.

### Como o sistema se comporta

A retenção do IRRF ocorre quando a soma das notas de serviço do mesmo dia, para o mesmo parceiro e empresa, atinge a base mínima estabelecida. O cálculo é realizado na nota em que o limite é alcançado, considerando toda a base acumulada do dia.

### Exemplo prático 1 (valores apenas ilustrativos)

- **Base mínima diária (exemplo):** R$ 500,00
- **Critério de soma:** mesmo dia + mesmo parceiro + mesma empresa

### Primeira Nota do Dia

- Valor (exemplo): **R$ 250,00**
- Soma diária: **R$ 250,00**

**Situação:** não atinge a base mínima — **não calcula IRRF**.

### Segunda Nota do Dia

- Valor (exemplo): **R$ 300,00**
- Soma diária acumulada:

**250 (nota 1) + 300 (nota 2) = 550**

**Situação:** ultrapassa a base mínima diária.

- O IRRF é calculado nesta segunda nota;
- Utilizando como base o valor total acumulado do dia: **R$ 550,00** (exemplo).

![Imagem 6: Utilizando como base o valor total acumulado do dia: R$ 550,00 (exemplo).](https://ajuda.sankhya.com.br/hc/article_attachments/37199758700695)

**INFORMAÇÕES ADICIONAIS:** a primeira nota (R$ 250,00, no exemplo) não teve IRRF, mas entra no **total acumulado do dia** que é usado para o cálculo na segunda nota.

### Exemplo prático 2 — imposto inferior ao valor mínimo na primeira nota (valores apenas ilustrativos)

Cenário com duas notas de aquisição de serviço lançadas no mesmo dia, para o mesmo parceiro e empresa, com alíquota de IR de 1,5% e valor mínimo de retenção de R$ 10,00 (valores de exemplo):

- **Nota 1 — R$ 116,34:** o IR calculado isoladamente (R$ 1,75) é inferior ao valor mínimo de R$ 10,00, portanto **não há retenção**. Com a opção “Registrar cálculo quando o imposto retido for inferior ao valor mínimo?” ativa, é gerado o registro em Outros Impostos com retenção zerada, para fins de EFD REINF;
- **Nota 2 — R$ 12.200,03 (mesmo dia):** a base acumulada do dia passa a ser 116,34 + 12.200,03 = **R$ 12.316,37**. A retenção do IR ocorre nesta nota sobre a base acumulada: 12.316,37 × 1,5% = **R$ 184,75** (e não R$ 183,00, que seria o cálculo apenas sobre a segunda nota).

Se, nesse cenário, a retenção estiver ocorrendo em cada nota isoladamente, sem somar as bases do dia, revise os parâmetros indicados na seção “Parâmetros que influenciam o cálculo” e refaça o teste com notas em uma nova data.

## Ponto importante do cálculo

Mesmo que nenhuma nota, de forma isolada, atinja a base mínima (R$ 500,00 no exemplo 1) ou gere imposto acima do valor mínimo (caso da nota de R$ 116,34 no exemplo 2) e o limite seja alcançado apenas na segunda (ou terceira) nota do dia, o IRRF incide sobre o **valor total acumulado do dia**, e não apenas sobre a nota que ultrapassou o limite.

## Pontos de atenção

O controle do cálculo do IRRF considera:

- Data;
- Parceiro;
- Empresa.

Outros pontos importantes:

- Notas de dias diferentes não se acumulam;
- Alteração de parceiro ou empresa zera o valor acumulado;
- Cancelamentos ou estornos de notas podem impactar o cálculo;
- A combinação dos parâmetros TIPIMPCALCDIA, CALCDIARIONOTA, CALCDIARIOREC e GERIMPOSTO deve ser revisada quando a retenção não estiver somando as bases do dia.

Esse comportamento deve estar claramente documentado para evitar divergências fiscais.

## Resumo do funcionamento

A retenção do IRRF ocorre quando a soma das notas de serviço do mesmo dia, para o mesmo parceiro e empresa, atinge a base mínima diária. O cálculo é realizado na nota em que o limite é alcançado, considerando toda a base acumulada do dia. Caso o valor calculado do IR seja inferior ao valor mínimo para retenção, o sistema não destaca o imposto — e, se a opção “Registrar cálculo quando o imposto retido for inferior ao valor mínimo?” estiver ativa, é gerado um registro em Outros Impostos com retenção zerada, garantindo os rendimentos tributáveis na EFD REINF.
