---
id: "35904027129239"
titulo: "EFD Contribuições - Conta Contábil nos registros D101 e D105"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35904027129239-EFD-Contribui%C3%A7%C3%B5es-Conta-Cont%C3%A1bil-nos-registros-D101-e-D105"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:24:26Z"
rotulos: ["Configuração", "Fiscal", "Contribuições", "Impostos", "Contabilização", "Escrituração Fiscal Digital", "EFD", "EFD Contribuições", "D105", "D101", "registros", "Conta Contábil"]
---

# EFD Contribuições - Conta Contábil nos registros D101 e D105

**SITUAÇÃO:**

Ao contabilizar documentos fiscais que compõem os registros D101 e D105, foi identificado que as contas contábeis não são geradas quando o documento é emitido ou lançado em uma empresa e a contabilização ocorre em outra, mesmo que as configurações contábeis estejam aparentemente corretas.

**SOLUÇÃO:**

Para que a geração das contas contábeis ocorra normalmente, existem duas alternativas:

**(1)** Realize a contabilização na própria empresa do documento, garantindo que a empresa da conta analítica corresponda à do documento.

**(2)** Na tela **“Empresa”** (Comercial» Preferências» Empresa), acesse a aba “**EFD – Escrituração Fiscal Digital”** e, na seção **“EFD Contribuições**”, desmarque a opção **“Contas contábeis analíticas para geração dos registros de apuração de PIS/COFINS”**.

**CAUSA:**

Quando a empresa está configurada para utilizar a rotina Contas contábeis analíticas para geração dos registros de apuração de PIS/COFINS, o sistema realiza a validação entre a empresa vinculada à conta contábil e a empresa do documento fiscal.
Dessa forma, caso a contabilização ocorra em uma empresa diferente daquela onde o documento foi lançado, o sistema não localiza a conta analítica correspondente, e, consequentemente, não gera as contas contábeis nos registros D101 e D105.
