---
id: "27575963532951"
titulo: "Sistema não está bloqueando lançar unidade alternativa nos itens mesmo estando inativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27575963532951-Sistema-n%C3%A3o-est%C3%A1-bloqueando-lan%C3%A7ar-unidade-alternativa-nos-itens-mesmo-estando-inativo"
trilha: "Dúvidas Frequentes > Compras e Estoque"
atualizado_em: "2026-07-22T14:39:32Z"
rotulos: ["Produtos", "Configuração", "XML", "Estoque", "Preferências", "Passos para resolver", "Razão do erro", "Detalhe do erro", "unidade alternativa", "VALCODVOLATIVO"]
---

# Sistema não está bloqueando lançar unidade alternativa nos itens mesmo estando inativo

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27631571634071) **SITUAÇÃO:**

Sistema não está bloqueando o lançamento de unidade alternativa nos itens, mesmo estando com o campo **"Ativo"** (Configurações » Cadastros » Produtos » Produtos) **desabilitado.**

![Imagem 2: Sistema não está bloqueando o lançamento de unidade alternativa nos itens, mesmo estando com o campo "Ativo"…](https://ajuda.sankhya.com.br/hc/article_attachments/27631566519319)

![Imagem 3: Sistema não está bloqueando o lançamento de unidade alternativa nos itens, mesmo estando com o campo "Ativo"…](https://ajuda.sankhya.com.br/hc/article_attachments/27575963494679)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/27575963150615)SOLUÇÃO:**

Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e habilite o parâmetro **"VALCODVOLATIVO"**.

Esse parâmetro tem as opções:

- Não Valida
- Valida Volume
- Valida Volume e Controle

![Imagem 5: Valida Volume e Controle](https://ajuda.sankhya.com.br/hc/article_attachments/27575963156503)

Configurando o parâmetro para uma das validações, o sistema não vai permitir o lançamento conforme abaixo.

![Imagem 6: Configurando o parâmetro para uma das validações, o sistema não vai permitir o lançamento conforme abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/27576694068887)

**Observação:** para que o sistema não considere uma unidade alternativa inativa em notas importadas por XML, além de configurar o parâmetro VALCODVOLATIVO, é necessário ajustar o campo **"Unidade"** no cadastro do produto, na aba [Produtos Equivalentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos#abaprodutosequivalentes). Esse campo deve ser preenchido com a unidade desejada para exibição nas centrais, garantindo que seja diferente da unidade alternativa inativa.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/27575963165847)CAUSA:**

O campo Ativo funciona junto com o parâmetro VALCODVOLATIVO. Caso o parâmetro esteja como Não Valida, o sistema vai deixar salvar o item mesmo quando a opção de Ativo estiver desabilitada.  Vale destacar que, o campo Ativo foi herdado do Mitra e para o funcionamento correto e seguro no SankhyaW  foi criando o parâmetro.
