---
id: "33643947375383"
titulo: "Como desabilitar a engrenagem de configurações para determinados usuários ou grupos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33643947375383-Como-desabilitar-a-engrenagem-de-configura%C3%A7%C3%B5es-para-determinados-usu%C3%A1rios-ou-grupos"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-10-06T17:44:11Z"
rotulos: ["Configuração", "Usuários", "Segurança", "Preferências", "Controle de Acesso", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Desabilitar a engrenagem", "UTLCGFACCESSGRD", "Engrenagem de configurações", "Squad Plataforma"]
---

# Como desabilitar a engrenagem de configurações para determinados usuários ou grupos?

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33643913111063)SOLUÇÃO:**

#### Configuração de permissões de acesso

**(1)** Acesse a tela [**''Acessos''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) (Configurações » Controle de Acesso » Acessos).

**(2)** Localize a rotina ou o módulo desejado.

**(3)** Selecione o usuário ou grupo para configurar.

**(4)** Desmarque a opção **''Configurar''** para impedir que o usuário altere a grade.

**Exemplo Portal de Compras:**

![Imagem 2: Exemplo Portal de Compras:](https://ajuda.sankhya.com.br/hc/article_attachments/36756174525975)

#### Habilitar parâmetro de controle

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''** busque pelo parâmetro **"UTLCGFACCESSGRD"**.

**(3)** No campo **''Ligado/Desligado''** altere para **''Ligado''**.

Assim, o sistema passa a respeitar as permissões de acesso definidas para a configuração da grade.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33643913112087)CAUSA:**

O acesso à engrenagem de configuração da grade permite que os usuários alterem a forma como as telas são exibidas. Quando essa personalização não é desejada, seja para manter um padrão ou evitar mudanças indevidas, é necessário restringir essa permissão.
