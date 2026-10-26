---
id: "9293993755799"
titulo: "\"ISNULL\": identificador inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9293993755799--ISNULL-identificador-inv%C3%A1lido"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:09:00Z"
rotulos: ["Produtos", "Configuração", "Central de Compras", "Fórmulas", "CORE_E04804", "Fórmula de Custo/Preço", "Revisão da fórmula", "ORA-00904", "Erro"]
---

# "ISNULL": identificador inválido

**MENSAGEM:**

[CORE\_E04804]  ORA-00904: "ISNULL": identificador inválido.

**SITUAÇÃO:**

Ao tentar confirmar uma transferência entre locais ou confirmar uma nota na central de compras a mensagem é apresentada.

**CAUSA:**

Ocorre por erro na fórmula.

**SOLUÇÃO:**

Em ambos os casos, faça a revisão da **Fórmula de custo/preço** (Caminho de acesso à tela: Comercial » Avançado » Fórmulas » Fórmulas de Custo/Preço)

![Imagem 1: Em ambos os casos, faça a revisão da Fórmula de custo/preço (Caminho de acesso à tela: Comercial » Avançado » Fórmulas…](https://ajuda.sankhya.com.br/hc/article_attachments/9293960567703)

Para isso, acesse o cadastro do **Produto** (Caminho de acesso à tela: Configurações » Cadastros » Produtos » Produtos) em questão, vá até a aba "Formação de Custo/Preço" e verifique a fórmula informada, ou caso a Empresa trabalhe com "**Custo por Empresa**", verifique a fórmula nas Preferências da Empresa (Caminho de acesso à tela: Comercial » Preferências » Empresa).

![Imagem 2: Para isso, acesse o cadastro do Produto ( Caminho de acesso à tela: Configurações » Cadastros » Produtos » Produtos) em…](https://ajuda.sankhya.com.br/hc/article_attachments/18787639477527)
