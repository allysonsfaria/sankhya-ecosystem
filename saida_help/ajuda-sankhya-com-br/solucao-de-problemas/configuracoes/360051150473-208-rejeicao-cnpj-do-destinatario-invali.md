---
id: "360051150473"
titulo: "208 - Rejeição: CNPJ do destinatário inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051150473-208-Rejei%C3%A7%C3%A3o-CNPJ-do-destinat%C3%A1rio-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:30:49Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "XML", "SEFAZ", "Rejeição 208", "CNPJ do Destinatário", "Correção de Cadastro", "Erro"]
---

# 208 - Rejeição: CNPJ do destinatário inválido

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18588952926615) MENSAGEM**:

208 - Rejeição: CNPJ do destinatário inválido.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588952935959) CAUSA:**

Ocorre quando se informado CNPJ com zeros ou dígito de controle inválido.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18588968902807) SOLUÇÃO:**

![Imagem 4: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/18588952955159) Configurações » Cadastros » Parceiros

1.1-Verifique e corrija o CNPJ do destinatário: Se informado CNPJ com zeros ou dígito de controle inválido, a rejeição será apresentada.

![Imagem 5: Deve-se consultar o CNPJ correto do destinatário no SINTEGRA e ajustar no cadastro do parceiro.Após corrigido, redigite…](https://ajuda.sankhya.com.br/hc/article_attachments/18588968912407) Deve-se consultar o CNPJ correto do destinatário no [SINTEGRA](http://www.sintegra.gov.br/) e ajustar no cadastro do parceiro.Após corrigido, redigite o cabeçalho da nota e gere um novo lote.

**Importante:**

![Imagem 6: Ao realizar a consulta no SINTEGRA , certifique-se que a situação Cadastral do parceiro encontra-se ATIVA/HABILITADA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588968918167) Ao realizar a consulta no [SINTEGRA](http://www.sintegra.gov.br/), certifique-se que a situação Cadastral do parceiro encontra-se ATIVA/HABILITADA:

![Imagem 7: Ao realizar a consulta no SINTEGRA , certifique-se que a situação Cadastral do parceiro encontra-se ATIVA/HABILITADA:](https://ajuda.sankhya.com.br/hc/article_attachments/18588952970391)

![Imagem 8: Ao gerar o XML em conferência, estará sendo validado nessa rejeição, as informações enviadas na tag <CNPJ> .](https://ajuda.sankhya.com.br/hc/article_attachments/18588952985111) Ao gerar o XML em conferência, estará sendo validado nessa rejeição, as informações enviadas na tag **<CNPJ>**.

![Imagem 9: Para parceiros 'estrangeiros' lembre-se de preencher o parâmetro CODPAISBRASIL (55). Mais detalhes, acesse: Quais as…](https://ajuda.sankhya.com.br/hc/article_attachments/18588968955543) Para parceiros 'estrangeiros' lembre-se de preencher o parâmetro CODPAISBRASIL [55]. Mais detalhes, acesse:[Quais as principais configurações para emissão de nota de exportação - parceiro estrangeiro ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042535474)
