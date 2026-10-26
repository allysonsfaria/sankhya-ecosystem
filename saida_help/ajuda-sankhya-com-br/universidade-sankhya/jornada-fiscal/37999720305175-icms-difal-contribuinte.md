---
id: "37999720305175"
titulo: "ICMS DIFAL Contribuinte"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37999720305175-ICMS-DIFAL-Contribuinte"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-07-22T14:02:59Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "DIFAL", "ICMS", "Impostos", "TOP"]
---

# ICMS DIFAL Contribuinte

#### Cenário prático

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do ICMS e seus desdobramentos.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do ICMS.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Produtos”**

Menu: Comercial » Configuração » Cadastros » Produtos

- Localize o(s) produto(s) de **uso e consumo**;
- Na aba **“Impostos”**, habilite os campos **“Calcular ICMS?”** e **“Calcular DIFAL?”**.

2. Acesse a tela “**Tipo de Operação - TOP”**

Menu: Comercial » Arquivo » Cadastros

- Localize os TOP's de compra tanto para **uso e consumo** quanto para **ativo imobilizado**;
- Na aba **“Impostos”**, habilite o campo **“Calcular diferença de ICMS”**.

3. Acesse a tela “**CFOP”**
   Menu: Comercial » Arquivos » Cadastros

- Localize o CFOP usado nesta operação;
- Marque a opção “**Calcular Diferença de ICMS”**.

4. Acesse a tela “**Alíquota de ICMS”** 
   Menu: Comercial » Arquivos » Cadastros » Alíquotas

- Certifique-se de que exista uma regra interna (origem e destinos iguais) cadastrada;
- Na aba **“Geral”**, verifique se o campo **“Alíquotas”** está preenchido.

5. Acesse a tela “**Empresa”**

Menu: Comercial » Preferências » Empresa

- Na aba **“Geração ICMS/IPI”**, defina o tipo de cálculo, por meio do campo **“Método para Calcular Diferencial de Alíquotas”**.

**É a sua vez! Siga as orientações para validar as configurações realizadas**

**Tarefa:** Acesse o Portal de Compras e emita uma Nota de Compra utilizando o produto e parceiro configurados acima.

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
- Salve as informações;
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Selecione a opção **“Consultar/Alterar Dados do Imposto do Item…”**;
- Verifique os campos:

  - **“Valor de Diferencial”;**
  - **“Alíquota de Diferencial”.**

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
