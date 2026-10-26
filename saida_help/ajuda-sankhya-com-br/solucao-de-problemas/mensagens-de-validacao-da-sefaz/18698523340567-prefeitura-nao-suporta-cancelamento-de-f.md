---
id: "18698523340567"
titulo: "Prefeitura não suporta cancelamento de forma automática (via integração/WebService)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/18698523340567-Prefeitura-n%C3%A3o-suporta-cancelamento-de-forma-autom%C3%A1tica-via-integra%C3%A7%C3%A3o-WebService"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:52:12Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Cancelamento Manual pela Prefeitura", "Erro", "Documentos Eletrônicos"]
---

# Prefeitura não suporta cancelamento de forma automática (via integração/WebService)

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18698561610263) **MENSAGEM:**

Prefeitura não suporta cancelamento de forma automática (via integração/WebService).

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18698534170903)CAUSA:**

O erro é apresentado porque essa Prefeitura em específico não permite cancelamento de notas via WebService, ou seja, por outros sistemas que não seja o seu Portal interno.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18698517370007)SOLUÇÃO:**

Nesse caso, é necessário que os cancelamentos sejam feitos a partir do Portal da Prefeitura, após certificar que a nota está devidamente cancelada na Prefeitura você deve validar esse cancelamento também no sistema, para que as informações fiquem de acordo tanto no sistema quanto na Prefeitura. Para isso é necessário ajustar as seguintes configurações:

- Cadastro de Cidades, aba > NFS-e, Campo:  Tipo de cancelamento para NFS-e = **Via prefeitura sem número de protocolo.**

**Nota:**

Para maiores informações acesse o artigo: [Nota Fiscal Eletrônica de Serviço - Prefeituras](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603434-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7o-Prefeituras)
