---
id: "4410489682455"
titulo: "Divergência entre dicionário de dados e arquivos binários do sistema"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4410489682455-Diverg%C3%AAncia-entre-dicion%C3%A1rio-de-dados-e-arquivos-bin%C3%A1rios-do-sistema"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:21:19Z"
rotulos: ["Configuração", "Atualização", "Dicionário de Dados", "#publicadoHyago", "#validadoJoaogomes", "divergência atualização backup", "Erro", "Sistema"]
---

# Divergência entre dicionário de dados e arquivos binários do sistema

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16120469232279) MENSAGEM**:

Divergência entre dicionário de dados e arquivos binários do sistema.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16120493771159) CAUSA:**

O erro pode ser apresentado devido a alguma atualização malsucedida (evento mais comum) ou  pela restauração de um backup da base de produção na base de testes sem atualizar a versão/release. exemplo:

**(1)** No caso apresentado, a versão da base de produção estava na 4.8b423 e a de testes estava na 4.6b248, ao restaurar o backup da base de produção ela virá, então, com a estrutura que lá estava: objetos e dicionários de dados da versão 4.8b423. Assim, o próximo passo a fazer na base de testes é atualizá-la com um pkg da versão 4.8b423 ou de uma versão superior a fim de 'alinhar' a versão de dicionário de dados e binários evitando o erro acima.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16120493768087) SOLUÇÃO:**

Execute a atualização do sistema para a um versão mais recente ou de acordo com a que foi apresentada na Versão do dicionário de dados da mensagem.
