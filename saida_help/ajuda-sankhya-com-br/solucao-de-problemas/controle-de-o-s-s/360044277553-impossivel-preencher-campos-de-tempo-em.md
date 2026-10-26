---
id: "360044277553"
titulo: "Impossível preencher campos de tempo em itens de fila: HRINICIAL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044277553-Imposs%C3%ADvel-preencher-campos-de-tempo-em-itens-de-fila-HRINICIAL"
trilha: "Solução de Problemas > Controle de O.S'S"
atualizado_em: "2026-07-22T15:59:12Z"
rotulos: ["#PUBLIFER", "#RevisadoBraga", "Configuração", "Funcionários", "Ordem de Serviço", "Controle de Acesso", "Correção de Erro ao Preencher Campos de Tempo em Itens de Fila", "Erro"]
---

# Impossível preencher campos de tempo em itens de fila: HRINICIAL

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16201268747543) MENSAGEM:**

Impossível preencher campos de tempo em itens de fila: HRINICIAL.

**![Imagem 2: S ITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201268751127) SITUAÇÃO:**

Ao tentar gerar o fechamento de ordem de serviço é apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16201297979159) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Identifique o usuário logado.](https://ajuda.sankhya.com.br/hc/article_attachments/16201297980567) Identifique o usuário logado.

![Imagem 5: Acesse a tela Configurações » Controle de Acesso » Relacionamento entre Usuários.](https://ajuda.sankhya.com.br/hc/article_attachments/16201297981719) Acesse a tela Configurações » Controle de Acesso » Relacionamento entre Usuários.

![Imagem 6: No campo usuário, filtre o usuário logado (identificado no item 1).](https://ajuda.sankhya.com.br/hc/article_attachments/16201268757271) No campo usuário, filtre o usuário logado (identificado no item 1).

![Imagem 7: Na aba Membros da fila, verifique se existem usuários informados.](https://ajuda.sankhya.com.br/hc/article_attachments/16201268758295) Na aba **Membros da fila,** verifique se existem usuários informados.

![Imagem 8: Caso a configuração esteja correta, por exemplo, o atual executante deste item é uma "Fila", é necessário que este item…](https://ajuda.sankhya.com.br/hc/article_attachments/16201268759447) Caso a configuração esteja correta, por exemplo, o atual executante deste item é uma "Fila", é necessário que este item seja direcionado a um executante desta fila.

![Imagem 9: Caso a configuração esteja correta, por exemplo, o atual executante deste item é uma "Fila", é necessário que este item…](https://ajuda.sankhya.com.br/hc/article_attachments/14664388475927)

![Imagem 10: Caso a configuração esteja incorreta e o atual executante deste item não seja uma fila, exclua-o da aba Membros da fila…](https://ajuda.sankhya.com.br/hc/article_attachments/16201297986455) Caso a configuração esteja incorreta e o atual executante deste item não seja uma fila, exclua-o da aba Membros da fila.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16201268761623) CAUSA:**

A mensagem: "Impossível preencher campos de tempo em itens de fila: HRFINAL" é apresentada pois o executante do item o qual estão tentando fechar é uma Fila.
