---
id: "42427484758935"
titulo: "Por que os e-mails que encaminho para meu endereço do Ploomes não aparecem na minha conta?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427484758935-Por-que-os-e-mails-que-encaminho-para-meu-endere%C3%A7o-do-Ploomes-n%C3%A3o-aparecem-na-minha-conta"
trilha: "PLOOMES: Automação de propostas  > E-mails"
atualizado_em: "2026-08-10T18:02:57Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452327", "sync_hash_da1c75bf8bd2"]
---

# Por que os e-mails que encaminho para meu endereço do Ploomes não aparecem na minha conta?

O Ploomes permite que os e-mails trocados com clientes sejam centralizados nos históricos de interação. Para isso, há duas formas de integração: **Gmail** e **SMTP**. Neste artigo, você entenderá as regras necessárias para que a sincronização ocorra corretamente ao encaminhar mensagens manualmente.

## Como funciona a vinculação de e-mails

- **Gmail:** toda mensagem enviada ou recebida é sincronizada automaticamente.
- **SMTP:** é necessário colocar em cópia o endereço definido nas configurações gerais de e-mail. Um exemplo deste endereço pode ser visto na imagem abaixo:

  ![Imagem 1: SMTP: é necessário colocar em cópia o endereço definido nas configurações gerais de e-mail. Um exemplo deste endereço…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2157641933/a96edc7fe3366c6189e344f6657a/image.png?expires=1786536000&signature=30e54f369ffc16a74196a8ad62a3424a2622d7d5c85d75bc96288898096305f7&req=diEiEc96nIhcWvMW3nq%2BgfmiRjbUZnr%2BWLxeQpthiTMmkoLJ%2BADtBuATiDos%0Am87HQBbYu1rbkET43q1F5mci02Y%3D%0A)

## Mas por que em alguns casos, mesmo encaminhando os e-mails para este endereço, a mensagem não aparece no Ploomes?

O Ploomes verifica algumas regras antes de vincular o e-mail. Se essas regras não forem atendidas, o e-mail não será exibido nem vinculado ao cliente.

O e-mail só será vinculado se:

1. O **Endereço de e-mail Ploomes** cadastrado estiver presente na lista de e-mails da mensagem (como remetente ou destinatário);
2. **E** uma das seguintes condições for atendida:

   - O e-mail **SMTP integrado** está na lista;
   - **OU** o e-mail de **login do usuário** no Ploomes está na lista.

## Exemplos de casos

## Caso bem-sucedido:

Para exemplificar, vamos considerar o seguinte cenário:

- **E-mail de login do usuário:** tiago.pagani@ploomes.com
- **E-mail SMTP integrado:** comercial@ploomes.com
- **Endereço de e-mail Ploomes:** tiago.pagani@mail.ploomes.com

Um e-mail é recebido pelo usuário com as seguintes características:

- **De:** comercial@seucliente.com.br
- **Para:** comercial@ploomes.com, joao@seucliente.com.br

Em seguida o usuário encaminha para seu endereço Ploomes, ficando assim:

- **De:** comercial@ploomes.com
- **Para:** tiago.pagani@mail.ploomes.com

Neste caso, o e-mail aparecerá no Ploomes porque a regra é atendida. Note:

O **endereço de e-mail Ploomes** (tiago.pagani@mail.ploomes.com) está na lista de e-mails e o **e-mail SMTP integrado** está na lista de e-mails.

## Caso sem sucesso:

Um e-mail é recebido pelo usuário com as seguintes características:

- **De:** comercial@seucliente.com.br
- **Para:** financeiro@ploomes.com, joao@seucliente.com.br

Em seguida o usuário encaminha para seu endereço Ploomes, ficando assim:

- **De:** financeiro@ploomes.com
- **Para:** tiago.pagani@mail.ploomes.com

Neste caso, o e-mail **NÃO** aparecerá no Ploomes porque a regra é não é atendida. Note que embora o e-mail tenha sido encaminhado para tiago.pagani@mail.ploomes.com, os outros endereços correspondentes ao usuário (endereço de login do Ploomes e endereço SMTP vinculado) não estão na relação de e-mails. Sendo assim o Ploomes não tem como comprovar a identidade do usuário.

## Consideração geral

O principal motivo para esta regra existir é para evitar que uma pessoa má intencionada envie SPAMs para um usuário Ploomes. Sem ela, qualquer pessoa que descubra seu endereço Ploomes poderia enviar mensagens que seriam vinculadas automaticamente aos clientes, prejudicando a qualidade dos dados e poluindo a conta do usuário.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
