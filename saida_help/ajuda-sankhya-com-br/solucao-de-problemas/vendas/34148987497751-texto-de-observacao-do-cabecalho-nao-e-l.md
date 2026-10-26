---
id: "34148987497751"
titulo: "Texto de observação do cabeçalho não é levado para a impressão da NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34148987497751-Texto-de-observa%C3%A7%C3%A3o-do-cabe%C3%A7alho-n%C3%A3o-%C3%A9-levado-para-a-impress%C3%A3o-da-NF-e"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:27:29Z"
rotulos: ["Configuração", "Impressão", "NF-e", "XML", "DANFE", "TOP"]
---

# Texto de observação do cabeçalho não é levado para a impressão da NF-e

**SITUAÇÃO**

Ocorre quando, ao emitir uma nota fiscal, as observações inseridas no cabeçalho não aparecem nas informações complementares do DANFE. Isso pode gerar falhas na comunicação de dados adicionais ao cliente e ao Fisco, especialmente quando informações fiscais, complementares ou tributárias não são impressas na nota.

**SOLUÇÃO**

**(1)**  **Verifique a origem das informações.**
As observações complementares do DANFE são geradas na tag **<infAdFisco>** do XML da NF-e. Essa tag é alimentada a partir dos seguintes campos no sistema:

- **"Observação padrão"** no cabeçalho da nota.
- **"Observação"** no cabeçalho da nota.
- Parâmetro **"CODOBSICMSCOMP"** (observações complementares de ICMS).
- **"Observação"** do cadastro de Alíquotas de ICMS.
- **"Observação padrão"** do item da nota (pode vir do cadastro de alíquotas de ICMS ou da nota de origem).

**(2)**  **Cheque os parâmetros do sistema.**

- **"ENVOBSPADNFE"** → Habilita o envio da observação padrão para o DANFE/XML.
  **Observação:** se a observação estiver cadastrada na alíquota de ICMS, este parâmetro precisa estar habilitado.
- **"ENVOBSNFE"** → Habilita o envio da observação do cabeçalho para o DANFE/XML.

Ambos devem estar configurados como **Sim** para garantir que as informações sejam levadas para a nota.

**(3)**  **Analise o modelo de dados adicionais na "TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).
Acesse a configuração da TOP utilizada e verifique se há um **"Modelo para Dados Adicionais de NF-e"** vinculado.
Quando existe um modelo configurado, as cargas médias tributárias e outras observações podem deixar de ser geradas na tag **<infCpl>**.
Nesse caso, ajuste o modelo para buscar essas informações usando a variável correta:

- **&vlrtributos01** → Retorna os dados das cargas médias tributárias para a impressão.

**(4)**  Verifique o modelo de impressão.
Se, mesmo após todos os ajustes, as observações não forem impressas, o modelo de impressão do DANFE pode estar sobrescrevendo as informações complementares. Nesse caso:

- Baixe o modelo padrão da DANFE 4.0 na tela **"Relatórios Formatados"** (Configurações » Avançado » Relatórios Formatados).
- Vincule este modelo à **"TOP"** da nota fiscal.
- Emita uma nova nota de teste para confirmar se as observações são impressas corretamente.

**CAUSA**

O problema ocorre quando as informações que deveriam alimentar a tag **<infAdFisco>** não chegam ao XML da NF-e. Isso pode acontecer por:

- Campos obrigatórios não preenchidos no cabeçalho ou na alíquota de ICMS.
- Parâmetros **ENVOBSPADNFE** ou **ENVOBSNFE** desabilitados.
- Modelo de dados adicionais configurado na **TOP** que não contempla a variável responsável pelas informações complementares.
- Modelo de impressão personalizado que ignora ou substitui as informações da tag **<infAdFisco>**.
