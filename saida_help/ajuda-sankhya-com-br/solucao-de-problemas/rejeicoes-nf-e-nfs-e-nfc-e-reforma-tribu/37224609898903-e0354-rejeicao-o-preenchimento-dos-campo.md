---
id: "37224609898903"
titulo: "E0354 Rejeição: O preenchimento dos campos nDI (Número da Declaração de Importação) ou do nRE (Número do Registro de Exportação) não é permitido quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 1."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224609898903-E0354-Rejei%C3%A7%C3%A3o-O-preenchimento-dos-campos-nDI-N%C3%BAmero-da-Declara%C3%A7%C3%A3o-de-Importa%C3%A7%C3%A3o-ou-do-nRE-N%C3%BAmero-do-Registro-de-Exporta%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitido-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-1"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:28Z"
rotulos: ["NF-e", "Portal de Vendas", "Importação", "SEFAZ", "Passos para resolver", "Erro", "Como Resolver", "Vínculo da Operação à Movimentação Temporária de Bens", "nRE (Número do Registro de Exportação)", "Declaração de Importação ou Registro de Exportação", "nDI (Número da Declaração de Importação)", "Exportacao"]
---

# E0354 Rejeição: O preenchimento dos campos nDI (Número da Declaração de Importação) ou do nRE (Número do Registro de Exportação) não é permitido quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 1.

**MENSAGEM**

E0354 Rejeição: O preenchimento dos campos nDI (Número da Declaração de Importação) ou do nRE (Número do Registro de Exportação) não é permitido quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 1.

**SITUAÇÃO**

Ao tentar processar uma Nota Fiscal Eletrônica (NF-e), o sistema apresenta a rejeição informando que **não é permitido preencher os campos de Declaração de Importação ou Registro de Exportação** quando a operação está vinculada à **movimentação temporária de bens**. O usuário estava emitindo uma nota fiscal com informações de importação ou exportação e, simultaneamente, indicou que a operação se refere a uma **movimentação temporária**, o que gera incompatibilidade nas informações fiscais.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse o **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) ou o **"Portal de Compras"** (Comercial » Consulta » Portal de Compras), conforme o tipo de operação da nota fiscal que apresentou a rejeição.

**(2)** Pesquise e acesse a nota fiscal que está apresentando a rejeição.

**(3)** Verifique se o campo **"Vínculo da Operação à Movimentação Temporária de Bens"** está preenchido com o valor **"1 - Sim"**. Este campo indica que a operação se refere a uma movimentação temporária de mercadorias.

**(4)** Identifique qual informação está incorreta na nota fiscal:

- Se a operação **não é uma movimentação temporária**, altere o campo **"Vínculo da Operação à Movimentação Temporária de Bens"** para **"0 - Não"** ou deixe-o em branco.
- Se a operação **é realmente uma movimentação temporária**, remova as informações de **Declaração de Importação** ou **Registro de Exportação** dos itens da nota fiscal.

**(5)** Para remover as informações de importação ou exportação, acesse os itens da nota e clique em **"Outras Opções"**:

- Selecione **"Declaração de Importação e Adições"** e remova os dados preenchidos no campo **"Número da Declaração de Importação (nDI)"**.
- Ou selecione **"Documentos Relacionados"** e remova as informações do campo **"Número do Registro de Exportação (nRE)"**.

**(6)** Salve as alterações realizadas no cabeçalho e nos itens da nota fiscal.

**(7)** Gere um novo lote da nota fiscal ou busque autorização novamente, conforme o status atual da NF-e.

**CAUSA**

A rejeição ocorre quando a nota fiscal contém **informações de Declaração de Importação (nDI) ou Registro de Exportação (nRE)** e, ao mesmo tempo, o campo **"Vínculo da Operação à Movimentação Temporária de Bens (movTempBens)"** está preenchido com o valor **"1 - Sim"**. Segundo as regras de validação da SEFAZ, **operações de movimentação temporária de bens não podem conter informações de importação ou exportação**, pois são naturezas de operação distintas e incompatíveis entre si. A movimentação temporária refere-se ao envio ou recebimento de mercadorias que retornarão ao remetente, enquanto importação e exportação envolvem operações definitivas de entrada ou saída de mercadorias do país.
