---
id: "26425057889303"
titulo: "MS1353-Não é permitido o envio de mais de um evento num mesmo período de apuração, mesmo estabelecimento, mesmo número de CNPJ do beneficiário..."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26425057889303-MS1353-N%C3%A3o-%C3%A9-permitido-o-envio-de-mais-de-um-evento-num-mesmo-per%C3%ADodo-de-apura%C3%A7%C3%A3o-mesmo-estabelecimento-mesmo-n%C3%BAmero-de-CNPJ-do-benefici%C3%A1rio"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:42:09Z"
rotulos: ["Eventos", "Parceiro", "XML", "eSocial", "Central do eSocial", "Não é permitido o envio de mais de um evento num mesmo período de apuração", "mesmo estabelecimento mesmo número de CNPJ do beneficiário", "exceto se for para retificação de evento enviado anteriormente", "mesmo identificador de evento adicional (ideEvtAdic)", "Erro"]
---

# MS1353-Não é permitido o envio de mais de um evento num mesmo período de apuração, mesmo estabelecimento, mesmo número de CNPJ do beneficiário...

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/26439121371543) MENSAGEM:**

MS1353 - Não é permitido o envio de mais de um evento num mesmo período de apuração, mesmo estabelecimento, mesmo número de CNPJ do beneficiário e mesmo identificador de evento adicional (ideEvtAdic), exceto se for para retificação de evento enviado anteriormente.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26439158039447) SOLUÇÃO:**

Deve ser analisado se o registo que já consta no e-CAC foi enviado manualmente por algum agente que possui o acesso. Pois, se é a primeira transmissão pelo sistema, essa é a possibilidade que mais acontece no dia a dia. Sendo essa a questão, verifique com os responsáveis se o melhor será excluir o que já consta no e-CAC e reenviar pelo nosso sistema ERP, assim pode-se manter todo o controle pela aplicação, garantido a integridade dos dados.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26439158043799)CAUSA:**

Ao "enviar" os eventos do REINF o retorno do e-CAC é uma rejeição, com a mensagem supracitada. Essa mensagem quer dizer que já existe no e-CAC um registro para o **Parceiro** do **Evento** (grupo 2000 e 4000) em questão, para a empresa e referência que está sendo enviada no momento, causando assim uma duplicidade de envio.
