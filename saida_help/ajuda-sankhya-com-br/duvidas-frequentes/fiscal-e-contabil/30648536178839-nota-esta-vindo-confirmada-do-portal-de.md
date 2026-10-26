---
id: "30648536178839"
titulo: "Nota está vindo confirmada do portal de importação de xml, veja o que fazer"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30648536178839-Nota-est%C3%A1-vindo-confirmada-do-portal-de-importa%C3%A7%C3%A3o-de-xml-veja-o-que-fazer"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:35:09Z"
rotulos: ["Configuração", "Empresa", "NF-e", "XML", "Importação", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Nota está vindo confirmada do portal de importação de xml"]
---

# Nota está vindo confirmada do portal de importação de xml, veja o que fazer

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30655654733335) **SITUAÇÃO:**

Ao importar uma nota pelo portal de importação de xml e clicar em abrir a nota a mesma está indo confirmada para a central de Compras.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30648536171671)SOLUÇÃO:**

Acesse a tela **"Empresa"** (Comercial » Preferências), vá até a aba **"Modelo de Importação de XML"** e verifique qual destes Modelo de notas e pedidos possuem a TOP da nota em questão. Para isso, acesse a tela **"Modelo de notas e pedidos"**e verifique o campo **"Tipo de operação".**

Depois, uma vez que identificar esse modelo, ainda na tela de Modelo de notas e pedidos, verifique agora o campo  **"Confirmada".** Se estiver marcado como **"Sim",** a nota será confirmada automaticamente na importação do xml. Nesse caso, entre em contato com o Service desk para analisar o motivo desse campo estar definido como Sim. Pois, isso ocorre quando o STATUSNOTA da tgfcab está como 'L'.

![Imagem 3: Depois, uma vez que identificar esse modelo, ainda na tela de Modelo de notas e pedidos, verifique agora o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/30656877197847)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30648536172567)CAUSA:**

Quando o modelo de Nota e pedidos está com o STATUSNOTA está igual a 'L', para o modelo de notas

esse campo deve estar igual a 'P'
