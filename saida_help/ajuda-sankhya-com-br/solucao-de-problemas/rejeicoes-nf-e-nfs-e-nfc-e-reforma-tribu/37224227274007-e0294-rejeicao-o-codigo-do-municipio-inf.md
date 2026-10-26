---
id: "37224227274007"
titulo: "E0294 Rejeição: O código do município informado na DPS para o endereço do intermediário do serviço não existe conforme tabela de município do IBGE."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224227274007-E0294-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:47Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "SEFAZ", "IBGE", "Declaração de Prestação de Serviços (DPS)", "Código válido na tabela oficial de municípios do IBGE", "Validação dos dados relacionados ao endereço do intermediário", "Código do município (cMun)", "Código do município informado na DPS para o endereço do intermediário"]
---

# E0294 Rejeição: O código do município informado na DPS para o endereço do intermediário do serviço não existe conforme tabela de município do IBGE.

**MENSAGEM**

E0294 Rejeição: O código do município informado na DPS para o endereço do intermediário do serviço não existe conforme tabela de município do IBGE.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)** com intermediário do serviço informado, a nota é rejeitada durante a **validação dos dados relacionados ao endereço do intermediário**, especificamente no município informado.

**SOLUÇÃO**

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(2)** Localize o parceiro intermediário vinculado á DPS rejeitada.

**(3)** Na aba **"Endereços"**, identifique o **"Cód.Cidade"** cadastrado para o intermediário.

**(4)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(5)** Localize a cidade identificada no passo anterior.

**(6)** Verifique o conteúdo do campo **"Mun. domicílio fiscal"** e valide se o código está correto.

**(7)** Acesse o site oficial do [**''IBGE''**](https://cidades.ibge.gov.br/):

- No campo **"Pesquisar"**, digite o nome da cidade do intermediário
- Ao abrir as informações da cidade, localize o **"Código do Município"** oficial

**(8)** Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo "Mun. domicílio fiscal" com o código obtido no site do IBGE.

**(9)** Acesse novamente a tela "Parceiro" (Configurações » Cadastros » Parceiros) e redigite os dados do endereço para que o sistema atualize as informações.

**(8)** Retorne à **DPS rejeitada**, redigite os dados do cabeçalho e gere um novo lote para transmissão.

**(9)** Caso a rejeição persista, inutilize ou exclua a DPS e refaça o lançamento.

**OBSERVAÇÃO:** Caso não consiga localizar o código do município no site do IBGE, solicite auxílio ao seu contador.

**CAUSA**

A rejeição ocorre quando o **código do município (cMun)** do endereço do intermediário do serviço, informado na DPS, está **em branco, incorreto ou não corresponde** a um código válido na tabela oficial de municípios do IBGE. Isso impede que a Secretaria da Fazenda valide corretamente as informações fiscais do documento, resultando na rejeição E0294.
