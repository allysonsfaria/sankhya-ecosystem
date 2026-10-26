---
id: "37224331380631"
titulo: "E0302 Rejeição: O código do local da prestação do serviço não existe conforme a tabela de municípios IBGE disponibilizada no ANEXO_A-MUNICIPIO_IBGE-PAISES_ISO2-SNNFSe."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224331380631-E0302-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-do-local-da-presta%C3%A7%C3%A3o-do-servi%C3%A7o-n%C3%A3o-existe-conforme-a-tabela-de-munic%C3%ADpios-IBGE-disponibilizada-no-ANEXO-A-MUNICIPIO-IBGE-PAISES-ISO2-SNNFSe"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:44Z"
rotulos: ["Configuração", "Cidades", "Prefeituras", "NFS-e", "IBGE", "Emissão de NFS-e", "Erro", "Local da prestação do serviço", "Código do município informado como local da prestação do serviço", "Código do município informado", "Ausente incorreto ou divergente"]
---

# E0302 Rejeição: O código do local da prestação do serviço não existe conforme a tabela de municípios IBGE disponibilizada no ANEXO_A-MUNICIPIO_IBGE-PAISES_ISO2-SNNFSe.

**MENSAGEM**

E0302 Rejeição: O código do local da prestação do serviço não existe conforme a tabela de municípios IBGE disponibilizada no ANEXO\_A-MUNICIPIO\_IBGE-PAISES\_ISO2-SNNFSe.

**SITUAÇÃO**

Esta rejeição ocorre durante a **emissão de NFS-e** quando o sistema tenta transmitir a nota fiscal de serviço eletrônica para a prefeitura, mas o **código do município informado como local da prestação do serviço** não está de acordo com a tabela oficial de municípios do IBGE ou está preenchido incorretamente no cadastro.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas).

**(2)** Localize a empresa emissora da NFS-e.

**(3)** Na aba **"Endereço"**, verifique qual **cidade** está cadastrada para a empresa.

**(4)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(5)** Localize a cidade identificada no passo anterior.

**(6)** Na aba **"Geral"**, verifique o conteúdo do campo **"Mun. domicílio fiscal"**.

- Este campo deve conter o **código oficial do município conforme a tabela do IBGE**.

**(5)** Acesse o site oficial do [**''IBGE''**](https://cidades.ibge.gov.br/).

- No campo **"Pesquisar"**, digite o nome da cidade.
- Ao abrir o conteúdo referente ao município, localize a informação **"Código do Município"**.

**(6)** Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo **"Mun. domicílio fiscal"** com o código localizado no site do IBGE.

**(7)** Caso a nota já tenha sido gerada, realize o **cancelamento da NFS-e** rejeitada.

**(8)** Gere novamente a NFS-e com as informações corrigidas.

**OBSERVAÇÃO:** Caso não consiga localizar o código do município no site do IBGE, solicite esta informação ao seu contador.

**CAUSA**

Esta rejeição ocorre quando o **código do município informado no campo "Mun. domicílio fiscal"** do cadastro de cidades está **ausente, incorreto ou divergente** da tabela oficial de municípios do IBGE. A prefeitura valida este código durante a transmissão da NFS-e e, caso não esteja conforme o padrão estabelecido no ANEXO\_A-MUNICIPIO\_IBGE-PAISES\_ISO2-SNNFSe, a nota é rejeitada.
