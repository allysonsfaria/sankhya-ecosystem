---
id: "360044593854"
titulo: "Faturamento de Grandes Volumes de Pedidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:18:56Z"
rotulos: ["Pedidos", "Configuração", "NF-e", "Faturamento", "Estoque", "Financeiro", "Processo de Clonagem de Tabelas", "Acompanhamento do Faturamento", "Faturamento em Grande Escala", "Documentos Eletrônicos"]
---

# Faturamento de Grandes Volumes de Pedidos

No artigo a seguir, pode-se consultar o conjunto das rotinas responsáveis do faturamento de grandes volumes de pedidos; visto que, esse processo consiste na transformação de um pedido em uma nota, onde o pedido já contém todas as informações necessárias para a geração da nota.

Assim, o sistema irá, basicamente, clonar as principais tabelas para o novo documento. Sabendo disso, tem-se a seguir as tabelas que serão clonadas ao realizar o faturamento:

- TGFCAB;
- TGFRAV;
- TGFRAT;
- TGFITE;
- TGFVAR;
- TGFDIN; e
- TGFFIN.

Todo o processamento ocorrerá através de uma fila de faturamento, sendo que essa fila será planejada por um JOB que processa e atualiza os status de cada pedido/lote, conforme as etapas do processo. 

Mesmo que haja somente uma duplicação das tabelas citadas acima, verifique as configurações a seguir:

| Faturamento de Grandes Volumes de Pedidos |
| --- |
| [Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Configura%C3%A7%C3%B5esIniciais) |
| [Fluxo do Processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#FluxodoProcesso) |
| [Faturamento e acompanhamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#faturamentoeacompanhamento) |
| [Parâmetros que influenciam nessa rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Parametrosqueinfluenciam) |

---

### Configurações Iniciais

| [TOP de faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#topdefaturamento) | [Série de faturamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#s%C3%A9riedefaturamento) |
| --- | --- |
| [Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#estoque) | [Financeiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#financeiro) |

---

#### TOP de faturamento

O Tipo de Operação utilizado no faturamento, será o mesmo da TOP de destino do documento de origem.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Configura%C3%A7%C3%B5esIniciais)

#### Série de faturamento

Faça o cadastro de diferentes séries por Empresa/TOP na tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba **"Série por empresa"**. Se não realizar nenhuma configuração para a TOP de faturamento, a mesma série do documento de origem será utilizada.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Configura%C3%A7%C3%B5esIniciais)

#### Estoque

A atualização de estoque ocorrerá conforme a TOP de faturamento.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Configura%C3%A7%C3%B5esIniciais)

#### Financeiro

Os financeiros também serão copiados da origem desde que a TOP de faturamento atualize financeiro. O status do faturamento pode ser acompanhado através da tabela TGFRFT, ou serviço específico que será detalhado mais adiante. Nela são apresentadas as informações:

- Número do lote;
- Nro. único do pedido;
- Status do pedido/lote;
- Dh. inclusão;
- Dh. última tentativa de processamento.

Sendo que, pode-se ter os status a seguir:

- **P - Pendente de faturamento:** o pedido foi registrado para faturamento, mas ainda não foi processado.
- **C - Aguardando correção:** o documento não foi faturado por alguma inconsistência de cadastro podendo ser configuração de faturamento, estoque, etc.
- **F - Documento faturado:** o pedido foi transformado em nota, mas no caso de documento fiscal, não significa que a nota já foi aprovada na SEFAZ. O serviço de consulta de status do faturamento também retorna a situação da NF-e.
- **E - Erro de impressão:** no caso de documento fiscal significa que a nota já foi aprovada, mas não foi possível gerar o PDF e link para download do documento; assim, poderá ser um problema no modelo utilizado para impressão.
- **I - NF-e impressa:** a nota foi aprovada (no caso de documento fiscal), o pedido faturado e o PDF gerado será disponibilizado no repositório de arquivos.

Além disso, existe outra estrutura denominada TGFLFT que irá armazenar os possíveis erros e avisos no decorrer do processo de faturamento. Assim, considere o exemplo:

Caso um pedido/lote esteja com status igual a Aguardando correção, na TGFLFT será detalhado qual foi o impedimento ocorreu nesse faturamento. Se um pedido/lote esteja com status igual a Erro de impressão, também constará nessa tabela o motivo pelo qual não foi possível gerar o PDF da nota.

**Observação:** os problemas originados pela SEFAZ não constarão nessa tabela, mas o serviço de resumo do faturamento está preparado para buscar as informações necessárias na tabela de ocorrências.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Configura%C3%A7%C3%B5esIniciais) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#top)

