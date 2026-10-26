---
id: "33820442146199"
titulo: "Tela Cadastro de Alíquotas IBS — Reforma Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Cadastro de impostos"
atualizado_em: "2026-10-07T16:27:47Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "br.com.sankhya.mgeliv.cadastros.AliquotaIbs", "IBS", "Reforma Tributária", "Alíquotas de IBS"]
---

# Tela Cadastro de Alíquotas IBS — Reforma Tributária

**Módulo:** Fiscal
**Versão mínima:** 4.17.05 (Módulo Livros Fiscais) · 4.33b172, 4.34b225, 4.35b221 (Sankhya W)
**Caminho de acesso:** **Menu Principal › Cadastros › Alíquotas IBS**

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#oque) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#antes) [Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#fluxo) [Como cadastrar uma nova alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#cadastrar)    ↳ [Aba Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#aba-identificacao)    ↳ [Aba Tributação](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#aba-tributacao) [Como editar uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#editar) [Como duplicar uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#duplicar) | [Visualização dos valores no documento fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#visualizar) [Crédito Presumido de IBS na Zona Franca de Manaus](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#zfm)    ↳ [Configuração do produto e emitente](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#zfm-config)    ↳ [Geração da nota de crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#zfm-nota-credito) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#pontos-atencao) [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#calculos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#faq) |
| --- | --- |

---

## O que é e para que serve

A tela **Cadastro de Alíquotas IBS** é onde você gerencia as regras de configuração do Imposto sobre Bens e Serviços no Sankhya OM — criando desde regras gerais, válidas para todas as empresas, até regras específicas para o seu negócio. O foco da tela é garantir o cálculo exato do IBS para cada transação, em conformidade com as regras da Reforma Tributária. A tela não cobre a configuração de CBS nem de alíquotas monofásicas.

Você pode definir as alíquotas com base em uma combinação de fatores:

- **Tipo de operação:** vendas, prestação de serviços etc.
- **Escopo da regra:** para uma empresa específica ou como regra geral para todas.
- **Classificação do item:** por NCM (produtos) ou NBS (serviços).
- **Atividade da empresa:** por CNAE.
- **Parceiro envolvido:** por código específico do cliente/fornecedor ou pelo grupo tributário (Grupo IBS/CBS).
- **Localização:** por UF e/ou Município da operação.
- **Regime tributário:** do parceiro envolvido na transação.
- **Período de validade:** da alíquota a ser aplicada.
- **Finalidade da operação:** considerada tanto a nível de nota quanto a nível de item para aumentar a precisão do cálculo.

![Imagem 1: Finalidade da operação: considerada tanto a nível de nota quanto a nível de item para aumentar a precisão do cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/39661679696023)

---

## Antes de começar

- Sistema atualizado para a versão 4.17.05 (Módulo Livros Fiscais).
- Permissões de acesso à tela **Cadastro de Alíquotas IBS** verificadas.

---

## Diagrama de fluxo

O fluxo abaixo resume as etapas das principais ações na tela de Cadastro de Alíquotas IBS:

