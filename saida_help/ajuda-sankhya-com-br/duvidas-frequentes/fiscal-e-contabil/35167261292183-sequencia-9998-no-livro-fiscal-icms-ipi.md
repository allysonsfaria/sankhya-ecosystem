---
id: "35167261292183"
titulo: "Sequência 9998 no Livro Fiscal ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35167261292183-Sequ%C3%AAncia-9998-no-Livro-Fiscal-ICMS-IPI"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:25:54Z"
rotulos: ["Configuração", "Fiscal", "ICMS", "Transporte", "TOP", "Livro Fiscal", "Sequência 9998 no Livro Fiscal ICMS/IPI", "diferença no cálculo do ICMS do frete", "ICMS informado no cabeçalho não confere com o ICMS calculado sobre a base de frete", "Sequência 9998", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Sequência 9998 no Livro Fiscal ICMS/IPI

A sequência **9998** indica **diferença no cálculo do ICMS do frete**. Ela é criada no Livro Fiscal quando o ICMS informado no cabeçalho não confere com o ICMS calculado sobre a base de frete.

## Entendendo o problema

### Principais causas da divergência

**1. Arredondamento na proporcionalização de despesas**

Quando há valores de **"frete"**, **"seguro"**, **"embalagem"** ou outras despesas no rodapé da nota, esses valores precisam ser rateados proporcionalmente entre os itens. Durante esse processo, podem ocorrer arredondamentos que geram diferenças de centavos.

**Exemplo prático:**

Frete total: R$ 10,00
3 itens na nota com valores diferentes
Ao ratear proporcionalmente, podem surgir valores como R$ 3,33 + R$ 3,33 + R$ 3,34 = R$ 10,00

**2. Cálculo do ICMS item a item**

O sistema calcula o ICMS individualmente para cada item e depois soma os valores. Esse processo pode gerar pequenas diferenças em relação a um cálculo feito diretamente sobre o total da nota.

**3. Redução de base de cálculo**

Quando há **"redução de base de cálculo do ICMS"**, os arredondamentos podem se multiplicar, gerando divergências de centavos entre o valor calculado item a item e o valor total esperado.

### Como o sistema trata essas diferenças

O ERP Sankhya possui mecanismos para identificar e tratar essas pequenas divergências, gerando sequências especiais nos **"Livros Fiscais"** (Fiscal >> Livros Fiscais >> Cadastro Livro ICMS/IPI):

- **Sequência 9999**: Indica diferença entre a base de ICMS do cabeçalho e o total da nota. Serve para ajustar automaticamente pequenas diferenças de arredondamento, garantindo que os valores totais estejam corretos.
- **Sequência 9998**: Indica diferença no cálculo do ICMS do frete. É criada quando o ICMS informado no cabeçalho não confere com o ICMS calculado sobre a base de frete.

### Detalhamento da Sequência 9998

A sequência 9998 ocorre quando:
Nota fiscal de **"frete próprio"** ou nota só de frete.
Divergências entre a alíquota usada e a **"base de ICMS do frete"**.
Arredondamentos incorretos ou ajustes manuais no valor do ICMS.

![Imagem 1: A sequência 9998 ocorre quando: Nota fiscal de "frete próprio" ou nota só de frete. Divergências entre a alíquota usada…](https://ajuda.sankhya.com.br/hc/article_attachments/35553569856919)

## Quando a sequência 9998 acontece

- Nota fiscal de **frete próprio** ou **nota só de frete**;
- Divergências entre a **alíquota usada** e a **base de ICMS do frete**;
- Arredondamentos incorretos ou ajustes manuais no valor do ICMS.

## Configurações que influenciam o cálculo

Na tela **“Tipos de Operação - TOP”** (Comercial » Arquivo » Cadastros » Tipos de Operação), a aba **“Despesas Acessórias”** possui configurações importantes:

- “ICMS Proporcional ao ICMS dos Itens”;

Na aba **“Impostos”** da TOP, o campo **“IPI incide na base de ICMS?”** também pode afetar os cálculos do ICMS do frete.

### SOLUÇÃO (Sequência 9998)

![Imagem 2: Realize as seguintes análises:](https://ajuda.sankhya.com.br/hc/article_attachments/41144639283991) Realize as seguintes análises:

- Confira no **TGFCAB**:

  - VLRICMS (valor do ICMS total);
  - ICMSFRETE e BASEICMSFRETE;

  Cheque a proporcionalização de frete na **TGFDIN**.

![Imagem 3: Em seguida, de acordo com as análises, execute uma das ações corretivas abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/41144639284631) Em seguida, de acordo com as análises, execute uma das ações corretivas abaixo:

- Corrija a **alíquota aplicada no frete**;
- Ajuste a base e o valor de ICMS do frete para que fechem com o cálculo;
- Valide se a configuração da TOP está correta para operações de transporte.

## Exemplo prático de ajuste (valores apenas ilustrativos)

**TGFCAB.ICMSFRETE** = R$ 120,00

Cálculo efetivo (BASEICMSFRETE R$ 1.000,00 × 12%) = **R$ 118,00**

Nesse exemplo, o sistema gera a **sequência 9998**. Para resolver, ajuste o ICMS do frete para **R$ 118,00**.

## Conclusão

A sequência 9998 no Livro Fiscal sinaliza uma divergência entre o ICMS do frete informado no documento e o ICMS calculado sobre a base de frete. Por representar uma inconsistência efetiva — e não um arredondamento aceitável — ela deve sempre ser investigada e corrigida, ajustando a alíquota, a base e o valor de ICMS do frete ou a configuração da TOP, de modo a garantir a conformidade fiscal das operações.
