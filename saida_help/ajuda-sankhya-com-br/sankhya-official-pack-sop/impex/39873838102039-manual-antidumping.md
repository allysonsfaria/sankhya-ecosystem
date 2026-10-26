---
id: "39873838102039"
titulo: "Manual Antidumping"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39873838102039-Manual-Antidumping"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T13:28:00Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Importação", "Impostos", "Financeiro", "Regras", "Antidumping", "Cálculo automático", "Uso nas notas e financeiro", "Nota Fiscal de Nacionalização", "Somar Antidumping à Base do ICMS", "Calcular Antidumping por Peso Líquido"]
---

# Manual Antidumping

#### 1. INTRODUÇÃO

##### 1.1 O que é Antidumping?

Antidumping é um encargo adicional cobrado pelo governo brasileiro sobre produtos importados que são vendidos abaixo do preço justo de mercado, prática que prejudica a indústria nacional. Quando um produto está sujeito a essa medida, o sistema calcula automaticamente o valor do antidumping e o inclui nos custos da importação.

**1.2 Como funciona no sistema?**

##### O processo segue três etapas principais:

1. Cadastro das regras → 2. Cálculo automático → 3. Uso nas notas e financeiro

####

#### 2. CADASTRO DAS REGRAS DE ANTIDUMPING (ETAPA 1)

Inicialmente, é necessário cadastrar as regras que definem os valores de antidumping a serem aplicados para cada produto. Para isso, acesse a tela **“Produtos”** (Configurações » Cadastros » Produtos » Produtos) e, em seguida, vá até a aba **“Antidumping”** (tabela TCEDUMPING).

![Imagem 1: Inicialmente, é necessário cadastrar as regras que definem os valores de antidumping a serem aplicados para cada…](https://ajuda.sankhya.com.br/hc/article_attachments/39873838096407)

Para cada regra, devem ser informadas as seguintes definições:

| **Campo** | **O que preencher** |
| --- | --- |
| Produto | O produto importado sujeito ao antidumping |
| País | O país de origem da importação |
| Parceiro (opcional) | O fornecedor específico, se a regra for diferente por exportador |
| Unidade de Medida (opcional) | Se o cálculo for por tonelada, informe TO |
| % Antidumping | Percentual a aplicar sobre o valor CIF do produto |
| Valor Fixo (US$) | Valor fixo em dólar por unidade ou por tonelada (alternativa ao percentual) |

**OBSERVAÇÃO:** Regras mais específicas com **Parceiro** e **Unidade** preenchidos, possuem prioridade sobre regras mais genéricas, que consideram apenas **Produto** e **País**.

#### 3. CÁLCULO AUTOMÁTICO (ETAPA 2)

Ao processar os itens da importação, o sistema identifica automaticamente o país do exportador e consulta as regras cadastradas.

**3.1 Como o sistema escolhe a fórmula**

O sistema realiza o cálculo seguindo uma ordem de prioridade, utilizando a primeira regra válida encontrada.

**3.1.1 Opção A — Valor Fixo por Quantidade**

Utilizada quando há um valor fixo cadastrado e o cálculo é baseado na quantidade negociada.

- **Fórmula:** Antidumping = Valor Fixo (US$) × Taxa de Câmbio × Quantidade
- **Exemplo:** Valor fixo de US$ 0,50 x Câmbio R$ 5,00 × 100 unidades = R$ 250,00.

**3.1.2 Opção B — Valor Fixo por Tonelada**

Utilizada quando a unidade de medida é **TO (tonelada)** e o cálculo por peso está ativo.

- **Fórmula:** Antidumping = Valor Fixo (US$/ton) × Taxa de Câmbio ÷ 1.000 × Peso Líquido (kg)
- **Exemplo:** US$ 10,00/ton x Câmbio R$ 5,00 ÷ 1.000 × 500 kg = R$ 25,00.

**3.1.3 Opção C — Percentual sobre o Valor CIF**

Utilizada quando não há valor fixo, mas existe um percentual cadastrado. A base de cálculo considera o valor do produto + frete + seguro (CIF).

- **Fórmula:** Base CIF = (Preço Unitário × Câmbio × Quantidade) + Frete + Seguro
- **Fórmula:** Antidumping = Base CIF × % Antidumping
- **Exemplo:** Base CIF R$ 10.000,00 x 12% = R$ 1.200,00.

Se não houver regra cadastrada para o produto/país da importação, o valor de antidumping será **zero**, sem aplicação de encargos.

#### 4. USO DO ANTIDUMPING (ETAPA 3)

Após o cálculo, o valor do antidumping é exibido no campo **“Vlr. Antidumping”** em cada item da importação e é utilizado em dois pontos:

**4.1 Na Nota Fiscal de Nacionalização**

O valor do antidumping é incluído:

- Nas despesas aduaneiras do item
- No valor de destaque da nota fiscal (campo **Outros/Destaque**)

**4.2 No Financeiro**

O sistema gera um lançamento financeiro específico para o antidumping, vinculado às despesas da importação, com o grupo **ANTIDUMPING**.

**ATENÇÃO:** Ao cadastrar a despesa de importação para antidumping, o campo **Grupo** deve ser preenchido exatamente como **ANTIDUMPING**, para que o lançamento financeiro seja gerado corretamente.

#### 5. CONFIGURAÇÕES (PARÂMETROS)

Há dois parâmetros do sistema que controlam o funcionamento do antidumping:

**5.1. Parâmetro "Somar Antidumping à Base do ICMS" (DVC\_SUMANTIDUMP)**

| **Tipo** | **O que acontece** |
| --- | --- |
| Desativado (padrão) | O antidumping é calculado e registrado, sem impactar o ICMS. |
| Ativado | O valor do antidumping é incluído na base de cálculo do ICMS, aumentando o imposto, e também é somado ao valor de destaque da nota. |

- Utilize essa opção apenas quando a legislação exigir que o antidumping componha a base do ICMS.

**5.2 Parâmetro "Calcular Antidumping por Peso Líquido" (IMP\_CALCPESOLIQ)**

| **Tipo** | **O que acontece** |
| --- | --- |
| Desativado (padrão) | O cálculo utiliza a quantidade negociada. |
| Ativado | O cálculo utiliza o peso líquido em toneladas (quando a unidade **TO** estiver cadastrada). |

#### 6. FAQ

- **O antidumping foi calculado como zero. O que verificar?**

1. Verifique se há regra cadastrada para o produto e o país do exportador.
2. Confirme se o parceiro exportador está vinculado a um país no cadastro.
3. Confira se a unidade de medida (**CODVOL**) do item corresponde à definida na regra;

- **O cálculo está usando o país errado. Por quê?**

O sistema identifica o país de exportação com base no parceiro exportador da importação. Se o cadastro do parceiro não tiver cidade e país corretamente preenchidos, o país não será identificado corretamente e o antidumping poderá não ser calculado como esperado.

- **A nota de nacionalização não está incluindo o antidumping. O que fazer?**

Verifique se o parâmetro **“Somar Antidumping à Base do ICMS” (DVC\_SUMANTIDUMP)** está ativado nas configurações do módulo de Comércio Exterior.

- **Posso ter regras diferentes para o mesmo produto dependendo do fornecedor?**

Sim. Cadastre a regra com o **Parceiro** preenchido. Ela terá prioridade sobre a regra genérica (sem parceiro) para esse fornecedor.

#### 7. VISÃO GERAL DO PROCESSO

![Imagem 2: 7. VISÃO GERAL DO PROCESSO](https://ajuda.sankhya.com.br/hc/article_attachments/39873838099095)
