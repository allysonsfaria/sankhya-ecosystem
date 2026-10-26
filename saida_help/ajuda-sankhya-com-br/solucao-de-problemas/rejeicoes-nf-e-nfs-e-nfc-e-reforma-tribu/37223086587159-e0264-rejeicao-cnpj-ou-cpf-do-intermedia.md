---
id: "37223086587159"
titulo: "E0264 Rejeição: CNPJ ou CPF do intermediário não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo de Retenção do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223086587159-E0264-Rejei%C3%A7%C3%A3o-CNPJ-ou-CPF-do-intermedi%C3%A1rio-n%C3%A3o-foi-informado-mas-existe-uma-indica%C3%A7%C3%A3o-para-reten%C3%A7%C3%A3o-do-ISSQN-na-DPS-no-campo-de-tipo-de-Reten%C3%A7%C3%A3o-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:03Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Passos para resolver", "Retenção do ISSQN", "Retido pelo Intermediário", "CNPJ ou CPF do intermediário não foi informado", "Retenção do ISSQN na DPS", "CNPJ ou CPF do intermediário"]
---

# E0264 Rejeição: CNPJ ou CPF do intermediário não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo de Retenção do ISSQN.

**MENSAGEM**

E0264 Rejeição: CNPJ ou CPF do intermediário não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo de Retenção do ISSQN.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)**, o sistema apresenta a mensagem de rejeição informando que o **CNPJ ou CPF do intermediário não foi informado**, porém o campo **"Tipo de Retenção do ISSQN"** está configurado como **"Retido pelo Intermediário"**.

**SOLUÇÃO**

Para resolver esta rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela de **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do **intermediário do serviço**.

**(2)** Na aba **''Identificação''**, verifique se o campo **''CNPJ / CPF''** está corretamente preenchido no cadastro.

**(3)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas), na grade **''Rodapé''**, na aba **''Impostos''**, verifique o campo **''Tipo de Retenção do ISS''**.

**(4)** Caso o serviço **não possua intermediário**, altere o campo "Tipo de Retenção do ISS" para uma das seguintes opções:

- **"Não Retido"** - quando não há retenção de ISSQN;
- **"Retido pelo Tomador"** - quando a retenção é feita pelo tomador do serviço.

**(5)** Caso o serviço **possua intermediário** e a retenção seja realmente feita por ele, certifique-se de que o **CNPJ ou CPF do intermediário** esteja informado no documento fiscal, no campo específico destinado aos dados do intermediário.

**(6)** Após realizar os ajustes necessários, **gere novamente o lote da NFS-e** e tente transmitir o documento.

**CAUSA**

A rejeição ocorre porque o campo **"Tipo de Retenção do ISSQN"** foi preenchido com a opção **"Retido pelo Intermediário"**, porém o **CNPJ ou CPF do intermediário não foi informado** no documento fiscal. A Prefeitura exige que, quando houver indicação de retenção pelo intermediário, os dados cadastrais completos deste intermediário sejam obrigatoriamente informados na DPS (Declaração de Prestação de Serviços).
