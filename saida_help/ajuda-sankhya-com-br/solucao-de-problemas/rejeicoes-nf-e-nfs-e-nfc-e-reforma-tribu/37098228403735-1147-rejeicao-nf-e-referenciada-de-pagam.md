---
id: "37098228403735"
titulo: "1147 Rejeição: NF-e referenciada de pagamento antecipado inexistente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37098228403735-1147-Rejei%C3%A7%C3%A3o-NF-e-referenciada-de-pagamento-antecipado-inexistente"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:20:16Z"
rotulos: ["NF-e", "Central de Vendas", "Portal de Vendas", "SEFAZ", "Erro", "Chave NF-e Referenciada", "NF-e de pagamento antecipado", "NF-e que referencia outra NF-e de pagamento antecipado", "Nota Referenciada", "Documentos Eletrônicos"]
---

# 1147 Rejeição: NF-e referenciada de pagamento antecipado inexistente

**MENSAGEM**

1147 Rejeição: NF-e referenciada de pagamento antecipado inexistente

**SITUAÇÃO**

Ao emitir uma **NF-e** que referencia uma **NF-e de pagamento antecipado**, o sistema retorna rejeição durante a transmissão do documento fiscal eletrônico.

**SOLUÇÃO**

**(1)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas).

**(2)** Consulte o status da nota referenciada.

**(3)** Verifique se a NF-e referenciada está com o status **“Autorizada”**. Caso esteja em **contingência** ou com outro status, aguarde a sua regularização antes de emitir a nova nota.

**(4)** Abra a nota fiscal que apresentou a rejeição. Ao selecioná-la, o sistema redirecionará automaticamente para a tela [''**Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

**(5)** Na aba **“Cabeçalho”**, confira o campo **“Chave NF-e referenciada”** e certifique-se de que a chave de acesso foi informada corretamente.

**(6)** Caso a NF-e referenciada já esteja **autorizada** e a **chave de acesso esteja correta**, gere um **novo lote** da NF-e que está apresentando a rejeição e realize novamente a transmissão.

**CAUSA**

Esta rejeição ocorre quando o sistema tenta validar a existência de uma NF-e referenciada de pagamento antecipado, mas não consegue localizá-la na base de dados da SEFAZ. Isso pode acontecer por três motivos principais:

1. A NF-e referenciada ainda não foi **transmitida** para a SEFAZ;
2. A NF-e referenciada foi transmitida, mas ainda não foi **autorizada** (está em processamento ou foi rejeitada);
3. A **chave de acesso** da NF-e referenciada foi informada incorretamente.

Similar à rejeição 267 (Chave de Acesso referenciada inexistente), esta validação específica verifica se a NF-e referenciada de pagamento antecipado existe e está autorizada na base de dados da SEFAZ antes de permitir que seja referenciada em um novo documento fiscal.
