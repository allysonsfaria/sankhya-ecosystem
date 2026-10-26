---
id: "360043137574"
titulo: "Não foi possível executar o serviço solicitado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043137574-N%C3%A3o-foi-poss%C3%ADvel-executar-o-servi%C3%A7o-solicitado"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:40Z"
rotulos: ["Configuração", "NF-e", "XML", "Atualização", "SEFAZ", "Atualize o SanNFe para a versão mais recente", "Configure TLSv1.2 no arquivo 'san-nfe.conf'", "XML inválido do webservice SEFaz", "Erro"]
---

# Não foi possível executar o serviço solicitado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16414035011223) MENSAGEM:**

Nenhum site de Nota Fiscal Eletrônica está disponível.
Erros encontrados:
Erro na resposta do webservice. Não foi retornado um xml válido. Uma das possíveis causas para esse erro, é algum erro que ocorreu no servidor(SEFAZ) e foi redirecionado para uma página HTML"

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16414022025367) SITUAÇÃO:**

Ao consultar a Situação do Serviço no SANNFE na versão 4.0 da NF-e, apresenta a mensagem.

![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16414022026519) **SOLUÇÃO:**

A partir da versão do **SanNFe 2.33b10**, por padrão foi inserido o protocolo ssl.context.nfe4=TLSv1.2 , no arquivo '**SanNFe\conf\san-nfe.conf**', para atender a NT2016/002 v1.40, que para a NFe 4.0 passará a utilizar o protocolo TLS a partir de abril/2018.

Foram criadas as seguintes configurações que podem ser inseridas no arquivo 'SanNFe\conf\san-nfe.conf':

ssl.context.nfe4
ssl.context.nfse
ssl.context.cte
ssl.context.mdfe
ssl.context.mde
ssl.context.dfecte

Hoje existe apenas a propriedade ssl.context que vale para todos os serviços, agora tem também uma específica por serviço.

O padrão para todas é o valor da ssl.context, que é SSL.

Se, por exemplo, precisar especificar o protocolo TLS para MDE, basta incluir no SanNFe\conf\san-nfe.conf a linha:
**ssl.context.mde=TLS**

Assim, para MDE o SanNFe ficaria utilizando TLS enquanto que para os outros serviços, SSL.

1ª solução: atualizar o SANNFE para a versão mais recente.

2ª solução: acessar o Servidor onde está instalado o SANNFE e editar o arquivo '**san-nfe.conf**'

O arquivo fica dentro do diretório de instalação do SANNFE: **SanNFe\conf\san-nfe.conf (Windows ou Linux)**

Alterar de:

ssl.context.nfe4=ssl

Para:

ssl.context.nfe4=TLSv1.2

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16414035013783) CAUSA:**

Quando for emitir ou testar o ambiente NF-e 4.0, e o SanNFE estiver desatualizado ou sem os padrões de protocolos de comunicação não informado no arquivo 'san-nfe.conf', apresentará os problemas relacionado acima.
