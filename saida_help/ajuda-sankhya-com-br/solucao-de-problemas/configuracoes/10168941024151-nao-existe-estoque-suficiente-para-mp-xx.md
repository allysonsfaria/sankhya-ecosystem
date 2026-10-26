---
id: "10168941024151"
titulo: "Não existe estoque suficiente para MP XXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10168941024151-N%C3%A3o-existe-estoque-suficiente-para-MP-XXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:22Z"
rotulos: ["Produtos", "Configuração", "Estoque", "Preferências", "CORE_E01247", "Estoque Insuficiente: MP XXX", "Erro"]
---

# Não existe estoque suficiente para MP XXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19276807689879) MENSAGEM:**

[CORE\_E01247] Não existe estoque suficiente para MP XXX.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19276830776087) SITUAÇÃO:**

Ao inserir um item que é kit no pedido a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19276807692055) SOLUÇÃO:**

Quando o item que é kit é inserido no pedido, o sistema tenta localizar o local onde o mesmo se encontra.

Assim, primeiro verifique se os 'componentes' possuem  o campo "CODLOCALMP"  preenchido.

Vale destacar que,  para que consiga informar o "Controle" nos componentes, o parâmetro **'Mostrar o controle da aba de componentes - CONTROLECOMPON',** na tela **Preferências** (Configurações » Avançado » Preferências), deve estar ligado. Desse modo, observe se o parâmetro está em conformidade.

![Imagem 4: Vale destacar que, para que consiga informar o "Controle" nos componentes, o parâmetro 'Mostrar o controle da aba de…](https://ajuda.sankhya.com.br/hc/article_attachments/19276807698327)

Após habilitar o parâmetro acima (caso ele esteja desligado), acesse o cadastro de **Produtos** (Caminho de acesso à tela: Configurações » Cadastros » Produtos » Produtos), vá até a aba 'Componentes' e informe o local para o componente.

![Imagem 5: Após habilitar o parâmetro acima (caso ele esteja desligado), acesse o cadastro de Produtos (Caminho de acesso à tela:…](https://ajuda.sankhya.com.br/hc/article_attachments/19276807698967)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19276830776727) CAUSA:**

Ocorre quando o componente está sem local definido ("Local" do componente está igual à 0).
