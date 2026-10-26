---
id: "37222627581207"
titulo: "REJEIÇÃO E0204: CNPJ ou CPF do tomador não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo \"Retenção do ISSQN\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222627581207-REJEI%C3%87%C3%83O-E0204-CNPJ-ou-CPF-do-tomador-n%C3%A3o-foi-informado-mas-existe-uma-indica%C3%A7%C3%A3o-para-reten%C3%A7%C3%A3o-do-ISSQN-na-DPS-no-campo-de-tipo-Reten%C3%A7%C3%A3o-do-ISSQN"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:36Z"
rotulos: ["Configuração", "Parceiro", "Impostos", "Prefeituras", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "Retenção do ISSQN", "Tipo de Retenção do ISS", "Retenção do ISSQN na DPS", "CNPJ ou CPF do tomador não foi informado", "CNPJ ou CPF do tomador do serviço"]
---

# REJEIÇÃO E0204: CNPJ ou CPF do tomador não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo "Retenção do ISSQN"

**MENSAGEM**

E0204 Rejeição: CNPJ ou CPF do tomador não foi informado, mas existe uma indicação para retenção do ISSQN na DPS no campo de tipo "Retenção do ISSQN".

**SITUAÇÃO**

Ao tentar emitir uma NFS-e (Nota Fiscal de Serviços Eletrônica) com **retenção de ISSQN**, a nota é rejeitada pela prefeitura apresentando a mensagem de erro E0204. Isso ocorre quando o sistema identifica que foi configurada a **retenção do imposto**, porém o **CNPJ ou CPF do tomador do serviço** não foi informado corretamente no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse o cadastro do **"Parceiro"** (Configurações » Cadastros » Parceiros) e localize o tomador do serviço para o qual está emitindo a NFS-e.

**(2)** Na aba **''Identificação''**, verifique se o campo **''CNPJ / CPF''** está preenchido corretamente.

- Caso esteja vazio ou incorreto, corrija a informação.

**(3)** Caso o tomador possua **Inscrição Municipal**, verifique se este campo também está preenchido corretamente no cadastro do parceiro.

**(4)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(5)** Na grade **''Rodapé''**, verifique na aba **''Impostos''** o campo **''Tipo de Retenção do ISS''**. Certifique-se de que está configurado corretamente:

- **''Não Retido'':** quando não há retenção de ISS;
- **''Retido pelo Tomador'':** quando o tomador é responsável pela retenção;
- **''Retido pelo Intermediário'':** quando há intermediário responsável pela retenção.

**(6)** Se o tomador **não deve reter o ISS**, acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(7)** Na aba **''Fiscal''**, desmarque o campo **"Retém ISS"**.

**(8)** Em seguida, no documento fiscal, altere o campo "Tipo de Retenção do ISS" para "Não retido".

**(9)** Após realizar as correções, gere novamente o lote da NFS-e e tente transmitir o documento fiscal.

**(10)** Se o erro persistir, retorne ao **passo 4**, clique em **''NFS-e''** e selecione a opção **''Gerar XML do RPS para NFS-e''**. No XML gerado, verifique se as tags relacionadas ao tomador estão preenchidas corretamente, especialmente as informações de **CNPJ/CPF** e **ISSRetido**.

**CAUSA**

A rejeição E0204 ocorre porque o sistema identificou que existe uma **indicação de retenção de ISSQN** configurada no documento fiscal (campo "Tipo de Retenção do ISSQN"), porém o **CNPJ ou CPF do tomador do serviço não foi informado** ou está incorreto. A prefeitura exige que, quando houver retenção de ISS, os dados cadastrais completos do tomador sejam enviados no XML da NFS-e, incluindo obrigatoriamente o documento de identificação (CNPJ ou CPF). Sem essa informação, não é possível identificar o responsável pela retenção do imposto, resultando na rejeição do documento fiscal.
