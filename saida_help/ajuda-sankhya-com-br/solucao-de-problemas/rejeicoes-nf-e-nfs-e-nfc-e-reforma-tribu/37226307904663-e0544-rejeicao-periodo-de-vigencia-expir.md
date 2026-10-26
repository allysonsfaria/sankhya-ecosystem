---
id: "37226307904663"
titulo: "E0544 Rejeição: Período de vigência expirado para o código de identificação do Benefício Municipal no município de incidência do ISSQN para a data de competência informada na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226307904663-E0544-Rejei%C3%A7%C3%A3o-Per%C3%ADodo-de-vig%C3%AAncia-expirado-para-o-c%C3%B3digo-de-identifica%C3%A7%C3%A3o-do-Benef%C3%ADcio-Municipal-no-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN-para-a-data-de-compet%C3%AAncia-informada-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:06Z"
rotulos: ["Configuração", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Erro", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Data de competência informada na DPS", "Período de vigência expirado", "Período de vigência expirado para o código de identificação do Benefício Municipal", "Cdigo de identificação do Benefício Municipal no município", "Benefício Municipal no município de incidência do ISSQN", "RPS (Recibo Provisório de Serviços)"]
---

# E0544 Rejeição: Período de vigência expirado para o código de identificação do Benefício Municipal no município de incidência do ISSQN para a data de competência informada na DPS.

**MENSAGEM**

E0544 Rejeição: Período de vigência expirado para o código de identificação do Benefício Municipal no município de incidência do ISSQN para a data de competência informada na DPS.

**SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** ou enviar um **RPS (Recibo Provisório de Serviços)** para conversão, o documento é **rejeitado pela prefeitura** com a mensagem de erro E0544, indicando que o **código do benefício municipal informado está com o período de vigência expirado** para a data de competência utilizada.

**SOLUÇÃO**

**(1)** Verifique junto à **prefeitura do município** qual é o **código de benefício fiscal municipal vigente** para a data de competência da nota fiscal que está sendo emitida.

**(2)** Acesse a tela **"Serviços"** (Configurações » Cadastros » Produtos » Serviço) e localize o **serviço utilizado** na nota fiscal rejeitada.

**(3)** Na aba **''Impostos''**, verifique o campo **"Cód. Trib. Município NFS-e"** e confirme se:

- O código informado está **correto e atualizado** conforme orientação da prefeitura;
- O **período de vigência** do código abrange a **data de competência** da nota fiscal.

**(4)** Caso o código esteja **expirado ou incorreto**, atualize o campo com o código vigente fornecido pela prefeitura.

**(5)** Salve as alterações.

**(6)** Retorne à tela de emissão da **NFS-e** e **gere novamente** o documento fiscal com as informações atualizadas.

**(7)** Caso a rejeição persista, entre em contato com a **administração pública municipal** para validar se há alguma **restrição adicional** ou atualização necessária no cadastro do benefício fiscal.

**CAUSA**

A rejeição ocorre quando o **código de identificação do benefício fiscal municipal** informado no cadastro do serviço está com o **período de vigência expirado** em relação à **data de competência** utilizada na emissão da NFS-e ou no RPS. Isso acontece porque as prefeituras estabelecem **períodos específicos de validade** para cada código de benefício, e ao tentar emitir uma nota com data de competência **fora desse período**, o sistema municipal rejeita o documento automaticamente.
