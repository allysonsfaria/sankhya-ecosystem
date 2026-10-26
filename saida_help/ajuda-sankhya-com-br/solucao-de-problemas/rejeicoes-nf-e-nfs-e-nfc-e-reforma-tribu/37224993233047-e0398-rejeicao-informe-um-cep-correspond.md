---
id: "37224993233047"
titulo: "E0398 Rejeição: Informe um CEP correspondente ao município do local da prestação do serviço informado nesta DPS para indicar corretamente o endereço da atividade ou evento."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224993233047-E0398-Rejei%C3%A7%C3%A3o-Informe-um-CEP-correspondente-ao-munic%C3%ADpio-do-local-da-presta%C3%A7%C3%A3o-do-servi%C3%A7o-informado-nesta-DPS-para-indicar-corretamente-o-endere%C3%A7o-da-atividade-ou-evento"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:17Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "SEFAZ", "Erro", "CEP informado no endereço", "Local da prestação do serviço", "CEP que não corresponde ao município indicado", "Consistência entre o endereço completo e o município"]
---

# E0398 Rejeição: Informe um CEP correspondente ao município do local da prestação do serviço informado nesta DPS para indicar corretamente o endereço da atividade ou evento.

**MENSAGEM**

E0398 Rejeição: Informe um CEP correspondente ao município do local da prestação do serviço informado nesta DPS para indicar corretamente o endereço da atividade ou evento.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviço (DPS)**, o usuário informou um **CEP que não corresponde ao município** indicado como **local da prestação do serviço**. Esta divergência entre o CEP e o município causa a rejeição do documento pela Sefaz, pois é necessário que haja **consistência entre o endereço completo e o município** onde o serviço será efetivamente prestado.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o parceiro envolvido na DPS rejeitada.

**(3)** Acesse a aba **"Endereço''** e confirme o tipo de operação da DPS.

**(4)** Confira os dados de localização, validando se o campo **''CEP''** está correto e se o campo **“Cód. Cidade”** corresponde ao município está adequado.

**(5)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(6)** Localize a cidade identificada no passo anterior.

**(7)** Verifique o conteúdo do campo **"Mun. domicílio fiscal"** e confirme se o código IBGE está correto.

**(8)** Acesse o site do [**''IBGE''**](https://cidades.ibge.gov.br/) para validar o código correto:

- No campo **"Pesquisar"**, digite o nome da cidade.
- Ao abrir o conteúdo referente à cidade, localize a informação **"Código do Município"**.

**(9)** Retorne à tela "Cidades" (Configurações » Cadastros » Endereços » Cidades) e corrija o campo "Mun. domicílio fiscal" com a informação localizada no site do IBGE.

**(10)** Retorne ao cadastro do "Parceiros" (Configurações » Cadastros » Parceiros) e atualize o "CEP" para que corresponda ao município correto do local da prestação do serviço.

**(11)** Reabra a DPS rejeitada, redigite os dados necessários e gere um novo lote para transmissão.

**OBSERVAÇÃO:** Caso não seja possível localizar a informação no site do IBGE, recomenda-se solicitar o auxílio do contador responsável pela empresa.

**CAUSA**

A rejeição ocorre porque o **CEP informado no endereço** da DPS **não pertence ao município** indicado como **local da prestação do serviço**. Esta inconsistência pode ser causada por:

- Cadastro incorreto do **CEP** no cadastro do parceiro;
- Código IBGE incorreto no campo **"Mun. domicílio fiscal"** da cidade cadastrada;
- Divergência entre o **endereço de entrega/recebimento** e o **município de prestação do serviço** informado na DPS;
- Duplicidade de cadastros de cidades com códigos IBGE distintos.
