---
id: "360043003853"
titulo: "Invalid content was found starting with element 'Discriminacão'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043003853-Invalid-content-was-found-starting-with-element-Discriminac%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:24Z"
rotulos: ["ERRONF", "Configuração", "Impostos", "Prefeituras", "NFS-e", "Correção de 'Discriminação' na NFS-e", "Erro"]
---

# Invalid content was found starting with element 'Discriminacão'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16455322435095) MENSAGEM:**

Invalid content was found starting with element 'Discriminação'. One of '{"http://www.abrasf.org.br/nfse.xsd":CodigoTributacaoMunicipio}' is expected

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16455305920279) SOLUÇÃO:**

Para correção, siga os passos abaixo.

![Imagem 3: Acesse a tela: " Serviço" : (Caminho de Acesso: Configurações » Cadastros » Produtos » Serviço )](https://ajuda.sankhya.com.br/hc/article_attachments/16455305923607) Acesse a tela: "**[Serviço"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553)** : (Caminho de Acesso: Configurações » Cadastros » Produtos » Serviço)

- Aba: "**Impostos"**

- Campo: "**Cód. Trib. Município NFS-e":** preencha o campo com um valor válido fornecido pela Prefeitura (buscar orientações com o Contador).

![Imagem 4: Acesse a tela: " Alíquotas de ISS ": (Caminho de Acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ISS…](https://ajuda.sankhya.com.br/hc/article_attachments/16455322445847) Acesse a tela: "[**Alíquotas de ISS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014)": (Caminho de Acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ISS)

- Campo: "**Cód. trib. Município"**: preencha o campo com um valor válido fornecido pela Prefeitura (buscar orientações com o Contador).

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16455305928727) CAUSA:**

Ao gerar uma NFS-e onde as informações de ‘Tributação do Município' não estão devidamente preenchidas, ocorrerá a rejeição.
