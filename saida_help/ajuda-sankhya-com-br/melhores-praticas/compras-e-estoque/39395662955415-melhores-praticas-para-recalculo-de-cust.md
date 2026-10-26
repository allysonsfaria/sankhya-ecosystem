---
id: "39395662955415"
titulo: "Melhores práticas para recálculo de custo e gestão de produtos com itens duplicados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39395662955415-Melhores-pr%C3%A1ticas-para-rec%C3%A1lculo-de-custo-e-gest%C3%A3o-de-produtos-com-itens-duplicados"
trilha: "Melhores Práticas > Compras e Estoque"
atualizado_em: "2026-09-14T00:58:22Z"
rotulos: ["Produtos", "Custos", "Configuração", "Análise de Giro", "Estoque", "Artigo criado KCS", "CVE - KCS"]
---

# Melhores práticas para recálculo de custo e gestão de produtos com itens duplicados

O recálculo de custos e a gestão adequada de produtos são processos fundamentais para manter a integridade dos dados no sistema. Registros duplicados de custos podem impedir o processamento correto de funcionalidades como a **"Análise de Giro"** e o **"Recálculo de Custos"**, causando inconsistências que afetam diretamente a operação.

Este artigo apresenta as melhores práticas para identificar e corrigir custos duplicados, além de orientações para executar o recálculo de custos de forma eficiente, evitando a perda de informações de apontamentos de produção.

### Identificação de custos duplicados

Antes de executar processos de recálculo ou consolidação, verifique se existem registros duplicados de custos na base de dados. Custos duplicados geralmente ocorrem quando os parâmetros **CUSTOPORCONT, CUSTOPORLOC ou CUSTOPOREMP** são ligados ou desligados e os custos não são recalculados.

Para identificar produtos com custos duplicados, para uma mesma data e empresa por exemplo, execute a seguinte consulta na tela **"DBExplorer"** (Configurações » Avançado » DBExplorer):

**SELECT CODPROD , CODEMP , DTATUAL, COUNT(1) AS QTD FROM TGFCUS GROUP BY CODPROD , CODEMP , DTATUAL HAVING COUNT(1) > 1 ORDER BY DTATUAL DESC, CODPROD**

Esta consulta retorna todos os produtos que possuem mais de um registro de custo para a mesma data e empresa, permitindo identificar as duplicidades que precisam ser tratadas.

### Recálculo de custos com filtro personalizado

Na tela **"**[**Recálculo de Custos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594214-Processo-Rec%C3%A1lculo-de-Custos)**"** (Comercial » Avançado » Recálculo de Custos), ao executar o recálculo é recomendável utilizar filtros personalizados de produtos para evitar que o sistema apague custos de produtos com apontamentos de produção.

Quando o recálculo é executado sem filtros específicos, o sistema pode zerar os custos de produtos que tiveram apontamento de produção, mesmo que esses custos estejam corretos. Este comportamento não afeta notas fiscais de compra, que continuam atualizando os custos normalmente.

**(1)** Acesse a tela **"Recálculo de Custos"** (Comercial » Avançado » Recálculo de Custos)

**(2)** Configure um filtro personalizado de produto selecionando apenas os produtos que necessitam recálculo. 

**(3)** Na tela **"Recálculo de Custos"** selecione também a empresa, caso necessário. Execute o recálculo aplicando o filtro configurado.

**(4)** Verifique se os custos foram recalculados corretamente e se não houve perda de informações.

### Processamento da Análise de Giro

A **"Análise de Giro"** (Comercial » Rotinas » Análise de Giro) depende de custos consistentes para processar corretamente a matriz. Custos duplicados impedem que o sistema identifique qual registro utilizar, travando o processamento.

**(1)** Antes de processar a matriz, execute a consulta de verificação de custos duplicados.

**(2)** Corrija todas as duplicidades identificadas conforme orientações anteriores.

**(3)** Acesse a tela **"Controle de Jobs"** (Configurações » Avançado » Controle de Jobs) e verifique se há erros registrados na consolidação de descrição 'AgendadorConsolidacaoGiroJob'.

**(4)** Execute novamente o processamento da **"Análise de Giro"** após a correção das duplicidades.

**(5)** Confirme que a data da última consolidação foi atualizada corretamente.

### Prevenção de duplicidades futuras

Para evitar a recorrência de custos duplicados, adote as seguintes práticas preventivas:

**(1)** Ao alterar os parâmetros **CUSTOPORCONT, CUSTOPORLOC** ou **CUSTOPOREMP,** realize o recálculo de custos dos produtos para que o sistema registre corretamente os valores de acordo com a nova configuração.

**(2)** Execute periodicamente a consulta de verificação de custos duplicados para identificar problemas precocemente.

**(3)** Documente todas as alterações em parâmetros relacionados a custos e estoque.

**(4)** Mantenha backups atualizados antes de executar processos de recálculo ou exclusão em massa.

**(5)** Realize testes em ambiente de homologação sempre que houver mudanças significativas nas configurações de custo.

Seguindo estas melhores práticas, você garante a integridade dos dados de custo, evita travamentos em processos críticos e mantém a confiabilidade das informações gerenciais do sistema.
