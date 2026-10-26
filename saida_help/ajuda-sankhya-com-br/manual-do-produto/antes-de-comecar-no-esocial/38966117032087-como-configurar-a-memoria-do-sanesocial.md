---
id: "38966117032087"
titulo: "Como configurar a memória do SanESocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38966117032087-Como-configurar-a-mem%C3%B3ria-do-SanESocial"
trilha: "Manual do Produto > Pessoas+ > eSocial > Antes de Começar no eSocial"
atualizado_em: "2026-10-02T15:57:19Z"
rotulos: ["Produtos", "Configuração", "Linux", "eSocial", "Windowns", "SanESocial", "Memória do SanESocial", "Configuração de Memória do SanESocial", "sanesocial-service", "Central de Projetos", "Windows"]
---

# Como configurar a memória do SanESocial

#### Windows

- ##### Para configurar a memória do SanESocial no ambiente Windows, caso ele seja iniciado como serviço:

Exemplo: **-J-Xms3072m -J-Xmx3072m**

![Imagem 1: Exemplo: -J-Xms3072m -J-Xmx3072m](https://ajuda.sankhya.com.br/hc/article_attachments/38967907057687)

- Também é possível criar um arquivo com as configurações padrão. Na mesma pasta onde se encontra o launcher da aplicação, deve ser criado o arquivo **"sanesocial-service.vmoptions"**, contendo as configurações **Xms** e **Xmx**.

![Imagem 2: Também é possível criar um arquivo com as configurações padrão. Na mesma pasta onde se encontra o launcher da…](https://ajuda.sankhya.com.br/hc/article_attachments/38967931096343)

#

#### Linux

- No Linux basta alterar as propriedades **-XMX** e -**XMS** do **sanesocial-service**.

![Imagem 3: No Linux basta alterar as propriedades -XMX e - XMS do sanesocial-service .](https://ajuda.sankhya.com.br/hc/article_attachments/38967931100823)
