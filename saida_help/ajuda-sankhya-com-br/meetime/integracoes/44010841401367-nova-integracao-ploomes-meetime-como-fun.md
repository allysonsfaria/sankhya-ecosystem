---
id: "44010841401367"
titulo: "Nova integração Ploomes <> meetime - como funciona na prática?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010841401367-Nova-integra%C3%A7%C3%A3o-Ploomes-meetime-como-funciona-na-pr%C3%A1tica"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:48:08Z"
rotulos: ["sync_hc", "meetime", "meetime_347", "sync_hash_415f2b0a48ad"]
---

# Nova integração Ploomes <> meetime - como funciona na prática?

Após concluir a nova integração entre Ploomes e Meetime, o fluxo já está pronto para uso.

A seguir, apresentamos um exemplo prático demonstrando como o processo funciona do início ao fim.

## Exemplo de configuração utilizada

Neste exemplo, foi criada uma automação com os seguintes parâmetros:

- **Funil que poderá enviar leads (Passo 4):** [Prospecção] Novos clientes

- **Comportamento de leads ganhos (Passo 4):** "Ganhar o negócio no Ploomes"

- **Cadência da Meetime selecionada (Passo 4)**: "Cadência de Prospecção"

- **Etapa do funil no Ploomes (Passo 8):** "Enviar para a Meetime"

![Imagem 1: - Etapa do funil no Ploomes (Passo 8): "Enviar para a Meetime"](https://ajuda.sankhya.com.br/hc/article_attachments/44010834511511)

![Imagem 2: - Etapa do funil no Ploomes (Passo 8): "Enviar para a Meetime"](https://ajuda.sankhya.com.br/hc/article_attachments/44010857964183)

Detalhe importante da integração: O campo de Contatos Relacionados é opcional no momento da criação do lead/negócio. Ao escolher essa opção, quando o card for enviado para a Meetime, todos os contatos relacionados são criados como leads associados ao mesmo negócio.

### Criação e envio do card

1. Um novo card é criado no funil e possui os principais campos preenchidos:
2. Cliente (Pessoa ou Empresa)
3. Responsável mais recente (Meetime) - é esse campo que irá determinar qual usuário sincronizado com a Meetime será responsável pelo lead.
4. Quando o card é movido para a etapa "Enviar para a Meetime" (manualmente ou por automação) e atende aos filtros e gatilhos definidos, o lead é automaticamente criado na Meetime e atribuído ao responsável configurado.

![Imagem 3: Quando o card é movido para a etapa "Enviar para a Meetime" (manualmente ou por automação) e atende aos filtros e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010820504727)

### Execução da cadência na Meetime

Na Meetime, o usuário irá executar as atividades (ligações, e-mails, reuniões etc.) conforme a cadência configurada.

Cada atividade realizada na Meetime gera um **Registro de interação correspondente** no Ploomes. Isso garante que o histórico de relacionamento permaneça centralizado. Essas atividades são enviadas para a Pessoa (Contato) correspondente e o Negócio (Card) associado.

![Imagem 4: Cada atividade realizada na Meetime gera um Registro de interação correspondente no Ploomes. Isso garante que o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010842799511)

Correspondência entre Atividades e Registros

![Imagem 5: Correspondência entre Atividades e Registros](https://ajuda.sankhya.com.br/hc/article_attachments/44010830241687)

### Adição de novos leads pela Meetime

Durante a prospecção, o usuário pode adicionar novos leads associados ao mesmo negócio diretamente pela Meetime.

Para isso, você precisa estar visualizando a página do lead > Clicar em "Leads neste negócio".

![Imagem 6: Para isso, você precisa estar visualizando a página do lead > Clicar em "Leads neste negócio".](https://ajuda.sankhya.com.br/hc/article_attachments/44010835922711)

Esses leads adicionais são sincronizados e passam a aparecer no Ploomes como Contatos Relacionados do card original.

### Movimentação de Etapa pela Meetime

Também é possível movimentar o lead pelas etapas do funil integrado, diretamente pela Meetime.

![Imagem 7: Também é possível movimentar o lead pelas etapas do funil integrado, diretamente pela Meetime.](https://ajuda.sankhya.com.br/hc/article_attachments/44010836219159)

Observação: se o funil no Ploomes possuir checklists obrigatórios, a movimentação não ocorrerá até que todos os itens sejam preenchidos.

### Conclusão da cadência: lead ganho ou perdido

Ao finalizar a cadência, o usuário pode dar ganho ou perdido no lead. Com isso, o fluxo da integração também se encerra quando o lead é ganho ou quando todos os leads vinculados ao negócio são perdidos.

#### Lead ganho

- Nas configurações da integração é possível definir se quando o lead é marcado como ganho na Meetime o negócio será ganho, movimentado ou mantido na mesma etapa no Ploomes.
- Caso existam outros leads associados ao mesmo negócio, é possível optar por dar perdido nos demais leads

![Imagem 8: Caso existam outros leads associados ao mesmo negócio, é possível optar por dar perdido nos demais leads](https://ajuda.sankhya.com.br/hc/article_attachments/44010831427223)

#### Lead perdido

- Ao marcar um lead como perdido na Meetime, é possível definir se o negócio também será perdido no Ploomes.
- Quando há mais de um lead associado, será perguntado se deseja perder os demais leads. Caso a resposta seja positiva, o negócio será perdido obrigatoriamente e o contato principal será atualizado.
- Quando todos os leads relacionados ao negócio são marcados como perdidos, o card será automaticamente marcado como perdido no Ploomes.
- Leads perdidos sempre resultam na perda do negócio correspondente no Ploomes.

![Imagem 9: Leads perdidos sempre resultam na perda do negócio correspondente no Ploomes.](https://ajuda.sankhya.com.br/hc/article_attachments/44010860233751)

### Sincronização de Motivos de Perda

Os motivos de perda são sincronizados automaticamente entre Ploomes e Meetime. Isso garante a rastreabilidade total dos dados e evita divergências entre os relatórios de perda das duas plataformas.

- Todos os motivos de perda cadastrados no funil integrado da Ploomes são exibidos automaticamente na Meetime, no campo "Motivo de perda".
- Caso um motivo de perda seja excluído ou alterado na Ploomes, a mudança é refletida automaticamente na Meetime.

**Envio de Anotações e Atualizações**

- Sempre que um lead integrado a um card é ganho ou todos os leads integrados a um card são perdidos, as anotações da Meetime são enviadas para Ploomes, criando registros no Contato Principal e nos Contatos Relacionados.
- Quando um lead relacionado é marcado como ganho ou perdido, a atualização é enviada para:A Pessoa (Contato) correspondenteO Negócio (Card) associado.
- Esse envio ocorre mesmo que o negócio ainda esteja aberto, garantindo que o histórico de interações permaneça atualizado em tempo real.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
