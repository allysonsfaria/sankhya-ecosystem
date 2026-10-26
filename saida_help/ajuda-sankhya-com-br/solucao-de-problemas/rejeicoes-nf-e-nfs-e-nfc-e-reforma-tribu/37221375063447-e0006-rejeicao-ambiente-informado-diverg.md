---
id: "37221375063447"
titulo: "E0006 Rejeição: Ambiente informado diverge do ambiente de recebimento para o qual o emitente enviou a DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221375063447-E0006-Rejei%C3%A7%C3%A3o-Ambiente-informado-diverge-do-ambiente-de-recebimento-para-o-qual-o-emitente-enviou-a-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:44Z"
rotulos: ["Configuração", "XML", "SEFAZ", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "DPS (Declaração de Prestação de Serviços)", "Ambiente de Produção", "Ambiente de Homologação", "Divergência entre o ambiente informado no documento fiscal", "Ambiente de recebimento", "Documentos Eletrônicos"]
---

# E0006 Rejeição: Ambiente informado diverge do ambiente de recebimento para o qual o emitente enviou a DPS.

**MENSAGEM**

E0006 Rejeição: Ambiente informado diverge do ambiente de recebimento para o qual o emitente enviou a DPS.

**SITUAÇÃO**

A DPS foi emitida com indicação de ambiente diferente daquele para o qual o documento foi transmitido.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Comercial » Preferências » Empresa).

**(2)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**, confira o campo **''Ambiente''**.

**(3)** Confirme se o ambiente selecionado está correto:

- **Ambiente de Produção:** utilizado para emissão de documentos fiscais com validade jurídica.
- **Ambiente de Homologação:** utilizado apenas para testes, sem validade fiscal.

**(4)** Caso o ambiente esteja **incorreto**, ajuste a configuração para o ambiente adequado e salve as alterações.

**(5)** Certifique-se de que o **certificado digital** utilizado está vinculado ao ambiente correto (produção ou homologação).

**(6)** Após realizar os ajustes, **gere novamente a DPS** e transmita para o ambiente correto.

**(7)** Valide no **XML da DPS** se a tag referente ao ambiente (tpAmb) está preenchida corretamente:

- **tpAmb = 1:** Produção
- **tpAmb = 2:** Homologação

**CAUSA**

A rejeição **E0006** ocorre quando há **divergência entre o ambiente informado** no documento fiscal (campo tpAmb no XML) e o **ambiente de recebimento** para o qual a DPS foi efetivamente transmitida. Isso pode acontecer quando o sistema está configurado para um ambiente, mas o documento é enviado para outro, gerando inconsistência na validação da Sefaz.
