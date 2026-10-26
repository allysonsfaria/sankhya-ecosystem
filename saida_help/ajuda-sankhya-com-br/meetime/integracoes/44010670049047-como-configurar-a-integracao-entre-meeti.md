---
id: "44010670049047"
titulo: "Como configurar a integração entre Meetime e Pipedrive?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010670049047-Como-configurar-a-integra%C3%A7%C3%A3o-entre-Meetime-e-Pipedrive"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:44:07Z"
rotulos: ["sync_hc", "meetime", "sync_hash_89bb648e3b18", "meetime_344"]
---

# Como configurar a integração entre Meetime e Pipedrive?

Esse artigo vai te mostrar o passo a passo de como realizar a integração entre Meetime e Pipedrive:

## Requisitos

- Conta no Pipedrive, com acesso a Administrador (não há restrição de plano)
- Conta na Meetime

## Módulo Flow

### Comportamento da integração

Ao dar um lead como Ganho na Meetime, será criado um Negócio no Pipedrive conforme estágio e funil selecionado. Ou, um Negócio já existente para o lead no CRM pode ser reaproveitado, mais infos [aqui](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1769020463-reaproveitamento-de-deal-no-pipedrive). Também é possível enviar dados do lead na Meetime (campos padrões e personalizados) a Pessoa, Negócio e Empresa no Pipedrive.

Em set./2023, lançamos a funcionalidade para que leads perdidos na Meetime também possam ser levados para o Pipe (criando Negócios no status “perdido” por lá), detalhes [aqui](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1769018316-como-enviar-leads-perdidos-para-o-pipedrive). Obs.: para leads perdidos não há reaproveitamento de um Negócio já existente no CRM.

Caso ative as funcionalidades de **Registro de Reunião + Feedback de Oportunidade** será enviado o link do formulário de Feedback de Oportunidade nas notas da Oportunidade, bem como será criada a atividade de Reunião.

### Como ativar:

A integração completa entre os dois sistemas se dá com os seguintes passos:

**1) Vincular contas e configurações**

- Um usuário com perfil de Administrador deve colocar o token do Pipedrive na Meetime e realizar a vinculação de atividades, conforme mostrado no vídeo abaixo. Depois, cada um dos usuários também precisa colocar seu token do Pipe dentro da nossa ferramenta.

**2) Configurar o envio de leads finalizados ao CRM**

- **Associação de campos:** Você poderá configurar quais campos deseja enviar à Oportunidade criada no Pipedrive. É só ir em Prospecção > Ajustes > Associação de campos > Pipedrive. É possível associar campos de Pessoa, Negócio e Organização no Pipedrive.

⚠️ Os dados de Prospector, Cadência, URL Pública do Lead e Anotações são enviadas em uma nota resumo no Pipedrive.

