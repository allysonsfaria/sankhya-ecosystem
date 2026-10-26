---
id: "44010749160215"
titulo: "Como importar leads na Meetime?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010749160215-Como-importar-leads-na-Meetime"
trilha: "Meetime > Leads"
atualizado_em: "2026-10-05T18:45:24Z"
rotulos: ["sync_hc", "meetime", "meetime_497", "sync_hash_4a9dec69b196"]
---

# Como importar leads na Meetime?

A importação de leads no Meetime Flow poder ser feita através de uma integração, pela adição manual ou por uma lista de leads.

## Integração

Através da integração de outras ferramentas ao Meetime Flow, os leads são adicionados automaticamente na plataforma.

Caso você utilize uma ferramenta para geração de leads que não tenha integração nativa com o Meetime Flow, a integração pode ser desenvolvida utilizando nossa API ([acesse aqui](https://meetime.readme.io/reference/introdu%C3%A7%C3%A3o) nossa documentação da API).

## Adição manual

Caso queira adicionar um lead por vez, basta acessar o menu Prospecção (barra superior preta) > Leads > + Adicionar

### Imagem 1: Configurações de entradaConfigurações de entrada

![Imagem 2: O lead adicionado manualmente será considerado como um lead Outbound, mas é possível selecionar a opção “ Adicionar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010728902679)O lead adicionado manualmente será considerado como um lead Outbound, mas é possível selecionar a opção “**Adicionar como lead inbound**”, caso esse seja o foco dessa abordagem

- Você também precisa indicar se o lead será disponibilizado imediatamente para o usuário prospectar, ou ficará aguardando início. No segundo caso, na tela de execução, o usuário precisa clicar em “Iniciar novas prospecções” pro ativamente, saiba mais acessando este artigo [Como adicionar mais atividades à página de Execução?](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768917962-como-adicionar-mais-atividades-a-pagina-de-execucao)
- Selecione o usuário responsável pelo lead, ou seja, o usuário que irá prospectar o lead
- Selecione a cadência de destino do lead. Lembrando que o responsável pelo lead deve ser participante da cadência selecionada. Veja aqui como configurar os participantes da cadência

### Informações do lead

Os campos **E-mail**, **Empresa**, **Primeiro nome** e **Nome completo**, estão marcados como obrigatórios, mas a partir do momento que você preencher um desses campos, os outros perdem a obrigatoriedade

É sempre importante adicionar o máximo de informações que tiver sobre o lead para agilizar e personalizar sua abordagem

Clicando em “**+ Ver mais”**, irá aparecer todos os campos disponíveis para preenchimento. É possível criar quantos campos forem necessários para a sua operação.

Quando finalizar o preenchimento das informações, clique em “**Salvar**”

## Lista de leads

Você pode adicionar leads em massa no Meetime Flow através de uma lista de leads

Quando os leads são adicionados através de uma lista, seu status sempre será **“Esperando início”**

### Como criar a lista de leads?

1. Você deve criar uma planilha na qual a primeira linha irá indicar o nome do campo (nome, telefone, e-mail...)
2. Depois é só preencher com as informações do lead. Cada linha irá representar um lead.

‼️Os campos da planilha precisam existir na ferramenta, você pode criar quantos campos precisar. Veja aqui como criar novos campos

‼️Não esqueça de colocar o telefone com DDD

![Imagem 3: ‼️Não esqueça de colocar o telefone com DDD](https://ajuda.sankhya.com.br/hc/article_attachments/44010742624023)

Para importar o arquivo no Meetime Flow você precisa salvá-lo no modelo CSV UTF-8, assim a formatação do arquivo será mantida

Você pode utilizar nossa planilha de exemplo como base, para acessar o arquivo basta [clicar aqui.](https://docs.google.com/spreadsheets/d/1RlT48bCr4vhgcK_iiFpDyGZ36I72Z8VyFPoXhpIMMas/edit?usp=sharing)

### Importar lista de leads

Para importar a lista de leads, basta clicar no menu Prospecção (barra superior preta) > Leads > Listas de importação > + Importar nova lista de leads.

![Imagem 4: 1. Faça o upload do arquivo](https://ajuda.sankhya.com.br/hc/article_attachments/44010758674071)1. Faça o upload do arquivo

![Imagem 5: 2. Agora vamos associar as colunas do arquivo com os campos do Meetime Flow. Essa ação é necessária para que os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010742983575)2. Agora vamos associar as colunas do arquivo com os campos do Meetime Flow. Essa ação é necessária para que os campos dos leads sejam preenchidos automaticamente com todas as informações contidas no arquivo

[GIF animado: Imagem 6: 2. Agora vamos associar as colunas do arquivo com os campos do Meetime Flow. Essa ação é necessária para que os campos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010737888279)

1. Adicione o nome da lista, para facilitar a identificação
2. Selecione a **cadência** de destino dos leads
3. Preencha a data em que os leads irão ficar disponíveis para a execução. Os usuários só terão acesso aos leads, para execução, a partir da **data definida** nesta etapa
4. Clique em **“próximo”**

Pronto, sua lista foi adicionada na plataforma!

## Dúvidas Frequentes

### Como definir o responsável pelo lead?

Quando você importar uma lista na plataforma, os leads ficarão disponíveis para qualquer usuário que seja participante da cadência em que a lista foi adicionada

Caso seja necessário definir o usuário que irá receber os lead, basta criar uma coluna, na planilha, com o **e-mail do usuário** responsável pelo lead e associar ao campo **“Proprietário no flow (E-mail)”**

### Como adicionar mais de um telefone para o mesmo lead?

Quando o lead possui mais de um telefone, basta criar mais de uma coluna com o nome “Telefone” e associar todas elas ao campo **“Telefone(s)”**

[Esse vídeo](https://vimeo.com/347815581?fl=pl&fe=sh) possui mais detalhes de como importar leads para a Meetime.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
