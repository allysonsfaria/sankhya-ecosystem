---
id: "360044607594"
titulo: "Razão Analítico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607594-Raz%C3%A3o-Anal%C3%ADtico"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-09-15T14:31:06Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Adicional", "Contábil", "Contas", "Projeto", "Centro de Resultado", "Conta", "Analítico", "Histórico", "Movimento", "Financeiro", "Razão", "Centro", "Contrapartida", "Resultado", "br.com.sankhya.mgecontab.rel.razaoanalitico", "Razão Analítico manual", "Razão Analítico: Relatório detalhado de contas contábeis.", "Configurações: Período contas centros de resultado e projetos.", "Impressão: Formatação ordenação logomarca e assinaturas."]
---

# Razão Analítico

As rotinas contábeis exigem que a verificação das contas contábeis seja feita constantemente, tanto para análise das contas, quanto para detectar possíveis erros. Fatos estes, que geram a necessidade de um documento para evidenciar estas informações de forma estruturada. Tem-se com o relatório **"Razão Analítico"**, um demostrativo dos lançamentos realizados nas contas contábeis dentro do período definido.

![Imagem 1: As rotinas contábeis exigem que a verificação das contas contábeis seja feita constantemente, tanto para análise das…](https://ajuda.sankhya.com.br/hc/article_attachments/360076236393)

No topo da tela, você irá visualizar um link **"Clique para selecionar uma empresa"** para definir a empresa que terá seu relatório gerado. Quando uma empresa é escolhida, este link é apresentado como o nome da mesma, clicando-se sobre ele, pode-se alterar para outra empresa.

Tem-se também o botão **"Visualizar Relatório"**, que permite a visualização dos dados, após definidas todas as configurações apresentadas abaixo.

No campo **"Período de Movimento"** defina o período a ser considerado para geração do relatório.

**Observação:** com o parâmetro **"Forçar o download de relatórios internos? - FORCEDOWNLOAD"** ligado e o parâmetro **"Utilizar JasperViwer p/ visualização de relatório? - UTZJASPERWC"** desligado, quando você efetuar o download do relatório interno, ele será apresentado no visualizador nativo do sistema.

![Imagem 2: Habilite o parâmetro "Usar busca única em relatório razão analítica - CTBUSABUSUNRRA" para utilizar uma forma de busca…](https://ajuda.sankhya.com.br/hc/article_attachments/28276567247511) Habilite o parâmetro **"Usar busca única em relatório razão analítica - CTBUSABUSUNRRA"** para utilizar uma forma de busca única e consolidada de calcular os valores de lançamentos, saldos iniciais e a somatória desses dados. Esse parâmetro será utilizado para reduzir o tempo de processamento e melhorar a eficiência no retorno das informações, especialmente em cenários com grande volume de dados. 

#### Seção Conta Contábil

Através do campo **"Considerar"** será feita a definição de apresentação das contas contábeis. São disponibilizadas as seguintes opções:

- Todas;
- Intervalo;
- Conta Reduzida.

Ao definir o campo Considerar com a opção **"Conta** **Reduzida"**, tem-se a exibição do campo **"Cód. Reduzido"** que deve ser preenchido com a conta reduzida.

Os campos **"Conta Inicial"** e **"Conta Final"** serão habilitados para preenchimento quando o campo Considerar for configurado com a opção Intervalo. Informe nestes campos, o intervalo das contas que deseja visualizar no relatório.

#### Seção Centro de Resultado

**Observação:** os campos desta seção estarão liberados para preenchimento somente se na tela [Empres](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa)[a](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa), aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos), a marcação **"Utiliza Centro de resultado"** estiver efetuada.

Preencha os campos **"Inicial"** e **"Final"** com o intervalo de Centros de Resultado que deseja considerar para geração do relatório Razão Analítico.

#### Seção Projeto

**Nota:** os campos desta seção estarão liberados para preenchimento apenas se na tela Empresa, aba Lançamentos, a marcação **"Utiliza Projeto"** estiver selecionada.

Informe nos campos Inicial e Final o intervalo de Projetos que deseja considerar para geração do relatório Razão Analítico.

#### Seção Parâmetros de impressão

A marcação **"Atualizar página do diário?"** permite que na impressão do relatório Razão Analítico de um determinado período, o sistema armazene a última página impressa para iniciar a impressão do período seguinte a partir desta página.

Ao acionar a marcação **"Imprimir Histórico completo?"**, o histórico será impresso considerando todas as informações inseridas no histórico; se desmarcada, será impressa apenas uma linha.

Se efetuar a marcação **"Se o valor das colulas Créd./Déb. for zero, imprimir em branco?"** e o valor das colunas **"Créd./Déb."** for igual azero, a conta será impressa com as colunas em branco, não imprimindo o valor **"0,00"** nas colunas de Crédito e Débito.

Utilize a marcação **"Quebrar razão por empresa de origem"** juntamente com a marcação **"Gravar Empresa de Origem nos lançamentos"** localizada na aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos) da tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa). Caso a mesma se encontre habilitada, o relatório Balancete de Verificação será apresentado por Empresa de Origem dos lançamentos, ou seja, os saldos apresentados serão demonstrados conforme a Empresa de Origem que gerou os mesmos.

