---
id: "42427470379159"
titulo: "Integração com Movidesk"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427470379159-Integra%C3%A7%C3%A3o-com-Movidesk"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:02:42Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5794875", "sync_hash_147a2c2189f8"]
---

# Integração com Movidesk

## Sobre o Movidesk

Movidesk é um software de atendimento que une recursos de Help Desk e Service Desk. Pode ser utilizado tanto para comunicação com os clientes quanto para comunicação interna. A ferramenta também torna as interações mais rápidas e mantém o histórico de cada uma delas, proporcionando um suporte muito mais organizado e eficiente.

---

## Introdução à integração

Esta integração nativa possui dois principais casos de uso:

- Alimentar o **histórico dos clientes** cadastrados no Ploomes com os **tickets** trabalhados no Movidesk (via **Registros de Interação**);

- Abrir um novo **ticket** no Movidesk a partir de um **negócio / card** criado no Ploomes, com posterior atualização deste negócio / card quando o ticket é finalizado.

  ![Imagem 1: Abrir um novo ticket no Movidesk a partir de um negócio / card criado no Ploomes, com posterior atualização deste…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1249260984/8c813ebbe32930fd0b9543d750b4/https3A2F2Fprod-files-secure.png?expires=1786536000&signature=d3d05d1a012ad7d34703b3f084743e8084f9496ca3757815b47bc5ec68ad4f62&req=dSIjH8t4nYhXXfMW3nq%2BgYdqW4cB9AZWkqhgHov%2B9Ned32M8nr7AyrW5yNyR%0AqtZqy7LWVKxSlmZRydlZeaYLu7Y%3D%0A)

---

## Integração de Clientes

- **Movidesk > Ploomes:**

  - **Criação:** disponível.

    - O Movidesk pode criar clientes no Ploomes caso esta opção esteja ativa nas configurações da integração;
    - Quando um ticket do Movidesk é enviado ao Ploomes, o Ploomes verifica se este cliente já está cadastrado em sua base (com base no e-mail). Caso não esteja, é criado de acordo com o mapeamento de campos;
  - **Alteração:** não disponível;
  - **Exclusão:** não disponível.
- **Ploomes > Movidesk:**

  - **Criação:** disponível.

    - Ao ativar a integração, um novo usuário de integração chamado Movidesk é criado no Ploomes de forma automática;
    - Quando um negócio / card é criado no Ploomes e tem seu campo de responsável ou usuários colaboradores preenchido com o usuário Movidesk, um novo ticket será criado no Movidesk;
    - Caso o cliente do card não exista no Movidesk (detecção a partir do e-mail ou do Id Movidesk), um novo será criado de acordo com o mapeamento de campos.
  - **Alteração:** não disponível;
  - **Exclusão:** não disponível.

---

## Integração de Tickets

- **Movidesk > Ploomes:**

  - **Criação:** disponível.

    - Os tickets são enviados do Movidesk ao Ploomes como Registros de Interação no histórico dos clientes. O conteúdo do registro terá as seguintes informações:

      - Status;
      - Id Ticket;
      - Assunto;
      - Data de abertura;
      - Categoria;
      - Urgência;
      - Responsável.
    - O momento do envio é configurado dentro das automações do Movidesk (explicado adiante neste artigo). É possível, por exemplo, enviar o ticket quando ele for finalizado ou quando for aberto.
  - **Alteração:** disponível.

    - Quando um ticket é criado pelo Ploomes no Movidesk, ao finalizar este Ticket pelo Movidesk, o negócio / card do Ploomes vinculado é dado como finalizado, e suas informações são atualizadas de acordo com o mapeamento de campos.
  - **Exclusão:** não disponível.
- **Ploomes > Movidesk:**

  - **Criação:** disponível.

    - Como explicado anteriormente, ao criar um negócio / card no Ploomes, basta incluir o usuário Movidesk como responsável ou usuário colaborador para que um ticket seja criado no Movidesk.
  - **Alteração:** não disponível;
  - **Exclusão:** não disponível.