### Fluxo do Processo

O processo completo de faturamento de grandes volumes pode seguir o fluxo descrito a seguir. No entanto, vale ressaltar que as etapas são independentes e não precisam ser realizadas obrigatoriamente em conjunto.

| [Transformação de pedido em nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#Transforma%C3%A7%C3%A3odepedidoemnota) |
| --- |
| [Geração de lote assíncrono (NF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#gera%C3%A7%C3%A3odeloteass%C3%ADncrono(nf-e)) |
| [Busca de autorização assíncrona (NF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#buscadeautoriza%C3%A7%C3%A3oass%C3%ADncrona(nf-e)) |
| [Impressão de nota de disponibilização de PDF via repositório de arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#impress%C3%A3odenotadedisponibiliza%C3%A7%C3%A3odepdfviareposit%C3%B3riodearquivos) |

---

#### Transformação de pedido em nota

O processamento dos pedidos ocorre através de uma fila de faturamento. Para incluir itens nesta fila pode ser utilizado a rotina (mgecom@SelecaoDocumentoSP.faturarLote) utilizando a API de integração ou rotina personalizada.

![Imagem 1: O processamento dos pedidos ocorre através de uma fila de faturamento. Para incluir itens nesta fila pode ser utilizado…](https://ajuda.sankhya.com.br/hc/article_attachments/24314763257623)

A fila é gerenciada por um JOB que processa os itens em ordem de data de inclusão, mas dá prioridade para os itens adicionados mais recentemente. Itens de reprocesso, que já foram processados ao menos uma vez mas apresentaram algum erro, são executados por último.

```
JOB: br.com.sankhya.modelcore.facades.FaturamentoScheduledAction
```

**(1)** A fila para faturamento é baseada na seguinte tabela:

- **TGFRFT:** tabela que representa a fila para transformação de pedidos em notas.

**(1)** Campos:

- **NUMLOTE:** número de controle utilizado pelo cliente;
- **NUNOTA:** número único do pedido;
- **STATUS:** status do documento;
- **QTDTENTFAT:** quantidade de tentativas de faturamento;
- **DHINCLUSAO:** data de inclusão do documento para faturamento;
- **DHULTTENTA:** data da última tentativa de faturamento.

![Imagem 2: DHULTTENTA: data da última tentativa de faturamento.](https://ajuda.sankhya.com.br/hc/article_attachments/24314721484823)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#FluxodoProcesso)

#### Geração de lote assíncrono (NF-e)

Após a transformação do pedido em nota, o sistema inclui o documento gerado em uma fila de envio de lote para SEFAZ. Um JOB fica exclusivamente responsável por essa fila e processa os documentos em ordem cronológica.

**Nota:** esse recurso pode ser desativado por meio do parâmetro **"Gera lote assincrono no fat. grandes volumes? - FATGVLOTASYNC"**.

```
JOB: br.com.sankhya.mgecomercial.model.facades.GeradorLoteNFeAssincrono
```

**(1)** A fila para enviar o lote à SEFAZ é baseada na seguinte tabela.

- **TGFNPG:** nota para gerar lote.

**(1)** Campos:

- **NUNOTA:** nro. único da nota;
- **DHINCLUSAO:** data de inclusão;
- **QTDENVIO:** quantidade de tentativas de envio;
- **DHULTTENTA:** data e hora da última tentativa.

![Imagem 3: DHULTTENTA: data e hora da última tentativa.](https://ajuda.sankhya.com.br/hc/article_attachments/24314754483735)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#FluxodoProcesso)

#### Busca de autorização assíncrona (NF-e)

Similar a geração do lote assíncrono, a autorização também é realizada por um JOB que trabalha baseado em fila e busca as autorizações de forma independente do envio do lote. Essa estratégia é ativada automaticamente caso a geração de lote assíncrona esteja ligada.

```
JOB: br.com.sankhya.mgecomercial.model.facades.AutorizarNFeAssincrona
```

**(1)** A fila para buscar autorização é baseada na seguinte tabela.

- **TGFNPA:** notas para buscar autorização.

**(1)** Campos:

- **NUNOTA:** nro. único da nota;
- **DHINCLUSAO:** data de inclusão;
- **QTDENVIO:** quantidade de tentativas para buscar autorização;
- **DHULTTENTA:** data e hora da última tentativa;
- **CODUSU:** usuário;
- **COMPENSAR:** flag para determinar se a nota pode ser compensada ou não.

![Imagem 4: COMPENSAR: flag para determinar se a nota pode ser compensada ou não.](https://ajuda.sankhya.com.br/hc/article_attachments/24315254973719)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#FluxodoProcesso)

#### Impressão de nota de disponibilização de PDF via repositório de arquivos

Um JOB fica responsável pela geração do PDF da nota e a disponibilização do artefato no repositório de arquivos. Por padrão esse recurso fica ativado, mas pode ser desligado ao desabilitar o parâmetro **"Gera impressão repositório fat. grandes volumes? - FATGVIMPASYNC"**.

Devido à grande quantidade de documentos que podem ser gerados diariamente, esses artefatos ficarão disponíveis apenas por um determinado período e pode ser configurado através do parâmetro **"Qtd. dias para manter PDF notas no repositório - QTDDIASPDFNOTA"**.

Para que o link de download do PDF da nota seja gerado corretamente, deve-se configurar também o parâmetro **"Endereço para acesso externo ao WGE - ENDACESSEXTWGE"**, que contém o endereço do **Sankhya Om** para acesso externo.

```
JOB: br.com.sankhya.modelcore.facades.GeradorPDFNotaScheduledAction
```

**(1)** A fila para gerar o PDF da nota é baseada na seguinte tabela.

- **TGFLKN:** Link para o PDF da nota.

**(1)** Campos:

- **NUNOTA:** nro. único da nota;
- **DHINCLUSAO:** data e hora de inclusão;
- **STATUS:** status;
- **QTDTENTIMP:** quantidade de tentativas para impressão e geração do link de download;
- **DHULTTENTA:** data e hora da última tentativa;
- **LINKNFE:** link para download do PDF.

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#FluxodoProcesso) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#top)

### Faturamento e acompanhamento

O início do processo de faturamento, acontece pela chamada de um serviço que inclui os pedidos em uma fila para processamento:

**Serviço:** mgecom@SelecaoDocumentoSP.faturarLote

**Parâmetros:**
{
numLote : 1,
documentos : [2695, 2694, 2714]
}

**numLote:** identificador único do tipo inteiro, gerado e controlado pelo Cliente. Sendo ele, um parâmetro obrigatório.

**Documentos:** consiste em um arranjo contendo os números únicos dos documentos que serão faturados. Na sua ausência, o sistema entende que será realizado um reprocessamento do lote, ou seja, os documentos que não foram faturados serão reprocessados.

O acompanhamento do faturamento pode ser realizado através de outro serviço que fornecerá o status atual do processo para cada um dos pedidos incluídos na fila de processamento.

**Serviço:** mgecom@SelecaoDocumentoSP.getResumoLoteFaturamento

**Parâmetros:**
{
numLote : 1,
documentos : [2695, 2694, 2714]
}

**numLote:** identificador único do tipo inteiro, gerado e controlado pelo Cliente; trata-se de um parâmetro obrigatório.

**Documentos:** é um arranjo contendo os números únicos dos documentos que se deseja verificar o status. Na sua ausência o sistema entende que deve ser gerado o resumo de todo o lote.

Para utilizar os serviços, é necessário compreender nossa [API de integração](https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya).

**Observação:** uma sugestão para obter um melhor aproveitamento das rotinas que foram criadas, é utilizar pelo menos 3 instâncias do **Sankhya Om**, da seguinte forma:

- Uma instância para faturamento e envio de lotes para Sefaz;
- Uma instância para buscar autorização;
- Uma instância para gerar o PDF dos documentos e disponibilizar no repositório de arquivos.

**Nota:** para que cada instância utilize apenas os JOBS necessários, configure o Jboss ou o Wildfly com o seguinte argumento:

- Instância 1: Job de faturamento e envio de lotes para Sefaz
  **-Dsankhyaw.only.jobs=-10017,-10019**
- Instância 2: Job para buscar autorização
  **-Dsankhyaw.only.jobs=-10001**
- Instância 3: Job para gerar PDF das notas e disponibilizar no repositório
  **-Dsankhyaw.only.jobs=-10018**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#top)

### Parâmetros que influenciam nessa rotina

**Qtd. dias para manter log faturamento - QTDDIASLOGFAT:** neste parâmetro defina a quantidade de dias que o registro de faturamento será armazenado. Por padrão, ele está configurado para 30 dias.

**Qtd. dias para manter resumo faturamento - QTDDIASRESFAT:** através deste parâmetro informe a quantidade de dias que será mantido o resumo do faturamento. Este por padrão está definido para 60 dias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593854-Faturamento-de-Grandes-Volumes-de-Pedidos#top)
