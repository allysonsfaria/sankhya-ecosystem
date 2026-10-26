---
id: "44012904026263"
titulo: "[Tracking] - Como enviar uma reentrega ao Roteirizador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012904026263--Tracking-Como-enviar-uma-reentrega-ao-Roteirizador"
trilha: "Lincros > Tracking > Monitoramento - Tracking"
atualizado_em: "2026-10-05T19:41:42Z"
rotulos: ["sync_hc", "lincros", "lincros_13433155", "sync_hash_b6a1b792ea7f"]
---

# [Tracking] - Como enviar uma reentrega ao Roteirizador

**Menu**: Tracking> Monitoramento> Tratar devolução> Reentrega;

**Objetivo**: Explicar o fluxo para uma devolução tratada no Tracking como reentrega enviar ao Roteirizador um pedido de reentrega.

**Considerações**: Com o Tracking, é possível tratar uma devolução como '**Reentrega**'. Se o cliente estiver utilizando tanto o Tracking quanto o Roteirizador, pode comunicar o pedido de reentrega diretamente ao Roteirizador durante o processo de tratamento da devolução no Tracking.

Orientações:
1. Parametrizações: 
**Tracking:**
  ° Em Configurações> Parâmetros> Integração com o Roteirizador (**Atenção:** Somente o time Lincros tem permissão para realizar alterações nos parâmetros. Para habilitar ou desabilitar alguma função, entre em contato com o suporte):
 • Habilitar o parâmetro: '**Enviar reentrega para roteirizador**';
• '**Identificador de prioridade da Reentrega**' (preencher o campo conforme o identificador criado no Roteirizador. Exemplo: R).
 ° Em Cadastros> Unidades de Negócio é necessário que os campos '**URL do Roteirizador**' e '**Token do Depósito'** estejam preenchidos (**Atenção:** usar a URL <https://interno-routing.lincros.com/> no campo. O token deve ser solicitado ao suporte).

 **Roteirizador**:
  ° Em Cadastros> Prioridade de Pedido é necessário criar um identificador (o mesmo que é informado no Tracking precisa ser informado no Roteirizador), conforme exemplo:

![Imagem 1: Considerações : Com o Tracking, é possível tratar uma devolução como ' Reentrega '. Se o cliente estiver utilizando…](https://ajuda.sankhya.com.br/hc/article_attachments/44012904186903)

A parte de parametrizações está finalizada. A partir desses ajustes, ocorrerá de forma automática o envio da reentrega ao Roteirizador.
Assim que um pedido é tratado como reentrega no Tracking, é enviado o pedido ao Roteirizador:
**Caminho:** Tracking> Monitoramento> Entrega> + Tratar devolução:

![Imagem 2: A parte de parametrizações está finalizada. A partir desses ajustes, ocorrerá de forma automática o envio da reentrega…](https://ajuda.sankhya.com.br/hc/article_attachments/44012858569751)

Na aba '**Ocorrências**' fica registrado o tratamento da devolução como **'Reentrega"** e também a confirmação do envio do pedido ao Roteirizador como reentrega:

![Imagem 3: Na aba ' Ocorrências ' fica registrado o tratamento da devolução como 'Reentrega" e também a confirmação do envio do…](https://ajuda.sankhya.com.br/hc/article_attachments/44012869709719)

No Roteirizador na tela de pedidos (Caminho: Roteirizador> Pedidos) existirão dois pedidos, o original e o pedido de reentrega:

![Imagem 4: No Roteirizador na tela de pedidos (Caminho: Roteirizador> Pedidos) existirão dois pedidos, o original e o pedido de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012904568727)

O pedido de reentrega tem a flag marcada '**Reentrega**', e a '**Data Pedido**' é a data informada no tratamento no Tracking como '**Data para Reentrega**'.
**Observação**: A comunicação de reentrega entre o Tracking e o Roteirizador exige que o pedido exista previamente no Roteirizador como um pedido normal.

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
