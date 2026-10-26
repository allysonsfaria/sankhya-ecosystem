---
id: "37229540593815"
titulo: "E0400 REJEIÇÃO: O CEP não deve ser informado quando o endereço da atividade de evento ocorrer no exterior do país"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37229540593815-E0400-REJEI%C3%87%C3%83O-O-CEP-n%C3%A3o-deve-ser-informado-quando-o-endere%C3%A7o-da-atividade-de-evento-ocorrer-no-exterior-do-pa%C3%ADs"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:13:55Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Cidades", "SEFAZ", "Sefaz valida que o campo CEP não deve ser informado", "Endereço da atividade do evento está localizado no exterior", "CEP não deve ser informado", "Endereço da atividade de evento ocorrer no exterior", "Exteriror", "Documentos Eletrônicos"]
---

# E0400 REJEIÇÃO: O CEP não deve ser informado quando o endereço da atividade de evento ocorrer no exterior do país

**MENSAGEM**

E0400 Rejeição: O CEP não deve ser informado quando o endereço da atividade de evento ocorrer no exterior do país.

**SITUAÇÃO**

A rejeição está relacionada à emissão de um documento fiscal de evento em que o local de realização da atividade está informado como sendo no exterior, com o preenchimento de CEP no endereço do evento.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Parceiros''** (Configurações » Cadastros » Parceiros) e localize o endereço do local da atividade.

**(2)** Acesse a tela **"Estados"** (Configurações » Cadastros » Endereços » Estados), busque pelo Estado do parceiro (prestador de serviço). Neste, verifique se o campo **"País"** está preenchido com um país diferente do Brasil (código diferente de 1058).

**(3)** Retorne ao passo 1, busque pelo parceiro (prestador de serviço). Na aba **''Endereço''**, certifique-se de que o campo **"CEP"** esteja quando o endereço for no exterior.

**(4)** Preencha corretamente os campos específicos para endereços no exterior:

- **"Endereço"**: informe o endereço completo no exterior;
- **"Número"**: informe o número do endereço;
- **"País"**: selecione o país correspondente (diferente do Brasil);
- **"Código Postal"**: informe o código postal do país de destino (se aplicável).

**(5)** Acesse a tela **''Cidade''** (Configurações » Cadastros » Endereços » Cidades) e verifique a configuração para o exterior:

- **"Cód. UF"**: deve estar vinculado ao estado "EXTERIOR" (sigla "EX");
- **"Mun. domicílio fiscal"**: deve estar preenchido com **"9999999"** para parceiros do exterior.

**(6)** Salve as alterações e **retransmita o evento** ou **gere novamente o documento fiscal**.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida que o campo CEP não deve ser informado** quando o **endereço da atividade do evento está localizado no exterior**. O CEP é um código específico do sistema postal brasileiro e **não se aplica a endereços internacionais**. Para endereços no exterior, devem ser utilizados os campos **"Código Postal"** e **"País"**, deixando o campo **"CEP" em branco**.
