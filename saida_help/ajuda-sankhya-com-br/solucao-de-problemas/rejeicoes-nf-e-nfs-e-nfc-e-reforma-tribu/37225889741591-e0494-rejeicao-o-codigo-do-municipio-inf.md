---
id: "37225889741591"
titulo: "E0494 Rejeição: O código do município informado na DPS para o endereço do fornecedor do serviço não existe conforme tabela de município do IBGE."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225889741591-E0494-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-munic%C3%ADpio-informado-na-DPS-para-o-endere%C3%A7o-do-fornecedor-do-servi%C3%A7o-n%C3%A3o-existe-conforme-tabela-de-munic%C3%ADpio-do-IBGE"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:30Z"
rotulos: ["Configuração", "Cidades", "Mun. domicílio fiscal", "SEFAZ", "IBGE", "Erro", "Declaração de Prestação de Serviços (DPS)", "código do município informado na DPS", "Rejeitada devido a inconsistência no código do município cadastrado", "código do município", "Tabela de Municípios do IBGE"]
---

# E0494 Rejeição: O código do município informado na DPS para o endereço do fornecedor do serviço não existe conforme tabela de município do IBGE.

**MENSAGEM**

E0494 Rejeição: O código do município informado na DPS para o endereço do fornecedor do serviço não existe conforme tabela de município do IBGE.

**SITUAÇÃO**

Ao emitir a Declaração de Prestação de Serviços (DPS), a declaração foi **rejeitada devido a inconsistência no código do município cadastrado** para o endereço do fornecedor.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas).

**(2)** Localize a **empresa emissora** da DPS.

**(3)** Na aba **''Endereço''**, verifique o campo **"Cidade"** e anote qual cidade está cadastrada.

**(4)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(5)** Localize a **cidade identificada** no passo anterior.

**(6)** Na aba **"Geral"**, verifique o conteúdo do campo **"Mun. domicílio fiscal"**.

- Este campo deve conter o **código oficial do município** conforme a Tabela do IBGE.

**(7)** Acesse o site oficial do [**''IBGE''**](https://cidades.ibge.gov.br/)**.**

**(8)** No campo **"Pesquisar"**, digite o **nome da cidade** e localize a informação **"Código do Município"** na página que será aberta.

**(9)** Retorne à tela "Cidades" (Configurações » Cadastros » Endereços) e corrija o campo "Mun. domicílio fiscal" com o **código localizado no site do IBGE**.

**(10)** Retorne à tela "Empresas" (Configurações » Cadastros » Empresas), na aba "Endereço", e **redigite o campo** "Cidade" para que o sistema atualize as informações com o código correto.

**(11)** Realize novamente a **emissão da DPS**.

**OBSERVAÇÃO:** Caso não consiga localizar a informação no site do IBGE, solicite o **código correto do município** ao seu contador.

**CAUSA**

A rejeição ocorre porque o **código do município** informado no campo **"Mun. domicílio fiscal"** do cadastro da cidade está **incorreto, em branco ou divergente** do código oficial estabelecido pela **Tabela de Municípios do IBGE**. Quando a DPS é transmitida, a SEFAZ valida se o código do município do fornecedor corresponde ao código oficial, e caso haja divergência, a declaração é rejeitada.
