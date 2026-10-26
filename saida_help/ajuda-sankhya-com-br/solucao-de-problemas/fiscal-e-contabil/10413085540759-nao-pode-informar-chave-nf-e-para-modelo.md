---
id: "10413085540759"
titulo: "Não pode informar Chave NF-e para 'Modelo do Documento' diferente de 55, 65, 66"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10413085540759-N%C3%A3o-pode-informar-Chave-NF-e-para-Modelo-do-Documento-diferente-de-55-65-66"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:03:44Z"
rotulos: ["Configuração", "NF-e", "TOP", "Financeiro", "LIV_E00010", "EFD Contribuições", "Verifique registros e configurações na tela Empresa e Tipo de Operação", "Assegure a correta configuração do CST e cálculo de PIS/COFINS", "Chave NF-e não deve ser usada para modelos diferentes de 55 65 66"]
---

# Não pode informar Chave NF-e para 'Modelo do Documento' diferente de 55, 65, 66

**Mensagem:**

[LIV\_E00010] Não pode informar Chave NF-e para 'Modelo do Documento' diferente de 55, 65, 66.

**Causa:**

Ocorre quando o modelo de documento não é 55,65 e 66 e o campo CHAVE NF-e ESTÁ preenchido, e isso é indevido, pois esse campo só deve ser preenchido para os tipos de modelo citados.

**Solução:**

Verifique as configurações abaixo:

- Na tela **Empresa** (Caminho de acesso à tela: Comercial » Preferências » Empresa), aba 'EFD - Escrituração Fiscal Digital' se os registros C500, C501 e C505, estão marcados.

![Imagem 1: - No cadastro do Tipo de Operação TOP (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Operação…](https://ajuda.sankhya.com.br/hc/article_attachments/14833258078743)

- No cadastro do **Tipo de Operação TOP** (Caminho de acesso à tela: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP), na aba 'NF-e/NFC-e/CF-e', observe se o campo 'Modelo do Documento' está preenchido com o dado: 06-Nota Fiscal Conta de Energia Elétrica.

![Imagem 2: -A CST do PIS e COFINS devem representar crédito e no lançamento deve ter o cálculo do PIS e COFINS. Segue abaixo um…](https://ajuda.sankhya.com.br/hc/article_attachments/14833213349655)

-A CST do PIS e COFINS devem representar crédito e no lançamento deve ter o cálculo do PIS e COFINS.

Segue abaixo um artigo da nossa Central de Ajuda para auxílio na configuração do registro C500.

[O que é necessário para um documento ser apresentado no Registro C500 - EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051122833-O-que-%C3%A9-necess%C3%A1rio-para-um-documento-ser-apresentado-no-Registro-C500-EFD-Contribui%C3%A7%C3%B5es-?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg2NzczNjE3NTQsInRpY2tldF9pZCI6MTI5OTM2LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYzNTAxNzcyNH0.a0mcSA7QRS3Dx932dhcqqB6svNBYZbQ3l5gSsRHNTd0)

[Lançamentos de 'energia elétrica' não estão sendo gerados no registro C500 do EFD Contribuições](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044901813-Lan%C3%A7amentos-de-energia-el%C3%A9trica-n%C3%A3o-est%C3%A3o-sendo-gerados-no-registro-C500-do-EFD-Contribui%C3%A7%C3%B5es-Como-resolver-?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjo0MDg2NzczNjE3NTQsInRpY2tldF9pZCI6MTI5OTM2LCJjaGFubmVsX2lkIjo2MywidHlwZSI6IlNFQVJDSCIsImV4cCI6MTYzNTAxNzcyNH0.a0mcSA7QRS3Dx932dhcqqB6svNBYZbQ3l5gSsRHNTd0)

Após as configurações gere o livro novamente e o arquivo SPED.
