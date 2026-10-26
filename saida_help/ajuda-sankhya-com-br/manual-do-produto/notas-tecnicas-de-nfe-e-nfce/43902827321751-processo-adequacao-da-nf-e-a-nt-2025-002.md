---
id: "43902827321751"
titulo: "Processo Adequação da NF-e à NT 2025.002 v1.51 e v1.52 RTC (IBS/CBS/IS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
rotulos: ["NT 2025.002 v1.51"]
---

# Processo Adequação da NF-e à NT 2025.002 v1.51 e v1.52 RTC (IBS/CBS/IS)

**Versão mínima (v1.51):** Módulo ERP Core 5.22.0 · Módulo Livros Fiscais 5.47.0 · Sankhya Om 4.35 e 4.36
**Versão mínima (v1.52):** sem alteração no Sankhya Om

**Caminho de acesso:**
**Menu Principal ›** [**Tipo de Operação - TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) **› aba Impostos**
**Menu Principal › Cadastros ›** [**Produtos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-) **› aba Combustível**
**Menu Principal › Livros Fiscais › Cadastros › Alíquotas Monofásicas**

---

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#oque) [Contexto regulatório](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#contexto) [O que foi alterado](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#alterado)    ↳ [NT 2025.002 RTC v1.51](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#v151)    ↳ [NT 2025.002 RTC v1.52](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#v152) | [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#pontos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#faq) |
| --- | --- |

## O que é e para que serve

O **Processo Adequação da NF-e à NT 2025.002 RTC** descreve, por versão, as adequações do emissor de NF-e e NFC-e do **Sankhya Om** à **Nota Técnica 2025.002 RTC**. A v1.51 trata das regras B25-80 e UB12-10: a partir dela, o **Sankhya Om** deixa de bloquear o cálculo e o envio de ICMS, IPI, PIS e COFINS em notas de crédito e de débito — quem define os tributos é a TOP e quem valida é a SEFAZ. Também passa a manter atualizada a tabela de combustíveis sujeitos à tributação monofásica, usada na classificação desses itens. A v1.52 corrige a regra de validação VC02-50 de NF-e de devolução de mercadoria e altera a data de entrada em produção da regra VC02-14, prevista desde a v1.51, sem alteração no **Sankhya Om**.

Esta adequação não define quais tributos cada nota de crédito ou de débito deve conter, não valida localmente essas combinações e não altera o cálculo de IBS e CBS. Este artigo não cobre a ativação inicial da NT 2025.002 RTC; para isso, consulte [Como ativar a Nota Técnica 2025.002 para emissão de NF com novos impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/35328394477975-Como-ativar-a-Nota-T%C3%A9cnica-2025-002-para-emiss%C3%A3o-de-NF-com-novos-impostos).

---

## Contexto regulatório

As versões v1.51 e v1.52 da NT 2025.002 RTC revisaram regras de validação que afetam a emissão de NF-e e NFC-e com IBS e CBS. A VC02-14 consta desde a v1.51, e a v1.52 alterou apenas a data de entrada em produção:

- **B25-80 (Grupo B — Identificação da NF-e) — v1.51** — trata dos tributos permitidos em notas de crédito (`finNFe=5`) e de débito (`finNFe=6`). A redação da regra mudou nas versões 1.31, 1.36 e 1.51 da NT, e a validação é feita pela SEFAZ.
- **UB12-10 (Grupo UB — Informações dos tributos IBS/CBS) — v1.51** — define quando o grupo **Grupo de Informações do IBS e da CBS** (`gIBSCBS`) é obrigatório e dispensa desse grupo os itens de combustíveis sujeitos à tributação monofásica.
- **VC02-14 (NF-e de devolução de mercadoria) — v1.51** — proíbe o referenciamento da nota de origem na tag `refNFe` na devolução (`finNFe=4`), que deve ser feito no grupo `DFeReferenciado`. A redação da regra não mudou na v1.52; mudou a data de entrada em produção.
- **VC02-50 (NF-e de devolução de mercadoria) — v1.52** — a comparação entre o emitente do documento referenciado e o destinatário da NF-e de devolução passa a valer apenas quando o documento referenciado também for de saída.

