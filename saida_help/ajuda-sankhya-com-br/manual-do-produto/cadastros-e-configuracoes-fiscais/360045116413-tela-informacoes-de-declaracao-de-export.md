---
id: "360045116413"
titulo: "Tela Informações de Declaração de Exportação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116413-Tela-Informa%C3%A7%C3%B5es-de-Declara%C3%A7%C3%A3o-de-Exporta%C3%A7%C3%A3o"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-21T15:12:24Z"
rotulos: ["AJUDA DO SKW", "manual", "Fiscal", "Livros Fiscais", "EFD", "br.com.sankhya.informacaodeclaracaoexportacao", "Informações de Declaração de Exportação manual", "Informe \"Nro Registro\" se necessário", "Preencha número tipo datas", "Selecione ajuste CFOP e \"Natureza\"", "Documentos Eletrônicos", "Exportacao"]
---

# Tela Informações de Declaração de Exportação

**Módulo:** Livros Fiscais › Avançado

**Caminho de acesso:** Menu Principal › Livros Fiscais › Avançado › Informações de Declaração de Exportação

## O que é e para que serve

Quando uma empresa efetua vendas para fora do país, é necessário emitir documentos específicos para que a exportação ocorra. A **Tela Informações de Declaração de Exportação** registra as informações comerciais, financeiras, cambiais e fiscais da Declaração de Exportação (DE) e do Registro de Exportação (RE) dessa operação. Essas informações alimentam os registros `1100` e `1105` da EFD - Escrituração Fiscal Digital - ICMS/IPI e os registros `85` e `86` do Sintegra, usados pela Receita Federal para o despacho aduaneiro. A tela **não** substitui a emissão da nota fiscal de exportação nem o despacho aduaneiro em si — ela registra as informações complementares da declaração e do registro de exportação vinculadas às notas de venda já emitidas.

Para saber mais sobre os registros gerados a partir desta tela, acesse [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614) (versão Flex) ou [EFD - Fiscal ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/7267044122263-EFD-Fiscal-ICMS-IPI) (versão HTML5), e [Sintegra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607534).

