---
id: "37987536364439"
titulo: "ICMS Substituição Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37987536364439-ICMS-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-08-07T20:58:48Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "ICMS", "Impostos", "Substituição Tributária"]
---

# ICMS Substituição Tributária

## Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do ICMS e seus desdobramentos.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do ICMS.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela “**Produtos”**

**Menu:** Configurações » Cadastros » Produtos » Produtos

- **Aba “Impostos”:**
- Configure os campos:

  - **Classificação Substituição Tributária;**
  - **Tipo de substituição;**
  - **CEST - Código Especificador ST.**
- **Atenção!** Caso a preferência **EMPPRODIMPOST** esteja ligada, acesse a aba **“Impostos / Informações por empresa”:**
- Preencha os campos abaixo:

  - Tipo de substituição;
  - Código Especificador ST.

2. Acesse a tela “**Tipo de Operação - TOP”**

Menu: Comercial » Arquivo » Cadastros 

- **VENDA NF-E:**
- Na aba “**Impostos”**, preencha/configure os campos conforme indicado abaixo:

  - **Soma ST no total da nota**: marcado;
  - **Usa Cus. Méd. Base ST**: marcado.
- Na aba “**Desp. Acessórias”**, marque todos os campos da seção correspondente ao ICMS ST. Marque também os campos abaixo:

  - **Usar base ICMS Frete Extra Nota p/calc. ST;**
  - **Calc. ICMS/ST extra nota p/ frete extra nota proporcional aos itens;**
  - **Frete/Seguro/Outras Despesas para ST extra nota.**

3. Acesse a tela “**Alíquota de ICMS**”
   Menu: Comercial » Arquivos » Cadastros » Alíquotas

- Para uma exceção, duplique um registro já existente;
- No campo **“Tipo 1”**, opte por **“por grupo de ICMS do produto”**;
- Será habilitado o campo **“Grupo de ICMS do produto”** para preenchimento;
- Aba **“Geral”:**

  - **“Tributação”:** 10-Tributada e c/ cobrança por substituição;
- Aba **“Substituição Tributária”:**

  - “**Margem Lucro (MVA)”:** 20;
  - **“Modalidade BC ICMS ST”:** Margem Valor Agregado (%);
- Clique em **“Salvar [F7]”**;
- No pop-up **“Prioridade das Restrições”**, defina a ordem das restrições e clique em **“Concluir”**.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Vendas e emita uma Nota de Venda utilizando o produto e parceiro configurados acima. 

1. **Acesse a tela “Portal de Vendas”**

**Menu:** Comercial » Consulta » Portal de Vendas

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **Nota de Venda.**
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).
- Selecione com um duplo clique o tipo de operação **VENDA NF-E**.

**Cabeçalho**

- Preencha o cabeçalho com as informações solicitadas e utilize o parceiro configurado;
- Salve o registro.

**Itens**

- Utilize na negociação o produto configurado;
- Salve as informações.
- No painel de itens, no menu acione o botão “**...**” (**Outras opções…**)
- Selecione a opção **“Consultar/Alterar Dados do Imposto do Item…”**;
- Verifique os campos:

  - **Base de Cálculo;**
  - **Alíquota;**
  - **Valor.**
- Após as validações siga com a confirmação da nota.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
