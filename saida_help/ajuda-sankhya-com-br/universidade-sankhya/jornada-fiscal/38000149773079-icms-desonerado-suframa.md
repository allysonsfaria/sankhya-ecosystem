---
id: "38000149773079"
titulo: "ICMS Desonerado Suframa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38000149773079-ICMS-Desonerado-Suframa"
trilha: "Universidade Sankhya > Jornada Fiscal "
atualizado_em: "2026-07-22T14:02:54Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "SUFRAMA", "ICMS", "TOP"]
---

# ICMS Desonerado Suframa

#### Cenário de aplicação

**Contexto:** Você é o responsável pelo setor fiscal da empresa Axis Ltda e deve realizar as configurações adequadas para o cálculo do ICMS e seus desdobramentos.

**Tarefa:** Configure todos os cadastros envolvidos para o devido cálculo do ICMS.

#### Chegou a hora de configurar no ERP Sankhya

1. Acesse a tela **“Parceiros”**
   Menu: Configurações » Cadastros » Parceiros

- Verifique, na aba **“Endereço”**, se os campos estão preenchidos corretamente;
- Na aba **“Fiscal”**, subaba **“SUFRAMA”**, preencha o campo “**Código SUFRAMA”.**

2. Acesse a tela **“Tipo de Operação - TOP”**

Menu: Comercial » Arquivo » Cadastros

- Na aba **“Livro Fiscal”**, configure a TOP de Venda com os CFOP’s adequados à operação com SUFRAMA, ou seja, **5109**, **6109** ou **6110**.

3. Acesse a tela **“Alíquotas de ICMS”**

Menu: Comercial » Arquivo » Cadastros »  Alíquotas

Crie exceções conforme sua necessidade.

- Na aba **“Geral”**, preencha os campos abaixo: 

  - **“Tributação”:** selecione a opção **"40-Isenta"**;
  - **“Alíquotas”**;
  - **“Cód.Mot.Desoneração ICMS”**: selecione a opção **“7-SUFRAMA”**.
- Na seção **“Repassar para o cliente”**, habilite o campo **“ICMS”** e preencha o campo **“Forma de repasse Desoneração”** com a opção que melhor se adequar à operação.
- Clique em **“Salvar [F7]”**;
- No pop-up “**Prioridade das Restrições**”, defina a ordem das restrições e clique em **“Concluir”**.

#### É a sua vez! Siga as orientações para validar as configurações realizadas

**Tarefa:** Acesse o Portal de Vendas e emita uma Nota de Venda utilizando o produto e parceiro configurados acima.

1. Acesse a tela **“Portal de Vendas”**

**Menu:** Comercial » Consulta » Portal de Vendas

- Acima do menu de filtros na lateral esquerda da tela, selecione, no “**Tipo** **de Movimento**”, a opção **Nota de Venda.**
- Abra as opções do novo documento, clicando na seta do botão “**+**” (**Novo documento**).
- Selecione com um duplo clique o tipo de operação **VENDA SUFRAMA**.

**Cabeçalho**

- Verifique o campos abaixo:

  - **Parceiro;**
  - **Empresa;**
  - **Tipo Operação.**

**Itens**

- Utilize na negociação o produto configurado;
- Salve as informações;
- Verifique o campo **“Tributação”**, o qual trará a regra indicada;
- O campo **“Cód. Mot. Desoneração ICMS”**, mostra o código da regra criada;
- **“CFOP”**, com o código que o sistema criou;
- No botão **“NF-e”**, clique na opção **“Gerar XML da NF-e em arquivo para conferência”** e confira se as tags foram geradas de maneira correta.

#### Correção e repetição

- Verifique se a TAG **vICMSDeson** foi gerada corretamente;
- **Compare com o cenário prático apresentado:** Analise se a configuração realizada condiz com o exemplo proposto na aula e refaça o cenário, se necessário, simulando novamente a operação no sistema;
- **Utilize documentação de apoio:** Consulte as tabelas de códigos fiscais e as orientações legais aplicáveis aos impostos trabalhados e use as referências da própria aula como guia;
- **Corrija e salve novamente:** Caso identifique inconsistências, edite os registros conforme os parâmetros corretos e salve as alterações;
- **Repita o procedimento até ganhar segurança:** A prática contínua é fundamental para fixar o aprendizado e refazer o exercício mais de uma vez ajuda a identificar padrões e evitar erros futuros;
- **Em caso de dúvidas:** Reveja a aula, consulte a documentação complementar ou entre em contato com o suporte da unidade. Aprofundar o entendimento evita erros em ambientes produtivos.
