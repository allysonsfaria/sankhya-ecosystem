---
id: "37224606214423"
titulo: "E0356 Rejeição: O preenchimento do campo nRE (Número do Registro de Exportação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 3."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224606214423-E0356-Rejei%C3%A7%C3%A3o-O-preenchimento-do-campo-nRE-N%C3%BAmero-do-Registro-de-Exporta%C3%A7%C3%A3o-%C3%A9-obrigat%C3%B3rio-quando-o-campo-movTempBens-V%C3%ADnculo-da-Opera%C3%A7%C3%A3o-%C3%A0-Movimenta%C3%A7%C3%A3o-Tempor%C3%A1ria-de-Bens-for-igual-a-3"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:27Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "SEFAZ", "CFOP", "Vínculo da Operação à Movimentação Temporária de Bens", "CFOP iniciado em 7000", "Número do Ato Concessório de Drawback", "HABTAGDETEXPORT", "3 - Operação com fim específico de exportação", "Número do Registro de Exportação (nRE)", "Documentos Eletrônicos", "Exportacao"]
---

# E0356 Rejeição: O preenchimento do campo nRE (Número do Registro de Exportação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 3.

**MENSAGEM**

E0356 Rejeição: O preenchimento do campo nRE (Número do Registro de Exportação) é obrigatório quando o campo (movTempBens) Vínculo da Operação à Movimentação Temporária de Bens for igual a 3.

**SITUAÇÃO**

Ao emitir uma NF-e de exportação com **CFOP iniciado em 7000**, o usuário configurou o campo **"Vínculo da Operação à Movimentação Temporária de Bens"** com o valor **"3 - Operação com fim específico de exportação"**, porém **não preencheu o campo "Número do Registro de Exportação" (nRE)** nas informações de exportação do item. Ao tentar gerar o lote da nota, o sistema retorna a rejeição E0356, pois a Sefaz exige que o número do Registro de Exportação seja informado quando a operação está vinculada à movimentação temporária com fim específico de exportação.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse o [**"Portal de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal que apresentou a rejeição.

**(2)** Abra a nota e acesse os **itens** da NF-e.

**(3)** Clique em **"Outras Opções''** (ícone de três pontos), e selecione a opção ''**Documentos relacionados"** para vincular a nota de origem (nota de importação ou entrada) que contém as informações da Declaração de Importação.

**(4)** Pesquise pela **nota de origem** e vincule-a aos itens da nota de exportação.

**(5)** Verifique se o campo **"Número do Registro de Exportação" (nRE)** foi preenchido automaticamente. Caso não tenha sido preenchido, insira manualmente o número do Registro de Exportação correspondente à operação.

**(6)** Certifique-se de que o campo **"Número do Ato Concessório de Drawback"** também esteja preenchido, caso aplicável à operação.

**(7)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(8)** Busque pelo parâmetro **"HABTAGDETEXPORT"** e verifique se ele está habilitado.

- Este parâmetro é necessário para a geração correta do grupo de tags de exportação no XML da NF-e.

**(9)** Salve as alterações.

**(10)** Gere novamente o lote da NF-e ou busque autorização, conforme o status atual da nota. 

**CAUSA**

A rejeição ocorre quando uma NF-e de exportação possui o campo **"Vínculo da Operação à Movimentação Temporária de Bens" (movTempBens)** preenchido com o valor **"3 - Operação com fim específico de exportação"**, mas o campo **"Número do Registro de Exportação" (nRE)** não foi informado. Segundo as regras da Sefaz, quando a operação está vinculada à movimentação temporária com fim específico de exportação, o preenchimento do número do Registro de Exportação é obrigatório para validação do documento fiscal eletrônico.
