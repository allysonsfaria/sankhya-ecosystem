---
id: "37224219909015"
titulo: "E0296 Rejeição: O CEP informado para o endereço nacional do intermediário do serviço não existe ou não pertence ao município do endereço do intermediário."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224219909015-E0296-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-existe-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-do-endere%C3%A7o-do-intermedi%C3%A1rio"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:46Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Cidades", "SEFAZ", "Erro", "CEP informado no cadastro do intermediário", "CEP informado não corresponde ao município", "CEP informado para o endereço nacional do intermediário do serviço não existe", "Intermediário do serviço"]
---

# E0296 Rejeição: O CEP informado para o endereço nacional do intermediário do serviço não existe ou não pertence ao município do endereço do intermediário.

**MENSAGEM**

E0296 Rejeição: O CEP informado para o endereço nacional do intermediário do serviço não existe ou não pertence ao município do endereço do intermediário.

**SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com informações de **intermediário do serviço**, o documento foi rejeitado pela SEFAZ porque o **CEP informado no cadastro do intermediário** não existe ou **não pertence ao município** cadastrado para o mesmo intermediário.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o **parceiro intermediário** envolvido na NF-e rejeitada.

**(3)** Na aba **"Endereços"**, verifique nos campos **"CEP"** e **"Cód.Cidade"** as informações cadastradas.

**(4)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(5)** Localize a cidade identificada no passo 3 e verifique o conteúdo do campo **"Mun. domicílio fiscal"**.

**(6)** Acesse o site dos [**''Correios''**](https://buscacepinter.correios.com.br/app/endereco/index.php)**,** e valide se o **CEP informado** realmente pertence ao **município cadastrado**.

**(7)** Caso o CEP esteja incorreto, corrija-o no cadastro do parceiro intermediário na aba **"Endereços".**

**(8)** Caso o município esteja incorreto, acesse o site do [**''IBGE'**](https://cidades.ibge.gov.br/)**'**.

- Pesquise o nome da cidade e localize o **"Código do Município"**.

**(9)** Retorne a tela ''Cidades'' (Configurações » Cadastros » Endereços » Cidades) e corrija o campo **"Mun. domicílio fiscal"** com a informação localizada no site do IBGE.

**(10)** Retorne à nota fiscal rejeitada, redigite os dados do cabeçalho e gere um novo lote para transmissão.

**OBSERVAÇÃO:** Se a rejeição persistir, inutilize ou exclua a respectiva NF-e e refaça o lançamento. Caso não consiga localizar as informações corretas, solicite auxílio ao seu contador.

**CAUSA**

A rejeição ocorre quando o **CEP informado no cadastro do intermediário** do serviço não existe na base de dados dos Correios ou quando o CEP informado **não corresponde ao município** cadastrado para o mesmo intermediário. Esta validação é realizada pela SEFAZ para garantir a **consistência dos dados de endereçamento** nas operações fiscais que envolvem intermediários de serviço.
