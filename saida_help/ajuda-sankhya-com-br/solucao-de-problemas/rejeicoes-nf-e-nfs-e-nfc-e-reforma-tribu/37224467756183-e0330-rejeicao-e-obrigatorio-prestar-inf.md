---
id: "37224467756183"
titulo: "E0330 Rejeição: É obrigatório prestar informações de comércio exterior para as situações de exportação de serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224467756183-E0330-Rejei%C3%A7%C3%A3o-%C3%89-obrigat%C3%B3rio-prestar-informa%C3%A7%C3%B5es-de-com%C3%A9rcio-exterior-para-as-situa%C3%A7%C3%B5es-de-exporta%C3%A7%C3%A3o-de-servi%C3%A7os"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:36Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "CFOP", "Financeiro", "NFS-e", "Identificação de Estrangeiro", "NFS-e de exportação de serviços", "Informações obrigatórias de comércio exterior não foram prestadas", "Prestar informações de comércio exterior", "Comércio exterior", "Exportacao"]
---

# E0330 Rejeição: É obrigatório prestar informações de comércio exterior para as situações de exportação de serviços

**MENSAGEM**

Rejeição E0330: É obrigatório prestar informações de comércio exterior para as situações de exportação de serviços.

**SITUAÇÃO**

Ao emitir uma **NFS-e de exportação de serviços**, o documento foi rejeitado pela Sefaz com a mensagem E0330, indicando que **informações obrigatórias de comércio exterior não foram prestadas** no documento fiscal.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**''Tipos de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP).

**(2)** Localize a natureza de operação utilizada na emissão da NFS-e de exportação.

**(3)** Na aba **"NFS-e"**, verifique se o campo **"Cód. Natureza Oper. ISS (NFS-e)"** está configurado com a opção **"4 - Exportação"**.

**(4)** Certifique-se de que o **parceiro cadastrado** na NFS-e está configurado como **estrangeiro**:

- Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).
- Na aba **“Identificação”**, confirme que o campo **“Identificação de Estrangeiro”** está preenchido corretamente, contendo **mínimo de 5 e máximo de 20 caracteres**.
- Verifique o endereço do parceiro e confirme se a **UF está informada como “EX” (Exterior)**.

**(5)** Confirme se o **CFOP** utilizado na operação é **adequado para exportação de serviços** (geralmente iniciado em **7**).

**(5)** Caso a **prefeitura exija informações adicionais de comércio exterior**, certifique-se de que **todos os campos obrigatórios relacionados à exportação** estejam devidamente preenchidos no documento fiscal.

**(6)** Após realizar os ajustes necessários, **emita novamente a NFS-e** e verifique se o documento foi **aceito pela Sefaz**.

**CAUSA**

A rejeição ocorre quando uma **NFS-e de exportação de serviços** é emitida sem o preenchimento adequado das **informações obrigatórias de comércio exterior**, como a configuração da exigibilidade do ISS como "Exportação", o cadastro correto do parceiro estrangeiro ou a utilização de CFOP inadequado para operações de exportação.
