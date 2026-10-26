---
id: "42426585997847"
titulo: "Eventos da Manifestação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426585997847-Eventos-da-Manifesta%C3%A7%C3%A3o"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Oráculo"
atualizado_em: "2026-08-03T12:24:58Z"
rotulos: ["asis", "sync_hc", "asis_52941198287123", "sync_hash_3a882e25eab4"]
---

# Eventos da Manifestação

**Evento de “Confirmação da Operação”**

O evento de “Confirmação da Operação” pelo destinatário confirma a operação e o recebimento
da mercadoria (para as operações com circulação de mercadoria). Se ocorrer a devolução total ou parcial das mercadorias, além do procedimento atual de geração da Nota Fiscal de devolução, também poderá ser comandado o evento da “Confirmação da operação”.
O registro deste evento libera a possibilidade da empresa efetuar o download da NF-e.

Nota: Após a Confirmação da Operação pelo destinatário, a empresa emitente fica automaticamente impedida de cancelar a NF-e.

**Evento de “Desconhecimento da Operação”**

O evento de “Desconhecimento da Operação” permite ao destinatário informar o seu desconhecimento de uma determinada operação.

**Evento de “Operação não Realizada”**

Em algumas situações, a empresa destinatária informa que a operação não foi realizada (com
recusa de recebimento da mercadoria e outros motivos), não cabendo neste caso a emissão de
uma Nota Fiscal de devolução.
Este evento permite o registro da declaração de Operação não Realizada pelo destinatário,
permitindo também a informação complementar da justificativa desta informação.

**Evento de “Ciência da Operação ou Ciência da Emissão”**

Neste evento, o destinatário declara ter ciência sobre uma determinada operação destinada ao seu CNPJ ou CPF, mas não possui elementos suficientes para apresentar a sua manifestação conclusiva sobre a operação citada.
O evento de “Ciência da Operação” é um evento opcional e pode ser evitado, já que normalmente o destinatário da NF-e deve possuir o arquivo XML da NF-e enviado e/ou disponibilizado pelo emitente. Após um período determinado, todas as operações com “Ciência da Operação” deverão obrigatoriamente ter a manifestação final do destinatário declarada em um dos eventos de Confirmação da Operação, Desconhecimento ou Operação não Realizada.

**Sobre a mudança da Manifestação do Destinatário**

O destinatário poderá enviar uma única mensagem de Confirmação da Operação, Desconhecimento da Operação ou Operação não Realizada, valendo apenas a última mensagem registrada.

Exemplo: o destinatário pode desconhecer uma operação que havia confirmado inicialmente ou confirmar uma operação que havia desconhecido inicialmente.
O evento de “Ciência da Operação” não configura a manifestação final do destinatário, portanto
não cabe o registro deste evento após a manifestação final do destinatário.
O destinatário deve apresentar uma manifestação conclusiva dentro de um prazo máximo definido,
contados a partir da data de autorização da NF-e. Este prazo é parametrizável e atualmente está
definido em 180 dias.
