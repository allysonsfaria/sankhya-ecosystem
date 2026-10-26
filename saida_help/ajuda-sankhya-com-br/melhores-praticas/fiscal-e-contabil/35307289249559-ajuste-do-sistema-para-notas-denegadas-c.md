---
id: "35307289249559"
titulo: "Ajuste do Sistema para Notas Denegadas conforme a NT 2024.001"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35307289249559-Ajuste-do-Sistema-para-Notas-Denegadas-conforme-a-NT-2024-001"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-08-04T17:44:05Z"
rotulos: ["Configuração", "NF-e", "Atualização", "SEFAZ", "TOP", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "NT 2025.001", "Rejeição 307", "Emitente bloqueado pela UF", "Notas Denegadas", "Squad Docs", "Documentos Eletrônicos"]
---

# Ajuste do Sistema para Notas Denegadas conforme a NT 2024.001

Recentemente a SEFAZ alterou o tratamento de notas denegadas. Com essa mudança, **o sistema não deverá mais gerar NF-e com status de denegadas** nessas situações, pois esse retorno passou a ser subistituido pela **Rejeição 307 - Emitente bloqueado pela UF de destino**, que não cria nota nem consome numeração.

Este help orienta como remover configurações antigas relacionadas ao tratamento de notas denegadas, atualizar a base para a Nota Técnica e corrigir registros que ainda tenham sido marcado como denegados.

**SOLUÇÃO:**

#### Tipo de Operação - TOP

**(1)** Para desfazer a configuração acesse a tela [**''Tipo de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Na aba **''NF-e/NFC-e/CF-e''**, localize as TOPs configuradas como **''Denegada''.**

**(3)** Remova as notas para os tipos de emissão: **Própria, Venda, Compra e Devolução**.

![Imagem 1: (3) Remova as notas para os tipos de emissão: Própria, Venda, Compra e Devolução .](https://ajuda.sankhya.com.br/hc/article_attachments/36639331321751)

#### Preferências

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''** pesquise por **''Denegada''** e/ou **''**`TOPNFEDENEG`**''**.

**(3)** Verifique o campo **''Chave''** e certifique-se de que o campo esteja vazio, sem TOP cadastrada.

![Imagem 2: (3) Verifique o campo ''Chave'' e certifique-se de que o campo esteja vazio, sem TOP cadastrada.](https://ajuda.sankhya.com.br/attachments/token/keji2mhshpkMdd77HuXXvw0I1/?name=image.png)

#### Atualização da Nota Técnica (NT)

Para evitar que o sistema continue rejeitando notas como denegadas, é necessário atualizar para a **NT 2024.001** ou **versões mais recentes disponibilizadas em 2025**.

**Benefícios da atualização:**

- Substitui o tratamento de notas denegadas pela **Rejeição 307 – Emitente bloqueado pela UF de destino**.
- Corrige exceções da regra N12-20.
- Inclui o CFOP 5910 na NFCe (RV 108-150).

Após a atualização, situações que anteriormente resultavam em nota denegada passarão a gerar a **Rejeição 307,** sem criação de nota e sem consumo de numeração. Isso elimina a necessidade de manter notas marcadas como denegadas em sistema.

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(2)** Em **''Configuração''** (ícone da engranagem), no ícone de **''+''**, crie uma nova aba com o nome de **''Documentos Fiscais Eletrônicos''.**

**(3)** Inclua nesta aba os campos relacionados aos documentos fiscais.

**(4)** Em, seguida ative a ''**NT 2024.001''** e demais NTs essenciais para garantir que o sistema acompanhe as últimas regras da SEFAZ.

![Imagem 3: (4) Em, seguida ative a '' NT 2024.001'' e demais NTs essenciais para garantir que o sistema acompanhe as últimas…](https://ajuda.sankhya.com.br/hc/article_attachments/36639331323671)

![Imagem 4: (4) Em, seguida ative a '' NT 2024.001'' e demais NTs essenciais para garantir que o sistema acompanhe as últimas…](https://ajuda.sankhya.com.br/hc/article_attachments/36639331324695)![Imagem 5: (4) Em, seguida ative a '' NT 2024.001'' e demais NTs essenciais para garantir que o sistema acompanhe as últimas…](https://ajuda.sankhya.com.br/hc/article_attachments/36639331325591)

#### Correção de notas já denegadas

##### Notas que já foram registradas como denegadas antes da atualização precisam ser ajustadas diretamente no banco de dados, pois o novo tratamento de SEFAZ não utiliza mais esse status.

**Procedimento:**

**(1)** Altere o status da nota para **“Aguardando Correção”**, permitindo que ela volte ao fluxo normal de tratamento.

**(2)** Verifique no sistema a situação atual da nota, garantindo que ela tenha retornado ao status adequado.

**(3)** Em seguida, ajuste os campos necessários no banco de dados, observando:

- `NUNOTA` → número da nota que será corrigida
- `CODEMP` → código da empresa
- `STATUSNFE` → novo status da nota

A alteração desses campos deve ser realizado **exclusivamente por um DBA**, garantindo a integridade da base e aplicando os ajustes apenas para a nota e empresa desejadas.

#### Resumo

1. Remova as TOPs denegadas configuradas nas TOPs de emissão.
2. Limpe o campo ''`TOPNFEDENEG`'' nas ''Preferências''.
3. Atualize o sistema para a **NT 2024.001** ou versão superior.
4. Crie a aba de ''Documentos Fiscais Eletrônicos'' e ative as NTs necessárias.
5. Corrija notas já denegadas diretamente no banco de dados (somente por DBA).
6. Após a mudança, notas que antes ficariam denegadas passarão a apresentar a **Rejeição 307**.
