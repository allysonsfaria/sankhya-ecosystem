---
id: "37999968114583"
titulo: "Financeiro de impostos sobre NF-e (GNRE)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37999968114583-Financeiro-de-impostos-sobre-NF-e-GNRE"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-08-18T13:33:48Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "GNRE", "Financeiro"]
---

# Financeiro de impostos sobre NF-e (GNRE)

## Como gerar financeiro de impostos sobre NF-e

#### O que é?

A Guia Nacional de Recolhimento de Tributos Estaduais (GNRE) é usada para pagar o ICMS devido a outro estado, quando há substituição tributária (ICMS-ST), diferencial de alíquota (DIFAL), fundo de combate à pobreza (FCP) ou antecipação tributária. Em certas operações de entrada de notas, o recolhimento do ICMS, tem como fato gerador a própria operação, independentemente da apuração mensal. Ao emitir um documento sujeito à regra de recolhimento do ICMS, é necessário gerar e pagar a guia de forma individual para cada operação. Esse procedimento pode ser executado pelo sistema, evitando a necessidade de acessar o portal de cada estado para gerar a guia de recolhimento.

#### Quais os riscos de não realizar a automatização para a geração do financeiro dos impostos?

- **Evita omissões no recolhimento do ICMS de entradas:** Garante que todas as notas sujeitas a ICMS-ST, DIFAL, FCP ou antecipação tenham seus tributos devidamente registrados e pagos;
- **Reduz o risco de autuações fiscais:** Ao assegurar que a guia seja gerada corretamente e no prazo, evita penalidades por descumprimento da legislação estadual;
- **Elimina a necessidade de acessar múltiplos portais estaduais:** Automatiza o processo de geração das GNREs, reduzindo o retrabalho manual e a chance de erro humano ao operar em diferentes sistemas estaduais;
- **Assegura o cumprimento da regra de recolhimento por operação:** Garante que o ICMS seja tratado conforme exigido (por operação e não por apuração mensal), evitando erros de interpretação;
- **Facilita a conciliação financeira e contábil:** O lançamento do financeiro da guia diretamente no ERP proporciona rastreabilidade e controle sobre os pagamentos realizados;
- **Agiliza o processo de regularização fiscal de entradas:** Com a geração automatizada do financeiro e da guia, o tempo entre a entrada da nota e o recolhimento do tributo é reduzido;
- **Evita esquecimentos no pagamento de tributos antecipados:** Com a sistematização do processo, o risco de não recolher o ICMS antecipado em operações interestaduais é praticamente eliminado.

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor financeiro da empresa Axis Ltda e deve realizar as configurações adequadas para gerar o financeiro dos impostos calculados.

**Tarefa:** Configurar todos os cadastros envolvidos para a devida geração do financeiro dos impostos calculados.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Tipos de Título”**
   Menu: Financeiro » Arquivos » Cadastros » Tipos de Título

- Com o modo grade ativado, localize o **tipo de título 1** e verifique se está ativo;
  **Atenção!** Caso não tenha na sua base, realize o cadastro de acordo com as orientações abaixo:
- Clique em **“+ Novo registro”**;
- Preencha os campos:

  - **Tipo de Título:** 1;
  - **Descrição:** Nota Fiscal;
  - **Espécie:** NF;
  - **Código da Receita (GNRE):** preencha com o código estipulado pelo estado;
  - **Código Detalhamento Receita (GNRE):** preencha com o código estipulado pelo estado;
  - **Código do Produto (GNRE):** preencha com o código estipulado pelo estado;
  - **Salve** o registro.

2. Acesse a tela **“Tipos de Negociação”**
   Menu: Comercial » Arquivo » Cadastros » Tipos de Negociação
   Aba **“Parcelas”**;

- Clique em **“+”** e preencha os campos: 

  - **Prazo;**
  - **Percentual;**
  - **Banco;**
  - **Natureza Padrão:** ICMS;
  - **Tipo de Título:** 1- Nota Fiscal;
  - **Tipo de Parceiro:** N - Nota;
  - **Fórmula:** 0;
  - **Tipo de Financeiro (REC/DESP):** N - Usar da Natureza Padrão.

3. Acesse a tela **“Natureza de Receitas e Despesas”**
   Menu: Configurações » Cadastro » Gerencial
   **Atenção!** Caso não tenha uma natureza de ICMS, realize o cadastro de acordo com as orientações abaixo:

