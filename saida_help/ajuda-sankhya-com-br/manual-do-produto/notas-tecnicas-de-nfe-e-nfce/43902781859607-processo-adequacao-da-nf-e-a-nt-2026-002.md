---
id: "43902781859607"
titulo: "Processo Adequação da NF-e à NT 2026.002 (v1.00 a v1.11) — Referenciamento de Documentos Fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-14T12:36:07Z"
---

# Processo Adequação da NF-e à NT 2026.002 (v1.00 a v1.11) — Referenciamento de Documentos Fiscais

**Versão mínima:** Módulo ERP Core 5.22.0 · Sankhya Om 4.36

**Caminho de acesso:**
[**Portal de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111953-Portal-de-Compras)
[**Portal de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas)
[**Central de Vendas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612374-Central-de-Vendas-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) **|** [**Central de Compras**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044593974-Central-de-Compras-Grade-Itens-Bot%C3%A3o-Outras-Op%C3%A7%C3%B5es) **› Grade Itens › Outras Opções › Documentos relacionados**

---

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#oque) [Contexto regulatório](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#contexto) [O que foi alterado](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#alterado)    ↳ [NT 2026.002 v1.00](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#v100) | ↳ [NT 2026.002 v1.10 e v1.10a](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#v110)    ↳ [NT 2026.002 v1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#v111) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#pontos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#faq) |
| --- | --- |

## O que é e para que serve

O **Processo Adequação da NF-e à NT 2026.002** descreve como o emissor de NF-e e NFC-e (modelos 55 e 65) do **Sankhya Om** trata cada versão da **Nota Técnica 2026.002**, emitida pelo ENCAT: v1.00, v1.10, v1.10a e v1.11. A adequação que exigiu ajuste na solução, introduzida na v1.10 e mantida na v1.10a, faz o **Sankhya Om** omitir do XML os referenciamentos a documentos fiscais legados vedados: nota fiscal em papel modelo 1/1A, nota fiscal de produtor e cupom fiscal ECF. A adequação é aplicada automaticamente a partir das datas de vigência e garante que NF-e de devolução, complementação ou aquisição que tenham esses documentos como origem continuem sendo autorizadas pela SEFAZ. A forma de vincular as notas de origem no **Sankhya Om** não mudou: o referenciamento continua sendo gerado a partir do faturamento ou da devolução nos portais e da opção **Documentos relacionados** nas centrais.

Esta adequação não altera telas, não cria parâmetro nem configuração por empresa, não converte um referenciamento legado em chave de acesso eletrônica e não reprocessa NF-e já autorizadas. O **Sankhya Om** também não exigiu alteração para atender a regra BA02-35, de validação do modelo da chave referenciada, e não oferece suporte ao DANFE Simplificado Tipo 2.

---

## Contexto regulatório

A NT 2026.002 v1.10a proíbe, no grupo **Informação de Documentos Fiscais Referenciados** (`NFref`, Grupo BA), três tipos de referenciamento que não identificam o documento de origem por chave de acesso eletrônica. NF-e transmitidas com esses referenciamentos após as datas de vigência são rejeitadas pela SEFAZ — o que bloqueia o faturamento de quem ainda referencia documentos em papel ou cupom fiscal.

| **Campo no XML** | **Documento referenciado** | **Regra da NT** |
| --- | --- | --- |
| `refNF` | Nota fiscal em papel modelo 1/1A | BA03-10 |
| `refNFP` | Nota fiscal de produtor | BA10-10 |
| `refECF` | Cupom fiscal emitido por ECF | BA20-30 |

As datas de vigência são:

- Ambiente de homologação: a partir de 01/09/2026
- Ambiente de produção: a partir de 05/10/2026

São especialmente impactados:

- Clientes que emitem NF-e de devolução ou complementação de notas recebidas ou emitidas em papel
- Clientes que adquirem mercadorias de produtor rural com nota fiscal de produtor
- Clientes que emitem NF-e de devolução de vendas realizadas com cupom fiscal ECF

Norma de referência: NT 2026.002 v1.10a (ENCAT) — Grupo BA, regras BA03-10, BA10-10 e BA20-30.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#sumario)

---

## O que foi alterado