As regras têm as seguintes datas de implantação. Os prazos da VC02-14 e da VC02-50 em produção refletem a prorrogação para 16/11/2026, divulgada em comunicado posterior à publicação da v1.52:

| **Versão** | **Regra** | **Homologação\*** | **Produção** |
| --- | --- | --- | --- |
| v1.51 | **B25-80** | Até 01/09/2026 | 05/10/2026 |
| v1.51 | **UB12-10** | Até 03/08/2026 | 03/08/2026 |
| v1.51 | **VC02-14** | — | 16/11/2026 (antes, 05/10/2026 na v1.51 e 03/11/2026 na v1.52) |
| v1.52 | **VC02-50** | Até 26/10/2026 (antes, 05/10/2026) | 16/11/2026 (antes, 03/11/2026) |

\* A implantação em homologação pode variar por UF nesse período.

São especialmente impactados:

- Clientes que emitem notas de crédito ou de débito e precisam informar tributos tradicionais
- Clientes que comercializam combustíveis sujeitos à tributação monofásica
- Clientes que emitem NF-e de devolução de mercadoria

**Normas de referência:** NT 2025.002 RTC v1.51 — regras B25-80, UB12-10 e VC02-14 · NT 2025.002 RTC v1.52 — regra VC02-50 e nova data da VC02-14 · comunicado de prorrogação dos prazos da v1.52 · Ajuste SINIEF nº 49/25 · Tabela de Combustíveis Sujeitos à Tributação Monofásica (ENCAT/ANP).

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#sumario)

---

## O que foi alterado

