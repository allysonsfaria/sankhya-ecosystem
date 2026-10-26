---
id: "37223138553111"
titulo: "E0268 Rejeição: CPF do intermediário não encontrado no cadastro CPF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223138553111-E0268-Rejei%C3%A7%C3%A3o-CPF-do-intermedi%C3%A1rio-n%C3%A3o-encontrado-no-cadastro-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:01Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "CPF", "Erro", "CPF do intermediário", "Erro de digitação no cadastro do parceiro", "NF-e ou NFC-e com informações de intermediador da operação", "CPF do intermediário informado no documento fiscal não foi encontrado", "CPF do intermediário não encontrado na base de dados da Receita Federal"]
---

# E0268 Rejeição: CPF do intermediário não encontrado no cadastro CPF.

**MENSAGEM**

E0268 Rejeição: CPF do intermediário não encontrado no cadastro CPF.

**SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com informações de intermediador da operação, o **CPF do intermediário** informado no documento fiscal **não foi encontrado** na base de dados da Receita Federal. A rejeição ocorre no momento da transmissão do documento fiscal eletrônico.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do **intermediador** da operação.

**(3)** Na aba **''Identificação''**, verifique se o **CPF informado** no campo **"CPF/CNPJ"** está correto e **devidamente cadastrado** na Receita Federal.

**(4)** Caso o CPF esteja incorreto, corrija a informação no cadastro do parceiro com o **número válido** do CPF do intermediador.

**(5)** Se o CPF estiver correto, mas ainda assim ocorrer a rejeição, verifique se o **CPF está ativo** e regularizado junto à Receita Federal através do site oficial.

**(6)** Após realizar as correções necessárias no cadastro do intermediador, **reemita a NF-e ou NFC-e** para que o documento seja transmitido corretamente. 

**CAUSA**

A rejeição é retornada pela **SEFAZ** quando o **CPF do intermediário** informado no documento fiscal eletrônico **não existe** ou **está inválido** na base de dados da Receita Federal. Isso pode ocorrer devido a **erro de digitação** no cadastro do parceiro, CPF **cancelado** ou **suspenso**, ou ainda por se tratar de um **número inexistente**.
