---
id: "10977147742615"
titulo: "Plano de Fundo Sankhya-Om"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10977147742615-Plano-de-Fundo-Sankhya-Om"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-03T11:34:42Z"
rotulos: ["Configuração", "Usuário", "Preferências", "não apagar", "Personalização", "Compartilhamento do Plano de Fundo no Sankhya-Om", "Sankhya-Om"]
---

# Plano de Fundo Sankhya-Om

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16363111295639) MENSAGEM:**

Ao alterar o plano de fundo do Sankhya-Om com o usuário SUP, o mesmo é alterado para os demais usuários.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363133680151)SOLUÇÃO:**

Esse é um comportamento do sistema, ao alterar o plano de fundo com o usuário SUP logado, o mesmo plano de fundo é inserido para aqueles usuários que nunca realizaram a mudança.

A partir da primeira alteração, mesmo que o usuário SUP altere o plano, a mudança não ocorrerá para o usuário em questão.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363133683863)CAUSA:**

O parâmetro **"WORKWALLPAPER"** no qual os planos de fundos são definidos é gerido por usuário. Então, para que ele consiga alterar para todos os usuários de uma vez só, é necessário deixar na TSIPAR apenas uma linha para o usuário SUP para este parâmetro, assim os demais usuários utilizarão o plano de fundo do usuário SUP. Mas se tiverem acesso a alteração e alterarem uma única vez, será criada uma linha para o respectivo usuário e o plano de fundo que ele escolher irá permanecer para ele.
