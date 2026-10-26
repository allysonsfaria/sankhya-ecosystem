---
id: "44012157830679"
titulo: "[TMS] - Integração de pedidos TMS X Routing"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012157830679--TMS-Integra%C3%A7%C3%A3o-de-pedidos-TMS-X-Routing"
trilha: "Lincros > TMS > Sistema - TMS"
atualizado_em: "2026-10-05T19:20:53Z"
rotulos: ["sync_hc", "lincros", "lincros_13434390", "sync_hash_7c6a44ee3e41"]
---

# [TMS] - Integração de pedidos TMS X Routing

## Integração de pedidos TMS X Routing

**Objetivo**: Como analisar e verificar a integração de pedidos do TMS para o Routing.

**Considerações**:

- Neste momento, é importante ter em mãos todas as informações do pedido;
- O tipo de pedido irá depender de cliente para cliente podendo ser Pré-notas ficais ou Notas fiscais;
- Dentro do pedido, sendo Pré-nota fiscal ou Nota fiscal, deve estar marcado a opção Roteirizar;
- Pedidos já integrados com o roteirizador é necessário excluir o log de integração no TMS para poder integrar novamente com o Router;
- Ter conhecimento sobre os tipos de situação do documento no TMS:

**Gerada**: Situação em que a nota entra no sistema e não é associada a um Pré-conhecimento;

**Associada**: Situação em que a nota entra no sistema e é associada a um Pré-conhecimento;

**Em transporte**: Situação em que o pré-conhecimento é associado a um CTe ou recebe ação de uma ocorrência informando o início do transporte;

**Transportado**: Situação em que a NF recebe ação de uma ocorrência, informando que foi transportada;

**Cancelada**: Situação em que NF foi cancelada no Sefaz;

**Identificada**: Situação em que a NF foi importada via Sefaz, Certificado Digital;

**Bloqueada**: Situação em que a NF fica bloqueada por algum problema fiscal;

**Finalizada**: Situação em que a NF recebe ocorrência finalizadora por algum motivo que não permita que a NF seja transportada com sucesso;

Abaixo segue os códigos do sistema para cada situação do documento:

## NOTA FISCAL:

0 = GERADA(false) - A nota fiscal foi criada e recebida pelo sistema;

1 = ASSOCIADA(false) - A nota fiscal já foi adicionada em um ou mais conhecimentos e aguarda o embarque do conhecimento;

2 = EM\_TRANSPORTE(false) - A nota fiscal está em um conhecimento de transporte que está atualmente em transporte;

3 = TRANSPORTADA(true) - A nota fiscal já foi transportada;

4 = CANCELADA(true) - A nota fiscal foi cancelada;

5 = IDENTIFICADA(false), - Foi identificada a existência da nota fiscal na Sefaz, porém a nota ainda não foi recebida;

6 = BLOQUEADA(false) - A nota fiscal foi bloqueada;

7 = FINALIZADA(true) - O transporte foi finalizado devido algum imprevisto, ex: roubo, avaria, etc;

## PRÉ-NOTA FISCAL:

0 = CRIADA - A pré-nota foi criada no sistema, mas ainda não foi calculada
1 = TRANSPORTADORA\_ESCOLHIDA - Foi selecionada a transportadora que deve realizar o transporte
2 = FATURADO - Esta pré-nota foi faturada e convertida em uma nota fiscal

3 = CANCELADA - Esta pré-nota fiscal foi descartada pelo usuário ou pelo sistema ERP

4 = SOLICITADO\_COTACAO - Esta pré-nota fiscal foi solicitada uma cotação

5 = SUBSTITUIDA - Quando a pré-nota fiscal é substituída por outro documento
6 = TRANSPORTADORA\_INDEFINIDA - Quando a transportadora não foi definida.

Código do tipo de documento na integração com o Roteirizador:

0 = Nota fiscal;

1 = Pré-nota;

 Para analisar a integração de pedidos entre o TMS e o Router, iremos precisar acessar as seguintes telas:

1. No Roteirizador acessar o menu: Importações > Pedidos e menu: Pedidos;
2. No TMS acessar o menu: Operacional>Exportação>Documentos para Roteirizar;

## Exemplo da Tela de importação de pedidos

