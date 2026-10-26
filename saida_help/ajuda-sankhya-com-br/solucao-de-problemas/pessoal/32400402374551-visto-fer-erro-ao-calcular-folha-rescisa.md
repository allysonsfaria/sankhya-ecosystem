---
id: "32400402374551"
titulo: "(Visto Fer) Erro ao Calcular Folha / Rescisão no Sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32400402374551--Visto-Fer-Erro-ao-Calcular-Folha-Rescis%C3%A3o-no-Sistema"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:19:48Z"
rotulos: ["Configuração", "Eventos", "Financeiro", "Folha de Pagamento", "Character", "is neither a decimal digit number", "Falha Não foi possível", "confirmar a folha de pagamento", "decimal point nor", "notation exponential mark", "Erro"]
---

# (Visto Fer) Erro ao Calcular Folha / Rescisão no Sistema

**MENSAGEM:**

**''Falha Não foi possível confirmar a folha de pagamento!''**

Motivo: ''**Character ; is neither a decimal digit number, decimal point, nor "e" notation exponential mark.''**

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32420651689623) **SITUAÇÃO:**

Esse problema pode ocorrer durante o cálculo ou a confirmação da folha, quando o sistema tenta interpretar a lista de eventos na tabela **TFPCON** como valores numéricos ou como parte de uma expressão matemática. Nesse contexto, o uso de ponto e vírgula é inválido, o que pode causar falhas no processamento.

**Exemplo de uma consulta com configuração incorreta:**

**SELECT CODCONVENIO, LISEVENTOS FROM TFPCON**

O conteúdo de **LISEVENTOS** para determinado convênio pode estar assim, por exemplo:

**101;102;103** (formato inválido).

**SOLUÇÃO:**

Para resolver o erro, siga os passos abaixo:

![Imagem 2: Identifique o registro com erro usando a consulta SQL acima;](https://ajuda.sankhya.com.br/hc/article_attachments/32420373618839) Identifique o registro com erro usando a consulta SQL acima;

![Imagem 3: Acesse a tela ''Plano de Saúde'' (Pessoal+» Cadastros» Plano de Saúde) e atualize o campo ''Evento'' , substituindo os…](https://ajuda.sankhya.com.br/hc/article_attachments/32420373620887) Acesse a tela**''Plano de Saúde''** (Pessoal+» Cadastros» Plano de Saúde) e atualize o campo **''Evento''**, substituindo os **pontos e vírgulas (;)** por apenas **vírgulas (,)**:

![Imagem 4: Refaça o cálculo da folha/rescisão e o sistema permitirá a confirmação do cálculo sem a presença da mensagem de erro.](https://ajuda.sankhya.com.br/hc/article_attachments/32420373623575) Refaça o cálculo da folha/rescisão e o sistema permitirá a confirmação do cálculo sem a presença da mensagem de erro.

**CAUSA:**

O erro está relacionado ao conteúdo da coluna **LISEVENTOS** na tabela **TFPCON**, que utiliza um delimitador **ponto e vírgula (;)** em vez da **vírgula (,)** para separar os eventos, sendo o formato esperado pela aplicação.
