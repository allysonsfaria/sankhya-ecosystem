---
id: "7215349603223"
titulo: "Acompanhamento de boletos - API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7215349603223-Acompanhamento-de-boletos-API"
trilha: "Manual do Produto > Financeiro e Patrimônio > Sankhya Fintech > Banking"
atualizado_em: "2026-09-08T19:49:32Z"
rotulos: ["Contas", "Movimentação Financeira", "Boleto", "Financeiro", "br.com.sankhya.acompanhamento.boleto.api", "Acompanhamento de Boletos - API", "API", "Registros de boletos API", "Filtros e status boletos", "Histórico e status eventos"]
---

# Acompanhamento de boletos - API

| ```  Módulo: Financeiro > Consultas             Versão disponível: A partir da 4.18 ``` |
| --- |

---

Serão apresentados nesta tela os registros dos boletos gerados pela API do banco. Desse modo, você poderá obter informações do boleto, como, por exemplo, sua emissão, alteração, cancelamento, entre outros.

![Imagem 1: Esta tela será disponibilizada automaticamente aos usuários que possuem permissão de acesso às telas Geração Arquivo de…](https://ajuda.sankhya.com.br/hc/article_attachments/31340551282967) Esta tela será disponibilizada automaticamente aos usuários que possuem permissão de acesso às telas **Geração Arquivo de Remessa**, **Processamento do Arquivo de Retorno** ou **Contas**. Além disso, o usuário, com essa permissão, poderá conceder aos demais usuários o acesso a esta tela normalmente.

---

| ![Imagem 2: Para saber como gerar os boletos via API do banco em nossa solução, acesse o artigo Boleto rápido API .](https://ajuda.sankhya.com.br/hc/article_attachments/42309666755095) Para saber como gerar os boletos via API do banco em nossa solução, acesse o artigo [Boleto rápido API](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559). |
| --- |

---

![Imagem 3: Para saber como gerar os boletos via API do banco em nossa solução, acesse o artigo Boleto rápido API .](https://ajuda.sankhya.com.br/hc/article_attachments/7218614642711)

Você pode conferir os registros dos boletos de forma mais rápida, para isso, configure os filtros na parte esquerda da tela.

Inicialmente no campo **"Status do Boleto"**, acione o tipo de busca dos registros dos boletos, conforme as alternativas abaixo:

- abertos;
- agendados;
- cancelados;
- liquidados;
- protestado;
- não registrados.

Ao acionar a marcação **"Não registrados"**, serão apresentados os boletos gerados no **Sankhya Om**, mas que não foram registrados no banco.

Além disso, é possível que você filtre os boletos considerando o **"Nro Único"**, o **"Nro Nota"**, o **"Nosso Número"**, **"Parceiro"**, a **"Data de Vencimento"** e a **"Data de Emissão"**.

Pode-se também realizar a busca dos boletos adicionando o banco e/ou a conta bancária na seção **"Banco"** e **"Conta Bancária"**, respectivamente.

Feito isso, clique em **"Aplicar"** para que os registros sejam exibidos no painel.

---

### Grade Boletos

Com as configurações acima realizadas, na grade **Boletos** serão exibidos os seguintes dados do boleto:

| - Nro. Único - Nro. Nota - Nosso Número - Data Vencimento Boleto - Data de Emissão (data de registro do boleto) - Vlr. do Desdobramento | - Status no Banco - Parceiro (cod.parceiro) - Nome Parceiro - Data Baixa - Empresa (cod. empresa) - Nome Fantasia |
| --- | --- |

---

### Histórico do Boleto

Ao selecionar um registro na grade **Boletos**, na grade inferior você poderá verificar as informações sobre o **Histórico do Boleto**, por meio dos campos abaixo.

[GIF animado: Imagem 4: Ao selecionar um registro na grade Boletos , na grade inferior você poderá verificar as informações sobre o Histórico…](https://ajuda.sankhya.com.br/hc/article_attachments/7272998572439)

No campo **"Tipo Evento"** analise qual o tipo de evento do boleto, isto é:

- emissão;
- alteração;
- baixa/cancelamento;
- retorno recebido do banco;

Verifique no campo **"Data Evento"** a data e o horário que foi realizado o evento.

No campo **"Descrição do Evento"** você pode conferir o detalhamento do evento, por exemplo:

- emissão de boleto enviada para o banco;
- alteração de boleto enviada para o banco;
- baixa/cancelamento de boleto enviada para o banco;
- retorno recebido do banco.

Por meio do campo **"Situação"** é exibido o status da solicitação, podendo ser:

- **processada:** a solicitação foi processada pelo banco com sucesso.
- **pendente de envio:** a solicitação está pendente de envio para o banco. Abaixo temos alguns exemplos de situações em que um evento poderá ficar **Pendente de Envio**:

  - solicitação de alteração ou cancelamento do boleto que foi registrado com menos de 30 minutos;
  - erro de comunicação com API;
  - job de envio não foi executado.
- **rejeitada:** a solicitação não foi acatada pelo banco.

No campo **"Retorno do Banco"** você pode verificar o status de retorno obtido pelo banco, como, por exemplo:

- status 200: Executado com sucesso;
- status 201: Criado com sucesso;
- status 404: Requisição não encontrada;
- status 500: Erro interno do Servidor.

Você também pode conferir por meio do campo **"Status do Boleto"** a situação do boleto. Na imagem abaixo confira as classificações dos status dos boletos:

![Imagem 5: Você também pode conferir por meio do campo "Status do Boleto" a situação do boleto. Na imagem abaixo confira as…](https://ajuda.sankhya.com.br/hc/article_attachments/7235025819031)

> **Observação**: Esta tela permite verificar se o boleto foi liquidado, mas não necessariamente como o pagamento foi feito (PIX ou código de barras). Essa informação depende do retorno enviado pelo banco: alguns bancos informam apenas que o título foi pago, sem especificar a forma de pagamento.

---

### Tabela Histórico de Boleto API - TGFHBA

Para acompanhar o histórico dos boletos API, temos a tabela TGFHBA. A seguir, conheça as siglas desta tabela:

**Status do título (STATUS):**

- **A - Aguardando envio:** ainda não foi enviado para a API;
- **E - Enviada:** já foi enviada para a API e para o banco;
- **B - Baixada:** financeiro foi baixado no sistema (pago);
- **P - Processada:** já foi enviado para a API, porém, ainda não consultou o status para o banco;
- **R - Renegociada:** foi renegociado no sistema;
- **X- Título Excluído:** foi excluído do sistema.

**Status de envio para o banco (STATUSENVIO):**

- **A - Aguardando envio:** ainda não foi enviado para a API;
- **P - Processada:** já foi enviado para a API, no entanto, ainda não consultou o status para o banco;
- **E - Enviada:** já foi enviada para a API e para o banco.

**Status que o título se encontra no banco (STATUSBANC):**

- 0 - Ainda não registrado;
- 1 - Normal;
- 2 - Movimento cartório;
- 3 - Em cartório;
- 4 - Titulo com ocorrência cartório;
- 5 - Protestado eletrônico;
- 6 - Liquidado;
- 7 - Baixado pelo banco;
- 8 - Titulo com pendência no cartório;
- 9 - Titulo protestado manualmente;
- 10 - Titulo baixado pago em cartório;
- 11 - Titulo liquidado protestado;
- 12 - Titulo liquidado em cartório;
- 13 - Titulo protestado aguardando baixa;
- 14 - Titulo em liquidação;
- 15 - Titulo agendado bb;
- 16 - Titulo creditado;
- 17 - Pago em cheque aguardando liquidação;
- 18 - Pago parcialmente;
- 19 - Pago parcialmente creditado;
- 21 - Titulo agendado outros bancos.

**Tipo de envio (TIPOENVIO):**

- A - Alteração;
- B - Baixa;
- E - Entrada;
- X - Exclusão.
