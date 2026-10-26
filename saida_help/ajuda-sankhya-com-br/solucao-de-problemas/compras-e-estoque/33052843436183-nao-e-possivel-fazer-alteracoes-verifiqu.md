---
id: "33052843436183"
titulo: "Não é possível fazer alterações. Verifique as permissões de acesso. - Matriz de Analise de Giro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33052843436183-N%C3%A3o-%C3%A9-poss%C3%ADvel-fazer-altera%C3%A7%C3%B5es-Verifique-as-permiss%C3%B5es-de-acesso-Matriz-de-Analise-de-Giro"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:29:47Z"
rotulos: ["Configuração", "Segurança", "Análise de Giro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Analise de giro", "CONTACESSMAT", "verifique as permissões de acesso", "matriz de analise de giro", "Erro", "Permissão de Acesso"]
---

# Não é possível fazer alterações. Verifique as permissões de acesso. - Matriz de Analise de Giro

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33052855288599) **MENSAGEM:**

Não é possível fazer alterações. Verifique as permissões de acesso.

**SITUAÇÃO:**

Ao tentar **alterar uma matriz de Análise de Giro**, mesmo com o login de um usuário que possui todos os acessos liberados via tela de acessos, a mensagem de erro é apresentada, impedindo a edição.

Essa situação costuma gerar dúvidas, pois o erro ocorre mesmo quando os acessos tradicionais já foram concedidos via grupos e permissões usuais.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33052843431959)SOLUÇÃO:**

Para que o usuário consiga editar a matriz desejada, siga os passos abaixo:

**(1)** Acesse a rotina **Análise de Giro (Comercial > Rotinas);**

**(2)** Selecione a matriz em questão;

**(3)** Clique no botão **“Segurança”;**

**(4)** No pop-up exibido, localize o usuário que precisa de acesso;

**(5)** Marque as permissões desejadas (visualizar, editar, excluir, etc.);

**(6)** Salve as alterações.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33052855291927)CAUSA:**

Quando o parâmetro **"Controla acesso por matriz de análise de giro? - CONTACESSMAT"** está ativado, o sistema passa a utilizar uma **camada adicional de segurança específica para a Matriz de Análise de Giro**, controlada por meio da aba **Segurança** dentro da própria rotina.

Essa configuração permite definir permissões por **usuário e grupo** diretamente para cada matriz individual, de forma independente das permissões gerais de acesso do sistema.
