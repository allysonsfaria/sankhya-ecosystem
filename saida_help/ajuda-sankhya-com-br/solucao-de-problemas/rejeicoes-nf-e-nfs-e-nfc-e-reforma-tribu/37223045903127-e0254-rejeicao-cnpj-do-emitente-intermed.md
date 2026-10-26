---
id: "37223045903127"
titulo: "E0254 Rejeição: CNPJ do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223045903127-E0254-Rejei%C3%A7%C3%A3o-CNPJ-do-emitente-intermedi%C3%A1rio-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CNPJ-e-CNC-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:05Z"
rotulos: ["Configuração", "Cidades", "SEFAZ", "NFS-e", "Erro", "Declaração de Prestação de Serviços (DPS)", "CNPJ do emitente intermediário", "Data de competência", "Emitente intermediário", "CNPJ não possui estabelecimento ou domicílio fiscal cadastrado"]
---

# E0254 Rejeição: CNPJ do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

**MENSAGEM**

E0254 Rejeição: CNPJ do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CNPJ e CNC NFS-e.

**SITUAÇÃO**

Esta rejeição ocorre ao emitir uma **Declaração de Prestação de Serviços (DPS)** informando um **emitente intermediário** cujo CNPJ não possui estabelecimento ou domicílio fiscal cadastrado no mesmo município do emitente principal da DPS, considerando a data de competência informada no documento.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Consulte o cadastro do **CNPJ do emitente intermediário** no site oficial da Receita Federal e verifique:

- A situação cadastral do CNPJ.
- O município de domicílio fiscal informado.
- A existência de filiais e os respectivos municípios de cada estabelecimento.

**(2)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

**(3)** Localize o cadastro do **emitente intermediário** utilizado na DPS.

**(4)** Na aba **“Geral”**, no campo **“CNPJ/CPF”**, confirme se o CNPJ informado está correto e corresponde a um estabelecimento situado **no mesmo município do emitente principal da NFS-e**.

**(5)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(6)** Verifique o cadastro do município vinculado ao endereço do emitente intermediário:

- Confirme se a cidade selecionada está correta.
- Verifique o campo **“Mun. Domicílio Fiscal”** e valide se o código do município está conforme a tabela oficial do IBGE.
- Caso necessário, consulte o código correto no site do **IBGE** e realize o ajuste.

**(7)** Caso o emitente intermediário **não possua estabelecimento no mesmo município** do emitente principal:

- Utilize o **CNPJ de uma filial** localizada no município correto.
- Remova a informação do emitente intermediário da DPS, caso essa informação não seja obrigatória para a operação.

**(8)** Após realizar os ajustes necessários, **redigite o cabeçalho da DPS**, gere um novo lote e realize novamente a transmissão do documento fiscal.

**CAUSA**

A rejeição ocorre quando o **CNPJ do emitente intermediário** informado na DPS não possui estabelecimento ou domicílio fiscal cadastrado no mesmo município do emitente principal do documento, conforme validação realizada pela SEFAZ nos cadastros oficiais (CNPJ e CNC NFS-e), considerando a **data de competência** informada na declaração.
