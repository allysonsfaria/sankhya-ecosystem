---
id: "44013362302359"
titulo: "[TMS] - Validações do Sistema ao Aceitar a Fatura"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013362302359--TMS-Valida%C3%A7%C3%B5es-do-Sistema-ao-Aceitar-a-Fatura"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:55:14Z"
rotulos: ["sync_hc", "lincros", "lincros_13432658", "sync_hash_f3a39dcf4fe5"]
---

# [TMS] - Validações do Sistema ao Aceitar a Fatura

**Menu**: Cadastros Gerais > Configurações da Empresa > Parâmetros > Empresa

**Objetivo**: Hoje a rotina de aceite de fatura efetua uma série de validações diferenciadas que definem se a fatura pode ou não ser aceita. Esse artigo tem como objetivo mostrar as validações que são feitas no processo de aceite de fatura, e todos os parâmetros de empresa envolvidos nessas validações.

**Considerações**:

- Somente o time de Suporte da Lincros pode alterar os valores dos parâmetros. Portanto, caso seja necessário realizar alguma alteração, contate o time de Suporte do TMS.

## Abaixo segue algumas validações:

- **Validar limite de CT-es por fatura**
  O sistema busca na configuração "quantidadeMaximaCTeFatura" a quantidade máxima permitida de CT-es pra cada fatura e valida se a fatura em questão não ultrapassou este limite. Caso a configuração esteja ativa e a quantidade de CT-es na fatura for maior, o aceite será cancelado;

- **Validar aceite com CT-es sem arquivo repositório**
  O sistema busca pela configuração "permitirIntegrarSemArquivoRepositorio" onde, caso esteja configurada como "false" (falso), o sistema irá buscar individualmente por cada CT-e e validar um a um se possuem arquivo em diretório. Caso a configuração esteja ativa e encontre um CT-e sem arquivo no diretório (XML ou EDI) o aceite será cancelado;

- **Validar aceite sem Ocorrência Entrega**
  O sistema busca pela configuração "permitirIntegrarSomenteComOcorrenciaEntrega" onde, caso esteja configurada como "true" (verdadeiro), o sistema irá percorrer todos os pré-conhecimentos de todos os CT-es e validará se todos possuem ocorrência de entrega. Caso a configuração esteja ativa e algum CT-e não tenha a ocorrência, o aceite será cancelado;

- **Validar pagador do frete**
  O sistema busca pela configuração "nivelValidacaoTipoPagadorAceiteFatura" onde, caso seja 2 (Bloquear), o sistema irá percorrer todos os CT-es da fatura e validará se as informações de pagamento e pagador estão corretas. Caso a configuração esteja ativa e algum CT-e tenha estas informações incorretas, o aceite será cancelado;

- **Validar Aceite fatura com conhecimento não deferido**
  O sistema busca pela configuração "aceitarFaturaConhecimentoNaoDeferido" onde, caso esteja configurada como "false" (falso), o sistema irá percorrer todos os CT-es da fatura buscando CT-es que tenham sua situação igual à INDEFERIDO ou AGUARDANDO APROVAÇÃO. Caso a configuração esteja ativa e sejam encontrados CT-es nestas situações, o aceite será cancelado;

- **Validar situação dos CT-es**
  O sistema busca pela configuração "validarSituacaoCteAceiteFatura" onde, caso esteja configurada como "true" (verdadeiro), o sistema irá percorrer todos os CT-es e valida se todos estão com situação diferente de CANCELADO e ANULADO. Caso contrário, o aceite será cancelado;

- **Validar aceite por situação de integração dos CT-es**
  O sistema busca pelas configurações "validarAceiteFaturaPorIntegracaoCTe" e "publicarMensagemParaEscrituracaoCte" onde, caso ambas estejam configuradas como "true" (verdadeiro), o sistema irá percorrer todos os CT-es validando se estão com situação igual a "integrado". Caso a configuração esteja ativa e algum CT-e não esteja integrado, o aceite será cancelado;

- **Validar valor total de frete dos CT-es**
  O sistema busca pela configuração "validarValorTotalFreteCTe" onde, caso esteja configurada como "true" (verdadeiro), o sistema percorrerá todos os CT-es para validar se todos possuem valor total de frete maior que zero. Caso contrário, o aceite será cancelado;

- **Validar aceite com CT-e sem chave de acesso**
  O sistema busca pela configuração "aceitarFaturaCTeSemChave" onde, caso esteja configurada como "false" (falso), o sistema percorre todos os CT-es buscando todos os CT-es que não tem chave de acesso. Caso a configuração esteja ativa e exista algum CT-e sem chave de acesso, o aceite será cancelado;

- **Valida aceite com CT-e sem protocolo**
  O sistema busca pela configuração "aceitarFaturaCTeSemProtocolo" onde, caso esteja configurada como "false" (falso), o sistema percorre todos os CT-es buscando os que são do tipo eletrônico e não possuem número de protocolo. Caso a configuração esteja ativa e exista algum CT-e eletrônico sem número de protocolo, o aceite será cancelado;

- **Validar situação importação CT-es**
  O sistema busca pela configuração "validarSituacaoImportacaoCte" onde, caso esteja configurada como "true" (verdadeiro), o sistema percorrerá todos os CT-es buscando se algum possui erro de importação. Caso algum CT-e tenha erros de importação, o aceite será cancelado;

- **Validar pendências em Aberto**
  O sistema busca pela configuração "validarPendenciasEmAberto" onde, caso esteja configurada como "true" (verdadeiro), o sistema irá realizar uma consulta de todos as pendências de fatura e de conhecimentos que não estejam resolvidas. Caso existam pendências não resolvidas, o aceite é cancelado;

