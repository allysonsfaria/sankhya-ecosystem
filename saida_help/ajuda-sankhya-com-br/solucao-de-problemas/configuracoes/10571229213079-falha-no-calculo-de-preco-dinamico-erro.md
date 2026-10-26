---
id: "10571229213079"
titulo: "Falha no cálculo de preço dinâmico: Erro ao executar a procedure"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10571229213079-Falha-no-c%C3%A1lculo-de-pre%C3%A7o-din%C3%A2mico-Erro-ao-executar-a-procedure"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:03:20Z"
rotulos: ["Produtos", "Configuração", "CORE_E02297", "Preferências", "Falha no Cálculo de Preço Dinâmico", "Erro"]
---

# Falha no cálculo de preço dinâmico: Erro ao executar a procedure

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19035953523095) MENSAGEM:**

[CORE\_E02297] Falha no cálculo de preço dinâmico: Erro ao executar a procedure.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19035953529239) SITUAÇÃO:**

Ao clicar em 'Consulta de Produtos' e pesquisar os produtos a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19035953534487) CAUSA:**

Ocorre quando a PROCEDURE não está correta.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19035937070615) SOLUÇÃO:**

Avalie a PROCEDURE, pois a mesma não está correta. A procedure para cálculo de preço dinâmico deve receber apenas um parâmetro de entrada e como resultado deve retornar um Json do tipo chave-valor. O campo "PRECO" é o preço dinâmico e esse dado é obrigatório no retorno, mesmo que seja zero. Por exemplo:

**{**

**"PRECO" : "50.0",**

**"PRECOBASE" : "50.0"**

**"AD\_TIPOPRECO" : "T"**

**}**

Ao criar a procedure, acesse a tela **'Preferências'** (Caminho de acesso à tela: Configurações » Avançado » Preferências), busque pelo parâmetro '**NOMPROCCALCPRE** **Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE'** e nele indique o nome da procedure criada para cálculo de preço dinâmico. Fazendo esse preenchimento significa que o sistema irá utilizar as rotinas de preço dinâmico.

**Observação:** Com os parâmetros de chave **'Nota modelo para cálculo de preço dinâmico - MODCALCPRECDIN'** e '**NOMPROCCALCPRE** **Procedure para cálculo de preço dinâmico - NOMPROCCALCPRE'** devidamente configurados, quando for lançada uma venda ou um pedido de venda informando o local do item, o valor unitário será calculado de acordo com a procedure cadastrada.