**Observação:** caso o campo da Empresa de Origem fique desmarcado, a exibição por empresa de origem não surtirá efeito.

Defina no campo **"Quebra"** como será realizada a quebra do relatório, ou seja, a partir de qual ou quais campos, os dados serão inicializados no registro seguinte. Por exemplo, se a quebra de um relatório foi por **"Código do Parceiro"**, sucessivamente a cada código tem-se o agrupamento de todos os outros campos selecionados para serem apresentados. Utilize as seguintes opções:

- Não quebrar;
- Quebrar por C.R.;
- Quebrar por Projeto;
- Quebrar por C.R./Projeto;
- Quebrar por Projeto/C.R..

O campo **"Data/Hora de Emissão"** registra automaticamente a data e a hora de acesso a tela, caracterizando assim que foi iniciada a emissão do relatório.

Em relação ao campo **"Última página impressa"** este será alimentado com a última página do relatório que foi impressa. Além de informá-lo manualmente, caso a marcação Atualizar página do diário esteja efetuada, este campo será alimentado automaticamente pelo sistema ao final de cada impressão realizada. Se alterado manualmente, o sistema considera esta modificação para continuidade nas numerações das páginas.

No campo **"Coluna Adicional"** será possível dizer se alguma coluna adicional será impressa no relatório. Pode-se escolher dentre as seguintes opções:

- Não imprimir;
- Centro de Resultado;
- Documento;
- Projeto.

Determine no campo **"Ordenar por"** a ordenação em que os campos serão impressos. Pode-se definir dentre duas possibilidades:

- Conta, Referência, Dia, Lote, Lançamento;
- Conta, Referência, Nro. Documento, Lançamento.

O campo **"Contas sem Movimento"** indica o tratamento dado no relatório impresso, às contas sem movimento.

- Não imprimir: As contas sem movimento, não serão impressas;
- Imprimir todas:  Todas as contas, mesmo sem movimento, serão impressas;
- Apenas COM saldo inicial: As contas sem movimento serão impressas, porém, desde que tenham saldo inicial.

Já no campo **"Contrapartida"** configure a impressão da Contrapartida. Têm-se as seguintes opções:

- **Não imprimir:** Não será impressa a contrapartida;
- **Imprimir conta reduzida:** Será impressa a contrapartida reduzida;
- **Imprimir conta normal:** Será feita a impressão da contrapartida normal, ou seja, a conta contábil.

Através do campo **"Formato da impressão"**, você irá definir se a extensão utilizada para impressão do relatório será em **"PDF"** ou **"Excel (.xlsx) Padrão"**.

**Importante:** com o parâmetro **"Gera relatório em excel sem considerar quebras. - GERRELEXCSEMQUE"** desligado, o campo Formato de impressão apresentará a opção **"Excel (.xlsx) Simplificado"**, trazendo o modelo de impressão padrão sem mesclas. Se o parâmetro estiver ligado, o campo trará apenas a opção de Excel Padrão, que é o modelo com mesclas.

**Observação:** no formato Excel, ao ser solicitada a visualização, teremos o download do relatório no referido formato contendo as informações condizentes com sua configuração.

Acione a marcação **"Imprime logomarca?"** quando desejar que a logomarca seja gerada/impressa no canto superior esquerdo do relatório.

A marcação **"Geração da Assinatura conforme signatários?"** permite que na última página do lado esquerdo dos relatórios seja exibida a primeira assinatura e assim por diante. A assinatura cadastrada deve pertencer a mesma empresa da geração do demonstrativo; a data de início/fim da assinatura deverá estar contida no período da data que está sendo gerado o demonstrativo e a marcação Gerar Relatórios Contábeis deve estar realizada.

**Importante:** caso várias assinaturas sejam impressas, pode ser que o espaço não seja suficiente, por isso serão ser impressas em outra página. A ordenação das assinaturas geradas será conforme o código do signatário.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607594-Raz%C3%A3o-Anal%C3%ADtico#top)