![Imagem 1: ⚠️ Os dados de Prospector, Cadência, URL Pública do Lead e Anotações são enviadas em uma nota resumo no Pipedrive.](https://ajuda.sankhya.com.br/hc/article_attachments/44010684156311)

**3. Configurações de Saída**

No momento de criar as cadências de prospecção você pode habilitar ou não as Configurações de Saída Pipedrive, em que irá selecionar:

- Estágio e Funil para criação da oportunidade;
- Quais vendedores podem receber a oportunidade, e se será roteamento manual ou automático.

![Imagem 2: Quais vendedores podem receber a oportunidade, e se será roteamento manual ou automático.](https://ajuda.sankhya.com.br/hc/article_attachments/44010700080535)

**4) Registro de Reunião e Feedback de Oportunidade**

O registro de reunião já está ativo na conta, mais informações, confira as orientações [aqui](https://suporte.meetime.com.br/hc/pt-br/articles/13029117590297-Registro-de-reuni%C3%A3o). O tipo de atividade criado no Pipedrive quando é feito o Registro de reunião é, por padrão, “Reunião” / “Meeting”.

Para ativar o Feedback de Oportunidade, é só ir nos ajustes da Prospecção, como orientado [aqui](https://suporte.meetime.com.br/hc/pt-br/articles/10351031263641-Feedback-de-Oportunidade) . Ao habilitar a funcionalidade, as oportunidades que a Meetime envia para o Pipedrive irão com um link para que o vendedor responsável possa preencher um feedback.

### Integração de Campos

**1 - Os campos associados entre Meetime e Pipedrive precisam seguir os mesmos padrões:** campos de seleção na Meetime serem campos de seleção no Pipedrive e campos de texto na Meetime serem campos de texto no Pipedrive.

Todos os valores de um campo selecionável precisam ser idênticos aos valores disponíveis na Meetime, incluindo acentos, letras, pontos e caracteres, caso contrário as informações não serão compatíveis e não chegarão à plataforma.

**2 - Alguns tipos de campos do Pipedrive não são integráveis aqui na Meetime**, como campos de múltipla seleção por exemplo, por não serem compatíveis aos formatos de campos disponíveis na Meetime.

Os tipos de campos do Pipedrive integráveis com a Meetime são:

> 'varchar', 'varchar\_auto', 'varchar\_options', 'text', 'double', 'int', 'phone', 'address', 'date', 'monetary', 'enum' e 'set'.

Esses e os outros tipos de campos do Pipedrive estão descritos na API do Pipedrive: <https://developers.pipedrive.com/docs/api/v1/DealFields#addDealField>

## Módulo Dialer

### 1. Comportamento da integração

Ao clicar no número do contato do Pipedrive, abrirá o painel da Meetime para execução da ligação. A chamada será registrada no histórico de interações do Pipedrive, bem como as gravações. Na Meetime também será possível ter acesso às estatísticas e incluir um Feedback para a Ligação. **A ligação precisa ser iniciada através da página do Deal no Pipedrive.**

### 2. Como ativar

A integração completa entre os dois sistemas se dá com os seguintes passos:

**a) Vincular contas e configurações**

- Um usuário com perfil de Administrador deve colocar o token do Pipedrive na Meetime e realizar a vinculação de atividades, conforme mostrado no vídeo abaixo. Depois, cada um dos usuários também precisa colocar seu token do Pipe dentro da nossa ferramenta.

**b) Configuração de chamadas integradas Meetime <> Pipedrive**

Através de um usuário Administrador deve ser configurado o click-to-call  (para iniciar as ligações diretamente da página de Negócio no Pipedrive) como mostra o vídeo abaixo.

### 3. Click-to-call

A imagem abaixo é referente à página de integrações do Pipedrive na Meetime. A parte superior, para adicionar o token, fica visível para todos os usuários. A parte inferior, de editar preferências e copiar link, só fica visível para usuários administradores/gestores:

![Imagem 3: A imagem abaixo é referente à página de integrações do Pipedrive na Meetime. A parte superior, para adicionar o token,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010692971543)

**3.1) Primeiro passo (token) - feito por todos os usuários:**

O token para integrar a Meetime com Pipedrive deve ser individual, para que reflita no Pipedrive qual usuário realizou a atividade. No Pipedrive, cada usuário deverá acessar a página “Ajustes > Preferências pessoais > API > Seu Token de API pessoal” para gerar o token:

![Imagem 4: Ao gerar o seu token, copiar e adicionar na página da Meetime, o usuário estará integrado com o Pipedrive e garantimos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010693174039)Ao gerar o seu token, copiar e adicionar na página da Meetime, o usuário estará integrado com o Pipedrive e garantimos que ao realizar uma atividade, o nome dele é que aparecerá no Pipedrive ao invés do nome do administrador/gestor. Esse passo só é necessário fazer uma unica vez.

#### 3.2) Segundo passo (preferências) - feito por um usuário administrador/gestor

Assim que realizar o passo anterior, o campo de preferências ficará visível para o usuário administrador/gestor e ele terá acesso à URL na sua tela.

Essa URL é a configuração que deve ser salva no Pipedrive para que o redirecionamento do click-to-call la seja redirecionado para a página da Meetime. Para fazer tal configuração, o usuário precisa acessar a página “Ajustes > Ferramentas e Aplicativos > Chamadas Telefônicas” clicar em “Aplicativo de chamada padrão > Personalizar > colar a URL na caixa de texto”:

![Imagem 5: Essa URL é a configuração que deve ser salva no Pipedrive para que o redirecionamento do click-to-call la seja…](https://ajuda.sankhya.com.br/hc/article_attachments/44010693382295)

É esperado que essa configuração seja replicado automaticamente para todos os usuários. Contudo, caso isso não ocorra, cada usuário pode acessar essa mesma página, utilizar o mesmo link e fazer a sua configuração pessoal. Dessa maneira, ao realizar a ação de click-to-call, eles devem ser redirecionado para a Meetime.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
