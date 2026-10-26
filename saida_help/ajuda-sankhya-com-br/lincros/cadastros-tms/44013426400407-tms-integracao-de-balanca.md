---
id: "44013426400407"
titulo: "[TMS] - Integração de Balança"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013426400407--TMS-Integra%C3%A7%C3%A3o-de-Balan%C3%A7a"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:56:42Z"
rotulos: ["sync_hc", "lincros", "sync_hash_646132173f43", "lincros_13432558"]
---

# [TMS] - Integração de Balança

**Menu**: Cadastros gerais > Portaria > Balança > Integrador de balança

**Objetivo**: Como realizar o cadastro para a integração de uma balança.

**Considerações**:

- Possuir acesso ao menu: Cadastros gerais > Portaria > Balança > Integrador de balança;
- Necessário ter a balança cadastrada;
- Vincular o integrador no cadastro da portaria;
- Recomendado utilizar autenticação via token;
- Para a Lincros conseguir realizar a leitura do peso da balança na operação de portaria, é necessário que o cliente crie um integrador que siga os padrões do Integrador NBW.

## Abaixo segue os procedimentos

1. Para cadastrar o integrador de balança, basta acessar o menu: Cadastros gerais > Portaria > Balança > Integrador de balança e clicar em 'Novo';

   ![Imagem 1: Para cadastrar o integrador de balança, basta acessar o menu: Cadastros gerais > Portaria > Balança > Integrador de…](https://ajuda.sankhya.com.br/hc/article_attachments/44013395151895)
2. Após clicar em 'Novo', necessário preencher todos os campos:

- **Nome**: Preencher com o nome desejado para identificação;
- **Provider**: com.transpobrasil.balanca.facade.IntegradorBalancaNBWProvider;
- **URL**:  Informar a URL criada no integrador ex: https://tmsbalanca.nomecliente.com.br;
- **Tipo de Autenticação**: Informar o método de autenticação utilizada no integrador;

- Usuário/senha: usuário e senha enviado no header da chamada do integrador.
- Token: enviado no header da chamada do integrador, o campo 'tk' (valor fixo no cadastro)

  ![Imagem 2: Token : enviado no header da chamada do integrador, o campo 'tk' (valor fixo no cadastro)](https://ajuda.sankhya.com.br/hc/article_attachments/44013412238871)

3. Ao preencher todos os campos necessários, basta clicar em 'Salvar'.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
