---
id: "38015580716311"
titulo: "Cálculo de comissão com percentual fixo por vendedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38015580716311-C%C3%A1lculo-de-comiss%C3%A3o-com-percentual-fixo-por-vendedor"
trilha: "Universidade Sankhya > Jornada de Vendas > Jornada de Comissionamento"
atualizado_em: "2026-07-22T14:02:29Z"
rotulos: ["Configuração", "Relatórios", "Portal de Vendas", "Comissão", "Vendedores"]
---

# Cálculo de comissão com percentual fixo por vendedor

## Como realizar o cálculo de comissão com percentual fixo por vendedor

#### Qual objetivo de calcular a comissão com percentual fixo por vendedor?

O cálculo de comissões é um processo que determina quanto um vendedor será remunerado, podendo variar de acordo com regras estabelecidas. Apresentar o cálculo de comissão com percentual fixo por vendedor pode ser vista como uma alternativa prática e estruturada para empresas que buscam clareza e padronização nos padrões de comissionamento. Esse modelo permite definir um percentual individual de comissão para cada profissional de vendas, facilitando o entendimento da remuneração e promovendo maior alinhamento com os objetivos comerciais.

#### Quais problemas esse recurso resolve?

- Falta de clareza nas regras de remuneração para a equipe comercial;
- Dificuldade em prever o impacto financeiro das comissões;
- Conflitos internos causados por percepções de desigualdade;
- Complexidade na conferência e auditoria dos pagamentos;
- Risco de insatisfação por regras inconsistentes ou mal aplicadas.

#### Quais os riscos de não utilizar o cálculo com percentual fixo por vendedor?

Deixar de aplicar um modelo com percentual fixo por vendedor pode gerar insegurança na equipe comercial, o que dificulta o entendimento sobre como a remuneração é construída. Isso tende a impactar diretamente a motivação e o desempenho, além de abrir margem para disputas internas e questionamentos constantes. Sem um critério claro e individualizado, aumentam as chances de erro nos cálculos e a dificuldade no controle dos pagamentos, exigindo mais tempo e esforço para ajustes e retrabalho — o que compromete tanto a eficiência operacional quanto a credibilidade do processo.

#### Demonstração prática

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1056861132)

#### Cenário de aplicação

**Contexto:** A Axis Ltda ampliou sua equipe de vendedores e, considerando as diferenças de performance e tempo de casa entre eles, decidiu adotar percentuais fixos de comissão por vendedor. A mudança visa trazer mais previsibilidade para a empresa e mais clareza para a equipe comercial, alinhando expectativas e facilitando a gestão dos pagamentos.

**Tarefa:** Siga as orientações indicadas para definir o percentual fixo de comissão por vendedor.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Vendedores/Compradores”**
   **Menu:** Configurações  »  Cadastros  »  Vendedores/Compradores

- Utilize o campo de busca e localize o cadastro do vendedor, como o **VENDEDOR 1**, por exemplo.

Aba **“Geral”:**

- Informe o percentual fixo do vendedor no campo **“Comissão venda”**, como 4,00, por exemplo;
- No campo **“Fórmula Comissão”**, informe a regra de cálculo a ser utilizada para o vendedor. Ex.: **FÓRMULA PADRÃO - VENDEDOR**;
- Clique no botão “**Salvar**”.

2. Acesse a tela **“Portal de Vendas”**
   **Menu:** Comercial  »  Consulta  »  Portal de Vendas

- Lance uma nota de venda e selecione o vendedor definido anteriormente, para que as parametrizações aplicadas nos passos anteriores sejam refletidas no sistema.

3. **Para validar as comissões configuradas**

- Acesse a tela **“Entradas e Saídas”**

**Menu:** Comercial  »  Relatórios  »  Entradas e Saídas

- Clique na seta lateral para abrir a pasta **“INDICADORES”**;
- Em seguida, abra as pastas **“COMISSIONAMENTO”** e **“(C) CONTROLE DE COMISSÕES”**;
- Dê um duplo clique sobre o relatório **“601 - Comissões sob Faturamento - Vendedor”**.
  **Parâmetros Relatório**
- Informe o período de referência (data da movimentação) preenchendo os campos **“Dt.Negoc. >=”** e **“Dt.Negoc. <=”**;
- Informe o **“Cód. Vendedor”** utilizado nesta atividade;
- Clique no botão “**OK**”.

**Atenção!** O relatório é alimentado a partir das movimentações de saída e devolução vinculadas ao vendedor. Para garantir o controle correto das remunerações variáveis, é fundamental que o vendedor esteja informado na nota de venda.

#### Correção e repetição

- Revise os registros para confirmar se os valores e percentuais estão corretos;
- Garanta que os lançamentos foram realizados de forma adequada e estão devidamente alinhados com os objetivos do processo;
- Caso haja erro no registro ou na alocação dos valores, refaça a atividade seguindo o passo a passo novamente.
