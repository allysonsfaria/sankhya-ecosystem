---
id: "4403372081559"
titulo: "O campo \"Vendedor\" da nota não está puxando o vendedor logado ao duplicar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403372081559-O-campo-Vendedor-da-nota-n%C3%A3o-est%C3%A1-puxando-o-vendedor-logado-ao-duplicar"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:23:57Z"
rotulos: ["Configuração", "Central de Vendas", "Portal de Vendas", "Vendedor", "não apagar", "Duplicação", "Inconsistência do Campo “Vendedor” ao Duplicar Nota"]
---

# O campo "Vendedor" da nota não está puxando o vendedor logado ao duplicar

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16343858375319) SITUAÇÃO:**

Pela tela **"Configurador de Layout da Nota"** é possível configurar o campo **"Vendedor"** para ser preenchido com um valor padrão de forma automática ao iniciar um lançamento. Configurando para buscar o vendedor do usuário logado, caso o usuário tenha um código de vendedor vinculado no seu cadastro, este será utilizado, conforme print:

![Imagem 2: Pela tela "Configurador de Layout da Nota" é possível configurar o campo "Vendedor" para ser preenchido com um valor…](https://ajuda.sankhya.com.br/hc/article_attachments/15081315201943)

No entanto, **ao duplicar um lançamento o valor do campo será o mesmo do documento duplicado**, pois a rotina de duplicação do Portal de Vendas faz uma cópia do documento original, não aplicando as regras para novo documento que são seguidas na Central de Vendas. Além disso, no Portal ainda não existe o layout que será utilizado para o lançamento do documento, não sendo possível verificar a informação que o vendedor deve ser o usuário logado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16343842763031) SOLUÇÃO:**

Dessa forma, essa situação trata-se de um **comportamento** previsto para o sistema. Caso o cliente deseje que a regra do layout seja obedecida, a duplicação não será o processo adequado.
