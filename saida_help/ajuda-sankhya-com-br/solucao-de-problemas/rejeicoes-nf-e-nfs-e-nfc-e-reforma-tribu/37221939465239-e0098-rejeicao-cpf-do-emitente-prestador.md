---
id: "37221939465239"
titulo: "E0098 Rejeição: CPF do emitente prestador não encontrado no cadastro CPF na data de competência."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221939465239-E0098-Rejei%C3%A7%C3%A3o-CPF-do-emitente-prestador-n%C3%A3o-encontrado-no-cadastro-CPF-na-data-de-compet%C3%AAncia"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:12Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Receita Federal", "SEFAZ", "Erro", "NF-e de serviços", "Base de dados da Receita Federal", "CPF do emitente prestador não foi encontrado", "Data de competência informada no documento fiscal", "CPF do emitente prestador"]
---

# E0098 Rejeição: CPF do emitente prestador não encontrado no cadastro CPF na data de competência.

**MENSAGEM**

E0098 Rejeição: CPF do emitente prestador não encontrado no cadastro CPF na data de competência.

**SITUAÇÃO**

Ao emitir uma **NF-e de serviços**, o documento foi **rejeitado pela SEFAZ** com a mensagem informando que o **CPF do emitente prestador** não foi encontrado no cadastro da Receita Federal na data de competência informada no documento fiscal.

**SOLUÇÃO**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Empresas) e localize o **cadastro da empresa emitente** do documento fiscal.

**(2)** Verifique se o **CPF informado no cadastro** está correto e corresponde ao CPF do prestador de serviços.

**(3)** Consulte o **CPF na Receita Federal** para confirmar se o mesmo está **ativo e regularizado** na data de competência do documento:

- Acesse o site da [**''Receita Federal''**](https://servicos.receita.fazenda.gov.br/);
- Realize a consulta da **situação cadastral do CPF**;

**(4)** Caso o **CPF esteja incorreto** no cadastro da empresa, corrija a informação na aba **''Geral''** no campo **"CPF/CNPJ"**.

**(5)** Caso o CPF esteja **inativo ou irregular** na Receita Federal, será necessário **regularizar a situação cadastral** junto ao órgão competente antes de emitir o documento fiscal.

**(6)** Após realizar as correções necessárias, **exclua a nota rejeitada** e realize o **faturamento novamente**. 

**CAUSA**

A rejeição ocorre quando o **CPF do emitente prestador** informado no documento fiscal **não consta na base de dados da Receita Federal** na data de competência do serviço, ou quando o CPF está **inativo, cancelado ou com situação cadastral irregular**. A SEFAZ realiza a validação cruzada das informações do emitente com os cadastros oficiais, e caso haja divergência ou inexistência do CPF, o documento é rejeitado.
