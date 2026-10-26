---
id: "9800946327703"
titulo: "Não podemos agrupar produtos com unidades diferentes "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9800946327703-N%C3%A3o-podemos-agrupar-produtos-com-unidades-diferentes"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:06:03Z"
rotulos: ["Produtos", "Configuração", "Preferências", "CORE_E04665", "Erro ao Agrupar Produtos com Unidades Diferentes", "Erro"]
---

# Não podemos agrupar produtos com unidades diferentes 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19296843332375) MENSAGEM:**

[CORE\_E04665] Não podemos agrupar produtos com unidades diferentes.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19296888356119) SITUAÇÃO:**

Ao faturar dois pedidos agrupados tendo 2 unidades diferentes para o mesmo produto a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19296843336215) CAUSA:**

Agrupar dois pedidos com mesmo produto porém unidades diferentes.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19296843339415) SOLUÇÃO:**

Existe um parâmetro que faz essa validação quando se trata do mesmo produto porém com unidades diferentes.

Assim, acesse a tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências) informe a chave **'Agrupar prod.repetido em qualquer faturamento? - AGRUPFATSEMP'** e desligue o mesmo.

![Imagem 5: Assim, acesse a tela Preferências (Caminho de acesso à tela: Configurações » Avançado » Preferências) informe a chave…](https://ajuda.sankhya.com.br/hc/article_attachments/19296888422935)

Trata-se de comportamento. Se o parâmetro estiver ligado o sistema irá tentar agrupar os produtos repetidos nos pedidos em uma linha só e, se tiver unidade diferente, não irá ser agrupado e a mensagem será apresentada.
Sendo assim, deve-se ajustar um dos pedidos ou avaliar a possibilidade de trabalhar com este parâmetro desabilitado.

Existe ainda a possibilidade de faturar os pedidos separadamente.
