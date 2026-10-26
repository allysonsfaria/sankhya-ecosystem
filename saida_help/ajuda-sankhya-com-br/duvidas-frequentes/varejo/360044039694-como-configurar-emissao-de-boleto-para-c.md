---
id: "360044039694"
titulo: "Como configurar emissão de Boleto para Cupom fiscal no Fast Service?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044039694-Como-configurar-emiss%C3%A3o-de-Boleto-para-Cupom-fiscal-no-Fast-Service"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:55:48Z"
rotulos: ["Configuração", "Impressão", "Fast Service", "Portal de Vendas", "Boleto", "Financeiro", "Configurar modelo de boleto", "Configurar boleto para cupom fiscal no Fast Service"]
---

# Como configurar emissão de Boleto para Cupom fiscal no Fast Service?

**(1)** Considere o comportamento da aplicação, conforme abaixo:

![Imagem 1: Acesse: Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/article_attachments/16831525001367) Acesse: Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)

Crie um modelo, para impressão do Boleto.

Caso utilize um modelo 'jrxml', crie um modelo antes em: Financeiro » Relatórios » Modelos de Boleto(s).

Utilize um modelo de boleto padrão ou personalize: baixe o modelo padrão através do botão **"Baixar Modelo Padrão"** e vincule este modelo, no **"Modelos de Nota Fiscal/Duplicatas/Boleto(s)"**.

![Imagem 2: Utilize um modelo de boleto padrão ou personalize: baixe o modelo padrão através do botão "Baixar Modelo Padrão" e…](https://ajuda.sankhya.com.br/hc/article_attachments/14660791283223)

![Imagem 3: Utilize um modelo de boleto padrão ou personalize: baixe o modelo padrão através do botão "Baixar Modelo Padrão" e…](https://ajuda.sankhya.com.br/hc/article_attachments/14660804718103)

![Imagem 4: Acesse: Configurações » Cadastros » Bancários » Contas](https://ajuda.sankhya.com.br/hc/article_attachments/16831525003031)  Acesse: Configurações » Cadastros » Bancários » Contas

Aba: **"Boleto(s)/Duplicatas"**

Crie ou utilize a Conta Bancária, que emite Boleto, e vincule o modelo criado anteriormente no campo **"Modelo"** e marque a opção que **"Emite"** boleto.

![Imagem 5: Crie ou utilize a Conta Bancária, que emite Boleto, e vincule o modelo criado anteriormente no campo "Modelo" e marque…](https://ajuda.sankhya.com.br/hc/article_attachments/14660829287063)

![Imagem 6: Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título](https://ajuda.sankhya.com.br/hc/article_attachments/16831539962775) Acesse: Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título

Aba: **"Fast Service"**

Crie um Tipo de Título, com o Subtipo: a prazo e marque a opção **"Utiliza no Fast Service"**.

![Imagem 7: Crie um Tipo de Título, com o Subtipo: a prazo e marque a opção "Utiliza no Fast Service" .](https://ajuda.sankhya.com.br/hc/article_attachments/14660836462615)

![Imagem 8: Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/16831539963927) Acesse: Comercial » Arquivo » Cadastros » Tipos de Negociação

Crie ou utilize um Tipo de Negociação, com o Subtipo: a Prazo e na aba: **"Parcelas"**, vincule a Conta Bancaria e o Tipo de Títulos, configurados anteriormente.

Após feito isso, o cliente deverá cadastrar um tipo de titulo a prazo e marcar a opção que o mesmo poderá ser utilizado no Fast Service. Tela: Arquivos » Cadastro » Tipos de Titulo.

![Imagem 9: Após feito isso, o cliente deverá cadastrar um tipo de titulo a prazo e marcar a opção que o mesmo poderá ser utilizado…](https://ajuda.sankhya.com.br/hc/article_attachments/14660908891287)

![Imagem 10: Acesse: Comercial » Consulta » Portal de Vendas](https://ajuda.sankhya.com.br/hc/article_attachments/16831539964951) Acesse: Comercial » Consulta » Portal de Vendas

Depois de ter feito estas configurações, lance o cupom no FAST Service (visualizar o mesmo na retaguarda no Portal de Vendas), selecione o Cupom Fiscal e clique no botão de **"Impressão"** (Ctrl+Shift+I), em seguida, em **"Imprimir Boleto"**.
