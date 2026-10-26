---
id: "37222543848087"
titulo: "E0174 Rejeição: Quando o prestador da NFS-e é MEI (opSimpNac = 2) o regime especial de tributação deve ser \"Nenhum\" (regEspTrib = 0)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222543848087-E0174-Rejei%C3%A7%C3%A3o-Quando-o-prestador-da-NFS-e-%C3%A9-MEI-opSimpNac-2-o-regime-especial-de-tributa%C3%A7%C3%A3o-deve-ser-Nenhum-regEspTrib-0"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:44Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "Erro", "MEI (Microempreendedor Individual)", "Regime especial de tributação do ISS", "Regime especial de tributação deve ser \"Nenhum\" (código 0)", "Incompatibilidade entre a configuração da empresa como MEI", "MEI"]
---

# E0174 Rejeição: Quando o prestador da NFS-e é MEI (opSimpNac = 2) o regime especial de tributação deve ser "Nenhum" (regEspTrib = 0).

**MENSAGEM**

E0174 Rejeição: Quando o prestador da NFS-e é MEI (opSimpNac = 2) o regime especial de tributação deve ser "Nenhum" (regEspTrib = 0).

**SITUAÇÃO**

Ao emitir uma NFS-e, o documento fiscal é rejeitado pela prefeitura porque a empresa prestadora está enquadrada como **MEI (Microempreendedor Individual)** e apresenta informações de **regime especial de tributação do ISS** incompatíveis com esse enquadramento no momento da transmissão da nota.

**SOLUÇÃO**

Para resolver esta rejeição, ajuste o regime especial de tributação do ISS seguindo os passos abaixo:

**(1)**  Acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

**(2)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **''NFS-e''**, sub-aba **''Geral''**.

**(3)** No campo **"Regime esp. tributação ISS (NFS-e)"**, selecione a opção **"0 - Normal/Nenhum"**.

**(4)** Salve as alterações realizadas.

**(5)** Emita novamente a NFS-e.

**CAUSA**

A rejeição ocorre porque **existe uma incompatibilidade entre a configuração da empresa como MEI** e o regime especial de tributação informado. Quando a empresa é optante pelo Simples Nacional na modalidade MEI, a legislação municipal determina que o **regime especial de tributação deve ser "Nenhum" (código 0)**, pois o MEI já possui um regime tributário específico e simplificado. Ao informar qualquer outro código de regime especial (como 1, 2, 3, 4, 5 ou 6), o sistema da prefeitura identifica a inconsistência e rejeita a NFS-e com a mensagem E0174.
