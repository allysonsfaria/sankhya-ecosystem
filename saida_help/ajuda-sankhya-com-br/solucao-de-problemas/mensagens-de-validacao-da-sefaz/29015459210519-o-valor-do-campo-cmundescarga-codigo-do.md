---
id: "29015459210519"
titulo: "O valor do campo cMunDescarga (Código do Município de Descarregamento) informado não é válido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29015459210519-O-valor-do-campo-cMunDescarga-C%C3%B3digo-do-Munic%C3%ADpio-de-Descarregamento-informado-n%C3%A3o-%C3%A9-v%C3%A1lido"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:37:25Z"
rotulos: ["MDF-e", "Configuração", "Parceiro", "NF-e", "Cidades", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "cMunDescarga", "Documentos Eletrônicos"]
---

# O valor do campo cMunDescarga (Código do Município de Descarregamento) informado não é válido

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/29015432818455) **MENSAGEM:**

O valor do campo cMunDescarga (Código do Município de Descarregamento) informado não é válido.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29015459170327)SOLUÇÃO:**

![Imagem 3: Na Tela "Viagens de Transporte (MDF-e)" selecione o MDF-e com a rejeição e gere o XML em conferência, conforme imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/29015432833687) Na Tela "Viagens de Transporte (MDF-e)" selecione o MDF-e com a rejeição e gere o XML em conferência, conforme imagem abaixo.

![Imagem 4: Na Tela "Viagens de Transporte (MDF-e)" selecione o MDF-e com a rejeição e gere o XML em conferência, conforme imagem…](https://ajuda.sankhya.com.br/hc/article_attachments/29649758735639)

![Imagem 5: Após isso, abra o arquivo XML no navegador e busque pelo texto "cMun", conforme imagem abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/29015432839063) Após isso, abra o arquivo XML no navegador e busque pelo texto "cMun", conforme imagem abaixo.

![Imagem 6: Após isso, abra o arquivo XML no navegador e busque pelo texto "cMun", conforme imagem abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/29649758737175)

![Imagem 7: Localize a chave de acesso da NF-e em que o campo cMun está incorreto e acesse o cadastro do parceiro vinculado à nota…](https://ajuda.sankhya.com.br/hc/article_attachments/29015459184791) Localize a chave de acesso da NF-e em que o campo **cMun** está incorreto e acesse o cadastro do parceiro vinculado à nota em questão. No cadastro do parceiro, navegue até a aba "Endereço" e valide a cidade configurada.

![Imagem 8: Logo em seguida, acesse o cadastro da cidade, a fim de validar o campo "Mun. domicílio fiscal".](https://ajuda.sankhya.com.br/hc/article_attachments/29015432848663) Logo em seguida, acesse o cadastro da cidade, a fim de validar o campo "Mun. domicílio fiscal".

**OBSERVAÇÃO:**

A cidade que foi levada no XML pode estar tanto na aba "Endereço" quanto na aba "Endereço de entrega", sendo necessário validar no cadastro do parceiro, conforme imagem abaixo.

![Imagem 9: A cidade que foi levada no XML pode estar tanto na aba "Endereço" quanto na aba "Endereço de entrega", sendo necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/29649734965783)

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/29015459192599)CAUSA:**

Quando uma NF-e for emitida e o Código do Município de Descarregamento (Município do domicílio fiscal) informado no cadastro da cidade estiver em branco ou incorreto de acordo com o IBGE, será apresentada uma rejeição, sendo necessário validar o cadastro do parceiro utilizado na NF-e.
