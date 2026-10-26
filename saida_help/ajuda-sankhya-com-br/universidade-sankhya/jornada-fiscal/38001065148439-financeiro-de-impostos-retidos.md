---
id: "38001065148439"
titulo: "Financeiro de impostos retidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38001065148439-Financeiro-de-impostos-retidos"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-08-25T21:34:47Z"
rotulos: ["Configuração", "NF-e", "Movimentação Financeira", "Impostos", "Financeiro"]
---

# Financeiro de impostos retidos

## Gerar Financeiro de Impostos retidos nas notas de serviço

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor financeiro da empresa Axis Ltda e deve realizar as configurações adequadas para gerar o financeiro dos impostos calculados.

**Tarefa:** Configure todos os cadastros envolvidos para a devida geração do financeiro dos impostos calculados.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP

1. Acesse a tela **“Tipos de Título”**
   Menu: Financeiro » Arquivos » Cadastros » Tipos de Título

- Insira um novo cadastro clicando em “**+ Novo registro”** e crie um para recolhimento federal e outro para recolhimento estadual;
- Preencha os campos:

  - **Tipo de Título:** 1;
  - **Descrição:** DARF;
  - **Tipo de Título:** 2;
  - **Descrição:** DAM.

2. Acesse a tela **“Tipos de Negociação”**
   Menu: Comercial » Arquivo » Cadastros » Tipos de Negociação » Aba parcelas

- Insira um novo cadastro clicando em **“+ Novo registro”** e preencha os campos: 

  - **Fórmula CSRF:**

 IF (PDES('TIPMOV','TGFCAB','NUNOTA='+NUNOTA)!='V',

VAL(PDES('NVL(SUM(IMN.VALOR),0)',

  'TGFIMN IMN, TGFITE ITE', 

  'IMN.NUNOTA=ITE.NUNOTA 

 AND IMN.SEQUENCIA=ITE.SEQUENCIA 

AND IMN.CODIMP IN (2, 3, 4)

 AND ITE.NUNOTA='+NUNOTA)),

 0

)

- **Fórmula INSS:**

IF (

PDES('TIPMOV','TGFCAB','NUNOTA='+NUNOTA)!='V',

VAL(PDES('NVL(SUM(IMN.VALOR),0)',

        'TGFIMN IMN, TGFITE ITE', 

        'IMN.NUNOTA=ITE.NUNOTA AND 

        IMN.SEQUENCIA=ITE.SEQUENCIA 

        AND IMN.CODIMP = 6 AND ITE.NUNOTA='+NUNOTA)),

    0

    )

- **Fórmula IRRF:**

IF (

PDES('TIPMOV','TGFCAB','NUNOTA='+NUNOTA)!='V',

VAL(PDES('NVL(SUM(IMN.VALOR),0)',

        'TGFIMN IMN, TGFITE ITE', 

        'IMN.NUNOTA=ITE.NUNOTA AND 

        IMN.SEQUENCIA=ITE.SEQUENCIA 

        AND IMN.CODIMP = 7 AND ITE.NUNOTA='+NUNOTA)),

    0

    )

- **Fórmula ISS:**

Val(Pdes('SUM(DIN.VALOR)','TGFDIN DIN','DIN.CODIMP=4 AND DIN.NUNOTA='+queTGFCAB.NUNOTA))

**Atenção!** As fórmulas dependem se os impostos foram configurados pela central de notas ou por outros impostos, devido alimentar tabelas diferentes, Central alimenta a **TGFDIN** e Outros Impostos a **TGFIMN.**

#### É a sua vez! Siga as orientações para validar as configurações realizadas

1. Acesse a tela **“Portal de Compras”**

**Menu:** Comercial » Consulta » Portal de Compras

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **“Nota de Compra”**;
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Tipo Negociação;**
  - **Empresa;**
  - **Tipo Operação:** COMPRA - SERVIÇOS, por exemplo.

**Itens**

- Utilize na negociação o serviço configurado;
- Salve as informações;
- Acione o botão “**...**” (**Outras opções…**);
- Clique na opção **“Resumo de Impostos”** e verifique o ISS e os campos **“Alíquotas”** e **“Valor”;**
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Clique em **“Outros Impostos”** e valide os campos de PIS, COFINS, CSLL, INSS e IRF;
- valide as informações no Rodapé da Nota, na aba **“Financeiro”** se foram geradas as parcelas referentes aos impostos.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