![Imagem 1: Exemplo da Tela de importação de pedidos](https://ajuda.sankhya.com.br/hc/article_attachments/44012158041367)

Nesta tela é obrigatório informar o depósito, o layout de integração com o TMS e as unidades de negócios cadastradas;

Informar se os documentos a serem importados serão do tipo '0' ou '1'. Sendo '0' para nota fiscal e '1' para pré-nota;

![Imagem 2: Informar se os documentos a serem importados serão do tipo '0' ou '1'. Sendo '0' para nota fiscal e '1' para pré-nota;](https://ajuda.sankhya.com.br/hc/article_attachments/44012155139479)

**Obs**: Sempre se atentar com a unidade de negócio selecionada. Pois, se não selecionar a unidade de negócio ou o selecionar de forma incorreta, pode acarretar de os pedidos de outra unidade de negócio serem importados para o depósito selecionado no roteirizador.

Dentro do TMS, acessar o menu: Operacional > Exportação > Documentos para Roteirizar, abaixo segue um exemplo:

![Imagem 3: Dentro do TMS, acessar o menu: Operacional > Exportação > Documentos para Roteirizar, abaixo segue um exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/44012158359575)

Ao clicarmos sobre a opção pré-nota é possível verificar as pré-notas que foram exportadas ao roteirizador para serem roteirizadas;

![Imagem 4: Ao clicarmos sobre a opção pré-nota é possível verificar as pré-notas que foram exportadas ao roteirizador para serem…](https://ajuda.sankhya.com.br/hc/article_attachments/44012124935703)

Voltando a Tela 1 do processo, dentro do roteirizador em importações pedidos, iremos identificar que estes pedidos foram importados com sucesso:

![Imagem 5: Voltando a Tela 1 do processo, dentro do roteirizador em importações pedidos, iremos identificar que estes pedidos…](https://ajuda.sankhya.com.br/hc/article_attachments/44012125067031)

 Ao consultar a tela pedidos dentro do roteirizador os pedidos devem aparecer no sistema conforme a imagem abaixo:

![Imagem 6: Ao consultar a tela pedidos dentro do roteirizador os pedidos devem aparecer no sistema conforme a imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44012142377495)

**Obs**.: Casos em que os pedidos solicitados para serem importados no roteirizador não aparecem como importados, devemos verificar as seguintes possibilidades:

1- Verificar se eles já constam como exportados no TMS. E verificar qual o CNPJ da chamada na tela de log.

2- Verificar se a unidade selecionada na importação pelo roteirizador foi a correta. Pois podem ter sido exportados para o depósito incorreto;

3 - Caso os documentos não apareçam no log da chamada no TMS. Verificar se no roteirizador eles já constam como importados anteriormente. Isto pode ser feito através do próprio TMS, clicando em filtros no menu: Operacional > Exportação >  Documentos para roteirizar;

4- Verificar pelo número da nota fiscal ou pré-nota se eles já não constam em uma chamada realizada anteriormente;

![Imagem 7: 4- Verificar pelo número da nota fiscal ou pré-nota se eles já não constam em uma chamada realizada anteriormente;](https://ajuda.sankhya.com.br/hc/article_attachments/44012158829719)

## Quando os documentos não constam no roteirizador e não constam no log de chamadas do TMS

1. Verificar o status destes documentos, pois de acordo com algumas situações os documentos não devem ser roteirizados;
2. Estas situações dependem de cliente para cliente. Mas segue alguns exemplos de situações de documentos que não devem ser roteirizados por padrão pelo sistema: Documentos em situação de Transporte ou Embarcado. (Não faz sentido programar a roteirização de algo que já está em um embarque), Documentos Cancelados, Documentos Bloqueados e Documentos Finalizados;
3. Porem isto depende de cliente para cliente onde na tela Cadastros Gerais > Configurações da Empresa > Parâmetros > Empresa, é configurado as situações que devem ser restritas para a roteirização, conforme exemplo abaixo:

![Imagem 8: Porem isto depende de cliente para cliente onde na tela Cadastros Gerais > Configurações da Empresa > Parâmetros >…](https://ajuda.sankhya.com.br/hc/article_attachments/44012137801239)

**OBS:**Para que a pré-nota seja enviada para o roteirizador. É necessário ter um pré-conhecimento vinculado a pré-nota

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
