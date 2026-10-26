---
id: "33874590545943"
titulo: "Tela Cadastro de Alíquotas Monofásicas  - Reforma Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Cadastro de impostos"
atualizado_em: "2026-10-16T13:47:47Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "br.com.sankhya.mgeliv.cadastros.AliquotaMonofasica", "Reforma Tributária", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# Tela Cadastro de Alíquotas Monofásicas  - Reforma Tributária

**Módulo:** Fiscal / Tributário
**Versão mínima:** 4.17.05 (Módulo Livros Fiscais) · 4.33b172, 4.34b225, 4.35b221 (Sankhya W)
**Caminho de acesso:** **Menu Principal › Fiscal › Impostos › Alíquotas Monofásicas IBS/CBS**

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#oque) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#antes) [Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#fluxo) [Como cadastrar uma nova alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#cadastrar) [Como editar uma alíquota existente](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#editar) [Como duplicar uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#duplicar) | [Como excluir uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#excluir) [Visualização dos valores no documento fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#visualizar) [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#calculos) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#pontos-atencao) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33874590545943-Tela-Cadastro-de-Al%C3%ADquotas-Monof%C3%A1sicas-Reforma-Tribut%C3%A1ria#faq) |
| --- | --- |

---

## O que é e para que serve

A tela **Cadastro de Alíquotas Monofásicas IBS/CBS** é onde você gerencia as regras de tributação monofásica no Sankhya OM — cadastrando, editando, duplicando e excluindo alíquotas. Ela garante que os impostos sejam aplicados corretamente em cada operação, respeitando as regras fiscais, os períodos de vigência e as validações exigidas pela Reforma Tributária. A tela não cobre a configuração de alíquotas de IBS e CBS fora do regime monofásico.

