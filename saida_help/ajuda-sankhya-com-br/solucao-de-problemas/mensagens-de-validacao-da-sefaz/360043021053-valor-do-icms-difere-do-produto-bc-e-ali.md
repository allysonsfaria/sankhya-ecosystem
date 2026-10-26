---
id: "360043021053"
titulo: "Valor do ICMS difere do produto BC e Alíquota (NT2010/007)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043021053-Valor-do-ICMS-difere-do-produto-BC-e-Al%C3%ADquota-NT2010-007"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-09-09T14:29:38Z"
rotulos: ["ERRONF", "Configuração", "NF-e", "SEFAZ", "ICMS", "Impostos", "TOP", "528", "Valor do ICMS Divergente da BC e Alíquota (NT2010/007)", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Valor do ICMS difere do produto BC e Alíquota (NT2010/007)

### SITUAÇÃO

Esta rejeição ocorre ao tentar transmitir ou autorizar uma NF-e para a Secretaria da Fazenda (SEFAZ). A mensagem indica que existe uma divergência entre o valor do ICMS calculado e o resultado da multiplicação da Base de Cálculo pela Alíquota do imposto. A SEFAZ considera uma diferença máxima de 0,01 centavos; se a soma das divergências nos itens ultrapassar este valor, a nota é rejeitada.

A situação é mais comum em cenários onde:

- Os itens são **"Desmembrados por lote"** no faturamento do pedido.
- A **"TOP"** (Tipo de Operação) está configurada para **"Agrupar itens no XML"**.
- Há **"Arredondamentos"** nos valores de ICMS de cada item que, somados, geram divergência no total.
- Notas de **"Reforma"** são habilitadas com cálculos incorretos de ICMS.
- Notas com múltiplos produtos onde a soma das diferenças de arredondamento ultrapassa o limite aceitável pela SEFAZ.

### SOLUÇÃO

A correção para esta rejeição já foi aplicada e validada pela equipe de desenvolvimento nas seguintes versões do sistema:

**Sankhya OM:**

- Versão 4.35b481 ou superior.
- Versão 4.34b376 ou superior.

Para resolver o problema, siga os passos abaixo:

**(1)** Verifique a **"Versão atual"** do seu sistema Sankhya e compare com as versões corrigidas listadas acima. Caso sua versão seja inferior, realize a atualização primeiramente na base de testes.

**(2)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP), aba **"Despesas Acessórias"**, e marque a opção **"ICMS, PIS, COFINS e IPI Proporcional ao ICMS dos Itens"** para garantir o rateio correto.

**(3)** Na aba **"NF-e/NFC-e"** da **"TOP"**, marque a opção **"Agrupar produtos semelhantes na NF-e?"**.

**(4)** Se a nota for de ajuste, selecione no campo **"Tipo de Emissão"** a opção **"Ajuste"**.

**(5)** Após realizar as atualizações e configurações, refaça a nota fiscal do zero para que o sistema recalcule os impostos com a nova lógica e tente **"Transmitir novamente"**.

### CAUSA

A rejeição 528 é causada por uma **"Inconsistência no cálculo do ICMS"** devido a divergências no arredondamento ou falhas na composição da base de cálculo (como falta de rateio de despesas acessórias). O problema ocorre quando:

- O sistema realiza **"Arredondamentos individuais"** no valor do ICMS de cada item da nota.
- A **"Soma desses valores arredondados"** não corresponde ao resultado da multiplicação da Base de Cálculo total pela Alíquota.
- A diferença entre o valor calculado e o valor esperado ultrapassa o limite aceitável pela SEFAZ.

A correção implementada ajusta o **"Algoritmo de cálculo e arredondamento"** para garantir compatibilidade com a NT2010/007.

**Observação:** Consulte a nota técnica 2010/007 para mais detalhes sobre as regras de validação da SEFAZ.
