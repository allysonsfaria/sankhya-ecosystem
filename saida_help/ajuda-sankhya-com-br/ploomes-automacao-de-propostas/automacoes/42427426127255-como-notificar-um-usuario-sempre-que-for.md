---
id: "42427426127255"
titulo: "Como notificar um usuário sempre que for criado um cliente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427426127255-Como-notificar-um-usu%C3%A1rio-sempre-que-for-criado-um-cliente"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:43Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452248", "sync_hash_7ede5e592dbf"]
---

# Como notificar um usuário sempre que for criado um cliente?

Notificar a equipe sempre que um novo cliente é criado é essencial para garantir agilidade no atendimento. Com as automações do Ploomes, é possível enviar alertas automáticos e manter todos os envolvidos informados em tempo real.

## Configuração

## 1. Acessar as automações de Cliente

- Acesse **Administração > Automações**.
- Selecione a entidade **Cliente**.
- Clique em **Nova automação**.

[GIF animado: Imagem 1: Clique em Nova automação .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221182335/02008598c20ce5da705302b2d085/msedge_g0pEIpQc1P.gif?expires=1786536000&signature=b13ed3bfee7330bd26b1ed93bd381e03473326e9b6ffd7526f53a37a330fcf73&req=diIlF8h2n4JcXPMW3nq%2BgU2U44u4hyGkw4N1WGI1T7GiMVURdNBBcCOS%2Brxt%0Ao3ShwLD%2B%2FpB7dQx23BukvIcFnyY%3D%0A)

## 2. Definir a automação

- Na Descrição, informe o objetivo da automação.
  Ex.: Alertar responsável após criação do cliente.
- No **gatilho**, selecione **Quando o item for criado**.

[GIF animado: Imagem 2: No gatilho , selecione Quando o item for criado .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221183491/ee7fc61a0a98665a134ff17ccf13/msedge_py5emN03fa.gif?expires=1786536000&signature=5917cf64881350de60a1da186b98269ea0a1b88c6a220ffad3b3a88236575c34&req=diIlF8h2noVWWPMW3nq%2BgUswyZ0w9%2BatRTU%2FI18aJDJ7Ik6dndrNC%2BntiqSZ%0AxYNDMH5sOz0qkZ49Asfy4cMs9cY%3D%0A)

## 3. (Opcional) Configurar o filtro

Caso queira restringir quais clientes irão disparar a automação, adicione um filtro.

Exemplo:

- Tipo do cliente = Empresa

[GIF animado: Imagem 3: Tipo do cliente = Empresa](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221184916/78e56989d565112864e8100297ad/msedge_vqa25X44J1.gif?expires=1786536000&signature=52242a1ec9e6d0eee7275b5e97bcb746c2589420dd2ec3411ef7d5bd17df8ec2&req=diIlF8h2mYheX%2FMW3nq%2BgaeLYV5bhF%2BW0QFE%2FUA9tP00MQzRgdX%2FZqpiVcu7%0AGIRYTDuYF6Jr%2BLpIDQny%2F1fkmao%3D%0A)

Se nenhum filtro for configurado, a automação será executada para todos os clientes criados.

## 4. Criar o campo para armazenar o link do cliente

Antes de configurar o envio do e-mail, é necessário criar um campo que armazenará a URL de acesso ao cliente.

- Em **Ao ser disparada, o que a automação deve fazer?**, adicione uma ação **Editar dados**.
- Clique em **Criação rápida** e crie um campo:

  - Nome: URL do cliente
  - **Tipo: Texto simples**

[GIF animado: Imagem 4: Tipo: Texto simples](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221189854/6c43e4d940dca181ba557f2900c1/msedge_vqPNZduJJz.gif?expires=1786536000&signature=29e546b38f8e2e817b408d3fdc3629c7409a280717baa3fb933feaae89594d49&req=diIlF8h2lIlaXfMW3nq%2BgffNtLfglLNmf03W1FX1AeMh38n3VZ%2FCs4Hpqxd8%0ALjW2fgiBelGSwof%2BI60hL3kaTKc%3D%0A)

## 5. Preencher o campo com a URL via fórmula

- No campo criado, altere o tipo de preenchimento para **Fórmula**.
- Insira a fórmula abaixo responsável por gerar o link do cliente (conforme disponibilizado).
- **Certifique-se de que a variável Cliente.Id está inserida**. Caso não esteja, basta apagar o texto [Cliente.Id] na fórmula e inserir novamente o campo pelo botão **Campos**.
- Salve a fórmula.

[GIF animado: Imagem 5: Salve a fórmula.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221210926/8eb96fef86bddcfb739caa3209da/msedge_glygC8T4PH.gif?expires=1786536000&signature=1fbfbc8669717b10f0f0bb1ae96ea9ac7fb0e62d85205c214f873d46dd97fca9&req=diIlF8t%2FnYhdX%2FMW3nq%2BgX2OiBe5tTlI6QpJZGfzFWyxIZ4Jw%2B46yaU2Z%2BEv%0A%2FIjWRtfCzeNnqvFOIOEnFyNBLjI%3D%0A)

**Fórmula**

(function () {

return "<a href='<https://app10.ploomes.com/contact/>" + "[Cliente.Id]" + "'>URL do Negocio</a>";

})();

Essa etapa permitirá utilizar o link diretamente no corpo do e-mail como atalho para acessar o cliente.

## 6. Configurar o envio de e-mail

Adicione uma nova ação:

- Selecione **Enviar e-mail**.

Preencha os campos:

- **Tipo de remetente**:
  Ex.: E-mail automático
- **Usuário para ser avisado em caso de falha**:
  Selecione um usuário (ex.: seu próprio usuário)
- **Destinatário (campo de e-mail)**:
  Selecione o campo **E-mail do responsável do cliente**

[GIF animado: Imagem 6: Destinatário (campo de e-mail) : Selecione o campo E-mail do responsável do cliente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221215886/57c93489bc3b5b6e2b0f782d4df7/msedge_Psp92EP063.gif?expires=1786536000&signature=2954e71b156ae86770ba9cb1574efa942dbad3d7996f297781d94fbc11b1abb0&req=diIlF8t%2FmIlXX%2FMW3nq%2BgfzWeF0W5V69l0mmuwXVb3l3ZZ0yUdCorzTmuz4Q%0Ajf6tBJJYPBcmKXXZa3gUU3WTasw%3D%0A)

## 7. Definir assunto e corpo do e-mail

- Defina o assunto:
  Ex.: Alerta de criação de novo cliente
- Preencha o corpo do e-mail (exemplo):

Olá, [Cliente.Responsável],
O cliente [Cliente.Nome] foi criado!
Acesse por aqui: [Cliente.URL do cliente]

- Em seguida, salve a automação

[GIF animado: Imagem 7: Em seguida, salve a automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221224557/23cf69cab5e895a4d5c8c26d09be/msedge_uYMNTHQ1Qy.gif?expires=1786536000&signature=1d5f53548dba49dcc1cf80689095800a413ff000d73625906c67025fdfdf9fb9&req=diIlF8t8mYRaXvMW3nq%2Bgd%2BYBWriXBAIUslu8N7i%2FpBYiq3awgJQy7aBfnTC%0A7TcWa24jGdU8u29M%2B9e%2BUcVm5mU%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
