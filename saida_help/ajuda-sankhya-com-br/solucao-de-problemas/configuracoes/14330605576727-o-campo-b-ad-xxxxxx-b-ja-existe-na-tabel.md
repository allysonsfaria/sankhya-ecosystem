---
id: "14330605576727"
titulo: "O campo <b>AD_XXXXXX</b> já existe na tabela <b>XXXXX</b> "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14330605576727-O-campo-b-AD-XXXXXX-b-j%C3%A1-existe-na-tabela-b-XXXXX-b"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:58:54Z"
rotulos: ["Configuração", "Campo Adicional", "DBExplorer", "CORE_E01914", "Conflito de Campo Adicional na Tabela", "Erro"]
---

# O campo <b>AD_XXXXXX</b> já existe na tabela <b>XXXXX</b> 

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16911542209815) **MENSAGEM:**

[CORE\_E01914]: O campo <b>AD\_XXXXXX</b> já existe na tabela <b>XXXXX</b>.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16911542211095)SOLUÇÃO:**

Acesse a tela **"DBExplorer"** (Caminho de acesso: Configurações » Avançado » DBExplorer) e faça a seguinte consulta SELECT (o nome do campo) FROM (nome da tabela) para certificar de que o campo que está tentando criar já existe na tabela. Segue exemplo abaixo:

![Imagem 3: Acesse a tela " DBExplorer" (Caminho de acesso: Configurações » Avançado » DBExplorer) e faça a seguinte consulta…](https://ajuda.sankhya.com.br/hc/article_attachments/14330550066455)

Caso seja apresentado o campo, não será possível criá-lo novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16911531965335)CAUSA:**

Ocorre quando usuário tenta criar um **Campo adicional** com o mesmo **nome** de um campo já existente na tabela.
