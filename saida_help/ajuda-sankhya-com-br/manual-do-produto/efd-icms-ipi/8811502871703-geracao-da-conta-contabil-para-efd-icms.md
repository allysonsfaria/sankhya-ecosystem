---
id: "8811502871703"
titulo: "Geração da Conta Contábil para EFD ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD ICMS/IPI"
atualizado_em: "2026-09-30T11:14:44Z"
rotulos: ["Configuração", "IPI", "ICMS", "Impostos", "Contabilização", "EFD", "Geração da Conta Contábil para EFD ICMS/IPI", "Registro 0500", "Registro 0300", "Geração da Conta Contábil para ICMS/IPI"]
---

# Processo Geração da Conta Contábil para EFD - ICMS-IPI

**Onde configurar:** [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba **EFD - Escrituração Fiscal Digital**, campo **Tipo da Conta Contábil para EFD ICMS/IPI** (opções **Cadastros** e **Contabilização**). A conta efetivamente usada depende também dos cadastros de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294), [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) e [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116393) — por isso este processo não tem uma única tela de acesso.

Este processo complementa o artigo [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5), que reúne a documentação completa da tela nas versões HTML5 e Flex.

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI#oque)
- [Formas de buscar a conta contábil](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI#formas)
- [Registros e naturezas aceitas](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI#registros)
- [Onde cada registro é gerado](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI#onde)

## O que é e para que serve

O processo de **Geração da Conta Contábil para EFD - ICMS/IPI** define qual conta contábil o sistema usa ao preencher os registros **0300, 0500, C170, C300, C350, C500, D100, D500, D510 e H010** do arquivo da **EFD - Fiscal ICMS/IPI**.

A definição pode vir de duas formas configuráveis: pela hierarquia de cadastros (Produtos, Grupos de Produtos/Serviços e TOP) ou pela contabilização do documento. O registro **H010** é a exceção: tem regra própria, descrita mais adiante.

**ℹ️ Nota**

Este processo não cria contas contábeis nem altera o Plano de Contas; ele só seleciona, entre as contas já cadastradas, qual será usada em cada registro.

---

## Formas de buscar a conta contábil

Nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba **EFD - Escrituração Fiscal Digital**, o campo **Tipo da Conta Contábil para EFD ICMS/IPI** define qual das duas formas abaixo o sistema usa.

### Modo Cadastros

Com esta opção, o sistema busca a conta contábil na seguinte ordem de prioridade:

1. [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) — para produtos, aba **Impostos/Informações por empresa**, campo **Contábil para EFD**; para serviços, tela [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Servi%C3%A7o), aba **Configurações por Empresa**, campo **Contábil para EFD**.
2. **Cadastro de Produtos** — aba **Impostos**, campo **Contábil para EFD**.
3. [Grupos de Produtos/Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598294) — aba **Impostos por Empresa**, campo **Conta contábil para EFD**; aba **Geral**, campo **Conta contábil para EFD**.
4. [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114) — aba **Livro Fiscal**, campo **Conta contábil para EFD**.

**ℹ️ Nota**

Para o registro **D100**, se a TOP tiver a Conta Contábil preenchida, o sistema a utiliza como primeiro nível da hierarquia — invertendo a ordem acima só para esse registro.

### Modo Contabilização

Com esta opção, o sistema verifica a contabilização do documento e usa a conta do lançamento contábil de maior valor, dentro do grupo **Natureza para EFD** configurado. As naturezas buscadas são:

| Código | Natureza para EFD |
| --- | --- |
| 01 | Receita de vendas |
| 02 | Receitas de vendas não tributadas |
| 03 | Receita de fretes; receita de transportes rodoviário de cargas |
| 04 | Custos de produtos/serviços prestados por pessoa jurídica |
| 05 | Custos com transportes |
| 06 | Despesas diversas |
| 07 | Despesas de fretes contratados e despesas de comercialização |
| 08 | Estoques, matéria-prima e material de embalagem |
| 09 | Aquisições de bens para revenda; aquisições de insumos para industrialização |
| 11 | Máquinas e equipamentos do ativo imobilizado, ativo fixo, etc. |

O sistema considera as movimentações pela origem:

- **Estoque** — `TCBINT.ORIGEM` = `'E'` ou `'L'`
- **Financeiro** — `TCBINT.ORIGEM` = `'F'`, `'B'`, `'M'`, `'R'` ou `'J'`
- **Imobilizado**

### Regra própria do registro H010

O campo **10 - COD\_CTA** do registro **H010** (inventário) não segue o campo **Tipo da Conta Contábil para EFD ICMS/IPI** — configurá-lo é um passo separado da escolha entre **Cadastros** e **Contabilização**.

#### 1. Parâmetros

Três parâmetros influenciam a geração do registro H010 do EFD:

| Parâmetro | Descrição | Aplica-se a |
| --- | --- | --- |
| `EFDH010` | "Conta p/inventário (H010) do EFD (SPED FISCAL)" | estoque próprio em poder da empresa |
| `EFDH010_PRTER` | "Conta p/inventário Prop. c/ Terc (H010) do EFD" | estoque próprio em poder de terceiros |
| `EFDH010_TER` | "Conta p/inventário Terceiro (H010) do EFD" | estoque de terceiros em poder da empresa |

Nesses parâmetros, informe contas contábeis fixas para o inventário; a informação incluída nos parâmetros será utilizada para a geração do **Campo 10 (Conta Contábil)** do Registro H010.

Caso uma conta contábil fixa não seja inserida, poderão ser informados valores especiais, de forma que o sistema localizará a conta contábil no [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), aba **Impostos**, onde há a seguinte hierarquia de busca:

- **Conta Contábil 1** — o sistema busca a conta contábil 1.
- **Conta Contábil 2** — o sistema utiliza a conta contábil 2.
- **Conta Contábil 3** — o sistema emprega a conta contábil 3.
- **Conta Contábil 4** — o sistema procura a conta contábil 4.

Assim, o sistema utilizará uma dessas quatro contas contábeis informadas.

#### 2. Configuração por empresa

Para as empresas que geram o registro H010 com Planos de Contas diferentes, a conta contábil pode ser definida por empresa, na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba **EFD - Escrituração Fiscal Digital**, nos campos:

- **Conta p/inventário (H010) do EFD (SPED FISCAL)** — mesma funcionalidade do parâmetro `EFDH010`.
- **Conta p/inventário Prop. c/ Terc (H010) do EFD** — mesma funcionalidade do parâmetro `EFDH010_PRTER`.
- **Conta p/inventário Terceiro (H010) do EFD** — mesma funcionalidade do parâmetro `EFDH010_TER`.

Os campos de seleção de conta possuem pesquisa com busca sob demanda.

#### 3. Ordem de verificação na geração

Ao realizar a geração do registro H010, campo 10 (COD\_CTA), o sistema efetua as seguintes verificações para preencher o campo:

1. **Preferências da Empresa**, aba **EFD - Escrituração Fiscal Digital** — verifica se, para aquele item e para a empresa da qual está sendo gerado o SPED, há configuração em algum dos três campos acima. Se algum deles estiver definido, seu conteúdo será utilizado para alimentar a conta contábil.
2. **Parâmetros** `EFDH010`, `EFDH010_PRTER` e `EFDH010_TER` — utilizados caso não exista configuração nos campos da empresa.
3. **Cadastro de Produtos**, aba **Impostos** — a hierarquia das Contas Contábeis 1 a 4, quando os parâmetros trazem valores especiais em vez de uma conta fixa.

**ℹ️ Nota**

A configuração por empresa sobrescreve os parâmetros globais. Em grupos com várias empresas, é ela que permite que cada empresa leve a sua própria conta ao H010 sem precisar mudar o parâmetro para todas.

---

## Registros e naturezas aceitas

A tabela abaixo resume, para cada registro que recebe conta contábil pelo modo Contabilização, o campo do registro e as naturezas aceitas (ver os códigos no tópico [Formas de buscar a conta contábil › Modo Contabilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI#contabilizacao)). O H010 não entra nesta tabela porque tem [regra própria](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703-Gera%C3%A7%C3%A3o-da-Conta-Cont%C3%A1bil-para-EFD-ICMS-IPI#h010).

| Registro | Campo | Documentos | Naturezas aceitas |
| --- | --- | --- | --- |
| C170 | Campo 37 | Itens do documento (códigos 01, 1b, 04, 55) — registro filho do C100 | 01, 02, 04, 06, 07, 08, 09 |
| C300 | Campo 11 | Resumo diário de notas fiscais de venda a consumidor (código 02) | 01, 02, 04, 06, 07, 08, 09 |
| C350 | Campo 12 | Nota fiscal de venda a consumidor (código 02) | 01, 02, 04, 06, 07, 08, 09 |
| C500 | Campo 33 | Notas fiscais/contas de energia elétrica (códigos 06, 66), fornecimento de água canalizada (código 29) e gás (código 28) | 01, 02, 03, 04, 06, 07, 08, 09 |
| D100 | Campo 23 | Notas fiscais de serviço de transporte (códigos 07, 08, 8b, 09, 10, 11, 26, 27, 57, 67, 63) | 03, 05, 06, 07, 08, 09, 11 |
| D500 (campo 23) / D510 (campo 20) | — | Notas fiscais de serviço de comunicação (código 21) e telecomunicação (código 22) | 06, 07 |

---

## Onde cada registro é gerado

As regras de geração de cada registro — o que ele é, quando sai e o que leva ao arquivo — estão no artigo [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5), no tópico [Demais abas da tela — Blocos 0 a 9](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocos):

- **Registro 0300** — [Bloco 0](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0300) e [Bloco G](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros0300eg125), onde também estão a hierarquia de busca da conta e as condições do campo **Conta Contábil para EFD**.
- **Registro 0500** — [Bloco 0](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0500), gerado conforme o Plano de Contas da empresa.
- **Registro C170** — Bloco C, no tópico dos [registros C170, C173 e C176](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrosc170c173ec176).
- **Registros C300, C350 e C500** — [Bloco C](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blococ).
- **Registro D100** — Bloco D, no tópico do [registro D100](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrod100).
- **Registros D500 e D510** — [Bloco D](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocod).
- **Registro H010** — [Bloco H](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocoh), no detalhamento do inventário.
