---
id: "37225326106775"
titulo: "E0440 Rejeição: O tipo de dedução/redução informado na DPS não é permitida pelo município de incidência do ISSQN, conforme parametrizações do código de serviço do município de incidência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225326106775-E0440-Rejei%C3%A7%C3%A3o-O-tipo-de-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-informado-na-DPS-n%C3%A3o-%C3%A9-permitida-pelo-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-conforme-parametriza%C3%A7%C3%B5es-do-c%C3%B3digo-de-servi%C3%A7o-do-munic%C3%ADpio-de-incid%C3%AAncia"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:02Z"
rotulos: ["Configuração", "Alíquota de ISS", "Prefeituras", "NFS-e", "ISSQN", "Cidade de prestação do serviço", "Município onde ocorre a incidência do ISSQN", "Manual da Prefeitura do município de incidência", "Tipo de dedução ou redução"]
---

# E0440 Rejeição: O tipo de dedução/redução informado na DPS não é permitida pelo município de incidência do ISSQN, conforme parametrizações do código de serviço do município de incidência.

**MENSAGEM**

E0440 Rejeição: O tipo de dedução/redução informado na DPS não é permitida pelo município de incidência do ISSQN, conforme parametrizações do código de serviço do município de incidência.

**SITUAÇÃO**

Ao emitir uma NFS-e, o sistema apresenta a mensagem de rejeição informando que **o tipo de dedução ou redução configurado não é permitido** pelo município onde ocorre a incidência do ISSQN.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o serviço utilizado na NFS-e rejeitada.

**(3)** Na aba **"Alíquotas de ISS"**, verifique as configurações para o município de incidência do ISSQN:

- Verifique o campo **"Cidade"** onde ocorre a incidência do imposto.
- Verifique o campo **"Cód. Tributação ISS"** e certifique-se de que está configurado corretamente conforme as regras do município.
- Verifique o campo **"Perc. de dedução na base do ISS"**.
- Verifique o campo **"Tipo de dedução de base do ISS"**.

**(4)** Consulte o **manual da Prefeitura do município de incidência** para validar quais tipos de dedução/redução são permitidos para o código de serviço utilizado.

**(5)** Caso o município não permita dedução ou redução para o serviço, ajuste as configurações:

- Remova o percentual do campo **"Perc. de dedução na base do ISS"** ou configure-o como zero.
- Ajuste o campo **"Tipo de dedução de base do ISS"** conforme permitido pelo município.

**(6)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(7)** Na aba **"NFS-e"**, verifique o campo **"Cód. Natureza Oper. ISS (NFS-e)"** para garantir que está configurado adequadamente para a operação.

**(8)** Acesse a tela [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

**(9)** Na aba **''Cabeçalho''**, verifique se o campo **''Cidade de Prestação do Serviço''** está preenchido com o município de incidência do ISSQN.

**(10)** Após realizar os ajustes necessários, emita novamente a NFS-e.

**CAUSA**

A rejeição ocorre porque **o tipo de dedução ou redução de base de cálculo do ISS** configurado no sistema **não está de acordo com as parametrizações permitidas** pelo município de incidência do ISSQN para o código de serviço utilizado. Cada município possui regras específicas sobre quais tipos de dedução são aceitos, e quando essas regras são violadas, a nota fiscal é rejeitada pela prefeitura.
