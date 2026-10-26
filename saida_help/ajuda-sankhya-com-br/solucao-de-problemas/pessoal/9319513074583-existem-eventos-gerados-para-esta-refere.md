---
id: "9319513074583"
titulo: "Existem eventos gerados para esta referência que já foram finalizados na receita. Não é possível excluí-la"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9319513074583-Existem-eventos-gerados-para-esta-refer%C3%AAncia-que-j%C3%A1-foram-finalizados-na-receita-N%C3%A3o-%C3%A9-poss%C3%ADvel-exclu%C3%AD-la"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:24:43Z"
rotulos: ["Configuração", "Eventos", "SEFAZ", "eSocial", "CORE_E01349", "Pause e reinicie o SanEsocial", "Eventos já finalizados na Receita", "Gere R2099 ou ajuste parâmetro \"FPSANREINFEXE\"", "Erro", "Central de Projetos"]
---

# Existem eventos gerados para esta referência que já foram finalizados na receita. Não é possível excluí-la

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16700891868055) MENSAGEM:**

[CORE\_E01349]: Existem eventos gerados para esta referência que já foram finalizados na receita. Não é possível excluí-la.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16700891871511) SITUAÇÃO:**

Ao consultar a referência na Receita Federal esta consta como aberta porém no sistema a mensagem é apresentada.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16700898186135) SOLUÇÃO:**

![Imagem 4: Caso existam eventos aprovados no eCAC a melhor prática é finalizar a referência gerando o R2099;](https://ajuda.sankhya.com.br/hc/article_attachments/16700891876375) Caso existam eventos aprovados no eCAC a melhor prática é finalizar a referência gerando o R2099;

![Imagem 5: Caso não se encaixe na situação acima, desligue o parâmetro "FPSANREINFEXE" na tela "Preferências" (Caminho de acesso:…](https://ajuda.sankhya.com.br/hc/article_attachments/16700891880727) Caso não se encaixe na situação acima, desligue o parâmetro  **"FPSANREINFEXE"** na tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências) e pause o SanEsocial.

![Imagem 6: Caso não se encaixe na situação acima, desligue o parâmetro "FPSANREINFEXE" na tela "Preferências" (Caminho de acesso:…](https://ajuda.sankhya.com.br/hc/article_attachments/16700891883415)

![Imagem 7: Depois que o evento for enviado corretamente, solicite ao TI que pare o SanEsocial e inicie ele novamente para que na…](https://ajuda.sankhya.com.br/hc/article_attachments/16700891890071) Depois que o evento for enviado corretamente, solicite ao TI que pare o SanEsocial e inicie ele novamente para que na próxima referência o SanEsocial não tente enviar os eventos.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16700898298391) CAUSA:**

Ao tentar excluir uma referência com eventos já finalizados na Receita.