- ## Validar CT-e's não entregues

O sistema busca pela ação de usuário "bloquearAceiteFaturaCTesNaoEntregues" onde, caso o usuário tenha esta ação configurada, o sistema percorrerá todos os CT-e's da fatura para validar se todos estão como ENTREGUE. Caso exista algum CT-e não entregue, o aceite é cancelado.

- **Não realizar nenhuma validação na fatura**
  Existe também uma configuração de empresa (aceitarFaturaSemValidar) que pode ser utilizada para impedir que todas estas validações citadas acima sejam executadas, sem a necessidade de cadastrar todas estas. O intuito de ter todas as outras configurações é apenas para que seja possível delimitar quais validações serão executadas e quais não irão.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

- **Validar limite de CT-es por fatura**
  O sistema busca na configuração "quantidadeMaximaCTeFatura" a quantidade máxima permitida de CT-es pra cada fatura e valida se a fatura em questão não ultrapassou este limite. Caso a configuração esteja ativa e a quantidade de CT-es na fatura for maior, o aceite será cancelado;

- **Validar aceite com CT-es sem arquivo repositório**
  O sistema busca pela configuração "permitirIntegrarSemArquivoRepositorio" onde, caso esteja configurada como **false**, o sistema irá buscar individualmente por cada CT-e e validar um a um se possuem arquivo em diretório. Caso a configuração esteja ativa e encontre um CT-e sem arquivo no diretório (XML ou EDI) o aceite será cancelado;
- **Validar aceite sem Ocorrência Entrega**
  O sistema busca pela configuração "permitirIntegrarSomenteComOcorrenciaEntrega" onde, caso esteja configurada como **true**, o sistema irá percorrer todos os conhecimentos de todos os CT-es e validará se todos possuem ocorrência de entrega. Caso a configuração esteja ativa e algum CT-e não tenha a ocorrência, o aceite será cancelado;

- **Validar pagador do frete**
  O sistema busca pela configuração "nivelValidacaoTipoPagadorAceiteFatura" onde, caso seja **2 (Bloquear)**, o sistema irá percorrer todos os CT-es da fatura e validará se as informações de pagamento e pagador estão corretas. Caso a configuração esteja ativa e algum CT-e tenha estas informações incorretas, o aceite será cancelado;

- **Validar Aceite fatura com conhecimento não deferido**
  O sistema busca pela configuração "aceitarFaturaConhecimentoNaoDeferido" onde, caso esteja configurada como **false**, o sistema irá percorrer todos os CT-es da fatura buscando CT-es que tenham sua situação igual à INDEFERIDO ou AGUARDANDO APROVAÇÃO. Caso a configuração esteja ativa e sejam encontrados CT-es nestas situações, o aceite será cancelado;

- **Validar situação dos CT-es**
  O sistema busca pela configuração "validarSituacaoCteAceiteFatura" onde, caso esteja configurada como **true**, o sistema irá percorrer todos os CT-es e valida se todos estão com situação diferente de CANCELADO e ANULADO. Caso contrário, o aceite será cancelado;
- **Validar aceite por situação de integração dos CT-es**
  O sistema busca pelas configurações "validarAceiteFaturaPorIntegracaoCTe" e "publicarMensagemParaEscrituracaoCte" onde, caso ambas estejam configuradas como **true**, o sistema irá percorrer todos os CT-es validando se estão com situação como integrado. Caso a configuração esteja ativa e algum CT-e não esteja integrado, o aceite será cancelado;

- **Validar valor total de frete dos CT-es**
  O sistema busca pela configuração "validarValorTotalFreteCTe" onde, caso esteja configurada como **true**, o sistema percorrerá todos os CT-es para validar se todos possuem valor total de frete maior que zero. Caso contrário, o aceite será cancelado;
- **Validar aceite com CT-e sem chave de acesso**
  O sistema busca pela configuração "aceitarFaturaCTeSemChave" onde, caso esteja configurada como **false**, o sistema percorre todos os CT-es buscando todos os CT-es que não tem chave de acesso. Caso a configuração esteja ativa e exista algum CT-e sem chave de acesso, o aceite será cancelado;

- **Valida aceite com CT-e sem protocolo**
  O sistema busca pela configuração "aceitarFaturaCTeSemProtocolo" onde, caso esteja configurada como **false**, o sistema percorre todos os CT-es buscando os que são do tipo eletrônico e não possuem número de protocolo. Caso a configuração esteja ativa e exista algum CT-e eletrônico sem número de protocolo, o aceite será cancelado;

- **Validar situação importação CTe's**
  O sistema busca pela configuração "validarSituacaoImportacaoCte" onde, caso esteja configurada como **true**, o sistema percorrerá todos os CT-es buscando se algum possui erro de importação. Caso algum CT-e tenha erros de importação, o aceite será cancelado;
- **Validar pendências em Aberto**
  O sistema busca pela configuração "validarPendenciasEmAberto" onde, caso esteja configurada como **true**, o sistema irá realizar uma consulta de todos as pendências de fatura e de conhecimentos que não estejam resolvidas. Caso existam pendências não resolvidas, o aceite é cancelado;

- ## Validar CT-e's não entregues
- O sistema busca pela ação de usuário "bloquearAceiteFaturaCTesNaoEntregues" onde, caso o usuário tenha esta ação configurada, o sistema percorrerá todos os CT-e's da fatura para validar se todos estão como ENTREGUE. Caso exista algum CT-e não entregue, o aceite é cancelado.
