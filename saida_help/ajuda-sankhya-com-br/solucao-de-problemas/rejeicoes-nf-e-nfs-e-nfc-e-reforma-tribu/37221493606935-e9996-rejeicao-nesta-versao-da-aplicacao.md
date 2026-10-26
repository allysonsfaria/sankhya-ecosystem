---
id: "37221493606935"
titulo: "E9996 Rejeição: Nesta versão da aplicação, não é permitida a emissão de NFS-e pelo tomador ou intermediário."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221493606935-E9996-Rejei%C3%A7%C3%A3o-Nesta-vers%C3%A3o-da-aplica%C3%A7%C3%A3o-n%C3%A3o-%C3%A9-permitida-a-emiss%C3%A3o-de-NFS-e-pelo-tomador-ou-intermedi%C3%A1rio"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:36Z"
rotulos: ["Configuração", "SEFAZ", "NFS-e", "Passos para resolver", "Erro", "Como Resolver", "NFS-e Padrão Nacional", "Tipo de Retenção do ISS", "Emissão de NFS-e pelo tomador ou intermediário", "Papel do emitente", "Documentos Eletrônicos"]
---

# E9996 Rejeição: Nesta versão da aplicação, não é permitida a emissão de NFS-e pelo tomador ou intermediário.

**MENSAGEM**

E9996 Rejeição: Nesta versão da aplicação, não é permitida a emissão de NFS-e pelo tomador ou intermediário.

**SITUAÇÃO**

Ao tentar emitir uma **NFS-e Padrão Nacional**, o sistema retorna a rejeição acima, indicando que a versão atual da aplicação **não permite a emissão de NFS-e pelo tomador ou intermediário**.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Central de Vendas"** (Comercial » Rotinas » Central de Vendas) e localize a nota fiscal de serviço que está sendo emitida.

**(2)** Verifique se a nota está configurada para **emissão pelo prestador de serviço**, e não pelo tomador ou intermediário. A NFS-e Padrão Nacional deve ser emitida exclusivamente pelo prestador do serviço.

**(3)** Caso a nota esteja configurada para emissão pelo tomador ou intermediário, ajuste as configurações para que a **emissão seja realizada pelo prestador**.

**(4)** Na aba **"Impostos"** verifique o campo **"Tipo de Retenção do ISS"** e certifique-se de que está preenchido corretamente com uma das seguintes opções:

- **"Não Retido"**
- **"Retido pelo Tomador"**
- **"Retido pelo Intermediário"**

**(5)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(6)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''Geral''**, verifique se o campo **''Emitir NFS-e Padrão Nacional''.**

**(7)** Verifique se a **série da NFS-e** está configurada corretamente, respeitando os requisitos do Padrão Nacional:

- Prefixo da Série: **2 dígitos** (ex: 80)
- Série da Nota: **3 dígitos** (ex: 000)
- Série NFS-e Padrão Nacional: **5 dígitos entre 80000 e 89999**

**(8)** Após realizar os ajustes necessários, tente emitir novamente a NFS-e.

**CAUSA**

A rejeição E9996 ocorre porque a **versão atual da aplicação do Padrão Nacional de NFS-e** não suporta a emissão de notas fiscais de serviço eletrônicas pelo tomador ou intermediário. O sistema está configurado para aceitar **apenas emissões realizadas pelo prestador do serviço**, conforme as especificações técnicas do layout Padrão Nacional. Quando há tentativa de emissão com configuração inadequada do tipo de emitente, o sistema retorna esta rejeição para garantir a conformidade com as regras estabelecidas.
