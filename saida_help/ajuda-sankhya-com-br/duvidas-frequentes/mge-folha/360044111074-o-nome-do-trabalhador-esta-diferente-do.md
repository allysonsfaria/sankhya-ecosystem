---
id: "360044111074"
titulo: "O Nome do Trabalhador está diferente do valor encontrado no Sistema da RFB"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044111074-O-Nome-do-Trabalhador-est%C3%A1-diferente-do-valor-encontrado-no-Sistema-da-RFB"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:32:39Z"
rotulos: ["#criadoRoger", "#RevisadoLorrana", "Funcionários", "RFB", "eSocial", "175", "Central do eSocial", "Cadastro", "Nome do Trabalhador Divergente com RFB", "Erro"]
---

# O Nome do Trabalhador está diferente do valor encontrado no Sistema da RFB

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16426186743959) MENSAGEM:**

[Erro 175] - O Nome do Trabalhador está diferente do valor encontrado no Sistema da RFB. Valor no Sistema = FULANO DE TAL.
Ação Sugerida: Procure unidade conveniada da RFB e efetue a regularização.
Elemento: /eSocial/evtAltCadastral/alteracao/dadosTrabalhador/nmTrab

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16426164575511) SITUAÇÃO:**

Ao tentar transmitir o evento S-2200/S-2205 para o eSocial apresenta a rejeição.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16426164578583) SOLUÇÃO:**

![Imagem 4: Realize uma consulta no site da receita federal. Clique Aqui](https://ajuda.sankhya.com.br/hc/article_attachments/16426186754199)Realize uma consulta no site da receita federal. [**Clique Aqui**](http://cpf.receita.fazenda.gov.br/situacao/default.asp)

![Imagem 5: Informe os dados do Funcionário (CPF e Data de Nascimento) e clique em " Não sou um Robô".](https://ajuda.sankhya.com.br/hc/article_attachments/16426186755863) Informe os dados do Funcionário (CPF e Data de Nascimento) e clique em "**Não sou um Robô".**

![Imagem 6: Será apresentada uma validação do site. Realize a mesma.](https://ajuda.sankhya.com.br/hc/article_attachments/16426186762007) Será apresentada uma validação do site. Realize a mesma.

![Imagem 7: Após realizar o preenchimento e a validação, clique em "Consultar".](https://ajuda.sankhya.com.br/hc/article_attachments/16426186765975) Após realizar o preenchimento e a validação, clique em **"Consultar".**

![Imagem 8: Serão apresentados os dados do Funcionário. Verifique como está preenchido o nome.](https://ajuda.sankhya.com.br/hc/article_attachments/16426164594199) Serão apresentados os dados do Funcionário. Verifique como está preenchido o nome.

![Imagem 9: Acesse MGEPessoal » Funcionários e efetue o ajuste do nome do Funcionário de acordo com o site da RFB-Receita Federal.](https://ajuda.sankhya.com.br/hc/article_attachments/16426186773271) Acesse MGEPessoal » Funcionários e efetue o ajuste do nome do Funcionário de acordo com o site da RFB-Receita Federal.

![Imagem 10: Salve o Registro.](https://ajuda.sankhya.com.br/hc/article_attachments/16426186775447) Salve o Registro.

![Imagem 11: Acesse MGEPessoal » Avançado » Central do eSocial e transmita novamente as obrigações.](https://ajuda.sankhya.com.br/hc/article_attachments/16426186777751) Acesse MGEPessoal » Avançado » Central do eSocial e transmita novamente as obrigações.

**![Imagem 12: OBSERVAÇÃO: Se o nome do Funcionário estiver incorreto no site da Receita, oriente o funcionário a procurar o órgão e…](https://ajuda.sankhya.com.br/hc/article_attachments/16426164606103) OBSERVAÇÃO:** Se o nome do Funcionário estiver incorreto no site da Receita, oriente o funcionário a procurar o órgão e efetuar a regularização.

**![Imagem 13: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16426186782359) CAUSA:**

Essa mensagem de erro de validação ocorre no retorno do Evento S-2200/S-2205 quando o nome do trabalhador está com alguma diferença entre o cadastro do sistema e o cadastro da RFB (Receita Federal do Brasil).
