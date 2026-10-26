---
id: "44010661290903"
titulo: "Integração Meetime <> Pipedrive"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010661290903-Integra%C3%A7%C3%A3o-Meetime-Pipedrive"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:43:33Z"
rotulos: ["sync_hc", "meetime", "meetime_343", "sync_hash_a5e4214e06bb"]
---

# Integração Meetime <> Pipedrive

Facilite a gestão das oportunidades comerciais! Com a integração da Meetime com o Pipedrive você consegue ter:

- **Tenha no CRM apenas oportunidades reais de negócio**
  Mantenha seu CRM organizado e limpo, com oportunidades que representem apenas potenciais de negócio;
- **Registro automático das atividades**
  Evite o trabalho manual do registro das interações realizadas com os leads no histórico das interações de prospecção, e nas chamadas integradas Meetime <> Pipedrive;
- **Ligações integradas** e **Preenchimento automatizado no CRM**
  Elimine os gargalos de registro de atividades, anotações e dados dos leads, aumentando a produtividade do time.

## Como funciona?

Ao dar um lead como Ganho na Meetime, será criado um Negócio no Pipedrive conforme estágio e funil selecionado. Também é possível enviar dados do lead na Meetime (campos padrões e personalizados) a Pessoa, Negócio e Empresa no Pipedrive.

Caso ative as funcionalidades de [Registro de Reunião](https://suporte.meetime.com.br/hc/pt-br/articles/13029117590297) **+** [Feedback de Oportunidade](https://suporte.meetime.com.br/hc/pt-br/articles/10351031263641) será enviado o link do formulário de Feedback de Oportunidade nas notas da Oportunidade, bem como será criada a atividade de Reunião.

## Como ativar a integração?

As configurações iniciais da integração precisam ser realizadas por um usuário de **Gestor ou Administrador**, seguindo os passos abaixo:

### 1. Vincular contas:

Primeiro passo é gerar a chave de API no Pipedrive. Isso pode ser feito acessando [Configurações > Preferências pessoais > API](https://support.pipedrive.com/pt/article/how-can-i-find-my-personal-api-key), em seu Pipedrive:

![Imagem 1: Primeiro passo é gerar a chave de API no Pipedrive. Isso pode ser feito acessando Configurações > Preferências pessoais…](https://ajuda.sankhya.com.br/hc/article_attachments/44010665572503)

Após copiar o código, basta acessar a Meetime e ir em **Menu > Integrações >** [Pipedrive](https://meetime.com.br/dashboard/integrations/pipedrive) para acessar a página onde o token deve ser incluído.

![Imagem 2: Após copiar o código, basta acessar a Meetime e ir em Menu > Integrações > Pipedrive para acessar a página onde o token…](https://ajuda.sankhya.com.br/hc/article_attachments/44010676427031)

Ao finalizar o processo de vinculação das contas, você será direcionado para a página de **Editar preferências**. Caso isso não aconteça automaticamente, basta clicar em **Editar preferências**.

![Imagem 3: Nessa página, você poderá definir como será o comportamento das informações das atividades entre a Meetime e o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010638907415)
Nessa página, você poderá definir como será o comportamento das informações das atividades entre a Meetime e o Pipedrive.

![Imagem 4: Nessa página, você poderá definir como será o comportamento das informações das atividades entre a Meetime e o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010689453847)

### 2. Associação de campos

A associação de campos permite encaminhar campo padrão e personalizado da Meetime para seu CRM, para configurar a associação de campos você precisa acessar **Prospecção > Ajustes > Associação de Campos >** [\*\*Pipedrive: \*\*](https://meetime.com.br/dashboard/prospector/config/field-association/pipedrive)

![Imagem 5: A associação de campos permite encaminhar campo padrão e personalizado da Meetime para seu CRM, para configurar a…](https://ajuda.sankhya.com.br/hc/article_attachments/44010677104279)

Nessa página você pode configurar os campos de **Pessoa, Organização e Negócio**. Basta clicar em + para abrir a opção de incluir campos e relacionar as opções:

![Imagem 6: Nessa página você pode configurar os campos de Pessoa, Organização e Negócio . Basta clicar em + para abrir a opção de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010681024151)

### 4. Configuração de cadência

Nas configurações de cadências você pode definir qual o funil/estágio o lead será enviado após o ganho e quais usuários do CRM poderão receber esses leads.

Essa configuração é feita acessando **Prospecção >** [Cadências](https://meetime.com.br/dashboard/prospector/cadences), clicar na cadência desejada e editar as informações em **Enviar leads para: Pipedrive**:

![Imagem 7: Essa configuração é feita acessando Prospecção > Cadências , clicar na cadência desejada e editar as informações em…](https://ajuda.sankhya.com.br/hc/article_attachments/44010708768919)

Nessa página você pode definir o estágio que a oportunidade será criada no Pipe, quais usuários poderão receber esses leads, o tipo de distribuição realizada (automática ou manual). Existe a possibilidade de configurar o envio de leads **perdidos** para o Pipedrive, basta ativar o envio e selecionar o estágio para o qual o lead será enviado.

## Como ativar o Click-to-Call?

Utilizando essa função, ao clicar no número do contato no Pipedrive, abrirá o painel da Meetime para execução da ligação. A chamada será registrada no histórico de interações do Pipedrive, bem como as gravações. Na Meetime também será possível ter acesso às estatísticas e incluir um Feedback para a Ligação.

Para ativar o Click-to-call você já precisa ter realizado pelos menos os 3 primeiros passos das configurações de integração, incluindo pelo menos as atividades de ligação no Pipe e nas preferências da integração na Meetime.

Após esse processo, **todos os usuários** que utilizam o sistema para ligações devem seguir os passos abaixo:

### 1. Copiar o link de integração na Meetime

O link está disponível em Menu > Integrações > Pipedrive e só aparece para os usuários que já fizeram a [vinculação das contas:](https://suporte.meetime.com.br/hc/pt-br/articles/29956577359897-Integra%C3%A7%C3%A3o-com-o-Pipedrive#h_01HS7GNSN8D9HVEWZ9B9J40WCN)

![Imagem 8: O link está disponível em Menu > Integrações > Pipedrive e só aparece para os usuários que já fizeram a vinculação das…](https://ajuda.sankhya.com.br/hc/article_attachments/44010690352791)

### 2. Cadastrar o link no Pipedrive

A configuração do link no pipedrive é feita em **Ferramentas e** **aplicativos > Chamadas telefônicas > Pessoal >** **Personalizar**:

![Imagem 9: A configuração do link no pipedrive é feita em Ferramentas e aplicativos > Chamadas telefônicas > Pessoal >…](https://ajuda.sankhya.com.br/hc/article_attachments/44010663872407)

Após essas configurações sua integração já estará pronta para funcionar.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
