---
id: "11061831662615"
titulo: "O registro de \"Conta Bancária\" (TSICTA) selecionado não está cadastrado, ou não está ativo, ou não é analítico, saiba como proceder"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11061831662615-O-registro-de-Conta-Banc%C3%A1ria-TSICTA-selecionado-n%C3%A3o-est%C3%A1-cadastrado-ou-n%C3%A3o-est%C3%A1-ativo-ou-n%C3%A3o-%C3%A9-anal%C3%ADtico-saiba-como-proceder"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:02:13Z"
rotulos: ["Configuração", "Contas", "Financeiro", "Mensagem: Conta Bancária não cadastrada ou ativa", "Verifique configurações CNAB e validação bancária", "Corrija posições do layout e variáveis na configuração", "Erro", "EDI Bancário"]
---

# O registro de "Conta Bancária" (TSICTA) selecionado não está cadastrado, ou não está ativo, ou não é analítico, saiba como proceder

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16418233206551) MENSAGEM:**

O registro de "Conta Bancária" (TSICTA) selecionado não está cadastrado, ou não está ativo, ou não é analítico

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418268808855) SITUAÇÃO:**

Ao processar o arquivo de retorno a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16418233211415)SOLUÇÃO:**

Sempre que estiver validando as configurações CNAB é importante que os cadastros sejam feitos e validados junto ao banco antes da utilização.

Normalmente esse erro é apresentado pois as posições definidas no layout de retorno não batem com o cadastro da conta bancária. As posições são definidas na tela **"Configuração Arquivo de Retorno"** (Caminho de acesso à tela: Financeiro » EDI Bancário » Configuração Arquivo de Retorno).

![Imagem 4: Normalmente esse erro é apresentado pois as posições definidas no layout de retorno não batem com o cadastro da conta…](https://ajuda.sankhya.com.br/hc/article_attachments/14550258965783)

Outra configuração que deverá ser verificada são das variáveis:

![Imagem 5: Outra configuração que deverá ser verificada são das variáveis:](https://ajuda.sankhya.com.br/hc/article_attachments/14550242455191)

O correto é que fique dessa forma:

![Imagem 6: O correto é que fique dessa forma:](https://ajuda.sankhya.com.br/hc/article_attachments/14550242453783)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16418268814103) CAUSA:**

Ocorre quando as posições definidas no layout de retorno não batem com o cadastro da conta bancária.
