---
id: "37225858478743"
titulo: "E0484 Rejeição: CPF do fornecedor informado na DPS é inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225858478743-E0484-Rejei%C3%A7%C3%A3o-CPF-do-fornecedor-informado-na-DPS-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:35Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "SEFAZ", "Erro", "CPF do fornecedor", "Documento de Prestação de Serviços (DPS)", "CPF do fornecedor informado na DPS inválido", "Dígito verificador inválido", "Sequência numérica incorreta", "Dígito verificador (último número do CPF) inválido", "E0484 Rejeição", "Rejeição E0484"]
---

# E0484 Rejeição: CPF do fornecedor informado na DPS é inválido

**MENSAGEM**

E0484 Rejeição: CPF do fornecedor informado na DPS é inválido.

**SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)** no sistema Sankhya, o usuário vinculou um parceiro cujo **CPF está incorreto** no cadastro. Durante a validação, o documento foi rejeitado porque o CPF informado apresenta **dígito verificador inválido, sequência numérica incorreta ou está preenchido apenas com zeros**.

**SOLUÇÃO**

Para corrigir a rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **parceiro** vinculado ao DPS rejeitado.

**(2)** Na aba **"Identificação"**, localize o campo **"CNPJ / CPF"**.

**(3)** Verifique se o campo **"Tipo de Pessoa"** está configurado como **"Física"**.

**(4)** Corrija o campo **"CNPJ / CPF"** inserindo um **CPF válido** com **11 dígitos**, sem pontos, traços ou espaços em branco.

**(5)** Salve as alterações realizadas no cadastro do parceiro.

**(6)** Retorne ao **DPS** e redigite o cabeçalho do documento, garantindo que o fornecedor atualizado seja vinculado corretamente.

**(7)** Gere um novo lote e transmita o documento.

**OBSERVAÇÕES:**

- Caso o fornecedor seja **estrangeiro**, certifique-se de que o campo **"Tipo de Pessoa"** está configurado como **"Física"**.
- Para parceiros estrangeiros, o campo **"CNPJ / CPF"** pode permanecer em branco, desde que o parâmetro **"Aceita CGC/CPF de Parceiro em branco? - ACEITACGCBRANCO"** esteja ativado.

**CAUSA**

A rejeição ocorre quando o **CPF do parceiro** informado no DPS está **inválido**. Isso pode acontecer quando o CPF é preenchido com **apenas zeros**, possui **sequência numérica incorreta** ou apresenta **dígito verificador (último número do CPF) inválido**. Ao validar a consistência do CPF durante o processamento do documento e, ao identificar inconsistências, retorna a rejeição E0484.