As seções abaixo descrevem as alterações por versão da NT: [NT 2025.002 RTC v1.51](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#v151) e [NT 2025.002 RTC v1.52](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#v152). Para ver todas as versões das notas técnicas de NF-e e NFC-e, acesse [Processo Notas Técnicas de NFe e NFCe](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732070683287-Processo-Notas-T%C3%A9cnicas-de-NFe-e-NFCe).

### NT 2025.002 RTC v1.51

As seções abaixo descrevem o comportamento do **Sankhya Om** a partir do **Módulo ERP Core 5.22.0** e do **Módulo Livros Fiscais 5.47.0**, nas versões 4.35 e 4.36. Nenhum parâmetro novo foi criado. A ação do usuário é necessária apenas para revisar as TOPs de notas de crédito e de débito e o cadastro dos combustíveis monofásicos.

#### Tributos tradicionais em notas de crédito e débito

Até esta versão, o **Sankhya Om** desmarcava automaticamente as marcações **Tem ICMS**, **Tem IPI**, **Tem Pis** e **Tem Cofins** ao salvar uma TOP de nota de crédito ou de débito, e zerava esses tributos no cálculo e no XML. Com a adequação à regra B25-80, esse bloqueio foi removido.

O comportamento passa a ser o seguinte:

- **Marcações da TOP** — as marcações **Tem ICMS**, **Tem IPI**, **Tem Pis** e **Tem Cofins** da aba **Impostos** permanecem como você salvou.
- **Cálculo e envio** — o tributo marcado na TOP é calculado e enviado no XML. O tributo desmarcado não é calculado.
- **Validação** — o **Sankhya Om** não bloqueia a emissão. A SEFAZ aceita ou rejeita a nota conforme a regra vigente.

O comportamento vale a partir da atualização de versão, sem depender de data de vigência. As demais finalidades de NF-e (normal, complementar, de ajuste e de devolução) não foram alteradas.

**⚠️ Atenção**

Como o **Sankhya Om** não bloqueia mais os tributos tradicionais nessas notas, a SEFAZ pode rejeitar a emissão com a mensagem "Rejeição: NF-e com finalidade de débito ou crédito somente para IBS/CBS" (Msg 1001). Antes de marcar tributos tradicionais em uma TOP de nota de crédito ou de débito, confirme se a operação está entre as permitidas pela NT e pelo Ajuste SINIEF nº 49/25.

#### Combustíveis sujeitos à tributação monofásica

A regra UB12-10 dispensa do grupo `gIBSCBS` os itens de combustíveis sujeitos à tributação monofásica. Esses itens devem ser emitidos com o CST e a classificação tributária de monofasia aplicáveis à operação — com essa classificação, o **Sankhya Om** não gera o grupo `gIBSCBS`, sem nenhuma regra adicional no emissor. O tratamento se aplica às empresas com a NT 2025.002 RTC ativa, a partir das datas de vigência da v1.51.

O **Sankhya Om** passou a manter a **Tabela de Combustíveis Sujeitos à Tributação Monofásica** (ENCAT/ANP), atualizada automaticamente, sem necessidade de nova versão. A tabela é relacionada ao campo **Código ANP** da aba **Combustível** do cadastro de **Produtos**. Registros que deixam de constar na tabela oficial são inativados com data de fim de vigência, e não excluídos, para preservar o histórico.

Para emitir corretamente esses itens:

1. Acesse **Menu Principal › Cadastros › Produtos**.
2. Na aba **Combustível**, confira se o campo **Código ANP** está preenchido com o código do combustível.
3. Acesse **Menu Principal › Livros Fiscais › Cadastros › Alíquotas Monofásicas**, cadastre o IBS e a CBS do combustível e informe o CST e a classificação tributária de monofasia aplicáveis à operação.

A tributação monofásica de IBS e CBS é configurada exclusivamente na tela **Alíquotas Monofásicas**, sem relação com os cadastros de **Alíquotas de IBS** e **Alíquotas de CBS**. Para essas operações, utilize o CST `620` — Tributação monofásica — e a classificação tributária correspondente à aplicação.

**⚠️ Atenção**

Nesta versão, o **Sankhya Om** ainda não gera o grupo **Grupo de Informações do IBS e da CBS em operações com tributação monofásica** (`gIBSCBSMono`) para itens classificados com CST de monofasia. Sem esse grupo, a SEFAZ pode rejeitar a NF-e pela regra UB13-40. A geração do grupo está prevista para novembro de 2026.

#### Referenciamento da nota de origem na devolução (VC02-14)

A regra VC02-14 consta na v1.51 e trata do referenciamento da nota de origem na NF-e de devolução de mercadoria. O comportamento da regra é o seguinte:

- **Referenciamento** — na NF-e de devolução de mercadoria (`finNFe=4`), a nota de origem deve ser referenciada por item, no grupo `DFeReferenciado` (`chaveAcesso`).
- **Tag refNFe** — fica proibido referenciar a nota de origem nessa tag na devolução.
- **Prazo** — produção em 05/10/2026, data original da v1.51, alterada na v1.52.

A redação da regra não mudou entre as versões; mudou apenas a data de entrada em produção. Consulte também [Referenciamento da nota de origem na devolução na NT 2025.002 RTC v1.52](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#vc0214).

### NT 2025.002 RTC v1.52

As seções abaixo descrevem as alterações da NT 2025.002 RTC v1.52 nas regras de validação de NF-e de devolução de mercadoria (`finNFe=4`). Não houve alteração no **Sankhya Om** e nenhum parâmetro novo foi criado.

#### Validação do emitente do documento referenciado em NF-e de devolução de saída

Até esta versão, a regra VC02-50 exigia, na NF-e de devolução de mercadoria de saída (`finNFe=4` e `tpNF=1`), que o CNPJ/CPF do emitente do documento referenciado fosse igual ao CNPJ/CPF do destinatário da NF-e atual, sem considerar o tipo do documento referenciado. Com a correção da redação da regra, o comportamento passa a ser o seguinte:

- **Documento referenciado de saída** — quando o `DFeReferenciado` for de saída (`tpNF=1`), o CNPJ/CPF do emitente dele deve ser igual ao CNPJ/CPF do destinatário da NF-e atual.
- **Documento referenciado de entrada** — a comparação entre emitente e destinatário não se aplica.
- **Nota Fiscal Avulsa (NFA)** — com o CNPJ da SEFAZ na chave de acesso, considera-se o CNPJ ou CPF do emitente.
- **Prazos** — homologação até 26/10/2026 (antes, 05/10/2026) e produção em 16/11/2026 (antes, 03/11/2026), conforme comunicado.

#### Referenciamento da nota de origem na devolução

A regra VC02-14 já estava prevista da mesma forma na [v1.51](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#vc0214v151) e não teve a redação alterada. Na v1.52, mudou apenas a data de entrada em produção: de 05/10/2026 para 03/11/2026 na NT e, depois, para 16/11/2026 conforme comunicado. O comportamento da regra é o seguinte:

- **Referenciamento** — na NF-e de devolução de mercadoria (`finNFe=4`), a nota de origem deve ser referenciada por item, no grupo `DFeReferenciado` (`chaveAcesso`).
- **Tag refNFe** — fica proibido referenciar a nota de origem nessa tag na devolução.
- **Prazo** — produção em 16/11/2026 (antes, 05/10/2026 na v1.51 e 03/11/2026 na v1.52).

**⚠️ Atenção**

A redação da NT ainda indica 03/11/2026 como data de implementação em produção. A prorrogação para 16/11/2026 foi divulgada em comunicado posterior, sem nova versão da NT. Considere 16/11/2026 como a data de implantação em produção.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#sumario)

---

## Pontos de atenção

Revise as TOPs de notas de crédito e de débito após a atualização. TOPs que tinham as marcações de tributos tradicionais desmarcadas automaticamente pelo **Sankhya Om** continuam desmarcadas — nada é remarcado sem sua ação.

Itens de combustível com o campo **Código ANP** preenchido, mas sem o cadastro com o CST e a classificação tributária de monofasia em **Alíquotas Monofásicas**, continuam gerando o grupo `gIBSCBS` normalmente. A dispensa depende da classificação tributária da operação, e não apenas do código ANP.

NF-e emitidas antes da atualização não são reprocessadas e mantêm o XML original.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#sumario)

---

## Perguntas frequentes

### Preciso ativar a v1.51 separadamente nas Preferências da Empresa?

Não. As adequações da v1.51 fazem parte da NT 2025.002 RTC já ativa na empresa e seguem as datas de vigência da v1.51. Basta estar no **Módulo ERP Core 5.22.0** e no **Módulo Livros Fiscais 5.47.0** ou superiores. A liberação dos tributos tradicionais em notas de crédito e débito vale a partir da atualização de versão.

### Minhas notas de crédito e débito passam a sair com ICMS automaticamente?

Não. O **Sankhya Om** só calcula os tributos marcados na aba **Impostos** da TOP. Se a TOP estiver com **Tem ICMS** desmarcado, a nota continua sem ICMS.

### Recebi a rejeição 1001 ao emitir uma nota de débito. O que fazer?

A SEFAZ não aceitou tributos tradicionais para essa operação. Revise a TOP e desmarque os tributos que não se aplicam, ou confirme se a operação está entre as exceções previstas no Ajuste SINIEF nº 49/25.

### Preciso cadastrar manualmente a tabela de combustíveis monofásicos?

Não. A tabela é atualizada automaticamente pelo **Sankhya Om**. Sua ação é manter o **Código ANP** preenchido no cadastro de **Produtos** e cadastrar o combustível em **Alíquotas Monofásicas** com o CST e a classificação tributária de monofasia aplicáveis à operação.

### A data de produção da regra VC02-14, prevista na v1.51, mudou?

Sim. A regra consta na v1.51 com produção em 05/10/2026. A redação não mudou, mas a data foi alterada para 03/11/2026 na v1.52 e, depois, para 16/11/2026, conforme comunicado. Considere 16/11/2026. Para saber mais, acesse [Referenciamento da nota de origem na devolução na NT 2025.002 RTC v1.52](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902827321751-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-51-e-v1-52-RTC-IBS-CBS-IS#vc0214).
