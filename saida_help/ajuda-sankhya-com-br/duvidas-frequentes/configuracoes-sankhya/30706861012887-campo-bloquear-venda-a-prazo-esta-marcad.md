---
id: "30706861012887"
titulo: "Campo \"Bloquear venda a prazo\" está marcado como valor padrão \"marcado\", mas a configuração não está sendo atribuída aos demais usuários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30706861012887-Campo-Bloquear-venda-a-prazo-est%C3%A1-marcado-como-valor-padr%C3%A3o-marcado-mas-a-configura%C3%A7%C3%A3o-n%C3%A3o-est%C3%A1-sendo-atribu%C3%ADda-aos-demais-usu%C3%A1rios"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:34:56Z"
rotulos: ["Configuração", "Parceiro", "Bloquear venda a prazo", "valor padrão \"marcado\"", "usuários acessam a tela e o campo ainda está \"desmarcado\"", "Erro", "Venda a Prazo"]
---

# Campo "Bloquear venda a prazo" está marcado como valor padrão "marcado", mas a configuração não está sendo atribuída aos demais usuários

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30706846225431) **SITUAÇÃO:**

Após configurar no layout do cadastro do parceiro o campo **"Bloquear venda a prazo"** como valor padrão "marcado", os usuários acessam a tela e o campo ainda está "desmarcado".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30706861009431)SOLUÇÃO:**

Acesse a tela **"Parceiros"** - com o usuário em que a marcação está apresentando desmarcada - e restaure a configuração da tela. Assim, ela será apresentada com as configurações realizadas com o usuário SUP.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30706846228375)CAUSA:**

Quando o usuário possui acesso à configuração na tela **Parceiros** e faz alguma alteração em default de campo, ou qualquer outra alteração na configuração da tela, o sistema gera uma linha na TSICFG para a chave 'br.com.sankhya.core.cad.parceiros'. Dessa forma, o sistema deixa de olhar para a configuração do usuário SUP. Para que o default de campos definidos pelo usuário SUP seja utilizado pelos demais usuários, é necessário restaurar a configuração do usuário e tirar o acesso de configuração para que não seja alterado.
