---
id: "360045116513"
titulo: "Importação de Lote"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-08-31T19:31:36Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Delimitador", "br.com.sankhya.contab.mov.importacaodelote", "Importação de Lote manual", "XML", "Importação", "Lote", "TXT", "Contabilidade", "Lançamentos Contábeis", "Importação de Lote na Contabilidade: Processo e Configurações"]
---

# Importação de Lote

```
 Módulo: Contabilidade > Rotinas
```

---

Esta rotina possibilita que você importe registros contábeis oriundos de sistemas de terceiros para o módulo de Contabilidade (registros compostos por informações de **"Folha de Pagamento"**, **"Estoque"**, **"Financeiro"** entre outros). Esse procedimento tem como resultado o agrupamento dos registros contábeis, permitindo sua conferência e geração de dados gerenciais e fiscais.

A importação de registros contábeis se dá pela leitura de um arquivo do tipo .txt ou XML gerado por outros sistemas, que estejam em conformidade com o layout preestabelecido; a importação desses registros pelo módulo de contabilidade é feita de forma que eles passam a compor a tabela de lançamentos contábeis do Módulo Contábil (TCBLAN). Sendo assim, teremos:

| [Campos da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#camposdatela) | [Botão Importar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#bot%C3%A3oimportar) |
| --- | --- |
| [Botão Histórico da importação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#bot%C3%A3ohist%C3%B3ricodaimporta%C3%A7%C3%A3o) | [Layouts para os tipos de arquivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#layoutsparaostiposdearquivo) |

![Imagem 1: Layouts para os tipos de arquivo](https://ajuda.sankhya.com.br/hc/article_attachments/31897174992535)

## Campos da tela

Primeiro, você determina o **"Tipo de Arquivo"** a ser importado, de acordo com as seguintes alternativas:

- **Texto Extensão TXT:** Os dados no arquivo estarão sequenciados, sem nenhum separador;
- **Texto Extensão TXT c/ Delimitador:** Por esta opção, você terá que informar no espaço à frente, o delimitador que foi utilizado para separar os dados dentro do arquivo;

**Observação:** não é pode informar como delimitador **"letras"**, **"números"** ou o caractere **"."** (ponto). O delimitador deve ser um caractere especial. No exemplo retratado na imagem acima, usamos o caractere **"|"** (barra vertical).

- **Extensão XML:** Os dados estarão disponibilizados em um arquivo XML.
- **Extensão XSL -** os dados estarão disponibilizados em um arquivo XSL.

Quando a marcação **"Lançamento normal para Contra-Partida sem Conta Contábil"** está realizada, faz com que a importação do lote utilize a conta Contrapartida quando não houver conta contábil.

Através da marcação **"Adiciona lançamentos em lotes já existentes"** você define se serão adicionados lançamentos em lotes que já existem. Quando desmarcada, essa adição não ocorrerá e será apresentado um questionamento, te perguntando se o processo de importação deverá ser paralisado.

A informação do campo **"Referência"** é carregada automaticamente, com base no campo **"Referência"** presente na tela [Preferências da Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), aba [Exercício](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abaexerccio). Porém, caso seja necessário, essa informação pode ser alterada.

No campo **"Lote"**, você pode escolher um número de lote para que somente este seja importado; deixando esse valor com "0", todos os lotes serão importados.

Através da marcação **"Gerar Partida Dobrada a partir de uma linha com duas contas"**, nosso sistema verificará na importação do arquivo se em cada linha existem informações nos campos **"Texto Extensão TXT"** / **"Extensão XML"**. Caso haja, será gerado um novo lançamento contábil para o mesmo número de lançamento, mantendo os dados conforme o lançamento de origem.

Considerando essa marcação, serão importados dois lançamentos no sistema: o lançamento de origem e o lançamento de contrapartida.

Se você habilitar a marcação **"Importar Número Documento"**, fará com que o número de documento ao qual se refere determinado lançamento contábil, seja apresentado nas linhas do arquivo de importação de lote. Sendo assim, o Sankhya Om procederá com as devidas validações.

Os documentos mencionados estão relacionados ao rastreio das origens dos lançamentos contábeis, considerando a conciliação entre os dados de origem e o que foi contabilizado.

Quando você selecionar a marcação **"Importar Código do Projeto"**, o sistema irá considerar as informações correspondentes ao código do projeto, sendo possível visualizá-lo nas linhas do arquivo de importação de lote mediante as validações do sistema.

Os lançamentos relacionados ao código do projeto estão vinculados ao fechamento contábil, a conciliação contábil e a [Geração de Arquivo - ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234974-Gera%C3%A7%C3%A3o-de-Arquivo-ECD). Assim, são adicionados projetos aos lançamentos contábeis.

**Nota:** a marcação Importar Código do Projeto só estará disponível quando a empresa selecionada estiver com a marcação **"Utiliza Projeto"** realizada na tela [Preferências da Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abalanamentos).

**Importante:** será permitido importar apenas os Códigos de Projetos que estiverem cadastrados em sua base de dados; caso contrário, será apresentada a seguinte mensagem:

**"O Código do Projeto X não está cadastrado. O arquivo não pode ser importado".**

**Observação:** quando você utiliza as marcações Importar Número Documento e Importar Código do Projeto o sistema procede com as devidas importações de lote, considerando diversos tipos de contabilizações e, proporcionando assim, o rastreio das informações para não ocorrerem divergências nos lançamentos contábeis.

**Nota:** ao habilitar as marcações Importar Número Documento e Importar Código do Projeto, serão inseridos os campos **"Núm. Documento"** e **"Projeto"** na tela [Lançamentos contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173).

**Observação:** quando você selecionar as marcações acima e no arquivo elas não existirem, a seguinte mensagem será exibida:

**"O campo Importar Número Documento/Importar Código Projeto está marcado e não há este dado na linha X".**

Ao ativar a marcação **"Importar Empresa de Origem"**, o código da empresa informado no layout de importação será importado e alimentará o campo **"Empresa de Origem**" da tela [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173). Uma vez que esta marcação esteja acionada e no layout não existir o código da Empresa de Origem informado, será apresentada a seguinte mensagem:

**"O campo Importar Empresa Origem está marcado e não há este dado na linha XPTO"**

Nesse caso, verifique os dados do layout de importação e alimente-os com as informações necessárias ou desative a marcação.

Com a marcação **"Importar Empresa de Destino"** habilitada, o sistema irá ignorar a Empresa selecionada e efetuar a importação de lotes conforme a Empresa de Destino no arquivo TXT. Assim, ao clicar no botão ![Imagem 2: Com a marcação "Importar Empresa de Destino" habilitada, o sistema irá ignorar a Empresa selecionada e efetuar a…](https://ajuda.sankhya.com.br/hc/article_attachments/22702266789527) **"Importar"** o sistema exibirá a mensagem:

**"A rotina está sendo efetuado com a opção para ignorar a empresa selecionada e passando a efetuar a importação pela Empresa Destino existente no Arquivo TXT.**

Desse modo, pode-se, ou não, confirmar a execução da importação com essa configuração.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#top)

## Botão Importar

O botão Importar presente no alto da tela, iniciará a importação dos lotes com base no arquivo selecionado. Ao acioná-lo, será aberta a tela para escolha do arquivo a ser trabalhado:

![Imagem 3: O botão Importar presente no alto da tela, iniciará a importação dos lotes com base no arquivo selecionado. Ao…](https://ajuda.sankhya.com.br/hc/article_attachments/4847930595863)

Feita a escolha do arquivo, teremos o início do processo de importação.

**Importante:** Ao importar um arquivo que contém Centro de Resultado, nosso sistema só irá considerar o CR se, no Plano de Contas, as contas envolvidas nos lançamentos estiverem com a marcação **"Centro de Resultado obrigatório"** (aba **"Geral"**) acionada. Ao habilitar o parâmetro **"Importar CR mesmo se não marcado como obrigatório? - IMPCRNAOOBRIG"**, você terá a importação do Centro de Resultado mesmo que a marcação esteja desabilitada.

**Nota:** Caso a Empresa utilize Centro de Resultado e a marcação **"Utiliza Centro de Resultado"** não esteja realizada, a importação não irá considerar o CR do arquivo e preencherá o lançamento com zero.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#top)

## Botão Histórico da Importação

O botão Histórico apresenta os processos de importação já realizados. Na grade com os processos, temos o **"Status"**, **"Empresa"**, as **"Datas de Execução"** (inicial e final), o **"Tempo de Execução"** e o **"Usuário"** que realizou a importação:

![Imagem 4: O botão Histórico apresenta os processos de importação já realizados. Na grade com os processos, temos o "Status" ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4850421295767)

Se o processo estiver com status Finalizado, você poderá baixar o arquivo e verificar se houveram erros ao consistir lote ou ao importar lote.

Caso apresente algum erro na importação dos lotes, é apresentado um pop-up apresentando o motivo o do erro.

**Observação:** Os erros ficam separados. Erros podem ter ocorrido na parte que o sistema consiste o lote, por isso, o arquivo (Log do erro) que é gerado ficará no repositório de arquivos no seguinte caminho: Contabilidade / Importação Lote /

**Validações na importação dos lotes:** Segue abaixo a lista das validações que o sistema realizará na importação dos lotes:

**1-** Para fazer a importação do lote, você deverá selecionar a empresa, caso contrário, a seguinte mensagem será exibida:

**"Para fazer a importação do lote é necessário informar a empresa."**

**2-** Para fazer a importação do lote, você tem que informar o ano de referência, caso contrário, a mensagem abaixo será exibida:

**"Para fazer a importação do lote é necessário informar o ano de referência."**

**2.1-** Além de ter que informar o ano, ele deve possuir valor maior que zero, caso contrário, a mensagem a seguir será exibida:

**"Informe um ano de referência com valor mais que zero."**

**3-** Para o Tipo de Arquivo **"Texto Extensão c/ Delimitador"**, você deve informar o delimitador, caso contrário, a seguinte mensagem será exibida:

**"Para o Tipo de Arquivo 'Texto Extensão c/ Delimitador' é necessário informar um delimitador."**

Ao clicar em Importar, se o lote não for informado ou possuir valor zero, o sistema irá apresentar um pop-up com o seguinte questionamento:

**"Deseja importação todos os lotes?"**

Se você clicar em não, a mensagem abaixo é exibida:

**"Número de Lote deve ser informado."**

Se você clicar em sim, um pop-up será apresentado para que você selecione o arquivo pra importação e dê inicio ao processo de importação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#top)

## Layouts para os tipos de arquivo

Nosso sistema está preparado somente para importar os arquivos que estiverem dentro do layout definido, o layout é diferente conforme a extensão do arquivo.

| [Texto Extensão TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#textoextens%C3%A3otxt) | [Texto Extensão TXT c/ Delimitador](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#textoextens%C3%A3otxtc/delimitador) |
| --- | --- |
| [Extensão XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#extens%C3%A3oxml) | [Layout para arquivos XLSX](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#LayoutparaarquivosXLSX) |

## Texto Extensão TXT

| **Campo** | **Tipo** | **Tamanho** | **Decimais** | **Pos. Inicial** | **Pos. Final** | **Correspondente** |
| --- | --- | --- | --- | --- | --- | --- |
| NUMLOTE | N | 11 | 0 | 1 | 11 | TCBLAN.NUMLOTE/TCBLOT.NUMLOTE |
| NUMLAN | N | 11 | 0 | 12 | 22 | TCBLAN.NUMLANC |
| CODCON | C | 14 | 0 | 23 | 36 | TCBLAN.CTACTB |
| CONPAR | C | 14 | 0 | 37 | 50 | TCBLAN.CODCONPAR |
| MESMOV | N | 6 | 0 | 51 | 56 | TCBÇAN.REFERENCIA/TCBLOT.REFERENCIA |
| DIAMOV | N | 6 | 0 | 57 | 62 | TCBLAN.DTMOV/TCBLOT.DTMOV |
| CENCUS | N | 11 | 0 | 63 | 73 | TCBLAN.CODCENCUS |
| VLRLAN | N | 20 | 0 | 74 | 93 | TCBLAN.VLRLAN |
| COSHIS | N | 6 | 0 | 94 | 99 | TCBLAN.CODHISTCTB |
| CONHIS | C | 140 | 0 | 100 | 239 | TCBLAN.CMPLHIST |
| TIPLAN | C | 1 | 0 | 240 | 240 | TCBLAN.TIPLAN |
| DATVCT | D | 10 | 0 | 241 | 252 | TCBLAN.VENCIMENTO |
| NUMDOC | N | 9 | 0 | 253 | 261 | TCBLAN.NUMDOC |
| CODPROJ | N | 10 | 0 | 262 | 271 | TCBLAN.CODPROJ |
| CODEMPORIG | N | 5 | 0 | 272 | 276 | TCBLAN.CODEMPORIG |
| CODEMPDEST | N | 5 | 0 | 277 | 282 | TCBLAN.CODEMPDEST |

Tipo = N (Alinhamento a direita com zeros à esquerda)

Tipo = C (Alinhamento com brancos à direita)

Tipo = D (Formato dd/mm/aaaa)

Considerações importantes:

- A data de referência (Campo 'MESMOV' - representará o mês) deve conter um valor entre 000001, e 000012, um valor diferente não será aceito pelo sistema;
- A data de movimento (Campo 'DIAMOV' - representará o dia) deve conter um valor entre 000001 e 000031, um valor diferente não será aceito pelo sistema;
- No banco de dados as datas serão salvas considerando o formato dd/mm/aaaa.

Exemplo de arquivo importado corretamente:

![Imagem 5: Exemplo de arquivo importado corretamente:](https://ajuda.sankhya.com.br/hc/article_attachments/4850169939607)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#layoutsparaostiposdearquivo)

## Texto Extensão TXT c/ Delimitador

Segue a mesma lógica dos campos, com a diferença que existe um delimitador, logo os campos não serão analisados pelo sistema pela posição e sim pelo delimitador.

00000000010|00000000010|1110100001|20101001|000001|000031||0000000000000023659||DESPESAS COM VARIAÇÃO CAMBIAL S/NF 123 IMPORTACAO|D|31/01/2015|

00000000010|00000000011|1110100001|10101001|000001|000031||0000000000000074896||DESPESAS COM VARIAÇÃO CAMBIAL S/NF 123 IMPORTACAO|D|31/01/2015|

00000000011|00000000012|2110100001|000001|000031||0000000000000012896||DESPESAS COM VARIAÇÃO CAMBIAL S/NF 123 IMPORTACAO|D|31/01/2015|

00000000011|00000000013|2110100001|000001|000031||0000000000000036958||DESPESAS COM VARIAÇÃO CAMBIAL S/NF 123 IMPORTACAO|D|31/01/2015|

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#layoutsparaostiposdearquivo)

## Extensão XML

Também segue a mesma lógica dos campos, porém, aqui deve-se respeitar o nome das tags. Elas devem possuir o mesmo nome do campo da tabela TCBLAN no layout para o arquivo .txt.

![Imagem 6: Também segue a mesma lógica dos campos, porém, aqui deve-se respeitar o nome das tags. Elas devem possuir o mesmo nome…](https://ajuda.sankhya.com.br/hc/article_attachments/4848546355095)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#layoutsparaostiposdearquivo)

## Layout para arquivos XLSX

A importação de lotes contábeis também pode ser feita através de planilhas Excel (XLSX). Esse formato é uma alternativa prática aos modelos tradicionais em TXT ou XML e facilita a preparação e conferência dos dados antes do envio ao sistema.

A planilha precisa seguir uma estrutura fixa, com **colunas obrigatórias** e, em alguns casos, **colunas adicionais**, dependendo da configuração do sistema. Para acessar as colunas confira a [planilha modelo](https://docs.google.com/spreadsheets/d/1GVUMoPgxF1pmTpnvbz8N8xwUmL6Zcl3-/edit?gid=2139834871#gid=2139834871).

**Importante:** As colunas devem estar exatamente com esses nomes. O sistema não reconhecerá variações ou abreviações.

O modelo de planilha fornecido pode conter uma linha com nomes descritivos das colunas (ex: "Número do Lote", "Código da Conta Contábil" etc.) para facilitar o entendimento. No entanto, essa linha descritiva deve ser excluída antes da importação. O arquivo final deve conter apenas a linha com os nomes dos campos utilizados pelo sistema, por exemplo: `NUMLOTE`, `NUMLAN`, etc.

#### Regras de Validação no Layout XLS

| Coluna | Tipo de Dado | Regra de Preenchimento |
| --- | --- | --- |
| **CODCTACTB** | **Texto** | O código da conta contábil deve ser preenchido por extenso, **sem nenhuma pontuação**. O Sankhya aplicará a máscara da empresa automaticamente. **Exemplo:** Se a conta no sistema for `01.01.01.01.00004`, o valor no arquivo deve ser `0101010100004`. |
| **CODCON** | **Texto** | Preencher como texto simples. Se o valor for extraído como numérico, o dado terá valor máximo de 2.147.483.647. |
| **CONPAR** | **Texto** | Preencher como texto simples. Se o valor for extraído como numérico, o dado terá valor máximo de 2.147.483.647. |

#### Colunas Necessárias no Arquivo a ser Importado

As colunas a seguir são essenciais. É fundamental que as colunas `CODCON` e `CONPAR` estejam formatadas como **Texto Simples** no Excel.

| Coluna | Tipo no Arquivo |
| --- | --- |
| **NUMLOTE** | Numérico |
| **NUMLAN** | Numérico |
| **CODCON** | **Texto** |
| **CONPAR** | **Texto** |
| **MESMOV** | Numérico |
| **DIAMOV** | Numérico |
| **CENCUS** | Numérico |
| **VLRLAN** | Numérico |
| **CODHIS** | Numérico |
| **COMHIS** | Texto |
| **TIPLAN** | Texto |
| **DATVCT** | **Data (no formato DD/MM/YYYY)** |
| **NUMDOC** | Numérico |
| **CODPROJ** | Numérico |
| **CODEMPORIG** | Numérico |
| **CODEMPDEST** | Numérico |

**![Imagem 7: No entanto, essa linha, pré-indicada na planilha, deve ser excluída antes da importação. Portanto, o arquivo final deve…](https://ajuda.sankhya.com.br/hc/article_attachments/32430774081175) No entanto, essa linha, pré-indicada na planilha,** **deve ser excluída antes da importação.** Portanto, o arquivo final deve conter apenas a linha com os nomes dos campos utilizados pelo sistema, por exemplo: **"NUMLOTE"**, **"NUMLAN"** etc.

**Observação:** a data de vencimento deve estar no formato dd/mm/aaaa, e as datas de referência e movimento devem respeitar os intervalos informados acima.

#### Exemplo de Importação

**Exemplo básico:**

```
NUMLOTE NUMLAN CODCTACTB CODCONPAR REFERENCIA DTMOV CODCENCUS VLRLANC CODHISTCTB COMPLHIST
TIPLANC VENCIMENTO

100     1     1.1.01.001 2.1.01.001 3 15 1001 150000 1 Pagamento fornecedor XYZ D 15/04/2025

100     2     2.1.01.001         3 15 1001 150000 1 Pagamento fornecedor XYZ R 15/04/2025
```

**Exemplo com campos adicionais:**

```
... NUMDOC CODPROJ CODEMPORIG CODEMPDEST

... 12345 100 1 2

... 12345 100 1 2
```

#### Regra de Importação: Código do Projeto (`CODPROJ`)

**Regra para o Campo** `CODPROJ`

Caso a empresa de destino (informada no cabeçalho ou no campo `CODEMPDEST`), no seu cadastro (**tela Empresa - Contabilidade**), estiver configurada para trabalhar com **"Utiliza Projeto"**, o campo `CODPROJ` será sempre **ativo e obrigatório**.

Neste caso, a coluna no arquivo de importação deve estar preenchida, e o projeto (`CODPROJ`) deve existir no sistema Sankhya para a respectiva empresa que está realizando a importação.

Se a empresa **não** estiver marcada para trabalhar com **"Utiliza Projeto"**, o campo `CODPROJ` se torna opcional na importação.

---

#### Regras de Validação

| Categoria | Campo | Regra |
| --- | --- | --- |
| **Datas** | DATVCT | Formato `dd/mm/aaaa` (ex.: 31/12/2025) |
|  | MESMOV | 1 a 12 (mês de referência) |
|  | DIAMOV | 1 a 31 (dentro do mês de movimento) |
| **Números** | VLRLAN | Valor em centavos, sem separadores (ex: R$ 1500,00 = 150000) |
|  | NUMLOTE | 1 a 32767 |
|  | NUMLAN | Não pode ser zero |
|  | CODHISTCTB | Até 32700 |
| **Textos** | CODCTACTB | Código extenso, sem pontuação (Ex: `0101010100004`) |
|  | COMPLHIST | Até 140 caracteres |
|  | TIPLAN | Apenas `D` (Débito) ou `R` (Crédito) |

---

#### Como importar no sistema? (Passos Finais)

**Preparar o arquivo**

- Salvar como XLSX (Excel 2007 ou superior).
- Verificar a ordem das colunas e os nomes na primeira linha.
- **Remover a linha de cabeçalho descritiva** e quaisquer linhas extras ou comentários.

**Configurar no sistema**

- Selecionar tipo de importação: "Arquivo XLS".
- Marcar os campos adicionais (se aplicável).
- Informar empresa de destino (se necessário).

**Validar importação**

O sistema checa automaticamente:

- Contas contábeis cadastradas.
- Centros de custo existentes.
- Históricos válidos.
- Datas consistentes.
- Empresas (quando aplicável).

**Observação Final sobre o Nome do Arquivo:**

O nome do arquivo XLSX precisa estar em **formato simples**, sem caracteres especiais, acentos ou espaços.

| ✅ Exemplos permitidos | ❌ Exemplos que causam erro |
| --- | --- |
| `lote_contabil_2025.xlsx` | `lote contábil março.xlsx` |
| `importacao100.xlsx` | `lançamentos#01.xlsx` |
| `lancamentos_marco.xlsx` | `importação.xlsx` |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116513-Importa%C3%A7%C3%A3o-de-Lote#layoutsparaostiposdearquivo)
