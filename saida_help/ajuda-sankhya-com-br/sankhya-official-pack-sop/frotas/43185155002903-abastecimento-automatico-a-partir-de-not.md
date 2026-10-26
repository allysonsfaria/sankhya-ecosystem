---
id: "43185155002903"
titulo: "Abastecimento Automático a partir de Nota de Compra de Combustível"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43185155002903-Abastecimento-Autom%C3%A1tico-a-partir-de-Nota-de-Compra-de-Combust%C3%ADvel"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-09-29T14:43:58Z"
rotulos: ["Abastecimento Automático", "Nota de Compra de Combustível", "registro de abastecimento"]
---

# Abastecimento Automático a partir de Nota de Compra de Combustível

Este manual explica como configurar o Sankhya para que, ao confirmar uma **nota de compra de combustível em posto externo**, o sistema **crie automaticamente o registro de abastecimento** correspondente — sem que o usuário precise digitar nada na tela de Abastecimentos. Em resumo, o fluxo é: **nota de compra de combustível confirmada → sistema lê produto, veículo, motorista e quilometragem → abastecimento é criado sozinho**, já vinculado à nota que o originou. 

O documento cobre a configuração principal na tela Tipos de Operação - TOP, os requisitos complementares em outras telas, as regras de negócio observadas, os pontos de atenção mais comuns e um roteiro de teste para validar tudo antes de liberar aos usuários. 

### Fluxo de Entrada — Passo a Passo

Mapa de leitura rápido do processo completo — cada passo é detalhado nas seções seguintes.

(1)** Configuração** — ligar as marcações na TOP de compra, preencher o Tipo de Combustível nos produtos e revisar a permissão de alteração nas Configurações do Gestão de Frotas.

(2)** Lançamento da Nota de Entrada** — a nota de compra de combustível é lançada pelo **Portal de Compra**, trazendo os dados do arquivo eletrônico do posto.

(3)** Validações** — o sistema confere: marcação ligada na TOP, itens com Tipo de Combustível informado, veículo e quilometragem preenchidos, ausência de liberação pendente e inexistência de abastecimento já lançado para aquela nota.

(4)** Registro da Nota de Compra** — a nota é confirmada normalmente.

**(5)** **Registro do Lançamento de Abastecimento** — o abastecimento é criado automaticamente, já vinculado à nota, com Tipo de Inclusão "Nota Fiscal" e Status "Não Inserido". 

| **Como usar este manual:** este documento apresenta o processo do ponto de vista de quem opera no dia a dia — como a nota de compra de combustível gera o abastecimento automaticamente, o que conferir e o que fazer quando algo não sai como esperado. As telas citadas aparecem ilustradas ao longo do texto. |
| --- |

### Acesso à Tela

A configuração principal deste fluxo fica na tela **Tipos de Operação - TOP** (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP)

**A complementar:** identificador interno (resourceID) da tela Tipos de Operação - TOP ainda não confirmado. 

