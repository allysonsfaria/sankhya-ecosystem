---
id: "37222043360663"
titulo: "E0099 Rejeição: CPF do emitente prestador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastro nacional complementar NFS-e (cLocEmi + CPF + IM informados na"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222043360663-E0099-Rejei%C3%A7%C3%A3o-CPF-do-emitente-prestador-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastro-nacional-complementar-NFS-e-cLocEmi-CPF-IM-informados-na"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:11Z"
rotulos: ["Configuração", "Prefeituras", "NFS-e", "Erro", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "DPS (Declaração de Prestação de Serviços)", "Divergência entre os dados cadastrais do prestador", "CPF do prestador informado na DPS não está vinculado ao município emissor", "Cadastro Nacional Complementar NFS-e (CNC NFS-e)", "Código do município está incorreto"]
---

# E0099 Rejeição: CPF do emitente prestador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastro nacional complementar NFS-e (cLocEmi + CPF + IM informados na

**MENSAGEM**

E0099 Rejeição: CPF do emitente prestador não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastro nacional complementar NFS-e (cLocEmi + CPF + IM informados na DPS para o prestador devem existir no CNC NFS-e).

**SITUAÇÃO**

Ao tentar emitir uma **Nota Fiscal de Serviço Eletrônica (NFS-e)**, o sistema retorna a rejeição E0099, indicando que o **CPF do prestador** informado na DPS (Declaração de Prestação de Serviços) não está vinculado ao **município emissor** no Cadastro Nacional Complementar NFS-e (CNC NFS-e) na data de competência informada.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o **cadastro da empresa prestadora** do serviço.

**(2)** Na aba **“Geral”**, verifique se o campo **“CNPJ / CPF”** está corretamente preenchido no cadastro da empresa e se o **CPF informado corresponde ao responsável cadastrado junto à prefeitura**.

**(3)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades) e localize o **município emissor** da NFS-e.

**(4)** Na aba **"Geral"**, verifique se o campo **"Mun. domicílio fiscal"** está preenchido corretamente com o código IBGE do município. Para confirmar o código correto:

- Acesse o site do [**''IBGE''**](https://cidades.ibge.gov.br/)**;**
- Digite o nome da cidade na pesquisa;
- Localize a informação **"Código do Município";**
- Corrija o campo **"Mun. domicílio fiscal"** com o código localizado.

**(5)** Verifique junto à **prefeitura do município emissor** se o CPF do responsável está devidamente cadastrado no **Cadastro Nacional Complementar NFS-e (CNC NFS-e)** para aquele município.

**(6)** Caso o CPF não esteja cadastrado ou esteja vinculado a outro município, será necessário **regularizar o cadastro junto à prefeitura** antes de emitir a NFS-e.

**(7)** Após realizar as correções, acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas), localize a nota rejeitada e tente **transmiti-la novamente**. 

**CAUSA**

A rejeição ocorre quando há **divergência entre os dados cadastrais** do prestador no sistema Sankhya e as informações registradas no **Cadastro Nacional Complementar NFS-e (CNC NFS-e)**. Especificamente, o CPF do responsável pela empresa não está vinculado ao município emissor informado na DPS, ou o **código do município** está incorreto no cadastro de cidades. Esta validação garante que apenas prestadores devidamente cadastrados na prefeitura possam emitir NFS-e para aquele município.
