---
id: "7919603403927"
titulo: "Empresa X de negociação não está ativa para a nota de Nro Único: XXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7919603403927-Empresa-X-de-negocia%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-ativa-para-a-nota-de-Nro-%C3%9Anico-XXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:12:39Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "XML", "não apagar", "ORA-20101", "Ativação de Empresa para Nota Única", "Erro"]
---

# Empresa X de negociação não está ativa para a nota de Nro Único: XXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16361645474071) MENSAGEM:**

[ORA-20101]: Empresa X de negociação não está ativa para a nota de Nro Único: XXX.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16361645476887)SOLUÇÃO:**

![Imagem 3: Acesse a tela: "Configurador de Layout da Nota", localize o layout do pedido/nota de compra e disponibilize o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16361630264343) Acesse a tela: "Configurador de Layout da Nota", localize o layout do pedido/nota de compra e disponibilize o campo **"Empresa da Negociação"**, conforme print abaixo.

![Imagem 4: Em seguida, na Central de Compras, caso a tela esteja aberta, feche e abra novamente para que o campo seja carregado.](https://ajuda.sankhya.com.br/hc/article_attachments/14680319121943)

![Imagem 5: Em seguida, na Central de Compras, caso a tela esteja aberta, feche e abra novamente para que o campo seja carregado.](https://ajuda.sankhya.com.br/hc/article_attachments/16361645477655) Em seguida, na Central de Compras, caso a tela esteja aberta, feche e abra novamente para que o campo seja carregado.

![Imagem 6: Verifique o campo "Empresa da Negociação", que deve estar incorretamente informado.](https://ajuda.sankhya.com.br/hc/article_attachments/16361630266391) Verifique o campo "Empresa da Negociação", que deve estar incorretamente informado.

![Imagem 7: Faça o ajuste e teste novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16361645479575) Faça o ajuste e teste novamente.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16361630267543)CAUSA:**

Acontece quando o arquivo XML vem com a informação de empresa negociação na tag e no momento da confirmação da nota na central o campo não existe no layout, ou caso exista, está oculto com valor incorreto.
