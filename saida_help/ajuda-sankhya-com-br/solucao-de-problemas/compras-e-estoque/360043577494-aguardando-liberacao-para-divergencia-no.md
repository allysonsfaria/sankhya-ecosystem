---
id: "360043577494"
titulo: "Aguardando liberação para divergência nos cadastros do produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043577494-Aguardando-libera%C3%A7%C3%A3o-para-diverg%C3%AAncia-nos-cadastros-do-produtos"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-31T00:13:40Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "Eventos", "Liberação de Limites", "XML", "Importação", "Liberação de Divergências em Produtos"]
---

# Aguardando liberação para divergência nos cadastros do produtos

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16192418199063) MENSAGEM:**

Aguardando liberação para divergência nos cadastros dos produtos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16192437818135) SOLUÇÃO:**

Esta mensagem está relacionada ao evento de liberação conforme configurado na tela '**Configurações para liberação de Divergências'** Significa que o XML importado está trazendo um valor diferente do que já está informado no cadastro de produto, considerando: NCM, CEST, Origem e FCI. O Evento pode

ser visualizado na tela do portal de importação de xml, no botão Liberações.

![Imagem 3: ser visualizado na tela do portal de importação de xml, no botão Liberações.](https://ajuda.sankhya.com.br/hc/article_attachments/33050224204439)

![Imagem 4: O usuário liberador deverá tomar a decisão se aceita ou não essas divergências e efetuar a liberação, ou negação do…](https://ajuda.sankhya.com.br/hc/article_attachments/16192418204439) O usuário liberador deverá tomar a decisão se aceita ou não essas divergências e efetuar a liberação, ou negação do evento em: Configurações » Avançado » Liberação de Limites. O evento acionado precisa

está configurado para o usuário liberador em Usuários / Outras opções / 'Limites para Liberação'

![Imagem 5: A configuração para validação deste evento é feita através do botão "Outras Opções" , opção "Configurações para…](https://ajuda.sankhya.com.br/hc/article_attachments/16192437820567) A configuração para validação deste evento é feita através do botão **"Outras Opções"**, opção **"Configurações para liberação de Divergências",** na tela **"[Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354)"** (Caminho de acesso: Comercial » Rotinas » Portal de importação de XML), com as opções abaixo:

![Imagem 6: A configuração para validação deste evento é feita através do botão "Outras Opções" , opção "Configurações para…](https://ajuda.sankhya.com.br/hc/article_attachments/14680380513687)

![Imagem 7: A configuração para validação deste evento é feita através do botão "Outras Opções" , opção "Configurações para…](https://ajuda.sankhya.com.br/hc/article_attachments/32847712863639)

![Imagem 8: Solicite ao gestor da área verificar as opções e escolher a melhor alternativa para o seu processo.](https://ajuda.sankhya.com.br/hc/article_attachments/16192418210455) Solicite ao gestor da área verificar as opções e escolher a melhor alternativa para o seu processo.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16192418211863) CAUSA:**

Ocorre quando a configuração de divergência de produtos, está ajustado para exigir liberação.

Eventos:

75 Diferença entre NCM, CEST, Origem ou FCI
85 Diferença entre NCM
86 Diferença entre CEST
87 Diferença entre Origem.
88 Diferença entre FCI
