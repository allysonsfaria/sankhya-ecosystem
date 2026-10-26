---
id: "360044526913"
titulo: "Como ter um controle de local dos produtos comercializados no FAST Service?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044526913-Como-ter-um-controle-de-local-dos-produtos-comercializados-no-FAST-Service"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:55:46Z"
rotulos: ["Produtos", "Configuração", "Fast Service", "Estoque", "Preferências", "Local Padrão Usuário: Baixa de produtos", "Preferências Empresa: Uso do parâmetro LOCALPADRAOFST", "Exceção Fast Service: Controle por local ignorado"]
---

# Como ter um controle de local dos produtos comercializados no FAST Service?

**(1)** Considere o comportamento da aplicação, conforme abaixo:

![Imagem 1: Acesse: Configurações » Controle de Acesso » Usuários](https://ajuda.sankhya.com.br/hc/article_attachments/16831592151319)  Acesse: Configurações » Controle de Acesso » Usuários

O primeiro campo a ser utilizado como local na baixa de um produto no FAST Service é o Local Padrão do cadastro do Usuário.

- Configurações » Controle de Acesso » Usuários

Botão: Outras Opções...>>Configurações do Usuário

Campo: **"Local padrão para pedidos e notas"**

![Imagem 2: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16831618520855) Acesse: Configurações » Avançado » Preferências

Caso o campo acima não esteja preenchido, o sistema verifica o parâmetro **"LOCALPADRAOFST'-Usa Local Padrão Empresa no Fast Service?"** (Ligado/Desligado)

Caso este parâmetro esteja habilitado, ele utiliza o local selecionado nas preferências da empresa, aba **"Estoque/Preço"** (Caminho de acesso: Comercial » Preferências » Empresa):

![Imagem 3: Caso este parâmetro esteja habilitado, ele utiliza o local selecionado nas preferências da empresa, aba "Estoque/Preço"…](https://ajuda.sankhya.com.br/hc/article_attachments/14660704825879)

![Imagem 4: Caso nenhum destes estejam indicando um valor de local e o produto não tenha controle por código de barras, o FAST ao…](https://ajuda.sankhya.com.br/hc/article_attachments/16831592159127) Caso nenhum destes estejam indicando um valor de local e o produto não tenha controle por código de barras, o FAST ao inserir um produto na tela de cupons irá solicitar a inserção de um local para baixa de estoque.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16831618523287) OBSERVAÇÃO:**

**(2)** Caso o parâmetro "**REPETELOCALANT**" esteja habilitado, o sistema irá utilizar o último local digitado na imagem acima. Ou seja, a funcionalidade do parâmetro é repetir o último local digitado para o próximo produto lançado;

**(2)** Quando o produto tem controle por local, porém as configurações para o uso do local padrão do cadastro do produto ou empresa não estão devidamente configurados, o Fast Service não preenche de forma automática o local no lançamento do item no cupom;

**(2)** Exceção a regra, o sistema não olha o campo **"Local"**, do cadastro do produto, quando a venda for pelo Fast Service.
