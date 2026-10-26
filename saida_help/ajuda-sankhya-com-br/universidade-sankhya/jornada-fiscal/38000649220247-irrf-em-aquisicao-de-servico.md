---
id: "38000649220247"
titulo: "IRRF em Aquisição de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000649220247-IRRF-em-Aquisi%C3%A7%C3%A3o-de-Servi%C3%A7o"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-10-14T22:32:47Z"
rotulos: ["Configuração", "Serviço", "Fiscal", "Impostos", "TOP", "IRRF"]
---

# IRRF em Aquisição de Serviço

## Retenção de IRRF na Aquisição de Serviços

#### O que é o IRRF?

O IRRF retido em nota de serviço ocorre quando a fonte pagadora retém uma parcela do imposto de renda no momento do pagamento, destacando essa retenção na nota fiscal ou no documento de pagamento. Essa retenção é obrigatória em serviços específicos previstos na legislação. Para pessoas jurídicas, a alíquota é geralmente de 1,5% sobre o valor bruto do serviço, enquanto para pessoas físicas segue a tabela progressiva do IRRF, com alíquotas variando entre 7,5% e 27,5%, aplicadas sobre o valor bruto após deduções permitidas. Empresas optantes pelo Simples Nacional estão isentas dessa retenção.

#### Quais problemas empresariais são resolvidos pela configuração do IRRF em um ERP?

- **Risco e conformidade fiscal:** Ocorrem erros manuais nos cálculos e retenções, dificultando o acompanhamento da legislação. Isso eleva o risco de autuações e multas por inconsistências ou omissões;
- **Controle e Rastreabilidade:** Há desorganização e falta de rastreabilidade nos registros de retenção, comprometendo o controle financeiro e contábil para fins de auditoria;
- **Ineficiência Operacional:** O excesso de processos manuais causa retrabalho e perda de tempo, impactando diretamente a produtividade da equipe fiscal.

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo dos impostos PIS/COFINS/CSLL retidos.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo dos impostos PIS/COFINS/CSLL retidos.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Pela Central de Notas:**

1. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastros

- Localize a TOP de compra de serviço;
- Na aba **“Impostos”**, marque a opção “**Tem IRF”.**

2. Acesse a tela **“Empresa”**
   Menu: Comercial » Preferências

- Na aba **“Propriedades”**, marque a opção **“Calcula IRRF”**.

3. Acesse a tela **“Parceiros”**
   Menu: Configurações » Cadastros

- Na aba **“Fiscal”**, marque a opção **“Calcula IRF”.**

4. Acesse a tela **“Serviço”**
   Menu: Configurações » Cadastros » Produtos

- Na aba **“Impostos”**, ative a opção “**Tem IRF”** e informe o **“%IRF”**

**Por Outros Impostos:**

1. Acesse a tela **“Impostos”**
   Menu: Configurações » Cadastros

- Com o imposto IRF já cadastrado, preencha os campos do cabeçalho:

  - **“Valor Mínimo do Imposto”:** informe o valor mínimo a partir do qual será registrado cálculo do imposto, por exemplo R$ 10,00;
  - **“Grupo Vlr. Mínimo do Imposto”:** IRF;
  - **“Tipo”:** selecione a opção “**todos, EXCETO os com a coluna "calcular" DESMARCADA”;**
  - **Tipo Imposto:** IRF;
  - **Usar para itens da nota:** Preço da Nota;
  - **Base para Impostos no Financeiro:** Valor do Pagamento.
- Na aba **“Serviço”**, configure os campos: 

  - **“Na Nota”**: selecione **“Subtrair”**;
  - **“No Financeiro de Origem Estoque”**: opte por **“Nenhum”**.

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
- Clique na opção **“Resumo de Impostos”** e verifique o IRF.

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
- Clique em **“Outros Impostos”** e valide o campo de IRF.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
