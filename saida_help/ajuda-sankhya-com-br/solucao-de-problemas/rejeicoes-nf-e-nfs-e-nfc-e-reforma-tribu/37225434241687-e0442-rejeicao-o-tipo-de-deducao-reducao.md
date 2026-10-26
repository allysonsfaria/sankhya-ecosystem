---
id: "37225434241687"
titulo: "E0442 Rejeição: O tipo de dedução/redução informado na DPS não é permitida para o prestador de serviço ME/EPP, apurando pelo SN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225434241687-E0442-Rejei%C3%A7%C3%A3o-O-tipo-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-%C3%A9-permitida-para-o-prestador-de-servi%C3%A7o-ME-EPP-apurando-pelo-SN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:00Z"
rotulos: ["ISS", "Configuração", "Simples Nacional", "Impostos", "NFS-e", "Empresas optantes pelo Simples Nacional", "ME ou EPP", "Simples Nacional (SN)", "Dedução/redução informado na DPS", "Base de cálculo do ISS", "Microempresa (ME) ou Empresa de Pequeno Porte (EPP)", "ME/EPP"]
---

# E0442 Rejeição: O tipo de dedução/redução informado na DPS não é permitida para o prestador de serviço ME/EPP, apurando pelo SN.

**MENSAGEM**

E0442 Rejeição: O tipo de dedução/redução informado na DPS não é permitida para o prestador de serviço ME/EPP, apurando pelo SN.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, a empresa enquadrada como **Microempresa (ME)** ou **Empresa de Pequeno Porte (EPP)**, optante pelo **Simples Nacional (SN)**, recebeu a rejeição E0442.

**SOLUÇÃO**

Para resolver esta rejeição, ajuste as configurações do serviço e da nota fiscal conforme os passos abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o serviço utilizado na nota fiscal rejeitada.

**(3)** Na aba **''Alíquotas de ISS''**, verifique o campo **"Tipo de dedução de base do ISS"** e certifique-se de que está configurado com uma opção **permitida para empresas ME/EPP optantes pelo Simples Nacional**.

**(4)** Caso o tipo de dedução informado não seja compatível com o regime do Simples Nacional, altere para uma das seguintes opções permitidas:

- 7 - Sem dedução
- 16 - Tributada integralmente
- 26 - Tributada no prestador
- A - Sem Dedução

**(5)** Confirme também que o campo **"Cód. Tributação ISS"** está configurado adequadamente para o regime tributário da empresa.

**(6)** Salve as alterações realizadas no cadastro do serviço.

**(7)** Retorne à nota fiscal rejeitada e realize uma **nova tentativa de emissão** com as configurações corrigidas.

**CAUSA**

A rejeição ocorre porque **empresas optantes pelo Simples Nacional**, enquadradas como **ME ou EPP**, possuem **restrições quanto aos tipos de dedução ou redução de base de cálculo do ISS** que podem ser utilizados na emissão de NFS-e. A legislação municipal e as regras do Simples Nacional **não permitem determinados tipos de dedução** que são aplicáveis a outros regimes tributários. Quando um tipo de dedução incompatível é informado no cadastro do serviço ou na nota fiscal, a prefeitura rejeita o documento com a mensagem E0442, exigindo que seja utilizado apenas um tipo de dedução permitido para este regime específico.
