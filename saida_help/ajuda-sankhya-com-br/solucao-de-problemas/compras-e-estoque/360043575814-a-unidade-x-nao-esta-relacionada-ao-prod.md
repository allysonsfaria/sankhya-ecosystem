---
id: "360043575814"
titulo: "A Unidade 'X' não está relacionada ao produto 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043575814-A-Unidade-X-n%C3%A3o-est%C3%A1-relacionada-ao-produto-X"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:18Z"
rotulos: ["#PUBLIFER", "CORE_E03128", "Produtos", "Configuração", "NF-e", "XML", "Cadastro", "Falta de Relacionamento de Unidade", "Erro"]
---

# A Unidade 'X' não está relacionada ao produto 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16171313452439) MENSAGEM:**

[CORE\_E03128] A Unidade 'X' não está relacionada ao produto 'X'. Relacione a Unidade através das configurações de Unidade padrão, Unid. Compra ou Unidade Alternativa. Caso seja uma Unid. de Compra, ela também deve estar cadastrada como Unid. Alternativa.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16171297815063) SOLUÇÃO:**

![Imagem 3: Acesse o cadastro do respectivo produto: Tela "Produtos" (Configurações » Cadastros » Produtos).](https://ajuda.sankhya.com.br/hc/article_attachments/16171297817239) Acesse o cadastro do respectivo produto: Tela **"Produtos"** (Configurações » Cadastros » Produtos).

![Imagem 4: Certifique-se que a unidade mencionada na mensagem de validação encontra-se devidamente cadastrada para esse produto,…](https://ajuda.sankhya.com.br/hc/article_attachments/16171297820311) Certifique-se que a unidade mencionada na mensagem de validação encontra-se devidamente cadastrada para esse produto, conforme exemplo abaixo:

- Aba **Geral** » Campo **"Unid.Compra":**

![Imagem 5: Aba Geral » Campo "Unid.Compra":](https://ajuda.sankhya.com.br/hc/article_attachments/14691749939479)

- Aba **Unidades Alternativas**: Cadastre a respectiva unidade corretamente. Para mais detalhes: [Clique aqui.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-#abaunidadesalternativas)

![Imagem 6: Aba Unidades Alternativas : Cadastre a respectiva unidade corretamente. Para mais detalhes: Clique aqui.](https://ajuda.sankhya.com.br/hc/article_attachments/14691785034135)

![Imagem 7: Realizado o cadastro da respectiva unidade corretamente, refaça a importação do XML.](https://ajuda.sankhya.com.br/hc/article_attachments/16171313464343) Realizado o cadastro da respectiva unidade corretamente, refaça a importação do XML.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16171297835927) CAUSA:**

Mensagem apresentada, quando a **Unidade** referenciada para o respectivo produto no XML, não encontra-se cadastrada para esse produto no sistema.
