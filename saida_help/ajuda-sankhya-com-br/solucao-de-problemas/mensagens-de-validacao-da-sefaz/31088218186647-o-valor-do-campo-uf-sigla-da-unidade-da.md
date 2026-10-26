---
id: "31088218186647"
titulo: "O valor do campo UF (Sigla da Unidade da Federação) informado não é valido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31088218186647-O-valor-do-campo-UF-Sigla-da-Unidade-da-Federa%C3%A7%C3%A3o-informado-n%C3%A3o-%C3%A9-valido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:33:39Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não é valido", "valor do campo UF", "Rejeição 410", "Erro"]
---

# O valor do campo UF (Sigla da Unidade da Federação) informado não é valido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/31088218176791) **MENSAGEM:**

O valor do campo UF (Sigla da Unidade da Federação) informado não é valido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31088218177559)SOLUÇÃO:**

Para resolver a '**Rejeição 410: UF informada no campo cUF não é atendida pelo webservice'**, verifique se o código da UF informada no campo **cUF** da NF-e está correto em relação a UF do WebService que está fazendo a recepção do documento. Ou seja, verifique se a UF de recepção atende a UF informada na NF-e. Pois, existem estados que não possuem WebService próprio e são atendidos por outros estados da federação.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/31088218178071)CAUSA:**

A Rejeição (410 - UF informada no campo cUF não é atendida pelo webservice) indica a emissão de uma NF-e tendo o campo **cUF** preenchido com uma UF não atendida pela UF de recepção do documento.

Isto implica que foi informado um código do estado incorreto, em que o webservice que está recebendo o XML não atende esta UF ou o webservice que está sendo setado para o envio do documento não é o correto.

Para consultar qual UF recebedora de NF-e uma determinada UF utiliza, verifique no [Portal da NF-e](http://www.nfe.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=Wak0FwB7dKs=).