- Clique em **“ + Novo registro”** e preencha os campos:

  - **Cód. Natureza:** defina um código;
  - **Descrição:** ICMS;
  - **Ativa:** Sim;
  - **Analítica:** Sim;
  - **Tipo de Natureza:** Despesa.

4. Acesse a tela **“Fórmula p/ Parcelas Independentes”**
   Menu: Financeiro » Arquivos » Cadastros » Tipos de Título

- Insira um novo cadastro clicando em **“+ Novo registro”** e preencha os campos:

  - **UF:** UF do parceiro que foi realizado a venda;
  - **Tipo de Título:** 1 - Nota Fiscal;
    Aba **“Geral”:**
  - **Parceiro:** Secretária da Fazendo do estado do parceiro;
  - **Receita ou Despesa:** Despesa;
  - **Fórmula**: informar a fórmula que irá buscar o valor do imposto, como por exemplo: **queTGFCAB.VLRICMSDIFALDEST**
  - **Financeiro para GNRE:** Ligado**.**
- **Salve** seu registro.

5. Acesse a tela **“Observação da Nota”**
   Menu: Comercial » Arquivo » Cadastros 
   **Atenção!** Caso não conste na sua base a opção “GNRE - DIFAL NÃO CONTRIBUINTE”, realize o cadastro de acordo com as orientações abaixo:

- Clique em **“+ Novo registro”** e preencha os campos:

  - **Código:** 1;
  - **Observação:** GNRE - DIFAL NÃO CONTRIBUINTE;
  - **Vincular DAE/GNRE:** marcado;
  - **Geração no EFD:** Observação do Lançamento Fiscal;
  - **Carrega Complemento p/ EFD:** marcado.
- **Salve** o registro.

6. Acesse a tela **“Estados”**
   Menu: Configurações » Cadastros

- No cadastro do estado para qual o imposto é devido, verifique os campos: 

  - **Cód. Parceiro Secretária da Receita Estadual:** SEFAZ do estado;
  - **Código da Receita (GNRE);**
  - **Código do Produto (GNRE);**
  - **Versão GNRE:** 2.0;
  - **Utiliza webservice para GNRE:** marcado caso utilize webservice para transmissão do lote GNRE.

7. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastros

- Localize a TOP a ser utilizada, como VENDA NF-E, por exemplo;
  Aba **“Financeiro”**:
- Marque o campo **“Gerar GNRE?”**.

8. Acesse a tela **“Empresa”**
   Menu: Comercial » Preferências

- Localize o registro da sua empresa;
  Aba **“Livros Fiscais”:**

  - **Gerar GNRE?**: ligado;

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Vendas e localize a venda que foi feita para o consumidor final não contribuinte, caso seja necessário gere uma nova nota com o tipo de negociação, parceiro, TOP e observação para notas conforme visto nas configurações

1. Acesse a tela **“Portal de Vendas”**

**Menu:** Comercial » Consulta » Portal de Vendas

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **Nota de Venda.**
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).
- Selecione com um duplo clique o tipo de operação **VENDA NF-E**.

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação;**
  - **Observação padrão.**

**Itens**

- Utilize na negociação o produto configurado;
- Salve as informações;
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Selecione a opção **“Consultar/Alterar Dados do Imposto do Item…”**;
- Verifique os campos:

  - **“Valor DIFAL UF Destino”.**

Aba **“Financeiro”:**

- Verifique a coluna **“Vlr do Desdobramento”**;
- Clique na opção **“Mov. Financeira”**, a qual te direcionará para outra tela;
- Analise os registros criados.

2. Acesse a tela **“Geração de lote GNRE”**
   Menu: Financeiro » Rotinas » Geração de lote GNRE

- Clique no botão **“Novo lote”** e faça a geração do arquivo XML;
- Utilize os filtros, como **“Empresa”**, **“Parceiro”** e **“Período”** e clique em **“Aplicar”**;
- Selecione o registro e clique em **“OK”**, para baixar o XML.
  **Obs.:** Os filtros personalizados, encontrados no menu lateral, podem ser usados para localizar algum lote gerado anteriormente. Assim como o botão “Baixar XML”, para realizar o download de algum arquivo.

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
