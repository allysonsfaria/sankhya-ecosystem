---
id: "36447768512663"
titulo: "1006 Rejeição: NFCe com grupo de compra governamental"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36447768512663-1006-Rejei%C3%A7%C3%A3o-NFCe-com-grupo-de-compra-governamental"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:22:58Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "TOP", "Erro", "NFCe com grupo de compra governamental", "Compra Governamental para documentos do modelo NFC-e", "órgão público", "1006 Rejeição", "Rejeição 1006", "Compra Governamental", "gCompraGov", "gTribCompraGov"]
---

# 1006 Rejeição: NFCe com grupo de compra governamental

**MENSAGEM**

1006 Rejeição: NFCe com grupo de compra governamental

**SITUAÇÃO**

Ao emitir uma nota fiscal o sistema gera uma **NFC-e** (modelo 65) contendo informações do grupo de **"Compra Governamental"**, que são vedadas neste tipo de documento fiscal. O erro acontece durante a emissão da NFC-e quando há configurações incorretas nas telas **"Tipos de Operação - TOP"** (Tipos de Operação » Cadastros » TOP) e/ou **"Parceiros"** (Configurações » Cadastros » Parceiros) que classificam a operação como destinada a ente governamental.

**SOLUÇÃO**

Para resolver essa rejeição, é necessário identificar e desativar as configurações que classificam a operação como Compra Governamental para documentos do modelo NFC-e.

**Opção 1: Ajustar a TOP para NFC-e (Se a nota não for realmente uma compra governamental)**

**(1)** Identifique se a operação realmente envolve um **órgão público**. Se não for uma compra governamental, prossiga com os ajustes abaixo.

**(2)** Acesse a tela **''Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e selecione a nota que apresentou a rejeição.

**(3)** Na grade **''Cabeçalho''**, no campo **''Tipo Operação''** identifique a TOP usada na nota.

**(4)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e localize a TOP utilizada na emissão da NFC-e rejeitada.

**(5)** Na aba **''NF-e/NFC-e/CF-e"**, localize o campo **"Tipo de operação com o ente governamental"**.

**(6)** Certifique-se de que este campo esteja **vazio** ou com uma opção que não ative a geração do grupo de compra governamental na NFC-e.

##### Opção 2: Revisar o Cadastro do Parceiro (Se o parceiro não for um órgão público)

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o parceiro destinatário da NFC-e.

**(2)** Navegue até a aba **"Fiscal"** e localize a seção **"Reforma Tributária"**.

**(3)** No campo **“Órgão Público”**, verifique a configuração:

- Se estiver marcado como **“SIM”** e o parceiro não for um órgão público, altere para **“NÃO”**.

**(4)** Remova a seleção do **"Tipo de Ente Governamental"** caso esteja preenchido incorretamente.

- Vale destacar que esse campo é exibido somente se o campo ''Órgão Público'' estiver habilitado.
- O campo “Tipo de Ente Governamental” está localizado na tela ''Parceiros'' (Configurações » Cadastros » Parceiros), na aba ''Fiscal'', na seção ''Reforma Tributária''.

**(5)** Após realizar os ajustes, **reemita a NFC-e** para que as alterações sejam aplicadas.

**CAUSA**

A rejeição ocorre porque alguma configuração na **"TOP"** ou no **"Cadastro de Parceiros"** está classificando a operação como **"Compra Governamental"**, gerando os grupos **gCompraGov** e **gTribCompraGov** no XML da NFC-e. Estes grupos são permitidos apenas em **NF-e** (modelo 55) destinadas a entes governamentais, sendo vedados na **NFC-e** (modelo 65).
