---
id: "37223192434199"
titulo: "E0272 Rejeição: CPF do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223192434199-E0272-Rejei%C3%A7%C3%A3o-CPF-do-emitente-intermedi%C3%A1rio-n%C3%A3o-possui-estabelecimento-ou-domic%C3%ADlio-em-um-munic%C3%ADpio-correspondente-ao-munic%C3%ADpio-emissor-na-data-de-compet%C3%AAncia-informada-na-DPS-conforme-cadastros-CPF-e-CNC-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:59Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "SEFAZ", "NFS-e", "Erro", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "CPF do emitente intermediário", "Cadastros CPF e CNC (Cadastro Nacional de Contribuintes)", "Estabelecimento ou domicílio fiscal no mesmo município do emissor", "Data de competência informada na DPS"]
---

# E0272 Rejeição: CPF do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e.

**MENSAGEM**

E0272 Rejeição: CPF do emitente intermediário não possui estabelecimento ou domicílio em um município correspondente ao município emissor, na data de competência informada na DPS, conforme cadastros CPF e CNC NFS-e.

**SITUAÇÃO**

Durante a emissão de uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** com intermediário, o documento fiscal é rejeitado na transmissão quando as informações do intermediário indicam que ele não possui estabelecimento ou domicílio fiscal no mesmo município do emissor, considerando a data de competência informada na DPS.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Consulte o **cadastro do CPF do intermediário** nos sistemas oficiais da Receita Federal para verificar qual é o **município de domicílio fiscal** registrado na data de competência da nota.

**(2)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros).

**(3)** Localize o cadastro do intermediário envolvido na emissão da NFS-e.

**(4)** Na aba **“Endereço”**, verifique o campo **“Cód. Cidade”** do cadastro do intermediário e confirme se ele está vinculado corretamente ao município de domicílio fiscal validado no passo 1.

**(5)** Acesse a tela [**''Cidades''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(6)** Localize a cidade identificada no cadastro do intermediário.

**(7)** Na aba **"Geral"**, verifique o campo **"Mun. Domicílio Fiscal"** e confirme se o código está correto.

- Se necessário, consulte o código oficial do município no site do [**''IBGE''**](https://cidades.ibge.gov.br/)**.**

**(8)** Corrija o campo **"Mun. Domicílio Fiscal"** com o código correto do município, caso esteja divergente.

**(9)** Certifique-se de que o **município do intermediário** corresponde ao **município emissor da NFS-e**, conforme exigido pela validação da SEFAZ.

**(10)** Após realizar os ajustes necessários, reemita a **NFS-e** para o destinatário.

**CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do emitente intermediário** informado na NFS-e não possui estabelecimento ou domicílio fiscal cadastrado no mesmo município do emissor da nota, na data de competência informada na DPS. Essa validação é realizada com base nos **cadastros CPF e CNC (Cadastro Nacional de Contribuintes)** da NFS-e, garantindo a conformidade fiscal e a correta identificação do intermediário no processo de prestação de serviços.
