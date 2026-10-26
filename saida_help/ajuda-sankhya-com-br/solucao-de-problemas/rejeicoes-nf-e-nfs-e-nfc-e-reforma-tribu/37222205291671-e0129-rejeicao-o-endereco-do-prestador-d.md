---
id: "37222205291671"
titulo: "E0129 Rejeição: O endereço do prestador deve ser informado na DPS quando o prestador não for o emitente da DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222205291671-E0129-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-do-prestador-deve-ser-informado-na-DPS-quando-o-prestador-n%C3%A3o-for-o-emitente-da-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:59Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "NFS-e", "Erro", "Endereço do prestador", "DPS é emitida e o prestador do serviço não é o próprio emitente", "Intermediação ou terceirização na prestação de serviços", "Endereço completo do prestador", "DPS (Documento de Prestação de Serviços)", "Endereço do prestador não foi preenchido corretamente no sistema"]
---

# E0129 Rejeição: O endereço do prestador deve ser informado na DPS quando o prestador não for o emitente da DPS.

**MENSAGEM**

E0129 Rejeição: O endereço do prestador deve ser informado na DPS quando o prestador não for o emitente da DPS.

**SITUAÇÃO**

Mensagem apresentada ao emitir uma **DPS (Documento de Prestação de Serviços)** em que o **prestador do serviço não é o emitente do documento** e as **informações de endereço do prestador não foram preenchidas** corretamente no sistema.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do prestador** do serviço que será informado na DPS.

**(2)** Na aba **"Identificação"**, verifique se os **dados de endereço** estão preenchidos corretamente:

- **"Logradouro"**
- **"Número"**
- **"Bairro"**
- **"Município"**
- **"UF"**
- **"CEP"**

**(3)** Caso o prestador possua **endereço específico para prestação do serviço:**

- Acesse a aba **"Contatos"** e cadastre o **endereço completo** do local onde o serviço será prestado.

**(4)** Salve as alterações.

**(5)** Retorne ao **lançamento da DPS** e informe corretamente o **prestador do serviço** com os dados de endereço atualizados.

**(6)** Realize novamente a **emissão da DPS**.

**CAUSA**

A rejeição ocorre quando uma **DPS é emitida** e o **prestador do serviço não é o próprio emitente** do documento, mas as **informações obrigatórias de endereço do prestador** (logradouro, número, bairro, município, UF e CEP) **não foram informadas** no cadastro do parceiro ou no documento fiscal. Conforme as **regras de validação da Sefaz** para a DPS, quando há **intermediação ou terceirização** na prestação de serviços, é obrigatório informar o **endereço completo do prestador** para garantir a **rastreabilidade e conformidade fiscal** do documento.
