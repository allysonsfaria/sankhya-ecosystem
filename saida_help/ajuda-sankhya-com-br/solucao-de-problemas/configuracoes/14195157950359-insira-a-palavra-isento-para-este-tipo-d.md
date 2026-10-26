---
id: "14195157950359"
titulo: "Insira a palavra ISENTO para este tipo de inscrição estadual."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14195157950359-Insira-a-palavra-ISENTO-para-este-tipo-de-inscri%C3%A7%C3%A3o-estadual"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-01T02:27:05Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "CORE_E05362", "Instrução para Inscrição Estadual ISENTO", "Inscrição Estadual", "Artigo atualizado KCS", "MEI", "CVE - KCS"]
---

# Insira a palavra ISENTO para este tipo de inscrição estadual.

**MENSAGEM**

[210] Rejeição: Inscrição Estadual do destinatário inválida

[CORE\_E05362]: Insira a palavra **"Isento"** para este tipo de inscrição estadual.

**SITUAÇÃO**

Ao tentar emitir uma **"NF-e"** ou **"NFC-e"**, o sistema apresenta a rejeição 210, indicando que a **"Inscrição Estadual"** do destinatário está inválida para a UF informada. Este erro ocorre durante o processo de autorização do documento fiscal eletrônico junto à SEFAZ. Também pode ocorrer para parceiros marcados como **"Micro empresário individual"** sem informação no campo de **"Inscrição Estadual"**.

**SOLUÇÃO**

**(1)** Verifique o **"Ambiente NF-e/NFC-e"** configurado na tela **"Preferências da Empresa"** (Comercial >> Preferências >> Empresa), aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFe"**. Confirme se está configurado como **"Produção"** ou **"Homologação"**.

**(2)** Acesse o portal da SEFAZ do estado do destinatário e consulte se o CNPJ/CPF está habilitado para receber notas fiscais no ambiente configurado. Utilize o portal: https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx.

**(3)** Acesse a tela **"Parceiros"** (Configurações >> Cadastros >> Parceiros) e localize o cadastro do destinatário que está apresentando o erro.

**(4)** Verifique se a **"Inscrição Estadual"** cadastrada está correta e completa. Caso a Inscrição Estadual possua menos caracteres que o padrão da UF, adicione zeros à esquerda até completar o formato válido.

**(5)** Para pessoas físicas, se o campo **"Inscrição Estadual"** estiver preenchido com RG ou outro documento, remova essa informação, pois pessoas físicas geralmente não possuem Inscrição Estadual válida para operações fiscais.

**(6)** Sempre que o parceiro estiver marcado como **"Micro empresário individual"** e não tiver **"Inscrição Estadual"**, insira no campo **"Insc. Estadual / Identidade"** a palavra **"Isento"**.

![Imagem do sistema](https://ajuda.sankhya.com.br/hc/article_attachments/16913983262487)

**(7)** Habilite o parâmetro **"Permitir IE para MEI ? - PERIEPARAMEI"** caso o MEI possua Inscrição Estadual obrigatória no estado.

**(8)** Caso o destinatário não esteja habilitado no ambiente de **"Homologação"**, altere o ambiente para **"Produção"** ou solicite ao parceiro que regularize sua situação junto à SEFAZ.

**(9)** Após realizar as correções necessárias no cadastro, tente emitir novamente a nota fiscal.

**CAUSA**

A rejeição 210 ocorre quando a **"Inscrição Estadual"** informada no cadastro do destinatário não está válida ou habilitada junto à SEFAZ da UF correspondente. As principais causas incluem:

- **"Inscrição Estadual"** incompleta: faltam caracteres (zeros à esquerda) para completar o formato válido da UF.
- Destinatário não habilitado no ambiente: o CNPJ/CPF não está cadastrado para receber notas no ambiente de **"Homologação"** ou **"Produção"** configurado.
- Irregularidade cadastral: o destinatário possui pendências ou irregularidades junto à SEFAZ.
- Pessoa física com **"Inscrição Estadual"** inválida: o campo foi preenchido incorretamente com RG ou outro documento não fiscal.
- **"Micro empresário individual"** (MEI): o parceiro está marcado como MEI e o campo **"Inscrição Estadual"** está vazio.
