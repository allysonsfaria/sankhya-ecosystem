---
id: "360042755774"
titulo: "A Justificativa de entrada em contingencia deve ser informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042755774-A-Justificativa-de-entrada-em-contingencia-deve-ser-informada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:14Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "Portal de Vendas", "SEFAZ", "557", "Gere novo lote e verifique justificativa", "Justificativa de contingência ausente", "Emissão no EPEC sem justificativa", "Erro", "Documentos Eletrônicos"]
---

# A Justificativa de entrada em contingencia deve ser informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16453118828439) MENSAGEM:**

[557 - Rejeição]: A Justificativa de entrada em contingência deve ser informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16453087091351) SOLUÇÃO:**

No sistema essa mensagem normalmente é retornada de forma "indevida" pela SEFAZ. Dessa forma, precisamos que um novo lote seja gerado, na expectativa que essa rejeição seja atualizada para uma rejeição válida.

**(1)** Gere um novo lote da respectiva nota, caso essa se mantenha 'Aguardando Correção', certifique-se que a última rejeição retornada foi atualizada para uma rejeição que difere da citada nesse artigo, e proceda com a tratativa da mesma.

Acesse: "[**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014)" :

- **"Outras Opções...": "Ver** **acompanhamento**"

Caso utilize os sistemas **G1/MGE** siga com os passos abaixo:

![Imagem 3: Acesse a tela " Manutenção de Contingência " : (Caminho de acesso: Comercial » Avançado » Manutenção de Contingência) :](https://ajuda.sankhya.com.br/hc/article_attachments/16453118839191) Acesse a tela "**[Manutenção de Contingência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612534)"**: (Caminho de acesso: Comercial » Avançado » Manutenção de Contingência) :

![Imagem 4: Certifique-se que existe uma justificativa de Contingência cadastrada para o período que foi lançada a nota em EPEC,…](https://ajuda.sankhya.com.br/hc/article_attachments/16453087099415) Certifique-se que existe uma justificativa de Contingência cadastrada para o período que foi lançada a nota em EPEC, que defina a causa do envio fora do ambiente Normal.
Exemplo: 'Justificativa: Contingência SVC em decorrência de problemas técnicos.'

![Imagem 5: Em caso negativo, cadastre a mesma.](https://ajuda.sankhya.com.br/hc/article_attachments/16453087101335) Em caso negativo, cadastre a mesma.

![Imagem 6: Inserir o Nro único Nota do lançamento rejeitado.](https://ajuda.sankhya.com.br/hc/article_attachments/16453087103767) Inserir o Nro único Nota do lançamento rejeitado.

![Imagem 7: Realizado o vínculo da nota na justificativa adequada, gere um novo lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16453087109399) Realizado o vínculo da nota na justificativa adequada, gere um novo lote.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16453118854423) CAUSA:**

Mensagem apresentada na emissão de nota eletrônica no ambiente EPEC, sem o vínculo da justificativa desse envio em contingência.
