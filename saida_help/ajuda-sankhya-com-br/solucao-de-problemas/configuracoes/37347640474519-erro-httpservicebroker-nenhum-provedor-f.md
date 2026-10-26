---
id: "37347640474519"
titulo: "Erro: \"HttpServiceBroker: Nenhum provedor foi encontrado para o serviço 'XXXXX'.\" em integração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37347640474519-Erro-HttpServiceBroker-Nenhum-provedor-foi-encontrado-para-o-servi%C3%A7o-XXXXX-em-integra%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:13:16Z"
rotulos: ["Configuração", "MGE", "Integração", "NFS-e", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "CACSP.incluirNota", "\"HttpServiceBroker", "Nenhum provedor foi encontrado para serviço", "MGECOM", "não pertence ao módulo informado"]
---

# Erro: "HttpServiceBroker: Nenhum provedor foi encontrado para o serviço 'XXXXX'." em integração

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/37347640466327) **MENSAGEM:**

"statusMessage": "HttpServiceBroker: Nenhum provedor foi encontrado para o serviço 'CACSP.incluirNota'."

![Imagem 2: "statusMessage": "HttpServiceBroker: Nenhum provedor foi encontrado para o serviço 'CACSP.incluirNota'."](https://ajuda.sankhya.com.br/hc/article_attachments/37347640466583)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/37347661939607)SOLUÇÃO:**

**(1)** Identifique o serviço informado no erro:

```
CACSP.incluirNota
```

**(2)** Verifique o módulo da URL utilizada na requisição.

- Confira se a chamada está sendo feita para:

```
/gateway/v1/mge/service.sbr
```

**(3)** Ajuste o módulo da URL, se necessário.

- O serviço **CACSP.incluirNota** pertence ao módulo **MGECOM** e não funciona no módulo MGE.
- A URL correta do módulo MGECOM:

```
/gateway/v1/mgecom/service.sbr?serviceName=CACSP.incluirNota&outputType=json
```

**(4)** Execute novamente a requisição.

**(5)** Após o ajuste da URL, o serviço será localizado corretamente e o erro não ocorrerá.

**OBSERVAÇÃO:** As URLs citadas são exemplos. O mesmo erro pode ocorrer com outros serviços e módulos sempre que a requisição for feita em um módulo diferente daquele ao qual o serviço pertence.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/37347661940503)CAUSA:**

O erro ocorre porque o serviço chamado **não pertence ao módulo informado** na requisição.

**Exemplo:**

Ao tentar incluir uma nota utilizando a URL do módulo **MGE**, a requisição falha, pois o serviço `CACSP.incluirNota` pertence ao módulo **MGECOM** e só funciona quando chamado nesse módulo. Ou seja, a requisição está apontando para o módulo errado, e o **Gateway** não encontra nenhum provedor que possa processar a chamada.
