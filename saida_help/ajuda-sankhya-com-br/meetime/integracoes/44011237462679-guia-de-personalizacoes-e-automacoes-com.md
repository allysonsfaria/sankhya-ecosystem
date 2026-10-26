---
id: "44011237462679"
titulo: "Guia de personalizações e automações com a API da Meetime"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011237462679-Guia-de-personaliza%C3%A7%C3%B5es-e-automa%C3%A7%C3%B5es-com-a-API-da-Meetime"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:59:02Z"
rotulos: ["sync_hc", "meetime", "meetime_1882", "sync_hash_06cd65273fc4"]
---

# Guia de personalizações e automações com a API da Meetime

A API da Meetime permite conectar a plataforma a outras ferramentas e criar personalizações de acordo com as necessidades do seu negócio.

Neste artigo, vamos apresentar as principais possibilidades de uso da API, as ferramentas que podem ajudar nesse processo e o nível de conhecimento necessário para cada tipo de personalização.

## ✅ Parte 1 - API Meetime

A API da Meetime é aberta e pode ser utilizada por qualquer usuário que possui uma conta ativa. Para acessá-la, é necessário acessar esse link e utilizar um API Token, que funciona como uma chave de autenticação.

O token pode ser encontrado na própria Meetime, em Configurações > Integrações > API, e deve ser utilizado nas requisições feitas à API.

![Imagem 1: 👉 Link API: https://meetime.readme.io/reference/introdução++](https://ajuda.sankhya.com.br/hc/article_attachments/44011262562583)
👉 Link API: [https://meetime.readme.io/reference/introdução++](https://meetime.readme.io/reference/introdu%C3%A7%C3%A3o++)

**Principais recursos da API**

**Leads:** Permite consultar, criar e atualizar leads, além de enviar informações como nome, e-mail, telefone, empresa e campos personalizados.

**Prospecções:** Permite consultar as prospecções dos leads, seus responsáveis, status, datas e informações relacionadas ao andamento da prospecção.

**Cadências:** Permite consultar as cadências disponíveis e utilizá-las para iniciar novas prospecções de leads.

**Atividades:** Permite consultar as atividades realizadas ou pendentes em uma prospecção, como ligações, e-mails, pesquisas e tarefas sociais.

**Campos personalizados:** Permite trabalhar com os campos personalizados criados na Meetime, incluindo o envio e consulta desses dados por integrações.

**Usuários:** Permite acessar informações dos usuários e relacioná-los aos leads, prospecções e atividades realizadas.

**Webhooks:** Permitem que a Meetime envie informações automaticamente para outro sistema quando determinados eventos acontecem, como um lead ser ganho ou uma atividade ser realizada.

**Reuniões:** Permite trabalhar com informações de reuniões relacionadas aos leads e às prospecções, como data, participantes e responsável.

**Origem do lead:** Permite registrar e consultar informações sobre a origem dos leads, como campanha, fonte e canal.

**Fit Score:** Permite consultar a pontuação de fit atribuída ao lead, ajudando a identificar e priorizar oportunidades.

## ✅ Parte 2 - Nível de conhecimento

Nem toda personalização exige conhecimento avançado em programação. O nível necessário **vai depender da ferramenta utilizada e do tipo de personalização** que você deseja fazer.

Para integrações mais simples, ferramentas como Make e n8n permitem criar automações com pouco ou nenhum código.

Já para personalizações **mais específicas**, pode ser necessário ter conhecimento em API, requisições HTTP e programação.

## ✅ Parte 3 - Ferramentas que podem ser utilizadas

Existem algumas ferramentas que podem ser utilizadas junto à API da Meetime para criar personalizações e automações, como:

- **Make:** permite conectar a Meetime com outras ferramentas e criar automações sem precisar programar.
- **n8n:** permite criar fluxos de automação mais personalizados, podendo também utilizar código quando necessário.
- **Zapier:** permite conectar a Meetime a diversas outras ferramentas e criar automações de forma simples.
- **Postman:** pode ser utilizado para testar os endpoints da API e entender como as informações são enviadas e recebidas.

## ✅ Parte 4 - Como realizar uma automação/personalização

Para criar uma personalização, é importante entender primeiro o que você deseja fazer e quais ferramentas podem ser utilizadas. Um fluxo básico pode seguir estes passos:

**1️⃣** **Verificar a API da Meetime**

Primeiro, verifique se a informação ou ação que você precisa está disponível na API da Meetime.

**2️⃣** **Definir o destino**

Depois, identifique para qual ferramenta ou sistema essas informações precisam ser enviadas ou de onde elas precisam ser recebidas.

**3️⃣** **Escolher a ferramenta de automação**

Defina qual ferramenta será utilizada para fazer essa comunicação. Algumas opções são Make, n8n ou Zapier.

**4️⃣** **Montar o fluxo**

Configurar a automação para buscar, receber ou enviar as informações entre a Meetime e a ferramenta escolhida.

**5️⃣** **Testar a personalização**

Faça alguns testes para verificar se as informações estão sendo enviadas e recebidas corretamente.

**6️⃣** **Colocar a automação em funcionamento**

Depois de validar o funcionamento, a automação pode ser utilizada no dia a dia.

👇

**De forma resumida: API da Meetime → Ferramenta de automação → Ferramenta ou sistema de destino**

Esse processo pode ser adaptado de acordo com a necessidade de cada empresa e com as possibilidades disponíveis na API da Meetime.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [++suporte@meetime.com.br++](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [++(48) 3204-7590++](https://wa.me/554832047590).![Imagem 2: Ainda tem dúvidas? Entre em contato com a gente através do e-mail ++suporte@meetime.com.br++ ou WhatsApp através do…](https://ajuda.sankhya.com.br/hc/pt-br/articles/44011237462679-Guia-de-personaliza%C3%A7%C3%B5es-e-automa%C3%A7%C3%B5es-com-a-API-da-Meetime)
