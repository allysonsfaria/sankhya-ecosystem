---
id: "7267044122263"
titulo: "Tela EFD - Fiscal ICMS/IPI (Flex e HTML5)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD ICMS/IPI"
atualizado_em: "2026-09-30T11:14:44Z"
rotulos: ["Configuração", "Fiscal", "IPI", "SEFAZ", "ICMS", "Impostos", "EFD", "br.com.sankhya.mgeliv.mov.efdfiscal.icmsipi", "UFEFDVLMERC", "Processamento EFD 017 - Versão 116", "Layouts a partir de 2021", "Configurações do EFD - Sub-abas", "LIVCODCONTAMAT"]
---

# Tela EFD - Fiscal ICMS/IPI (Flex e HTML5)

**Neste artigo**

- [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#oque)
- [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#antes)
- [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#comousar)
- [Diferenças entre as telas Flex e HTML5](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#diferencas)
- [Aba Configurações (HTML5) / aba Parâmetros (Flex)](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#config)
- [Botões da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#botoes)
- [Demais abas da tela — Blocos 0 a 9 (exclusivo HTML5)](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocos)
- [Verificação de divergências](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#divergencias)
- [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#atencao)

## O que é e para que serve

A **Escrituração Fiscal Digital (EFD)** é um arquivo digital constituído de um conjunto de escriturações de documentos fiscais e de outras informações de interesse dos fiscos das Unidades Federadas e da Secretaria da Receita Federal do Brasil, bem como de registros de apuração de impostos referentes às operações e prestações praticadas pelo contribuinte.

Este artigo cobre as duas versões da tela:

- **EFD - Escrituração Fiscal Digital ICMS/IPI (Flex)** — versão anterior, mantida em paralelo. Gera os layouts 001 a 017 (versões 1.00 a 1.16).
- **EFD - Fiscal ICMS/IPI (HTML5)** — versão atual. Gera os layouts 015 a 021 (versões 1.14 a 1.20), de 2021 em diante.

A tela produz o arquivo TXT para submissão ao Programa Validador e Assinador (PVA) do fisco; ela **não** valida, assina nem transmite a escrituração — essas etapas continuam sendo feitas no PVA. Para o detalhamento campo a campo de cada registro, consulte o [Guia Prático da EFD ICMS/IPI](http://sped.rfb.gov.br/pasta/show/1573) vigente.

**ℹ️ Nota**

Na tela HTML5 é possível gerar apenas os layouts a partir do exercício de **2021 (Layout 015 / Versão 1.14)**. Ao tentar gerar um layout anterior, o sistema exibe a mensagem: "Prezado usuário, para geração de arquivos em layout's anteriores ao exercício 2021 (Layout 015/Versão114), acessar a rotina: EFD - Escrituração Fiscal Digital ICMS/IPI em (Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI)."

---

## Antes de começar

Garanta os pré-requisitos abaixo, todos resolvidos fora desta tela:

- **Configurar os blocos e registros da EFD** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893), aba **EFD - Escrituração Fiscal Digital**, sub-aba **Blocos e Registros**. É aqui que se define quais registros serão gerados e a estrutura hierárquica pai-filho entre eles, além do campo **Tipo de Escrituração** (selecione **EFD**).
- **Definir a forma de busca da conta contábil** usada nos registros do arquivo, no campo **Tipo da Conta Contábil para EFD ICMS/IPI** (**Preferências da Empresa › aba EFD - Escrituração Fiscal Digital**), com as opções **Cadastros** e **Contabilização**. O registro **H010** tem regra própria, com parâmetros específicos (`EFDH010`, `EFDH010_PRTER` e `EFDH010_TER`, os campos equivalentes nas Preferências da Empresa e as Contas Contábeis 1 a 4 do Cadastro de Produtos). O procedimento completo está em [Geração da Conta Contábil para EFD - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703).
- **Revisar os cadastros que alimentam os registros**: [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113), [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494), Cadastro de Cidades e [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173).
- **(Flex)** Nenhum parâmetro de habilitação é necessário — a tela está disponível para todos os contribuintes.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Como usar a tela

O preenchimento inicial define a empresa, o período e a versão do layout. Em seguida, configure as abas e gere o arquivo. Na versão HTML5, o resultado só aparece nas abas por bloco após o **Processar**.

### Preenchimentos iniciais (Flex e HTML5)

Os campos de preenchimento inicial são os mesmos nas duas versões; muda apenas onde eles aparecem:

- **Na HTML5** — o **painel principal** traz Empresa, Referência, Versão do Layout e Arquivo confirmado; os demais campos (Código da Finalidade do Arquivo, Período, UF, Finalidade de Apresentação do Arquivo, Data do inventário, Data da contagem p/ K200, Perfil EFD e Nro. Único Nota) ficam na **aba Configurações**.
- **Na Flex** — o **painel principal** traz Empresa, UF e Período; os demais ficam na **aba Parâmetros**.

Campos:

- **Empresa** — a primeira informação a ser preenchida: a empresa da qual serão gerados os dados para escrituração. Mantendo o campo **em branco**, é possível, previamente à geração, selecionar **várias ou todas as empresas** configuradas para gerar a EFD; na HTML5, isso permite a geração prévia de dados ou o processamento simultâneo de múltiplas empresas.
- **Referência** (HTML5) — informe o primeiro dia do mês/ano para o qual o arquivo será gerado.
- **Período** — a abrangência da geração, informada por uma **Data Inicial** e uma **Data Final**. Na HTML5, o período é baseado na data de Referência do painel principal.
- **UF** — a Unidade Federada a ser considerada para a geração do arquivo.
- **Finalidade de Apresentação do Arquivo** — o objetivo da geração, com as opções **Remessa do arquivo original** e **Remessa do arquivo substituto**.
- **Versão do Layout** — campo **sem edição**; exibe a versão do layout utilizada, definida automaticamente de acordo com o período informado. Na Flex o campo se chama **Versão do Layout do Arquivo**.
- **Arquivo confirmado** (HTML5) — ao marcar, o sistema **bloqueia qualquer reprocessamento** do arquivo.
- **Data do inventário** — a data que o sistema considera para a geração da escrituração.
- **Data de Inventário em substituição ao Bloco K** — destinada à geração do **H005 na posição mensal**, em substituição ao Bloco K: o sistema gera um Bloco H correspondente à **cópia de estoque** registrada na data informada. Exibida quando o parâmetro `GERBLHSUBSK` ("Gerar Bloco H em substituição ao Bloco K") está ligado. **Sempre que houver Bloco H para a data informada, o sistema deixa de gerar o Bloco K.**
- **Utilizar dados do inventário mensal** (HTML5) — modal com as opções **Pela cópia** e **Pela contagem**, para definir qual posição de estoque será utilizada no EFD: gerar o H005 pelos saldos da **cópia de estoque** ou pelos saldos da **contagem de estoque** da data informada.
- **Data da contagem p/ K200** — data da contagem para a geração do registro **K200** na tela [Dashboard auxiliar do BLOCO K](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159), usada após a execução de cópia e contagem de estoque no processo de inventário. Exibida quando o parâmetro `GERAK200CTE` está ligado. Com o parâmetro **desligado**, considera-se o estoque do **último dia** do período da geração do SPED Fiscal.
- **Perfil EFD** — o perfil no qual o arquivo será gerado.
- **Nro. Único Nota** — quando informado, o sistema gera as informações apenas da nota indicada.

**Regras de conflito entre as datas de inventário** (com `GERBLHSUBSK` e `GERAK200CTE` ligados simultaneamente):

| Situação | Comportamento |
| --- | --- |
| As duas datas preenchidas | O sistema exibe a mensagem: "O campo 'Data de contagem p/ K200' não pode estar preenchido se o campo 'Data de Inventario em substituição ao Bloco K' também estiver preenchido. Defina qual data será utilizada para a geração do arquivo." |
| Só a **Data da contagem p/ K200** | Gera o Bloco K no Dashboard, depois do inventário |
| Só a **Data de Inventário em substituição ao Bloco K** | Gera o Bloco H substituindo o Bloco K |
| As duas vazias | O sistema exibe a mensagem: "O parâmetro GERAK200CTE está ligado, então a 'Data da Contagem p/ K200' deve ser informada." |

### Versões de layout

A versão do layout é determinada pelo período informado — na HTML5, pelo período da **Referência**. A tela **Flex** gera os layouts **001 a 017** (versões 1.00 a 1.16); a tela **HTML5** gera os layouts **015 a 021** (versões 1.14 a 1.20).

| Código | Versão | Leiaute instituído por | Vigência (início) | Vigência (fim) | Gerada em |
| --- | --- | --- | --- | --- | --- |
| 001 | 1.00 | Ato COTEPE | 01/01/2008 | 31/12/2008 | Flex |
| 002 | 1.01 | Ato COTEPE | 01/01/2009 | 31/12/2009 | Flex |
| 003 | 1.02 | Ato COTEPE | 01/01/2010 | 31/12/2010 | Flex |
| 004 | 1.03 | Ato COTEPE | 01/01/2011 | 31/12/2011 | Flex |
| 005 | 1.04 | Ato COTEPE | 01/01/2012 | 30/06/2012 | Flex |
| 006 | 1.05 | Ato COTEPE | 01/07/2012 | 31/12/2012 | Flex |
| 007 | 1.06 | Ato COTEPE | 01/01/2013 | 31/12/2013 | Flex |
| 008 | 1.07 | Ato COTEPE | 01/01/2014 | 31/12/2014 | Flex |
| 009 | 1.08 | Ato COTEPE | 01/01/2015 | 31/12/2015 | Flex |
| 010 | 1.09 | Ato COTEPE | 01/01/2016 | 31/12/2016 | Flex |
| 011 | 1.10 | Ato COTEPE | 01/01/2017 | 31/12/2017 | Flex |
| 012 | 1.11 | Ato COTEPE | 01/01/2018 | 31/12/2018 | Flex |
| 013 | 1.12 | Ato COTEPE/ICMS nº 44/2018 | 01/01/2019 | 31/12/2019 | Flex |
| 014 | 1.13 | Ato COTEPE | 01/01/2020 | 31/12/2020 | Flex |
| 015 | 1.14 | Ato COTEPE | 01/01/2021 | 31/12/2021 | Flex e HTML5 |
| 016 | 1.15 | Ato COTEPE | 01/01/2022 | 31/12/2022 | Flex e HTML5 |
| 017 | 1.16 | Ato COTEPE | 01/01/2023 | 31/12/2023 | Flex e HTML5 |
| 018 | 1.17 | Ato COTEPE | 01/01/2024 | 31/12/2024 | HTML5 |
| 019 | 1.18 | Ato COTEPE | 01/01/2025 | 31/12/2025 | HTML5 |
| 020 | 1.19 | Ato COTEPE/ICMS nº 79/2025 | 01/01/2026 | 31/12/2026 | HTML5 |
| 021 | 1.20 | Ato COTEPE/ICMS (v. 3.2.x/futura) | 01/01/2027 | — | HTML5 |

**Últimas publicações do Ato COTEPE** — além do leiaute 013 (v. 3.0), instituído pelo **Ato COTEPE/ICMS nº 44/2018**, com obrigatoriedade em 01/01/2019, e do leiaute **020 (NT 2025.001)**, instituído pelo **Ato COTEPE/ICMS nº 79/2025**, com obrigatoriedade em 01/01/2026, já está publicado o leiaute **021 (NT 2026.001)**, versão **1.20**, com obrigatoriedade a partir de **01/01/2027**.

O sistema seleciona a versão automaticamente, conforme o período: qualquer escrituração com data-base **igual ou posterior a 01/01/2026**, por exemplo, usa a **Versão 1.19 (Código 020)**, do novo leiaute 3.1.9/3.2.0 da Reforma Tributária do Consumo — ver o tópico [Adequação do ERP ao SPED Fiscal (EFD-ICMS/IPI) 3.1.9 e 3.2.0](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#adequacaodoerpaospedfiscalefdicmsipi319e320).

**ℹ️ Nota**

Na HTML5, o campo **Versão do Layout** é apresentado sem possibilidade de edição e exibe a versão utilizada na geração da escrituração. Na Flex, o campo equivalente é **Versão do Layout do Arquivo**, também sem edição.

### Inclusão e exclusão de referência (HTML5)

- Ao informar a **mesma Empresa** em uma **Referência posterior** a uma já processada, os dados da sub-aba **Restituição/Complementação de ST** são **copiados automaticamente** do período anterior. Porém, caso haja uma nova inclusão e essa aba já possua preenchimento, o processo de cópia **não** será efetuado.
- Ao **excluir uma referência**, todas as movimentações e registros dela são **excluídos do banco de dados**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Diferenças entre as telas Flex e HTML5

As duas versões geram o mesmo arquivo da EFD ICMS/IPI e compartilham as mesmas configurações e regras de registro. As diferenças de interface e de fluxo estão resumidas abaixo.

| Recurso | EFD - Escrituração Fiscal Digital (Flex) | EFD - Fiscal ICMS/IPI (HTML5) |
| --- | --- | --- |
| **Disponibilidade** | Versão anterior, mantida em paralelo. Gera layouts anteriores a 2021. | Versão atual. Gera layouts de 2021 em diante. |
| **Preenchimentos iniciais** | Painel principal (Empresa, UF, Período) + aba **Parâmetros** (Finalidade de Apresentação, Versão do Layout, Data do inventário, Data de Inventário em substituição ao Bloco K, Data da contagem p/ K200, Perfil EFD, Nro. Único Nota). | Painel principal (Empresa, Referência, Versão do Layout, Arquivo confirmado) + aba **Configurações** (Código da Finalidade do Arquivo, Período, UF, Finalidade de Apresentação do Arquivo, Data do inventário, Data da contagem p/ K200, Perfil EFD, Nro. Único Nota). |
| **Organização dos registros** | Seis abas de configuração (Parâmetros, Opções, Restituição/Complementação de ST, Sub-Apuração EFD, Prodepe, Arquivos para Registro D695). | Aba **Configurações** com sub-abas + abas por bloco (0, B, C, D, E, G, H, K, 1 e 9), preenchidas após o **Processar**. |
| **Fluxo de geração** | **Gerar Arquivo** produz o TXT diretamente. | **Processar** preenche as abas por bloco e depois **Gerar** produz o TXT. |
| **Consulta e histórico** | Botões **Histórico de gerações** e **Consultar Nota Não Gerada**. | Botão **Histórico de Gerações** (modal **Processos**). |
| **Confirmação do arquivo** | Não possui. | Campo **Arquivo confirmado**, que bloqueia o reprocessamento. |
| **Versões de layout geradas** | Layouts **001 a 017** (versões 1.00 a 1.16), de 01/01/2008 a 31/12/2023. | Layouts **015 a 021** (versões 1.14 a 1.20), de 01/01/2021 em diante. |

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Aba Configurações (HTML5) / aba Parâmetros (Flex)

Este tópico reúne as parametrizações necessárias para a geração do arquivo EFD. Todos os campos descritos aqui são comuns às duas versões da tela: o que muda é apenas onde eles aparecem — na versão HTML5, como **sub-abas da aba Configurações**; na versão Flex, como **abas próprias da tela** (Opções, Restituição/Complementação de ST, Prodepe, Sub-Apuração EFD e Arquivos para Registro D695). Os poucos campos exclusivos de uma das versões estão sinalizados com **(Flex)** ou **(HTML5)** ao lado do nome.

### Sub-aba Opções

#### Campos de custo

- **Tirar Serviços do valor contábil** — quando marcada, se a nota fiscal possuir serviços entre os itens, os valores desses serviços não serão considerados na geração dos dados.
- **Custo para o Inventário** — determina o método de custo aplicado na geração do **Bloco H (Inventário)**. Opções: **Médio com ICMS**, **Médio sem ICMS**, **Gerencial**, **Reposição** e **Usar maior custo**. Ao selecionar **Usar maior custo**, é habilitada a seção **Maior Custo para valor do item**, na qual você informa **dois tipos de custo** para comparação (Médio Gerencial, Médio com ICMS, Médio sem ICMS, Gerencial, Reposição) — prevalece o de maior valor.
- **Custo para Inventário/Efeitos IR (Campo 11/reg. H010)** — determina o custo considerado no **campo 11 do registro H010**. Mesmas opções do campo anterior. **Habilitado apenas para períodos posteriores a 31/12/2014.** Ao selecionar **Usar maior custo**, é habilitada a seção **Maior Custo para efeitos de IR**, que compara dois tipos de custo e aplica o maior ao campo 11.
- **Substituir saldo credor sub-apuração ICMS** — opções **Não substituir** (mantém os saldos existentes) e **De todas Sub-Apurações** (exclui/deleta cada sub-apuração quando o valor credor do mês difere do novo valor credor).

#### Marcações

| Marcação | O que faz |
| --- | --- |
| **Gerar Registro C170/C173/C176 para NF-e de emissão própria** | Na geração do SPED Fiscal são apresentados os registros C170, C173 e C176 para NF-e de emissão própria (as demais notas já geram o C170 naturalmente). |
| **Gerar registros C110/C111/C112/C113/C114/C115 para NF-e de emissão própria** | Para empresas que precisam gerar todos os registros filhos do C100, por contabilidade externa ou fins fiscais. A geração respeita a hierarquia C113 → C110 → 0450. |
| **Gerar o item da Nota com Unidade Comercializada** | Apresenta o registro **0220 - FATORES DE CONVERSÃO DE UNIDADES** com a unidade alternativa informada nos lançamentos. Se não acionada, apenas o registro **0200** é gerado, na Unidade Padrão. |
| **Item de cupom fiscal com 'Código do Produto para NF-e' vazio, usar o parâmetro IMPREFCUPOM** | Marcar quando o Parceiro utiliza a referência na impressão de cupons e o Produto não possui o campo **Cód. Produto p/ NF-e** preenchido. |
| **Apresenta K200 estoque escriturado negativo para conferência** | Permite visualizar produtos com estoque negativo **apenas para conferência**; sem a marcação, somente o estoque positivo é gerado. O validador do SPED não aceita estoque negativo. |
| **Incluir estoque de terceiro a partir das movimentações, no Registro H010?** | Selecione apenas quando existir controle de estoque envolvendo terceiros. |
| **Excluir registro H010 para itens cuja quantidade tenha mais de 3 casas decimais** | Os itens cuja quantidade em estoque tenha mais de três casas decimais não são levados ao H010, evitando a rejeição do arquivo no validador do SPED. |
| **Gerar o registro H020 para inventário motivo 01** | Gera o inventário de final de período (Motivo = 01) com os campos pertinentes ao H020, conforme a legislação da SEFAZ do **Rio Grande do Sul**. Exige o campo **Data do inventário** preenchido. |
| **Gerar BC e ICMS no H020 para Inventário Motivo 01** (HTML5) | Liberada apenas com a marcação anterior habilitada. Com ambas ativas e **CST = 000**, gera um H020 para cada H010 (quando H005 = 01), preenchendo automaticamente **Base de cálculo do ICMS** e **Valor do ICMS a ser debitado ou creditado**. |
| **Considera valor unitário para os campos BC\_ICMS e VL\_ICMS do registro H020** (HTML5) | Ativar junto com as demais configurações de H020; garante que o H020 utilize corretamente o valor unitário. |
| **Conversão CST 090 Para CST 00 na geração do registro H020** | Converte o CST 090 em CST 00 na geração do H020. |
| **Gerar registro H020 do CST anterior a mudança de tributação** (Flex) | Gera o H020 demonstrando as informações **antes e depois** da mudança de tributação — o H020 sai **duas vezes** para o produto. **Descontinuado na HTML5** quando a rotina **Produtos com Mudança de Tributação** foi reformulada; na Flex, que não recebe melhorias, o comportamento anterior é mantido. |
| **Gerar registro D190 pela Escrituração Fiscal** (HTML5) | Prioriza as informações registradas no **Livro Fiscal** no formato de geração do D190. Caso contrário, considera as informações da Central. |
| **Gera valores PIS/COFINS no EFD? (É dispensado para quem entrega EFD Contribuições)** | Gera os valores de PIS/COFINS no EFD. É dispensada para quem entrega a EFD Contribuições separadamente. |
| **Gerar registro 1600 pelo Resumo de Operações com Cartão?** | O sistema usa os dados da tela [Resumo de Operações com Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595154) para o tratamento manual das informações do Registro 1600. Desabilitada, o sistema não utiliza esses dados. |
| **Gerar registro 1601 pelo Resumo de Operações com Cartão?** | Idem, para o **Registro 1601**. |
| **Gerar registro C191 mesmo que o ICMS/ST esteja majorando com o FCP?** | Mesmo que o FCP esteja junto ao ICMS/ST no registro C190, os valores do FCP são gerados no C191. |

**⚠️ Atenção**

As marcações **Conversão CST 090 Para CST 00 na geração do registro H020** e **Gerar registro H020 do CST anterior a mudança de tributação** **não podem ser habilitadas conjuntamente**.

**Procedimento da conversão CST 090 → CST 00:**

1. Execute a **cópia e a contagem de estoque**.
2. Faça a configuração na **aba Geral** da tela [Produtos com Mudança de Tributação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597614).
3. Importe e processe os produtos, identificando os que estão com **CST 090**.
4. Libere para a EFD os registros com CST 090.
5. Acione a marcação.

#### Conteúdo do campo DESCR\_COMPL do Reg. C170 (parâmetro DESCPRODFORNEC)

Define o conteúdo do campo **04 - DESCR\_COMPL** do C170, com as alternativas **Padrão Complemento**, **Descrição do Produto Equivalente** e **A partir da função** (função `SNK_GET_DESCPROD_PARC`). Liga-se à tela **Produtos Equivalentes**.

#### Cod. Cont. Origem no Reg C170 Contabil. por Matriz (parâmetro LIVCODCONTAMAT)

Habilitar quando houver transferência entre empresas que utilizam o mesmo plano de contas, contabilizando na matriz. Define a conta contábil de origem no C170.

#### Regras do registro 0220 detalhadas nesta aba

- É preciso marcar **Gerar Registro** para o 0220 nas **Preferências da Empresa › aba EFD - Escrituração Fiscal Digital › sub-aba Blocos e Registros**. Sem isso, o sistema exibe a mensagem: "Atenção: A opção 'Gerar o Item da Nota com a Unidade Comercializada' será desmarcada porque o registro '0220' não está marcado para ser gerado."
- Se o produto possuir **mais de uma unidade alternativa para o mesmo volume**, diferenciando-se pelo **Controle**, **apenas o primeiro volume alternativo** encontrado na geração será gerado no 0220; os demais saem com o volume padrão.
- O item é gerado em **Unidade Padrão** quando:
- Registros envolvidos nessa configuração: **0190** (Identificação das Unidades de Medida), **0200** (Tabela de Identificação do Item), **0220** (Fatores de Conversão de Unidades), **C170** (Itens do Documento) e **H010** (Inventário).

### Sub-aba Restituição/Complementação de ST

Permite configurar as informações para o cálculo dos valores médios conforme a necessidade. Contribuintes de **Minas Gerais** devem consultar o artigo [Instruções para geração dos Registros EFD ICMS/IPI - Restituição/Ressarcimento ICMS ST Minas Gerais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057819854).

**Campos:**

- **Data do inventário** — data para a realização da geração dos cálculos.
- **Tipo de inventário** — opções **Cópia** e **Contagem**.
- **Valor do ICMS da Operação** — campo de fórmula.
- **Base de ST** — campo de fórmula.
- **Valor de ST** — campo de fórmula.
- **Valor do FCP de ST** — campo de fórmula.
- **Filtro Personalizado** — campo de fórmula/filtro customizado.

**Marcações:** **Ignorar filtro padrão** e **Recalcula Inventario**, usadas conforme a necessidade (também citadas no tópico do [Registro C180](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registroc180), como opcionais para o ressarcimento de ST).

**Botões auxiliares:**

- **Construtor** — auxilia na construção das fórmulas personalizadas.
- **Utilizar padrão** — restaura/aplica a fórmula padrão do sistema.

**Histórico de fórmulas:** ao alterar qualquer um dos campos **Valor do ICMS da Operação**, **Base de ST**, **Valor de ST**, **Valor do FCP de ST** e **Filtro Personalizado**, a fórmula utilizada anteriormente fica gravada na rotina [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594), aba **Fórmula Sped**, pasta **EFD**.

**Cópia entre períodos (HTML5):** os dados desta sub-aba são copiados do período anterior quando a mesma empresa é informada em uma referência posterior — exceto se a aba já possuir preenchimento na nova inclusão.

### Sub-aba Prodepe

Realiza as configurações e os cálculos referentes ao **Benefício PRODEPE** (Pernambuco); vincula-se ao **Registro C177** nas Preferências da Empresa.

**Campos:**

- **Indicador de enquadramento** — opções:
- **Indicador de Sub-Apuração** — seleciona o tipo de sub-apuração ao qual o registro pertence.
- **Cód. do Produto Sem Incentivo** — preenchido com o respectivo código PRODEPE referente ao Registro C177 quando, no **Cadastro de Produtos › aba Impostos**, o campo **Indicador Esp. Inc. PRODEPE/FUNCRESCE** estiver com a marcação **Sem incentivo** selecionada.

### Sub-aba Sub-Apuração EFD

Aba de visualização, sem preenchimento manual. Demonstra as informações referentes ao **valor do saldo credor** no momento da geração do EFD, em **duas grades**: uma representa o saldo credor do **mês anterior** e a outra, o do **mês atual**. Os dados são calculados automaticamente.

### Sub-aba Arquivos para Registro D695

Permite **vincular os arquivos** que as empresas enquadradas no **Convênio ICMS 115/03** entregam mensalmente. Esse arquivo alimenta os campos dos registros **D695** e **D696**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Botões da tela

### HTML5

- **Processar** — executa a geração e o preenchimento das abas de registros conforme as abas Parâmetros e Opções. Após processar um período, é necessário **reprocessar** para salvar modificações em registros ou alterações de configuração.
- **Gerar** — realiza a geração do arquivo de escrituração conforme as abas Parâmetros e Opções.

  **ℹ️ Nota**

  Ao gerar os registros **C100, C460, C500, C800, D100 e D500** com Data de Referência **igual ou superior a 01/01/2023**, as movimentações com situação de documento **04 - NF-e, NFC-e ou CT-e Denegado** e **05 - NF-e, NFC-e ou CT-e Numeração inutilizada** **não são apresentadas no arquivo TXT**.
- **Histórico de Gerações** — permite visualizar o histórico das gerações de arquivo realizadas; ao acioná-lo, o modal **Processos** é exibido na tela.
- **Excluir** — remove **um registro por vez**; não permite a exclusão múltipla de registros.

**Painel de controle das abas por bloco.** Depois do **Processar**, cada aba por bloco traz um painel de controle sobre a grade de registros, com as ações:

- **Incluir** — adiciona manualmente um registro à aba, para os casos em que o dado não vem das movimentações.
- **Excluir** — deleta um registro de cada vez; não permite a exclusão múltipla.
- **Navegação entre registros** — percorre os registros da grade (primeiro, anterior, próximo e último), permitindo conferir linha a linha antes de gerar.

As alterações feitas pelo painel são salvas ao acionar o **Processar** novamente.

### Flex

- **Gerar Arquivo** — realiza a geração do arquivo de escrituração de acordo com as condições estabelecidas nas abas **Parâmetros** e **Opções**. Exibe um modal ao ser acionado.

  **ℹ️ Nota**

  Durante a geração, as movimentações com situações de documento **04** (NF-e, NFC-e ou CT-e Denegado) e **05** (NF-e, NFC-e ou CT-e Numeração inutilizada) **não são apresentadas no arquivo TXT**.
- **Histórico de gerações** — visualiza o histórico das gerações de arquivo realizadas anteriormente, em tela dedicada.
- **Consultar Nota Não Gerada** — permite consultar alguma nota que não tenha sido gerada no livro. Após informar os dados da nota e clicar em **Consultar**, a consulta pode retornar quatro situações:

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Demais abas da tela — Blocos 0 a 9 (exclusivo HTML5)

**ℹ️ Nota**

As abas por bloco existem **apenas na versão HTML5**. Na Flex, o arquivo é gerado diretamente pelo botão **Gerar Arquivo**, sem grade de conferência por registro. As regras de geração descritas neste tópico, porém, valem para as **duas versões**.

Na versão HTML5, após o **Processar**, a tela organiza o resultado em abas por bloco de registro, conforme o layout da Receita Federal: **0000, 0001, B001, C001, D001, E001, G001, H001, K001, 1001, 9001 e 9999**.

| Aba | Registros contidos |
| --- | --- |
| **0001** (Bloco 0) | 0002, 0005, 0015, 0100, 0150, 0175, 0190, 0200, 0205, 0206, 0210, 0220, 0300, 0305, 0400, 0450, 0460, 0500 e 0600 |
| **B001** (Bloco B) | B020, B025, B420, B440, B460 e B470 |
| **C001** (Bloco C) | C100, C101, C110, C120, C130, C140, C141, C160, C170, C172, C173, C176, C177, C178, C180, C181, C185, C186, C190, C191, C195, C197, C300, C310, C320, C321, C350, C370, C390, C400, C405, C410, C420, C425, C460, C470, C490, C495, C500, C590, C591, C595, C597, C800, C850, C855, C857, C860, C890, C895 e C897 |
| **D001** (Bloco D) | D100, D101, D110, D120, D130, D160, D161, D190, D195, D197 e D500 |
| **E001** (Bloco E) | E100, E110, E111, E112, E115, E116, E200, E210, E220, E230, E240, E250, E300, E310, E311, E312, E313, E316, E500, E510, E520, E530 e E531 |
| **G001** (Bloco G) | G110, G125, G126, G130 e G140 |
| **H001** (Bloco H) | H005, H010, H020 e H030 |
| **K001** (Bloco K) | K010, K100, K200, K210, K215, K220, K230, K235, K250, K255, K260, K265, K280, K290, K291 e K292 |
| **1001** (Bloco 1) | 1010, 1100, 1105, 1110, 1200, 1210, 1250, 1255, 1400, 1600, 1601, 1900, 1910, 1920, 1921, 1922, 1923, 1925, 1926, 1960, 1970, 1975 e 1980 |
| **9001** (Bloco 9) | 9900 |
| **9999** | Registro 9999 |

### Neste tópico

- [**Bloco 0**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#bloco0) — [Unidades de medida](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#unidadesdemedida) · [Registro 0205](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0205) · [Registro 0221](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0221) · [Registro 0300](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0300) · [Registro 0450](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0450) · [Registro 0500](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro0500)
- [**Bloco B**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocob)
- [**Bloco C**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blococ) — [Registro C100](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registroc100) · [Registros 0450, C110 e C113](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros0450c110ec113) · [Registros C170, C173 e C176](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrosc170c173ec176) · [Registro C177](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registroc177) · [Registro C180](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registroc180) · [Registros C190 e C191](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrosc190ec191) · [Registros C800, C855/C857 e C895/C897](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrosc800c855c857ec895c897)
- [**Bloco D**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocod) — [Registro D100](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrod100) · [Registro D190](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrod190) · [Registros D695 e D696](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrosd695ed696) · [Consolidação da NFCom](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#consolidacaodanfcom)
- [**Bloco E**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocoe) — [Apuração do ICMS (E100 a E316)](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#apuracaodoicmse100ae316) · [Número do processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#numerodoprocesso) · [Ajuste automático do IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#ajusteautomaticodoipi) · [Diferencial de Alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#diferencialdealiquota)
- [**Bloco G**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocog) — [Registros 0300 e G125](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros0300eg125) · [Devoluções de venda no CIAP](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#devolucoesdevendanociap) · [Composição da Receita Bruta para o Bloco G (CIAP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#composicaodareceitabrutaparaoblocogciap)
- [**Bloco H**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocoh)
- [**Bloco K**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#blocok) — [K010](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k010) · [K100](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k100) · [K200](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k200) · [K210](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k210) · [K215](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k215) · [K220](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k220) · [K230](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k230) · [K235](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k235) · [K250](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k250) · [K255](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k255) · [K260 e K265](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k260ek265) · [K280](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k280) · [K290, K291 e K292](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#k290k291ek292) · [Substituição do Bloco K pelo Bloco H](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#substituicaodoblocokpeloblocoh)
- [**Bloco 1**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#bloco1) — [Registro 1400](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro1400) · [Registros 1600 e 1601](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros1600e1601) · [Registro 1960](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registro1960) · [Registros 1970 e 1980 (PRODEPE/FUNCRESCE)](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros1970e1980prodepefuncresce) · [Número do processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#numerodoprocesso2)
- [**Bloco 9**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#bloco9)
- [**Adequação do ERP ao SPED Fiscal (EFD-ICMS/IPI) 3.1.9 e 3.2.0**](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#adequacaodoerpaospedfiscalefdicmsipi319e320) — [Atualização e vigência do leiaute](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#atualizacaoevigenciadoleiaute) · [Ajustes em registros](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#ajustesemregistros) · [Considerações para a escrituração dos novos tributos (CBS, IBS e IS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#consideracoesparaaescrituracaodosnovostributoscbsibseis)

### Bloco 0

O Bloco 0 traz a abertura do arquivo e os cadastros de apoio: itens, participantes, unidades de medida e referências.

#### Unidades de medida — registros 0190, 0200 e 0220

O registro **0190** identifica as unidades de medida; o **0200** é a Tabela de Identificação do Item (Produto e Serviços), cujo **campo 06** é o **UNID\_INV**; o **0220** traz os Fatores de Conversão de Unidades.

O 0220 é gerado quando a marcação **Gerar o item da Nota com Unidade Comercializada** está acionada, apresentando a unidade alternativa informada nos lançamentos. Sem a marcação, apenas o registro **0200** é gerado, na Unidade Padrão.

**Configuração obrigatória:** é preciso marcar **Gerar Registro** para o 0220 nas **Preferências da Empresa › aba EFD - Escrituração Fiscal Digital › sub-aba Blocos e Registros**. Sem isso, o sistema exibe a mensagem: "Atenção: A opção 'Gerar o Item da Nota com a Unidade Comercializada' será desmarcada porque o registro '0220' não está marcado para ser gerado."

**Regra do Controle:** se o produto possuir **mais de uma unidade alternativa para o mesmo volume**, diferenciando-se pelo campo **Controle**, **apenas o primeiro volume alternativo** encontrado na geração será gerado no 0220; os demais saem com o volume padrão.

**O item é gerado em Unidade Padrão quando:**

1. nas Preferências da Empresa, o registro **0220** estiver **desmarcado**;
2. a nota for **NF-e de emissão própria** e o parâmetro `USARUNIDPADNFE` estiver ligado;
3. a nota **não** for NF-e e a marcação **Gerar o Item da Nota com a Unidade Comercializada** **não** estiver realizada;
4. o produto possuir **duas unidades alternativas iguais**, diferenciadas apenas pelo campo **Controle**.

Registros envolvidos nessa configuração: **0190**, **0200**, **0220**, **C170** e **H010**.

#### Registro 0205 — alteração da descrição do item

- A geração deve ocorrer **no mês em que a alteração da descrição do produto foi realizada**, desde que haja **movimentação do produto** nesse período.
- **Sem movimentação no mês da alteração**, o 0205 é gerado **no primeiro período subsequente em que houver movimentação** do produto.
- Condições: alteração registrada no cadastro do produto; movimentação fiscal obrigatória; retroatividade apenas ao primeiro período com movimento.
- Vinculado às configurações de geração de registros do **Bloco 0** nas **Preferências da Empresa › aba EFD - Escrituração Fiscal Digital › sub-aba Blocos e Registros**.

#### Registro 0221 — correlação de itens

**Finalidade:** correlação de mercadorias para revenda equivalentes — produtos similares, kits/cestas e substituições.

**Configurações obrigatórias:**

1. Nas **Preferências da Empresa**, aba **EFD - Escrituração Fiscal Digital**, com tipo de escrituração **EFD**, cadastre o registro **0221** no Bloco 0.
2. No **Cadastro de Produtos, aba Geral**, o produto deve estar classificado como **Mercadoria para Revenda** no campo **Tipo do Item/Sped**, **ou** como **Revenda** no campo **Usado como**.
3. Para **kits/cestas**, vincule os componentes pela aba **Componentes** do Cadastro de Produtos, indicando a quantidade de cada componente.

**Configuração por empresa** (aba **Impostos / Informações por empresa**):

- Configure a empresa como **Mercadoria para Revenda** no campo **Tipo do item p/ SPED** da sub-aba **Geral**; **ou**
- Configure **Tipo do item p/ SPED** como **Utilizar do 'Uso do Produto'** e defina **Uso do Produto** como **Revenda**.
- Nessa modalidade, o sistema considera as informações desta aba, **desconsiderando o que estiver configurado na aba Geral**.

**Campo crítico — Cód. Produto p/ NF-e/NFC-e/CF-e (seção NF-E):** se um produto for lançado em duas notas no mesmo mês com preenchimentos diferentes nesse campo, serão gerados registros **0200 e 0221** para esse produto. Quando se usa o código da **Referência** e o campo **Referência** da aba Geral estiver sem preenchimento, o sistema exibe a mensagem: "O produto XXX está com o campo 'Referência' sem preenchimento."

**Limitação:** o registro **não engloba produtos semelhantes com códigos de produto diferentes** — se existirem dois produtos semelhantes com cadastros/códigos diversos, o sistema não os correlaciona no 0221.

**Acesso à geração:** tela **EFD - Fiscal ICMS/IPI**, aba **0001**, sub-aba **0200**.

#### Registro 0300

Identificação do bem ou componente. As regras de geração e a relação com o CIAP estão no **Bloco G**, no tópico [Registros 0300 e G125](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros0300eg125).

**Conta contábil do registro.** A hierarquia de busca é:

1. **Cadastro de Produtos**, aba **Impostos**.
2. **Tipos de Operação (TOP)**, aba **Livro Fiscal**.

O campo **Conta Contábil para EFD** do Cadastro de Produtos (aba **Impostos**, seção **EFD Fiscal/Contribuições/Reinf/Sintegra**) aplica-se a produtos classificados como **bem do ativo imobilizado** e só é usado quando as **duas condições** abaixo são atendidas:

1. a conta contábil está **ligada à empresa** no plano de contas (**Preferências da Empresa**, aba **Contabilidade**);
2. o campo **Natureza para EFD** (aba **Geral** do produto) está configurado como **11 - Máquinas e Equipamentos do Ativo Imobilizado, ativo fixo, etc.**

Se qualquer uma dessas condições não for atendida, o sistema preenche o registro com a conta indicada no campo **Conta Contábil 1** do Cadastro de Produtos. As duas formas de busca da conta — modos **Cadastros** e **Contabilização** — e a tabela de naturezas aceitas por registro estão em [Geração da Conta Contábil para EFD - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703).

#### Registro 0450

Registro complementar, gerado quando a nota possui Observação Padrão configurada como **Informação Complementar do Documento Fiscal**. O procedimento completo está no **Bloco C**, no tópico [Registros 0450, C110 e C113](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registros0450c110ec113).

#### Registro 0500

Gerado conforme o **Cadastro de Plano de Contas** da empresa. Se as filiais forem incluídas no arquivo, seus planos de contas também são gerados. **Apenas as contas que aparecem em outros registros do arquivo são geradas.** O plano de contas é configurado nas **Preferências da Empresa**, aba **Contabilidade**. Consulte [Geração da Conta Contábil para EFD - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703).

### Bloco B

O Bloco B traz a apuração do ISS para os contribuintes que a entregam pela EFD ICMS/IPI. Contém os registros **B020, B025, B420, B440, B460 e B470**, gerados conforme a configuração de blocos e registros das **Preferências da Empresa**.

### Bloco C

O Bloco C concentra os documentos fiscais de mercadorias (NF-e, NFC-e e afins). É o maior bloco do arquivo.

#### Registro C100 — série, modelos e situações

- **Campo 07 (série):** os modelos de documento **55 - Nota Fiscal Eletrônica** e **65 - Nota Fiscal de Venda a Consumidor** (tela [TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba **Livro Fiscal**) são gerados com **três casas decimais, complementados com zeros à esquerda**. Para os demais modelos, a série é informada conforme consta no lançamento. Na série, é possível inserir até três casas decimais.
- **Campo 17 (IND\_FRT):** a partir de **01/01/2018**, os indicadores permitidos são:

| Código | Modalidade do frete |
| --- | --- |
| 0 | Contratação do Frete por conta do Remetente (CIF) |
| 1 | Contratação do Frete por conta do Destinatário (FOB) |
| 2 | Contratação do Frete por conta de Terceiros |
| 3 | Transporte Próprio por conta do Remetente |
| 4 | Transporte Próprio por conta do Destinatário |
| 9 | Sem Ocorrência de Transporte |

- **Situações 04 e 05:** com Data de Referência **igual ou superior a 01/01/2023**, as movimentações com situação **04 (NF-e, NFC-e ou CT-e Denegado)** e **05 (NF-e, NFC-e ou CT-e Numeração inutilizada)** não aparecem no arquivo TXT — vale também para **C460, C500, C800, D100 e D500**. Na Flex, a regra vale para toda a geração.
- **Modelos de conhecimento de transporte desativados** desde 01/01/2019 — ver o tópico do [Registro D100](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registrod100), no Bloco D.
- **Parâmetro** `GERARREGSPED` ("Gerar os reg. C100 e C190 no SPED com os valores de ST?"): quando ligado, os campos de ST (base e valor — campos 23 e 24 do C100 e 08 e 09 do C190) **não são considerados na somatória do registro E210** quando houver a utilização dos **CFOPs 1949 e 2949**. Se o parâmetro estiver **desligado** e o CFOP for de outro estado, é necessário que a **Inscrição Estadual** do Substituto Tributário esteja cadastrada nas Preferências da Empresa, aba **Insc. Estadual Contribuinte ST no Estado Dest.**
- **Parâmetro** `UFEFDVLMERC` ("UFs que soma valor não apropriado ao VLRMERC (EFD)"): insira a UF da empresa para que o sistema some IPI e ICMS-ST ao valor da mercadoria.
- **Documentos extemporâneos (NF-e de emissão própria):** habilite o parâmetro `DOCEXTEMP` ("Permite informar data extemporâneos na CAF?") e informe a data extemporânea na tela **CAF**.

#### Registros 0450, C110 e C113

**Configurações preliminares (Preferências da Empresa):**

1. No campo **Tipo de Escrituração**, selecione **EFD**.
2. No quadrante **Blocos**, selecione **Bloco 0**; no quadrante **Registros**, selecione **0450** e marque **Gerar Registro**.
3. No quadrante **Blocos**, selecione **Bloco C**; no quadrante **Registros**, selecione **C110** ou **C113**, marcando **Gerar Registro** e as opções **Gerar Entrada** ou **Gerar Saída**.

**Requisitos obrigatórios para a geração:**

1. A nota fiscal precisa possuir uma **Observação Padrão** informada (tela [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173)).
2. Na configuração da Observação Padrão, o campo **Geração no EFD** deve estar assinalado com **Informação Complementar do Documento Fiscal**.
3. Para preencher o campo **03 - TXT\_COMPL** do C110, marque **Carrega Complemento p/EFD** na configuração da Observação Padrão.
4. O **TOP** utilizado no lançamento deve possuir a marcação **Buscar NF de origem p/ referenciar** — na aba **Validações** (Flex) / aba **NF-e/NFC-e** (HTML5).
5. O TOP do documento de origem (para gerar o C113) deve estar com o campo **Atualização de Livro ICMS** — aba **Livros fiscais** — devidamente definido, de modo a atualizar o livro correto.

**Comportamento:** feitas as configurações, o sistema gera automaticamente **0450** e **C110**. O **C113** é gerado apenas quando a nota estiver vinculada à sua origem (por exemplo, devolução de compra vinculada à nota de compra; nota de retorno vinculada à remessa).

Na geração do C113, são apresentadas as chaves referenciadas salvas no campo **Chave NFe Referenciada Inexistente** do cabeçalho da tela **Central de Compras**, evitando duplicidades.

**Hierarquia:** o registro **C113 é filho do C110**, que por sua vez é **filho do 0450**. Para gerar o C113 é preciso gerar o C110, e para gerar o C110 é preciso gerar o 0450.

**Registros C110 a C115 para NF-e de emissão própria:** a marcação **Gerar registros C110/C111/C112/C113/C114/C115 para NF-e de emissão própria** atende empresas que precisam gerar todos os registros filhos do C100, por contabilidade externa ou fins fiscais. O **C115** demonstra o local de entrega.

#### Registros C170, C173 e C176

**C170 — itens do documento.** Gerado para NF-e de emissão própria quando a marcação **Gerar Registro C170/C173/C176 para NF-e de emissão própria** está acionada; as demais notas já geram o C170 naturalmente. O parâmetro `DESCPRODFORNEC` define o conteúdo do campo **04 - DESCR\_COMPL**, com as opções **Padrão Complemento**, **Descrição do Produto Equivalente** e **A partir da função** (função `SNK_GET_DESCPROD_PARC`), ligando-se à tela **Produtos Equivalentes**. O parâmetro `LIVCODCONTAMAT` define a conta contábil de origem no C170 na contabilização por matriz — habilite quando houver transferência entre empresas que utilizam o mesmo plano de contas.

**C173 — Preço Máximo ao Consumidor (medicamentos).**

**Configuração:**

1. Cadastre as **Tabelas de Preço PMC** e **PF** (para estados diferentes).
2. Na tela **Estados**, aba **Geral**, preencha:

**Sequência de validação do sistema:**

1. Na **UF de Destino**, verifica se o produto (medicamento) consta na **tabela PMC** com data de vigor **menor ou igual** à data do documento; se sim e o preço for maior que zero, assume esse valor para o **campo 08 do C173**.
2. Se não encontrar, verifica na UF de Destino a **tabela PF** com data de vigor adequada; se sim e o preço for maior que zero, utiliza esse valor.
3. Se o produto não estiver em nenhuma tabela, retorna mensagem informando que o valor do preço máximo não foi encontrado.

**Parâmetro alternativo:** se os campos **Tabela de Preço PMC** e **Tabela de Preço PF** da tela Estados não estiverem preenchidos, o sistema valida a tabela configurada no parâmetro **Tabela de Preço PMC** (`CODTABPMC`). **Se nenhuma configuração existir, o C173 não é gerado.**

**Mensagens de erro:**

- Produto não encontrado nas tabelas dos Estados: "Nota de número único: ? Tabela Preço PMC/PF: ? Produto: ? Valor não encontrado"
- Usando o parâmetro: "Parâmetro CODTABPMC: ? Produto: ? Valor máximo não encontrado"

**C176 — ressarcimento de ICMS ST.** Gerado junto com C170/C173 para NF-e de emissão própria, conforme a mesma marcação.

#### Registro C177 — PRODEPE

**1. Configuração da empresa** — **Comercial › Preferências › Empresa**.

- Aba **EFD - Escrituração Fiscal Digital**, sub-aba **Blocos e Registros**: ative a geração do **Registro C177**.
- Aba **Livros Fiscais**: marque **Beneficiário de Incentivo PRODEPE/FUNCRESCE?**.

**2. Cadastro de incentivos fiscais** — **Livros Fiscais › Arquivo › Cadastros Incentivos Fiscais/Financeiros**. Cadastre o incentivo fiscal na tela [Cadastro Incentivos Fiscais/Financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052979134) e **vincule à empresa** responsável pela nota fiscal.

**3. Configuração de produtos** — **Configurações › Cadastros › Produtos**. Nos campos **Cód. Apur. Inc. PRODEPE/FUNCRESCE** e **Indicador Esp. Inc. PRODEPE/FUNCRESCE**, selecione **Com Incentivos**.

**4. Definição de CFOP** — **Comercial › Arquivo › Cadastros › CFOP**. No CFOP usado no lançamento, marque **Tipo de Operação PRODEPE** como **Operação Incentivada**.

**5. Configuração de parceiros** — **Configurações › Cadastros › Parceiros**, aba **Fiscal**. A opção **Parceiro elegível à inaplicabilidade do PRODEPE?** deve estar **DESMARCADA**. Se habilitada, as movimentações com esse parceiro não serão consideradas.

**6. Validação da configuração:**

- **Lançamento da nota fiscal** — **Comercial › Consulta › Portal de Compras**: lance a nota fiscal de compra vinculada à empresa configurada.
- **Geração do livro fiscal** — **Livros Fiscais › Arquivos › Geração ICMS/IPI** (acesse [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953)): gere a nota no Livro Fiscal.
- **Processamento no EFD** — **Livros Fiscais › Conexão › EFD - Fiscal ICMS/IPI**: processe a referência da nota.

**7. Verificação do resultado esperado:**

- Geração do **Bloco C**, incluindo os registros de detalhamento do item.
- **Registro C177** gerado com o valor fixo **PE000100** no **campo 2**.
- No arquivo TXT, a linha correspondente: `|C177|PE000100|`

As configurações de enquadramento ficam na sub-aba **Prodepe** da aba Configurações.

#### Registro C180 — documentos de arrecadação

**Finalidade:** informações sobre documentos de arrecadação (GNRE ou Documento Estadual de Arrecadação) que acompanham operações registradas em notas fiscais de compra.

**Campos:**

- **Campo 10 (COD\_DA)** — Código do Modelo de Documento de Arrecadação.
- **Campo 11 (NUM\_DA)** — Número do Documento de Arrecadação.

**Origem dos dados:** **Portal de Compras**, campos **Número do Documento de Arrecadação** e **Cód. Mód. Documento de Arrecadação**, preenchíveis tanto no **cabeçalho** quanto no **item** da nota de compra.

**Regras de priorização:**

- Os dados do **item têm prioridade** sobre os do cabeçalho.
- Se ambos estiverem vazios, os campos 10 e 11 são gerados vazios.
- Um dos dois campos não pode estar preenchido isoladamente; se um contiver dado, o outro também deve conter.

**Preenchimento do COD\_DA:** **GNRE** selecionado → gera valor **1**; **Documento Estadual de Arrecadação** selecionado → gera valor **0**.

**NUM\_DA:** não há restrição de quantidade de caracteres na legislação; o sistema considera o tamanho padrão do campo do cabeçalho da nota.

**Aplicação em Ressarcimento de ST** (gerar H010 com ressarcimento de ST e C180):

1. No **Cadastro de Produto** (aba Impostos / Informações por empresa), o campo **Tipo de substituição** **não** pode ser **Não tem** nem **Venda com Substituição Tributária (ST na Venda)**.
2. O item deve estar no inventário, **inclusive com quantidade zero** — exige o parâmetro **Gerar H030 para estoque zerado?** (`GERH30EST0`) ativado.
3. Opcionalmente, use as marcações **Ignorar filtro padrão** e **Recalcula Inventario** (aba Configurações, sub-aba Restituição/Complementação de ST).

#### Registros C190 e C191

Quando a marcação **Gerar registro C191 mesmo que o ICMS/ST esteja majorando com o FCP?** está acionada, os valores do FCP são gerados no **C191** mesmo estando junto ao ICMS/ST no **C190**. A relação entre o C190, o parâmetro `GERARREGSPED` e o registro E210 está descrita no tópico do [Registro C100](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registroc100).

#### Registros C800, C855/C857 e C895/C897

- **C800** — o campo **CNPJ ou CPF** é preenchido automaticamente com a informação do campo **CNPJ/CPF** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494).
- **C855 e C857** (Versão 1.16 / código 017, a partir de 01/01/2023) — gerados para **perfil A**, buscando notas **modelo 59**, com as informações registradas nas **Preferências da Empresa › aba EFD - Escrituração Fiscal Digital**, seguindo a hierarquia do layout: **C855 na hierarquia 3** e **C857 na hierarquia 4**, ambos abaixo do **C800**.
- **C895 e C897** (Versão 1.16) — gerados para **perfis B e C**, buscando notas **modelo 59**: **C895 na hierarquia 3** e **C897 na hierarquia 4**, abaixo do **C860**.

### Bloco D

O Bloco D concentra os documentos fiscais de serviços e transporte (CT-e, BP-e, NFCom e afins).

#### Registro D100 — frete, municípios e modelos

**Indicador de Frete — campo 17 (IND\_FRT).** Conforme o **Manual Layout 1.05 / Código 006** do SPED Fiscal, aplicável aos modelos **CT-e 57 e 67**. Indicadores permitidos a partir de 01/01/2018: **0** - Por conta do emitente (CIF); **1** - Por conta do destinatário/remetente (FOB); **2** - Por conta de terceiros; **3** - Transporte próprio por conta do remetente; **4** - Transporte próprio por conta do destinatário; **9** - Sem cobrança de frete / sem transporte.

**Validações por origem do lançamento:**

- [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874) — se o tomador do frete é a empresa e o valor é maior que zero → **Por conta do destinatário/remetente**.
- **Portal de Compras** — mesmo comportamento: tomador = empresa e valor > 0 → **Por conta do destinatário/remetente**.
- **Portal de Vendas:**

**ℹ️ Nota**

Não é necessária configuração manual: o sistema preenche automaticamente após a geração do Livro ICMS/IPI e do EFD.

**Municípios — COD\_MUN\_ORIG (campo 24) e COD\_MUN\_DEST (campo 25):**

- Apresentam os **Códigos Município Domicílio Fiscal** preenchidos anteriormente no **Cadastro de Cidades**; se não houver informação prévia, os campos são gerados **vazios**.
- Para **CT-e Simplificado (tipos 5 e 6)**, são preenchidos fixamente com **9999998** (operações nacionais) ou **9999999** (exterior). Para CT-e normal, usam o código IBGE da empresa e do parceiro (nacional) ou 9999999 (exterior).
- **Versão 1.18 (código 019, a partir de 01/01/2025):** os campos 24 e 25 são preenchidos conforme **Código do município IBGE de origem** e **Código do município IBGE de destino** da aba D100.

**Chave do Bilhete de Passagem Eletrônico substituído (Versão 1.18):** preenchida com a **Chave CT-e referenciada** da **Central de Compras** ou da **Movimentação Financeira**, quando o tipo de CT-e for **3 ou 6**.

**Modelos de conhecimento de transporte desativados pela Sefaz desde 01/01/2019:**

| Modelo | Documento |
| --- | --- |
| 07 | Nota Fiscal de Serviço de Transporte |
| 08 | Conhecimento de Transporte Rodoviário de Cargas |
| 09 | Conhecimento de Transporte Aquaviário de Cargas |
| 10 | Conhecimento Aéreo |
| 11 | Conhecimento de Transporte Ferroviário de Cargas |
| 26 | Conhecimento de Transporte Multimodal de Cargas |
| 27 | Nota Fiscal de Transporte Ferroviário de Carga |
| 8B | Conhecimento de Transporte de Cargas Avulso |

O sistema exibe a mensagem: "O modelo de documento X foi desativado pela Sefaz a partir de 01/01/2019, ou seja, para este modelo o EFD ICMS/IPI não aceita o registro D100 com o campo 11 - DT\_DOC maior ou igual a 01/01/2019".

Validação dos modelos **08 e 8B**: o campo **COD\_MOD** deverá ser igual a **07, 09, 10, 11, 26 ou 27** e a data informada deverá ser **menor que 01/01/2019**.

**Modelo 63 - Bilhete de Passagem Eletrônico:** considerado na geração dos registros **D100 e D200**, conforme informado na tela [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba **Livro Fiscal**.

**Documentos extemporâneos (CT-e de terceiros):** habilite o parâmetro `DOCMOVFINEXTEMP` ("Permite informar data extemporânea no Financeiro") e informe a **Data Extemporânea** na Movimentação Financeira.

#### Registro D190

Com a marcação **Gerar registro D190 pela Escrituração Fiscal** habilitada, o sistema prioriza as informações registradas no **Livro Fiscal** no formato de geração do D190; caso contrário, considera as informações da Central.

#### Registros D695 e D696

Alimentados pelos arquivos vinculados na sub-aba **Arquivos para Registro D695** — arquivos que as empresas enquadradas no **Convênio ICMS 115/03** entregam mensalmente.

#### Consolidação da NFCom — registros D700, D750, D760 e D761

Atende às legislações estaduais que exigem escrituração consolidada de notas de telecomunicação (**NFCom - Modelo 62**).

**1. Como habilitar a consolidação:**

- Acesse **Comercial › Preferências › Empresa**.
- Na aba **EFD - Escrituração Fiscal Digital**, adicione o registro **D750**.
- O sistema separa automaticamente os documentos conforme as regras; **não é necessário remover o D700**.

**2. Regras de separação (D750 × D700):**

- **Vão para o D750 (consolidado):** apenas documentos **NFCom (Modelo 62)**; apenas notas de **saída**; apenas **Finalidade Normal (finNFCom = 0)**; documentos **regulares autorizados**.
- **Permanecem no D700 (individualizado):** notas de **entrada**; notas de **ajuste ou substituição (finNFCom ≠ 0)**; notas que representam ajustes de apuração por documento.
- **Documentos cancelados não são escriturados em nenhum registro.**
- **Notas sem CST preenchido impedem a escrituração**, com mensagem de alerta.

**3. Estrutura dos novos registros:**

- **D750 (consolidação)** — agrupa notas de saída pela combinação de **Modelo, Série, Data de Emissão e Indicador de Pagamento**. Por padrão, o indicador é **1 (Pós-pago)**. As deduções são preenchidas quando a classificação de serviço (**cClass**) for **590**.
- **D760 (detalhamento)** — registro **filho do D750**; detalha os valores consolidados pela combinação de **CFOP, Alíquota ICMS e CST**. Não há linhas duplicadas com a mesma combinação para o mesmo dia/série.
- **D761 (Fundo de Combate à Pobreza)** — informa os valores referentes ao **FCP** nas NFComs consolidadas; natureza **informativa**.

### Bloco E

O Bloco E traz a apuração do ICMS e do IPI e seus ajustes.

#### Apuração do ICMS (E100 a E316)

- **E113** (Versão 1.18) — o campo **Parceiro** (campo 02) é preenchido conforme o modelo de documento: para os modelos **59 (CF-e SAT)**, **63 (BP-e)** e **65 (NFC-e)** o campo é gerado **vazio**; para os modelos **06 (NF/CEE)** e **66 (NF3e)** o campo não é obrigatório; para os demais (por exemplo, 55 - NF-e) é obrigatório, com o código do parceiro.
- **E200 a E250** — operações estaduais; a geração de valores de PIS/COFINS depende da marcação **Gera valores PIS/COFINS no EFD?**.
- **E210** — apuração do ICMS ST; não recebe o C100/C190 com CFOP 1949/2949 quando o parâmetro `GERARREGSPED` está ativo.
- **E300 a E316** — ajustes da apuração; os registros E312 e E313 exigem a configuração de número de processo específico.

#### Número do processo

Campo 03 nos registros **E112, E230 e E312** e campo 06 nos registros **E116, E250 e E316**: **até 15 caracteres** para períodos até 2022 e **até 60 caracteres** a partir de 2023 (Versão 1.16 / 01/01/2023).

#### Ajuste automático do IPI — registros E530 e E531

Ao término da geração do livro ICMS/IPI, as informações pertinentes ao valor calculado do IPI são modificadas em um ajuste automático. Isso ocorre quando:

1. pelo menos um parceiro do livro estiver com o campo **Enquadro no Art. 227. para cálculo de IPI?** assinalado, na aba **Fiscal** do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494); **e**
2. a marcação **Gerar linhas da Nota separadamente no Livro Fiscal?** estiver habilitada nas Preferências da Empresa, aba **Livros Fiscais**.

Para que o crédito do IPI seja recebido, devem ser escriturados os documentos que comprovem esse benefício — os dados são enviados nos registros **E530 e E531**. No arquivo de escrituração, a cada linha do **E530** correspondem um ou mais registros **E531**.

#### Diferencial de Alíquota

Para os registros do Diferencial de Alíquota, consulte [Geração do EFD Sped Fiscal - Registros do DIFAL](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600654).

### Bloco G

O Bloco G registra o controle do crédito de ICMS do ativo permanente (CIAP), pelos registros **G110, G125, G126, G130 e G140**.

#### Registros 0300 e G125

**Registro 0300 (Tabela de Identificação do Item).** Quando a marcação **Gerar CIAP de componentes para SPED** estiver realizada nas **Preferências da Empresa**, aba **Bens**, o sistema gera o Registro 0300 considerando o preenchimento do **campo 05 (COD\_PRNC)**, vinculando-o a um bem principal, gerando um Registro 0300 **para o bem principal** e preenchendo o **campo 03 (IDENT\_MERC)** com a opção **2 - componente**.

**ℹ️ Nota**

Para o Registro **G125**, o parâmetro **Utiliza TIPOENTCIAP para geração do SPED** (`TIPOENTCIAPSPED`) já leva ao EFD **todos os produtos**, independentemente de serem bens ou componentes, conforme a opção marcada no campo **Tipo de Movimentação do Bem ou Componente** da aba **Bens** do **Cadastro de Produtos**.

Ao fazer o cadastro de um componente ou bem marcando a opção **IA - Imobilização em Andamento - Componente**, o sistema leva esse código para o EFD. Assim, após processar o EFD na tela **EFD - Fiscal ICMS/IPI**, é possível validar que o **campo 05 (COD\_PRNC)** está vinculado a um bem principal e demonstrado nele, bem como verificar a marcação correta do **campo 03 (IDENT\_MERC)** como sendo um componente, uma vez que está vinculado a um bem principal.

#### Devoluções de venda no CIAP

**Configuração do parâmetro** `UFCONSDEVCIAP` ("UFs que consideram devoluções de venda no CIAP"): configure em **Preferências** e insira as UFs separadas por vírgula (exemplo: **RS, MG, RJ**). Quando a empresa está em UF configurada, as devoluções de venda são consideradas no índice de crédito de ICMS.

**Regras de aplicação:** os valores das devoluções são **subtraídos automaticamente** das colunas **Tributadas** e **Exportação** e do **Total de Saídas**, ajustando os registros do Bloco G.

**Impacto na geração do Bloco G:** as devoluções reduzem a receita bruta, o **índice/percentual de apropriação de crédito é recalculado**, afetando os registros **G110, G125, G126, G130 e G140**.

#### Composição da Receita Bruta para o Bloco G (CIAP)

Configuração no [Cadastro de CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714), nesta hierarquia:

1. Campo **Receita Bruta p/ CIAP** (prioridade máxima) — define os valores que compõem o Bloco G sem afetar outras obrigações.
2. Campo **Receita Bruta p/ EFD Contribuições** — usado como alternativa quando o campo anterior está vazio.

**⚠️ Atenção**

O campo **Receita Bruta p/ CIAP não impacta o evento R-2060 da EFD-Reinf**, permitindo configurar o CFOP como **Somar** no CIAP e **Não Afetar** na CPRB simultaneamente, eliminando conflitos de apuração.

**Para saber mais:** [Melhores Práticas - Configuração e Cálculo do CIAP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044580254).

### Bloco H

O Bloco H trata do inventário. O que ele leva ao arquivo depende da **data** considerada, do **custo** aplicado e da **origem do saldo** (cópia ou contagem de estoque) — todos configurados nos tópicos [Como usar a tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#comousar) e [Sub-aba Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#subaba-opcoes).

- **H005 — Totais do inventário.** Gerado na posição mensal quando usada a **Data de Inventário em substituição ao Bloco K** (parâmetro `GERBLHSUBSK`), a partir da **cópia de estoque** registrada na data informada. Gerado com H005 = **01** (início) ou **02** (fim) do período. A escolha entre **Pela cópia** e **Pela contagem** é feita no modal **Utilizar dados do inventário mensal**.
- **H010 — Detalhe do inventário.** Traz código do produto, quantidade e valor unitário. O **campo 10 (COD\_CTA)** segue a regra de conta contábil descrita em [Geração da Conta Contábil para EFD - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703), que inclui os parâmetros `EFDH010`, `EFDH010_PRTER` e `EFDH010_TER`, os campos equivalentes nas Preferências da Empresa e as Contas Contábeis 1 a 4 do Cadastro de Produtos. O **campo 11** é definido pelo campo **Custo para Inventário/Efeitos IR (Campo 11/reg. H010)**, aplicável apenas para períodos posteriores a **31/12/2014**. É escriturado para produtos com estoque positivo. O estoque de terceiros entra pela marcação **Incluir estoque de terceiro a partir das movimentações, no Registro H010?**.
- **H020 — Informação complementar do inventário.** Gerado apenas para inventário motivo 01 e conforme as marcações da sub-aba Opções. Com **CST = 000** e as duas marcações de motivo 01 ativas, gera um H020 para cada H010 (quando H005 = 01).
- **H030 — Informações complementares do inventário.** Gerado para produtos com saldo positivo; para gerar também para itens com **estoque zerado**, ative o parâmetro `GERH30EST0` ("Gerar H030 para estoque zerado?") — configuração exigida no ressarcimento de ST com o registro C180 (ver o tópico [Registro C180](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#registroc180), no Bloco C).

### Bloco K

O Bloco K é a parte do SPED Fiscal que contém as informações para **controle da produção e dos estoques**. Registros: **K010, K100, K200, K210, K215, K220, K230, K235, K250, K255, K260, K265, K280, K290, K291 e K292**.

#### K010

Disponível **apenas para os exercícios de 2023 em diante**; não é gerado com os demais registros do bloco para períodos anteriores. Gerado conforme o layout definido no campo **Indicador de tipo de Layout (Registro K010)** das **Preferências da Empresa**.

O campo **Indicador de tipo de Layout (Registro K010)** define o leiaute do Bloco K informado no K010 e, com isso, quais registros de produção conjunta entram no arquivo:

- **1 - Leiaute completo** — o sistema gera os registros **K290, K291 e K292**.
- **0 - Leiaute simplificado** — o sistema gera os registros **K290 e K291** e **não** gera o **K292**.

#### K100

Informa o **período de apuração** (data inicial e final) da escrituração do estoque, conforme a data informada na tela de geração do EFD.

#### K200 — estoque escriturado

Vinculado ao processo de **cópia e contagem de estoque**. Usa a **Data da contagem p/ K200** (informada na tela) quando o parâmetro `GERAK200CTE` está habilitado, gerando o registro a partir da tela [Dashboard auxiliar do BLOCO K](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159); com o parâmetro desligado, considera-se o estoque do último dia do período. A marcação **Apresenta K200 estoque escriturado negativo para conferência** permite exibir quantidades negativas — apenas para conferência, já que o validador do SPED não aceita estoque negativo.

#### K210 — Desmontagem de mercadorias (Item de Origem)

Tem o objetivo de escriturar a desmontagem de mercadorias dos tipos:

- **00** – Mercadoria para revenda
- **01** – Matéria-Prima
- **02** – Embalagem
- **03** – Produtos em Processo
- **04** – Produto Acabado
- **05** – Subproduto
- **10** – Outros Insumos

A quantidade deve ser expressa, **obrigatoriamente, na unidade de medida de controle de estoque** constante no **campo 06 do registro 0200 - UNID\_INV**.

**ℹ️ Nota**

Quando houver identificação da ordem de serviço, a chave desse registro será os campos **COD\_DOC\_OS** e **COD\_ITEM\_ORI**. Nos casos em que a ordem de serviço não for identificada, o campo chave passa a ser **COD\_ITEM\_ORI**.

#### K215 — Desmontagem de mercadorias (Item de Destino)

Tem a finalidade de escriturar a desmontagem (com ou sem ordem de serviço) de mercadorias dos mesmos tipos do K210: **00** – Mercadoria para revenda; **01** – Matéria-Prima; **02** – Embalagem; **03** – Produtos em Processo; **04** – Produto Acabado; **05** – Subproduto; **10** – Outros Insumos.

**⚠️ Atenção**

O K215 é **obrigatório** caso exista o registro-pai **K210** e o controle da desmontagem **não** seja por ordem de serviço (campos **DT\_INI\_OS**, **DT\_FIN\_OS** e **COD\_DOC\_OS** do K210 em branco). Nesse caso, a saída do estoque do item de origem e a entrada em estoque do item de destino **têm que ocorrer no período de apuração do Registro K100**. Quando o controle da desmontagem for por ordem de serviço, deverá existir o K215 até o encerramento da ordem de serviço, que poderá ocorrer em outro período de apuração.

A quantidade deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200 - UNID\_INV.

**ℹ️ Nota**

A chave do Registro K215 é o campo **COD\_ITEM\_DES**.

#### K220 — Outras movimentações internas entre mercadorias

Tem o objetivo de informar a movimentação interna entre mercadorias dos tipos indicados no campo **TIPO\_ITEM** do registro 0200 e que **não se enquadrem** nas movimentações internas já informadas nos demais tipos de registros:

- **00** - Mercadorias para revenda
- **01** - Matéria Prima
- **02** - Embalagem
- **03** - Produtos em processo
- **04** - Produtos Acabados
- **05** - Subprodutos
- **10** - Outros insumos

**ℹ️ Nota**

As informações para a geração do Registro K220 são buscadas da tela **Reclassificação do Produto**.

#### K230 — Itens produzidos (produção própria)

Informa a **produção acabada** de produtos em processo (tipo 03) e produtos acabados (tipo 04).

- Demonstra as produções **finalizadas (confirmadas)** com **TOP** do tipo **F-Produção** dentro do período do **K100**, para produtos **tipo 04** (Produto Acabado, `USORPOD='V'`).
- **Data da produção** — data de baixa da matéria-prima e do produto acabado.
- **Número da OP** — `nunota`.

**ℹ️ Nota**

As **perdas** são escrituradas conforme as notas fiscais nos registros **C100**, conforme orientação da RFB.

#### K235 — Itens consumidos (produção própria)

Informa o **consumo de insumo (MP)** no processo produtivo, vinculado ao produto resultante informado no **K230**.

- Demonstra as MPs consumidas vinculadas à **OP do K230**.
- São gerados os itens **efetivamente consumidos** constantes da OP finalizada, determinados pela **fórmula de produção**.
- Campo **05 - COD\_INS\_SUBST** — não gerado no momento.
- Insumos com **quantidade consumida igual a zero** não são listados.

#### K250 — Industrialização efetuada por terceiros: itens produzidos

Informa os produtos **industrializados por terceiros** e suas quantidades, expressas na unidade de medida de controle de estoque (**campo 06 do registro 0200 - UNID\_INV**).

- Demonstra as produções **finalizadas (confirmadas)** com **TOP** do tipo **F-Produção** dentro do período do **K100**, para produtos **tipo 04** (`USORPOD='V'`) marcados com **Industrialização efetuada por terceiros** na aba **Estoque de terceiros**.
- Esse campo é habilitado apenas para TOPs do tipo **F-Produção**.
- **Data da produção** — data de baixa da matéria-prima e do produto acabado.
- **Número da OP** — `nunota`.
- As industrializações devem ser lançadas normalmente, usando a TOP de produção com essa marcação, para que o **K250** e o **K255** sejam gerados corretamente.

#### K255 — Industrialização por terceiros: itens consumidos

Informa a **quantidade consumida do insumo remetido para industrialização em terceiro**, vinculada ao produto resultante do **K250**.

- Demonstra as MPs consumidas vinculadas à **OP gerada no K250**.
- São gerados os itens **efetivamente consumidos** constantes da OP finalizada, determinados pela **fórmula de produção**.
- Campo **05 - COD\_INS\_SUBST** — não gerado no momento.

#### K260 e K265 — Reprocessamento e reparo

Têm o objetivo de informar o produto que será reprocessado ou que foi reprocessado e o insumo que será reparado ou que foi reparado no **período de apuração do Registro K100**.

- **K260 — Reprocessamento/reparo de produto/insumo.** Apresenta os produtos que saíram do estoque no período de apuração para serem reprocessados, incluindo a **ordem de produção/serviço**, o **código do produto** que foi reprocessado, a **data de saída do estoque**, a **quantidade que saiu do estoque**, a **data de retorno ao estoque** e a **quantidade que retornou ao estoque**.
- **K265 — Reprocessamento/reparo: mercadorias consumidas e(ou) retornadas.** Apresenta os produtos que foram consumidos no período de apuração no reprocessamento do produto informado no K260, incluindo o **código do produto**, a **quantidade consumida** e a **quantidade que retornou ao estoque**.

**Configuração inicial.** Na tela **Empresa** (**Comercial › Preferências › Empresa**), aba **EFD - Escrituração Fiscal Digital**, selecione **EFD** no campo **Tipo de Escrituração**; na sub-aba **Blocos e Registros**, confirme que o **Bloco K** está criado e marcado para gerar e que os registros **K260** e **K265** também estão criados e marcados para geração.

**Regras para a geração do K260.** O sistema busca as Notas de Produção originadas da tela **Ordens de Produção**, atendendo às condições:

1. O **tipo de movimento da TOP** utilizada na **Central de Produção** deve ser **Produção**.
2. A data do campo **Dt. Movimento**, na Central de Produção, deve estar contida no período de geração do arquivo TXT do EFD — é esse campo que o sistema usa para filtrar a busca.
3. O documento na Central de Produção deve estar com a situação **Confirmado**.
4. Na tela **Processo Produtivo**, o campo **Reprocessamento/reparo** deve estar marcado.
5. Na tela **Composição do Produto**, aba **Matérias-Primas**, é possível incluir o produto acabado como matéria-prima de si mesmo quando o parâmetro **Permitir definir produto como MP de si próprio** (`PRODMPPROP`) estiver habilitado.
6. Na grade de itens da Central de Produção, o campo **Quantidade** deve ser **maior que zero**.

**Regras para a geração do K265.**

1. Na grade de itens da Central de Produção, o campo **Quantidade** deve ser **maior que zero**.
2. No [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) (**Configurações › Cadastros › Produtos**), aba **Formação de Custo/Preço**, os campos **Filtro p/ Cálc. Custo baseado no Financeiro** e **Filtro p/ Cálc. Custo baseado na Requisição** são considerados na geração.
3. Ainda no Cadastro de Produtos, o campo **Usado como** deve estar configurado com uma destas opções: **Revenda**, **Matéria-prima**, **Embalagem**, **Em Processo**, **Venda (fabricação própria)**, **Subproduto** ou **Outros insumos**.

#### K280 — Correção de Apontamento do K200

O K280 ajusta o que foi enviado no **Registro K200**. Ou seja: depois de entregar o K200, ao realizar a contagem do estoque e verificar a necessidade de corrigir o valor enviado nesse registro, emite-se uma **Nota de Ajuste de Estoque** com as configurações abaixo devidamente realizadas, para que o K280 possa ser enviado.

**Exemplo:** foi enviado o Registro K200 no mês de **dezembro/2019**, porém, em **janeiro/2019** constatou-se a diferença no estoque. Assim, será preciso emitir a Nota de Ajuste de Estoque corrigindo essa diferença e, quando for encaminhado o SPED em **fevereiro/2019**, será enviado o K280 com a quantidade ajustada, assim como o K200, que será enviado normalmente com o valor do período.

**⚠️ Atenção**

Quando a Nota de Ajuste for emitida, deve-se inserir a **data de ajuste do estoque**; ou seja, conforme o exemplo acima, a data de **dezembro** deverá ser informada para que o Registro K280 seja gerado.

**Resumo das configurações por cenário** — em todos eles, a marcação **Gerar Correção de Apontamento (K280)** deve estar acionada na aba **Livro Fiscal** da TOP:

| Cenário | TOP | Atualização do Estoque (aba Geral) | Estoque com/de Terceiros (aba Estoque de Terceiros) |
| --- | --- | --- | --- |
| Ajuste de entrada — positivo, estoque próprio | Nota de Ajuste de Entrada de Estoque | **Entrar** | **Não controla** |
| Ajuste de saída — negativo, estoque próprio | Nota de Ajuste de Saída de Estoque | **Baixar** | **Não controla** |
| Ajuste de entrada — estoque de terceiro | — | **Nenhuma** | **Somar ao estoque próprio em poder de terceiro** |
| Ajuste de saída — estoque de terceiro | — | **Nenhuma** | **Subtrair ao estoque próprio em poder de terceiro** |
| Ajuste de entrada — propriedade de terceiro | — | **Nenhuma** | **Somar ao estoque de terceiros em poder da empresa** |
| Ajuste de saída — propriedade de terceiro | — | **Nenhuma** | **Subtrair ao estoque de terceiros em poder da empresa** |

**Ajuste de Entrada = Ajuste Positivo de Estoque Próprio**

1. Na TOP **Nota de Ajuste de Entrada de Estoque** (tela [Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba **Livro Fiscal**), acione a marcação **Gerar Correção de Apontamento (K280)**.
2. Na aba **Geral** da mesma tela, configure o campo **Atualização do Estoque** com a opção **Entrar**.
3. Na aba **Estoque de Terceiros**, o campo **Estoque com/de Terceiros** deve possuir a opção **Não controla** selecionada.
4. Feitos os ajustes, crie a **Nota** com as devidas entradas de produtos.
5. Em seguida, faça a geração do SPED Fiscal.
6. Ao abrir o arquivo gerado, o registro **K280** aparece gerado e validado no PVA sem erros, com a quantidade de produtos **positiva**.

**Ajuste de Saída = Ajuste Negativo de Estoque Próprio**

1. Selecione a TOP **Nota de Ajuste de Saída de Estoque** e realize a marcação **Gerar Correção de Apontamento (K280)** na aba **Livro Fiscal**.
2. Na aba **Geral** da tela **Tipos de Operação - TOP**, o campo **Atualização do Estoque** deve estar com a opção **Baixar** selecionada.
3. O campo **Estoque com/de Terceiros**, na aba **Estoque de Terceiros**, também deve possuir a opção **Não controla**.
4. Posteriormente, uma nota com a **saída** dos produtos será criada.
5. Depois disso, o sistema realiza a geração do SPED Fiscal e você observa no arquivo a geração de uma **correção negativa** dos produtos.

**Ajuste de Entrada (positivo) ou Saída (negativo) de Estoque de Terceiro**

1. Assim como nos ajustes acima, a marcação **Gerar Correção de Apontamento (K280)** deve ser efetuada, tanto para o ajuste de entrada quanto para o de saída.
2. O campo **Atualização do Estoque** precisa estar com a opção **Nenhuma** selecionada.
3. No campo **Estoque com/de Terceiros**: para o **Ajuste de Entrada**, selecione **Somar ao estoque próprio em poder de terceiro**; para o **Ajuste de Saída**, **Subtrair ao estoque próprio em poder de terceiro**.
4. Realizadas as configurações, crie as notas de entrada e de saída de produtos.
5. Após gerar o SPED Fiscal, observe no arquivo a geração **positiva e negativa** dos produtos.

**Ajuste de Entrada ou Saída em Propriedade de Terceiro**

1. Selecione a marcação **Gerar Correção de Apontamento (K280)**.
2. Insira a opção **Nenhuma** no campo **Atualização do Estoque**, tanto para o ajuste de Entrada quanto para o de Saída.
3. No campo **Estoque com/de Terceiros**: **Somar ao estoque de terceiros em poder da empresa** para o **Ajuste de Entrada** e **Subtrair ao estoque de terceiros em poder da empresa** para o **Ajuste de Saída**.
4. Depois disso, realize os mesmos procedimentos dos ajustes anteriormente informados.

#### K290, K291 e K292 — Produção conjunta

Informam as **ordens de produção conjunta** do período: a ordem de produção (**K290**), os itens produzidos (**K291**) e os insumos consumidos (**K292**). O sistema **não cria nem altera ordens de produção** — ele apenas lê as ordens de produção conjunta já registradas no módulo de **Produção**.

**Pré-requisitos.** Para que o sistema encontre as ordens e gere os registros:

- A ordem de produção precisa estar registrada como **produção conjunta** no módulo de Produção.
- As **notas de produção** vinculadas à ordem precisam estar **confirmadas**.
- Os produtos precisam estar cadastrados com o campo **Usado como** igual a **Venda (fabricação própria)**.
- Os itens produzidos e os insumos consumidos precisam ter o **Tipo do Item** compatível com o registro 0200.
- Os registros **K290**, **K291** e **K292** precisam estar com **Gerar Registro** = **Sim** nas **Preferências da Empresa › aba EFD - Escrituração Fiscal Digital › sub-aba Blocos e Registros**, com o **Bloco K** marcado para gerar e o campo **Indicador de tipo de Layout (Registro K010)** preenchido.

**⚠️ Atenção**

O sistema valida o **Tipo do Item** (campo 07 do registro 0200) dos itens informados. No **K291**, o item produzido precisa ser **03 - Produto em Processo** ou **04 - Produto Acabado**. No **K292**, o insumo consumido precisa ser **00 - Mercadoria para Revenda**, **01 - Matéria-prima**, **02 - Embalagem**, **03 - Produto em Processo**, **04 - Produto Acabado**, **05 - Subproduto** ou **10 - Outros insumos**.

**Quais ordens entram na escrituração.** O sistema considera as ordens de produção conjunta da empresa que tenham notas de produção confirmadas de itens de fabricação própria e que atendam a **pelo menos uma** destas condições:

- foram **concluídas** dentro do período da escrituração;
- tiveram **notas de produção** dentro do período da escrituração;
- ainda estão **em andamento**, sem data de conclusão, na data final do período.

**Onde conferir.** Depois do **Processar**, abra a aba **K001**, o nível **K100** e a aba **K290**. Os registros ficam em níveis encadeados: cada ordem de produção conjunta gera um **K290** no nível K100, e cada K290 tem as abas **K291** e **K292** com os itens daquela ordem. Na versão **HTML5** é possível **incluir e editar** os registros K290, K291 e K292 manualmente, antes de gerar o arquivo.

**K290 — Produção conjunta: ordem de produção.** Identifica a ordem e o período em que ela foi executada.

- **Nro. OP Conjunta** — código de identificação da ordem de produção. Obrigatório, com até 30 caracteres. Gera o campo `COD_DOC_OP`.
- **Data de início da ordem de produção** — data em que a ordem começou. Gera o campo `DT_INI_OP`.
- **Data de conclusão da ordem de produção** — gera o campo `DT_FIN_OP`. **Preenchido:** a data é enviada no arquivo. **Vazio:** a ordem ainda está em andamento e o `DT_FIN_OP` sai vazio.

**K291 — Produção conjunta: itens produzidos.** Lista os itens resultantes da ordem.

- **Código do item produzido** — produto resultante da ordem. Obrigatório, com até 60 caracteres. Gera o campo `COD_ITEM`.
- **Quantidade** — quantidade de produção acabada, com 6 casas decimais. Gera o campo `QTD`.

**K292 — Produção conjunta: insumos consumidos.** Lista os insumos e componentes consumidos na ordem. **Só é gerado com o leiaute completo do Bloco K** (Indicador de tipo de Layout = 1).

- **Código do item consumido** — insumo ou componente consumido. Obrigatório, com até 60 caracteres. Gera o campo `COD_ITEM`.
- **Quantidade** — quantidade consumida, com 6 casas decimais. Gera o campo `QTD`.

**Exemplo no arquivo TXT.** Ordem de produção conjunta número 10, iniciada em 10/11/2022 e concluída em 23/11/2022, com dois itens produzidos e dois insumos consumidos, no leiaute completo:

- `K290|10112022|23112022|10`
- `K291|50|10,000000`
- `K291|60|30,000000`
- `K292|30|7,000000`
- `K292|25|5,000000`

Se a ordem ainda estiver em andamento, a linha do K290 sai sem a data de conclusão: `K290|10112022||10`. No leiaute simplificado, as linhas do K292 não aparecem no arquivo.

**Exclusão.** Quando o arquivo está confirmado (marcação **Arquivo confirmado**), o sistema não permite excluir os registros K290. A exclusão de um K290 **remove também todos os K291 e K292 vinculados a ele** e não pode ser desfeita — os itens produzidos e os insumos consumidos daquela ordem precisam ser gerados ou incluídos novamente.

#### Substituição do Bloco K pelo Bloco H

Quando o parâmetro `GERBLHSUBSK` está ligado e a **Data de Inventário em substituição ao Bloco K** é informada, o sistema gera o Bloco H na posição mensal e **deixa de gerar o Bloco K** para aquela data.

**Para saber mais:** [Dashboard auxiliar do BLOCO K](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411588603159) · [Quais as configurações necessárias para geração do BLOCO K](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513933) · [Geração EFD Fiscal - Registros K260 e K265](https://ajuda.sankhya.com.br/hc/pt-br/articles/29413236538775).

### Bloco 1

O Bloco 1 traz o complemento da escrituração e as obrigações específicas.

#### Registro 1400 — município do fato gerador

**Regras obrigatórias (todas simultâneas):**

1. A nota deverá ter sido inserida no **Registro C100**.
2. Parâmetros configurados: `CFOPNAODED1400` ("CFOPs que geram Não Dedutíveis no registro 1400"), `UFSNAODED1400` ("UFs que geram Não Dedutíveis no registro 1400") e `UFSVENREG1400` ("UFs que geram NF-e de Venda no registro 1400").
3. A nota deve possuir **Modelo de Documento** = **55 - Nota Fiscal Eletrônica** (tela [Tipos de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114), aba **Livro Fiscal**).
4. Deve ser **saída**, com **Tipo de Movimento** = **P - Pedido de venda** ou **V - Venda**.
5. O **valor de frete** deve ser igual a **zero**.
6. Campo **Indicador de Presença para NF-e/NFC-e** (TOP, aba **Impressão**) com **0 - Não se aplica**, **1 - Operação presencial** ou **5 - Presencial, fora do estabelecimento**.
7. Na aba **Livro Fiscal** da TOP, a marcação **Gerar Registro 1400 no SPED Fiscal?** deve estar acionada.
8. A tela [Códigos de itens (IPM) por UF no registro 1400](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116093) deve ter o seu devido registro.

**Impressão do código do item:** realize os cadastros das abas **Grupo de Produto**, **Produto** e **Tipos de Operação** da tela acima.

**Regra do município:** quando o documento é um **CT-e**, o município considerado é o de **origem do CT-e**. O registro só é gerado quando o município fizer parte do **estado da empresa geradora do EFD**. Exemplo: empresa em **Minas Gerais** prestando serviço de transporte iniciado no próprio estado **gera** o registro; iniciando em **São Paulo**, **não gera**.

**Parâmetro** `IBGEPARC1400` ("UFs com cód. IBGE parceiro fornecedor p/ reg.1400"): insira as UFs (separadas por vírgula) para que, na geração do 1400, seja considerado o **código do município do Parceiro** — ampara a regra **DIPAM** do estado de **SP** e outras UFs.

**Parâmetro** `UFSCTEOUTUF1400` ("UFs que geram CT-e Iniciados em Outro Estado no registro 1400"): insira a UF no campo **Texto**. A UF informada influencia **apenas registros de saída**.

**Modelo 04 (NF Produtor Rural):** ao incluí-lo na geração do 1400, o município do parceiro também será gerado, assim como nos modelos **01, 1A, 1B, 55 e 65**.

**Configurações necessárias (exemplo SP):**

- **Empresa** no estado de **SP**
- **Parceiro** no estado de **SP** — **não pode possuir inscrição estadual**
- **Nota de entrada** nos modelos **01, 1A, 55 ou 65**
- O **Parceiro** deve ser do **mesmo estado da empresa** e a **UF deve estar preenchida no parâmetro**

#### Registros 1600 e 1601

Gerados pelo tratamento manual da tela [Resumo de Operações com Cartão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595154), quando as marcações **Gerar registro 1600 pelo Resumo de Operações com Cartão?** e **Gerar registro 1601 pelo Resumo de Operações com Cartão?** estão acionadas.

#### Registro 1960

O benefício cadastrado deve possuir a opção **1-Indústria (crédito presumido)** no campo **Indicador de Enquadramento** da tela [Cadastro Incentivos Fiscais/Financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052979134).

#### Registros 1970 e 1980 (PRODEPE/FUNCRESCE)

São declarações GIAF 3 (Guia de Informação e Apuração de Incentivos Fiscais e Financeiros). O **1970** trata do diferimento na entrada e do crédito presumido e é acompanhado do **1975** (saídas internas por faixa de alíquota, obrigatório quando houver 1970). O **1980** trata da central de distribuição.

- Nas **Preferências da Empresa**, aba **Livros Fiscais**, marque **Beneficiário de Incentivo PRODEPE/FUNCRESCE?**.
- Nas **Preferências da Empresa**, aba **EFD - Escrituração Fiscal Digital**, sub-aba **Blocos e Registros**, marque **Gerar Registro** para o **1001** (abertura), o **1990** (encerramento) e, conforme o caso, o **1970** — acompanhado do **1975** — ou o **1980**.
- Na tela [CFOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600714), preencha o campo **Tipo de Operação PRODEPE**.
- No **Cadastro de Produtos**, aba **Impostos**, seção **Prodepe**, selecione **Cód. Apur. Inc. PRODEPE/FUNCRESCE?** como **Com incentivo** e defina o **Indicador Esp. Inc. PRODEPE/FUNCRESCE**.
- No [Cadastro Incentivos Fiscais/Financeiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360052979134), defina o **Indicador de Enquadramento** — **3-Importação (diferimento/crédito presumido)** para o 1970 ou **4-Central de distribuição (entradas/saídas)** para o 1980 — e vincule os produtos.
- Na tela **EFD - Fiscal ICMS/IPI**, preencha **Empresa** e **Data Referência**; na aba Configurações, ajuste **Período**, **UF** e **Finalidade de Apresentação do Arquivo**. Clique em **Processar** — o sistema preenche as abas 1001 e 1970/1975 ou 1980 e exibe "Registros processados com sucesso."

#### Número do processo

Campo 03 no registro **1922** e campo 06 no registro **1926**: até 15 caracteres para períodos até 2022 e até 60 caracteres a partir de 2023.

### Bloco 9

O Bloco 9 encerra o arquivo. A aba **9001** contém o registro **9900** (registros do arquivo) e a aba **9999** traz o registro de encerramento **9999**, com a totalização das linhas.

### Adequação do ERP ao SPED Fiscal (EFD-ICMS/IPI) 3.1.9 e 3.2.0

A partir de **01/01/2026**, o ERP passa a gerar o SPED Fiscal (EFD-ICMS/IPI) em conformidade com o novo leiaute (versão **3.1.9/3.2.0**) e com as orientações da **Reforma Tributária do Consumo**, incluindo os tributos **CBS**, **IBS** e **IS**.

A atualização foca em garantir a correta escrituração, especialmente em **operações interestaduais com consumidor final não contribuinte**, que exigem o **registro 0150 adicional** quando há divergência de UF.

#### Atualização e vigência do leiaute

Para garantir a conformidade, a tabela de controle de versões do SPED Fiscal foi atualizada com o **Código do Leiaute 020 / Versão 1.19**, vigente a partir de **01/01/2026**. O sistema o seleciona automaticamente para qualquer escrituração com data-base igual ou posterior a essa data — a tabela completa de versões está no tópico [Como usar a tela › Versões de layout](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#versoes).

#### Ajustes em registros

**Registro C120.** O registro (caminho **C001 › C100 › C120**) sofreu uma atualização em seu campo de identificação:

- **Campo atualizado:** campo 02
- **Novo valor válido adicionado:** **2**

O sistema foi devidamente ajustado para permitir, validar e exportar esse novo valor no domínio do campo 02 do Registro C120.

#### Considerações para a escrituração dos novos tributos (CBS, IBS e IS)

A EFD ICMS/IPI **não deve ser utilizada para a apuração** dos novos tributos — **CBS** (Contribuição sobre Bens e Serviços), **IBS** (Imposto sobre Bens e Serviços) e **IS** (Imposto Seletivo). No entanto, futuramente eles devem ser considerados no **valor total dos documentos fiscais escriturados**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Verificação de divergências

Caso haja uma ou mais divergências de escrituração no período da geração informado, uma mensagem é exibida questionando se você deseja ou não visualizá-las. Ao confirmar, o sistema é direcionado à tela [Divergências de Escrituração](https://ajuda.sankhya.com.br/hc/pt-br/articles/15370034234775) para as devidas análises.

Para que a mensagem seja exibida, a marcação **Verificar divergências?** — aba **Parâmetros** da tela [Geração ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115953-Gera%C3%A7%C3%A3o-ICMS-IPI#abaparmetros) — deve estar habilitada.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-Tela-EFD-Fiscal-ICMS-IPI-Flex-e-HTML5#sumario)

---

## Pontos de atenção

- **Datas de inventário mutuamente exclusivas** — preencha a **Data de Inventário em substituição ao Bloco K** ou a **Data da contagem p/ K200**, nunca as duas.
- **Custo para Inventário/Efeitos IR** só fica habilitado para períodos posteriores a **31/12/2014**.
- **Estoque negativo** só deve ser apresentado para conferência interna; o validador do SPED não o aceita.
- **Quantidades com mais de três casas decimais** no H010 são rejeitadas pelo validador — use a marcação de exclusão quando for o caso.
- **K215 é obrigatório** sempre que houver um K210 sem ordem de serviço.
- **K292** só é gerado com o **Indicador de tipo de Layout (Registro K010)** = **1 - Leiaute completo**; no leiaute simplificado ele não sai no arquivo.
- **Excluir um K290** apaga junto todos os K291 e K292 vinculados, e a exclusão não pode ser desfeita. Com o **Arquivo confirmado**, a exclusão do K290 é bloqueada.
- No **K280**, o que define o período é a **data de ajuste do estoque**, não a data da nota.
- **Conversão CST 090 → CST 00** e **H020 do CST anterior à mudança de tributação** não podem ser habilitadas ao mesmo tempo.
- **Situações 04 e 05** não entram no TXT a partir de 01/01/2023 (HTML5); na Flex, a regra vale para toda a geração.
- **Modelos de transporte 07, 08, 09, 10, 11, 26, 27 e 8B** foram desativados pela Sefaz desde 01/01/2019.
- **Arquivo confirmado** (HTML5) bloqueia o reprocessamento — desmarque antes de reprocessar.
- **Excluir uma referência** (HTML5) apaga todas as movimentações e registros dela do banco de dados.
- **Conta contábil** — a troca da forma de busca depois do arquivo gerado exige o reprocessamento do período; no modo Contabilização, sem a contabilização do período concluída o registro sai sem conta contábil. O **H010 é a exceção**: não segue o campo **Tipo da Conta Contábil para EFD ICMS/IPI** — configurá-lo é um passo separado. Detalhes em [Geração da Conta Contábil para EFD - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/8811502871703).
