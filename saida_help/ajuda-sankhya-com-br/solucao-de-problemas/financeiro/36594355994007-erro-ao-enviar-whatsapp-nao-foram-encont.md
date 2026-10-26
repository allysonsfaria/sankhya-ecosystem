---
id: "36594355994007"
titulo: "Erro ao enviar whatsapp. Não foram encontrados dados de destinatário para o respectivo título"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36594355994007-Erro-ao-enviar-whatsapp-N%C3%A3o-foram-encontrados-dados-de-destinat%C3%A1rio-para-o-respectivo-t%C3%ADtulo"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:22:44Z"
rotulos: ["Configuração", "Parceiro", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Whatsapp", "Contato do Parceiro", "Régua de Cobrança", "Responsável pela cobrança"]
---

# Erro ao enviar whatsapp. Não foram encontrados dados de destinatário para o respectivo título

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/36594355981719) **MENSAGEM:**

Erro ao enviar whatsapp. Não foram encontrados dados de destinatário para o respectivo título.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/36594350779671)SOLUÇÃO:**

**(1)** Acesse a tela [''**Régua de Cobrança''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602534-R%C3%A9gua-de-Cobran%C3%A7a) (Financeiro » Cobrança » Régua de Cobrança).

**(2)** Verifique para quem o envio está configurado: **Parceiro** ou **Contato do Parceiro**.

  Essa verificação é essencial, pois **determina onde o número** de celular **deve estar cadastrado**.

**(3)** Quando o **envio** for **destinado a um parceiro,** acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(4)** Na aba **''Endereço''**, certifique-se de que o campo **''Celular/Fax''** está preenchido com o número de celular do parceiro (**incluindo o DDD**). Esse preechimento é obrigatório para que o WhatsApp seja enviado corretamente.

![Imagem 3: (4) Na aba ''Endereço'' , certifique-se de que o campo ''Celular/Fax'' está preenchido com o número de celular do…](https://ajuda.sankhya.com.br/hc/article_attachments/36594355982487)

**(5)** Quando o **envio** for **destinado a um contato específico do parceiro,** ainda na tela **''Parceiros''** acesse a aba **''Contatos''**.

**(6)** Verifique quais contatos estão configurados para receber cobranças, e, para cada um deles, certifique-se de que:

- O campo **“Celular”** está preenchido com um número válido.
- Na aba ''**Geral''**, a opção **“Responsável pela cobrança”** está habilitada.

**(7)** Somente com essas informações preenchidas o sistema conseguirá realizar o envio do WhatsApp de forma correta.

![Imagem 4: (7) Somente com essas informações preenchidas o sistema conseguirá realizar o envio do WhatsApp de forma correta.](https://ajuda.sankhya.com.br/hc/article_attachments/36594350781207)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/36594350781463)CAUSA:**

O erro ocorre porque a Régua de Cobrança tenta executar o evento **“Envio de WhatsApp”**, porém **não há número** de celular **cadastrado** nos campos obrigatórios do **parceiro** ou do **contato responsável pela cobrança**.

Sem essa informação, o sistema não consegue completar o envio.
