---
id: "37226682722967"
titulo: "E0672 Rejeição: Não pode haver retenção do ISSQN se o tomador for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226682722967-E0672-Rejei%C3%A7%C3%A3o-N%C3%A3o-pode-haver-reten%C3%A7%C3%A3o-do-ISSQN-se-o-tomador-for-o-emitente-da-DPS-e-estiver-estabelecido-em-munic%C3%ADpio-diferente-do-munic%C3%ADpio-de-incid%C3%AAncia-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:46Z"
rotulos: ["Configuração", "Parceiro", "XML", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "NFS-e para um tomador de serviço localizado em município diferente", "Retenção de ISSQN configurada", "Reter o ISSQN", "Tomador do serviço não está inscrito no município de incidência do imposto", "Empresas inscritas no município podem efetuar a retenção de ISSQN"]
---

# E0672 Rejeição: Não pode haver retenção do ISSQN se o tomador for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN.

**MENSAGEM**

E0672 Rejeição: Não pode haver retenção do ISSQN se o tomador for o emitente da DPS e estiver estabelecido em município diferente do município de incidência do ISSQN.

**SITUAÇÃO**

Ao tentar emitir uma NFS-e para um tomador de serviço localizado em município diferente do município onde ocorreu a prestação do serviço, com **retenção de ISSQN configurada**, a nota é rejeitada pela prefeitura apresentando a mensagem de erro E0672.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse o cadastro do **"Parceiro"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço.

**(2)** Verifique o campo **“Retém ISS”** no cadastro da operação. Caso esteja configurado como **“Sim”**, altere para **“Não”**, uma vez que o tomador do serviço não possui inscrição no município de incidência do ISSQN.

**(3)** Confirme se o **CNPJ** e a **Inscrição Municipal** do tomador estão corretos no cadastro.

**(4)** Acesse a tela [**''Central de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas), na aba **''Cabeçalho''**, verifique se o campo **''Cidade de Prestação de Serviço''** está preenchido corretamente com o município onde o serviço foi efetivamente prestado.

**(5)** Acesse o cadastro do [**"Tipo de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(6)** Na aba **“NFS-e”**, no campo **“Cód. Natureza Oper. ISS (NFS-e)”**, selecione a natureza de operação adequada à prestação do serviço, garantindo que a configuração esteja compatível com **operações sem retenção de ISS**, quando o tomador estiver localizado em município diferente do município de incidência do imposto.

**(7)** Gere novamente o lote da NFS-e e exporte o arquivo XML no Portal de Vendas (NFS-e » Gerar XML do RPS para NFS-e).

**(8)** Verifique no XML se a tag **<ISSRetido>** está preenchida com **"2"** (Sem retenção de ISSQN). Se estiver com valor diferente, revise as configurações anteriores. 

**CAUSA**

A rejeição ocorre porque o sistema está configurado para **reter o ISSQN**, porém o **tomador do serviço não está inscrito no município de incidência do imposto**. Segundo as regras da legislação tributária municipal, **apenas empresas inscritas no município podem efetuar a retenção de ISSQN**. Quando o tomador está estabelecido em município diferente do município onde ocorreu a prestação do serviço, a retenção não é permitida, devendo o ISSQN ser recolhido pelo prestador no município de incidência.
