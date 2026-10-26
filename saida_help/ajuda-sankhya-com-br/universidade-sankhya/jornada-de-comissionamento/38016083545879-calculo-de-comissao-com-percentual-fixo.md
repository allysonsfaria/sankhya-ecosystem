---
id: "38016083545879"
titulo: "Cálculo de comissão com percentual fixo por tipo de negociação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38016083545879-C%C3%A1lculo-de-comiss%C3%A3o-com-percentual-fixo-por-tipo-de-negocia%C3%A7%C3%A3o"
trilha: "Universidade Sankhya > Jornada de Vendas > Jornada de Comissionamento"
atualizado_em: "2026-07-22T14:02:27Z"
rotulos: ["Configuração", "Relatórios", "Portal de Vendas", "Vendedor", "Comissão", "Financeiro"]
---

# Cálculo de comissão com percentual fixo por tipo de negociação

## Como realizar o cálculo de comissão com percentual fixo por tipo de negociação

#### Qual objetivo de calcular a comissão com percentual fixo por tipo de negociação?

Apresentar o modelo de comissão com percentual fixo por tipo de negociação como uma estratégia para alinhar as condições de pagamento oferecidas aos clientes com os objetivos financeiros da empresa. Essa abordagem permite configurar percentuais distintos conforme a forma de pagamento, trazendo previsibilidade para o time comercial e maior controle para a gestão.

#### Quais problemas este recurso resolve?

- Desalinhamento entre a política de vendas e o fluxo de caixa da empresa;
- Dificuldade em prever os custos com comissões devido à variação nas condições de pagamento;
- Incentivos que favorecem negociações pouco vantajosas para a empresa;
- Falta de compreensão dos critérios de comissão por parte dos vendedores.

#### Quais os riscos de não calcular a comissão com percentual fixo por tipo de negociação?

Sem uma estrutura de comissão baseada no tipo de negociação, a empresa corre o risco de incentivar práticas comerciais que comprometem o fluxo de caixa, como prazos longos ou parcelamentos excessivos. A ausência de regras claras também dificulta a transparência com a equipe de vendas, gerando insatisfação e dúvidas sobre os ganhos. Além disso, a falta de controle sobre os percentuais aplicados pode impactar negativamente o planejamento financeiro e dificultar a análise do desempenho comercial com base nas condições negociadas.

#### Demonstração prática

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1056845475)

#### Cenário de aplicação

**Contexto:** A Axis Ltda identificou que muitas negociações estavam sendo fechadas com prazos de pagamento pouco vantajosos para o caixa da empresa. Para equilibrar as condições comerciais com os resultados financeiros, a gestão adotou percentuais de comissão diferenciados conforme a forma de pagamento. A medida trouxe mais previsibilidade para a área financeira e ajudou a direcionar o time de vendas a propor condições mais estratégicas.

**Tarefa:** Siga as orientações indicadas para calcular a comissão com percentual fixo por tipo de negociação.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Fórmulas de Comissão”**
   **Menu:** Comercial » Avançado » Fórmulas de Comissão

- Clique no botão “**+**” **(Cadastrar Fórmulas de Comissão)**;
- Informe o **“Código”** de identificação da fórmula;
- Defina a **“Descrição da Fórmula”** no campo indicado. Ex.: **FÓRMULA C/ TIP NEG**

Aba **“Região Própria Vendedor”**

- Insira a fórmula no campo destinado às expressões.
  **Obs.:** Para este treinamento, utilize a fórmula:

**LIQ**

**\***

**IF(queProd.COMVEND=0 AND queVend.COMVEND=0, CTIP/100**

**\***

**IF(queCab.TIPMOV='D',-1,1), IF(queVend.COMVEND = 0, queProd.COMVEND, queVend.COMVEND)/ 100**

**\***

**IF(queCab.TIPMOV='D',-1, 1))**

![Imagem 1: IF(queCab.TIPMOV='D',-1, 1))](https://ajuda.sankhya.com.br/hc/article_attachments/38016141332375)

- Clique no botão “**Salvar**”.

**Importante:** na construção das fórmulas, os campos disponíveis podem ser consultados na rotina **Dicionário de Dados** (Menu: Configurações » Avançado » Dicionário de Dados). Utilize os links abaixo para aprofundar seus conhecimentos e acelerar o desenvolvimento das fórmulas:

[Ajuda Sankhya - Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados)

[Ajuda Sankhya - Fórmulas de Comissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108013-F%C3%B3rmulas-de-Comiss%C3%A3o)

2. Acesse a tela **“Vendedores/Compradores”**
   **Menu:** Configurações  »  Cadastros  »  Vendedores/Compradores

- Utilize o campo de busca e localize o cadastro do vendedor. Ex.: **VENDEDOR 3**

Aba **“Geral”**

- No campo **“Fórmula Comissão”**, informe a regra de cálculo a ser utilizada para o vendedor. Ex.: **FÓRMULA C/ TIP NEG**
- Clique no botão “**Salvar**”.

3. Acesse a tela **“Tipos de Negociação”**
   **Menu:** Comercial » Arquivo » Cadastros » Tipos de Negociação

- Clique em **“Mostrar grade”**;
- Clique no botão “**Atualizar**”;
- Dê um duplo clique no tipo de negociação que estiver alinhado às estratégias da empresa.

Aba **“Características”**

- No campo **“Comissão”**, defina o percentual para o tipo de negociação selecionado;
- Salve as alterações.

4. Acesse a tela **“Portal de Vendas”**
   **Menu:** Comercial  »  Consulta  »  Portal de Vendas

- Lance uma nota de venda com o tipo de negociação configurado nesta atividade e selecione o **VENDEDOR 3** (cadastrado na preparação desta jornada), para que as parametrizações aplicadas nos passos anteriores sejam refletidas no sistema.
  **Importante!** Atente-se ao produto utilizado no lançamento da nota. Para validar esta melhor prática, é essencial que o campo de comissão do produto esteja zerado.

5. **Para validar as comissões configuradas**

- Acesse a tela **“Entradas e Saídas”**

**Menu:** Comercial  »  Relatórios  »  Entradas e Saídas

- Clique na seta lateral para abrir a pasta **“INDICADORES”**;
- Em seguida, abra as pastas **“COMISSIONAMENTO”** e **“(C) CONTROLE DE COMISSÕES”**;
- Dê um duplo clique sobre o relatório **“602 - Comissões sob Faturamento - Tipo de Neg.”**.
  **Parâmetros Relatório**
- Informe o período de referência (data da movimentação) preenchendo os campos **“Dt.Negoc. >=”** e **“Dt.Negoc. <=”**;
- Informe o **“Cód. Vendedor”** utilizado nesta atividade;
- Clique no botão “**OK**”.

**Atenção!** O relatório é alimentado a partir das movimentações de saída e devolução vinculadas ao vendedor e tipo de negociação. Para garantir o controle correto das remunerações variáveis, é fundamental que o vendedor esteja informado na nota de venda.

#### Correção e repetição

- Revise os registros para confirmar se os valores e percentuais estão corretos;
- Garanta que os lançamentos foram realizados de forma adequada e estão devidamente alinhados com os objetivos do processo;
- Caso haja erro no registro ou na alocação dos valores, refaça a atividade seguindo o passo a passo novamente.
