---
id: "37224330415255"
titulo: "E0304 Rejeição: Informe um código de país existente diferente de Brasil (BR), conforme tabela de país ISO2."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224330415255-E0304-Rejei%C3%A7%C3%A3o-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-diferente-de-Brasil-BR-conforme-tabela-de-pa%C3%ADs-ISO2"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:43Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Identificação de Estrangeiro", "Código de país válido e diferente do Brasil", "Brasil (código 1058)", "Código do país informado está incorreto", "Código do País", "País"]
---

# E0304 Rejeição: Informe um código de país existente diferente de Brasil (BR), conforme tabela de país ISO2.

**MENSAGEM**

E0304 Rejeição: Informe um código de país existente diferente de Brasil (BR), conforme tabela de país ISO2.

**SITUAÇÃO**

Ao emitir uma **NF-e ou NFC-e** para operações com o **exterior**, o sistema rejeitou o documento fiscal porque o **código do país informado** no cadastro do destinatário está **incorreto, inexistente ou configurado como Brasil**, quando deveria ser um código válido de país estrangeiro conforme a **tabela ISO2**.

**SOLUÇÃO**

Para corrigir esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Países"** (Configurações » Cadastros » Endereços » Países) e **verifique se o país do destinatário** está cadastrado corretamente.

- No campo **"País Domicílio Fiscal"**, informe o **código de quatro dígitos** conforme a **Tabela do BACEN** (Anexo IX - Tabela de UF, Município e País).
- Exemplo: Para o México, o código é **4936**; para os Estados Unidos, o código é **2496**.
- Certifique-se de que o código informado **não seja 1058** (Brasil).

**(2)** Acesse a tela **"Estados"** (Configurações » Cadastros » Endereços » Estados) e **crie um estado** para o país do exterior com as seguintes características:

- **"Descrição"**: EXTERIOR
- **"País"**: selecione o país cadastrado no passo anterior
- **"Sigla"**: EX
- **"Código IBGE"**: 99999

**(3)** Acesse a tela **"Cidades"** (Configurações » Cadastros » Endereços » Cidades) e **crie uma cidade** para o endereço do exterior:

- **"Nome"**: informe o nome da cidade do exterior
- **"Cód. UF"**: selecione o estado criado no passo anterior
- **"Mun. domicílio fiscal"**: 9999999

**(4)** Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências) e **configure o parâmetro**:

- **"CODPAISBRASIL - Código do País Brasil"**: informe o valor **55**

**(5)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e **vincule a cidade cadastrada** ao parceiro do exterior:

- Na aba **"Endereço"**, no campo **"Cód. Cidade"**, selecione a cidade criada no passo 3.
- Na aba **"Identificação"**, no campo **"Identificação de Estrangeiro"**, preencha adequadamente conforme orientação do contador.

**(6)** Após realizar todos os ajustes, **gere novamente a NF-e ou NFC-e** e envie para autorização.

**CAUSA**

Esta rejeição ocorre quando o **código do país informado** no cadastro do destinatário da NF-e ou NFC-e está **incorreto, inexistente na tabela de países da Sefaz** ou está configurado como **Brasil (código 1058)** em uma operação que deveria ser com o exterior. A Sefaz exige que, para **operações com destinatários estrangeiros**, seja informado um **código de país válido e diferente do Brasil**, conforme a **tabela ISO2 e a tabela do BACEN**.
