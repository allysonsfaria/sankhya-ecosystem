---
id: "37222903724695"
titulo: "E0237 Rejeição: O endereço nacional do tomador do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo tomador, exceto se o emitente da DPS é o próprio tomador do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222903724695-E0237-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-tomador-do-servi%C3%A7o-deve-ser-informado-na-DPS-quando-o-valor-do-ISSQN-for-retido-pelo-tomador-exceto-se-o-emitente-da-DPS-%C3%A9-o-pr%C3%B3prio-tomador-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:14Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Impostos", "NFS-e", "Correção de Erro", "Passos para resolver", "Tipo de Retenção do ISS", "Retenção de ISSQN pelo tomador", "Retido pelo tomador", "Cadastro do tomador do serviço", "Não retido", "NFS-e (Documento de Prestação de Serviços)"]
---

# E0237 Rejeição: O endereço nacional do tomador do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo tomador, exceto se o emitente da DPS é o próprio tomador do serviço.

**MENSAGEM**

E0237 Rejeição: O endereço nacional do tomador do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo tomador, exceto se o emitente da DPS é o próprio tomador do serviço.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Documento de Prestação de Serviços)** com **retenção de ISSQN pelo tomador**, o sistema apresenta a rejeição E0237 porque **o endereço completo do tomador do serviço não foi informado** corretamente no cadastro ou na nota fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do tomador do serviço** que está sendo utilizado na NFS-e.

**(2)** Na aba **''Endereço''**, verifique se os **dados de endereço do tomador** estão completos e corretos, incluindo:

- **Logradouro**
- **Número**
- **Bairro**
- **Cidade**
- **UF (Estado)**
- **CEP**

**(3)** Caso algum campo esteja **vazio ou incorreto**, preencha ou corrija as informações e salve o cadastro.

**(4)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(5)** Na grade **''Rodapé''**, na aba **''Impostos''**, verifique se o campo **"Cidade"** está preenchido corretamente com a **cidade onde ocorreu a prestação do serviço**.

**(6)** Confirme se o campo **"Tipo de Retenção do ISS"** está configurado corretamente:

- Se o tomador **retém o ISS**, o campo deve estar marcado como **"Retido pelo tomador''**.
- Se o tomador **não retém o ISS**, altere para **"Não retido''**.

**(7)** Após realizar os ajustes necessários, **emita novamente a NFS-e**.

**CAUSA**

A rejeição ocorre porque a **SEFAZ exige que o endereço completo do tomador do serviço seja informado** quando há **retenção de ISSQN pelo tomador**. Esta validação garante a **identificação correta do responsável tributário** e a **localização da prestação do serviço** para fins de arrecadação municipal. A exceção ocorre apenas quando **o emitente da DPS é o próprio tomador do serviço**, situação em que o endereço já está implícito no cadastro do emitente.
