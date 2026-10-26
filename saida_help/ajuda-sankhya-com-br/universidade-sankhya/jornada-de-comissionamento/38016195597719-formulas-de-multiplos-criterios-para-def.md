---
id: "38016195597719"
titulo: "Fórmulas de múltiplos critérios para definição do percentual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38016195597719-F%C3%B3rmulas-de-m%C3%BAltiplos-crit%C3%A9rios-para-defini%C3%A7%C3%A3o-do-percentual"
trilha: "Universidade Sankhya > Jornada de Vendas > Jornada de Comissionamento"
atualizado_em: "2026-07-22T14:02:26Z"
rotulos: ["Produtos", "Configuração", "Fórmulas", "Comissão", "Vendedores", "Comercial"]
---

# Fórmulas de múltiplos critérios para definição do percentual

## Como calcular comissão com fórmulas de múltiplos critérios para definição do percentual

#### Qual o objetivo do cálculo de comissão por fórmula de múltiplos critérios?

O objetivo desse modelo de cálculo é tornar a remuneração mais estratégica e orientada ao comportamento desejado. Ao incorporar variáveis como tipo de produto, perfil do vendedor, condições de pagamento e alcance de metas, a empresa passa a definir percentuais de comissão que estimulam práticas comerciais coerentes com suas prioridades. Dessa forma, a gestão ganha maior controle sobre o desempenho da equipe e assegura uma distribuição mais justa dos ganhos, considerando as particularidades de cada negociação.

#### Quais problemas este recurso resolve?

- Falta de flexibilidade nos modelos tradicionais de comissão;
- Dificuldade em conectar metas individuais aos objetivos da empresa;
- Sensação de injustiça por parte da equipe de vendas ao aplicar regras genéricas;
- Baixo incentivo à venda de produtos estratégicos ou com maior margem;
- Desalinhamento entre o esforço do vendedor e o retorno financeiro.

#### Qual o risco de não utilizar o cálculo de comissão por fórmula de múltiplos critérios?

Ignorar esse recurso pode gerar desalinhamentos entre a estratégia da empresa e o comportamento da equipe comercial. Sem um modelo flexível, baseado em múltiplos fatores, os vendedores podem atuar direcionados apenas por metas genéricas, perdendo foco em resultados realmente estratégicos para o negócio. Além disso, o reconhecimento inadequado do esforço individual tende a reduzir a motivação, aumentando o risco de evasão de talentos e comprometendo a competitividade nas negociações.

#### Cenário de aplicação

**Contexto:** A Axis Ltda adota duas regras para o cálculo de comissão: cada produto tem um percentual próprio, definido com base na sua rentabilidade, e cada vendedor possui um percentual máximo de comissão, conforme sua experiência na empresa. Na prática, o sistema compara os dois percentuais — o do produto e o do vendedor — e aplica sempre o menor. Essa estratégia equilibra o incentivo à venda de produtos rentáveis com o reconhecimento do tempo de casa.

Por exemplo:

- O VENDEDOR 2 possui um percentual máximo de 5%;
- O VENDEDOR 3 possui um percentual máximo de 7%.

Já os produtos seguem os seguintes percentuais:

- Produto A: 6%;
- Produto B: 7%;
- Produto C: 8%.

Em caso de devolução, a comissão deve ser abatida proporcionalmente ao valor devolvido.

**Tarefa:** Siga as orientações indicadas para configurar a fórmula de comissionamento considerando múltiplos critérios. 

#### Chegou a hora de configurar no ERP Sankhya

1. **Configure a comissão dos produtos**

- Acesse a tela **“Produtos”**
  **Menu:** Comercial » Configuração » Cadastros » Produtos
- Utilize o campo de busca para localizar o **“Produto A”**, previamente cadastrado na preparação da jornada;
- Acesse a aba **“Venda”** e preencha o campo “**% Comissão vendedor**” com o valor **6,00**;
- **Salve** a alteração.
  **Atenção!** Replique o mesmo procedimento nos Produtos B e C, com base nos dados apresentados no cenário acima.

2. **Cadastre a fórmula com múltiplos critérios**

- Acesse a tela **“Fórmulas de Comissão”**
  **Menu:** Comercial » Avançado » Fórmulas » Fórmulas de Comissão
- Clique no botão “**+**” (**Cadastrar Fórmulas de Comissão [F8]**);
- Informe o **“Código”** de identificação da fórmula;
- No campo **“Descrição da Fórmula”**, nomeie a fórmula.

Aba **“Região Própria Vendedor”**

- Insira a fórmula no campo destinado às expressões.
  **Obs.:** Para este treinamento, utilize a fórmula:

**LIQ**

**\***

**(IF (  queProd.COMVEND< queVend.COMVENDA, queProd.COMVEND, queVend.COMVENDA ) /100 )**

**\***

**IF( queCab.TIPMOV='V',1,-1)**

![Imagem 1: IF( queCab.TIPMOV='V',1,-1)](https://ajuda.sankhya.com.br/hc/article_attachments/38016156167447)

- Clique no botão “**Salvar**”.

**Atenção!** Na construção das fórmulas, os campos disponíveis podem ser consultados na tela **Dicionário de Dados** (Menu: Configurações » Avançado » Dicionário de Dados). Utilize os links abaixo para aprofundar seus conhecimentos e acelerar o desenvolvimento das fórmulas.

[Ajuda Sankhya - Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados)

[Ajuda Sankhya -  Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o)

3. **Configure a comissão dos vendedores**

- Acesse a tela **“Vendedores/Compradores”**
  **Menu:** Configurações  »  Cadastros  »  Vendedores/Compradores
- Utilize o campo de busca para localizar o cadastro do **VENDEDOR 2**, previamente cadastrado na preparação da jornada;
- Acesse a aba **“Geral”** e preencha o campo **"Comissão venda”** com o valor **5,00**;
- Preencha o campo **“Fórmula Comissão”** com a regra de cálculo criada na aula “Como calcular comissão com fórmulas de múltiplos critérios para definição do percentual”;
- **Salve** a alteração.
  **Atenção!** Aplique o mesmo procedimento no VENDEDOR 3, com base nos dados apresentados no cenário acima.

4. Acesse a tela **“Portal de Vendas”**
   **Menu:** Comercial  »  Consulta  »  Portal de Vendas

- Lance uma nota de venda para cada vendedor configurado nesta atividade, utilizando os produtos já parametrizados, para que as configurações aplicadas nos passos anteriores sejam refletidas no sistema.

#### Correção e repetição

- Revise os registros para confirmar se os valores e percentuais estão corretos;
- Garanta que os lançamentos foram realizados de forma adequada e estão devidamente alinhados com os objetivos do processo;
- Caso haja erro no registro ou na alocação dos valores, refaça a atividade seguindo o passo a passo novamente.
