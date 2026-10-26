---
id: "9372035856663"
titulo: "Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9372035856663-N%C3%A3o-%C3%A9-permitido-edi%C3%A7%C3%A3o-pois-j%C3%A1-existem-Ordens-de-Produ%C3%A7%C3%A3o-lan%C3%A7adas-para-este-Processo-Produtivo-Crie-uma-nova-vers%C3%A3o-para-realizar-edi%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T15:08:28Z"
rotulos: ["Configuração", "Ordem de Produção", "Processo Produtivo", "Produção", "Preferências", "PROD_E00266", "Habilite/Desabilite parâmetros para permitir edição", "Alteração de matérias-primas após lançamento de OP", "Edição não permitida; já há Ordens de Produção"]
---

# Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16702984056343) MENSAGEM:**

[PROD\_E00266]: Não é permitido edição, pois já existem Ordens de Produção lançadas para este Processo Produtivo. Crie uma nova versão para realizar edição.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16702988375319) SITUAÇÃO:**

Ao tentar realizar alteração das matérias primas na tela composição do produto após já ter Ordens de Produção lançada na versão atual do processo produtivo.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16702984087447) SOLUÇÃO:**

![Imagem 4: Habilite os parâmetros "PERMITEDITLSTMP/PERMITEDITMP" para que o sistema permita editar as MPs na composição dos…](https://ajuda.sankhya.com.br/hc/article_attachments/16702988380823) Habilite os parâmetros **"PERMITEDITLSTMP/PERMITEDITMP"** para que o sistema permita editar as MPs na composição dos produtos e não valide a versão do processo;

![Imagem 5: Caso deseje manter o comportamento de validar a versão e não permitir alteração sem versionar, mantenha os parâmetros…](https://ajuda.sankhya.com.br/hc/article_attachments/16702984094487) Caso deseje manter o comportamento de validar a versão e não permitir alteração sem versionar, mantenha os parâmetros PERMITEDITLSTMP/PERMITEDITMP desabilitados;

![Imagem 6: Acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/16702984100887) Acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro PERMITEDITMP e desligue o mesmo:

![Imagem 7: Acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/9371980001047)

![Imagem 8: Acesse a tela Preferências (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/16702988400023) Acesse a tela Preferências (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro PERMITEDITLSTMP e desligue o mesmo:

![Imagem 9: Acesse a tela Preferências (Caminho de acesso: Configurações » Avançado » Preferências), informe o parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/9372031473047)

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16702984108951) CAUSA:**

Alterar as matérias primas na composição de produto após lançamento de OP sem versionar o processo produtivo.

![Imagem 11: O botão Despublicar na tela "Processo produtivo nova" (Caminho de acesso: Produção » Cadastros » Processo Produtivo -…](https://ajuda.sankhya.com.br/hc/article_attachments/16702984112919) O botão Despublicar na tela **"Processo produtivo nova"** (Caminho de acesso: Produção » Cadastros » Processo Produtivo - Nova) não permite despublicar e alterar o processo e será desabilitado nas próximas versões.
