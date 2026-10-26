---
id: "36159004046743"
titulo: "Geração do Registro A100 – EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36159004046743-Gera%C3%A7%C3%A3o-do-Registro-A100-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:23:30Z"
rotulos: ["Configuração", "Impostos", "TOP", "Financeiro", "NFS-e", "EFD Contribuições", "Registro A100", "SPED Contribuções", "Artigo atualizado KCS", "Fiscal/Contábil - KCS"]
---

# Geração do Registro A100 – EFD Contribuições

Ao gerar o **"SPED Contribuições"**, algumas **"notas fiscais de serviço (NFS-e)"** podem não ser incluídas no **"Registro A100"**, ou aparecer com informações incompletas, bem como divergências gerais de valores apurados ou ausência de notas fiscais no arquivo digital.

### SITUAÇÃO

O **"Registro A100"** é composto por notas de serviços sujeitas a **"PIS"**/**"COFINS"**, e depende de informações provenientes de diversas tabelas, como **"TGFCAB"**, **"TGFLIS"**, **"TGFTOP"**, **"TGFPAR"**, **"TGFNFSE"** e **"TGFDIN"**.

A ausência ou inconsistência nos arquivos do **"SPED"** ocorre, geralmente, por configurações incorretas nos cadastros fiscais do sistema. Essa falha ocorre quando: a **"TOP"** está configurada incorretamente, faltam lançamentos de **"PIS"**/**"COFINS"** na nota (**"TGFDIN"**), o **"Parceiro"** não possui **"CNPJ"**/**"CPF"** válido, a nota não está marcada para atualizar o **"Livro Fiscal"** ou quando a nota já consta na tabela **"TGFLIV"**, evitando duplicidade. Também pode ocorrer quando há duplicidade de ajustes fiscais em operações de transferência, impedindo a gravação das notas no **"Livro Fiscal"** e, consequentemente, sua exportação ao **"EFD Contribuições"**.

### SOLUÇÃO

Para que o sistema gere de forma correta o **"Registro A100"** e o arquivo do **"SPED Contribuições"**, siga os passos abaixo:

### 1. Tipo de Operação (TOP)

Acesse a tela **"Tipo de Operação (TOP)"** (Financeiro >> Arquivos >> Cadastros >> Tipos de Operação - TOP) e configure os campos conforme abaixo:

| Campo | Ação a realizar |
| --- | --- |
| **"Natureza Base de Crédito (NATBCCRED)"** | Defina a natureza de crédito correspondente ao **"PIS"**/**"COFINS"**. |
| **"Atualiza Livro Fiscal (ATUALLIVFIS)"** | Marque como **"Sim"**. |
| **"Complemento / Modelo Doc. (CODMODDOC)"** | Configure para modelo de **"NFS-e"**. |
| **"NFE"** | Marque como **"Sim"** se a nota for eletrônica. |
| **"Natureza EFD-Contribuições (NATEFDCONTM410M810)"** | Informe conforme layout do guia prático. |
| **"Classificação ICMS (CLASSIFICMS)"** | Verifique e ajuste a classificação **"ICMS"** conforme necessidade. |

- A **"TOP"** é o item mais crítico para o **"A100"** — se configurado incorretamente, a nota será ignorada.

### 2. Parceiro (Cliente/Fornecedor)

Acesse a tela **"Parceiro"** (Configurações >> Cadastros >> Parceiros) e verifique se o parceiro envolvido na nota fiscal possui as seguintes informações:

| Campo | Ação a realizar |
| --- | --- |
| **"CNPJ/CPF (CGC\_CPF)"** | Preencha com um **"CNPJ"** ou **"CPF"** válido. |
| **"Razão Social"** | Informe o nome completo do parceiro. |
| **"Classificação ICMS"** | Verifique e ajuste a classificação **"ICMS"**. |

- Parceiros sem **"CNPJ"**/**"CPF"** ou com dados incompletos podem gerar erros de validação no **"PVA"**.

### 3. Empresa (TSIEMP)

Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa) e confirme se a empresa está parametrizada corretamente:

| Campo / Informação | Ação a realizar |
| --- | --- |
| **"Código do município (TSICID)"** | Verifique e corrija se necessário. |
| **"UF e país"** | Confirme que os dados estão corretos. |
| **"Natureza jurídica e regime tributário"** | Informe corretamente conforme parametrização da empresa. |

- Essas informações são usadas para identificar a origem e destino da prestação de serviço.

### 4. Nota Fiscal de Serviço (TGFCAB / TGFLIS / TGFNFSE)

Na tela **"Nota Fiscal de Serviço (TGFCAB / TGFLIS / TGFNFSE)"** (Faturamento >> Movimentações) confirme:

| Campo / Critério | Ação a realizar |
| --- | --- |
| **"TOP de serviço"** | Verifique se a nota está associada a uma **"TOP"** de serviço. |
| **"NUMNFSE"**, **"CODVERIFNFSE"** e **"STATUSNFSE"** | Preencha ou confirme que os campos estão corretos. |
| **"Data de movimento (DTMOV)"** | Confira se está dentro do período de apuração. |

- Notas sem número de **"NFS-e"** ou código de verificação não são exportadas para o **"A100"**.

### 5. Impostos – PIS e COFINS (TGFDIN)

Acesse a tela **"Impostos – PIS e COFINS (TGFDIN)"** (Fiscal >> Detalhamento de Impostos) e confirme que a nota possui os lançamentos corretos de **"PIS"** e **"COFINS"**:

| Campo / Critério | Ação a realizar |
| --- | --- |
| **"Lançamento de PIS (CODIMP=6)"** | Verifique e inclua se não existir. |
| **"Lançamento de COFINS (CODIMP=7)"** | Verifique e inclua se não existir. |
| **"CST"** | Confirme que esteja dentro da faixa 50 a 66. |
| **"Valor e Base de Cálculo"** | Certifique-se de que sejam maiores que zero. |

- Se não houver **"TGFDIN"** vinculado à nota, ela não será considerada no **"Registro A100"**.

### 6. Livro Fiscal (TGFLIS)

Além de verificar a presença da nota em **"TGFLIS"**, siga estas etapas caso identifique divergências na geração do **"SPED"**:

| Critério / Verificação | Ação a realizar |
| --- | --- |
| **"Processamento"** | Caso as notas não estejam presentes no **"Livro Fiscal"**, realize o processamento da geração do **"Livro ICMS/IPI"** para a competência correspondente. |
| **"Erros de ajustes"** | Verifique se ocorrem erros de ajustes fiscais. Se houver duplicidade (comum em transferências), exclua as notas conflitantes e reprocesse. |
| **"Regeneração"** | Após a correção no **"Livro"**, acesse a tela de **"Geração do EFD Contribuições"** e processe novamente. |

- Garanta que o **"Livro Fiscal"** esteja processado sem erros para que o **"SPED"** consiga ler as informações corretamente.