A NT 2026.002 foi publicada em quatro versões: v1.00, v1.10, v1.10a e v1.11. As seções abaixo trazem, para cada versão, os prazos de vigência e o tratamento dado no **Sankhya Om**. Apenas as versões v1.10 e v1.10a exigiram ajuste na solução.

### NT 2026.002 v1.00 — DANFE Simplificado Tipo 2

A v1.00 introduz o DANFE Simplificado Tipo 2. O **Sankhya Om** não oferece suporte ao DANFE Simplificado Tipo 2. As regras I08-180 e BA02-35 foram avaliadas nesta versão e não exigiram alteração na solução. Para ver o detalhe de cada regra, acesse [NT 2026.002 v1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#v111).

Prazos de vigência da versão:

- Ambiente de homologação: a partir de 01/07/2026
- Ambiente de produção: a partir de 03/08/2026

### NT 2026.002 v1.10 e v1.10a — Alteração nas regras de referenciamento

Esta seção cobre as duas versões que alteram as regras de referenciamento de documentos fiscais:

- v1.10: DANFE Simplificado Tipo 2 e alteração nas regras de referenciamento
- v1.10a: DANFE Simplificado Tipo 2, alteração nas regras de referenciamento e validações de nota fiscal de produtor referenciada

Prazos de vigência das versões:

- Ambiente de homologação: a partir de 01/09/2026
- Ambiente de produção: a partir de 05/10/2026

O **Sankhya Om** foi ajustado para tratar as regras de validação BA03-10, BA10-10 e BA20-30, que deixam de suportar o referenciamento a nota fiscal em papel, nota fiscal de produtor e cupom fiscal ECF (`refNF`, `refNFP` e `refECF`). A v1.10a não alterou o que foi implementado para a v1.10: o tratamento permanece em vigor nas mesmas datas. As demais implementações e alterações em regras de validação das duas versões foram avaliadas e não exigiram alteração na solução. Para ver as regras BA02-35 e VC02-40, acesse [NT 2026.002 v1.11](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#v111).

As seções abaixo descrevem o comportamento do **Sankhya Om** 4.36 a partir do **Módulo ERP Core 5.22.0**. Todas as mudanças são aplicadas automaticamente na geração do XML — nenhuma configuração é necessária. A ação do usuário só é necessária no cenário de nota de crédito descrito em [Nota de crédito que exige referenciamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#credito).

**⚠️ Atenção**

A adequação está disponível apenas no **Sankhya Om** 4.36 e não é oferecida na versão 4.35. Empresas na versão 4.35 que emitem NF-e referenciando nota em papel, nota de produtor ou cupom ECF precisam atualizar para a 4.36 antes de 05/10/2026 — sem a atualização, essas NF-e são rejeitadas pela SEFAZ a partir dessa data.

#### Supressão dos referenciamentos vedados

A partir da data de vigência do ambiente de destino, o **Sankhya Om** deixa de gerar no XML da NF-e os campos `refNF`, `refNFP` e `refECF`, mesmo que a nota de origem correspondente esteja vinculada. A vinculação no **Sankhya Om** permanece como está: a nota de origem continua registrada nos portais e em **Documentos relacionados**, e apenas o campo vedado deixa de ser enviado à SEFAZ.

A regra funciona da seguinte forma:

- **Data considerada** — o **Sankhya Om** compara a data em que o XML é gerado para transmissão com a data de vigência. A data de emissão da nota não é considerada.
- **Ambientes independentes** — homologação e produção têm datas próprias. A vigência em homologação não antecipa a supressão em produção.
- **Antes da vigência** — o XML continua sendo gerado com `refNF`, `refNFP` e `refECF`, como antes da adequação.
- **Dados de devolução** — a nota de origem continua sendo considerada no cálculo das informações de devolução, como o **Percentual da mercadoria devolvida** (`pDevol`) e o **Valor do IPI devolvido** (`vIPIDevol`).

**ℹ️ Nota**

A NT 2026.002 não aparece como nota técnica disponível para ativação em **Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e**. O foco principal dessa NT são as operações de vendas presenciais e não presenciais com impressão do DANFE Simplificado Tipo 2, que não foi implementado. A supressão dos referenciamentos vedados é aplicada automaticamente com base nas datas de vigência, e não depende da ativação ou inativação de nenhuma nota técnica nas **Preferências da Empresa**.

#### Referenciamentos preservados

A supressão atinge exclusivamente os três campos vedados. O **Sankhya Om** continua gerando normalmente os referenciamentos por chave de acesso eletrônica e os demais campos do grupo **Informação de Documentos Fiscais Referenciados** (`NFref`):

- **Chave de acesso da NF-e referenciada** (`refNFe`)
- **Chave de acesso do CT-e referenciado** (`refCTe`)
- **Chave de acesso da NF-e referenciada com código numérico zerado** (`refNFeSig`)

O campo `refNFeSig` é gerado quando a marcação **Gerar chave referenciada sigilosa?** está ativa em **Preferências da Empresa** e preserva o sigilo fiscal da NF-e referenciada. Para saber mais, acesse [Processo Adequação da NF-e à NT 2022.003 v.1.00](https://ajuda.sankhya.com.br/hc/pt-br/articles/42733329043351-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2022-003-v-1-00).

Quando a NF-e tem origens mistas — por exemplo, uma NF-e eletrônica e uma nota em papel —, só o referenciamento vedado é omitido. O `refNFe` da origem eletrônica permanece íntegro no XML autorizado.

#### Nota de crédito que exige referenciamento

Em empresas com a NT 2025.002 RTC ativa, a TOP de nota de crédito que exige referenciamento continua bloqueando a emissão quando a nota fica sem nenhum documento referenciado. Se a única origem vinculada for uma nota em papel, uma nota de produtor ou um cupom ECF, a supressão remove esse referenciamento e o **Sankhya Om** bloqueia a emissão localmente, sem transmitir à SEFAZ.

Nesse caso, o **Sankhya Om** exibe a mensagem "Este tipo de nota exige documento fiscal referenciado, mas o único referenciamento existente (tag refNF) foi omitido do XML por vedação da NT 2026.002 (BA03-10 refNF, BA10-10 refNFP, BA20-30 refECF). Referencie um documento fiscal eletrônico por chave de acesso (refNFe) para emitir esta nota." A tag indicada entre parênteses corresponde ao referenciamento suprimido na nota — `refNF`, `refNFP` ou `refECF`. Para concluir a emissão, vincule como origem uma NF-e com chave de acesso em **Documentos relacionados**.

**⚠️ Atenção**

Vincular novamente a mesma nota em papel, nota de produtor ou cupom ECF não resolve o bloqueio. Após a vigência, esses documentos não são aceitos como referência na NF-e.

### NT 2026.002 v1.11 — Prorrogação da entrada em produção de regras de validação

A v1.11 altera a data de entrada em produção das regras de validação I08-180, BA02-35 e VC02-40. Nenhuma das três exigiu alteração no **Sankhya Om**, e a prorrogação também não impacta a solução.

Prazos de vigência da versão:

- Ambiente de homologação: a partir de 01/09/2026
- Ambiente de produção: a partir de 14/12/2026

As regras BA02-35 e VC02-40 vedam os mesmos modelos de documento, mas atuam em grupos diferentes do XML. A BA02-35 atua no grupo **Informação de Documentos Fiscais Referenciados** (`NFref`, Grupo BA), que referencia o documento fiscal pela tag `refNFe`. A VC02-40 atua no grupo **Referenciamento de item de outro Documento Fiscal Eletrônico - DF-e** (Grupo VC), que referencia o item do documento pela tag `DFeReferenciado/chaveAcesso`.

Situação de cada regra:

- I08-180: regra da v1.00 que proíbe NF-e com lançamento relativo a Cupom Fiscal (CFOP 5.929 ou 6.929) referenciando uma NFC-e. A análise da v1.00 não identificou necessidade de alteração no **Sankhya Om**.
- BA02-35: regra da v1.00 que se aplica à NF-e de saída (`tpNF=1`) com NF-e referenciada (`refNFe`) e finalidade (`finNFe`) diferente de 2 (NF-e complementar) e de 4 (NF-e de devolução). Nesses casos, o modelo da NF-e referenciada não pode ser:

  - NFC-e (modelo 65)
  - CF-e (modelo 59)
  - NF-e (modelo 55) com DANFE Simplificado Tipo 2 (`tpImp=6`)

  A análise da v1.00 e da v1.10 não identificou necessidade de alteração no **Sankhya Om**.
- VC02-40: regra da v1.10 que proíbe, na NF-e de saída, o referenciamento de chaves de acesso de documentos dos modelos abaixo:

  - NFC-e (modelo 65)
  - CF-e (modelo 59)
  - NF-e (modelo 55) com DANFE Simplificado Tipo 2 (`tpImp=6`), quando a finalidade da NF-e (`finNFe`) for diferente de 2 (NF-e complementar) e de 4 (NF-e de devolução)

  A análise da v1.10 não identificou necessidade de alteração no **Sankhya Om**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#sumario)

---

## Pontos de atenção

A supressão vale para todas as empresas que emitem NF-e e NFC-e (modelos 55 e 65), inclusive as que ainda não ativaram a NT 2025.002 RTC. A vedação do Grupo BA não depende da Reforma Tributária.

O campo `refECF` é suprimido em todas as UFs. A regra BA20-30 permite que cada UF decida se aplica a validação, mas o **Sankhya Om** adota a supressão nacional para evitar rejeições.

A supressão não gera aviso na tela. Para saber se um referenciamento foi omitido, consulte o XML autorizado: o grupo `NFref` não contém `refNF`, `refNFP` nem `refECF`. NF-e autorizadas antes das datas de vigência não são reprocessadas e mantêm o XML original.

**⚠️ Atenção**

Integrações externas que leem o XML da NF-e e esperam encontrar `refNF`, `refNFP` ou `refECF` precisam ser ajustadas. Após a vigência, esses campos não constam nos XML autorizados.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43902781859607-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2026-002-v1-00-a-v1-11-Referenciamento-de-Documentos-Fiscais#sumario)

---

## Perguntas frequentes

### Preciso configurar alguma coisa para a adequação funcionar?

Não. Basta estar no **Sankhya Om** 4.36 com o **Módulo ERP Core 5.22.0** ou superior. A supressão é aplicada automaticamente a partir da data de vigência de cada ambiente, sem parâmetro nem configuração por empresa.

### Preciso ativar a NT 2026.002 nas Preferências da Empresa?

Não. A NT 2026.002 não é listada na sub-aba **Nota Técnica NF-e** das **Preferências da Empresa**, porque o DANFE Simplificado Tipo 2 — foco principal da NT — não foi implementado. A supressão ocorre automaticamente a partir das datas de vigência de cada ambiente.

### Minha empresa está na versão 4.35. A adequação está disponível?

Não. A adequação é oferecida apenas no **Sankhya Om** 4.36. Atualize para a 4.36 com o **Módulo ERP Core 5.22.0** ou superior antes de 05/10/2026 para evitar a rejeição de NF-e com referenciamentos vedados.

### Minha empresa ainda não ativou a NT 2025.002 RTC. A mudança me afeta?

Sim. A vedação vale para todo emissor de NF-e e NFC-e (modelos 55 e 65), independentemente da Reforma Tributária. A única regra que depende da NT 2025.002 RTC ativa é o bloqueio da nota de crédito sem referenciamento.

### A nota de origem em papel deixa de ficar vinculada à NF-e no Sankhya Om?

Não. A vinculação continua registrada nos portais e em **Documentos relacionados**, e continua sendo usada no cálculo das informações de devolução. Só o campo vedado deixa de ser gerado no XML enviado à SEFAZ.

### Qual a relação com a regra de referenciamento em devoluções da NT 2025.002 RTC?

São regras complementares. A partir de 16/11/2026, a regra VC02-14 passa a exigir o referenciamento por item em NF-e de devolução. A NT 2026.002 v1.10a proíbe os referenciamentos a documentos em papel, de produtor e ECF em qualquer NF-e. Para saber mais sobre a VC02-14, acesse [Processo Adequação da NF-e à NT 2025.002 v1.40 RTC (IBS/CBS/IS)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42661261578647-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-40-RTC-IBS-CBS-IS#referenciamentodfedevolucoes).
