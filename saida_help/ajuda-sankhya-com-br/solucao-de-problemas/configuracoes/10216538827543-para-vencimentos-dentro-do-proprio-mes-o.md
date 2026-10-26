---
id: "10216538827543"
titulo: "Para vencimentos dentro do próprio mês o dia de vencimento deve ser posterior ao dia final de venda"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10216538827543-Para-vencimentos-dentro-do-pr%C3%B3prio-m%C3%AAs-o-dia-de-vencimento-deve-ser-posterior-ao-dia-final-de-venda"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:12Z"
rotulos: ["Configuração", "Vencimento", "Financeiro", "Tipos de Negociação", "CORE_E05457", "Bases de Vencimento para Tipos de Negociação", "Erro"]
---

# Para vencimentos dentro do próprio mês o dia de vencimento deve ser posterior ao dia final de venda

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19551236707479) MENSAGEM:**

[CORE\_E05457] Para vencimentos dentro do próprio mês o dia de vencimento deve ser posterior ao dia final de venda.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19551214907287) SITUAÇÃO:**

Ao cadastrar um tipo de negociação a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19551236729751) CAUSA:**

Ocorre ao cadastrar um tipo de negociação com base de vencimento incorreta.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19551236732567) SOLUÇÃO:**

Na aba "Bases para vencimento", dentro da tela **Tipos de negociação** (Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de Negociação), estão as configurações para que o cálculo das Datas de vencimento dos títulos sejam feitos considerando períodos e datas previamente definidos. As parcelas no financeiro dos títulos serão geradas automaticamente em função dos períodos e datas configurados nessa tela.

![Imagem 5: Na aba " Bases para vencimento ", dentro da tela Tipos de negociação (Caminho de acesso à tela: Comercial » Arquivo »…](https://ajuda.sankhya.com.br/hc/article_attachments/19551236737559)

Entenda os campos presentes nessa aba:

**Sequência:** Corresponde ao encadeamento das datas de venda e vencimento a serem inseridas;

**Dia inicial da venda:** Dia inicial do período em que a venda acontece;

**Dia final da venda:** Dia final do período em que a venda acontece;

**Dia do vencimento:** Este será o dia gerado como base do vencimento;

**Mês de vencimento:** Corresponde ao mês da data a ser gerada como base do vencimento. Neste campo tem-se as seguintes opções:

- Mês atual;
- 1º mês subsequente;
- 2º mês subsequente;
- 3º mês subsequente;
- 4º mês subsequente;
- 5º mês subsequente;
- 6º mês subsequente.

Para utilização das Bases de Vencimento no Tipo de Negociação, tem-se algumas regras (os campos citados abaixo se encontram na aba Características), a saber:

**Subtipo:** Quando o Subtipo é **"A vista"** esta funcionalidade não tem efeito. Não é possível criar base de vencimento para Tipos de negociação A vista;

**Base de prazo:** Quando houver Base para vencimento vigente, será desconsiderado;

**Soma prazo de cliente:** Existindo Base para vencimento vigente, será desconsiderado;

**Fixa vencimento:** Quando houver Base para vencimento vigente, será desconsiderado. Além disso, o pop-up correspondente a Data Base não será apresentado;

**Prazo (PPG):** Quando existir Base para vencimento vigente, os prazos serão sempre mensais, deste modo, haverá uma conta para determinar o intervalo de meses;

**Base de prazo (PPG):** Havendo Base para vencimento vigente, será desconsiderado;

**Vencimento fixo (PPG):** Se existir Base para vencimento vigente, será desconsiderado;

**Soma prazo cliente (PPG):** Quando houver Base para vencimento vigente, será desconsiderado

**Observações:**

- Ao cadastrar um sequenciamento de bases de vencimento, o Dia final de venda de uma linha não pode ser igual ao Dia inicial de venda da linha seguinte. Caso seja feita a tentativa de confirmação de um cadastro nessas condições, será apresentada a seguinte mensagem de aviso:

**"A data inicial já está em um intervalo cadastrado."**

- Na tentativa de cadastro do Mês de vencimento definido como Mês atual e o Dia de vencimento anterior ao Dia final de venda, será exibida a seguinte mensagem de aviso:

**"Para vencimentos dentro do próprio mês o dia de vencimento deve ser posterior ao dia final de venda."**

Este cadastro será possível (Dia de vencimento anterior ao Dia final de venda) caso o Mês de vencimento seja definido como uma opção diferente de Mês atual.
