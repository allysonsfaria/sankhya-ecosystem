---
id: "33876093578775"
titulo: "Tela Cadastro de Alíquotas do IS - Reforma Tributária"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Cadastro de impostos"
atualizado_em: "2026-10-01T13:18:34Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "NCM", "br.com.sankhya.mgeliv.cadastros.AliquotaIs", "Reforma Tributária", "NBS", "Alíquotas de IS"]
---

# Tela Cadastro de Alíquotas do IS - Reforma Tributária

**Módulo:** Fiscal
**Versão mínima:** 4.17.05 (Módulo Livros Fiscais) · 4.33b172, 4.34b225, 4.35b221 (Sankhya W)
**Caminho de acesso:** **Menu Principal › Cadastros › Alíquotas de IS**

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#oque) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#antes) [Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#fluxo) [Como cadastrar uma nova alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#cadastrar)    ↳ [Aba Tributação](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#aba-tributacao) [Como editar uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#editar) | [Como duplicar uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#duplicar) [Visualização dos valores no documento fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#visualizar) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#pontos-atencao) [Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#calculos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#faq) |
| --- | --- |

---

## O que é e para que serve

A tela **Cadastro de Alíquotas do IS** é onde você centraliza a configuração do Imposto Seletivo (IS) no Sankhya OM — criando regras de tributação com base em critérios como operação, localização, CNAE, produto, parceiro envolvido (cliente/fornecedor) ou período de vigência. O sistema de validações automáticas bloqueia erros de preenchimento e o cadastro de alíquotas duplicadas para produtos que podem ser prejudiciais à saúde ou ao meio ambiente. A tela não cobre a configuração de IBS nem de CBS.

