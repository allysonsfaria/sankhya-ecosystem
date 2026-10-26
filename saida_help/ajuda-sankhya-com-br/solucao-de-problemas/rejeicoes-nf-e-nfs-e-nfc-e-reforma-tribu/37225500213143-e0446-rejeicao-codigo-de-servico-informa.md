---
id: "37225500213143"
titulo: "E0446 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por valor monetário."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225500213143-E0446-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-valor-monet%C3%A1rio"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:55Z"
rotulos: ["Configuração", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "NFS-e (Nota Fiscal de Serviço Eletrônica)", "Base de cálculo do ISSQN por valor monetário", "Código de serviço", "Dedução ou redução na base de cálculo", "Percentual de dedução ou redução"]
---

# E0446 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por valor monetário.

**MENSAGEM**

E0446 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por valor monetário.

**SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)**, o usuário configurou no sistema um **percentual de dedução ou redução na base de cálculo do ISSQN** por valor monetário. Porém, o **código de serviço** informado na DPS (Declaração de Prestação de Serviços) **não permite** esse tipo de dedução conforme as regras estabelecidas pela legislação municipal. Ao tentar transmitir a nota, a Sefaz rejeitou o documento com a mensagem de erro acima.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o **serviço** que está sendo utilizado na NFS-e rejeitada.

**(3)** Na aba **''Impostos''** no campo **"Cód. Trib. Município NFS-e"**, verifique o **''Código de Tributação do Município''** vinculado ao serviço.

- Confirme junto á prefeitura municipal se este código permite dedução ou redução na base de cálculo do ISSQN por valor monetário.

**(4)** Caso o código de serviço **não permita dedução**, remova o percentual informado no campo **"Perc. de dedução na base do ISS"** no cadastro do serviço, deixando-o zerado ou em branco.

**(5)**  Ajuste também o campo **"Tipo de dedução de base do ISS"**, selecionando a opção adequada conforme a legislação municipal, como:

- **07 - Não Tributado**
- **06 - Isento**
- **00 - Tributado**
- **Ou outra opção que não envolva dedução por valor monetário**

**(6)** Salve as alterações realizadas no **cadastro do serviço**.

**(7)** Retorne à **NFS-e rejeitada** e refaça a emissão do documento, garantindo que **nenhum valor de dedução** seja aplicado na base de cálculo do ISSQN.

**(7)** Transmita novamente a **NFS-e** para a Sefaz.

**CAUSA**

A rejeição ocorre porque o **código de serviço** informado na DPS **não está habilitado** pela legislação municipal para permitir **dedução ou redução na base de cálculo do ISSQN por valor monetário**. Cada município possui **regras específicas** sobre quais serviços podem ter deduções aplicadas, e quando o sistema tenta transmitir uma nota com dedução para um código de serviço que não a permite, a **Sefaz rejeita** o documento com o erro E0446.
