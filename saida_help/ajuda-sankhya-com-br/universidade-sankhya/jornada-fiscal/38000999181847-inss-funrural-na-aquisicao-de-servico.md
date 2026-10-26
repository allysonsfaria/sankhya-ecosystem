---
id: "38000999181847"
titulo: "INSS/Funrural na Aquisição de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000999181847-INSS-Funrural-na-Aquisi%C3%A7%C3%A3o-de-Servi%C3%A7o"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-08-18T13:43:26Z"
rotulos: ["Configuração", "Serviço", "Fiscal", "Impostos", "INSS", "Funrural"]
---

# INSS/Funrural na Aquisição de Serviço

## INSS, FUNRURAL, GILRAT E SENAR

#### O que é o INSS?

O **INSS Retido** sobre nota fiscal refere-se à retenção e ao recolhimento da contribuição sobre valores pagos por serviços que envolvam cessão de mão de obra ou empreitada. A alíquota padrão de retenção é de 11% sobre o valor bruto do serviço (podendo excluir o ISS). A empresa contratante é a responsável legal por realizar essa retenção e efetuar o recolhimento à Receita Federal. Empresas optantes pelo Simples Nacional geralmente estão isentas desta retenção. Outras contribuições previdenciárias relacionadas incluem o Funrural, GILRAT e Senar.

#### Quais os riscos de não realizar a automatização do cálculo do INSS?

- **Descumprimento legal:** Aumenta a probabilidade de descumprimento de regras previdenciárias, expondo a empresa a sanções legais;
- **Penalidades financeiras:** Atrasos no recolhimento das contribuições geram penalidades financeiras e prejudicam o relacionamento com os órgãos reguladores;
- **Risco de autuações:** Inconsistências em declarações obrigatórias como o eSocial e a DCTFWeb elevam significativamente o risco de autuações fiscais.

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do INSS retido.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do INSS retido.

#### Chegou a hora de configurar no ERP Sankhya

**Pela Central de Notas:**

1. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastros

- Na aba **“Impostos”**, marque a opção **“Tem FUNRURAL/INSS”.**

2. Acesse a tela **“Empresa”**
   Menu: Comercial » Preferências

- Na aba **“Propriedades”**, marque a opção “**Calcula FUNRURAL/INSS”**.

3. Acesse a tela **“Parceiros”**
   Menu: Configurações » Cadastros

- Na aba **“Fiscal”**, marque a opção **“Calcular FUNRURAL/INSS”.**

4. Acesse a tela **Serviço**
   Menu: Configurações » Cadastros » Produtos

- Na aba **“Impostos”**, seção **ICMS/ST/FUNRURAL/INSS**, configure os campos:

  - **“Tem INSS”**: marcado**;**
  - **“% INSS”:** defina o percentual de retenção.

**Por Outros Impostos:**

1. Acesse a tela **”Impostos”**
   Menu: Configurações » Cadastros

- Com o imposto INSS já cadastrado, preencha os campos do cabeçalho:

  - **“Tipo”:** selecione a opção “**todos, EXCETO os com a coluna "calcular" DESMARCADA”**;
  - **“Usar para itens da nota”:** selecione a opção **“Preço da Nota”**;
  - **“Base para Impostos no Financeiro”:** opte pela opção **“Valor do Pagamento”**.
- Na aba **“Serviço”**, configure os campos:
- **“Na nota”**: selecione **“Subtrair”**;
- **“No Financeiro de Origem Estoque”**: selecione **“Nenhum”**.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Compras e gere um pedido de compra com a TOP de compra de serviço.

**Pela Central de Notas:**

1. Acesse a tela **“Portal de Compras”**

**Menu:** Comercial » Consulta » Portal de Compras

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **“Nota de Compra”**;
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação:** COMPRA - SERVIÇOS, por exemplo.

**Itens**

- Utilize na negociação o serviço configurado;
- Salve as informações;
- Acione o botão “**...**” (**Outras opções…**);
- Clique na opção **“Resumo de Impostos”** e verifique o INSS.

**Por Outros Impostos:**

1. Acesse a tela **“Portal de Compras”**

**Menu:** Comercial » Consulta » Portal de Compras

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **“Nota de Compra”**;
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação:** COMPRA - SERVIÇOS, por exemplo.

**Itens**

- Utilize na negociação o serviço configurado;
- Salve as informações;
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Clique em **“Outros Impostos”** e valide o campo de INSS.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
