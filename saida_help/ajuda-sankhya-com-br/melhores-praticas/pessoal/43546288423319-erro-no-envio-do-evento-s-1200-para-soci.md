---
id: "43546288423319"
titulo: "Erro no envio do evento S-1200 para sócio categoria 722 - Grupo 'Informações complementares contratuais do trabalhador' deve ser preenchido e matrícula ou categoria '722' informada deve ser igual a existente no cadastro do trabalhador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546288423319-Erro-no-envio-do-evento-S-1200-para-s%C3%B3cio-categoria-722-Grupo-Informa%C3%A7%C3%B5es-complementares-contratuais-do-trabalhador-deve-ser-preenchido-e-matr%C3%ADcula-ou-categoria-722-informada-deve-ser-igual-a-existente-no-cadastro-do-trabalhador"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-06T11:47:50Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro no envio do evento S-1200 para sócio categoria 722 - Grupo 'Informações complementares contratuais do trabalhador' deve ser preenchido e matrícula ou categoria '722' informada deve ser igual a existente no cadastro do trabalhador

**MENSAGEM**

[312] A matrícula 'xxxx' ou categoria 'xxx' informada deve ser igual à existente no cadastro do trabalhador no Ambiente Nacional do eSocial. Grupo 'Informações complementares contratuais do trabalhador' deve ser preenchido.

**SITUAÇÃO**

O erro ocorre ao tentar enviar o evento S-1200 para um trabalhador classificado como sócio/pro-laborista (categoria 722) no eSocial. O sistema retorna a mensagem de que a matrícula ou categoria informada não corresponde ao cadastro do trabalhador no Ambiente Nacional do eSocial, impedindo a transmissão do evento de remuneração.

**SOLUÇÃO**

**(1)** Acesse o cadastro do trabalhador na tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários) e verifique se os campos **"Matrícula"**, **"Matrícula Alternativa"** e **"Categoria para o eSocial"** estão preenchidos corretamente e de acordo com as informações enviadas anteriormente ao eSocial.

**(2)** Acesse o **Portal do eSocial**, localize o trabalhador e confira qual **matrícula** e **categoria** estão cadastradas para ele.

É importante que tanto a matrícula quanto a categoria informadas no sistema sejam as mesmas que constam no eSocial, garantindo a correta identificação do trabalhador.

**(3)** Caso a matrícula esteja diferente da informação apresentada no eSocial, informe a matrícula correta no sistema, utilizando o campo **"Matrícula"** ou **"Matrícula Alternativa"**, conforme o cenário.

**(4)** Em seguida, gere e transmita novamente o evento S-1200 para o sócio/pro-laborista.

**(1)** **Atenção:** Caso o trabalhador não seja localizado no eSocial, será necessário realizar a geração e o envio do evento de admissão **S-2200 ou S-2300**, conforme o tipo de trabalhador, para que seu cadastro seja incluído no eSocial.

Se, mesmo após o envio, o erro continuar sendo apresentado, isso indica que a **matrícula informada já está sendo utilizada por outro trabalhador no eSocial**. Nesse caso, altere a matrícula do trabalhador no sistema para uma matrícula que não esteja sendo utilizada e, em seguida, realize novamente o envio do evento.

**CAUSA**

O erro é causado quando a matrícula ou a categoria informada no evento S-1200 não corresponde ao que está cadastrado no eSocial para o trabalhador, ou quando a matrícula já foi utilizada por outro colaborador. Também pode ocorrer se o grupo "Informações complementares contratuais do trabalhador" não for preenchido corretamente para a categoria 722 (diretor não empregado/pro-laborista), conforme exigência do eSocial.
