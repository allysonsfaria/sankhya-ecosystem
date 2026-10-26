---
id: "4676851918999"
titulo: "Rejeição NFS-e EL10: Item da lista de serviço inexistente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4676851918999-Rejei%C3%A7%C3%A3o-NFS-e-EL10-Item-da-lista-de-servi%C3%A7o-inexistente"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:18:39Z"
rotulos: ["Configuração", "Impostos", "E030", "Prefeituras", "NFS-e", "Rejeição ao gerar lote de NFS-e", "Verifique e registre o item na lista da Prefeitura e atualize o cadastro do serviço", "[E030]: Item da lista de serviço inexistente", "Erro"]
---

# Rejeição NFS-e EL10: Item da lista de serviço inexistente

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16360941974679) MENSAGEM:**

[E030]: Item da lista de serviço inexistente
Possível solução: Consulte a legislação vigente para saber o item da lista de serviço que deverá ser informado neste campo. (RPS Número: X Série: A)

Código: [EL10]

Descrição: Item da lista de Serviço inexistente - Consulte a legislação vigente para saber o item da lista de serviço que deverá ser informado neste campo.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16360941975831) SITUAÇÃO:**

Ao gerar lote de uma NFS-e, é apresentada a mensagem de rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16360893972759)SOLUÇÃO:**

![Imagem 4: Entre em contato com a Prefeitura para verificar a relação de Lista de Serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16360893973527) Entre em contato com a Prefeitura para verificar a relação de Lista de Serviço.

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Lista de Serviços:](https://ajuda.sankhya.com.br/hc/article_attachments/16360893974039) Acesse: Comercial » Arquivo » Cadastros » Lista de Serviços:

- Identifique se o serviço prestado possui uma relação com a Lista de Serviço. Caso não, faça o cadastro de acordo com a lista adquirida na Prefeitura.

![Imagem 6: Acesse: Configurações » Cadastros » Produtos » Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/16360941978007) Acesse: Configurações » Cadastros » Produtos » Serviço

- Aba: **"Impostos"**
- Campo **"Tipo de Serviço"**: informe o código correto neste campo

![Imagem 7: Acesse o Portal de Vendas e gere novo lote de envio para esta NFS-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16360893975447) Acesse o Portal de Vendas e gere novo lote de envio para esta NFS-e.

Foi criado um check no cadastro de Cidades na aba NFS-e, quando ativado o sistema não formata o LC116 deixando conforme o cadastro :

No cadastro da Cidade » aba NFS-e » desmarque o campo **"Não formatar LC116"**

Marcando o campo Não formatar LC116, a tag listadeserviço irá sem o formato com pontuação. **Exemplo:** 17.01, assim a tag passará a apresentar apenas 4 caracteres, ex: 1701.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16360893975703)CAUSA:**

Esta mensagem é apresentada, pois o item da lista de serviço utilizado não está cadastrado no site da Prefeitura em questão.