![Imagem 1: A tela Cadastro de Alíquotas do IS é onde você centraliza a configuração do Imposto Seletivo (IS) no Sankhya OM —…](https://ajuda.sankhya.com.br/hc/article_attachments/39661703157015)

---

## Antes de começar

- Sistema atualizado para a versão 4.17.05 (Módulo Livros Fiscais).
- Tabela de Tipos de Operação (TOP) fiscal configurada.
- Tabelas oficiais de UF e Municípios atualizadas.
- Tabelas de CNAE, CST, `cClassTrib`, NCM e NBS devidamente cadastradas.

---

## Diagrama de fluxo

O fluxo abaixo representa o processo principal de cadastro e manutenção de alíquotas do Imposto Seletivo:

![Imagem 2: O fluxo abaixo representa o processo principal de cadastro e manutenção de alíquotas do Imposto Seletivo:](https://ajuda.sankhya.com.br/hc/article_attachments/35191061000983)

---

## Como cadastrar uma nova alíquota

1. Acesse **Menu Principal › Cadastros › Alíquotas de IS**.
2. Preencha os campos obrigatórios. Para criar regras gerais, informe **0** nos campos obrigatórios — a alíquota será aplicada a todos os casos não especificados.
3. Selecione **NCM** ou **NBS** — nunca os dois simultaneamente.
4. Preencha a [Aba Tributação](https://ajuda.sankhya.com.br/hc/pt-br/articles/33876093578775-Tela-Cadastro-de-Al%C3%ADquotas-do-IS-Reforma-Tribut%C3%A1ria#aba-tributacao).
5. Defina o intervalo de vigência. A data de início é obrigatória.
6. Clique em **Salvar**. O sistema realizará as seguintes validações automáticas:
   - Verifica duplicidade de dados.
   - Valida UF e Município contra as tabelas oficiais.
   - Garante que apenas NCM ou NBS esteja preenchido.
   - Limita a alíquota a 4 casas decimais.

Se os dados estiverem corretos, o cadastro será confirmado. Caso contrário, uma mensagem indicará o que precisa ser ajustado.

### Aba Tributação

#### Seção Alíquotas

A Lei Complementar prevê que as alíquotas do IS incidentes sobre veículos automotores classificados no Anexo XVII da NCM/SH serão definidas por lei ordinária. Informe os valores conforme a legislação vigente para o tipo de produto ou serviço cadastrado.

#### Seção Vigência

Preencha as datas de início e fim da vigência da alíquota. O preenchimento da data de início é obrigatório — o sistema bloqueará o salvamento caso esteja em branco.

**ℹ️ Nota**

A importação de alíquotas via planilha e o Assistente de Configuração aceitam os campos de Parceiro e Grupo de Parceiro — o preenchimento é opcional. Planilhas anteriores à atualização serão importadas normalmente.

---

## Como editar uma alíquota

Use para corrigir dados, alterar percentuais ou ajustar vigências de alíquotas já cadastradas.

1. Use os **filtros de busca** para localizar rapidamente o cadastro desejado.
2. Selecione a alíquota e clique em **Editar**.
3. Altere os campos necessários e clique em **Salvar**.

---

## Como duplicar uma alíquota

Use para criar variações de alíquotas similares, otimizando o tempo de cadastro quando você tem regras parecidas.

1. Selecione a alíquota que servirá como modelo.
2. Clique em **Duplicar**. O sistema criará uma cópia em modo de edição com um novo ID único.
3. Ajuste os campos desejados e clique em **Salvar**.

---

## Visualização dos valores no documento fiscal

Ao emitir uma nota com itens sujeitos ao Imposto Seletivo, o sistema calcula automaticamente todos os tributos. Basta manter as alíquotas cadastradas corretamente e, ao salvar o documento, o valor final do IS já é exibido no rodapé. No rodapé da nota você pode conferir:

- A base de cálculo total do IS.
- A alíquota aplicada.
- O valor calculado de IS por item.
- O total do Imposto Seletivo da nota.

---

## Pontos de atenção

- NCM e NBS não podem ser preenchidos simultaneamente — o sistema bloqueará o cadastro.
- UF e Município devem ser válidos conforme as tabelas oficiais. Use as listas suspensas para garantir valores corretos.
- Não é possível cadastrar alíquotas duplicadas (mesma combinação de campos).
- A data de início de vigência é obrigatória.
- Alíquotas devem ter até 4 casas decimais — valores superiores são bloqueados ou arredondados pelo sistema.

---

## Cálculos

O cálculo do IS segue as regras definidas pela legislação da Reforma Tributária.

### Composição da Base de Cálculo (`vBC`)

```
vBC = vProd + vServ + vFrete + vSeg + vOutro + vII
      - vDesc - vPis* - vCofins* - vICMS - vICMSUFDest
      - vFCP - vFCPUFDest - vICMSMono - vISSQN
```

- O valor da embalagem é somado em "Outras Despesas".
- O valor de Importação (`vII`) corresponde ao declarado na DI.
- Itens com \* são subtraídos apenas se compuserem o valor do item.

### Seleção da alíquota

A alíquota é encontrada automaticamente pelo **Motor de Seleção**, que avalia critérios como NCM/NBS, tipo de bem, finalidade e vigência.

### Cálculo do valor do IS (`vIS`)

Se `pISEspec` ≠ 0:

```
vIS = qTrib * pISEspec
```

Se `pIS` ≠ 0:

```
vIS = vBC * pIS
```

Se ambos existirem:

```
vIS = (vBC * pIS) + (qTrib * pISEspec)
```

### Registro do imposto

O valor calculado é registrado na tabela de impostos com o tipo **IS**, incluindo:

- O valor do IS.
- O código de classificação tributária (`CodClassTribIS`).
- A estrutura de agrupamento definida na planilha oficial de memória de cálculo.

### Totalização na nota fiscal

No rodapé da nota, o campo **Total do Imposto Seletivo** soma automaticamente os valores de IS de todos os itens. Esse total também é utilizado nos documentos eletrônicos (NF-e, NFS-e etc.), conforme a legislação.

**💡 Dica**

Para saber o que significa cada sigla, acesse o [Glossário de Termos Técnicos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais). Para entender o contexto completo da Reforma Tributária, acesse o [Guia da Reforma Tributária](https://www.sankhya.com.br/guia-reforma-tributaria/#introducao).

---

## Perguntas frequentes

### Posso cadastrar uma alíquota sem informar a empresa?

Sim. Informe **0** no campo **Empresa** para aplicar a regra geral a todas as empresas.

### O que acontece se eu preencher NCM e NBS juntos?

O sistema bloqueia o cadastro e exibe mensagem de erro — apenas um dos campos pode ser preenchido.

### Como garantir que UF e Município são válidos?

Utilize as listas suspensas, que trazem apenas valores oficiais das tabelas do sistema.

### É possível editar ou duplicar um cadastro existente?

Sim. Selecione o cadastro desejado e utilize as opções **Editar** ou **Duplicar**.

### O que significa informar "0" em campos obrigatórios?

Significa que a alíquota será aplicada de forma genérica, abrangendo todos os casos não especificados.

### Como o sistema escolhe qual alíquota de IS aplicar se houver várias regras que se encaixam?

O motor de cálculo utiliza uma hierarquia rígida, do mais específico para o mais genérico:

- **1ª prioridade — Produto/Serviço:** regras que especificam o item (NCM/NBS) têm precedência sobre as demais.
- **2ª prioridade — Parceiro:** se não houver regra por produto, o sistema aplica a regra específica do Parceiro (Código ou Grupo IS).
- **3ª prioridade — Empresa e Operação:** se não houver regra para produto nem parceiro, o sistema usa a regra geral configurada para a Empresa ou para a Operação.
