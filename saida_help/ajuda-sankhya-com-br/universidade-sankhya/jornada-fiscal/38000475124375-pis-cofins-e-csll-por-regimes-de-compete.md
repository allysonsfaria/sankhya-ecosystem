---
id: "38000475124375"
titulo: "PIS, COFINS e CSLL por regimes de competência e de caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000475124375-PIS-COFINS-e-CSLL-por-regimes-de-compet%C3%AAncia-e-de-caixa"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-08-18T12:56:00Z"
rotulos: ["Configuração", "Fiscal", "COFINS", "PIS", "CSLL", "Impostos", "EFD Contribuições"]
---

# PIS, COFINS e CSLL por regimes de competência e de caixa

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo dos impostos PIS/COFINS/CSLL retidos.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo dos impostos PIS/COFINS/CSLL retidos.

![Imagem 1: Tarefa: Configure todos os cadastros envolvidos para o devido cálculo dos impostos PIS/COFINS/CSLL retidos.](https://ajuda.sankhya.com.br/hc/article_attachments/38000475121303)

#### Chegou a hora de configurar no ERP Sankhya

**PIS/COFINS/CSLL retidos por regime de competência**

1. Acesse a tela **“Impostos”**
   Menu: Configurações » Cadastros

- Selecione o imposto desejado e preencha os campos conforme abaixo:

  - **“Tipo”:** selecione a opção **“todos, EXCETO os com a coluna "calcular" DESMARCADA”**;
  - **“Usar para itens da nota”:** selecione **“Preço da Nota”**;
  - **“Base para Impostos no Financeiro”:** opte por **“Valor do pagamento”**;
  - **“Grupo Vlr. Mínimo do Imposto”:** adicione **“CSRF”**.
- Na aba **”Serviço”**, configure os campos:

  - **“Na nota”**: opte por **“Subtrair”**;
  - **“Alíquota”:** informe a alíquota correspondente ao imposto;
  - **“No Financeiro de Origem Estoque”**: selecione a opção **“Nenhum”**.

**Atenção!** Todas as configurações realizadas acima devem ser replicadas para PIS, COFINS e CSLL.

2. Acesse a tela “Serviços”
   Menu: Configurações » Cadastros » Produtos

- Selecione o serviço configurado na tela **“Impostos”**;
- Na aba **“Outros Impostos”**, verifique a configuração realizada no passo a passo anterior.

**PIS/COFINS/CSLL retidos por regime de caixa**

1. Configure a aba **“Serviço”**, considerando:

- **“Na nota”**: opte por **“Já incluso”**;
- **“Alíquota”:** informe a alíquota correspondente ao imposto.
- **“No Financeiro de Origem Estoque”**: selecione a opção **“Subtrair”**.

**É a sua vez! Siga as orientações para validar as configurações realizadas**

**Tarefa:** Acesse o Portal de Compras e gere um pedido de compra com a TOP de compra de serviço.

**PIS/COFINS/CSLL retidos por regime de competência**

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

- Utilize na negociação o serviço configurado por regime de competência;
- Salve as informações.
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Clique em **“Outros Impostos”** e valide os impostos retidos de acordo com cada alíquota.

**PIS/COFINS/CSLL retidos por regime de caixa**

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

- Utilize na negociação o serviço configurado por regime de caixa;
- Salve as informações.
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Clique em **“Outros Impostos”** e valide os impostos retidos de acordo com cada alíquota;
- No **Rodapé**, na aba **“Financeiro”**, clique na opção **“Mov. Financeira”**, a qual te direcionará para outra tela;
- Selecione o título e clique em **“Baixar”**, no canto superior direito, verifique a linha **“Impostos”** ou o campo **“Outros Impostos”**.

#### Correção e Repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
