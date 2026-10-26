---
id: "360043734154"
titulo: "Solução do erro: Quantidade da tarefa está fragmentada. Tarefa=X, Seq=Y, Prod=ZZZ, Qtd.orig=999,9, Qtd.dest=999,9"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043734154-Solu%C3%A7%C3%A3o-do-erro-Quantidade-da-tarefa-est%C3%A1-fragmentada-Tarefa-X-Seq-Y-Prod-ZZZ-Qtd-orig-999-9-Qtd-dest-999-9"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T15:59:14Z"
rotulos: ["#criadoRoger", "Produtos", "Configuração", "WMS", "Estoque", "Preferências", "Correção de Erro: Quantidade Fragmentada na Tarefa", "Erro"]
---

# Solução do erro: Quantidade da tarefa está fragmentada. Tarefa=X, Seq=Y, Prod=ZZZ, Qtd.orig=999,9, Qtd.dest=999,9

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16305888331415) MENSAGEM**:

[SQL-50001]: Quantidade da tarefa está fragmentada. Tarefa=X, Seq=Y, Prod=ZZZ, Qtd.orig=999,9, Qtd.dest=999,9

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16305888334231) SOLUÇÃO**:

Para correção siga os passos abaixo:

![Imagem 3: Acesse Comercial » Preferências » Empresa , aba WMS e marque a opção "Permitir estoque fragmentado" ;](https://ajuda.sankhya.com.br/hc/article_attachments/16305888337559) Acesse Comercial » Preferências » Empresa, aba **WMS** e marque a opção **"Permitir estoque fragmentado"**;

![Imagem 4: Acesse Configurações » Avançado » Preferências e ligue o parâmetro "FRAGMENTAESTWMS" ;](https://ajuda.sankhya.com.br/hc/article_attachments/16305888339351) Acesse Configurações » Avançado » Preferências e ligue o parâmetro **"FRAGMENTAESTWMS"**;

![Imagem 5: Acesse WMS » Cadastros » Endereço de Armazenamento e marque o campo "Permite Fragmentar Estoque" .](https://ajuda.sankhya.com.br/hc/article_attachments/16305859449367) Acesse WMS » Cadastros » Endereço de Armazenamento e marque o campo **"Permite Fragmentar Estoque"**.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16305888346903) CAUSA**:

Quando o produto permite separação fragmentada, trabalha com unidade que permite fragmentação e os parâmetros e marcações não estão habilitados.
