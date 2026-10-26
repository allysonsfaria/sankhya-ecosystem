---
id: "37222985208599"
titulo: "E0246 Rejeição: O código de país informado para o endereço no exterior do tomador do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do tomador do serv"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222985208599-E0246-Rejei%C3%A7%C3%A3o-O-c%C3%B3digo-de-pa%C3%ADs-informado-para-o-endere%C3%A7o-no-exterior-do-tomador-do-servi%C3%A7o-n%C3%A3o-existe-ou-%C3%A9-igual-ao-c%C3%B3digo-do-Brasil-Informe-um-c%C3%B3digo-de-pa%C3%ADs-existente-e-diferente-do-c%C3%B3digo-do-Brasil-BR-para-o-endere%C3%A7o-no-exterior-do-tomador-do-serv"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:11Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Países", "NFS-e", "Identificação de Estrangeiro", "Código do país informado no cadastro do tomador do serviço", "Código do país informado no cadastro não existe na tabela de países", "Código do Brasil", "Finalização da emissão da nota fiscal de exportação de serviços", "Tabela de país ISO2", "Informar um código de país válido e diferente do Brasil", "NFS-e para um tomador de serviço no exterior"]
---

# E0246 Rejeição: O código de país informado para o endereço no exterior do tomador do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do tomador do serv

**MENSAGEM**

E0246 Rejeição: O código de país informado para o endereço no exterior do tomador do serviço não existe ou é igual ao código do Brasil. Informe um código de país existente e diferente do código do Brasil (BR) para o endereço no exterior do tomador do serviço, conforme tabela de país ISO2.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e para um tomador de serviço localizado no exterior**, o sistema apresenta a rejeição E0246. O erro impede a **finalização da emissão da nota fiscal de exportação de serviços**.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** Busque pelo parâmetro **''CODPAISBRASIL - Código do País Brasil"**.

**(3)** Preencha este parâmetro com o valor **''55''**, representando o código do Brasil.

- A partir da segunda citação, utilize apenas **"CODPAISBRASIL"**.

**(4)** Acesse a tela [**"Países"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044600894-Pa%C3%ADses) (Configurações » Cadastros » Endereços » Países) e cadastre o **país estrangeiro** do tomador do serviço:

- Na aba **''Geral''**, no campo **"País Domicílio Fiscal"**, informe o código do país conforme a **tabela BACEN** (Anexo IX - Tabela de UF, Município e País).
- **Exemplo:** Código do México: 4936.

**(5)** Acesse a tela [**"Estados"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601294-Estados) (Configurações » Cadastros » Endereços » Estados) e cadastre um estado para o exterior com as seguintes características:

- **"Descrição"**: EXTERIOR
- **"País"**: selecione o país cadastrado no passo anterior
- **"Sigla"**: EX
- **"Código IBGE"**: 99

**(6)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e cadastre a cidade do exterior:

- No campo **"Descrição"**, informe o nome da cidade do exterior.
- No campo **"Cód. UF"**, selecione o estado **"EX"** criado no passo anterior.
- No campo **"Município Domicílio Fiscal"**, preencha com **"9999999"** (sete dígitos 9).

**(7)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do tomador do serviço no exterior:

- Na aba **"Endereço"**, no campo **"Cód. Cidade"**, vincule a cidade cadastrada no passo anterior.
- Certifique-se de que o parceiro esteja marcado como **"Pessoa Jurídica"**, pois se marcado como Pessoa Física, poderá ocorrer erro na validação do CPF.
- Na aba **"Identificação"**, preencha o campo **"Identificação de Estrangeiro"** com a informação de identificação fornecida pelo parceiro.

**(8)** Após realizar todos os ajustes nos cadastros, **gere novamente o lote da NFS-e**.

**CAUSA**

A rejeição ocorre quando o **código do país informado no cadastro do tomador do serviço** não existe na tabela de países ISO2, está incorreto ou está configurado com o **código do Brasil**. Para emissão de NFS-e para tomadores no exterior, é obrigatório informar um **código de país válido e diferente do Brasil**, conforme a tabela BACEN e ISO2.
