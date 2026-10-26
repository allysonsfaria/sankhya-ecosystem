---
id: "30139667382935"
titulo: "As UFs a seguir não utilizam a configuração de Webservice do Portal GNRE: XX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30139667382935-As-UFs-a-seguir-n%C3%A3o-utilizam-a-configura%C3%A7%C3%A3o-de-Webservice-do-Portal-GNRE-XX"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:36:28Z"
rotulos: ["Configuração", "SEFAZ", "GNRE", "Passos para resolver", "Razão do erro", "Detalhe do erro", "FIN_E00539", "Erro", "Documentos Eletrônicos"]
---

# As UFs a seguir não utilizam a configuração de Webservice do Portal GNRE: XX

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30139707283095) **MENSAGEM:**

[FIN\_E00539] As UFs a seguir não utilizam a configuração de Webservice do Portal GNRE: XX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30139667380887)SOLUÇÃO:**

Verifique no cadastro do **Estado** (Configurações » Cadastros » Endereços » Estados), se o campo **Utiliza webservice para GNRE** está marcado e valide junto ao Portal GNRE a habilitação de uso do Web Service, lembrando que além desta solicitação, é necessário o uso do certificado digital da sua empresa.

![Imagem 3: Verifique no cadastro do Estado (Configurações » Cadastros » Endereços » Estados) , se o campo Utiliza webservice para…](https://ajuda.sankhya.com.br/hc/article_attachments/30192600448151)

Informações no Portal GNRE sobre a solicitação de uso do Webservice:

[https://www.gnre.pe.gov.br:444/gnre/portal/automacao.jsp#](https://www.gnre.pe.gov.br:444/gnre/portal/automacao.jsp)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30139667381527)CAUSA:**

Ocorre ao tentar enviar um lote GNRE pela tela Geração de Lote GNRE sem que a marcação **Utiliza webservice para GNRE** ou habilitação junto ao Portal GNRE esteja realizada.
