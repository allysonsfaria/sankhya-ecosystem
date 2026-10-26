---
id: "44011131624599"
titulo: "Ativação Click to Call > HubSpot"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011131624599-Ativa%C3%A7%C3%A3o-Click-to-Call-HubSpot"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:56:56Z"
rotulos: ["sync_hc", "meetime", "sync_hash_e0d4c874cb33", "meetime_826"]
---

# Ativação Click to Call > HubSpot

Para utilizar o click-to-call é necessário instalar o app do click-to-call da Meetime na conta do Hubspot.

## ✅Etapa 1: Instalação

Para realizar a **instalação**, é necessário solicitar ao time da Meetime a URL de instalação. Com a URL em mãos, basta colá-la na barra de endereços do navegador e pressionar Enter. Em seguida, a janela abaixo será exibida:

![Imagem 1: Para realizar a instalação , é necessário solicitar ao time da Meetime a URL de instalação. Com a URL em mãos, basta…](https://ajuda.sankhya.com.br/hc/article_attachments/44011140336919)

## ✅ Etapa 2: Conexão

Nesta etapa, será necessário realizar a **conexão** da conta. Para isso, o usuário deve ser superadministrador da conta no HubSpot ou possuir as seguintes permissões:

- crm.objects.users.read, crm.objects.contacts.write, crm.objects.companies.write, crm.objects.deals.write.

Para conectar, basta selecionar a conta “Meetime” e clicar em “Escolher conta”.

![Imagem 2: Para conectar, basta selecionar a conta “Meetime” e clicar em “Escolher conta”.](https://ajuda.sankhya.com.br/hc/article_attachments/44011131979031)

## ✅ Etapa 3: Webhook

Após a conexão, é criado um **Webhook** na conta da Meetime para os eventos CALL.FINISHED e CALL.UPDATED apontando para a URL:

<https://v1.dataflow.meetime.com.br/webhook/9c5ab0ee-f6f4-4365-9550-9caf8d58cfa4>

- Para verificar se o Webhook está ativo, siga o caminho: Perfil → Integrações → Webhooks.

Verifique se o webhook de ligação com a URL informada foi criado e está ativo, conforme abaixo:

![Imagem 3: Verifique se o webhook de ligação com a URL informada foi criado e está ativo, conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44011140657047)

## Uso

Com o app instalado, sempre que uma página de Negócio (Deal), Empresa ou Contato for acessada no HubSpot, o widget de Click-to-Call da Meetime será exibido na barra lateral direita:

![Imagem 4: Com o app instalado, sempre que uma página de Negócio (Deal), Empresa ou Contato for acessada no HubSpot, o widget de…](https://ajuda.sankhya.com.br/hc/article_attachments/44011150092311)

Inicialmente o widget vai aparecer abaixo de todos os outros. É possível arrastá-lo para cima para ele ficar mais acessível.

![Imagem 5: Inicialmente o widget vai aparecer abaixo de todos os outros. É possível arrastá-lo para cima para ele ficar mais…](https://ajuda.sankhya.com.br/hc/article_attachments/44011165953943)

## Widget

**👉 O widget irá gerar links de chamada para cada telefone associado ao objeto da página, conforme abaixo:**

• Deal (Negócio): o widget exibirá todos os telefones dos Contatos e Empresas relacionadas.

• Empresa: o widget exibirá todos os telefones da Empresa e dos Contatos relacionados.

• Contato: o widget exibirá todos os telefones do Contato.

**👉 O widget utilizará os seguintes campos de telefone dos objetos:**

• Empresa: o widget buscará o telefone no campo phone.

• Contato: o widget buscará os telefones nos campos phone e mobilephone.

## 🔄️ Retorno das informações para o HubSpot (fluxo de volta)

> Quando uma ligação é realizada a partir de um telefone de **Contato** ou **Empresa**, em qualquer uma das páginas de **Contato**, **Empresa** ou **Deal** no HubSpot, as informações da chamada retornam para o HubSpot associadas aos respectivos objetos.

As informações são enviadas em **duas etapas**:

### 1. Finalização da ligação

Após o término da ligação, os seguintes dados são enviados ao HubSpot:

- Data e hora da ligação
- Duração
- Telefone de origem
- Telefone de destino
- Gravação da ligação
- Status da ligação (`COMPLETED` ou `NO_ANSWER`)
- Direção da ligação (sempre `OUTBOUND`)
- Usuário responsável pela ligação

### 2. Atualização da ligação com anotações e output

Quando a ligação é atualizada com anotações ou output, os dados enviados incluem:

- Data e hora da ligação
- Descrição da ligação no formato:
  `"Ligação Meetime ({{OUTPUT}}) {{Anotação da ligação}}"`
- Duração
- Telefone de origem
- Telefone de destino
- Status da ligação (`COMPLETED` ou `NO_ANSWER`)
- Direção da ligação (sempre `OUTBOUND`)
- Usuário responsável pela ligação

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
