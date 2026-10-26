---
id: "10135818887703"
titulo: "Para emissão de NFSe para a prefeitura de Goiânia é necessário informar Cód. município DMS para a cidade do prestador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10135818887703-Para-emiss%C3%A3o-de-NFSe-para-a-prefeitura-de-Goi%C3%A2nia-%C3%A9-necess%C3%A1rio-informar-C%C3%B3d-munic%C3%ADpio-DMS-para-a-cidade-do-prestador"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:25Z"
rotulos: ["Configuração", "Cidades", "CORE_E00559", "Prefeituras", "NFS-e", "Emissão de NFSe para Goiânia e Cód. Município DMS", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Para emissão de NFSe para a prefeitura de Goiânia é necessário informar Cód. município DMS para a cidade do prestador

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16446906624535) MENSAGEM:**

[CORE\_E00559] Para emissão de NFS-e para a prefeitura de Goiânia é necessário informar Cód. município DMS para a cidade do prestador. Faça a alteração no cadastro de Cidades.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16446906628631) SITUAÇÃO:**

Ao tentar emitir Nota Fiscal de Serviço Eletrônica da prefeitura de Goiânia a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16446906631447) SOLUÇÃO:**

Quando o campo "Cidade" for preenchido na **central de vendas** (Caminho de acesso à tela: Comercial » Rotinas » Central de Vendas) o sistema considera esse município como o de prestação. Caso o campo não esteja preenchido o sistema considera a cidade do prestador configurada no cadastro de empresa.

![Imagem 4: Quando o campo " Cidade " for preenchido na central de vendas (Caminho de acesso à tela: Comercial » Rotinas » Central…](https://ajuda.sankhya.com.br/hc/article_attachments/16446838379799)

Nesse caso, para que a mensagem de erro não seja apresentada, acesse o cadastro de **Cidades** (Configurações » Cadastros » Endereços » Cidades) e preencha com o código de Goiânia.

![Imagem 5: Cada cidade possui código DMS.](https://ajuda.sankhya.com.br/hc/article_attachments/16446872433431)

Cada cidade possui código DMS.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16446901127447) CAUSA:**

Ocorre quando a cidade é informada no cabeçalho da nota, mas o Cód. município DMS não foi informado no cadastro da cidade.
