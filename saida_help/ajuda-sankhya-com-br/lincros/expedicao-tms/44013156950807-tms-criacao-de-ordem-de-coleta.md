---
id: "44013156950807"
titulo: "[TMS] - Criação de Ordem de Coleta"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013156950807--TMS-Cria%C3%A7%C3%A3o-de-Ordem-de-Coleta"
trilha: "Lincros > TMS > Expedição - TMS"
atualizado_em: "2026-10-05T19:49:08Z"
rotulos: ["sync_hc", "lincros", "lincros_13432922", "sync_hash_a57a45c3840e"]
---

# [TMS] - Criação de Ordem de Coleta

**Menu:** Expedição > Coletas > Ordem de coleta

**Objetivo:** A ordem de coleta é utilizada para documentar o trânsito ou transporte da mercadoria em questão, logo no primeiro contato em que a transportadora tem com a carga (durante sua coleta), até o seu próprio endereço – onde a carga será processada e encaminhada ao seu destino. Nela, inclui-se o endereço de remetente, as informações referentes à transportadora responsável por aquele trecho e qualquer outro detalhe pertinente ao transporte daquela carga. É enviada via e-mail ou via agendamento para a transportadora, informando a data em que os documentos devem ser coletados.

## Considerações:

- Para realizar o envio automático da ordem de coleta verificar o artigo: [[TMS] - Ordem de Coleta Automática](https://lincros.movidesk.com/kb/article/234043/tms-ordem-de-coleta-automatica?menuId=6324-56776-234043&ticketId=&q=);
- Para realizar o processo de pátio e portaria através da ordem de coleta, verificar o artigo: [[TMS] - Pátio e portaria - Entrada e saída de veículos](https://lincros.movidesk.com/kb/article/266314/tms-patio-portaria?menuId=6324-56776-266314&ticketId=&q=);

## Preenchendo os campos da Ordem de Coleta

1. Clicar em “Novo” para realizar a criação de uma nova ordem de coleta:

![Imagem 1: 1. Clicar em “Novo” para realizar a criação de uma nova ordem de coleta:](https://ajuda.sankhya.com.br/hc/article_attachments/44013146088215)

**Unidade**: Informar a unidade do embarcador;

**Transportadora**: Informar a transportadora responsável pela coleta;

**Filial**: Informar a filial da transportadora responsável pela coleta;

**Agrupar conhecimentos**: A opção “Agrupar conhecimentos”, tem a mesma funcionalidade do botão Forçar união na tela de pré-conhecimentos;

**Obs**.: Para que o agrupamento ocorra, é necessário que a origem, destino, remetente e destinatário dos conhecimentos existentes na ordem de coleta sejam iguais, caso contrário não irá agrupá-los em um só;

**Agrupar unidade no arquivo NOTIFIS:** se houver notas fiscais de unidades diferentes na mesma ordem de coleta, elas são agrupadas no arquivo NOTFIS como sendo de uma unidade só;

![Imagem 2: Agrupar unidade no arquivo NOTIFIS: se houver notas fiscais de unidades diferentes na mesma ordem de coleta, elas são…](https://ajuda.sankhya.com.br/hc/article_attachments/44013157397271)

**Marcadores:**informar o marcador caso seja utilizado;

**Observação**: informar alguma instrução à transportadora caso necessário;

**Fluxo de transporte**: informar o fluxo de transporte caso seja utilizado;

**Tipo de viagem**: informar o tipo de viagem caso seja utilizado;

![Imagem 3: Tipo de viagem : informar o tipo de viagem caso seja utilizado;](https://ajuda.sankhya.com.br/hc/article_attachments/44013157535127)

**Escolta/Seguro/Trocar de motorista:** Marcar as opções caso seja necessário;

**Placa/Veículo/Motorista**: Informar o veículo/motorista responsável pela ordem de coleta;

**Quantidade de motoristas**: Informar a quantidade caso seja maior que 1;

**Grupo veículo**: Será informado automaticamente caso o cadastro do veículo possuir essa informação (exemplo: truck, carreta, van, etc);

![Imagem 4: Grupo veículo : Será informado automaticamente caso o cadastro do veículo possuir essa informação (exemplo: truck,…](https://ajuda.sankhya.com.br/hc/article_attachments/44013134019735)

**Implementos rodoviários**: Se necessário, informar o veículo e clicar em “Adicionar”. Caso seja alterado o implemento na ordem de coleta, o embarque e o conhecimento vinculados também terão seus implementos alterados;

**Obriga pesagem**: Por padrão ficará marcado. Essa opção quando desmarcada, permite o fluxo da portaria para esta ordem de coleta sem a necessidade de informar os pesos de entrada e saída, quando estiver alocado numa doca que for de uma portaria que tenha a opção “Utilizar peso da balança na portaria” marcada (pois esta opção obriga a informar os pesos na portaria);

**Pesos**: informados na portaria, quando utilizada;

**Coleta em terceiros**: Se a coleta for em terceiros e não no embarcador, marcar a opção e preencher a data mínima a máxima que irão ser apresentadas automaticamente;

![Imagem 5: Coleta em terceiros : Se a coleta for em terceiros e não no embarcador, marcar a opção e preencher a data mínima a…](https://ajuda.sankhya.com.br/hc/article_attachments/44013149011223)

**Integração**: Dados referentes à quando a ordem for enviada para integração com o ERP;

**Necessita mais de uma alocação para descarga**: Se necessário, marcar a opção;

**Data/hora do agendamento**: Data e hora que o embarcador deseja que seja feita a coleta;

**Data/hora limite confirmação**: Até quando a transportadora poderá confirmar no portal da transportadora que irá realizar a coleta;

![Imagem 6: Data/hora limite confirmação : Até quando a transportadora poderá confirmar no portal da transportadora que irá…](https://ajuda.sankhya.com.br/hc/article_attachments/44013149163671)

**Documentos**: A inserção de documentos na ordem de coleta pode ser através da nota fiscal por número ou chave, através de uma pré-nota já existente ou criando uma nova a partir da opção “Criar documento”, e através de um embarque ou pedido;

**Obs**.:  A opção “Criar documento” habilita os campos para preencher as informações necessárias para a criação da pré-nota. Ao clicar em “Adicionar”, a pré-nota é criada com a mesma transportadora da ordem de coleta, e ao clicar em Salvar realiza o vínculo na pré-nota com a ordem de coleta. Se a transportadora da ordem de coleta for alterada, a pré-nota será removida da ordem de coleta;

**Justificativas de cancelamento**: Caso a ordem seja cancelada e informado um motivo, ele é listado nesta seção;

![Imagem 7: Justificativas de cancelamento : Caso a ordem seja cancelada e informado um motivo, ele é listado nesta seção;](https://ajuda.sankhya.com.br/hc/article_attachments/44013119029271)

## Situações da ordem de Coleta

**Gerada**: Quando a ordem de coleta foi apenas criada;
**Enviada à transportadora**: Quando as informações de uma ordem de coleta foram enviadas ao transportador. Ocorre ao clicar no botão Enviar;
**Confirmada**: Quando o transportador confirma que irá coletar a mercadoria através do menu: Carga/descarga > Ordem de coleta no portal do transportador;
**Finalizada**: Quando a mercadoria é coletada pelo transportador na fábrica/depósito e o embarcador confirma através do menu: Expedição > Coletas > Confirmação de coleta, lançando uma ocorrência de coleta que contenha a ação "confirmacaocoleta - Ação executada quando é confirmado uma coleta" ou se a transportadora enviar uma ocorrência que possua essa ação;
**Cancelada**: Quando a ordem de coleta é cancelada.

## Cancelamento da ordem de coleta

Ao efetuar o cancelamento da ordem de coleta serão cancelados também os documentos vinculados (pré-conhecimento e embarque) de forma conjunta (configuração de empresa permiterCancelarDocumentosCancelarOrdemColeta).

1. Ao cancelar a ordem de coleta, cancela o pré conhecimento ou embarque vinculado ao documento e a ordem de coleta, porém:
   -Se o documento estiver vinculado a um pré-conhecimento ou embarque já está vinculado a um CT-e NÃO será cancelado;
   -Quando cancelar o pré-conhecimento ou embarque será cancelado também a cotação.
2. NÃO cancela documentos do tipo NOTA FISCAL vinculados a ordem de coleta NEM seus pré-conhecimentos vinculados;
3. Quando habilitada a configuração remove somente as notas fiscais e seus pré-conhecimentos, se desabilitada, ao cancelar uma ordem de coleta remove todos os documentos;
4. Ao cancelar a ordem de coleta pode ser informada uma justificativa de cancelamento, que fica salva na ordem de coleta. Essa justificativa é previamente cadastrada na tela de justificativas;
5. O cancelamento da ordem de coleta pode ser realizado pelo portal do transportador ou embarcador.
6. Para obrigar que sejam informadas justificativas de cancelamento pelo portal do Transportador deverá ser ativada a configuração usarJustificativaCancelamentoOrdemColetaTransportador. Somente serão listadas as justificativas de 'CANCELAMENTO' e de 'ORDEM DE COLETA'. Neste caso, também será levado em consideração a empresa da Ordem de Coleta em questão;
7. Ao reabrir a ordem de coleta reabre também os documentos do tipo PRÉ NOTA FISCAL que estão com situação CANCELADA, registrando a reabertura no histórico;
8. As cotações e solicitações de frete se mantém com a situação de cancelada.

## Ordem de coleta cancelada pela transportadora

Caso o embarcador deseje, é possível configurar para que seja criada pendência quando a ordem for cancelada pela transportadora (tanto se a empresa usar portaria ou não)

Configurações necessárias: No menu Cadastros gerais > Configurações de empresa > Parâmetros > Empresa, configurar geraPendenciaOrdemColetaCancelada = true.

Desta forma, caso a ordem seja cancelada por um usuário de transportadora, seja via portal ou webservice, será criada a pendência de Ordem de coleta cancelada, atrelada à ordem. A mesma não será resolvida automaticamente, somente de forma manual, e o usuário logado precisa possuir permissão (cadastrado na tela de Permissões de resolução).
Caso esteja configurado para notificar, será disparado o e-mail de notificação para o usuário que estiver cadastrado na tela de Responsáveis por classificação.

![Imagem 8: Desta forma, caso a ordem seja cancelada por um usuário de transportadora, seja via portal ou webservice, será criada a…](https://ajuda.sankhya.com.br/hc/article_attachments/44013119126423)

**Importante:**Quando a ordem de coleta é cancelada, por padrão os documentos são removidos dela (ou cancelados, se a configuração permitirCancelarDocumentosCancelarOrdemColeta estiver true).
Então, se a ordem for cancelada e a pendência resolvida, e porventura a ordem for reaberta, a pendência não será reaberta. Se for utilizada a mesma ordem de coleta inserindo os documentos nela e enviado para a transportadora novamente, e ela cancelar de novo, a pendência também não será reaberta. O correto é que quando uma ordem for cancelada, seja criada uma nova.

## Envio para a transportadora

 Ao clicar em 'Enviar', a situação da ordem é alterada para 'Enviada à transportadora'.
   - Permite enviar a ordem de coleta para a transportadora por e-mail, FTP ou SFTP;
   - A opção e-mail não considera usuários que possuem somente o perfil de Webservice transportadora vinculado ao usuário;

![Imagem 9: Ao clicar em 'Enviar', a situação da ordem é alterada para 'Enviada à transportadora'. - Permite enviar a ordem de…](https://ajuda.sankhya.com.br/hc/article_attachments/44013166594583)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
