---
id: "360043116433"
titulo: " Não foi possível cancelar a nota pois a mesma está vincula a um MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043116433--N%C3%A3o-foi-poss%C3%ADvel-cancelar-a-nota-pois-a-mesma-est%C3%A1-vincula-a-um-MDF-e"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:47Z"
rotulos: ["ERRONF", "MDF-e", "CT-e", "Eventos", "NF-e", "SEFAZ", "690", "Impedimento de cancelamento: NF-e MDF-e rejeição", "Procedimento de consulta: SEFAZ validação MDF-e", "Causa do problema: Vínculo CT-e registro", "Documentos Eletrônicos", "Rejeição SEFAZ"]
---

#  Não foi possível cancelar a nota pois a mesma está vincula a um MDF-e

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16504601258007) **MENSAGEM:**

Não foi possível cancelar a nota pois a mesma está vincula a um MDF-e.

[690 - Rejeição]: Pedido de cancelamento para NF-e com CT-e ou MDF-e

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16504601260439) SOLUÇÃO:**

![Imagem 3: Realize a consulta da chave NF-e da nota a ser cancelada na SEFAZ e valide a existência de MDF-e conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16504614991639) Realize a consulta da chave NF-e da nota a ser cancelada na SEFAZ e valide a existência de MDF-e conforme abaixo:

![Imagem 4: Realize a consulta da chave NF-e da nota a ser cancelada na SEFAZ e valide a existência de MDF-e conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360059967694)

Consulta: <http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=completa&tipoConteudo=XbSeqxE8pl8=>

![Imagem 5: O cancelamento dessa NF-e só será permitido após cancelamento dos eventos apresentados acima (CT-e/ MDF-e).](https://ajuda.sankhya.com.br/hc/article_attachments/16504601265303) O cancelamento dessa NF-e só será permitido após cancelamento dos eventos apresentados acima (CT-e/ MDF-e).

- O cancelamento do evento é realizado pela empresa emissora do Evento.
- Busque orientações com a Equipe Fiscal da empresa para o ato de se cancelar a CT-e ou MDF-e, pois poderá ocorrer de algum desses documentos já ter registrado eventos em barreiras fiscais.
- Caso o cancelamento de tais eventos não seja mais possível, o seu contador deverá lhe orientar na melhor solução. Visto que trata-se de um impedimento da SEFAZ, e não do sistema.

Realizados os respectivos cancelamentos, seus eventos também serão registrados junto à SEFAZ. Feito isso, o cancelamento da NF-e poderá ser realizado.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16504614993943) CAUSA:**

Uma NF-e pode estar referenciada em diferentes CT-es ou MDF-es, nos Grupos de documentos referenciados deste modelos. Quando uma NF-e está vinculada a um CT-e ou MDF-e, esta não poderá ser cancelada. Caso o emitente da NF-e tente registar um evento de cancelamento, quando há um vinculo desta com um CT-e ou MDF-e a Sefaz retornará a rejeição.
