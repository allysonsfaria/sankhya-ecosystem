---
id: "38016269515671"
titulo: "Comissão escalonada por valor total de vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38016269515671-Comiss%C3%A3o-escalonada-por-valor-total-de-vendas"
trilha: "Universidade Sankhya > Jornada de Vendas > Jornada de Comissionamento"
atualizado_em: "2026-07-22T14:02:25Z"
rotulos: ["Configuração", "Fórmulas", "Vendedor", "Financeiro", "Comercial"]
---

# Comissão escalonada por valor total de vendas

## Como calcular comissão escalonada por valor total de vendas

#### Qual o objetivo de calcular a comissão escalonada por valor total de vendas?

Aplicar a comissão escalonada com base no valor total da venda é uma estratégia que possibilita reconhecer proporcionalmente o desempenho comercial em operações de maior relevância financeira. Esse modelo favorece a construção de negociações mais robustas e estratégicas, à medida que os percentuais de comissão são ajustados conforme faixas de valor. Com isso, a empresa melhora o controle da política de incentivos, promove maior alinhamento com as metas corporativas e estimula a equipe de vendas a maximizar o ticket médio por transação.

#### Quais problemas este recurso resolve?

- Padronização de comissões que não considera o peso financeiro das vendas;
- Falta de incentivo à busca por vendas de maior valor agregado;
- Baixa aderência entre o modelo de comissionamento e os objetivos de margem e lucratividade;
- Dificuldade em aplicar critérios escaláveis e sustentáveis de incentivo;
- Modelo de remuneração desalinhado com o grau de complexidade ou esforço comercial.

#### Quais os riscos de não calcular a comissão utilizando este critério?

A ausência de uma estrutura escalonada pode comprometer a eficiência do modelo de remuneração variável, gerando desestímulo para negociações de maior valor e afetando diretamente indicadores como ticket médio, margem de contribuição e rentabilidade por operação. Além disso, manter uma lógica única para vendas com pesos diferentes tende a gerar percepção de injustiça e dificultar a gestão da performance comercial com foco estratégico.

#### Cenário de aplicação

**Contexto:** A Axis Ltda implementou uma nova estratégia de incentivo para reconhecer o alto desempenho da equipe de vendas. Para isso, ativou o recurso de Comissões por Fórmula, com o objetivo de automatizar os cálculos, agilizar o fechamento e garantir justiça nos pagamentos.

A campanha foi estruturada com base nos seguintes critérios: 

- **Comissões só serão pagas para vendas individuais acima de R$ 500,00;**
  (Vendas com comissão inferior a esse valor serão desconsideradas.)
- **Notas com devolução geram comissão negativa;**
  (A devolução impacta diretamente o resultado do vendedor no período.)
- **O percentual de comissão será aplicado com base no total de vendas no período, conforme a tabela abaixo:**

| Total das Vendas no Período | Comissão do vendedor |
| --- | --- |
| < R$ 20.000,00 | 5% |
| >= R$ 20.000,00 e < R$ 40.000,00 | 6% |
| >= R$ 40.000,00 e < R$ 60.000,00 | 8% |
| >= R$ 60.000,00 | 10% |

**Tarefa:** Siga as orientações abaixo para calcular a comissão da campanha proposta, aplicando as regras definidas.

#### Chegou a hora de configurar no ERP Sankhya

1. **Cadastre a fórmula de comissão**

- Acesse a tela **“Fórmulas de Comissão”**
  **Menu:** Comercial » Avançado » Fórmulas » Fórmulas de Comissão
- Clique no botão “**+**” (**Cadastrar Fórmulas de Comissão [F8]**);
- Informe o **“Código”** de identificação da fórmula;
- Nomeie a fórmula preenchendo o campo **“Descrição da Fórmula”**. Ex.: CAMPANHA.

Aba **“Região Própria Vendedor”**

- Insira a fórmula no campo destinado às expressões.
  **Obs.:** Para este treinamento, utilize a fórmula:

**(LIQ \* IF (queTotalVendas.VALOR > 60000, 10,**

**IF (queTotalVendas.VALOR > 40000, 8,**

**IF (queTotalVendas.VALOR > 20000, 6, 5)))) / 100**

**\* IF (queCab.TIPMOV = 'V', IF (queCab.VLRNOTA > 500, 1, 0), -1)**

![Imagem 1: * IF (queCab.TIPMOV = 'V', IF (queCab.VLRNOTA > 500, 1, 0), -1)](https://ajuda.sankhya.com.br/hc/article_attachments/38016269513751)

- Clique no botão “**Salvar**”.

**Atenção!** Na construção das fórmulas, os campos disponíveis podem ser consultados na rotina **Dicionário de Dados** (Menu: Configurações » Avançado » Dicionário de Dados). Utilize os links abaixo para aprofundar seus conhecimentos e acelerar o desenvolvimento das fórmulas.

[Ajuda Sankhya - Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados)

[Ajuda Sankhya -  Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o)

2. **Configure o cadastro do vendedor**

- Acesse a tela **“Vendedores/Compradores”**
  **Menu:** Configurações  »  Cadastros  »  Vendedores/Compradores
- Utilize o campo de busca para localizar o cadastro do **VENDEDOR 1**, previamente cadastrado na preparação da jornada;
- Preencha o campo **“Fórmula Comissão”** com a regra de cálculo criada no passo anterior;
- **Salve** a alteração.

3. Acesse a tela **“Portal de Vendas”**
   **Menu:** Comercial  »  Consulta  »  Portal de Vendas

- Lance uma nota de venda para o VENDEDOR 1 configurado nesta atividade, para que as configurações aplicadas nos passos anteriores sejam refletidas no sistema.

#### Correção e repetição

- Revise os registros para confirmar se os valores e percentuais estão corretos;
- Garanta que os lançamentos foram realizados de forma adequada e estão devidamente alinhados com os objetivos do processo;
- Caso haja erro no registro ou na alocação dos valores, refaça a atividade seguindo o passo a passo novamente.
