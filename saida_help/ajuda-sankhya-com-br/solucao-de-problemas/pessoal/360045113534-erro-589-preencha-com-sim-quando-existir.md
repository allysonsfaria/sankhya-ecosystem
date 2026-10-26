---
id: "360045113534"
titulo: "Erro 589 - Preencha com Sim quando existir informação de pagamento de rendimento do trabalho no período e Não quando não existir. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113534-Erro-589-Preencha-com-Sim-quando-existir-informa%C3%A7%C3%A3o-de-pagamento-de-rendimento-do-trabalho-no-per%C3%ADodo-e-N%C3%A3o-quando-n%C3%A3o-existir-Como-resolver"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-16T12:02:35Z"
rotulos: ["#criadoRoger", "Eventos", "Folha", "#textmining", "#AGUARDANDOVALIDAÇÃO", "eSocial", "Preenchimento incorreto de pagamento", "Evento S-1210 enviado por outro sistema", "Consultor transfere recibos ou regenerar totalizadores", "Erro", "Central de Projetos"]
---

# Erro 589 - Preencha com Sim quando existir informação de pagamento de rendimento do trabalho no período e Não quando não existir. Como resolver?

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18610880683799) MENSAGEM**:

Erro 589 - Preencha com Sim quando existir informação de pagamento de rendimento do trabalho no período e Não quando não existir.
Elemento: /eSocial/evtFechaEvPer/infoFech/evtPgtos
[N]

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18610925762839) CAUSA**:

Ao tentar transmitir o evento S-1299 apresenta a mensagem, quando o evento S-1210 foi transmitido em um sistema posterior. Necessitando intervenção de um consultor da Unidade para acertos.

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/18610925764759) SOLUÇÃO**

Verifique o comportamento da aplicação:

**1º Cenário:** Se o evento S-1210 foi enviado de outro sistema, e estiver tentando transmitir o fechamento pelo sistema atual, apresentara a mensagem, melhor prática sera o acompanhamento de um consultor para que possa trazer os números dos recibos dos eventos transmitidos no antigo sistema para o atual(Sankhya).

**2º Cenário:** Pode ocorrer de perder a sequência dos eventos, onde pode ser constatado que na aba: Totalizadores os envios são zerados. Nessa situação, devera realizar uma nova geração, posteriormente verificar se a na aba Totalizadores ira alimentar corretamente, e por fim realizar o fechamento.
