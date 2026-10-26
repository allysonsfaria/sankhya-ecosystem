---
id: "44010838308119"
titulo: "Nova integração Ploomes <> Meetime - Dúvidas Frequentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010838308119-Nova-integra%C3%A7%C3%A3o-Ploomes-Meetime-D%C3%BAvidas-Frequentes"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:48:21Z"
rotulos: ["sync_hc", "meetime", "meetime_348", "sync_hash_82eb4edcb359"]
---

# Nova integração Ploomes <> Meetime - Dúvidas Frequentes

## Posso usar os dois fluxos da integração (Centralização no CRM e Leads Ganhos) ao mesmo tempo?

Não. Cada conta Ploomes pode utilizar apenas um tipo de integração por vez.

## É possível enviar leads de qualquer funil?

Não. Somente funis habilitados nas configurações da integração podem ser utilizados para enviar leads.

## Preciso preencher todos os campos do card para enviar o lead?

Não, mas o lead só será criado na Meetime se o card tiver pelo menos um dos seguintes campos preenchidos:

- Contato Principal – Nome
- Contato Principal – E-mail
- Empresa – Nome

## O que acontece se o card tiver apenas uma empresa (sem contato)?

O Ploomes criará automaticamente uma pessoa "fantasma" para associar as informações à Meetime. Assim, toda informação do contato atualizada pela Meetime, atualizará a informação dessa pessoa correspondente.

Essa pessoa não é duplicada nem impacta registros reais de contatos.

## Como funciona o campo “Responsável mais recente”?

É o campo que define quem será o responsável pelo lead na Meetime.
Pode ser alterado no Ploomes até o envio do card; depois da integração, só a Meetime pode atualizar esse valor.

## E se o lead já existir na Meetime com o mesmo e-mail?

Quando o Ploomes tenta enviar um lead com um e-mail que já está cadastrado, a integração segue esta lógica:

- Se o lead estiver fechado (ganho ou perdido), ele será reaberto na Meetime e entrará na nova cadência enviada pela Ploomes.
- Se o lead estiver aberto e a nova cadência tiver prioridade maior que a atual, o lead será atualizado com a nova cadência e com os dados mais recentes enviados pela Ploomes.
- Se o lead estiver aberto e a nova cadência tiver prioridade menor, nenhuma atualização será feita — o lead continuará com a cadência e as informações que já possui.

Essa regra garante que não haja duplicidade de leads e que apenas cadências mais relevantes ou recentes substituam as anteriores.

## Posso adicionar novos leads relacionados a um mesmo negócio?

Sim, mas com comportamentos diferentes dependendo do momento:

**Antes da integração:** Se, ao criar o card na Ploomes, você preencher o campo Contatos Relacionados, todos esses contatos serão enviados juntos para a Meetime, tornando-se múltiplos leads associados ao mesmo negócio.

**Depois da integração:** A criação de novos leads vinculados ao mesmo negócio deve ser feita diretamente pela Meetime. Se um novo Contato Relacionado for adicionado na Ploomes após o envio do card, ele não será sincronizado com a Meetime.

Em resumo: antes de enviar o card, os contatos relacionados são criados como leads na Meetime; depois de integrado, apenas a Meetime pode gerar novos leads associados ao mesmo negócio

## E se eu alterar o e-mail do contato na Ploomes depois da integração?

- Se o novo e-mail já existir em outro lead na Meetime, a integração bloqueia a atualização e reverte o valor original no Ploomes.
  Nesse caso, é criado um Registro de Interação informando a tentativa e a reversão automática.
- Se o novo e-mail não existir na Meetime, a atualização é realizada com sucesso, e o novo endereço passa a ser o e-mail válido do lead sincronizado.

## Como os motivos de perda são sincronizados?

Todos os motivos de perda do funil integrado na Ploomes aparecem automaticamente listados na Meetime.

Para que o motivo apareça na Meetime, ele precisa existir no Ploomes no funil correspondente.

## O que acontece quando um lead é ganho na Meetime?

Quando um lead é marcado como ganho na Meetime, o negócio na Ploomes pode:

- Ser movimentado de etapa.
- Permanecer na mesma etapa.
- Ser marcado como ganho, conforme definido nas configurações da conta.

Se existirem outros leads associados ao mesmo negócio, é possível mantê-los abertos ou marcá-los como perdidos, encerrando o ciclo para todos.

## O que acontece quando um lead é perdido na Meetime?

Quando um lead é marcado como perdido na Meetime, o negócio correspondente na Ploomes também pode ser marcado como perdido.

Se todos os leads associados ao mesmo negócio forem perdidos, o negócio será automaticamente perdido no Ploomes.

## E se houver checklists obrigatórios no funil da Ploomes?

A Meetime respeita as validações de checklist.

Se houver pendências obrigatórias, a movimentação de etapa do lead não será permitida até que os itens sejam preenchidos no Ploomes.

## O que é encerrado quando o lead associado ao negócio é ganho ou perdido?

Quando um lead vinculado a um negócio é ganho ou perdido na Meetime, o fluxo da integração é encerrado para aquele negócio. Ou seja, novas atualizações de dados deixam de ser enviadas, mas todo o histórico permanece disponível nas duas plataformas.

O comportamento, porém, depende se o negócio possui múltiplos leads associados:

**Negócio com apenas um lead:**

- Assim que o lead é ganho ou perdido, o negócio é encerrado na Ploomes. Nenhum novo dado é sincronizado, e a integração é finalizada.

**Negócio com múltiplos leads:**

- Se um dos leads for ganho, o negócio na Ploomes pode avançar de etapa, manter-se na mesma etapa ou ser marcado como ganho, conforme as configurações da conta e a integração é finalizada para aquele negócio.
- Se um lead for perdido, mas ainda houver outros leads em aberto, o negócio permanece ativo, e a integração continua funcionando normalmente.
- Se todos os leads associados forem marcados como perdidos, o negócio é automaticamente marcado como perdido, e a integração é encerrada.

## As atividades realizadas na Meetime aparecem no histórico da Ploomes?

Sim, cada atividade da cadência é automaticamente registrada como Registro de Interação correspondente (ex.: ligação → registro de telefone, e-mail → registro de e-mail, etc.).

## Posso mudar a cadência de um lead depois que ele foi enviado?

A alteração de cadência pode ser feita apenas pela Meetime. A informação será atualizada no campo da Ploomes em Cadência Mais Recente (Ploomes).

## Preciso atualizar manualmente usuários entre Ploomes e Meetime?

Não. Os usuários da Meetime são sincronizados automaticamente com os usuários do Ploomes (associação via e-mail). Novos usuários criados na Meetime também serão criados no Ploomes com o perfil padrão configurado.

## O que acontece se um funil for excluído da configuração da integração?

Ao remover um funil da integração, as automações “Enviar lead para a Meetime” configuradas nesse funil deixarão de funcionar, e nenhum novo lead será enviado.

## É possível associar duas contas Ploomes com uma conta da Meetime?

Atualmente não é possível.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
