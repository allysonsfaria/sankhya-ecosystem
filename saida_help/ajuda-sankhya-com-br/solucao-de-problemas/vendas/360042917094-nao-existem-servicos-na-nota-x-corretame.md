---
id: "360042917094"
titulo: "Não existem serviços na nota 'X' corretamente configurados para a emissão da Nota Fiscal Eletrônica de Serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042917094-N%C3%A3o-existem-servi%C3%A7os-na-nota-X-corretamente-configurados-para-a-emiss%C3%A3o-da-Nota-Fiscal-Eletr%C3%B4nica-de-Servi%C3%A7os"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:01Z"
rotulos: ["#PUBLIFER", "CORE_E00576", "Produtos", "Configuração", "Fiscal", "NFS-e", "Corrija 'Usado como' para produtos", "Verifique cadastro de serviços", "Use a tela correta para serviços", "Erro"]
---

# Não existem serviços na nota 'X' corretamente configurados para a emissão da Nota Fiscal Eletrônica de Serviços

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16117005029527) MENSAGEM:**

[CORE\_E00576] Não existem serviços na nota 'X' corretamente configurados para a emissão da Nota Fiscal Eletrônica de Serviços.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117034980247) SITUAÇÃO:**

Mensagem apresentada na emissão de nota fiscal de serviço.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16117034983319) SOLUÇÃO:**

![Imagem 4: Certifique-se que os itens inseridos na nota foram cadastrados na tela "Serviço" (Caminho de acesso: Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/16117034987287) Certifique-se que os itens inseridos na nota foram cadastrados na tela **"Serviço"** (Caminho de acesso: Configurações » Cadastros » Produtos » Serviços):

![Imagem 5: Certifique-se que os itens inseridos na nota foram cadastrados na tela "Serviço" (Caminho de acesso: Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/12069677724439)

![Imagem 6: Caso o cadastro tenha sido realizado na tela "Produtos" , a emissão de NFS-e não será permitida, visto que será…](https://ajuda.sankhya.com.br/hc/article_attachments/16117005042711) Caso o cadastro tenha sido realizado na tela **"Produtos"**, a emissão de NFS-e não será permitida, visto que será validado o **"USOPROD = 'S'"**. Realizado o cadastro corretamente, refaça o lançamento. 

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16117005046167) CAUSA:**

Mensagem apresentada na emissão de nota fiscal de serviços quando o 'Usado como' do produto difere de 'Serviço'.
