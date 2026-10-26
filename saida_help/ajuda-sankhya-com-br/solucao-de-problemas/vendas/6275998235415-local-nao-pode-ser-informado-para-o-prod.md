---
id: "6275998235415"
titulo: "Local não pode ser informado para o produto "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/6275998235415-Local-n%C3%A3o-pode-ser-informado-para-o-produto"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-16T15:26:23Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Estoque", "#publifercausaraiz", "CORE_E00776", "Local não aplicável ao produto", "Configuração de local padrão para produtos sem controle de local", "Marque 'Usa Local' no cadastro do produto se necessário", "Erro"]
---

# Local não pode ser informado para o produto 

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16430195614231) MENSAGEM:**

[CORE\_E00776] Local não pode ser informado para o produto.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16430212276119) SOLUÇÃO:**

![Imagem 3: Certifique se os produtos lançados na nota devem possuir controle por local.](https://ajuda.sankhya.com.br/hc/article_attachments/16430212277143) Certifique se os produtos lançados na nota **devem possuir controle por local.**

Em caso positivo, acesse o cadastro do respectivo produto (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) e marque a opção 'Usa local':

- Aba: **"Medidas e estoque"**
- Sub-aba: **"Estoque"**
- Marcação: **"Usa Local"**

Em seguida, refaça o lançamento/faturamento.

![Imagem 4: Caso o produto não seja controlado por local, o campo "Local" do lançamento deverá estar em branco .](https://ajuda.sankhya.com.br/hc/article_attachments/16430195619479) Caso o **produto não seja controlado por local, o campo "Local" do lançamento deverá estar em branco**.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16430212283543)CAUSA:**

Quando, por alguma configuração de 'Local Padrão', o sistema está sugerindo local para determinado item e esse não possui a marcação **"Usa Local"**.
