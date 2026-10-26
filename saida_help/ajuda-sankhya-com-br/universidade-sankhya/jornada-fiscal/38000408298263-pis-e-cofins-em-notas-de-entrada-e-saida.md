---
id: "38000408298263"
titulo: "PIS e COFINS em Notas de Entrada e Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000408298263-PIS-e-COFINS-em-Notas-de-Entrada-e-Sa%C3%ADda"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-09-25T13:29:54Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "COFINS", "PIS", "Impostos"]
---

# PIS e COFINS em Notas de Entrada e Saída

## PIS e COFINS em entradas e saídas - Produtos e serviços

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do PIS e COFINS.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do PIS e COFINS.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Empresa”**
   Menu: Comercial » Preferências » Empresa

- Na aba **“Propriedades”**, configure os campos:

  - **“Calcula PIS”**: marcado;
  - **“Calcula COFINS”**: marcado;
  - **“Tem Créd.PIS”**: marque de acordo com a necessidade da sua operação;
  - **“Tem Créd.COFINS”**: marque de acordo com a necessidade da sua operação;
  - **“Considera Repasse ICMS na BC PIS/COFINS”**: marque de acordo com a necessidade da sua operação;
  - **“CSTs que não Reduzem o ICMS da BC do PIS e COFINS”**: informe os CST que estejam nessa condição, separados por vírgula;
  - **“Deduzir valor de FCP e FCP ST na BC do PIS e COFINS”**: marque de acordo com a necessidade da sua operação;
  - **“Deduzir valor de ST da compra da BC do PIS e COFINS da Venda”**: marque de acordo com a necessidade da sua operação;
  - **“Calcula PIS e Cofins na confirmação do financeiro”**: marque de acordo com a necessidade da sua operação.

2. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastros

- Na aba **“Geral”**, habilite a marcação **“Calcula PIS/COFINS por percentual das notas”**.
- Na aba **“Impostos”**, configure os campos: 

  - **“Tem PIS”**: marcado;
  - **“Tem COFINS”**: marcado;
  - **“Natureza da Base de Cálculo do Crédito de Pis/Cofins”**: defina o código apropriado à sua operação;
  - **“Deduzir valor do ICMS na BC do PIS e COFINS?”**: marque de acordo com a necessidade da sua operação;
  - **“Deduzir valor do PIS/COFINS da BC do PIS e COFINS?”:** marque de acordo com a necessidade da sua operação;
  - **“Deduzir valor do ICMS/ST na BC do PIS e COFINS?”:** marque de acordo com a necessidade da sua operação;
  - **“Deduzir valor de FCP na BC do PIS e COFINS?”:** marque de acordo com a necessidade da sua operação;
  - **“Calcula PIS/COFINS red. pela aquisição”**: seleciona a opção **Usa do parâmetro;**
  - **“Desconsiderar CST’s de ICMS da BC do PIS/COFINS?”**: informe os CST que estejam nessa condição, separados por vírgula;
- Na aba **“Desp. Acessórias”**, marque todos os campos das seções **PIS** e **COFINS**.

3. Acesse as telas **“Alíquotas de PIS”** e **“Alíquotas de COFINS”**
   Menu: Comercial » Arquivo » Cadastros » Alíquotas

- Crie as regras para as operações de entrada e saída em **“+ Novo registro”**
- Valide os campos com **“\*”**, uma vez que são obrigatórios.

4. Acesse a tela **“Parceiros”**
   Menu: Configurações » Cadastros

- Na aba **“Fiscal”**, verifique:

  - Marque o campo **“Possui Suframa para PIS/COFINS”**;
  - O campo **“Deduzir valor de IPI da BC do PIS e COFINS”** caso esteja desabilitado, o IPI será somado ao valor da Base de Cálculo. No entanto, se estiver habilitado, o IPI será excluído da Base de Cálculo.

5. Acesse a tela **“Produtos”**
   Menu: Configurações » Cadastros » Produtos

- Na aba **“Impostos”**, seção **PIS/COFINS/CSLL**, configure:

  - **Grupo PIS**: defina o grupo de cálculo que irá incidir no produto;
  - **Grupo COFINS**: defina o grupo de cálculo que irá incidir no produto.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Compras, para movimentações de entrada, ou o Portal de Vendas, para movimentações de saída, e emita uma Nota utilizando o produto e parceiro configurados acima.

1. Acesse a tela **“Portal de Compras”**

**Menu:** Comercial » Consulta » Portal de Compras

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **“Nota de Compra”**;
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação.**

**Itens**

- Utilize na negociação o produto configurado;
- Salve as informações.
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Selecione a opção **“Consultar/Alterar Dados do Imposto do Item…”**;
- No modo grade, localize as linhas de PIS e COFINS para realizar a conferência.

**Atenção!** A validação de PIS e COFINS é realizada no momento da confirmação da Nota.

- Acione o botão “**...**” (**Outras opções…**);
- Clique em **“Resumo de Impostos”** e realize a conferência no pop-up que aparecerá.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
