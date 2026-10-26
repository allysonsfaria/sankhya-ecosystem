---
id: "37224213873559"
titulo: "E0293 Rejeição: O endereço nacional do intermediário do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo intermediário, exceto se o emitente da DPS é o intermediário do serviço."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224213873559-E0293-Rejei%C3%A7%C3%A3o-O-endere%C3%A7o-nacional-do-intermedi%C3%A1rio-do-servi%C3%A7o-deve-ser-informado-na-DPS-quando-o-valor-do-ISSQN-for-retido-pelo-intermedi%C3%A1rio-exceto-se-o-emitente-da-DPS-%C3%A9-o-intermedi%C3%A1rio-do-servi%C3%A7o"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:48Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Impostos", "NFS-e", "NFS-e (Nota Fiscal de Serviços Eletrônica)", "Tipo de Retenção do ISS", "Retido pelo Intermediário", "Retenção de ISSQN pelo intermediário"]
---

# E0293 Rejeição: O endereço nacional do intermediário do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo intermediário, exceto se o emitente da DPS é o intermediário do serviço.

**MENSAGEM**

E0293 Rejeição: O endereço nacional do intermediário do serviço deve ser informado na DPS quando o valor do ISSQN for retido pelo intermediário, exceto se o emitente da DPS é o intermediário do serviço.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e (Nota Fiscal de Serviços Eletrônica)** no padrão nacional, o sistema apresenta a rejeição E0293. Isso ocorre quando o **ISSQN está configurado para ser retido pelo intermediário** do serviço, mas as **informações do endereço nacional do intermediário não foram preenchidas** corretamente no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Central de Vendas"** (Comercial » Movimentos » Central de Vendas) e localize o documento fiscal que será emitido.

**(2)** Na aba **"Impostos"**, localize o campo **"Tipo de Retenção do ISS"** no rodapé do documento fiscal.

**(3)**  Verifique se o campo está preenchido com a opção **"Retido pelo Intermediário"**. Se estiver, prossiga para o próximo passo.

**(4)** Certifique-se de que o **cadastro do intermediário do serviço** está completo com todas as informações de endereço nacional:

- Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros);
- Localize o cadastro do **intermediário do serviço**;
- Na aba **''Identificação''**, verifique se os campos de **endereço** (logradouro, número, complemento, bairro, cidade, UF e CEP) estão **preenchidos corretamente**;
- Salve as alterações, se necessário.

**(5)** Retorne à **"Central de Vendas"** e verifique se o **intermediário está vinculado corretamente** ao documento fiscal.

**(6)** Caso o **emitente da NFS-e seja o próprio intermediário**, altere o campo **"Tipo de Retenção do ISS"** para **"Não Retido"** ou **"Retido pelo Tomador"**, conforme a operação.

**(7)** Após realizar os ajustes necessários, **gere novamente o XML** da NFS-e e tente emitir o documento.

**CAUSA**

A rejeição ocorre quando a **NFS-e no padrão nacional** é emitida com o **campo "Tipo de Retenção do ISS"** configurado como **"Retido pelo Intermediário"**, mas o sistema **não localiza as informações completas do endereço nacional do intermediário** do serviço no cadastro de parceiros.

Conforme as regras de validação da Sefaz, quando há **retenção de ISSQN pelo intermediário**, é obrigatório informar o endereço completo deste intermediário na DPS (Declaração de Prestação de Serviços), **exceto quando o próprio emitente da NFS-e é o intermediário** do serviço. A ausência ou incompletude dessas informações impede a validação do documento fiscal pela prefeitura.
