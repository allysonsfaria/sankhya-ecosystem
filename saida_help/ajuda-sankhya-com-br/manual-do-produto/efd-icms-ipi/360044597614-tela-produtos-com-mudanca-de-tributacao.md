---
id: "360044597614"
titulo: "Tela Produtos com Mudança de Tributação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD ICMS/IPI"
atualizado_em: "2026-09-30T11:18:05Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "br.com.sankhya.mgeliv.cad.produtos.mudanca.tributacao", "Produtos com Mudança de Tributação manual", "Fiscal", "Impostos", "EFD", "Estoque", "Preencha \"Empresa\" e \"Dt. Ref. da escrituração\"", "Defina \"Motivo do Inventário\" e \"Custo\"", "Ajuste ICMS e ST conforme regras e opções"]
---

# Tela Produtos com Mudança de Tributação

**Módulo:** Livros Fiscais › Arquivos

**Caminho de acesso:** Menu Principal › Livros Fiscais › Arquivos › Produtos com Mudança de Tributação

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#oque)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#antes)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#comousar)
- [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#geral)
- [Aba Produto Mudança Tributação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#produtomudtrib)
- [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#botoes)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#atencao)

## O que é e para que serve

A **Tela Produtos com Mudança de Tributação** gera as informações que compõem o Inventário de Mudança de Tributação de Produtos em Estoque, sempre que houver alteração na tributação aplicável aos itens. Esse inventário é registrado no arquivo da EFD por meio do `registro H020` do Bloco H, com os valores processados conforme os parâmetros definidos nesta tela. A tela **não** realiza a contagem de estoque nem substitui a configuração das novas regras de tributação — esses procedimentos continuam sendo feitos em outras rotinas, antes de usar esta tela — e também não gera o arquivo da EFD em si; ela apenas alimenta o registro que a EFD vai usar.

![Cabeçalho da tela Produtos com Mudança de Tributação, com os campos Empresa, Status EFD, Dt. Ref. da escrituração e Dt.…](https://ajuda.sankhya.com.br/hc/article_attachments/31912052121495)

---

## Antes de começar

Antes de usar esta tela, garanta os pré-requisitos abaixo, resolvidos fora dela:

- Realize a contagem de estoque na tela Contagem de Estoque, com base na data da mudança de tributação.
- Configure as novas regras de tributação correspondentes aos tributos que sofreram alteração.
- Habilite o registro `H020` nas **Preferências da Empresa**, aba **EFD - Escrituração Fiscal Digital** — sem isso, o registro não é gerado no arquivo. Para saber mais, acesse [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893).
- Cadastre o produto na tela [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) e configure-o para ser considerado na contagem, antes de vinculá-lo nesta tela.

**💡 Dica**

Para o detalhamento campo a campo desta tela, acesse o [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294).

---

## Como usar a tela

Ao acessar a tela, clique em **Novo Registro** para inserir um cadastro. Os registros desta tela são sempre de dois tipos: **Digitados** (inseridos manualmente) ou **Não Digitados** (trazidos pelo botão **Importar**).

![Opções iniciais exibidas ao acessar a tela Produtos com Mudança de Tributação](https://ajuda.sankhya.com.br/hc/article_attachments/17998890270103)

No cabeçalho da tela, preencha:

- **Empresa** — o código da empresa correspondente ao inventário.
- **Status EFD** — campo informativo e somente leitura; o sistema exibe automaticamente **Liberado** ou **Pendente**, conforme a situação da Escrituração Fiscal Digital.
- **Dt. Ref. da escrituração** — a referência de geração da EFD na qual as informações desta tela serão utilizadas.
- **Dt. Mud. Tributação** — a data da mudança de tributação. Se você tentar informar um horário neste campo, o sistema exibe "Não é permitido informar hora em 'Dt. Mud. Tributação'. Por favor, revise o cadastro!"

**ℹ️ Nota**

Para registros de inventário sem relação com mudança de tributação, informe a data na tela [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI) (aba Parâmetros, campo **Data do Inventário**) ou na tela [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI) (aba Configurações, campo **Data do Inventário**).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#sumario)

---

## Aba Geral

Nesta aba você define o custo, o motivo do inventário e as regras de cálculo que serão usadas na geração do registro `H020`.

### Campos gerais

- **Custo** — o custo do inventário considerado na geração do Bloco H. Opções: **Custo de Reposição**, **Custo Gerencial**, **Custo Médio com ICMS**, **Custo Médio sem ICMS**, **Custo Médio Gerencial**, **Custo Variável**, **Entrada com ICMS** e **Entrada sem ICMS**.
- **Considerar empresa p/ busca da última compra** — usada para identificar a última nota de compra do produto; disponível somente quando a marcação **Gerar SPED com os valores de ST (Compra)** estiver desmarcada.
- **Considerar ICMS Anterior e ST Anterior e Extra Nota** — inclui os impostos de ICMS/ST Anterior e Extra Nota na composição dos valores; disponível apenas quando **Gerar SPED com os valores de ST (Compra)** está habilitada.
- **Considerar Operação com Valor Unitário** — considera os valores unitários (em vez de totais) na geração dos registros do SPED Fiscal EFD-ICMS/IPI; disponível apenas quando o campo **Motivo do Inventário** está definido como **02** ou **05**.

#### Gerar SPED com os valores de ST (Compra)

**O que faz:** quando ativada, a rotina de mudança de tributação passa a considerar os impostos retidos nas operações de entrada, usando esses valores na composição do registro de inventário gerado no SPED.

**Quando usar:** use quando o produto já tiver ST retido nas notas de compra e você quiser que esses valores componham o registro H020, em vez de simular os valores a partir de alíquotas.

**Como funciona:** ativada, a tela exibe a seção **Valores Recuperados (Estoque)** na aba Produto Mudança Tributação e habilita as marcações **Separa ICMS Normal e ICMS/ST em dois registros H020**, **Soma ICMS Normal e ICMS/ST em um único registro H020** e **Considerar ICMS Anterior e ST Anterior e Extra Nota**. Desativada, a tela exibe a seção **Valores Simulados**, calculada por alíquota, e habilita o campo **Considerar empresa p/ busca da última compra**.

**Impacto no sistema:** determina a origem dos valores do registro H020 no Bloco H da EFD-ICMS/IPI.

#### Motivo do Inventário

**O que faz:** define o motivo do inventário que comporá o Bloco H na geração da EFD-ICMS/IPI. Opções: **02 - Na mudança de forma de tributação da mercadoria (ICMS)**, **04 - Na alteração de regime de pagamento**, **05 - Por determinação dos fiscos** e **06 - Para controle das mercadorias sujeitas ao regime de ST - restituição/ressarc/compl.**

**Quando usar:** use **02 - Na mudança de forma de tributação da mercadoria (ICMS)** para o cenário padrão desta tela; as demais opções atendem a outros motivos de inventário previstos no Guia Prático da EFD.

**Como funciona:** selecionar **02** ou **05** habilita as marcações **Pela média das notas que amparam o estoque** e **Considerar Operação com Valor Unitário**; com os demais motivos selecionados, essas marcações ficam indisponíveis.

**Impacto no sistema:** define o código do motivo do registro H020 gerado no SPED Fiscal.

#### Pela média das notas que amparam o estoque

**O que faz:** determina se o processamento considera a média das notas de compra que compõem o estoque do produto.

**Quando usar:** disponível apenas quando o campo **Motivo do Inventário** está definido como **02** ou **05**.

**Como funciona:** ativada e processada, o sistema busca as notas de entrada que amparam o estoque e as apresenta na sub-aba **Notas do Produto com Mudança de Tributação**, dentro da aba Produto Mudança Tributação.

**Impacto no sistema:** os valores processados aqui impactam diretamente a geração do registro H020 no SPED Fiscal, pois definem a base de cálculo dos impostos do registro de inventário.

#### Separar ou somar ICMS Normal e ICMS/ST no registro H020

**O que faz:** define se o SPED Fiscal EFD-ICMS/IPI gera um registro H020 único ou dois registros separados para ICMS e ICMS/ST.

**Quando usar:** disponível apenas quando **Gerar SPED com os valores de ST (Compra)** está habilitada. Use **Separa ICMS Normal e ICMS/ST em dois registros H020** quando precisar distinguir os dois impostos no arquivo; use **Soma ICMS Normal e ICMS/ST em um único registro H020** quando eles puderem compor um único registro.

**Como funciona:** com a marcação de separar ativada, as informações da aba Produto com Mudança de Tributação geram registros H020 individuais para cada imposto. Com a marcação de somar ativada, é gerado apenas um registro H020 para ambos.

**Impacto no sistema:** estrutura dos registros gerados no Bloco H da EFD-ICMS/IPI.

### Seção Parâmetros de Cálculo de Impostos

- **Parceiro** — o código do parceiro, previamente cadastrado no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494).
- **Tipo de Operação** — o código da TOP (Tipo de Operação) utilizada.
- **Utilizar alíquota de ICMS para cálculo** — durante a simulação, o sistema busca uma alíquota de ICMS cadastrada; se não encontrar, usa a alíquota informada no campo **Alíquota Interna**.
- **Alíquota Interna** — a alíquota interna aplicada na simulação dos valores.
- **Utilizar valor de custo quando não tiver ST na compra** — usa o valor de custo para compor as informações de ST quando a nota de compra não tiver ST.
- **Usar ST anterior quando não tiver ST na compra** — durante o rastreamento dos produtos, usa o ST anterior quando não encontra o ST na compra.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#sumario)

---

## Aba Produto Mudança Tributação

Nesta aba você associa um produto a uma nova regra de tributação.

![Aba Produto Mudança Tributação, com os campos do produto vinculado à nova regra de tributação](https://ajuda.sankhya.com.br/hc/article_attachments/4416288011671)

### Campos do produto

- **Produto** — o código do item a vincular à regra de tributação; o produto deve estar cadastrado no Cadastro de Produtos e configurado para ser considerado na contagem.
- **Grupo** — o grupo vinculado ao produto.
- **NCM** — o código de oito dígitos da Nomenclatura Comum do Mercosul (NCM).
- **Unidade Padrão** — a unidade de venda do produto (unidade, caixa, pacote, entre outras).
- **Usado como** — a funcionalidade do produto. Opções: **Subproduto**, **Prod. Intermediário**, **Brinde**, **Consumo**, **Revenda (por fórmula)**, **Embalagem**, **Brinde (NF)**, **Imobilizado**, **Matéria-Prima**, **Outros Insumos**, **Em Processo**, **Revenda**, **Terceiros** e **Venda (fabricação própria)**.
- **Estoque** — a quantidade apresentada na contagem de estoque.
- **Digitado?** — indica se o registro é do tipo Digitado ou Não Digitado.
- **Valor de custo utilizado** — quando o sistema não encontra valores de ST no item, usa o custo selecionado no campo **Custo** da aba Geral para preencher os valores do registro H020.

**ℹ️ Nota**

As notas exibidas na sub-aba **Notas do Produto com Mudança de Tributação** são filtradas pela Data de Entrada ou Saída. A opção **Consultar/Alterar Múltiplos Componentes** é habilitada ao selecionar um item.

### Seção Valores Simulados

Esta seção aparece quando a marcação **Gerar SPED com os valores de ST (Compra)** está desativada e os campos da seção Parâmetros de Cálculo de Impostos estão preenchidos. Os valores são calculados com base no custo da mercadoria, aplicando a alíquota obtida na simulação.

![Seção Valores Simulados, com os campos calculados com base no custo e na alíquota da mercadoria](https://ajuda.sankhya.com.br/hc/article_attachments/31912052125079)

- **Cód. Alíq. ICMS** — preenchido automaticamente pelo sistema, conforme o código cadastrado na tela Alíquotas de ICMS.
- **Tributação** — o código da situação tributária, conforme a tela Alíquotas de ICMS, aba Geral, campo Tributação.

#### Base ICMS e Vlr. ICMS

**O que fazem:** compõem a base de cálculo e o valor do ICMS no registro H020.

**Quando usar:** preenchidos sempre que a seção Valores Simulados está ativa.

**Como funciona:** se o CST for diferente de 10, 30, 60 e 70, a **Base ICMS** é o valor do item (valor unitário × quantidade) e o **Vlr. ICMS** é Base de Cálculo H020 × Alíquota.

Exemplo: Base de Cálculo H020 de R$ 150,00 com alíquota de 12% resulta em R$ 150,00 × 0,12 = R$ 18,00.

**Impacto no sistema:** compõe o registro H020 do Bloco H na EFD-ICMS/IPI.

- **MVA** — a Margem de Valor Agregado, conforme a regra fiscal atual do produto.
- **Alíquota ST** — a alíquota de substituição tributária, conforme a regra fiscal atual do produto.

#### Base Substituição e Vlr. Substituição

**O que fazem:** compõem a base de cálculo e o valor da substituição tributária no registro H020.

**Quando usar:** preenchidos quando o CST do produto é 10, 30, 60 ou 70.

**Como funciona:** a **Base Substituição** parte do valor do item (valor unitário × quantidade), majorado pelo MVA: valor do item × (1 + MVA). O **Vlr. Substituição** é (Base de Cálculo H020 × Alíquota ST) − (quantidade em estoque × valor do ICMS unitário).

Exemplo da Base Substituição: valor unitário de R$ 150,00 e MVA de 45,33% resultam em R$ 150,00 × 1,4533 = R$ 218,00.

Exemplo do Vlr. Substituição: Base de Cálculo H020 de R$ 218,00, Alíquota ST de 18%, quantidade de 1 e Valor do ICMS Unitário de R$ 14,40 resultam em (R$ 218,00 × 0,18) − (1 × R$ 14,40) = R$ 39,24 − R$ 14,40 = R$ 24,84.

**Impacto no sistema:** compõe o registro H020 do Bloco H na EFD-ICMS/IPI.

### Seção Valores Recuperados (Estoque)

Esta seção aparece quando a marcação **Gerar SPED com os valores de ST (Compra)**, na aba Geral, está habilitada. Os valores são calculados a partir das notas fiscais de entrada listadas na sub-aba **Notas do Produto com Mudança de Tributação**, desde que a marcação **Pela média das notas que amparam o estoque** também esteja ativada. Se essa marcação estiver desativada, os valores vêm da última nota de compra informada nos campos **Nro. Único Compra** e **Parceiro da Compra**, proporcionalizados ao total do estoque.

![Seção Valores Recuperados (Estoque), com os valores calculados a partir das notas fiscais de entrada](https://ajuda.sankhya.com.br/hc/article_attachments/31912022827031)

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#sumario)

---

## Botões da tela

- **Importar** — busca todos os produtos ativos considerados na contagem de estoque na data informada em **Dt. Mud. Tributação**, na empresa informada, e realiza a importação. Nos registros já Digitados, os valores inseridos não são sobrepostos.
- **Processar** — processa as informações dos produtos Não Digitados. Ao processar novamente a mesma data, o sistema sobrepõe as informações anteriores. Depende do parâmetro **Exigir CR na central/financeiro/rateio?** (`EXIGCRCFR`) para localizar o Centro de Resultado — ver [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#atencao).
- **Liberar EFD** — libera as informações para a geração do Bloco H da EFD-ICMS/IPI; o campo **Status EFD** passa a exibir **Liberado**. Ao gerar a EFD do mês de referência da mudança de tributação, o sistema considera essas informações no preenchimento do Bloco H.
- **Configuração da tela** — reúne a opção **Processar ao importar os produtos**, que realiza a importação e o processamento em uma única ação, inserindo uma linha por produto.
- **Excluir Dig./Não** — abre o pop-up **Excluir os registros**, com três opções: **Digitados** (exclui os registros inseridos manualmente), **Não Digitados** (exclui os registros importados) e **Ambos** (exclui todos os registros desta tela).

**ℹ️ Nota**

Com o parâmetro **Somente produtos ativos ao imp. mud. tributação?** (`PRODATIVMUDTRIB`) desligado, é possível importar produtos que estavam ativos no período da contagem, mesmo que hoje estejam desativados.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614-Tela-Produtos-com-Mudan%C3%A7a-de-Tributa%C3%A7%C3%A3o#sumario)

---

## Pontos de atenção

- Quando o campo **Data do Inventário** está preenchido na tela EFD - Escrituração Fiscal Digital - ICMS/IPI (aba Parâmetros) ou na tela EFD - Fiscal ICMS/IPI (aba Configurações) para o mesmo período em que há lançamentos liberados nesta tela, o sistema gera dois inventários: o padrão de final de período (motivo 01) e o de mudança de tributação (motivo 02).
- O registro `H020` não é gerado para o inventário físico de final de período. Para incluir as informações complementares desse inventário, configure o registro H020 nas Preferências da Empresa, aba EFD - Escrituração Fiscal Digital, sub-aba Blocos e Registros.
- Com o parâmetro **Exigir CR na central/financeiro/rateio?** (`EXIGCRCFR`) habilitado, o botão Processar busca o Centro de Resultado ativo, analítico e com código diferente de 0, de menor código. Se não encontrar nenhum nessas condições, o sistema exibe: "Erro ao tentar inserir modelo de Mudança de Tributação. Não foi encontrado nenhum Centro de Resultado ativo, analítico e diferente de 0. E como o parâmetro 'EXIGCRCFR' está ligado, a operação foi abortada."
