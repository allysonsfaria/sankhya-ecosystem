---
id: "36451519189015"
titulo: "1008 Rejeição:  As alíquotas de IBS e CBS são obrigatórias para operações com entes governamentais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36451519189015-1008-Rejei%C3%A7%C3%A3o-As-al%C3%ADquotas-de-IBS-e-CBS-s%C3%A3o-obrigat%C3%B3rias-para-opera%C3%A7%C3%B5es-com-entes-governamentais"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:22:57Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "XML", "Impostos", "Rejeição 1008", "para operações com entes governamentais", "As alíquotas de IBS e CBS são obrigatórias para operações com entes governamentais", "Squad Docs", "1008 Rejeição", "As alíquotas de IBS e CBS são obrigatórias", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# 1008 Rejeição:  As alíquotas de IBS e CBS são obrigatórias para operações com entes governamentais

**MENSAGEM**

1008 Rejeição:  As alíquotas de IBS e CBS são obrigatórias para operações com entes governamentais

**SITUAÇÃO**

Esta validação ocorre durante a **emissão de documentos fiscais** para entes governamentais (União, Estado, Distrito Federal ou Município) quando o sistema identifica que as **alíquotas de IBS e CBS** não estão configuradas corretamente ou estão ausentes no cadastro.

**SOLUÇÃO**

#### **(1)**Verificação do Cadastro de Alíquotas

**(1)** Acesse o **cadastro de alíquotas** e verifique se as alíquotas aplicáveis estão definidas para o respectivo ano: • **IBS da UF** (pIBSUF): 0,1% para 2025 e 2026, 0,05% para 2027 e 2028 • **IBS do Município** (pIBSMun): 0% para 2025 e 2026, 0,05% para 2027 e 2028 • **CBS** (pCBS): 0,9% para 2025 e 2026

**(2)** Acesse a tela **"Parceiros"** (Menu Principal Cadastros Parceiro).

**(3)** Na **Aba Fiscal**, dentro da seção **"Reforma Tributária"**, marque a opção **"Órgão Público"** como **"SIM"**.

**(4)** Preencha o campo **"Tipo de Ente Governamental"** selecionando entre União, Estado, Distrito Federal ou Município.

**(5)** Acesse a tela **"Tipos de Operação - TOP"** (Menu Principal Tipo de Operação TOP).

**(6)** Na **Aba NF-e/NFC-e/CF-e**, preencha o campo **"Tipo de operação com o ente governamental"** com: • 1 – Fornecimento • 2 – Recebimento do pagamento

**CAUSA**

A validação ocorre porque o sistema identificou uma **operação com ente governamental** mas as **alíquotas de IBS e CBS** não estão cadastradas ou configuradas corretamente. A regra 1008 exige que essas alíquotas estejam presentes no XML para operações que geram o grupo **gCompraGov**, garantindo conformidade com a legislação da Reforma Tributária.
