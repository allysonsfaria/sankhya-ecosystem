---
id: "9408281989271"
titulo: "Campo OPERACAOCTF não configurado para o tipo de título"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9408281989271-Campo-OPERACAOCTF-n%C3%A3o-configurado-para-o-tipo-de-t%C3%ADtulo"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T15:07:55Z"
rotulos: ["Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "Tipos de Título", "CORE_E05658", "Campo OPERACAOCTF não configurado", "Tipo de título sem Operação CTF definida", "Habilite \"USARECEBCARTCTF\" e configure \"Operação CTF\""]
---

# Campo OPERACAOCTF não configurado para o tipo de título

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16703298041239) MENSAGEM:**

[CORE\_E05658]: Campo OPERACAOCTF não configurado para o tipo de título.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16703298046231) SITUAÇÃO:**

Ao tentar receber a venda no cartão de crédito ou débito a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16703304252183) SOLUÇÃO:**

![Imagem 4: Habilite o parâmetro "USARECEBCARTCTF" na tela "Preferências" (Caminho de acesso: Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/16703298050455) Habilite o parâmetro **"USARECEBCARTCTF"** na tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências).

![Imagem 5: Habilite o parâmetro "USARECEBCARTCTF" na tela "Preferências" (Caminho de acesso: Configurações » Avançado »…](https://ajuda.sankhya.com.br/hc/article_attachments/9408131000087)

![Imagem 6: Feito isso, acesse o cadastro do "Tipo de título" (Financeiro » Arquivos » Cadastros » Tipos de Título) utilizado no…](https://ajuda.sankhya.com.br/hc/article_attachments/16703298054423) Feito isso, acesse o cadastro do **"Tipo de título"** (Financeiro » Arquivos » Cadastros » Tipos de Título) utilizado no lançamento e configure corretamente o campo **"Operação CTF"**, na aba **"Preferências de cartão"** com a operação primordial a ser realizada pelo CTF, dentre as seguintes opções:

- Créd. a vista;
- Créd. Parcelado Lojista (sem juros);
- Créd. Parcelado Administradora (com juros);
- Débito;
- Voucher.

![Imagem 7: Voucher.](https://ajuda.sankhya.com.br/hc/article_attachments/16703298057751)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16703304265111) CAUSA:**

Ao realizar o recebimento de uma venda e o tipo de título não esteja com a Operação CTF definida.
