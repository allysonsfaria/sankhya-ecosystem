---
id: "360043608254"
titulo: "Título não baixado, pois depende de liberação de limites"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043608254-T%C3%ADtulo-n%C3%A3o-baixado-pois-depende-de-libera%C3%A7%C3%A3o-de-limites"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:01:14Z"
rotulos: ["#revisadoclaudio", "Configuração", "Liberação de Limites", "Preferências", "Financeiro", "Título não baixado por limite de desconto.", "Se necessário desative liberação de limites por alçada", "Solicite aumento de limite ou liberação ao gerente.", "Erro"]
---

# Título não baixado, pois depende de liberação de limites

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16090522985367) MENSAGEM:**

Título não baixado, pois depende de liberação de limites!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16090536445207) SOLUÇÃO:**

A mensagem será apresentada quando o valor de desconto fornecido para o respectivo título é superior ao limite de desconto definido para o usuário logado. Nesse caso, as possibilidades abaixo devem ser analisadas para solução:

![Imagem 3: Solicitar ao gerente/supervisor da empresa, responsável pela definição de limites de liberação, um aumento do limite…](https://ajuda.sankhya.com.br/hc/article_attachments/16090536448919) Solicitar ao gerente/supervisor da empresa, responsável pela definição de limites de liberação, um aumento do limite desse usuário para o evento 29:

- Tela **"Usuários"** » Outras Opções » Limites para Liberação » no campo **"Evento"** informe o evento 29:

![Imagem 4: Tela "Usuários" » Outras Opções » Limites para Liberação » no campo "Evento" informe o evento 29:](https://ajuda.sankhya.com.br/hc/article_attachments/12274720350487)

![Imagem 5: Caso o ajuste acima não seja permitido para esse usuário, defina o liberador e solicite que o mesmo execute as…](https://ajuda.sankhya.com.br/hc/article_attachments/16090536451735) Caso o ajuste acima não seja permitido para esse usuário, defina o liberador e solicite que o mesmo execute as liberações através da rotina 'Liberação de Limites'. 

![Imagem 6: Por fim, caso a empresa não trabalhe com liberação de limites por alçada , alinhe com o usuário implantador do sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/16090523002135) Por fim, caso a empresa **não trabalhe com liberação de limites por alçada**, alinhe com o usuário implantador do sistema e redefina o parâmetro abaixo para **"DESLIGADO"**:

- Tela **"Preferências"**(Configurações » Avançado » Preferências)
- Chave **"USALIBLIM - 'Usar liberação de limites por alçada?"**

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16090523004439) CAUSA:**

Mensagem apresentada ao realizar baixa, quando o valor de desconto fornecido para o respectivo título é superior ao limite de desconto definido para o usuário logado.
