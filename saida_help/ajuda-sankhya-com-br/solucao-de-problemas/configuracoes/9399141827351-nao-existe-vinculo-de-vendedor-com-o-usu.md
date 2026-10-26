---
id: "9399141827351"
titulo: "Não existe vínculo de vendedor com o usuário logado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9399141827351-N%C3%A3o-existe-v%C3%ADnculo-de-vendedor-com-o-usu%C3%A1rio-logado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:08Z"
rotulos: ["Configuração", "Portal de Vendas", "Usuário", "Vendedor", "CORE_E02037", "SVC_E00242", "Falha de Vínculo de Vendedor", "Erro"]
---

# Não existe vínculo de vendedor com o usuário logado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18603188019863) MENSAGEM:**

[CORE\_E02037]  Não existe vínculo de vendedor com o usuário logado.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603172394775) SITUAÇÃO:**

Ao tentar visualizar os pedidos no portal de vendas a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18603172402839) CAUSA:**

Não possuir vendedor informado no cadastro do usuário e opção Ver pedidos/notas (web): 'Do Vendedor' marcada.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18603188066199) SOLUÇÃO:**

![Imagem 5: Verifique no cadastro do usuário (Configurações » Controle de Acesso » Usuários) se o campo vendedor está preenchido,…](https://ajuda.sankhya.com.br/hc/article_attachments/18603172412695) Verifique no cadastro do **usuário** (Configurações » Controle de Acesso » Usuários) se o campo vendedor está preenchido, caso não esteja basta informar um vendedor para esse usuário.

![Imagem 6: Verifique no cadastro do usuário (Configurações » Controle de Acesso » Usuários) se o campo vendedor está preenchido,…](https://ajuda.sankhya.com.br/hc/article_attachments/18603188075927)

![Imagem 7: Ver na Configuração da aba Segurança no Cadastro deste usuário, campo: Ver pedidos/notas (web) : Se estiver como 'Do…](https://ajuda.sankhya.com.br/hc/article_attachments/18603188087575) Ver na Configuração da aba Segurança no Cadastro deste usuário, campo: **Ver pedidos/notas (web)**: Se estiver como 'Do Vendedor' é preciso que exista um vendedor vinculado ao usuário logado. Caso queria visualizar os lançamentos de todos vendedores, deverá modificar a opção para 'De todos'.
