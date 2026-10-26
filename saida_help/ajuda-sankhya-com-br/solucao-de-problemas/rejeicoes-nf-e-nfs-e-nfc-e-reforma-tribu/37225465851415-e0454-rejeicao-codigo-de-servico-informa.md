---
id: "37225465851415"
titulo: "E0454 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por percentual."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225465851415-E0454-Rejei%C3%A7%C3%A3o-C%C3%B3digo-de-servi%C3%A7o-informado-na-DPS-n%C3%A3o-permite-dedu%C3%A7%C3%A3o-redu%C3%A7%C3%A3o-na-base-de-c%C3%A1lculo-do-ISSQN-por-percentual"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:58Z"
rotulos: ["Configuração", "Alíquota de ISS", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "Prefeitura do Município", "Percentual de dedução ou redução na base de cálculo"]
---

# E0454 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por percentual.

**MENSAGEM**

E0454 Rejeição: Código de serviço informado na DPS não permite dedução/redução na base de cálculo do ISSQN por percentual.

**SITUAÇÃO**

Ao emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o sistema retornou uma rejeição relacionada ao **percentual de dedução ou redução da base de cálculo do ISSQN** informado no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize a **alíquota de ISS** vinculada ao serviço que está sendo utilizado na nota fiscal rejeitada.

**(3)** Na aba **''Alíquota de ISS''** verifique se o campo **"Perc. de dedução na base do ISS"** está preenchido com algum valor percentual.

**(4)** Consulte junto à **prefeitura do município** ou ao seu **contador** se o código de serviço utilizado permite dedução ou redução na base de cálculo do ISSQN:

- Se o código de serviço **não permitir dedução**, remova o percentual informado no campo **"Perc. de dedução na base do ISS"**, deixando-o zerado ou em branco.
- Se o código de serviço **permitir dedução**, mas a rejeição persistir, verifique se o **"Tipo de dedução de base do ISS"** está configurado corretamente conforme a legislação municipal.

**(5)** Caso necessário, ajuste também o campo **"Cód. Tributação ISS"**, selecionando a opção adequada:

- 00 - Tributado
- 01 - Tributado com ISS Retido
- 06 - Isento
- 07 - Não Tributado

**(6)** Salve as alterações realizadas no cadastro.

**(7)** Acesse a tela ''**Central de Compras''** (Comercial » Rotinas » Central de Compras) e/ou **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(9)** Emita novamente a **Nota Fiscal de Serviço Eletrônica (NFS-e)**.

**CAUSA**

A rejeição ocorre porque foi informado um **percentual de dedução ou redução na base de cálculo do ISSQN** no cadastro de alíquotas, porém o **código de serviço** utilizado na nota fiscal **não está autorizado pela legislação municipal** a ter este tipo de dedução. Cada município possui regras específicas sobre quais serviços permitem dedução na base de cálculo, e a **Sefaz valida** se o código de serviço informado está compatível com a dedução aplicada.
