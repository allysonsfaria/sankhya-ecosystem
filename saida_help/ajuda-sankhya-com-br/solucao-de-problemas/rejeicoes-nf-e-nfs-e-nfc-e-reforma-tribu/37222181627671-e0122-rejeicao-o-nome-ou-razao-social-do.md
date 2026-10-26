---
id: "37222181627671"
titulo: "E0122 Rejeição: O nome ou razão social do prestador deve ser informado quando o emitente da DPS não for o próprio prestador."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222181627671-E0122-Rejei%C3%A7%C3%A3o-O-nome-ou-raz%C3%A3o-social-do-prestador-deve-ser-informado-quando-o-emitente-da-DPS-n%C3%A3o-for-o-pr%C3%B3prio-prestador"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:02Z"
rotulos: ["Configuração", "Central de Vendas", "SEFAZ", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "DPS (Documento de Prestação de Serviços)", "Emitente do documento", "Próprio prestador do serviço", "Nome ou razão social", "DPS é emitida por um intermediário"]
---

# E0122 Rejeição: O nome ou razão social do prestador deve ser informado quando o emitente da DPS não for o próprio prestador.

**MENSAGEM**

E0122 Rejeição: O nome ou razão social do prestador deve ser informado quando o emitente da DPS não for o próprio prestador.

**SITUAÇÃO**

Mensagem apresentada ao emitir uma **DPS (Documento de Prestação de Serviços)** em que o **emitente do documento não é o próprio prestador do serviço**, mas as informações do prestador real não foram devidamente preenchidas no sistema.

**SOLUÇÃO**

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Identifique se o **emitente da DPS é diferente do prestador do serviço**.

- Caso seja, prossiga para o próximo passo.

**(3)** Na grade **''Cabeçalho''**, verifique o campo **''Empresa''**.

**(4)** Preencha obrigatoriamente o campo **"Nome ou Razão Social do Prestador"** com os dados corretos do prestador real do serviço.

**(5)** Verifique se os demais dados do prestador, como **CNPJ/CPF** e **endereço**, também estão preenchidos corretamente.

**(6)** Salve as alterações e tente emitir novamente a DPS.

**CAUSA**

A rejeição ocorre quando uma **DPS é emitida por um intermediário** (emitente diferente do prestador) e o sistema **não identifica o nome ou razão social do prestador real do serviço** no documento fiscal. Conforme as regras de validação da Sefaz, quando o **emitente não é o próprio prestador**, é obrigatório informar os dados completos do prestador, incluindo o **nome ou razão social**, para garantir a correta identificação dos responsáveis pela prestação do serviço e pela tributação aplicável.
