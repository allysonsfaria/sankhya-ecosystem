---
id: "4403603017751"
titulo: "Relatórios Formatados no SankhyaFlow"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow"
trilha: "Manual do Produto > Plataforma e Integrações > Flow"
atualizado_em: "2026-07-29T15:08:42Z"
rotulos: ["Configuração", "Impressão", "Relatórios Formatados", "Estoque", "sankhyaflow", "processos de negócio", "Gere e imprima relatórios para contagem de estoque", "Crie e acesse relatórios formatados com parâmetros do processo", "Personalize e vincule relatórios na Lista de Tarefas"]
---

# Relatórios Formatados no SankhyaFlow

Com o recurso de relatório formatado, o modelador será capaz de vincular relatórios personalizados em tarefas que serão disponibilizadas para impressão na [Lista de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595434-Lista-de-Tarefas).

É possível personalizar o relatório contendo informações do contexto SankhyaFlow, ou seja, dinamicamente o SankhyaFlow irá injetar no relatório o número da Instância do Processo, o Código do usuário de abertura do processo e etc.

O modelador pode criar um relatório personalizado como uma ferramenta acessória do processo, nas situações onde seja necessário gerar uma impressão de documento, como por exemplo, colher a assinatura de um cliente, ou ainda em cenários em que as tarefas são executadas em ambientes sem disponibilidade de acesso ao sistema e uma  impressão com resumo da tarefa te guiará na execução.

Nessas situações, acessamos a Lista de Tarefas e na tarefa existe uma opção em que podemos gerar essas impressões.

Nesse artigo, você terá acesso aos seguintes tópicos:

---

