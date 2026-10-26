---
id: "37221535745047"
titulo: "E0038 Rejeição: A situação do convênio do município emissor informado na DPS deve ser \"ATIVO\" no cadastro de convênio municipal do sistema nacional."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221535745047-E0038-Rejei%C3%A7%C3%A3o-A-situa%C3%A7%C3%A3o-do-conv%C3%AAnio-do-munic%C3%ADpio-emissor-informado-na-DPS-deve-ser-ATIVO-no-cadastro-de-conv%C3%AAnio-municipal-do-sistema-nacional"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:33Z"
rotulos: ["Configuração", "NF-e", "Cidades", "SEFAZ", "Impostos", "Documento Fiscal Eletrônico (NF-e ou NFC-e)", "IBS (Imposto sobre Bens e Serviços)", "Documento fiscal não possui convênio ativo", "tributação municipal", "Convênio do município emissor"]
---

# E0038 Rejeição: A situação do convênio do município emissor informado na DPS deve ser "ATIVO" no cadastro de convênio municipal do sistema nacional.

**MENSAGEM**

E0038 Rejeição: A situação do convênio do município emissor informado na DPS deve ser "ATIVO" no cadastro de convênio municipal do sistema nacional.

**SITUAÇÃO**

Ao emitir um **Documento Fiscal Eletrônico** (NF-e ou NFC-e) contendo informações de **tributação municipal** relacionadas ao **IBS (Imposto sobre Bens e Serviços)**, o sistema identifica que o **convênio do município emissor** não está com a situação **"ATIVO"** no cadastro nacional da Sefaz. Dessa forma, a nota fiscal é **rejeitada** e a mensagem de erro E0038 é apresentada.

**SOLUÇÃO**

Para corrigir esta rejeição, é necessário **verificar e atualizar** o cadastro da empresa emissora no sistema, garantindo que o **município informado** possua convênio ativo. Siga os passos abaixo:

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas).

**(2)** Localize a **empresa emissora** do documento fiscal que foi rejeitado.

**(3)** Verifique na aba **"Geral"** se o campo **"Inscrição Municipal"** está corretamente preenchido com o município emissor.

**(4)** Confirme junto ao **setor fiscal ou contábil** da empresa se o município informado **possui convênio ativo** no sistema nacional da Sefaz para emissão de documentos fiscais com tributação de IBS.

**(5)** Caso o município **não possua convênio ativo**, será necessário:

- Aguardar a **ativação do convênio** pelo município junto à Sefaz; ou
- Ajustar o **cadastro da empresa** para um município que possua convênio ativo, se aplicável.

**(6)** Após a confirmação de que o **convênio está ativo**, realize uma nova tentativa de **emissão do documento fiscal**. 

**CAUSA**

A rejeição E0038 ocorre quando o **município emissor** informado no documento fiscal **não possui convênio ativo** no cadastro de convênio municipal do sistema nacional da Sefaz. Isso impede que o documento seja **autorizado**, pois a Sefaz exige que o município esteja **devidamente habilitado** para a emissão de documentos fiscais eletrônicos com tributação municipal relacionada ao **IBS**, conforme as regras estabelecidas pela **Reforma Tributária** (Lei Complementar nº 214/2025).
