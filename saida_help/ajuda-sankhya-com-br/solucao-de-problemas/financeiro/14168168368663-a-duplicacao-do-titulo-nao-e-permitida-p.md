---
id: "14168168368663"
titulo: "A duplicação do título não é permitida pelo parâmetro PERDUPLFIN"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14168168368663-A-duplica%C3%A7%C3%A3o-do-t%C3%ADtulo-n%C3%A3o-%C3%A9-permitida-pelo-par%C3%A2metro-PERDUPLFIN"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:59:32Z"
rotulos: ["Configuração", "Movimentação Financeira", "Preferências", "Financeiro", "CORE_E02391", "Ative a Duplicação", "Duplicação de Título", "Parâmetro Desabilitado", "Erro"]
---

# A duplicação do título não é permitida pelo parâmetro PERDUPLFIN

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16914410599319) MENSAGEM:**

[CORE\_E02391]: A duplicação do título não é permitida pelo parâmetro PERDUPLFIN.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16914440508055) SITUAÇÃO:**

Ao tentar duplicar um lançamento na movimentação financeira a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16914440538007)CAUSA:**

Ocorre quando tenta duplicar um lançamento na movimentação financeira com o parâmetro **"Permite Duplicar Financeiro? - PERDUPLFIN"** desabilitado.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16914410600855) SOLUÇÃO:**

![Imagem 5: Há um parâmetro chamado "Permite Duplicar Financeiro? - PERDUPLFIN" que, quando ligado irá irá habilitar a função de…](https://ajuda.sankhya.com.br/hc/article_attachments/16914440526487) Há um parâmetro chamado **"Permite Duplicar Financeiro? - PERDUPLFIN"** que, quando ligado irá irá habilitar a função de duplicação na movimentação financeira para todos os usuários.
 
![Imagem 6: Há um parâmetro chamado "Permite Duplicar Financeiro? - PERDUPLFIN" que, quando ligado irá irá habilitar a função de…](https://ajuda.sankhya.com.br/hc/article_attachments/16914410607639) Acesse a tela **"Preferências",** coloque o parâmetro **"Permite Duplicar Financeiro? - PERDUPLFIN"**  e habilite o mesmo.

![Imagem 7: Caso queira que somente alguns usuários possuam essa funcionalidade, há parâmetro: "Controla acesso de duplicação de…](https://ajuda.sankhya.com.br/hc/article_attachments/14168167179031)
 
![Imagem 8: Caso queira que somente alguns usuários possuam essa funcionalidade, há parâmetro: "Controla acesso de duplicação de…](https://ajuda.sankhya.com.br/hc/article_attachments/16914410612119) Caso queira que somente alguns usuários possuam essa funcionalidade, há parâmetro:  **"Controla acesso de duplicação de registros? - CONTACESSDUPLIC".** Quando habilitado, fará com que os usuários do sistema percam o acesso ao botão de duplicação de todas as telas, sendo necessário que este acesso seja concedido através de uma opção do Controle de Acessos do sistema. Quando o parâmetro estiver desabilitado, o sistema não apresenta a opção Duplicar no Controle de Acessos e não faz validação quanto ao acesso de duplicação e todos os usuários terão acesso ao botão Duplicar.