---

## Como ativar a integração

1. **Token de acesso à API do Movidesk**

![Imagem 2: 1. Token de acesso à API do Movidesk](https://downloads.intercomcdn.com/i/o/431103979/8a4277a3950dd814800453d0/Captura+de+Tela+2021-12-08+a%CC%80s+10.45.45.png?expires=1786536000&signature=f0d0d2c270fe569cef860cfb9aee2a69d274fe8a5450d45b6c2989c5ee624faf&req=cCMmF8l9lIZWFb4V1XW4gRIkKe1Hd9HVHe3I9JnYEPYNZtAUzfaf%2BDGkgaFZ%0AAnAqTVMcV6ZecN4mgNoe6nl9eA%3D%3D%0A)

Acesse a tela de configurações do Movidesk e clique em **Parâmetros**. Dentro dessa nova tela, no final, copie e cole a chave da API no Ploomes, como mostra as imagens abaixo:

![Imagem 3: Acesse a tela de configurações do Movidesk e clique em Parâmetros . Dentro dessa nova tela, no final, copie e cole a…](https://downloads.intercomcdn.com/i/o/431107967/6805fb165c864f2639b986f7/Captura+de+Tela+2021-12-08+a%CC%80s+10.50.40.png?expires=1786536000&signature=3c115a52d136e109d9564eafefc08bf3f1a4d516a67b52e7efa9f1d2ce235767&req=cCMmF8l5lIdYFb4V1XW4gQnNOtF8tTzrhZ4oYJQRyPDJLZnzHWODRqa%2BRTHr%0AcVQpmw4o%2BagxcRh8jnm1D5auNw%3D%3D%0A)

2. **No Ploomes,** acesse a tela de Integrações **plug-and-play;**

![Imagem 4: 2. No Ploomes, acesse a tela de Integrações plug-and-play;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235812636/2b51daf325116bf4c4f2936829b3/I7mAlHv.png?expires=1786536000&signature=4aac06d6343ec305c04f053d8bf1ecf02ca77d0ebc82036fcc6ca4df711cace3&req=dSIkE8F%2Fn4dcX%2FMW3nq%2BgUAg4G4F%2FE9WaYsUcxnZ%2FdLQdNkEhdMLRe9t%2FOhI%0ABBb%2B39hFu2oSC83rrYwmcQmxEfY%3D%0A)

3. Clique no ícone do **Movidesk** para selecioná-lo;

![Imagem 5: 3. Clique no ícone do Movidesk para selecioná-lo;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235812926/05ebbd507877f1089e5c998d252c/funI3yB.png?expires=1786536000&signature=6259c0f0cc1fb2e86c07ff3a319b4f98ffbf5ac38646aea02a45e4b7ea73d3c4&req=dSIkE8F%2Fn4hdX%2FMW3nq%2BgbNGXRfjXzvQU3LqG%2Fttw7w2ccapqUzfKSpedCv%2F%0AtJBU9tgsMNPpzWR03Gv1KHHodX0%3D%0A)

4. Clique em **Habilitar integração;**

![Imagem 6: 4. Clique em Habilitar integração;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235816320/1348f2bccc26b36eb47519f548cc/AGQjJr7.png?expires=1786536000&signature=865d1ea20a1dd8fba08b03b6cf94a700383b3c116408662ccf87b8bba46fde21&req=dSIkE8F%2Fm4JdWfMW3nq%2BgUUo4TPPr62Harb6V7K7tgEbPn5sWjUOcwVurv1K%0AkvN4VGZQQO0hAzRksm6vwc3efDM%3D%0A)

5. Clique em **Autorizar Integração;**

![Imagem 7: 5. Clique em Autorizar Integração;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235816709/4fcf579958b80d96ef34b73bb10a/bzhoDlz.png?expires=1786536000&signature=7df0c5e4984d719cbf26590fb92e293d3e18aa31f58cec60c635cb67e050116b&req=dSIkE8F%2Fm4ZfUPMW3nq%2BgTYZcDlONH2AxKsyi3P1QSC%2BlbCDPWYZVtHg9Qwf%0AEVJlRybpTOsKIZt3Rn%2FcgkbRdXQ%3D%0A)

6. Em seguida, **insira o token de API no campo indicado e clique no botão Confirmar;**

![Imagem 8: 6. Em seguida, insira o token de API no campo indicado e clique no botão Confirmar;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235818042/212c2882abaf2d9850d0dffed1a9/Untitled.png?expires=1786536000&signature=04fa957acff438fca5f82022d8ec2304bd96bc07050fe605cd4eb0e5f5997cfb&req=dSIkE8F%2FlYFbW%2FMW3nq%2BgYjoEkDznHavCjVMNTmo6FLayBLZ9G6FAD92%2BmtQ%0ATrsOUb3%2FryBSpCd3PVA299Mk9NM%3D%0A)

7. Na sessão de configurações da Integração, ative a opção “**Caso o cliente não exista no Ploomes, deseja criá-lo quando um novo ticket chegar?”** se desejar automatizar a criação de clientes ao finalizar um ticket no Movidesk;

![Imagem 9: 7. Na sessão de configurações da Integração, ative a opção “ Caso o cliente não exista no Ploomes, deseja criá-lo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235818956/bfaf88babac910b2468d1f2c1276/T2JdIWL.png?expires=1786536000&signature=2969fc9f0e4e89f7847a8633f29f74108f3f0f4fcdcb6b9e20d970b6b217ce25&req=dSIkE8F%2FlYhaX%2FMW3nq%2BgdCkagWD2UvwLydVhFGrpa%2FL2aLU0N7C%2F6BkLGV8%0AEaafvP7rgcroAuqcFmN7n0I0uLI%3D%0A)

8. Configure o mapeamento dos campos.

![Imagem 10: 8. Configure o mapeamento dos campos.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235820145/ef77bc98f51eeaa43c620edb5bed/Untitled+%281%29.png?expires=1786536000&signature=ec26a55b74e8e0ef4c7240b45d52169a41114757689e9f7a876f7684d8db52e2&req=dSIkE8F8nYBbXPMW3nq%2BgXyRH7GBVHp8MENRGcIOXSRJwFl2q4R%2BV48zh44M%0AJofyiT1zh1QZxRahLUdWMPV5mk0%3D%0A)

9. Clique em **Ativar Integração**;

![Imagem 11: 9. Clique em Ativar Integração ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235822530/1000d8a08c14961d78bf54a5ca63/zmizKGo.png?expires=1786536000&signature=a9c61c650cfcc2d9990df26e27b1e67f1e7a44290ee286e11e2c90cb3494d8df&req=dSIkE8F8n4RcWfMW3nq%2BgfZzvUDWCfyillRFOzISFyV%2BzEcucY29AypTcECL%0AldHaobh8qPBvE4gE3mNqSIeKDo4%3D%0A)

10. Copie a url gerada;

![Imagem 12: 10. Copie a url gerada;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235822798/626c4f2020ea5c477a4bfaed9829/z1o4hmW.png?expires=1786536000&signature=37d883fa61d87a102b720af57013a88b8adf5b3a505844d215133b53b752fe79&req=dSIkE8F8n4ZWUfMW3nq%2BgafaKjzBh8G6hZZcA25i3HGm4NBf41dfGjRjtlXl%0AZnWK2NnWpjdrM06v8XqrQfb15Cw%3D%0A)

11. **De volta ao Movidesk,** para garantir que um webhook seja disparado para o Ploomes sempre que um ticket no Movidesk tiver o status alterado para "Resolvido", é necessário configurar os gatilhos. **Clique no ícone da engrenagem no canto inferior esquerdo e selecione Gatilhos;**

![Imagem 13: 11. De volta ao Movidesk, para garantir que um webhook seja disparado para o Ploomes sempre que um ticket no Movidesk…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235825302/5946c6109e455e4cdadc2a81bd01/0Cb2uf0.png?expires=1786536000&signature=286b66628910bc60f48c14d04c67fe2648bd4cc8869e8ecaf33c7a1b1bac76d3&req=dSIkE8F8mIJfW%2FMW3nq%2BgSUZU9dp6jyv8OmIs4B4ZuUTX4MCyI51I8tWxKXt%0A%2FV0onJ%2BhO88OeO9Gm3bALFEapMk%3D%0A)

12. Clique no ícone de **adição** para criar um gatilho;

![Imagem 14: 12. Clique no ícone de adição para criar um gatilho;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235826023/92c80b0fdc747132e64832274ec9/Untitled+%282%29.png?expires=1786536000&signature=821e495e765242754b2a742e65890da876e94ae20c8fa2e398860a68e4b56b0c&req=dSIkE8F8m4FdWvMW3nq%2BgYLBTtU08PoztbgzrcDbS8Gf%2B80lsFDFJcEyNc3U%0AiFZRrVPPFsqYyvsgG8f7xueZ0qc%3D%0A)

13. Adicione um nome ao gatilho;

![Imagem 15: 13. Adicione um nome ao gatilho;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235826267/6d1e170987522a037124dd6164fc/Untitled+%283%29.png?expires=1786536000&signature=a518c2380524d5c1a83c8c67b9f7224a96701c401ef8d81eea498f5125336f31&req=dSIkE8F8m4NZXvMW3nq%2Bge8%2FljFG7k9OC1%2F79EOFtno1pYcqMlHziTI93fdq%0Aj6Tf3YngiPnuzGYwsczyIyTzSYs%3D%0A)

14. Em “Gatilho para” selecione **Tickets**;

![Imagem 16: 14. Em “Gatilho para” selecione Tickets ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235826709/d42b7decf6efff9dc091f995437f/Untitled+%284%29.png?expires=1786536000&signature=0e3c7394152e4a6c5db86fcfe471f7d2a51815cec9abb383077775d460da2f76&req=dSIkE8F8m4ZfUPMW3nq%2BgSjjNmMKlPJzdRJ938wGqKlw9oiVfjIHdZ8hB%2BJL%0A5GqkieVifuX0XaUUSDrmF5U0AQE%3D%0A)

15. Em “Condições” adicione as seguintes opções:

- Se “**Ticket: Status**” → “**Alterado para**” → “**Resolvido”** . Isso envia os tickets que forem resolvidos;
- e “**Ticket: TAG**” → “**Diferente de**” → “**Enviado**”. Isso evita o envio de tickets duplicados ao Ploomes (Opcional);
- Se “**Ticket: Resolvido em**” → “**Igual a**” → “**Hoje**” . Isso envia os tickets que forem resolvidos na data em questão (Opcional).

![Imagem 17: Se “ Ticket: Resolvido em ” → “ Igual a ” → “ Hoje ” . Isso envia os tickets que forem resolvidos na data em questão…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235827364/b0d1dcc1253a03c3852f0a614592/Untitled+%285%29.png?expires=1786536000&signature=9d2f947888b1f3b0ee02477fbc474693631ec78776bc73b95e47d52065219fef&req=dSIkE8F8moJZXfMW3nq%2BgSTfz6%2FmvU2%2F8XdVXgX%2Boa3rPfKb%2BmV%2Bb104zqQ0%0AsZWmW%2FiN1f7rYrsR7RZkDcTWF4E%3D%0A)

16. Em “Ações” selecione **Acionar Webhook** e no campo “URL” cole a url obtida ao ativar a integração no Ploomes.

![Imagem 18: 16. Em “Ações” selecione Acionar Webhook e no campo “URL” cole a url obtida ao ativar a integração no Ploomes.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1235827801/e549bd7c02153fc10073fd685e58/Untitled+%286%29.png?expires=1786536000&signature=603b6b162217ac3f3d1cc14a790ae41469b24a0fb136417d9f84bd9ead8c9d86&req=dSIkE8F8molfWPMW3nq%2BgW6u%2BsKHtt%2BWWe6K%2FXzVQtpYkxQX95d19JYjTGpx%0A4qbKEEv9vam%2FTQ4ZVUiH7VgasMg%3D%0A)

Com isso, basta clicar em "Salvar" e pronto, sua integração já está pronta para uso.

## Todos os campos mapeáveis

![Imagem 19: Todos os campos mapeáveis](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1249267343/73f0a96422dfe69be797ce2136c7/https3A2F2Fprod-files-secure.png?expires=1786536000&signature=9cbfa58554a0405b41db68e73a5fe96c2c0b2b68445172e00da0c568b5cbd366&req=dSIjH8t4moJbWvMW3nq%2BgapRDq4%2FAUBxgumEUolNTdgPth0pZLdaTD1Zt4Pe%0AOZ7IGXCJPLIRtQLUVMet5IQE%2Bwo%3D%0A)

## Mapeamento de Contato → Pessoa

Este mapeamento integra as informações do cliente do tipo pessoa da Ploomes com a pessoa do Movidesk

| Campo (Movidesk) | Tipo do campo (Ploomes) | Descrição |
| --- | --- | --- |
| Código Referêncial Adicional | Texto Simples | Campo Cód. Ref. Adicional. Identificador não obrigatório, porém único da pessoa. (Alfanumérico) |
| Nome do Usuário | Texto Simples | Campo usuário. Deve ser único por domínio. Campo obrigatório quando for informado um domínio para autenticação diferente que o Movidesk. |
| Id do Superior | Texto Simples | Id (Cod. Ref.) existente do superior hierárquico da pessoa. |
| Nome do Superior(Somente leitura) | Texto Simples | Nome do superior hierárquico (somente leitura). |
| Classificação | Opções pré-cadastradas múltiplas | Classificação da pessoa. Se informada uma classificação inexistente, a mesma será criada. |
| Data de Criação | Data | Data da criação da pessoa. Deve ser menor ou igual a data atual. A data informada deve estar no formato UTC\*. Se o campo não for informado, será populado com a data atual. Somente leitura após a criação. |
| Data Ultima Alteração | Data | Data da ultima alteração da pessoa. Campo somente leitura. |
| Id da Pessoa que Alterou | Texto Simples | Cod. Ref. da pessoa que alterou pela ultima vez a pessoa consultada. Campo somente leitura. |
| Observações | Texto Multilinha | Observações. |

## Mapeamento de Cliente → Empresa

Este mapeamento integra as informações do cliente do tipo empresa da Ploomes com a empresa do Movidesk

| Campo (Movidesk) | Tipo do campo (Ploomes) | Descrição |
| --- | --- | --- |
| Código Referêncial Adicional | Texto Simples | Campo Cód. Ref. Adicional. Identificador não obrigatório, porém único da pessoa. (Alfanumérico) |
| Ramo da Atividade | Texto Simples | Campo Ramo de atividade para pessoa do tipo Empresa. |
| Nome do Usuário | Texto Simples | Campo usuário. Deve ser único por domínio. Campo obrigatório quando for informado um domínio para autenticação diferente que o Movidesk. |
| Id do Superior | Texto Simples | Id (Cod. Ref.) existente do superior hierárquico da pessoa. |
| Nome do Superior(Somente leitura) | Texto Simples | Nome do superior hierárquico (somente leitura). |
| Classificação | Opções pré-cadastradas múltiplas | Classificação da pessoa. Se informada uma classificação inexistente, a mesma será criada. |
| Data de Criação | Data | Data da criação da pessoa. Deve ser menor ou igual a data atual. A data informada deve estar no formato UTC\*. Se o campo não for informado, será populado com a data atual. Somente leitura após a criação. |
| Data Ultima Alteração | Data | Data da ultima alteração da pessoa. Campo somente leitura. |
| Id da Pessoa que Alterou | Texto Simples | Cod. Ref. da pessoa que alterou pela ultima vez a pessoa consultada. Campo somente leitura. |
| Observações | Texto Multilinha | Observações. |

## Mapeamento de Negócio → Ticket

Este mapeamento envia as informações do negócio da Ploomes para o ticket no Movidesk

| Campo (Movidesk) | Tipo do campo (Ploomes) | Descrição |
| --- | --- | --- |
| Id | Texto Simples | Número do ticket (somente leitura). |
| Protocolo | Texto Simples | Protocolo do ticket (somente leitura). \*Caso não utilizado será apresentado como null. |
| Assunto | Texto Simples | Assunto do ticket. |
| Categoria | Opções pré-cadastradas não múltiplas | Nome da categoria do ticket. Deve ser informada uma categoria existente e que esteja relacionada ao tipo e ao serviço (caso este esteja informado) do ticket. **Categorias**: Dúvida, Problema, Solicitação de Serviço, Sugestão. |
| Urgência | Opções pré-cadastradas não múltiplas | Nome da urgência do ticket. Deve ser informada uma urgência existente e que esteja relacionada a categoria (caso esta esteja informada no ticket). **Urgências**: Alta, Baixa, Média, Urgente |
| Status | Opções pré-cadastradas não múltiplas | Nome do status do ticket. Para alterar esse campo deve ser também informada a justificativa. O status deve ser um existente e que esteja relacionado ao tipo do ticket. \*Caso não informado, será utilizado o status base Novo padrão. **Status**: Aguardando, Cancelado, Em atendimento, Fechado, Novo, Resolvido |
| Base de Status | Texto Simples | Nome do status base do ticket (Somente leitura). |
| Justificativa | Opções pré-cadastradas não múltiplas | Nome da justificativa do ticket. Deve ser informada uma justificativa existente que esteja relacionada ao status do ticket. O preenchimento desse campo é obrigatório quando o status do ticket o exigir. Para alterar esse campo deve ser também informado o status. **Justificativas**: Aprovação de orçamento, Equipe de desenvolvimento, Liberação de versão, Retorno do cliente |
| Data de Criação | Data | Data de abertura do ticket. A data informada deve estar no formato UTC\*. \*Caso não for informada, será preenchida com a data atual. Somente leitura após a criação. |
| Conta de Email de Origem | Texto Simples | Conta de e-mail na qual o ticket foi recebido (Somente leitura). |
| Serviço Completo | Opções pré cadastradas múltiplas | Lista com os nomes dos níveis do serviço selecionado no ticket (Somente leitura). |
| Primeiro Nível do Serviço | Texto Simples | Nome do primeiro nível do serviço selecionado no ticket (Somente leitura). |
| Nome do serviço que esta selecionado no ticket. |  |  |
| Segundo Nível do Serviço | Texto Simples | Nome do segundo nível do serviço selecionado no ticket (Somente leitura). |
| Terceiro Nível do Serviço | Texto Simples | Nome do terceiro nível do serviço selecionado no ticket (Somente leitura). |
| Nome do serviço de primeiro nível. |  |  |
| Formulário de Contato | Texto Simples | Nome do formulário de contato através do qual o ticket foi aberto (Somente leitura). |
| Tags | Opções pré-cadastradas múltiplas | Lista de strings com as TAGs as quais o ticket esta relacionado. Caso sejam informadas TAGs inexistentes, as mesmas serão adicionadas na base de dados. |
| CC | Texto Multilinha | Relação dos e-mails informados no campo Cc, **separados por vírgula** (Somente leitura). |
| Resolvido em | Data | Data na qual o ticket foi indicado pelo agente como resolvido. A data informada deve estar no formato UTC. |
| Reaberto Em | Data | Data na qual o ticket teve a ultima reabertura (Somente leitura). |
| Fechado em | Data | Data na qual o ticket foi indicado como fechado. A data informada deve estar no formato UTC. |
| Data da Última Ação | Data | Data da última ação do ticket (Somente leitura). |
| Contagem de Ações | Número inteiro | Quantidade de ações do ticket (Somente leitura). |
| Última Atualização | Data | Data UTC da ultima alteração do ticket (Somente leitura). |
| Tempo de Vida do Projeto | Número inteiro | Tempo de vida do ticket em minutos em horas úteis desde a abertura (Somente leitura). |
| Tempo Parado | Número inteiro | Tempo que o ticket ficou no status parado em minutos em horas corridas (Somente leitura). |
| Tempo Parado do Projeto | Número inteiro | Tempo que o ticket ficou no status parado em minutos em horas úteis (Somente leitura). |
| Resolvido na Primeira Chamada | Checkbox | Indicador que representa se o ticket foi resolvido já no momento da abertura ou num momento posterior (Somente leitura). |
| Ferramenta de Chat | Texto Simples | Aplicativo de chat através do qual o ticket foi aberto (Somente leitura). |
| Grupo de Chat | Texto Simples | Grupo de chat através do qual o ticket foi aberto (Somente leitura). |
| Tempo Falado em Chat | Número inteiro | Tempo de duração do chat em segundos (Somente leitura). |
| Tempo de Espera no Chat | Número inteiro | Tempo que o cliente ficou aguardando para ser atendido em segundos (Somente leitura). |
| Sequência | Número inteiro | Número inteiro armazenado no campo Sequência. |
| Acordo de Sla | Texto Simples | Contrato SLA utilizado no ticket (Somente leitura). |
| Acordo de Regra de Sla | Texto Simples | Regra do contrato SLA (Somente leitura). |
| Tempo de Solução Sla | Número inteiro | Tempo de solução do contrato SLA (Somente leitura). |
| Tempo de Resposta Sla | Número inteiro | Tempo de resposta do contrato SLA (Somente leitura). |
| Solução de Sla Alterada Pelo Usuário | Checkbox | Indica se o contrato SLA foi manualmente alterado pelo usuário (Somente leitura). |
| Data da Solução Sla | Data | Data de solução do SLA. Caso informado, será considerado que o SLA foi manualmente alterado pelo usuário que criou a ação. A data informada deve estar no formato UTC. |
| Data de Solução Sla está pausada | Checkbox | Indica se a data de solução do SLA está pausada (Somente leitura). |
| Data de Resposta Sla | Data | Data de resposta do SLA (Somente leitura). |
| Real Data de Resposta Sla | Data | Data UTC real da resposta do SLA (Somente leitura). |
| Chave de problema de Jira | Texto Simples | Chave da issue do Jira Software que está associada ao ticket por integração (Somente leitura). |
| Id do Problema da Redmine | Número inteiro | ID da issue do Redmine que está associada ao ticket por integração (Somente leitura). |
| [Ações.Id](http://xn--Aes-2la4e.Id) | Número inteiro | Id (Número da ação) (Somente leitura). \*Deve ser informado quando necessário alterar a ação já existente. |
| Ações.Descrição | Texto Simples | Descrição da ação. Em operações de escrita, esse campo será interpretado como HTML e deve ser corretamente formatado para ser apresentado normalmente na tela de tickets. Em operações de leitura, esse campo é somente texto. |
| Ações.HTML de Descrição | Texto Multilinha | Descrição da ação em formato HTML (Somente leitura). \*Esse campo só é retornado quando a busca é feita por ID do Ticket. Na listagem de Tickets ele não será retornado. Para retornar o HTML, deve-se utilizar o endpoint /tickets/htmldescription. |
| Ações.Status | Texto Simples | Status da ação (Somente leitura). |
| Ações.Justificação | Texto Simples | Justificativa da ação (Somente leitura). |
| Ações.Data de criação | Data | Data de criação da ação. A data informada deve estar no formato UTC. \*Caso não informada, será preenchida com a data atual. |
| Ações.Está Excluído | Checkbox | Verdadeiro se a ação foi deletada (Somente leitura). |
| Ações.Tags | Opções pré-cadastradas não múltiplas | Lista de strings com as TAGs as quais a ação esta relacionada. Caso sejam informadas TAGs inexistentes, as mesmas serão adicionadas na base de dados. |
| Ticket [Pai.Id](http://Pai.Id) | Número inteiro | Id (Número) do ticket. |
| Ticket Pai.Assunto | Texto Simples | Assunto do ticket (Somente leitura). |
| Ticket Pai.Está Excluído | Checkbox | Verdadeiro se foi deletado (Somente leitura). |
| Ticket [Filho.Id](http://Filho.Id) | Número inteiro | Id (Número) do ticket. |
| Ticket Filho.Assunto | Texto Simples | Assunto do ticket (Somente leitura). |
| Ticket Filho.Está Excluído | Checkbox | Verdadeiro se foi deletado (Somente leitura). |
| Históricos de responsabilidades.Time Responsável | Texto Simples | Equipe do responsável pelo ticket (Somente leitura). |
| Históricos de responsabilidades.Tempo Total de Permanência | Número com casas decimais ilimitadas | Tempo de permanência do responsável pelo ticket em segundos. (Somente leitura). |
| Históricos de responsabilidades.Tempo Total de Permanência Trabalhado | Número com casas decimais ilimitadas | Tempo útil de permanência do responsável pelo ticket em segundos. (Somente leitura). |
| Históricos de responsabilidades.Data de Alteração | Data | Data UTC que o responsável pelo ticket foi alterado (Somente leitura). |
| Históricos de status.Status | Texto Simples | Status do ticket (Somente leitura). |
| Históricos de status.Justificativa | Texto Simples | Justificativa do ticket (Somente leitura). |
| Históricos de status.Tempo Total de Permanência | Número com casas decimais ilimitadas | Tempo de permanência do status do ticket em segundos. (Somente leitura). |
| Históricos de status.Permanência de Tempo Trabalhado | Número com casas decimais ilimitadas | Tempo útil de permanência do status do ticket em segundos. (Somente leitura). |
| Históricos de status.Data de Alteração | Data | Data UTC que o status do ticket foi alterado (Somente leitura). |
| Respostas de [Satisfação.Id](http://xn--Satisfao-xza3b.Id) | Número Inteiro | Id (Código) da resposta de satisfação (Somente leitura). |
| Respostas de Satisfação.Data da Resposta | Data | Data UTC da resposta. |
| Respostas de Satisfação.Modelo de Pontuação da Resposta | Número inteiro | Modelo de pontuação da resposta: 1 = Positivo/Negativo, 2 = Faces sorridentes, 3 = NPS (Somente leitura). |
| Respostas de Satisfação.NPS | Número inteiro | Pontuação de 0 a 10 (NPS). \*Obrigatório dependendo da escolha do satisfactionSurveyModel. |
| Respostas de Satisfação.Positivas ou Negativas | Número inteiro | Pontuação: 1 = Positivo e 2 = Negativo. \*Obrigatório dependendo da escolha do satisfactionSurveyModel. |
| Respostas de Satisfação.Pontuação Face | Número inteiro | Pontuação faces sorridentes: 1 = Muito insatisfeito, 2 = Insatisfeito, 3 = Neutro, 4 = Satisfeito, 5 = Muito satisfeito. \*Obrigatório dependendo da escolha do satisfactionSurveyModel. |
| Respostas de Satisfação.Comentários | Texto Multilinha | Comentários. |
