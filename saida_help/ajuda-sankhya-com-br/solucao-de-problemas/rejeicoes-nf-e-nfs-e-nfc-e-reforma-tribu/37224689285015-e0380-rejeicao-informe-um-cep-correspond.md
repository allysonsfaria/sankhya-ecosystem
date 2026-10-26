---
id: "37224689285015"
titulo: "E0380 Rejeição: Informe um CEP correspondente ao município do local da prestação do serviço informado nesta DPS para indicar corretamente o endereço da obra."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224689285015-E0380-Rejei%C3%A7%C3%A3o-Informe-um-CEP-correspondente-ao-munic%C3%ADpio-do-local-da-presta%C3%A7%C3%A3o-do-servi%C3%A7o-informado-nesta-DPS-para-indicar-corretamente-o-endere%C3%A7o-da-obra"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:24Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Cidades", "SEFAZ", "Local da prestação do serviço na DPS", "Inconsistência entre o CEP cadastrado", "Município informado", "CEP corresponda exatamente ao município"]
---

# E0380 Rejeição: Informe um CEP correspondente ao município do local da prestação do serviço informado nesta DPS para indicar corretamente o endereço da obra.

**MENSAGEM**

E0380 Rejeição: Informe um CEP correspondente ao município do local da prestação do serviço informado nesta DPS para indicar corretamente o endereço da obra.

**SITUAÇÃO**

Esta rejeição ocorre quando o **CEP informado no endereço da obra** não corresponde ao **município do local da prestação do serviço** registrado na DPS (Declaração de Prestação de Serviços). O sistema identifica uma **divergência entre o município extraído do CEP** e o **município informado como local do fato gerador**, impedindo a autorização do documento fiscal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o parceiro destinatário envolvido na nota fiscal rejeitada.

**(3)** Na aba **"Endereço"**, no campo **''CEP''** verifique o cadastro para o endereço da obra.

**(4)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços).

**(5)** Localize a cidade correspondente ao CEP cadastrado.

**(6)** Confirme se o campo **''Mun. domicílio fiscal"** informado está correto e se **corresponde ao município do local da prestação do serviço**.

**(7)** Caso necessário, consulte o código correto do município no site do IBGE:

- Acesse o site do [**''IBGE''**](https://cidades.ibge.gov.br/)**.**
- No campo **''Pesquisar''**, digite o nome da cidade.
- Localize a informação **"Código do Município"** na página da cidade.

**(8)** Retorne à tela "Cidades" (Configurações » Cadastros » Endereços), e corrija o campo "Mun. domicílio fiscal" com o código obtido no site do IBGE.

**(9)** Retorne à tela "Parceiros" (Configurações » Cadastros » Parceiros), na aba "Endereços", e atualize o **"Cód. Cidade"** para o município correto correspondente ao CEP da obra.

**(10)** Reabra o documento fiscal rejeitado e redigite os dados do cabeçalho.

**(11)** Salve as alterações e gere um novo lote para transmissão.

**(12)** Se a rejeição persistir, inutilize ou exclua a nota fiscal e refaça o lançamento com as informações corrigidas.

**OBSERVAÇÃO:** Caso não seja possível localizar a informação no site do IBGE, recomenda-se solicitar o auxílio do contador responsável para obter o **código correto do município**.

**CAUSA**

A rejeição ocorre quando há **inconsistência entre o CEP cadastrado** no endereço da obra e o **município informado como local da prestação do serviço** na DPS. Isso pode acontecer devido a:

- **CEP incorreto** cadastrado no endereço de entrega do parceiro
- **Código IBGE do município** cadastrado de forma errada na tela **"Cidades"**
- **Cadastros duplicados** da mesma cidade com códigos IBGE distintos
- **Município do local da prestação** divergente do município extraído do CEP informado

A validação da Sefaz exige que o **CEP corresponda exatamente ao município** onde o serviço está sendo prestado, garantindo a **correta identificação do local do fato gerador** para fins de tributação do IBS e CBS.
