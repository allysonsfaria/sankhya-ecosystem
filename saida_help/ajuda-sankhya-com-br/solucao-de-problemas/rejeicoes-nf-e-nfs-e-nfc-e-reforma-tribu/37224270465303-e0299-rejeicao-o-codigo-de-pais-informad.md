---
id: "37224270465303"
titulo: "E0299 Rejeição: O código de país informado para o endereço no exterior do intermediário do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do intermedi"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224270465303-E0299-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-pa%C3%ADs-informado-para-o-endere%C3%A7o-no-exterior-do-intermedi%C3%A1rio-do-servi%C3%A7o-n%C3%A3o-existe-ou-%C3%A9-igual-ao-c%C3%B3digo-do-Brasil-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-e-diferente-do-c%C3%B3digo-do-Brasil-BR-para-o-endere%C3%A7o-no-exterior-do-intermedi"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-09-30T19:24:02Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Países", "CODPAISBRASIL", "NFS-e", "Erro", "Código do país informado para o intermediário do serviço", "Código do Brasil (1058)", "Tabela ISO2 e BACEN", "Código do País Brasil", "NFS-e com intermediário do serviço no exterior", "Informe um código de país existente e diferente do código do Brasil"]
---

# E0299 Rejeição: O código de país informado para o endereço no exterior do intermediário do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do intermedi

**MENSAGEM**

E0299 Rejeição: O código de país informado para o endereço no exterior do intermediário do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do intermediário do serviço, conforme tabela de país ISO2.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e com intermediário do serviço no exterior**, o sistema apresenta a rejeição E0299. Isso ocorre quando o **código do país cadastrado para o intermediário** está incorreto, inexistente ou configurado como Brasil.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** Localize o parâmetro **“CODPAISBRASIL – Código do País Brasil”** e, no campo **“Inteiro”**, configure o valor **''55''**.

**(3)** Acesse a tela [**“Países”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600894-Pa%C3%ADses) (Configurações » Cadastros » Endereços » Países) e cadastre o país do intermediário do serviço:

- No campo **“País Domicílio Fiscal”**, informe o código conforme a tabela do **BACEN** (Anexo IX – Tabela de UF, Município e País);
- Preencha o campo **“Código do país”** com o código correspondente;
- Informe a **“Descrição”** com o nome do país;
- Preencha a **“Abreviatura”** com a sigla do país.

**(4)** Acesse a tela [**“Estados”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados) (Configurações » Cadastros » Endereços » Estados) e cadastre um estado para o exterior:

- **Descrição**: EXTERIOR
- **País**: vincule o país cadastrado no passo anterior
- **Sigla**: EX
- **Código IBGE**: 99

**(5)** Acesse a tela [**“Cidades”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e cadastre a cidade do intermediário:

- **Descrição**: informe o nome da cidade no exterior;
- **Cód. UF**: vincule o estado **EXTERIOR**;
- **Mun. domicílio fiscal**: informe **9999999** (sete dígitos 9).

**(6)** Acesse a tela **“Parceiros” (**Configurações » Cadastros » Parceiros) e configure o cadastro do intermediário:

- Na aba **“Endereço”**, no campo **“Cód. Cidade”**, selecione a cidade cadastrada no passo anterior;
- Marque o parceiro como **“Pessoa Jurídica”**, evitando erros de validação de CPF;
- Na aba **“Identificação”**, preencha o campo **“Identificação de Estrangeiro”** conforme informado pelo intermediário.

**(7)** Após concluir todas as configurações, gere novamente a **NFS-e**, informando corretamente o intermediário do serviço no exterior.

**CAUSA**

A rejeição ocorre quando o **código do país informado para o intermediário do serviço** no exterior não existe na tabela de países ou está configurado com o **código do Brasil (1058)**. O sistema valida se o código do país está de acordo com a **tabela ISO2 e BACEN**, e se é diferente do código brasileiro. Sem a configuração adequada dos cadastros de **país, estado e cidade do exterior**, a NFS-e não pode ser emitida corretamente.
