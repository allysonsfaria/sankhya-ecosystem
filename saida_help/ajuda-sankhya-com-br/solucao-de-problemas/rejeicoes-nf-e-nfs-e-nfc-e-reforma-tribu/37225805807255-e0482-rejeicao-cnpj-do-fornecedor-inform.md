---
id: "37225805807255"
titulo: "E0482 Rejeição: CNPJ do fornecedor informado na DPS não encontrado no cadastro CNPJ"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225805807255-E0482-Rejei%C3%A7%C3%A3o-CNPJ-do-fornecedor-informado-na-DPS-n%C3%A3o-encontrado-no-cadastro-CNPJ"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:36Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Erro", "CNPJ do fornecedor informado na DPS não encontrado", "DPS não encontrado no cadastro CNPJ", "CNPJ do fornecedor", "DPS (Declaração de Prestação de Serviços)", "CNPJ cadastrado com caracteres especiais", "Rejeição E0482", "E0482 Rejeição"]
---

# E0482 Rejeição: CNPJ do fornecedor informado na DPS não encontrado no cadastro CNPJ

**MENSAGEM**

E0482 Rejeição: CNPJ do fornecedor informado na DPS não encontrado no cadastro CNPJ.

**SITUAÇÃO**

Ao emitir um documento fiscal eletrônico (NF-e ou NFC-e) contendo informações da **DPS (Declaração de Prestação de Serviços)** relacionada à Reforma Tributária, o sistema tenta validar o **CNPJ do fornecedor** informado na DPS. Caso este CNPJ não seja localizado no cadastro de parceiros do sistema, a nota é rejeitada pela Sefaz com a mensagem de erro E0482.

**SOLUÇÃO**

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o cadastro do fornecedor utilizando o **CNPJ** informado na DPS.

**(2)** Verifique se o **CNPJ** está cadastrado corretamente, **sem caracteres especiais** como pontos (.), barras (/) ou hífens (-), mantendo apenas os números.

**(3)** Na aba **''Identificação''**, no campo **''Tipo''**, confirme se o parceiro está definido como **''Fornecedor''**.

**(4)** Verifique se o campo **"Insc. Estadual / Identidade"** está preenchido corretamente, sem caracteres especiais, pontos ou hífens, contendo apenas números.

- Caso o fornecedor seja isento, deixe o campo vazio e configure adequadamente a **"Classificação I.E"**.

**(5)** Certifique-se de que o cadastro do parceiro está com o status **"Ativo"**.

**(6)** Após realizar as correções necessárias, salve o cadastro do parceiro.

**(7)** Retorne ao documento fiscal e gere novamente o lote da NF-e ou NFC-e para transmissão à Sefaz. 

**CAUSA**

A rejeição ocorre quando o **CNPJ do fornecedor** informado na **DPS (Declaração de Prestação de Serviços)** do documento fiscal **não está cadastrado** no sistema ou apresenta **divergências no cadastro**, como:

- CNPJ cadastrado com **caracteres especiais** (pontos, barras ou hífens);
- Parceiro não classificado como **"Fornecedor"**;
- **Inscrição Estadual** preenchida incorretamente, contendo caracteres especiais ou sem os zeros à esquerda;
- Cadastro do parceiro com status **"Inativo"**;
- CNPJ inexistente ou não localizado na base de dados do sistema.
