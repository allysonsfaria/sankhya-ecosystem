---
id: "44010440096535"
titulo: "Integração HubSpot + Meetime: Como preencher a documentação?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010440096535-Integra%C3%A7%C3%A3o-HubSpot-Meetime-Como-preencher-a-documenta%C3%A7%C3%A3o"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:38:21Z"
rotulos: ["sync_hc", "meetime", "meetime_337", "sync_hash_2e76a12d94b6"]
---

# Integração HubSpot + Meetime: Como preencher a documentação?

## O que é a documentação?

A documentação faz parte do processo de integração entre o HubSpot e a Meetime. Trata-se de uma planilha onde você irá informar os dados que deseja integrar e definir quais fluxos vai utilizar.

O preenchimento dessa documentação corresponde à **etapa 3** do processo de integração. Você pode conferir todas as etapas detalhadamente nesse artigo: [Integração HubSpot + Meetime: Como ativar a integração?](https://suporte.meetime.com.br/hc/pt-br/articles/48792217971993/live_preview/01K1E6TC8RV5RJ0SW4X0AGAXTQ)

Após realizar o primeiro passo da integração — a ativação dentro da sua conta Meetime — e o segundo passo, que consiste na definição dos fluxos e na criação das cadências e campos personalizados, o time de Suporte irá disponibilizar a documentação para preenchimento.

## Preenchimento da documentação:

Agora que você já criou as cadências, configurou os campos personalizados, definiu os fluxos que irá utilizar e respondeu às 5 perguntas relacionadas, é só seguir com o preenchimento da planilha!

Abaixo, você confere o detalhamento de como realizar esse preenchimento. Utilize como base as respostas das 5 perguntinhas e preencha apenas o que for correspondente ao fluxo que você irá utilizar.

\*Campos em verde na planilha são editáveis, já os campos em cinza não podem ser editados!

### Aba 01. Associação de campos de contato

Nessa aba, é feita a associação entre os campos da Meetime e os campos correspondentes no HubSpot — ou seja, você pode escolher como as informações devem ser mapeadas entre as duas plataformas.

![Imagem 1: Nessa aba, é feita a associação entre os campos da Meetime e os campos correspondentes no HubSpot — ou seja, você pode…](https://ajuda.sankhya.com.br/hc/article_attachments/44010457569431)

> **Conteúdo Extra: Associação de campos**
>
> Além de associar os campos padrão da Meetime, você também pode criar campos personalizados para enviar e receber informações entre Meetime e HubSpot.
>
> Tipos de campos suportados na Meetime:
>
> - Texto
> - Texto Aberto
> - Campo de seleção
>
> **Como criar campos personalizados na Meetime:**
>
> 1. Acesse o menu Prospecção.
> 2. Vá em Ajustes > Campos dos Leads.
> 3. Clique no botão “+” para adicionar um novo campo.
> 4. Defina o nome, tipo e demais configurações desejadas.
> 5. Após configurar, clique em Salvar.
>
> ![Imagem 2: Após configurar, clique em Salvar .](https://ajuda.sankhya.com.br/hc/article_attachments/44010420811287)
>
> ![Imagem 3: Após configurar, clique em Salvar .](https://ajuda.sankhya.com.br/hc/article_attachments/44010425411351)
>
> Você pode repetir o processo para adicionar quantos campos personalizados forem necessários.

### Aba 02. Associação de Atividades

Nessa aba,  você define, de acordo com o resultado da ligação na Meetime, o que deseja que seja registrado no HubSpot.

Só precisa preencher a coluna "Associação de ligações HubSpot".

![Imagem 4: Só precisa preencher a coluna "Associação de ligações HubSpot".](https://ajuda.sankhya.com.br/hc/article_attachments/44010458481303)

### Aba 03. Envio dos leads do HubSpot para a Meetime

Para que o fluxo de envio de leads HubSpot → Meetime funcione, você precisa ter um plano específico no HubSpot, que é o Plano Marketing PRO, e também ter os Webhooks liberados.

Quando não possui esse plano, infelizmente não é possível utilizar esse fluxo.

Agora, se você já tem o plano e deseja ativar o fluxo, é só preencher a coluna "Nome da cadência na Meetime" na documentação com as cadências onde deseja receber os leads.

![Imagem 5: Agora, se você já tem o plano e deseja ativar o fluxo, é só preencher a coluna "Nome da cadência na Meetime" na…](https://ajuda.sankhya.com.br/hc/article_attachments/44010488581783)

### Aba 04. Envio de leads finalizados Meetime > HubSpot

Nessa aba, você define o que deve acontecer quando o lead é finalizado (dado como ganho ou perdido).

- Se desejar ativar o fluxo de envio de leads ganhos para o HubSpot, é necessário preencher a coluna "Lead Status HubSpot" da tabela: “Associação do status do lead Meetime <> HubSpot”

![Imagem 6: Se desejar ativar o fluxo de envio de leads ganhos para o HubSpot, é necessário preencher a coluna "Lead Status…](https://ajuda.sankhya.com.br/hc/article_attachments/44010488827799)

- Se desejar ativar o envio de leads perdidos, é necessário preencher as colunas: "Motivos de Perda Meetime" e "Lead Status HubSpot" na tabela: LEAD PERDIDO: Associação dos motivos de perda ao status do HubSpot

![Imagem 7: Se desejar ativar o envio de leads perdidos, é necessário preencher as colunas: "Motivos de Perda Meetime" e "Lead…](https://ajuda.sankhya.com.br/hc/article_attachments/44010441874199)

- Se desejar que um Deal (Negócio) seja criado quando o lead for ganho, deve preencher a tabela: LEAD GANHO: Funil e Estágio padrão para criação de Deals no HubSpot, indicando o Funil e o Estágio do Funil onde os leads ganhos serão criados.

![Imagem 8: Se desejar que um Deal (Negócio) seja criado quando o lead for ganho, deve preencher a tabela: LEAD GANHO: Funil e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010474922647)

- Se quiser definir Funis e Estágios diferentes para cada cadência, deve preencher a tabela: OPCIONAL: Criação de deals em diferentes funis com base na cadência da Meetime.

![Imagem 9: Se quiser definir Funis e Estágios diferentes para cada cadência, deve preencher a tabela: OPCIONAL: Criação de deals…](https://ajuda.sankhya.com.br/hc/article_attachments/44010475136535)

- Se houver cadências nas quais você não deseja que um Deal seja criado, é necessário listar essas cadências na tabela: OPCIONAL: Cadências em Blacklist

![Imagem 10: Se houver cadências nas quais você não deseja que um Deal seja criado, é necessário listar essas cadências na tabela:…](https://ajuda.sankhya.com.br/hc/article_attachments/44010475387671)

### Aba 05. Associação de campos de negócio (Deals)

Nessa aba, é feita a associação entre os campos da Meetime e os campos correspondentes no HubSpot — ou seja, você escolhe como as informações devem ser mapeadas entre as duas plataformas.

![Imagem 11: Nessa aba, é feita a associação entre os campos da Meetime e os campos correspondentes no HubSpot — ou seja, você…](https://ajuda.sankhya.com.br/hc/article_attachments/44010489923735)

Ao finalizar essa etapa, envie o link da planilha preenchida para o nosso time de Suporte, juntamente com as 5 perguntas respondidas. Em seguida, você receberá por e-mail as instruções para configurar os Webhooks na Meetime.

Você pode conferir o passo a passo para configurar os Webhooks neste artigo: [Integração HubSpot + Meetime: Como ativar a integração?](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768595752-integracao-hub_spot-meetime-como-ativar-a-integracao) — a partir do Tópico 3.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
