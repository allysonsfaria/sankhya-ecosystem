---
id: "37226596023703"
titulo: "E0652 Rejeição: Em caso de importação de serviço pelo intermediário, o ISSQN deve ser retido pelo intermediário."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226596023703-E0652-Rejei%C3%A7%C3%A3o-Em-caso-de-importa%C3%A7%C3%A3o-de-servi%C3%A7o-pelo-intermedi%C3%A1rio-o-ISSQN-deve-ser-retido-pelo-intermedi%C3%A1rio"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:49Z"
rotulos: ["Central de Vendas", "SEFAZ", "Impostos", "Prefeituras", "NFS-e", "ISSQN", "Importação de Serviço", "Tipo de Retenção do ISS", "Retido pelo Intermediário", "ISSQN (Imposto Sobre Serviços de Qualquer Natureza)"]
---

# E0652 Rejeição: Em caso de importação de serviço pelo intermediário, o ISSQN deve ser retido pelo intermediário.

**MENSAGEM**

E0652 Rejeição: Em caso de importação de serviço pelo intermediário, o ISSQN deve ser retido pelo intermediário.

**SITUAÇÃO**

Ao emitir uma **NFS-e (Nota Fiscal de Serviço Eletrônica)** envolvendo importação de serviço com intermediário, o sistema retorna uma rejeição relacionada ao campo **"Tipo de Retenção do ISS"** informado no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas) e localize a nota fiscal de serviço que será emitida ou que foi rejeitada.

**(2)** Na aba **''Impostos''**, verifique se o campo **''Tipo de Retenção do ISS''** está preenchido como **''Tipo de Retenção do ISS''**, uma vez que envolve importação de serviço com intermediário.

**(3)** Confirme que todos os demais dados da nota estão corretos, incluindo:

- Dados do **tomador do serviço**;
- Dados do **intermediário**;
- Informações do **serviço prestado**;
- Valores e **alíquotas de ISS** aplicáveis

**(4)** Salve as alterações realizadas na nota fiscal.

**(5)** Emita novamente a **NFS-e** com as configurações corrigidas.

**CAUSA**

A rejeição ocorre porque a **legislação tributária federal e municipal** determina que, em operações de **importação de serviços** realizadas por meio de **intermediário**, a **responsabilidade pela retenção do ISSQN** é transferida para o intermediário.

Quando o campo **"Tipo de Retenção do ISS"** não está preenchido como **"Retido pelo Intermediário"**, o sistema gera o XML da NFS-e com informações divergentes das regras fiscais, fazendo com que a Sefaz rejeite o documento com a mensagem **E0652**. O preenchimento correto deste campo é **obrigatório** para garantir a conformidade fiscal e a aceitação da nota pela prefeitura.
