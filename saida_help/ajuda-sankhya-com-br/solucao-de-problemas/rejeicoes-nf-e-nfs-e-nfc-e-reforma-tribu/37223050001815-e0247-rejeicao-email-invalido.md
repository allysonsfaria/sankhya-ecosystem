---
id: "37223050001815"
titulo: "E0247 Rejeição: Email inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37223050001815-E0247-Rejei%C3%A7%C3%A3o-Email-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:09Z"
rotulos: ["MDF-e", "CT-e", "Configuração", "Parceiro", "NF-e", "SEFAZ", "Erro", "Endereço de e-mail não atende aos padrões válidos de formatação", "Email inválido", "Preenchimento incorreto ou inválido do endereço de e-mail no cadastro do parceiro", "Padrões técnicos estabelecidos", "Endereço de e-mail"]
---

# E0247 Rejeição: Email inválido.

**MENSAGEM**

E0247 Rejeição: Email inválido.

**SITUAÇÃO**

O documento fiscal eletrônico (NF-e, NFC-e, CT-e ou MDF-e) foi emitido com um endereço de e-mail informado nos dados cadastrais que não está em conformidade com o formato esperado, resultando na rejeição pelo sistema.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros).

**(2)** Localize o cadastro do **destinatário** ou **emitente** relacionado ao documento fiscal rejeitado.

**(3)** Na aba **''Endereço''**, no campo **''E-mail''**, certifique-se de que o endereço eletrônico está preenchido corretamente, seguindo o formato padrão:

- usuario@dominio.com

**(4)** Corrija possíveis erros de digitação, como:

- Ausência do símbolo **"@"**;
- Espaços em branco antes, durante ou depois do endereço;
- Caracteres especiais inválidos;
- Falta de domínio (exemplo: .com, .com.br, .gov.br);
- E-mail preenchido com zeros ou informações genéricas inválidas.

**(5)** Caso o documento seja um **CT-e** ou **MDF-e**, verifique também o e-mail cadastrado na tela **''Empresas''** (Configurações » Cadastros » Empresas), na aba **''Endereço''**, no campo **''E-mail''**.

**(6)** Se o documento possuir informações de **Responsável Técnico**, acesse a tela de configuração correspondente e valide o campo **"E-mail do Responsável Técnico"**.

**(7)** Após realizar as correções necessárias, **salve o cadastro** e retorne à tela de emissão do documento fiscal.

**(8)** **Redigite o documento fiscal** para que as informações atualizadas sejam carregadas no XML.

**(9)** **Gere um novo lote** e tente transmitir o documento novamente para a Sefaz.

**CAUSA**

A rejeição **E0247** é causada pelo **preenchimento incorreto ou inválido** do endereço de e-mail no cadastro do parceiro, empresa ou responsável técnico. A Sefaz valida o formato do e-mail informado no XML do documento fiscal e, caso não esteja em conformidade com os **padrões técnicos estabelecidos** (presença de "@", domínio válido, ausência de caracteres especiais inválidos, etc.), o documento é rejeitado.
