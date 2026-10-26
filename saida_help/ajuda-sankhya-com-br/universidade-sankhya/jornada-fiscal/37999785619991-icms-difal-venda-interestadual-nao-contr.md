---
id: "37999785619991"
titulo: "ICMS DIFAL (Venda Interestadual - Não contribuinte)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37999785619991-ICMS-DIFAL-Venda-Interestadual-N%C3%A3o-contribuinte"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-07-22T14:02:58Z"
rotulos: ["Configuração", "Fiscal", "DIFAL", "ICMS", "TOP"]
---

# ICMS DIFAL (Venda Interestadual - Não contribuinte)

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do ICMS e seus desdobramentos.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do ICMS.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela “**Tipo de Operação - TOP”**

Menu: Comercial » Arquivo » Cadastros

- Na aba “**Impostos”**, habilite o campo “**Calcular DIFAL Partilhado”**;
- Atenção para o campo “**Classificação ICMS”**. Se este estiver configurado como **“Usar do Parceiro”**, deve-se validar a configuração do parceiro.

2. Acesse a tela “**Produtos”**
   Menu: Configurações » Cadastros » Produtos

- Na aba de **“Impostos”**, marque o campo **“Calcular DIFAL”.**

3. Acesse a tela “**Parceiros”**
   Menu: Configurações » Cadastros » Parceiros

- Na aba **“Fiscal”,** preencha o campo **“Classificação ICMS”** com a opção **“Consumidor Final Não Contribuinte”**.
- Para que o contato do parceiro seja considerado como local de entrega, na aba **“Contatos”**, preencha o campo “**CPF/CNPJ”** e o campo “**Cód Cidade”**.

4. Acesse a tela “**Partilhas DIFAL”** 
   Menu: Configurações » Cadastros » Partilhas DIFAL

- Cadastre as partilhas referentes ao diferencial de alíquota clicando em “**+ Novo registro”**.
- Preencha os campos “**Data Início Partilha”** e “**Percentual de Partilha DIFAL”**.

5. Acesse a tela **“Alíquota de ICMS”** 
   Menu: Comercial » Arquivos » Cadastros » Alíquotas

- Na seção **“DIFAL/FCP (Não Contribuinte)”**, configure o campo **“Alíq Interna Destino”**.
- Atenção ao campo **“Tipo de Cálculo DIFAL”**: Em algumas situações específicas, é necessário  indicar o tipo de cálculo que deve ser aplicado para o cálculo do imposto.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Vendas e emita uma Nota de Venda utilizando o produto e parceiro configurados acima. 

1. Acesse a tela **“Portal de Vendas”**

**Menu:** Comercial » Consulta » Portal de Vendas

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **Nota de Venda.**
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).
- Selecione com um duplo clique o tipo de operação **VENDA NF-E**.

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação.**

**Itens**

- Utilize na negociação o produto configurado;
- Salve as informações;
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Selecione a opção **“Consultar/Alterar Dados do Imposto do Item…”**;
- Verifique os campos:

  - **“Percentual de Partilha DIFAL”;**
  - **“Valor DIFAL UF Destino”;**
  - **“Base DIFAL”.**

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