![Imagem 1: A complementar: identificador interno (resourceID) da tela Tipos de Operação - TOP ainda não confirmado.](https://ajuda.sankhya.com.br/hc/article_attachments/43186380464535)

Tela Tipos de Operação - TOP — registro 9, "NOTA DE COMPRA LANÇA ABASTECIMENTO", aba Geral. Os quatro campos em verde estão ligados; "Gerar abastecimento na confirmação" (destaque amarelo) é o campo que efetivamente dispara a criação do abastecimento. 

### Pré-Requisitos

##### **(1)** Uma Tipos de Operação - TOP de compra (tipo de movimento C-Compra) configurada para a nota de combustível — no ambiente descrito neste manual, o registro 9 - Nota de Compra Lança Abastecimento.

##### **(2)** Produtos de combustível cadastrados no Cadastro de Produtos com o campo Tipo de Combustível preenchido.

##### **(3)** Cadastro de veículos e motoristas completo e ativo (placa e CPF corretos). 4 Parceiro do posto marcado como Posto no Cadastro de Parceiros.

##### **(4)** Parceiro motorista marcado como Motorista no Cadastro de Parceiros.

##### **(4)** Padrão de observação fiscal combinado com o fornecedor de combustível (placa, CPF do motorista e KM/ODÔMETRO reconhecíveis), quando a nota chegar por arquivo eletrônico.

##### **(5)** Configurações do Gestão de Frotas revisadas, em especial o campo Permite Alterar Abastecimento com Requisição Gerada.

##### **(6)** Perfil de acesso do usuário com permissão para lançar/confirmar notas de entrada e para consultar a tela de Abastecimentos.

##### **(7)** Ambiente de homologação/teste disponível para rodar o roteiro de teste ponta a ponta antes de usar em produção.

### Visão Geral da Tela

Na tela Tipos de Operação - TOP, o cabeçalho do registro traz os campos **Cód.Tipo Operação**, **Descrição**, **Tipo de movimento**, **Ativo** e **Grupo**. Para o fluxo de abastecimento automático, o registro de referência é o de tipo de movimento **C-Compra**, situação **Ativo** e grupo **Compra**. 

Na **aba Geral** desse registro ficam os campos relevantes para este manual, sempre no formato de chave liga/desliga: 

- **Importar Motorista da Observação:** lê o CPF escrito na observação da nota e preenche o motorista do abastecimento.
- **Importar Veículo da Observação:** lê a placa escrita na observação da nota e preenche o veículo.
- **Importar KM da Observação:** lê o odômetro escrito na observação e preenche a quilometragem.
- **Gerar abastecimento na confirmação:** é o campo que efetivamente cria o abastecimento quando a nota é confirmada.

| **Importante:** os três campos "Importar ... da Observação" são **auxiliares** — eles só servem para preencher veículo, motorista e quilometragem automaticamente quando a nota chega por arquivo eletrônico. Quem de fato dispara a criação do abastecimento é o campo **Gerar abastecimento na confirmação**. Se o usuário preferir digitar veículo e quilometragem manualmente na nota, os três campos de importação podem ficar desligados — mas veículo e quilometragem precisam estar preenchidos de algum jeito para o abastecimento ser gerado. |
| --- |

### Configurações Complementares Necessárias

Além de ligar o campo **Gerar abastecimento na confirmação** na TOP, outros pontos de configuração e regras de contexto precisam estar corretos para o abastecimento ser criado.

#### 1. Tipos de Operação - TOP da nota de compra

Na TOP usada para lançar a nota de compra (entrada) de combustível, o campo **Gerar abastecimento na confirmação**, na aba Geral, precisa estar ligado. Esta é a configuração central descrita na seção Acesso à Tela acima.

#### 2. Cadastro de Produtos — Tipo de Combustível

No **Cadastro de Produtos**, cada produto de combustível precisa ter o campo **Tipo de Combustível** preenchido. Somente os itens da nota cujo produto tem esse campo informado entram no abastecimento gerado. **Este é o ponto que mais causa o sintoma "configurei e não gerou".**

Menu: **(caminho de menu a confirmar)**

![Imagem 2: Menu: (caminho de menu a confirmar)](https://ajuda.sankhya.com.br/hc/article_attachments/43186380465943)

Cadastro de Produtos — produto "DIESEL S10". O campo **Tipo de Combustível** fica no tema **Gestão de Frotas**, aqui preenchido com "Diesel". É esse preenchimento que faz o item da nota ser reconhecido como combustível. 

#### 3. Veículo e quilometragem informados na nota

A nota precisa ter **veículo** e **quilometragem** informados — normalmente vindos da observação fiscal do arquivo eletrônico da nota de entrada, lidos pelos campos "Importar ... da Observação", ou digitados manualmente na nota quando esses campos estiverem desligados. 

#### 4. Liberação da nota (alçada)

A nota **não pode estar com liberação pendente** (regra de alçada) no momento da confirmação. Enquanto a liberação estiver pendente, o abastecimento não é gerado. 

#### 5. Abastecimento único por nota

**Não pode existir abastecimento já lançado para aquela nota.** O sistema aceita apenas um registro de abastecimento por nota — não há geração duplicada. 

#### 6. Configurações do Gestão de Frotas

Nas **Configurações do Gestão de Frotas**, avaliar o campo **Permite Alterar Abastecimento com Requisição Gerada**, que define se o abastecimento criado automaticamente poderá ser editado depois. 

Menu: **(caminho de menu a confirmar)**

![Imagem 3: Menu: (caminho de menu a confirmar)](https://ajuda.sankhya.com.br/hc/article_attachments/43186380466711)

Configurações do Gestão de Frotas, seção **Abastecimento**. O campo **Permite Alterar Abastecimento com Requisição Gerada** (em destaque) está ligado, permitindo editar o abastecimento depois de criado. 

#### 7. Parceiro do Posto — marcação Posto

O registro de abastecimento só aceita, no campo **Posto**, um parceiro que esteja marcado como **Posto** no **Cadastro de Parceiros**. Não é uma recomendação — é uma restrição do próprio sistema: parceiro sem essa marcação não é aceito no campo. 

Menu: **(caminho de menu a confirmar)**

![Imagem 4: Menu: (caminho de menu a confirmar)](https://ajuda.sankhya.com.br/hc/article_attachments/43186380467735)

Cadastro de Parceiros — parceiro "POSTO RECREIO". A chave **Posto** fica no **cabeçalho do cadastro**, logo abaixo de Tipo de pessoa, e precisa estar ligada. 

#### 8. Parceiro Motorista — marcação Motorista

Da mesma forma, o campo **Motorista** do abastecimento só aceita um parceiro marcado como **Motorista** no **Cadastro de Parceiros**. 

Menu: **(caminho de menu a confirmar)**

![Imagem 5: Menu: (caminho de menu a confirmar)](https://ajuda.sankhya.com.br/hc/article_attachments/43186380469911)

Cadastro de Parceiros — parceiro motorista. Diferente da chave Posto, a marcação **Motorista** fica **dentro do campo Tipo**: abra a lista e ligue a opção Motorista. No exemplo, o parceiro é Fornecedor e Motorista ao mesmo tempo.

 

| **No fluxo automático, essas duas marcações não são um detalhe cadastral — são parte da configuração.** O campo Posto do abastecimento é preenchido com o fornecedor da nota de compra, e o campo Motorista com o motorista informado na nota. Se o fornecedor da nota não estiver marcado como Posto, ou o motorista não estiver marcado como Motorista, a criação do abastecimento não se completa — e, como já documentado, a nota é confirmada normalmente e nenhuma mensagem aparece. Consequência prática: ao cadastrar um posto novo de combustível, marcar o parceiro como Posto passa a ser parte da configuração deste fluxo, não um detalhe esquecível; o mesmo vale para motoristas novos. Este é exatamente o cenário que o passo 6 do Roteiro de Teste Ponta a Ponta (cenário de falha proposital) serve para comprovar. |
| --- |

| **Não confundir com Posto Interno.** O Cadastro de Parceiros também tem a marcação "Posto Interno", usada para postos próprios da empresa. Ela não é requisito deste fluxo — a marcação exigida aqui é apenas "Posto". |
| --- |

### Leitura Automática de Veículo, Motorista e Quilometragem

Quando a nota de compra de combustível chega pelo arquivo eletrônico do posto, os dados do abastecimento costumam vir escritos no campo de **observação** da nota. As marcações **Importar Veículo da Observação**, **Importar Motorista da Observação** e **Importar KM da Observação** (aba Geral da tela Tipos de Operação - TOP) mandam o sistema procurar essas informações dentro desse texto. 

O sistema já vem com um padrão de leitura de fábrica. As preferências desta seção só precisam ser preenchidas **quando o posto escreve a observação em formato diferente do esperado**. 

| **Caso feliz — nada a configurar:** se a observação vier neste formato, o padrão de fábrica já lê sozinho, sem preencher nenhuma preferência:    ``` PLACA: ABC1D23 - MOTORISTA CPF 12345678901 - ODOMETRO: 123456 ```   Resultado: veículo, motorista e quilometragem preenchidos sozinhos na nota. Antes de customizar qualquer coisa, teste o formato real do posto — ele pode já funcionar sem ajuste nenhum |
| --- |

**Onde se preenche:** tela de **Preferências**, no grupo de configurações do módulo de Logística. Localizar a preferência pela chave. 

Menu: **(caminho de menu a confirmar)**

| **Preferência** | **Para que serve** | **Preencher quando** |
| --- | --- | --- |
| **RGXPLACAXML** | Padrão de leitura da placa   dentro da observação | O posto escreve a placa em minúsculas ou em formato   diferente |
| **RGXCPFMOTXML** | Padrão de leitura do CPF do   motorista | O CPF vem em formato   diferente do esperado |
| **RGXKMODOXML** | Padrão de leitura do   odômetro/quilometragem | O posto usa outra palavra   antes do número (ex.:   "HODOMETRO", "ODOM.") |

As três preferências já nascem **em branco**. Em branco significa "usar o padrão de fábrica" — não significa desligado. 

### Exemplos prontos para colar

**Placa escrita em minúscula ou mista** (ex.: abc1d23 ) — preencher **RGXPLACAXML** com:

```
(?i)\b[A-Z]{3}-?\d[A-Z0-9]\d{2}\b
```

**Odômetro com outra palavra antes do número** (ex.: HODOMETRO 123456 ou ODOM. 123456 ) — preencher **RGXKMODOXML** com: 

```
(?i)\b(?:H?OD[ÔO]METRO|ODOM\.?|KM)\s*[:\-]?\s*([\d.,]+)\b
```

**Posto que só usa placa no formato antigo** (ex.: ABC-1234 ) — preencher **RGXPLACAXML** com: 

```
\b[A-Z]{3}-?\d{4}\b
```

### Cuidados

| **Só altere com apoio técnico.** O conteúdo dessas preferências é uma expressão de busca; um valor mal formado faz o sistema deixar de encontrar a informação, sem apresentar erro. |
| --- |

| **No padrão da quilometragem, os parênteses são obrigatórios.** É o trecho entre parênteses que o sistema aproveita como número. Sem eles, a quilometragem não é preenchida. |
| --- |

| **Nos padrões de placa e de CPF vale o contrário:** o padrão deve delimitar apenas a placa ou apenas o CPF. Se incluir a palavra "PLACA:" no padrão, essa palavra passa a fazer parte do valor procurado e o veículo não é encontrado. |
| --- |

| **Placa e CPF diferenciam maiúsculas de minúsculas; a quilometragem não.** Por isso o exemplo de placa em minúscula começa com (?i) . |
| --- |

| **CPF com pontuação não é localizado.** Se a observação trouxer o CPF no formato 123.456.789-01 , o sistema procura o motorista exatamente com essa pontuação, enquanto o cadastro guarda apenas os números — nenhuma alteração de preferência resolve isso. Duas saídas: pedir ao posto o CPF sem pontuação, ou simplesmente deixar em branco, porque quando a placa é localizada o sistema já traz o motorista a partir da composição do veículo e, na falta dela, do próprio cadastro do veículo. Na prática, acertar a leitura da placa costuma resolver o motorista. |
| --- |

| **Quilometragem com separador:** 123.456 é entendido como 123456; valores com casas decimais são arredondados para número inteiro. Se o texto não puder ser convertido em número, a nota segue sem a quilometragem, sem aviso. |
| --- |

| **Bônus quando a placa é localizada:** além do veículo, o sistema também preenche o Centro de Resultado da nota a partir do cadastro do veículo. |
| --- |

### Como Funciona o Fluxo de Geração Automática

Existem, na prática, três caminhos possíveis a partir da mesma configuração: 

- **Nota eletrônica com leitura automática da observação** — a nota chega por arquivo eletrônico já com placa, CPF do motorista e KM/ODÔMETRO na observação fiscal; o sistema lê tudo sozinho.
- **Nota lançada manualmente** — o usuário digita veículo e quilometragem diretamente na nota, sem depender da leitura automática da observação.
- **Regularização de notas antigas** — para notas confirmadas antes de a configuração ser ligada, existe um botão específico para gerar o abastecimento retroativamente.

### Fluxo Operacional — Nota Eletrônica com Leitura Automática da Observação

Use este fluxo quando a nota de compra de combustível chega por arquivo eletrônico (NF-e) do fornecedor, com a observação fiscal já preenchida.

(1)** Receber a nota eletrônica** — a nota chega por arquivo eletrônico do fornecedor e é lançada no **Portal de Compra**, com a observação fiscal já preenchida pelo posto, contendo placa, CPF do motorista e KM/ODÔMETRO. 

| **Exemplo real do lançamento:** a imagem da seção Fluxo Operacional — Regularização de Notas Antigas mostra uma nota de compra de combustível já lançada, com Veículo, Motorista, Placa e KM preenchidos no cabeçalho e o texto da observação visível — exatamente o cenário descrito neste passo. |
| --- |

(2)** Conferir a TOP vinculada à nota** — confirmar que a Tipos de Operação - TOP usada está com Gerar abastecimento na confirmação ligado, na aba Geral (ver print na seção Acesso à Tela).

(3)** Conferir o produto de combustível** — validar que o item da nota está associado a um produto com Tipo de Combustível preenchido no Cadastro de Produtos.

(4)** Confirmar a nota** — confirmar o documento de entrada normalmente.

(5)** Sistema lê a observação e gera o abastecimento** — veículo, motorista e quilometragem são preenchidos automaticamente; o abastecimento nasce com Tipo de Inclusão = Nota Fiscal e Status = Não Inserido.

(6)** Conferir na tela de Abastecimentos** — localizar o registro gerado na listagem e abrir o detalhe para validar os dados (veículo, motorista, quilometragem, litros, valores, média). 

### Fluxo Operacional — Nota Lançada Manualmente

Use este fluxo quando a nota não traz observação fiscal reconhecível, ou quando a empresa optar por não usar os campos de importação automática.

(1)** Lançar a nota de compra** — usar a TOP com Gerar abastecimento na confirmação ligado. 

(2)** Informar o veículo manualmente na nota** — preencher o campo de veículo diretamente, sem depender da leitura da observação.

(3)** Informar a quilometragem manualmente na nota** — preencher o odômetro do veículo no momento do abastecimento.

(4)** Conferir o produto de combustível** — mesmo requisito do fluxo eletrônico: Tipo de Combustível preenchido no Cadastro de Produtos.

(5)** Confirmar a nota** — o abastecimento é gerado com os dados digitados manualmente.

(6)** Conferir na tela de Abastecimentos** — validar o registro criado. 

| **Importante:** neste fluxo, os campos "Importar ... da Observação" podem ficar desligados na TOP — eles não são obrigatórios. O único campo indispensável para a geração automática é Gerar abastecimento na confirmação. |
| --- |

### Fluxo Operacional — Regularização de Notas Antigas

Use este fluxo para notas de compra de combustível que já foram confirmadas **antes** de a configuração Gerar abastecimento na confirmação ser ligada, e que por isso não geraram abastecimento na época.

(1)** Localizar as notas antigas** — na tela de notas, identificar as notas de compra de combustível já confirmadas sem abastecimento vinculado.

(2)** Selecionar as notas** — marcar as notas que devem ser regularizadas. 

(3)** Acionar o botão Gerar Abastecimento** — disponível na tela de notas, cria o abastecimento das notas selecionadas já confirmadas.

(4)** Conferir na tela de Abastecimentos** — validar se os registros foram criados corretamente para as notas regularizadas. 

![Imagem 6: (4) Conferir na tela de Abastecimentos — validar se os registros foram criados corretamente para as notas regularizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/43186391347479)

Central de Compras — nota de compra de combustível. No menu de ações (ícone de raio), a opção **Gerar Abastecimento** cria o abastecimento de notas já confirmadas. Repare no cabeçalho: **Veículo**, **Motorista**, **Placa** e **KM** preenchidos, e a **Observação** com o texto ODOMETRO: 879897 PLACA: SNK2O22 — exatamente o formato que a leitura automática reconhece sem nenhuma customização. 

### Roteiro de Teste Ponta a Ponta

Antes de liberar a configuração para os usuários, execute este roteiro em ambiente de homologação: 

**(1)** **Cadastrar/ajustar a TOP** — Gerar abastecimento na confirmação ligado na Tipos de Operação - TOP de compra de combustível.

**(2)** **Conferir o produto de combustível** — Tipo de Combustível preenchido no Cadastro de Produtos para o item de teste.

**(3)** **Lançar uma nota de teste** — com veículo e quilometragem informados (via observação eletrônica ou digitação manual).

**(4)** **Confirmar a nota de teste.**

(5)** Verificar o registro na tela de Abastecimentos** — conferir Tipo de Inclusão = Nota Fiscal, Status = Não Inserido, e os dados de veículo/motorista/quilometragem/valores.

**(6)** **Testar um cenário de falha proposital** — por exemplo, um produto sem Tipo de Combustível preenchido — e confirmar que a nota é confirmada normalmente, sem mensagem de erro, e que nenhum abastecimento é gerado. Isso mostra, na prática, o comportamento silencioso descrito ao longo deste manual: quando algum requisito falta, a nota é confirmada e o abastecimento simplesmente não aparece. 

### Indicadores de Acompanhamento

Depois de ligar a configuração, acompanhe estes pontos para garantir que o fluxo automático está funcionando de forma saudável: 

| **Indicador** | **O que acompanhar** |
| --- | --- |
| Abastecimentos gerados por nota | Quantidade de registros com Tipo de Inclusão = Nota Fiscal no período — mostra o volume que está sendo automatizado. |
| Notas de combustível   confirmadas sem   abastecimento gerado | Sinal de falha silenciosa a investigar (produto sem Tipo de Combustível, nota sem veículo/KM, etc.). |
| Média de consumo por   veículo | Evolução mês a mês; quedas ou picos bruscos   costumam indicar quilometragem digitada errada na nota. |
| Abastecimentos bloqueados para edição | Quantidade de registros gerados por nota que não podem mais ser alterados, conforme o campo Permite Alterar Abastecimento com Requisição Gerada. |

| **A complementar:** relatório ou dashboard oficial para acompanhar esses indicadores (nome da tela e caminho de menu) — a confirmar com o time de BI/Frotas. |
| --- |

### Regras de Negócio

| **Regra** | **Descrição** |
| --- | --- |
| RN001 | O campo Gerar abastecimento na confirmação, na Tipos de Operação - TOP da nota de compra, é a regra mestra: sem ele, nenhum abastecimento é criado. |
| RN002 | Somente os itens da nota cujo produto tem o Tipo de Combustível preenchido no Cadastro de Produtos entram no abastecimento gerado. |
| RN003 | A nota precisa ter veículo e quilometragem informados (via observação lida automaticamente ou digitação manual) para o abastecimento ser gerado. |
| RN004 | Nota com liberação pendente (alçada) não gera abastecimento até ser liberada e confirmada. |
| RN005 | Só é permitido um abastecimento por nota; não existe geração duplicada para a mesma nota. |
| RN006 | O abastecimento criado nasce com Tipo de Inclusão = Nota Fiscal e Status = Não Inserido, já vinculado à nota de origem. |
| RN007 | Se qualquer requisito não for atendido, a nota é confirmada normalmente e nenhuma mensagem de erro é exibida — a criação do abastecimento falha silenciosamente. |
| RN008 | Quantidade em litros, valor unitário, desconto e valor total do abastecimento são copiados dos itens da nota; as regras de precificação do lançamento manual (custo médio, último preço de compra, digitação de valor unitário) não se aplicam neste caminho. |
| RN009 | A média de consumo de cada item é calculada usando a quilometragem informada na nota e a do abastecimento anterior do mesmo veículo. |
| RN010 | Se o campo Permite Alterar Abastecimento com Requisição Gerada, nas Configurações do Gestão de Frotas, estiver desligado, o abastecimento gerado por nota não pode ser alterado nem receber novos itens. |
| RN011 | Uma vez gerado o abastecimento, o sistema impede a troca do veículo na nota, avisando que já existe abastecimento gerado. |
| RN012 | A leitura automática da observação reconhece placa, CPF do motorista e o odômetro (aceita as palavras "KM" ou "ODÔMETRO" antes do número); leiautes diferentes exigem ajuste de parâmetro pelo time técnico. |
| RN013 | Para notas confirmadas antes de a configuração ser ativada, o botão Gerar Abastecimento na tela de notas permite regularizar retroativamente. |
| RN014 | Os três campos "Importar ... da Observação" são auxiliares, não obrigatórios: preenchendo veículo e quilometragem manualmente na nota, o campo Gerar abastecimento na confirmação funciona da mesma forma. |
| RN015 | O abastecimento gerado automaticamente fica vinculado à nota que o originou para fins de rastreabilidade e conferência. |
| RN016 | O campo Posto do abastecimento só aceita parceiro marcado como Posto, e o campo Motorista só aceita parceiro marcado como Motorista, ambos no Cadastro de Parceiros; sem essas marcações, o abastecimento não é gerado. |

| **A complementar:** regras de alçada/liberação específicas (quem libera, valores de corte) e o conjunto completo de valores possíveis para o Status do abastecimento (além de Não Inserido) ainda não foram detalhados — a confirmar com o time funcional. |
| --- |

### Boas Práticas Operacionais

- **Conferir a tela de Abastecimentos logo após confirmar notas de combustível.** Como a falha na geração é silenciosa, não dá para confiar apenas na ausência de erro. **2** **Cadastrar o Tipo de Combustível em todo produto de combustível assim que ele for criado**, antes da primeira nota chegar.
- **Padronizar com o fornecedor o formato da observação fiscal** (placa, CPF, KM/ODÔMETRO) para garantir a leitura automática.
- **Definir conscientemente o campo Permite Alterar Abastecimento com Requisição Gerada**, alinhando com o time de frotas se a prioridade é flexibilidade ou proteção do histórico.
- **Revisar periodicamente a média de consumo dos veículos** para detectar quilometragem digitada errada na nota.
- **Rodar o roteiro de teste ponta a ponta** sempre que alterar a TOP, o Cadastro de Produtos ou as Configurações do Gestão de Frotas.
- **Usar o botão Gerar Abastecimento com critério**, revisando as notas antigas antes de regularizar em lote.
- **Avisar os usuários que confirmam notas** de que um abastecimento gerado automaticamente pode ficar bloqueado para edição, conforme a configuração vigente.

### Perguntas Frequentes

- **Confirmei a nota e não gerou nada, e agora?**

Confira, nesta ordem: (1) a TOP usada na nota está com Gerar abastecimento na confirmação ligado; (2) o produto de combustível do item tem Tipo de Combustível preenchido no Cadastro de Produtos; (3) a nota tem veículo e quilometragem informados; (4) não havia liberação pendente na nota; (5) não existe abastecimento anterior para essa mesma nota. Se tudo estiver certo e mesmo assim não gerar, use o botão Gerar Abastecimento na tela de notas ou acione o time técnico. 

- **Por que não consigo editar o abastecimento gerado?**

Porque, nas Configurações do Gestão de Frotas, o campo Permite Alterar Abastecimento com Requisição Gerada está desligado — o sistema bloqueia alteração e inclusão de itens nesse abastecimento, com a mensagem "Não é permitido alterações após a geração da requisição". 

- **Gerou o abastecimento, mas ficou sem alguns itens da nota. Por quê?**

Só entram no abastecimento os itens cujo produto tem o Tipo de Combustível preenchido no Cadastro de Produtos; itens sem essa informação são ignorados na geração. 

- **A média de consumo saiu errada. O que verificar?**

A média usa a quilometragem informada na nota e a do abastecimento anterior do mesmo veículo. Confira se a quilometragem lançada (ou importada da observação) está correta. 

- **Posso gerar de novo o abastecimento para a mesma nota?**

Não. O sistema aceita apenas um abastecimento por nota. 

- **Posso trocar o veículo da nota depois que o abastecimento já foi gerado?**

Não. O sistema bloqueia a troca do veículo na nota, avisando que já existe abastecimento gerado. É preciso ajustar diretamente no abastecimento, se a configuração permitir, ou tratar o caso com o time responsável. 

- **E as notas que já foram confirmadas antes de eu ligar a configuração?**

Use o botão Gerar Abastecimento na tela de notas para essas notas antigas já confirmadas — ele regulariza o passado. 

- **O fornecedor escreve a observação de um jeito diferente do padrão. O que fazer?**

O padrão de leitura da observação pode ser ajustado por parâmetro do sistema; acione o time técnico para adequar ao formato do fornecedor. 

- **Confirmei a nota e o abastecimento não foi criado, e o produto está certo — o que mais verificar?**

Depois de conferir o Tipo de Combustível no produto, a causa mais comum é o Cadastro de Parceiros: o parceiro informado como posto (fornecedor da nota) precisa estar marcado como Posto, e o parceiro informado como motorista precisa estar marcado como Motorista. Sem essas duas marcações, o abastecimento não é gerado — e, como nos demais casos, sem nenhuma mensagem de erro. 

### Telas Relacionadas

- **Tipos de Operação - TOP** — configuração central deste fluxo (menu: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).
- **Cadastro de Produtos** — onde se preenche o Tipo de Combustível dos itens (caminho de menu a confirmar).
- **Configurações do Gestão de Frotas** — onde fica o campo Permite Alterar Abastecimento com Requisição Gerada (caminho de menu a confirmar).
- **Abastecimentos** — onde o registro criado automaticamente é conferido e consultado (caminho de menu a confirmar).
- **Notas de Entrada/Compra** — origem do processo; também é onde fica o botão Gerar Abastecimento para regularização de notas antigas (caminho de menu a confirmar).
- **Portal de Compra** — tela onde a nota de compra de combustível é lançada, trazendo os dados do arquivo eletrônico do posto (caminho de menu a confirmar).
- **Cadastro de Parceiros** — onde ficam as marcações Posto e Motorista, exigidas pelo abastecimento (caminho de menu a confirmar).