![Imagem 2: O fluxo abaixo resume as etapas das principais ações na tela de Cadastro de Alíquotas IBS:](https://ajuda.sankhya.com.br/hc/article_attachments/35190773120663)

---

## Como cadastrar uma nova alíquota

1. Acesse **Menu Principal › Cadastros › Alíquotas IBS** e clique em **Cadastrar** para abrir o formulário de uma nova regra.
2. Preencha os campos obrigatórios da [Aba Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#aba-identificacao).
3. Preencha a [Aba Tributação](https://ajuda.sankhya.com.br/hc/pt-br/articles/33820442146199-Tela-Cadastro-de-Al%C3%ADquotas-IBS-Reforma-Tribut%C3%A1ria#aba-tributacao) conforme o tipo de regra.
4. Clique em **Salvar**. O sistema validará todos os dados. Se estiverem corretos, o cadastro será confirmado; caso contrário, uma mensagem indicará o que precisa ser ajustado.

### Aba Identificação

Defina aqui o escopo da regra — se é geral ou específica.

**Para criar uma regra geral** (aplicável a múltiplos casos):

- **Empresa:** digite **0** para aplicar a todas as empresas do grupo.
- **CNAE, NCM, NBS:** digite **0** para regras abrangentes.
- **UF/Município:** deixe vazios para aplicar a qualquer localização.
- **Regime Tributário:** deixe vazio para todos os regimes.
- **Finalidade da Operação:** informe a finalidade específica (ex: Consumo, Revenda). O sistema priorizará alíquotas que coincidam exatamente com a finalidade informada no item da nota ou na nota.

**Para criar uma regra específica:**

- **Empresa:** selecione uma empresa específica ou mantenha **0** para todas.
- **CNAE, NCM, NBS:** use códigos completos ou parciais (hierárquicos).
- **UF/Município:** informe a localização.
- **Regime Tributário:** selecione conforme a situação fiscal da empresa.
- **CST,** `cClassTrib`**:** validados contra tabelas específicas do sistema.

**ℹ️ Nota**

NCM e NBS não podem ser preenchidos simultaneamente. O sistema bloqueará o salvamento com a mensagem "Não é possível cadastrar uma alíquota para um produto e serviço simultaneamente". Use NCM para produtos e NBS para serviços — em registros separados quando necessário.

### Aba Tributação

#### Seção Referência

As alíquotas de referência do IBS e da CBS serão estabelecidas por resolução do Senado Federal, conforme os seguintes períodos de transição:

- **CBS:** vigora de 2027 a 2035.
- **IBS:** vigora de 2029 a 2035.
- **Ambos:** a partir de 2036, mantém-se a alíquota definida para o ano anterior.

Para configuração no sistema, informe a alíquota de referência total e o percentual de repartição entre União (CBS) e Estados/Municípios (IBS), conforme os valores definidos pelo Senado Federal para o período vigente.

#### Seção Alíquotas

As alíquotas padrão da CBS e do IBS serão definidas por lei específica de cada ente federativo:

- **União:** fixa a alíquota da CBS.
- **Estados e Municípios:** fixam as alíquotas do IBS.
- **Distrito Federal:** define ambas.

Para configuração no sistema, informe a alíquota padrão da CBS (União) e as alíquotas padrão do IBS (Estado e Município de destino). Se não houver lei específica, adote a alíquota de referência vigente para o ente federativo.

#### Seção Redução e Diferimentos

Para preencher os campos desta seção, consulte a tabela de classificação tributária no [Portal da Conformidade Fácil](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria).

**💡 Dica**

Para mais informações sobre versões das Notas Técnicas, acesse **Menu Principal › Preferências › Empresa ›** [**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), selecione o documento fiscal (CT-e, NF-e ou NFCom) e acesse a aba **Nota Técnica**.

#### Seção IBS Presumido

Para preencher os campos desta seção, consulte a tabela de crédito presumido no [Portal da Conformidade Fácil](https://dfe-portal.svrs.rs.gov.br/CFF/TabelaCreditoPresumido).

- Para operações na **Zona Franca de Manaus (ZFM)**, o CST deve possuir o indicador de crédito presumido habilitado (`ind_gCredPresIBSZFM = 1`).
- O sistema validará se o produto possui a **Classificação para subapuração do IBS na ZFM** preenchida em seu cadastro.

#### Seção Tributação Regular

Ao utilizar a Nota Técnica 2025.001-RTC v1.05, o sistema se adapta aos novos layouts da SEFAZ, gerando, validando e transmitindo documentos com a estrutura necessária para os tributos IBS e CBS. Nesta seção, configure os valores integrais dos impostos, sem reduções especiais, para geração do bloco **Grupo de Tributação Regular**.

**💡 Dica**

Para mais informações sobre versões das Notas Técnicas, acesse **Menu Principal › Preferências › Empresa ›** [**Documentos Fiscais Eletrônicos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), selecione o documento fiscal (CT-e, NF-e ou NFCom) e acesse a aba **Nota Técnica**.

O código de classificação tributária regular preenchido nesta seção é enviado na emissão da NFS-e, no grupo `tributacaoRegular` do JSON transmitido ao Nota Gateway. Quando a alíquota tem preenchimento em mais de um nível, o Sankhya Om considera o IBS Municipal; se ele não estiver preenchido, o IBS Estadual; e, se nenhum dos dois estiver, a CBS.

Para saber mais, acesse [NFS-e e Reforma Tributária: Configuração e Uso do IBS/CBS via Nota Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/36881907516567#tributacao-regular).

#### Seção Vigência

Preencha as datas de início e fim da vigência da alíquota. O preenchimento da data de início é obrigatório — o sistema bloqueará o salvamento caso esteja em branco.

**ℹ️ Nota**

Para garantir a aplicação correta das alíquotas, cadastre as regras da mais específica para a mais geral. Cadastre alíquotas futuras com antecedência e use datas de fim para substituições programadas — você pode usar uma data de vigência futura para simular o resultado sem impactar a operação diária.

---

## Como editar uma alíquota

Use para corrigir dados, alterar percentuais ou ajustar vigências de alíquotas já cadastradas.

1. Use os **filtros de busca** no topo da tela para localizar a alíquota — filtre por empresa, operação, vigência ou produto.
2. Clique duas vezes na linha, com o botão direito do mouse, ou selecione-a e clique em **Editar**.
3. Altere vigência, empresa, percentual ou qualquer campo necessário.
4. Clique em **Salvar** ou use **Ctrl+S**.

---

## Como duplicar uma alíquota

Use para criar variações de alíquotas similares, otimizando o tempo de cadastro quando você tem regras parecidas.

1. Selecione a alíquota que servirá como modelo.
2. Clique em **Duplicar**. O sistema criará uma cópia em modo de edição com um novo ID único.
3. Ajuste os campos desejados e clique em **Salvar**.

---

## Visualização dos valores no documento fiscal

Ao emitir documentos fiscais com IBS, o sistema calcula automaticamente todos os tributos conforme as regras da Reforma Tributária — considerando reduções de alíquota, diferimento, devoluções e créditos presumidos. Basta manter as alíquotas cadastradas corretamente e, ao salvar a nota, o valor do IBS será exibido com todos os ajustes aplicados.

No rodapé do documento fiscal você pode conferir:

- A base de cálculo total do IBS.
- Os valores de diferimento, créditos e devoluções.
- O imposto calculado separadamente para UF e Município.
- O valor total do IBS.

---

## Crédito Presumido de IBS na Zona Franca de Manaus

Esta funcionalidade atende à **NT 2025.002-RTC v1.30**, permitindo a apropriação do crédito presumido de IBS sobre o saldo devedor na Zona Franca de Manaus (ZFM).

### Configuração do produto e emitente

Para que a opção de crédito presumido seja habilitada, o sistema valida a localização e o cadastro do emitente. Em **Produtos › Impostos › Reforma Tributária**, preencha o campo **Classificação para subapuração do IBS na ZFM**.

**ℹ️ Nota**

Este campo só aparece para emitentes de UFs específicas (AM, AC, RO, RR e determinados municípios do AP) com inscrição SUFRAMA ativa. O campo não é gerado em **NFC-e (Modelo 65)**.

O valor informado é refletido diretamente na tag correspondente no XML do item:

```
<prod>
    <cProd>001</cProd>
    <cEAN>SEM GTIN</cEAN>
    <xProd>Produto Reforma</xProd>
    <NCM>11010010</NCM>
    <tpCredPresIBSZFM>0</tpCredPresIBSZFM>
    ...
</prod>
```

### Geração da nota de crédito

A geração automática do grupo de crédito presumido (`gCredPresIBSZFM`) no XML depende da combinação exata dos seguintes parâmetros fiscais:

- **Finalidade da Nota:** deve ser **5 (Crédito)**.
- **Tipo de Nota de Crédito (TOP):** deve ser configurado como **02 — Bens de capital (75%)**.
- **CST e Classificação:** o CST deve possuir o indicador de crédito presumido habilitado (`ind_gCredPresIBSZFM = 1`).

Estrutura XML gerada:

```
<gCredPresIBSZFM>
    <competApur>AAAA-MM</competApur>
    <tpCredPresIBSZFM>n</tpCredPresIBSZFM>
    <vCredPresIBSZFM>n.nn</vCredPresIBSZFM>
</gCredPresIBSZFM>
```

O sistema aplica as seguintes validações automáticas:

- Geração bloqueada em **NFC-e (Modelo 65)**.
- Unicidade por item: não pode haver mais de um item na mesma nota com o mesmo código de classificação (`tpCredPresIBSZFM`).
- O campo **Código de Classificação do Crédito Presumido (**`cCredPres`**)** exibe na pesquisa apenas os códigos compatíveis com o IBS (indicador `ind_gIBSCredPres = 1`, conforme Anexo IV da legislação). Códigos exclusivos de outros tributos (como o código 6, exclusivo da CBS) serão bloqueados no salvamento.
- O valor do crédito (`vCredPresIBSZFM`) deve ser obrigatoriamente maior que zero.
- O campo `competApur` não pode ser superior ao mês/ano atual da emissão.

---

## Pontos de atenção

- **Duplicidade:** o sistema impede o cadastro de regras duplicadas (mesma combinação de parâmetros) e exibe mensagem de erro com o ID do registro já existente.
- **Classificação:** informe NCM (produtos) ou NBS (serviços), nunca os dois no mesmo cadastro.
- **Localidade:** UF e Município devem conter códigos válidos — campos com valores inválidos ficam vazios após Tab/Enter, sem gerar mensagem de erro.
- **Prioridade de Finalidade:** se um item da nota tiver finalidade diferente do cabeçalho, o sistema usará a finalidade do item para buscar a alíquota. Se o item estiver vazio, herda a do cabeçalho.
- **Regra de Desempate:** se duas alíquotas tiverem a mesma pontuação de ranqueamento, o sistema selecionará a de vigência mais recente.
- **Bloqueios ZFM:** o crédito presumido de IBS para ZFM é exclusivo para NF-e (Modelo 55).
- **Precisão:** o valor da alíquota aceita no máximo 4 casas decimais.
- **Impactos:** alíquotas incorretas afetam diretamente as notas fiscais, relatórios fiscais e podem gerar problemas em auditorias da Receita Federal.

---

## Cálculos

Entenda como são feitas as composições dos cálculos dos impostos da Reforma Tributária.

### Composição da Base de Cálculo (`vBC`)

```
vBC = vProd + vServ + vFrete + vSeg + vOutro + vII - vDesc - vPis* -
vCofins* - vICMS - vICMSUFDest - vFCP - vFCPUFDest - vICMSMono - vISSQN + vIS
```

Itens com \* serão subtraídos apenas se compuserem o valor do item.

**ℹ️ Nota**

A partir da versão 5.22.0 do **Módulo ERP Core**, o Sankhya Om deduz da `vBC` apenas o ICMS destacado no documento (`vICMS`). O ICMS desonerado (`vICMSDeson`) não é mais deduzido e permanece na base de cálculo do IBS e da CBS. O campo `motDesICMS` não altera a base.

Na desoneração parcial, apenas o `vICMS` é deduzido. Exemplo: em uma operação de R$ 1.000,00 com `vICMS` de R$ 100,00 e `vICMSDeson` de R$ 80,00, a base é de R$ 900,00. Na desoneração total (`vICMS` igual a 0,00), nenhum ICMS é deduzido e a base corresponde ao valor bruto da operação.

### Diferimento

Se IBS da UF:

```
vDif = vBC * pIBSUF * pDif
```

Se IBS do Município:

```
vDif = vBC * pIBSMun * pDif
```

### Redução de alíquota e cálculo da alíquota efetiva

Se IBS da UF:

```
pAliqEfet = pIBSUF × (1 - (pRedAliq ÷ 100))
```

Se IBS do Município:

```
pAliqEfet = pIBSMun × (1 - (pRedAliq ÷ 100))
```

### Crédito Presumido

Para a UF:

```
vCredPres = vIBSUF * (1 - pCredPres / 100)
```

Para o Município:

```
vCredPres = vIBSMun * (1 - pCredPres / 100)
```

Para o cálculo do crédito presumido na ZFM (`vCredPresIBSZFM`), o valor deve ser obrigatoriamente positivo e a competência de apuração (`competApur`) não pode ser superior à data atual.

### Cálculo do valor do IBS

Para a UF:

```
Se pAliqEfet ≠ 0:
    vIBSUF = vBC * pAliqEfet - vDif - vDevTrib
Senão:
    vIBSUF = vBC * pIBSUF - vDif - vDevTrib
```

Para o Município:

```
Se pAliqEfet ≠ 0:
    vIBSMun = vBC * pAliqEfet - vDif - vDevTrib
Senão:
    vIBSMun = vBC * pIBSMun - vDif - vDevTrib
```

O valor total do IBS do item (`vIBS`) é o somatório de `vIBSUF` e `vIBSMun`, deduzido do crédito presumido quando aplicável:

```
vIBS = vIBSUF + vIBSMun – vCredPres (se indDeduzCredPres = 1)
```

### Cálculo da alíquota efetiva — IBS UF

Se o grupo de redução `gIBSUF/gRed` estiver informado:

Sem compra governamental:

```
pAliqEfet = pIBSUF × (1 - pRedAliq / 100)
```

Com compra governamental:

```
pAliqEfet = pIBSUF × (1 - pRedAliq / 100) × (1 - pRedutor / 100)
```

### Cálculo da alíquota efetiva — IBS Município

Se o grupo de redução `gIBSMun/gRed` estiver informado:

Sem compra governamental:

```
pAliqEfet = pIBSMun × (1 - pRedAliq / 100)
```

Com compra governamental:

```
pAliqEfet = pIBSMun × (1 - pRedAliq / 100) × (1 - pRedutor / 100)
```

**💡 Dica**

Para saber o que significa cada sigla, acesse o [Glossário de Termos Técnicos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais). Para entender o contexto completo da Reforma Tributária, acesse o [Guia completo da Reforma Tributária](https://www.sankhya.com.br/guia-reforma-tributaria/) e a [Seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria) na central de ajuda.

---

## Perguntas frequentes

### Posso cadastrar uma alíquota sem especificar empresa?

Sim. Preenchendo o campo **Empresa** com **0**, a alíquota será aplicada a todas as empresas que atenderem aos demais critérios — funcionando como regra padrão quando não há configurações mais específicas.

### Como funciona a validação de NCM e NBS?

O sistema permite três situações: apenas NCM preenchido, apenas NBS preenchido, ou ambos vazios. Se você tentar preencher os dois simultaneamente, o sistema bloqueia o salvamento com a mensagem "Não é possível cadastrar uma alíquota para um produto e serviço simultaneamente". Use NCM para produtos físicos e NBS para serviços.

### O que acontece se eu informar uma UF ou Município inválido?

O sistema não gera mensagem de erro imediata. Ao pressionar Tab ou Enter após digitar um código inválido, o campo fica vazio — indicando que o código não existe na tabela oficial. Use apenas códigos válidos de UF (2 dígitos) e municípios compatíveis com a UF selecionada.

### Posso usar códigos parciais em CNAE, NCM ou NBS?

Sim. O sistema aceita códigos hierárquicos para criar regras mais abrangentes. Por exemplo: **1** aplica a toda a seção 1, **1.1** aplica à divisão 1.1, e **1.1.11** aplica apenas à classe específica. Isso é útil para criar regras por categoria em vez de produto por produto.

### Como altero a vigência de uma alíquota já cadastrada?

Use a função **Editar**, selecione a alíquota e modifique as datas de início e/ou fim. Se houver conflito com outras alíquotas, o sistema exibirá uma mensagem específica.

### Quantas casas decimais posso usar na alíquota?

O campo aceita até 4 casas decimais (exemplo: 12,3456%). Se você digitar mais, o sistema pode bloquear a entrada ou arredondar automaticamente. Use sempre vírgula como separador decimal.

### Se eu duplicar uma alíquota, posso modificar qualquer campo?

Sim. Após duplicar, você pode modificar qualquer campo antes de salvar. O sistema cria uma nova linha com novo ID único — a alíquota original permanece inalterada. As mesmas regras de validação de um cadastro novo se aplicam.

### Como o sistema escolhe qual alíquota aplicar se houver várias regras que se encaixam?

O motor de cálculo utiliza uma hierarquia rígida, do mais específico para o mais genérico:

- **1ª prioridade — Produto/Serviço:** regras que especificam o item (NCM/NBS) têm precedência sobre as demais.
- **2ª prioridade — Parceiro:** se não houver regra por produto, o sistema aplica a regra específica do Parceiro (Código ou Grupo).
- **3ª prioridade — Empresa e Operação:** se não houver regra para produto nem parceiro, o sistema usa a regra geral configurada para a Empresa ou para a TOP/Finalidade da operação.

### Posso ter alíquotas com vigências sobrepostas?

Para a mesma combinação de parâmetros, vigências sobrepostas podem causar ambiguidade no cálculo. Use datas de fim em uma alíquota e datas de início na próxima para fazer transições limpas.

### O que significa o ID único que o sistema gera?

Cada alíquota recebe um identificador único criado automaticamente pelo banco de dados. Ele é usado internamente pelo sistema e aparece em mensagens de erro de duplicidade — útil para identificar registros específicos quando necessário.

### Como visualizo o valor do IBS calculado em uma nota fiscal?

Após salvar a nota, confira o detalhamento completo do IBS no rodapé do documento: base de cálculo, valores de diferimento, créditos e devoluções, imposto calculado separadamente para UF e Município, e valor total do IBS.

### O que acontece se a finalidade do item for diferente da finalidade do cabeçalho?

O motor de seleção priorizará a finalidade informada no item, garantindo que cada produto receba a tributação correta de acordo com sua natureza específica.
