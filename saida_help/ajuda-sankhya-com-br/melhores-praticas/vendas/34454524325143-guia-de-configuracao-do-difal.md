---
id: "34454524325143"
titulo: "Guia de Configuração do DIFAL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34454524325143-Guia-de-Configura%C3%A7%C3%A3o-do-DIFAL"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-07-22T14:27:05Z"
rotulos: ["Configuração", "NF-e", "DIFAL", "SEFAZ", "ICMS", "Impostos", "Guia de Configuração do DIFAL", "Diferencial de Alíquota do ICMS", "Alíquota interestadual (origem)", "Alíquota interna do destino (cadastro da UF)", "DIFAL seja calculado corretamente"]
---

# Guia de Configuração do DIFAL

O cálculo do **DIFAL (Diferencial de Alíquota do ICMS)** no Sankhya depende de uma série de cadastros e parâmetros.
Este guia apresenta os pontos que devem ser verificados para garantir o funcionamento correto da rotina.

### 1. Partilhas DIFAL

**Caminho:** Configurações » Cadastros » Partilhas DIFAL

- Verifique se existe partilha cadastrada para o ano vigente.
- Configure a **data de início** e o **percentual aplicável** da partilha.

### 2. Cadastro da TOP

**Caminho:** Comercial » Arquivo » Cadastros » Tipos de Operação – TOP

Na TOP utilizada para operações sujeitas a DIFAL, verifique os campos:

(1)** Cálculo de ICMS, IPI e ISS:** deve estar configurado para calcular ICMS (ex.: Calcula e Digita/Calcula e Não Digita);

(1)** Calcular DIFAL Partilhado:** deve estar marcado;

(1)** Tem ICMS?:** deve estar marcado;

(1)** Classificação ICMS:**

**(2)** Caso esteja definido como **Consumidor Final Não Contribuinte**, a classificação será levada diretamente da TOP;

**(2)**Caso esteja configurado para buscar do **Parceiro**, será necessário validar também o cadastro do parceiro.

### 3. Configuração de Parceiros

**Caminho:** Configurações » Cadastros » Parceiros

**No cadastro do parceiro:**

(1)** Estado (UF):** conferir se está informado corretamente;

(1)** Classificação ICMS:** deve estar definido como **Consumidor Final Não Contribuinte** quando aplicável.

**Atenção:** o sistema calcula o **DIFAL apenas para Consumidor Final Não Contribuinte de outra UF**.

### 4. Cadastro de Produtos

**Caminho:** Configurações » Cadastros » Produtos » Produtos

**Verifique se cada produto possui:**

(1)** Tributação de ICMS** configurada corretamente;

(1)** NCM válido** (alguns cenários dependem dele para definição da alíquota interestadual).

**Campos obrigatórios:**

(1)**Calcula ICMS:** deve estar marcado;

(1)** Calcula DIFAL Partilhado:** deve estar marcado.

### 5. Cadastro de Alíquotas de ICMS

**Caminho:** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

**Na regra de ICMS da nota em questão, valide:**

(1)** Alíquota interna do destino** configurada corretamente.

(1)** Alíquota interestadual** deverá estar preenchida.

(1)** Tipo de Cálculo de DIFAL** configurado.

Essas **informações são essenciais para que o sistema apure corretamente** a diferença do DIFAL.

![Imagem 1: Essas informações são essenciais para que o sistema apure corretamente a diferença do DIFAL.](https://ajuda.sankhya.com.br/hc/article_attachments/35006267013015)

### 6. Regras de Partilha do DIFAL

No Sankhya é necessário configurar as regras de partilha:

**(1)** Percentual destinado à **UF de origem** e à **UF de destino**, conforme legislação vigente.

  **Observação:** até 2021 havia partilha; a partir de **2022 o valor integral é destinado à UF de destino** (validar se o parâmetro está ajustado).

### Resumindo

No momento da emissão da NF-e, o sistema considera:

- **Alíquota interestadual (origem);**
- **Alíquota interna do destino (cadastro da UF);**
- Calcula a diferença entre elas → **DIFAL**.

Para que o **DIFAL seja calculado corretamente, é indispensável que todos os cadastros listados acima estejam configurados de forma adequada**. Verifique cada item antes da emissão da NF-e.

### Exemplo de rejeição e XML

Se ao emitir uma NF-e o **Valor do ICMS Interestadual para a UF de Destino (vICMSUFDest)** divergir do cálculo da SEFAZ, é necessário revisar os cadastros acima.

EX de XML

![Imagem 2: EX de XML](https://ajuda.sankhya.com.br/hc/article_attachments/35006292610711)

####

#### Confira também links relacionados à rotina:

[Alíquota Interna de Destino](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abaalquotainternadedestino)

[Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934)

[Partilha DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111373)

[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114)

[Tipos de Cálculos de Difal / Formulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/24110650363031-Quais-tipos-de-c%C3%A1lculos-de-Difal-est%C3%A3o-dispon%C3%ADveis-no-sistema)
