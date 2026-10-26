---
id: "360043102893"
titulo: "Ambiente de Contingencia EPEC bloqueado para o Emitente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043102893-Ambiente-de-Contingencia-EPEC-bloqueado-para-o-Emitente"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:18Z"
rotulos: ["ERRONF", "EPEC", "NF-e", "SEFAZ", "Contingência", "Localizar notas pendentes", "Regularização com SEFAZ", "Status: 142 Contingência EPEC", "Erro", "Artigo atualizado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Ambiente de Contingencia EPEC bloqueado para o Emitente

**MENSAGEM:**

Rejeição 142: Ambiente de Contingência EPEC bloqueado para o Emitente.

**SITUAÇÃO:**

Ao emitir NF-e/NFC-e com o evento EPEC para o Ambiente Nacional e existir algum EPEC pendente de conciliação neste ambiente, o órgão autorizador retornará a rejeição 142.

**SOLUÇÃO:**

**(1)** Localize no sistema a(s) nota(s) referenciadas na mensagem de validação retornada pela SEFAZ. Conforme exemplo abaixo, nota-se que a informação de chave da nota que está bloqueando o envio EPEC é especificada:

**"**Status de retorno: 142, motivo: Ambiente de contingência EPEC bloqueado para o emitente. **Notas Pendentes: 35181108064928000141550010000034764809136XXX"**

**(2)** Localizada a nota, através do número de chave especificado, realize as devidas tratativas da mesma no sistema, conforme detalhado em: [Nota Fiscal Eletrônica status 'Enviada em Ambiente de Contingência'(EPEC). Como funciona?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360042626354)

**(3)** Caso a aprovação não seja possível por motivos alheios ao sistema, ou o erro persista, a regularização deverá ser tratada diretamente com a **SEFAZ**, com o apoio do **Contador** da empresa.

- Apenas a **SEFAZ** pode remover as pendências e desbloquear a emissão de **EPEC**. Se o CNPJ estiver bloqueado para esse tipo de emissão, é necessário solicitar a regularização junto à SEFAZ Estadual.
- Quando o ambiente de autorização do EPEC estiver bloqueado, a SEFAZ retornará a relação de notas pendentes de conciliação (tag **chNFePend**), limitada a até 50 chaves de acesso. O desbloqueio deve ser solicitado por meio de denúncia espontânea ou abertura de chamado junto à SEFAZ.

**(4)** Acesse o Portal da SEFAZ:

- Ambiente de homologação ([clique aqui para acessar o portal](https://hom.nfe.fazenda.gov.br/)):
- Ambiente de produção ([clique aqui para acessar o portal](https://www.nfe.fazenda.gov.br/portal/principal.aspx)).
- No portal da SEFAZ, é necessário acessar a opção Serviços >> Consultar/Liberação de EPEC Pendente de Conciliação, conforme imagem abaixo:

![Imagem 1: No portal da SEFAZ, é necessário acessar a opção Serviços >> Consultar/Liberação de EPEC Pendente de Conciliação,…](https://ajuda.sankhya.com.br/hc/article_attachments/41928677364119)

- 3. Será exibida a lista de NF-e pendentes de conciliação EPEC:

![Imagem 2: 3. Será exibida a lista de NF-e pendentes de conciliação EPEC:](https://suporte.senior.com.br/hc/article_attachments/5572930048916/mceclip1.png)

**Observação:**

É necessário que o certificado digital da empresa esteja instalado diretamente no Computador que está acessando o Portal da SEFAZ para realizar essa operação.

**CAUSA:**

Esta mensagem é apresentada quando existem **EPECs pendentes de conciliação** no ambiente nacional. Após o registro de um EPEC, o emitente tem até **7 dias (168 horas)** para obter a autorização da NF-e na SEFAZ Estadual. Após essa autorização, a SEFAZ Estadual realiza a conciliação do documento com o ambiente nacional.

Caso a conciliação não ocorra dentro desse prazo, a SEFAZ bloqueia automaticamente o ambiente de contingência EPEC para o emitente, impedindo a autorização de novos EPECs até que as pendências sejam regularizadas.

Essa rejeição também pode ocorrer em razão de bloqueios cadastrais ou fiscais do CNPJ junto à SEFAZ, que impedem a utilização do ambiente de contingência EPEC.

**IMPORTANTE:**

- Quando o EPEC for registrado pela SEFAZ, a identificação pode ser feita pelos campos **"Dt. Emissão EPEC"**, **"Nro. Reg. DPEC"**, **"Status NF-e"** e **"Dt. Reg. EPEC"** no cabeçalho da nota.
- Pendências de EPEC não se limitam às notas emitidas pelo sistema atual. Em caso de troca de provedor e existência de pendências anteriores, a situação deve ser informada à SEFAZ para análise e desbloqueio.

**OBSERVAÇÃO:**

A SEFAZ orienta os clientes bloqueados a entrar em contato para que seja avaliado o desbloqueio, caso a caso, ([NT2014/001](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=1m6MlHgr744=)) - Nota Técnica.