![Imagem 1: A tela Cadastro de Alíquotas Monofásicas IBS/CBS é onde você gerencia as regras de tributação monofásica no Sankhya OM…](https://ajuda.sankhya.com.br/hc/article_attachments/39661651577239)

---

## Antes de começar

- Tabelas de referência atualizadas: UF, Município, CNAE, NCM, NBS, CST, `cClassTrib` e `TGFFOP`.
- Integração com tabelas oficiais e parametrização de regras gerais configuradas.
- Verifique as permissões de acesso antes de iniciar o cadastro. G
- Garanta que todas as tabelas de referência estejam atualizadas antes de cadastrar ou editar alíquotas.

---

## Diagrama de fluxo

O fluxo abaixo resume as etapas das principais ações na tela de Cadastro de Alíquotas Monofásicas IBS/CBS:

![Imagem 2: O fluxo abaixo resume as etapas das principais ações na tela de Cadastro de Alíquotas Monofásicas IBS/CBS:](https://ajuda.sankhya.com.br/hc/article_attachments/35190876296983)

---

## Como cadastrar uma nova alíquota

1. Acesse **Menu Principal › Fiscal › Impostos › Alíquotas Monofásicas IBS/CBS** e clique em **Cadastrar**.
2. Preencha os campos obrigatórios: **Empresa**, **Produto/Serviço**, **NCM/NBS**, **UF**, **Município** e **Vigência**.
3. Na aba **Tributação**, informe os valores de alíquotas ad rem para IBS e CBS conforme o contexto legal de cada campo:

| Grupo de alíquotas | Quando usar |
| --- | --- |
| **Alíquotas** | Tributação Monofásica Padrão (venda ou saída geral). Informar conforme o Art. 172 da LC 214/25. |
| **Alíquotas com Retenção Atual** | Operações com combustíveis derivados de petróleo para retenção do imposto sobre o biocombustível a ser misturado. Aplicação baseada no Art. 178 da LC 214/2025. |
| **Alíquotas com Retenção Anterior** | Tributação Monofásica Própria sobre combustíveis cobrada anteriormente. Aplicável nos casos de revenda, comercialização ou distribuição sem importação. |
| **Diferimento Monofásico** | Percentual de diferimento aplicado a operações específicas, como as envolvendo biocombustíveis (por exemplo, operações do produtor de biocombustível ou usina). |

**ℹ️ Nota**

Para criar regras gerais, deixe campos específicos em branco — eles serão gravados como **0**. NCM e NBS não podem ser preenchidos simultaneamente: o sistema bloqueará o cadastro e exibirá mensagem de erro. Preencha apenas um dos dois.

4. Clique em **Salvar**. O sistema validará todos os dados. Se estiverem corretos, o cadastro será confirmado; caso contrário, uma mensagem indicará o que precisa ser ajustado.

---

## Como editar uma alíquota existente

Use para corrigir dados, alterar percentuais ou ajustar vigências de alíquotas já cadastradas.

1. Use os **filtros** ou a **pesquisa avançada** para localizar a alíquota — você pode filtrar por empresa, operação, vigência ou produto.
2. Clique duas vezes na linha, com o botão direito do mouse, ou selecione-a e clique em **Editar**.
3. Altere os campos necessários e clique em **Salvar** ou use **Ctrl+S**.

---

## Como duplicar uma alíquota

Use para criar variações de alíquotas similares, otimizando o tempo de cadastro quando você tem regras parecidas.

1. Selecione a alíquota que servirá como modelo.
2. Clique em **Duplicar**. O sistema criará uma cópia em modo de edição.
3. Ajuste os campos desejados e clique em **Salvar**.

---

## Como excluir uma alíquota

1. Use os filtros para localizar a alíquota que deseja remover.
2. Clique duas vezes na linha, com o botão direito do mouse, ou selecione-a e clique em **Excluir**.
3. Confirme a exclusão na janela de confirmação.

---

## Visualização dos valores no documento fiscal

Ao emitir um documento fiscal com incidência de IBS ou CBS no regime monofásico, o sistema calcula automaticamente os tributos conforme a quantidade tributável (`qTrib`) e a alíquota ad rem cadastrada. Você encontra no rodapé da nota fiscal os campos específicos para o regime monofásico:

- `vIBSMono` **e** `vCBSMono` — valores calculados sobre a quantidade tributável.
- `vIBSMonoReten` **e** `vCBSMonoReten` — valores calculados em cenários de retenção atual.
- `vIBSMonoRet` **e** `vCBSMonoRet` — valores calculados em cenários de retenção anterior.

O sistema também calcula o diferimento e totaliza por item. Os totais consolidados do IBS e CBS monofásicos são exibidos no rodapé da nota.

---

## Cálculos

Entenda como são feitas as composições dos cálculos dos impostos da Reforma Tributária.

### Composição da base de cálculo

```
qBCMono = qTrib
qBCMonoReten = qTrib
qBCMonoRet = qTrib
qTrib = qCom convertido na unidade de tributação
```

### Diferimento

Com base no tipo de alíquota aplicada (geral, retenção atual ou anterior), aplica-se o percentual de diferimento:

**Alíquota geral:**

```
vIBSMonoDif = (qBCMono * adRemIBS) * pDifIBS
vCBSMonoDif = (qBCMono * adRemCBS) * pDifCBS
```

**Retenção atual:**

```
vIBSMonoDif = (qBCMonoReten * adRemIBSReten) * pDifIBS
vCBSMonoDif = (qBCMonoReten * adRemCBSReten) * pDifCBS
```

**Retenção anterior:**

```
vIBSMonoDif = (qBCMonoRet * adRemIBSRet) * pDifIBS
vCBSMonoDif = (qBCMonoRet * adRemCBSRet) * pDifCBS
```

### Valor do IBS e CBS Monofásico

Após compor a base e selecionar a alíquota, calcula-se:

**Alíquota geral:**

```
vIBSMono = qBCMono * adRemIBS
vCBSMono = qBCMono * adRemCBS
```

**Retenção atual:**

```
vIBSMonoReten = qBCMonoReten * adRemIBSReten
vCBSMonoReten = qBCMonoReten * adRemCBSReten
```

**Retenção anterior:**

```
vIBSMonoRet = qBCMonoRet * adRemIBSRet
vCBSMonoRet = qBCMonoRet * adRemCBSRet
```

### Totalizadores

```
vTotIBSMono = vIBSMono + vIBSMonoReten - vIBSMonoDif
vTotCBSMono = vCBSMono + vCBSMonoReten - vCBSMonoDif
```

**💡 Dica**

Para saber o que significa cada sigla, acesse o [Glossário de Termos Técnicos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais).

---

## Pontos de atenção

- Atenção às datas de vigência — o cadastro sem data de início é bloqueado pelo sistema.
- Evite cadastros duplicados — o sistema bloqueará o salvamento e exibirá mensagem de erro.
- NCM e NBS não podem ser preenchidos simultaneamente.
- Alíquotas com mais de 4 casas decimais serão bloqueadas ou arredondadas pelo sistema.
- A importação de alíquotas via planilha e o Assistente de Configuração aceitam os campos de Parceiro e Grupo de Parceiro — o preenchimento é opcional. Planilhas anteriores à atualização serão importadas normalmente.

---

## Perguntas frequentes

### Como faço para cadastrar uma nova alíquota?

Acesse **Menu Principal › Fiscal › Impostos › Alíquotas Monofásicas IBS/CBS**, clique em **Cadastrar**, preencha os dados obrigatórios e salve.

### É possível editar uma alíquota já cadastrada?

Sim. Use a pesquisa para localizar a alíquota, clique em **Editar**, faça as alterações necessárias e salve.

### Como excluir uma alíquota?

Localize a alíquota, clique em **Excluir** e confirme a operação na janela de confirmação.

### O que fazer se encontrar um erro na alíquota cadastrada?

Localize a alíquota e utilize a opção **Editar** para corrigir as informações.

### Como garantir que as alíquotas estão atualizadas conforme a legislação?

Mantenha as tabelas de referência sempre atualizadas e revise as alíquotas periodicamente.

### Como o sistema escolhe qual alíquota aplicar se houver várias regras que se encaixam?

O motor de cálculo utiliza uma hierarquia rígida, do mais específico para o mais genérico:

- **1ª prioridade — Produto/Serviço:** regras que especificam o item (NCM/NBS) têm precedência sobre as demais.
- **2ª prioridade — Parceiro:** se não houver regra por produto, o sistema aplica a regra específica do Parceiro (Código ou Grupo IBS/CBS).
- **3ª prioridade — Empresa e Operação:** se não houver regra para produto nem parceiro, o sistema usa a regra geral configurada para a Empresa ou para a Operação.
