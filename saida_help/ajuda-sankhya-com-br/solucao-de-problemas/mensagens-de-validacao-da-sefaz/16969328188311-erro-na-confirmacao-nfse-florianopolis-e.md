---
id: "16969328188311"
titulo: "Erro na confirmação NFSe FLORIANOPOLIS - Erro na resposta do webservice"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16969328188311-Erro-na-confirma%C3%A7%C3%A3o-NFSe-FLORIANOPOLIS-Erro-na-resposta-do-webservice"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:54:05Z"
rotulos: ["Configuração", "XML", "SEFAZ", "Prefeituras", "NFS-e", "Verifique e ajuste o campo Código ID CNAE", "Erro no XML retornado", "Campo Código ID CNAE não preenchido corretamente", "Erro"]
---

# Erro na confirmação NFSe FLORIANOPOLIS - Erro na resposta do webservice

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16969328179479) **MENSAGEM:**

Erro na resposta do webservice: The content of elements must consist of well-formed character data or markup. Não foi retornado um xml válido. Uma das possíveis causas para esse erro, é algum erro que ocorreu no servidor(SEFAZ) e foi redirecionado para uma página HTML.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16969361046551)CAUSA:**

Para emitir NFS-e para Florianópolis foi criado o campo Código ID CNAE dentro do cadastro do serviço, quando o mesmo não é preenchido corretamente, ao confirmar a nota é apresentado o erro.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16969337573527)SOLUÇÃO:**

Como se trata de um erro genérico, pode haver demais informações a serem validadas, mas uma das opções seria:

Verifique em um XML emitido diretamente na Prefeitura de Florianópolis a tag idCNAE

![Imagem 4: Verifique em um XML emitido diretamente na Prefeitura de Florianópolis a tag idCNAE](https://ajuda.sankhya.com.br/hc/article_attachments/16969622676247)

Consulte no cadastro do Serviço, como esta preenchido o campo Código ID CNAE, deve conter a mesma informação do XML emitido na Prefeitura, caso esteja diferente, altere e gere uma nova NFS-e.

![Imagem 5: Consulte no cadastro do Serviço, como esta preenchido o campo Código ID CNAE, deve conter a mesma informação do XML…](https://ajuda.sankhya.com.br/hc/article_attachments/16969357952151)
