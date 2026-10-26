---
id: "360045106353"
titulo: "Editor de Mensagens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens"
trilha: "Manual do Produto > Inteligência e Análise > BI Móvel"
atualizado_em: "2026-07-29T13:40:06Z"
rotulos: ["AJUDA DO SKW", "manual", "BI Móvel", "SMS", "Script", "Tabelas", "Aba Mensagem", "Aba Propriedades", "Autor", "Caracteres alfanuméricos", "Cursores", "Editor de Mensagens", "Fila de Mensagem", "HTML", "Indicação", "Iteradores", "OSEMAILBIMOVEL", "Perfis Destinatários", "SeletorDados", "Tentativas", "br.com.sankhya.bim.edtmensagens", "Editor de Mensagens manual", "SERVDIRMOD", "SQL", "Configuração", "E-mail", "RMVQUEBRALNMSG", "Personalização de Mensagens no BI Móvel", "mensagens variáveis destinatários", "Mensagens"]
---

# Editor de Mensagens

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42310426284439) Módulo: BI Móvel > Mensagens      
```

---

A **"Mensagem"** é como os valores das variáveis serão apresentados ao usuário. São compostas por texto e fórmulas que serão enviadas por E-mail ou Mensagens SMS no celular. Para a composição de uma mensagem, atente-se para as informações que serão descritas nos tópicos a seguir.

Inicialmente, tem-se o **"Código"** único da mensagem que é atribuído automaticamente pelo sistema.

A marcação **"Ativa"** é responsável por dizer se a mensagem está habilitada e poderá ser utilizada em outras telas do sistema.

| Funcionalidades da tela |
| --- |
| [Aba Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#abapropriedades) |
| [Aba Mensagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#abamensagem) |
| [Aba Condição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#abacondio) |
| [Aba Perfis Destinatários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#abaperfisdestinatrios) |

![Imagem 2: Aba Perfis Destinatários](https://ajuda.sankhya.com.br/hc/article_attachments/1500005449062)

### Aba Propriedades

![Imagem 3: Aba Propriedades](https://ajuda.sankhya.com.br/hc/article_attachments/1500005545761)

Os seguintes campos fazem parte da aba Propriedades:

O campo **"Autor"** é preenchido por quem escreveu a mensagem automaticamente.

A **"Indicação"** será o meio pelo qual a mensagem será enviada, que poderá ser:

- E-mail/SMS;
- Mensagem Instantânea;
- Aplicativo Móvel;
- E-mail;
- SMS;
- Notificação do Sistema.

Em **"Data de alteração"** insira a data da última modificação na mensagem.

No campo **"Tentativas"**, tem-se o número de tentativas de envio para a mensagem antes de ser considerada falha de envio.

O **"Período"** possui configuração semelhante do campo Período das variáveis, e indicará os horários em que a condição da mensagem será testada para o envio. Se a condição for atendida, a mensagem será inserida na fila de envio.

Ao preencher o **"Tipo de conteúdo"**, será informado ao sistema se o texto da mensagem deve ser tratado como HTML ou texto plano (indicado para mensagens SMS).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#top)

### Aba Condição

Aqui é definida a condição que deve ser satisfeita para que uma mensagem seja enviada. Essa condição pode ser escrita tanto na linguagem de script própria do BI Móvel quanto na linguagem Java. Para mais detalhes sobre a construção da fórmula da condição, veja o tópico **"Condição de disparo das Mensagens"** dentro da aba [Mensagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#abamensagem).

![Imagem 4: Aqui é definida a condição que deve ser satisfeita para que uma mensagem seja enviada. Essa condição pode ser escrita…](https://ajuda.sankhya.com.br/hc/article_attachments/1500005545981)

**Observação:** para que as mensagens sejam enviadas apenas uma vez por dia, deve-se ligar o parâmetro **"Forçar envio único de Mens. diária BI Móvel? - MSDFORCUNDIA"**, porém, a mensagem deve possuir apenas um agendamento diário. Desse modo, caso haja um envio programado para depois da hora do processamento atual, este não será enviado.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#top)

### Aba Mensagem

Defina nessa aba o texto da mensagem. As regras para a formulação da mensagem serão discutidas no artigo [Linguagem de Script do BI MÓVEL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL).

![Imagem 5: Defina nessa aba o texto da mensagem. As regras para a formulação da mensagem serão discutidas no artigo Linguagem de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500005546101)

**Observação:** ligue o parâmetro **"Remove quebra de linha de mensagem BI Móvel?-RMVQUEBRALNMSG"** para que seja removido os caracteres de quebra de linha ("\n") do corpo da mensagem cadastrada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#top)

### Aba Perfis Destinatários

Aqui serão exibidas a lista de perfis contendo os consumidores para os quais a mensagem será enviada. Os consumidores e os perfis de envio devem ser previamente cadastrados.

![Imagem 6: Aqui serão exibidas a lista de perfis contendo os consumidores para os quais a mensagem será enviada. Os consumidores e…](https://ajuda.sankhya.com.br/hc/article_attachments/1500005449342)

![Imagem 7: Para verificar as especificidades do BI Móvel referente ao Editor de Mensagens , acesse a documentação Linguagem de…](https://ajuda.sankhya.com.br/hc/article_attachments/20473619002135) Para verificar as especificidades do BI Móvel referente ao Editor de Mensagens, acesse a documentação [Linguagem de Script do BI Móvel](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051941074-Linguagem-de-Script-do-BI-M%C3%93VEL).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106353-Editor-de-Mensagens#top)
