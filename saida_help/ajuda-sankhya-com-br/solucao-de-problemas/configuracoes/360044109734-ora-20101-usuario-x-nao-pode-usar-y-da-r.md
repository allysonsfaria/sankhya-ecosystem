---
id: "360044109734"
titulo: " ORA-20101: Usuário \"X\" não pode usar \"Y\" da regra \"Z\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109734--ORA-20101-Usu%C3%A1rio-X-n%C3%A3o-pode-usar-Y-da-regra-Z"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:28Z"
rotulos: ["#criadoRoger", "CORE_E02940", "Configuração", "Usuários", "Central de Certificações", "ORA-20101", "Validações de Acesso", "Regra de validação", "Erro"]
---

#  ORA-20101: Usuário "X" não pode usar "Y" da regra "Z"

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16980995289239) MENSAGEM:**

[CORE\_E02940]: Usuário "X" não pode usar "Y" da regra "Z"

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16980995302551) SITUAÇÃO:**

Mensagem apresentada em lançamentos diversos dentro do sistema Sankhya.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16980964015383) SOLUÇÃO:**

![Imagem 4: Acesse a tela "Usuários" (Caminho de acesso: Configurações » Controle de Acesso » Usuários);](https://ajuda.sankhya.com.br/hc/article_attachments/16980995307031) Acesse a tela **"Usuários"** (Caminho de acesso: Configurações » Controle de Acesso » Usuários);

![Imagem 5: Selecione o usuário que está logado no sistema, quando a mensagem é apresentada;](https://ajuda.sankhya.com.br/hc/article_attachments/16980995308311) Selecione o usuário que está logado no sistema, quando a mensagem é apresentada;

![Imagem 6: Na aba "Validações", verifique as Regras vinculadas para esse usuário;](https://ajuda.sankhya.com.br/hc/article_attachments/16980964023191) Na aba **"Validações",** verifique as Regras vinculadas para esse usuário;

![Imagem 7: Acesse a tela " Central de Certificações " (Caminho de acesso: Comercial » Avançado » Certificações) e selecione a…](https://ajuda.sankhya.com.br/hc/article_attachments/16980964027287) Acesse a tela "**Central de Certificações**" (Caminho de acesso: Comercial » Avançado » Certificações) e selecione a Regra localizada no item 3;

![Imagem 8: Analise a regra para compreender a permissão ou proibição que essa irá gerar;](https://ajuda.sankhya.com.br/hc/article_attachments/16980995316375) Analise a regra para compreender a permissão ou proibição que essa irá gerar;

![Imagem 9: Como solução, sintonize com o implantador e/ou usuário da empresa responsável pela criação e vinculação das regras,…](https://ajuda.sankhya.com.br/hc/article_attachments/16980964032791) Como solução, sintonize com o implantador e/ou usuário da empresa responsável pela criação e vinculação das regras, para compreender sua necessidade. Caso a regra esteja de acordo com o processo atual, reveja o lançamento realizado, informando dados compatíveis com as validações atuais.

**(1)** Para mais detalhes sobre a rotina acesse o link:

[Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053)

**![Imagem 10: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16980995322519)CAUSA:**

Ao tentar visualizar informações ou executar rotinas no sistema, se o usuário possuir uma 'Validação' da central de certificações que impeça o processo, será apresentada a mensagem.
