---
id: "37221461105943"
titulo: "E0020 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data de inscrição do CPF do emitente no cadastro CPF."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221461105943-E0020-Rejei%C3%A7%C3%A3o-A-data-de-compet%C3%AAncia-informada-na-DPS-deve-ser-igual-ou-posterior-%C3%A0-data-de-inscri%C3%A7%C3%A3o-do-CPF-do-emitente-no-cadastro-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:39Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "Erro", "Declaração de Prestação de Serviços (DPS)", "Data de inscrição do CPF do emitente no cadastro da Receita Federal", "CPF do emitente ainda não estava regularmente inscrito", "DPS deve ser igual ou posterior à data de inscrição do CPF do emitente"]
---

# E0020 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data de inscrição do CPF do emitente no cadastro CPF.

**MENSAGEM**

E0020 Rejeição: A data de competência informada na DPS deve ser igual ou posterior à data de inscrição do CPF do emitente no cadastro CPF.

**SITUAÇÃO**

Ao emitir uma **Declaração de Prestação de Serviços (DPS)**, o sistema rejeitou o documento porque a **data de competência informada** é anterior à **data de inscrição do CPF do emitente** no cadastro da Receita Federal. Isso significa que está sendo tentado declarar uma prestação de serviço em um período no qual o CPF do emitente ainda não estava regularmente inscrito.

**SOLUÇÃO**

**(1)** Verifique a **data de inscrição do CPF do emitente** no cadastro da Receita Federal. Acesse o site oficial da Receita Federal ou consulte o comprovante de inscrição no CPF para confirmar a data exata de cadastramento.

**(2)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do emitente da DPS.

**(3)** Confira se o **CPF informado** no cadastro está correto e corresponde ao CPF do emitente que consta na Receita Federal.

**(4)** Verifique a **data de competência** informada na DPS. Certifique-se de que esta data seja **igual ou posterior** à data de inscrição do CPF do emitente.

**(5)** Caso a data de competência esteja incorreta, ajuste-a para uma data válida que respeite a regra de validação da Receita Federal.

**(6)** Salve as alterações.

**(7)** Reenvie a **Declaração de Prestação de Serviços (DPS)** para processamento. 

**CAUSA**

A rejeição **E0020** ocorre quando a **data de competência** informada na Declaração de Prestação de Serviços é **anterior à data de inscrição do CPF do emitente** no cadastro da Receita Federal. Esta validação garante que não sejam declaradas prestações de serviços em períodos nos quais o CPF do emitente ainda não estava regularmente inscrito, assegurando a conformidade fiscal e a integridade das informações prestadas ao Fisco.
