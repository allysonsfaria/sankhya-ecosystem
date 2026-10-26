---
id: "38000299278615"
titulo: "IPI em Notas de Entrada e Saída"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000299278615-IPI-em-Notas-de-Entrada-e-Sa%C3%ADda"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-07-22T14:02:51Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "IPI", "Impostos", "TOP"]
---

# IPI em Notas de Entrada e Saída

## IPI nas entradas e saídas - Produtos e serviços

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do IPI.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do IPI.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Empresa”**
   Menu: Comercial » Preferências » Empresas

- Na aba **“Propriedades”**, configure os campos abaixo:

  - **Trabalha com IPI**: marcado;
  - **IPl incide no ICMS**: marcado;
  - **Código Sit Trib IPI Entrada**: preencha com o código adequado à sua operação;
  - **Código Sit Trib IPI Saída**: preencha com o código adequado à sua operação;
  - **Compensa o IPI**: marcado.

**Observação** : Nas notas de entrada, a empresa não precisa estar configurada para cálculo de IPI.

- Na aba **“Geração ICMS/IPI”**, marque a opção **“Compensa o IPI”**, caso a sua empresa seja indústria e deseja aproveitar o crédito IPI.

2. Acesse a tela **“Parceiros”**
   Menu: Configurações » Cadastros

- Na aba **“Fiscal”**, configure os campos abaixo:

  - **Código Sit Trib IPI Entrada**: preencha com o código adequado à sua operação;
  - **Código Sit Trib IPI Saída**: preencha com o código adequado à sua operação;
  - **Código Enq. Legal IPI Entrada:** preencha com o código adequado à operação;
  - **Código Enq. Legal IPI Saída:** preencha com o código adequado à operação;
  - **IPl incide no ICMS**: marcado;
  - **Tem IPI**: marcado.

3. Acesse a tela **“Tipos de Operação - TOP”**
   Menu: Comercial » Arquivo » Cadastros

- Na aba **“Impostos”**, configure:

  - **Cálculo de ICMS, IPI e ISS**: **“Calcula e Digita”**, para notas de venda, enquanto **“Não calcula e Digita”**, para notas de compra;
  - **Devolver sem destacar IPI**: marcado;
  - Na seção **IPI**, preencha todos os campos de acordo com a operação realizada.

4. Acesse a tela **“Alíquotas de IPI”**
   Menu: Comercial » Arquivo » Cadastros » Alíquotas

- Caso precise incluir as alíquotas, clique em **“+ Novo registro”**;
- Defina os campos **“Código do IPI”** e **“Descrição”**, para identificação;
- Preencha os campos **“Percentual”**, **“Cód.Sit.Trib.IPI Entrada”** e **“Cód.Sit.Trib.IPI Saída”** com as informações pertinentes à sua operação.

**Atenção!** O campo **“Código Situação Tributária do IPI – Entrada e Saída”** está disponível em diferentes cadastros relacionados ao IPI, como Tipo de Operação (TOP), Produto, Empresa e Parceiro. Quando todos os cadastros estiverem configurados para o cálculo do IPI, o sistema adotará o CST definido na Alíquota de IPI aplicada na operação. No entanto, se algum desses cadastros estiver com o cálculo de IPI desmarcado, o sistema buscará a CST diretamente nesse cadastro, respeitando a seguinte ordem de prioridade: TOP → Produto → Empresa → Parceiro. Essa regra também se aplica para o cálculo do **Cód. Enquadramento Legal do IPI**. Caso precise das regras para buscar o CST de IPI e realizar o cálculo de impostos, acesse o [Ajuda Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042753354-Regras-para-Buscar-a-CST-de-IPI-e-o-c%C3%A1lculo-do-imposto-no-Sistema-SankhyaW).

5. Acesse a tela **“Produtos”**
   Menu: Configurações » Cadastros » Produtos

- Na aba **“Impostos”**, seção **“IPI”**, configure:

  - **IPI**: vincule a alíquota de IPI que irá incidir no produto;
  - **Tem IPI na venda**: marcado;
  - **Tem IPI na compra**: marcado;
  - **Código Sit Trib IPI Entrada**: preencha com o código adequado à operação;
  - **Código Sit Trib IPI Saída**: preencha com o código adequado à operação;
  - **Código Enq. Legal IPI Entrada:** preencha com o código adequado à operação;
  - **Código Enq. Legal IPI Saída:** preencha com o código adequado à operação.

**Atenção!** A aba **“Impostos / Informações por empresa”**, caso tenha sido preenchida,  terá prioridade sobre as configurações das outras abas.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Vendas e emita uma Nota de Venda utilizando o produto e parceiro configurados acima.

1. Acesse a tela **“Portal de Vendas”**

**Menu:** Comercial » Consulta » Portal de Vendas

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **“Nota de Venda”**;
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**);
- Selecione com um duplo clique o tipo de operação **VENDA NF-E**.

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação.**

**Itens**

- Utilize na negociação o produto configurado;
- Salve as informações;
- No rodapé da página, em **“Impostos”,** valide o campo **“Vlr. do IPI”**;
- No painel de itens, acione o botão “**...**” (**Outras opções…**);
- Selecione a opção **“Consultar/Alterar Dados do Imposto do Item…”**;
- No modo grade, localize a linha referente ao IPI e valide os seguintes campos:

  - **“Base de Cálculo”;**
  - **“Alíquota”;**
  - **“Valor”.**

#### Correção e repetição

- **Revise os parâmetros inseridos:** Verifique CFOP, CST, natureza de operação, tipo de negociação e grupo tributário e confirme se os campos obrigatórios foram preenchidos corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