![Painel Principal da tela Informações de Declaração de Exportação, com os campos Nro Declaração, Tipo Declaração, Data…](https://ajuda.sankhya.com.br/hc/article_attachments/4638406960023)

---

## Painel Principal

O Painel Principal, no alto da tela, reúne as informações pertinentes à Declaração de Exportação.

- **Nro Declaração** — a numeração que identifica a declaração realizada.
- **Data Declaração** — o período ao qual a declaração foi composta.
- **Data Averbação** — o período em que ocorreu a concretização da operação.
- **Natureza** — opções: **Direta**, **Indireta**, **Não - antes de 01/07/2005** e **Sim - antes de 01/07/2005**.
- **Código do País de Destino** — o país destinatário da exportação.

#### Tipo Declaração

**O que faz:** define o tipo de declaração de exportação. Opções: **Declaração Única de Exportação (DU-E)**, **Declaração Simplificada** e **Declaração de Exportação**.

**Quando usar:** use **Declaração de Exportação** quando o Registro de Exportação (RE) tiver número próprio, diferente de zero; use **Declaração Única de Exportação (DU-E)** quando a exportação for tratada pela DU-E.

**Como funciona:** com **Declaração de Exportação** selecionada, o campo **Nro Registro** (aba Informações de Registro Exportação) deve ter um valor diferente de zero. Com **Declaração Única de Exportação (DU-E)** selecionada, é necessário preencher o campo **Natureza** na sub-aba Exportação Direta/Indireta; caso contrário, o sistema exibe: "Não foi possível atualizar o registro! É necessário informar o campo NATUREZA da nota para declaração D10, pois possui tipo de declaração única."

**Impacto no sistema:** determina se o Nro Registro e o campo Natureza da nota são exigidos para salvar o registro.

---

## Aba Informações de Registro Exportação

Esta aba reúne os dados do Registro de Exportação (RE). Informe o número do registro e o período em que ele foi realizado.

- **Data Registro** — o período em que o Registro de Exportação foi realizado.

#### Nro Registro

**O que faz:** identifica o número do Registro de Exportação (RE).

**Quando usar:** use um valor diferente de 0 (zero) apenas quando o campo **Tipo Declaração**, no Painel Principal, estiver com a opção **Declaração de Exportação** selecionada. Por padrão, o sistema insere 0 (zero) neste campo.

**Como funciona:** se o Tipo Declaração for **Declaração de Exportação** e o Nro Registro não for informado ou permanecer igual a 0, o sistema exibe: "Se o campo Tipo Declaração for igual a Declaração de Exportação, o Nro Registro deve ser informado e ser diferente de 0."

**Impacto no sistema:** impede a gravação do registro quando a condição não é atendida.

### Sub-aba Informações de Nota Exportação

Nesta sub-aba, dentro de Informações de Registro Exportação, você aponta os documentos que compõem o Registro de Exportação. A grade traz as colunas **Nro Único Nota**, **Data Conhecimento**, **Nro Conhecimento** e **Tipo Conhecimento**.

#### Nro Único Nota

**O que faz:** preenche e busca os documentos vinculados ao Registro de Exportação. Os documentos pesquisados pertencem apenas à modalidade de venda.

**Quando usar:** use para localizar uma ou mais notas de venda a inserir no Registro de Exportação.

**Como funciona:** ao acionar o campo, o sistema exibe o pop-up **Filtro por Notas**, que permite refinar a busca e selecionar um ou vários documentos para inserir no Registro de Exportação.

![Pop-up Filtro por Notas, acionado a partir do campo Nro Único Nota, na sub-aba Informações de Nota Exportação](https://ajuda.sankhya.com.br/hc/article_attachments/4638402978455)

#### Data do Conhecimento

**O que faz:** registra a data do conhecimento vinculado ao documento selecionado.

**Quando usar:** preencha para cada documento selecionado no Registro de Exportação.

**Como funciona:** a Data do Conhecimento pode ser maior que a Data Declaração, desde que não ultrapasse o último dia do mês de referência desta última — por exemplo, se a Data Declaração for 21/09/2021, a Data do Conhecimento não pode ser posterior a 30/09/2021. Com o parâmetro **Validar dt. conhecimento de declaração Exportação?** (`VALDTDECDTCTEXP`) desligado, o sistema permite informar a Data do Conhecimento maior que a Data Declaração sem essa restrição.

**Impacto no sistema:** o parâmetro `VALDTDECDTCTEXP` altera a validação aplicada a este campo.

### Sub-aba Exportação Direta/Indireta

Aninhada dentro de Informações de Nota Exportação, nesta sub-aba você registra a **Natureza** e o **CFOP** associados à nota vinculada — ambos exibidos como campos obrigatórios na tela.

#### Sugestão de Natureza pelo CFOP dos itens

**O que faz:** sugere automaticamente o valor do campo **Natureza**, nesta sub-aba, a partir do CFOP dos itens do documento vinculado.

**Quando usar:** aplica-se sempre que você vincula uma nota na sub-aba Informações de Nota Exportação.

**Como funciona:** se todos os itens da nota têm o mesmo CFOP e esse CFOP não é **7501**, o sistema apresenta o valor desse CFOP no campo **CFOP** e sugere **Direta** no campo Natureza. Se todos os itens têm o mesmo CFOP e esse CFOP é **7501**, o sistema apresenta o valor no campo CFOP e sugere **Indireta** no campo Natureza. Se os itens da nota têm CFOP's diferentes entre si, o sistema exibe: "O documento vinculado possui mais de um CFOP e não foi possível determinar qual a natureza da exportação será adotada."

**Impacto no sistema:** ao gerar o arquivo SPED Fiscal, o registro `1100` é gerado para cada nota com a informação de Natureza (campo 5) conforme definida na sub-aba Exportação Direta/Indireta. Se o campo Natureza não for preenchido ali, o sistema considera o campo Natureza do Painel Principal.
