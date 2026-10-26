---
id: "37994092910615"
titulo: "Como realizar o lançamento da cotação a partir da tela Análise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37994092910615-Como-realizar-o-lan%C3%A7amento-da-cota%C3%A7%C3%A3o-a-partir-da-tela-An%C3%A1lise-de-Giro"
trilha: "Universidade Sankhya > Jornada de Cotação"
atualizado_em: "2026-07-22T14:03:13Z"
rotulos: ["Produtos", "Cotação", "Análise de Giro", "Estoque", "Sankhya", "Compras"]
---

# Como realizar o lançamento da cotação a partir da tela Análise de Giro

## Geração de cotação a partir da sugestão de compra da análise do Giro

#### Qual é o objetivo e por que esse procedimento é essencial para a tomada de decisões?

O lançamento de uma cotação pode ser feito a partir da tela Análise de Giro, desta forma o processo de compra é alinhado à real necessidade de reposição do estoque, com base na sugestão de compra. Nesse processo pode considerar diferentes critérios como: sugestão de compra, com base no giro ou giro ajustado. Seguindo este padrão a cotação se torna mais ágil e estratégica, estruturando a necessidade de compra e os fornecedores cotados em uma única tela. 

#### Quais problemas este recurso resolve?

- **Rupturas de estoque:** evita excessos de estoque e compras emergenciais de produtos, alinhando reposições à demanda real e reduzindo custos.
- **Falta de automatização do planejamento:** Melhora a gestão de fornecedores e proporciona visibilidade do estoque, assegurando eficiência operacional e financeira.
- **Perdas e obsolescência:** Ao identificar itens de baixa rotatividade ou próximos ao vencimento, reduz perdas e desperdícios.

#### Quais os riscos de não utilizar?

Não utilizar esse recurso expõe a empresa a riscos de ineficiência operacional, com maior chance de erros manuais e compras emergenciais, que resultam em condições comerciais desfavoráveis. A falta de automação e dados consolidados dificulta o planejamento financeiro e prejudica a previsibilidade, impactando o capital de giro e o equilíbrio orçamentário. Esses problemas comprometem a competitividade, afetando prazos, atendimento ao cliente e a capacidade de atender rapidamente às demandas do mercado.

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa Axis Ltda acumulou prejuízos significativos após realizar cotações manuais sem critério. Produtos foram adquiridos em excesso, sem real necessidade, e fornecedores com pouca vantagem comercial foram selecionados para as negociações. A falta de controle e análise gerou desperdícios e impactos no capital de giro.

Com a implementação do ERP Sankhya, o processo de cotação passou a ser conduzido de forma estratégica, com base em dados reais de giro de estoque. A equipe de compras ganhou eficiência e segurança nas decisões, sem aumentar a carga de trabalho ou criar burocracia.

**Tarefa:** Siga as instruções para gerar a cotação com base na sugestão de compra apresentada pela tela Análise de Giro.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Acesse a tela Análise de Giro:**

Comercial >> Rotinas >> Análise de Giro

- Clique no botão **“Outras opções”**
- Marque a opção “**Modo cotação”**
- No campo “**Usar qtd”** informe qual será a sugestão de compra usada para a cotação, as opções são: **Sug. Compra, Sug Compra Giro** e **Sug Compra Giro Ajustado**.
- No painel de “**Itens”**, utilize os botões **“Remove Selecionados”** e “**Remove NÃO selecionados”** para manter no painel apenas os produtos que serão enviados para cotação.

**Clique no botão Preferências, será aberto o popup “Preferências do lançamento de cotações”, nele preencha as informações básicas para o registro da cotação:**

- **Empresa:** Selecione a empresa
- **Centro de resultado:** Compras
- **Natureza:** Receitas de vendas
- **Usuário responsável:** Selecione o comprador responsável
- **Cotar com:** Marque as opções que melhor atendem às necessidades e ao cenário da empresa.

As opções são: 

- **Fornecedor Preferencial**: Gera cotação para parceiros configurados como fornecedor preferencial no **Cadastro do Produto**

**Observação**: Para utilizar essa opção, no cadastro do produto, na aba "**Geral**", o campo "**Parceiro Fornecedor preferencial**" deve estar preenchido

- **Fornecedor com Perfil de Consumo**: Gera cotação para fornecedores que possuem **Perfil de consumo principal** definido para o produto e **Perfil secundário** configurado
- **Quem já Cotou Antes**: Gera cotação para fornecedores que já cotaram o produto (Considera o período configurado no parâmetro QTDMESESJACOTOU)
- **Quem já Forneceu Antes**: Gera cotação para fornecedores que já forneceram o produto (Considera o período configurado no parâmetro QTDMESESJAFORNE)
- Clique em “**OK**” para salvar as preferências
- Clique em **Gerar pedido**
- O sistema abrirá a tela **Cotação**, onde a cotação que acabou de ser gerada está com o Status “**Aberta**”
- Com um duplo clique na cotação, verifique na aba **“Fornecedores e Coleta de Preços”** quais os fornecedores foram sugeridos para a cotação.
- Se os fornecedores sugeridos tiverem a **“Coleta de preço”** igual a **“Online”** clique no botão “**Enviar”** para que os fornecedores preencham a cotação no **“Portal de Cotação Online”.**
- Caso os fornecedores tenham a **“Coleta de preço”** igual a **“Manual”** será necessário fazer a coleta manual dos preços dos produtos a serem cotados.

#### Correção e repetição

- Confirme que todos os campos obrigatórios foram preenchidos de maneira correta e completa.
- Certifique-se de que os valores inseridos estão conforme as políticas e diretrizes da empresa, garantindo conformidade e precisão no pedido.
- Se os valores sugeridos não forem os esperados, revise o processo e corrija as informações necessárias antes de tentar novamente.
- Para reforçar sua habilidade no sistema, pratique criando um novo cenário, como um fornecedor, cliente ou produto diferente.
- Lembre-se de verificar as informações na tela **Cotação** antes de enviar.
