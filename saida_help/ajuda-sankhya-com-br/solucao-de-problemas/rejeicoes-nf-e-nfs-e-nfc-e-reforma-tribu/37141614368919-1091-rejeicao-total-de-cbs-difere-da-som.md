---
id: "37141614368919"
titulo: "1091 Rejeição: Total de CBS difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37141614368919-1091-Rejei%C3%A7%C3%A3o-Total-de-CBS-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:00Z"
rotulos: ["Configuração", "NF-e", "Impostos", "TOP", "Reforma Tributária", "Artigo atualizado KCS", "Alíquotas de CBS", "CBS (Contribuição sobre Bens e Serviços)", "valor total da CBS", "CBS difere da soma dos itens", "soma dos valores de CBS de cada item da nota", "Docs Eletrônicos - KCS"]
---

# 1091 Rejeição: Total de CBS difere da soma dos itens

1091 - Rejeição: Total de CBS difere da soma dos itens

### SITUAÇÃO

Esta rejeição ocorre ao tentar transmitir ou aprovar uma NF-e ou NFC-e, quando o sistema identifica que o valor total da CBS (Contribuição sobre Bens e Serviços) informado no documento fiscal não corresponde à soma dos valores de CBS calculados nos itens individuais da nota.

### SOLUÇÃO

Para corrigir esta rejeição, siga os procedimentos abaixo, verificando tanto as configurações do TOP quanto os dados da nota:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação - TOP).

**(2)** Localize o **"Tipos de Operação - TOP"** utilizado na nota fiscal rejeitada e abra-o para edição.

**(3)** Na aba **"Impostos"**, na seção **"Reforma Tributária"**, verifique se o campo **"Tem CBS"** está habilitado.

**(4)** Salve as alterações realizadas no **"Tipos de Operação - TOP"**.

**(5)** Se o erro persistir, acesse a **"Central de Vendas"** (Comercial >> Consulta >> Central de Vendas), localize a NF-e e verifique os dados de imposto de cada item (clicando em **"Outras Opções do Item"** > **"Consultar/Alterar Dados de Imposto do Item"**) para validar a base de cálculo e alíquota de CBS.

**(6)** Realize o recálculo dos totais da nota fiscal para garantir a consistência dos valores.

**(7)** Caso a inconsistência persista, inutilize a NF-e rejeitada, exclua o registro e realize um novo lançamento da nota fiscal.

### CAUSA

A rejeição 1091 ocorre devido a uma divergência entre o valor total da CBS declarado no totalizador da nota fiscal e a soma dos valores de CBS calculados nos itens individuais. Esta inconsistência pode ser causada por:

- O cálculo da CBS não estar configurado para ser proporcional aos itens no **"Tipos de Operação - TOP"** utilizado;
- Erro de arredondamento ou truncamento nos cálculos dos impostos;
- Configuração incorreta da alíquota de CBS no cadastro de alíquotas;
- Base de cálculo da CBS incorreta em um ou mais itens da nota;
- Alteração manual indevida nos valores de CBS que não foram refletidas no total do documento.

De acordo com as regras da Reforma Tributária (Lei Complementar 214/2025), os valores de CBS devem ser calculados corretamente para cada item e o total do documento deve corresponder exatamente à soma dos valores de CBS de todos os itens.
