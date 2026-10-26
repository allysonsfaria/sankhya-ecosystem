---
id: "44010902569495"
titulo: "RD CRM x Meetime: Como funciona a integração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010902569495-RD-CRM-x-Meetime-Como-funciona-a-integra%C3%A7%C3%A3o"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:49:32Z"
rotulos: ["sync_hc", "meetime", "meetime_350", "sync_hash_4b542a481342"]
---

# RD CRM x Meetime: Como funciona a integração

A integração automatizará o envio de oportunidades qualificadas para o RD CRM. Sempre que um lead for ganho na Meetime, todas as atividades realizadas e informações sobre a prospecção do lead serão enviadas para o CRM.

**Importante:** Essa integração só está disponível para usuários dos planos Basic e Pro do RD Station CRM e do módulo Flow na Meetime.

Aqui explicaremos como funciona a integração, caso queira realizar essa integração basta acessar: [Como fazer a integração da Meetime e RD CRM](https://cloudchat2.cloudhumans.com/hc/meetime/articles/1768601801-como-fazer-a-integracao-da-meetime-e-rd-crm)

## O que acontece após o lead ganho?

Ao dar um lead como ganho em uma cadência integrado ao RD CRM serão criadas oportunidade, empresa e contato no CRM.

Cada opção tem suas particularidades ao ser criada, por isso detalharemos cada uma:

- **Oportunidade:** a oportunidade será criada no funil e etapa cadastrados na configuração de saída da cadência. O SDR será responsável por selecionar o vendedor responsável pela oportunidade no CRM, mas caso a reunião já esteja registrada, o responsável pela reunião também será atribuído como responsável pela oportunidade. 
  **Não é possível reaproveitar uma oportunidade já existente, a integração sempre criará uma nova oportunidade.**
- **Conta:** a conta possui um nome único para o RD CRM, nesse caso não é possível ter mais de uma conta com o mesmo nome. Assim a integração verificar se já existe uma conta com esse nome, caso exista essa conta será atualizada com as informações do lead após o ganho na Meetime, senão será criada uma nova conta e o nome será igual ao campo Empresa, Nome completo ou E-mail na Meetime.
- **Contato:** a criação do contato é realizada com base no e-mail da conta, quando já existe um contato com o mesmo e-mail ao dar ganho na Meetime o contato será atualizado e associada a oportunidade. Se o contato ainda não existe no CRM, ele será criado pela integração e associado a oportunidade.

Além desses passos também serão enviados os registros de atividades executadas na Meetime, essas atividades já são enviadas como concluídas e com a data e hora em que o lead foi marcado como ganho.

São enviadas todas as atividades realizadas do tipo E-mail, Ligação, Social Point e Pesquisa.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
