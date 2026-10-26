---
id: "25313858585495"
titulo: "Para criar, alterar, duplicar ou excluir registros nesta tela, é necessário estar logado com um usuário do Sankhya OM que possua vínculo com o Sankhya ID"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25313858585495-Para-criar-alterar-duplicar-ou-excluir-registros-nesta-tela-%C3%A9-necess%C3%A1rio-estar-logado-com-um-usu%C3%A1rio-do-Sankhya-OM-que-possua-v%C3%ADnculo-com-o-Sankhya-ID"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:45:56Z"
rotulos: ["Configuração", "Segurança", "Preferências", "Sankhya ID", "Usuário deve ter Sankhya ID", "Use usuário com Sankhya ID ou desative parâmetro", "CORE_F00008", "Ação bloqueada com usuário SUP e parâmetro ativo", "Erro"]
---

# Para criar, alterar, duplicar ou excluir registros nesta tela, é necessário estar logado com um usuário do Sankhya OM que possua vínculo com o Sankhya ID

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/25313872664599)MENSAGEM:**

[CORE\_F00008] Para criar, alterar, duplicar ou excluir registros nesta tela, é necessário estar logado com um usuário do Sankhya OM que possua vínculo com o Sankhya ID. Realize o login com um usuário com vínculo com o Sankhya ID para realizar as ações desejadas

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/25313858573079) **SOLUÇÃO:**

Acesse o sistema com um usuário que difere do usuário SUP, vinculado a um SankhyaID. Ou, caso seja possível dentro das diretrizes da empresa, acesse a tela **"Preferências",**busque pelo parâmetro **"EXIGESKIDPNZ - Exige Sankhya ID para criar personalizações"** e desabilite-o.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/25313858575127) **CAUSA:**

O erro é apresentado ao tentar executar algumas ações de edição no sistema estando logado com um usuário SUP e tendo o parâmetro EXIGESKIDPNZ ligado.