1. [Caso de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#casodeuso)
2. [Criando o Relatório Formatado "Inventário Flow"](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#criandoorelat%C3%B3rioformatadoinvent%C3%A1rioflow)
3. [Configurando e Acessando o Relatório Formatado na Tarefa de Usuário](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#configurandoeacessandoorelat%C3%B3rioformatadonatarefadeusu%C3%A1rio)
4. [Resultado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#resultado)
5. [Demais parâmetros disponíveis no uso do Relatório Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#demaispar%C3%A2metrosdispon%C3%ADveisnousodorelat%C3%B3rioformatado)

---

#### Caso de Uso

O processo de Inventário de Estoque foi criado para identificar os itens que estão armazenados em estoque, analisar se o controle de estoque está compatível com sua realidade e tratar eventuais divergências, da forma mais simples e automatizada possível.

![Imagem 1: O processo de Inventário de Estoque foi criado para identificar os itens que estão armazenados em estoque, analisar se…](https://ajuda.sankhya.com.br/hc/article_attachments/4403597425815)

| **Inventário de Estoque** |
| --- |

Para iniciar o processo de Inventário, precisamos informar a **"Empresa"** que desejamos realizar o inventário e a **"Data de Cópia do Estoque"**.

A tarefa de serviço **"Gravar cópia de estoque"** registrará a cópia no Sankhya Om de acordo com a Empresa e a Data que informamos na abertura do processo. Em seguida, na tarefa **"Contagem de estoque"**, o estoquista irá imprimir o relatório personalizado com os itens do estoque e realizará a contagem física do mesmo, para então retornar a atividade do processo para lançar a contagem feita.

Na sequência, o processo grava esses valores da contagem e, por fim, a última tarefa é para conferir a divergência da contagem, entre o que tinha gravado no sistema e o que existia no estoque real.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#top)

#### Criando o Relatório Formatado "Inventário Flow"

Qualquer cópia de estoque é gerada em função de uma Data de Cópia de Estoque, portanto, esse é o campo principal que vamos utilizar para poder gerar automaticamente o relatório de Inventário Flow.

---

**Inserindo a consulta no relatório**

A consulta foi criada de forma que o valor do campo Data de Cópia do Estoque retornasse do formulário formatado **"AD\_TWFCOPIAESTOQUE"**. A forma que utilizamos para chegar ao valor da Data da Cópia de Estoque é através do Parâmetro Instância do Processo. Por meio desse número, montamos a consulta para acessar a Data de Cópia do Estoque e então passamos como argumento final, para então gerar o relatório contendo os itens de estoque referente à data em que inserimos na abertura do processo.

SELECT DISTINCT CTE.CODPROD AS "CódProd",

                PRO.DESCRPROD AS "DescrProd",

                CTE.CONTROLE AS "Controle\_Adicional",

                CTE.CODVOL AS "CódVol",

                '\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_' AS "Qtd\_Contada",

                LOC.CODLOCAL AS "Cód\_Local",

                LOC.DESCRLOCAL AS "Desc\_Local"

FROM TGFCTE CTE, TGFPRO PRO,

     DUAL,

     TGFLOC LOC

WHERE CTE.CODPROD = PRO.CODPROD

  AND CTE.CODLOCAL = LOC.CODLOCAL

  AND CTE.SEQUENCIA = 1

  AND CTE.DTCONTAGEM = (SELECT DISTINCT DTCONTAGEM 

                 FROM AD\_TWFCOPIAESTOQUE

                  WHERE IDINSTPRN = $P{IDINSTPRN})

ORDER BY "Cód\_Local", "CódProd"

Como dito, foi utilizado o parâmetro $P{IDINSTPRN} (escrito na linha 16). Assim, o SankhyaFlow injetou o valor desse parâmetro quando requisitamos visualizar o Relatório Formatado **"Inventário Flow"**.

---

**Disponibilizando o relatório de exemplo**

O relatório personalizado criado para esse caso de uso pode ser acessado pelos link's abaixo. Vale lembrar que existem conteúdos na Universidade Sankhya referente à criação, formatação de Relatórios Formatados e existe o link para download das ferramentas de criação de relatório.

[Relatório - Inventário Flow](https://drive.google.com/drive/folders/19tDFucHr2eloqPsEto6-__OHtvEzeEZt)

[Universidade Sankhya - Relatório Formatado](https://ead.sankhya.com.br/html/videos.php?curso=2509&up=1)

[Ferramentas iReport e plugins - Download Sankhya](http://downloads.sankhya.com.br/downloads?app=i-Report)

Após baixar o relatório do case, você deve acessar a tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) no Sankhya Om, adicionar um novo relatório, escrever a descrição e por fim subir o arquivo.

Apenas com a descrição e o upload do relatório já será possível utilizá-lo no processo. Observe como fazer:

[GIF animado: Imagem 2: Apenas com a descrição e o upload do relatório já será possível utilizá-lo no processo. Observe como fazer:](https://ajuda.sankhya.com.br/hc/article_attachments/4403626171031)

| **Fazendo upload do Relatório Formatado no Sankhya Om** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#top)

#### Configurando e Acessando o Relatório Formatado na Tarefa de Usuário

Para que a gente possa consumir o relatório, é necessário configurá-lo na tarefa. Para isso, basta dar um duplo clique na tarefa para acessar o painel de configuração.
Esse painel contém a aba [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360047567214?flash_digest=75aac1ec4ff99f4ad0af4f482fd6d45b99c14aaf#abarelat%C3%B3riosformatadostarefasdeusu%C3%A1rio) e, dentro dessa aba, existe um campo de pesquisa por relatórios formatados que a base contém. Abaixo demonstramos o procedimento:

[GIF animado: Imagem 3: Para que a gente possa consumir o relatório, é necessário configurá-lo na tarefa. Para isso, basta dar um duplo clique…](https://ajuda.sankhya.com.br/hc/article_attachments/4403626139671)

| **Configuração do Relatório Formatado** |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#top)

#### Resultado

Dessa forma, podemos gerar a impressão desse relatório na tarefa configurada. Acessamos o relatório na [Lista de Tarefas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595434-Lista-de-Tarefas) e, uma vez posicionado na tarefa em específico, clicamos no botão ![Imagem 4: Dessa forma, podemos gerar a impressão desse relatório na tarefa configurada. Acessamos o relatório na Lista de Tarefas…](https://ajuda.sankhya.com.br/hc/article_attachments/4403605121687) **"Outras opções…"** para visualizar o relatório, conforme demonstramos abaixo:

[GIF animado: Imagem 5: Dessa forma, podemos gerar a impressão desse relatório na tarefa configurada. Acessamos o relatório na Lista de Tarefas…](https://ajuda.sankhya.com.br/hc/article_attachments/4403610680343)

| **Acessando o Relatório** |
| --- |

**Observação:** uma mesma tarefa pode conter vários relatórios.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#top)

#### Demais parâmetros disponíveis no uso do Relatório Formatado

Utilizamos no caso de uso apenas um dos parâmetros disponíveis do contexto SankhyaFlow. Caso você queira, é possível utilizar outros parâmetros, sendo eles:

---

**Instância Processo**

**CODPRN -** Recebe BigDecimal

**VERSAO -** Recebe BigDecimal

**IDINSTPRN -** Recebe BigDecimal

**CODUSUINC -** Recebe BigDecimal

---

**Instância Tarefa**

**IDINSTTAR -** Recebe BigDecimal

**IDELEMENTO -** Recebe String

**NOMEELEMENTO -** Recebe String

**CODUSUDONO -** Recebe BigDecimal

---

O modelador então tem a liberdade de montar uma consulta munida desses parâmetros listados acima. Com eles é possível acessar qualquer informação contida em tabelas do SankhyaFlow ou de Formulários de processos modelados no SankhyaFlow.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403603017751-Relat%C3%B3rios-Formatados-no-SankhyaFlow#top)
