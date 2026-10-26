---
id: "36690300291351"
titulo: "1026 Rejeição: Alíquota do IBS da UF inválida [nItem: 1]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36690300291351-1026-Rejei%C3%A7%C3%A3o-Al%C3%ADquota-do-IBS-da-UF-inv%C3%A1lida-nItem-1"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:22:31Z"
rotulos: ["Configuração", "NFe", "NF-e", "Central de Vendas", "Portal de Vendas", "SEFAZ", "Impostos", "Tributação", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Alíquota do IBS da UF inválida", "Alíquota do IBS", "Reforma Tributária", "Artigo atualizado KCS", "Alíquotas de IBS", "Docs Eletrônicos - KCS"]
---

# 1026 Rejeição: Alíquota do IBS da UF inválida [nItem: 1]

**MENSAGEM**

[1026] Rejeição: Alíquota do IBS da UF inválida [nItem: 1]

Ou ainda:

[1026] Rejeição: Alíquota do IBS da UF deve ser igual a 0,1% para documento emitido em 2026 [nItem: 1]

### SITUAÇÃO

Esta rejeição indica que a **alíquota do imposto IBS** informada na nota fiscal é diferente do valor de **0,1%** exigido pela **SEFAZ** conforme a legislação para o ano de emissão. Isso ocorre geralmente em emissões de NF-e (modelo 55) ou NFC-e (modelo 65) quando os parâmetros tributários estão incorretos.

### SOLUÇÃO

Para corrigir a rejeição, ajuste a **"Alíquota do IBS da UF"** no cadastro de alíquotas, seguindo os passos abaixo:

**(1)** Acesse o **"Cadastro de Alíquotas IBS/CBS da Reforma Tributária"** (Livros Fiscais >> Cadastros >> Alíquotas de IBS) e localize a alíquota utilizada no item rejeitado.

**(2)** Caso seja necessário identificar o código, acesse o **Portal de Vendas** (**Comercial > Consultas > Portal de Vendas**). Localize a nota e dê um duplo clique sobre ela para abrir a tela **Central de Vendas**. Em seguida, clique no botão **Outras Opções do Item** (ícone de três pontos) e selecione a opção "**Consultar/Alterar Dados do Imposto do Item"**.
![Imagem 1: (1) Acesse o "Cadastro de Alíquotas IBS/CBS da Reforma Tributária" (Livros Fiscais >> Cadastros >> Alíquotas de IBS) e…](https://ajuda.sankhya.com.br/hc/article_attachments/36690300272023)

**(3)** Em seguida, acesse a tela de **''Alíquota de IBS''**(Livros Fiscais » Cadastros » Aliquotas de IBS), no cadastro da alíquota identificada, acesse a aba **"Tributação"**, seção **"Alíquotas"** e ajuste conforme o ano de emissão do documento:

- **2025 e 2026:** configure **"Alíquota IBS Estado"** como 0,1%.
- **2027 e 2028:** configure **"Alíquota IBS Estado"** como 0,05%.
- **Anos posteriores a 2028:** utilize a alíquota de referência ou específica publicada pela legislação.
- **Exceção:** Se o campo **"Classificação Tributária"** (cClassTrib) possuir indicador de **Tributação Regular**, a alíquota deve ser igual a **zero**.

  ![Imagem 2: Exceção: Se o campo "Classificação Tributária" (cClassTrib) possuir indicador de Tributação Regular , a alíquota deve…](https://ajuda.sankhya.com.br/hc/article_attachments/41802917540759)

**(4)** Configure a **"Alíquota IBS Município"** conforme a legislação:

- **2026:** mantenha com valor **zerado (0,00)**, conforme Art. 343 da LC 214/2025.
- **2027 e 2028:** configure como 0,05%.
  ![Imagem 3: 2027 e 2028: configure como 0,05%.](https://ajuda.sankhya.com.br/hc/article_attachments/41802917542423)

**(5)** Verifique também a tela **"Alíquota CBS"**. Certifique-se de que esteja configurada como **0,9%** para documentos emitidos em 2025 e 2026, conforme Art. 346 da LC 214/2025. Isso evitará a rejeição 1037.

![Imagem 4: Mantenha os campos "Alíquota Referência" , "% Estado" e "% Município" com valores zerados , caso não sejam aplicáveis.…](https://ajuda.sankhya.com.br/hc/article_attachments/41802917544727)

**(6)** Mantenha os campos **"Alíquota Referência"**, **"% Estado"** e **"% Município"** com valores **zerados**, caso não sejam aplicáveis.

**(7)** Salve as alterações. Caso a nota fiscal já esteja confirmada, duplique o documento ou exclua a nota e gere-a novamente para que os impostos sejam recalculados. Em seguida, tente realizar a emissão novamente. Em caso de exclusão da nota, lembre-se de inutilizar a numeração da nota fiscal anterior..
![Imagem 5: (6) Mantenha os campos "Alíquota Referência" , "% Estado" e "% Município" com valores zerados , caso não sejam…](https://ajuda.sankhya.com.br/hc/article_attachments/36690316091287)

<https://dfe-portal.svrs.rs.gov.br/CFF/ClassificacaoTributaria>

**Observações importantes:**

• Durante o **período de teste em 2026**, as alíquotas possuem valores específicos definidos pela legislação. Os valores de IBS e CBS **ainda não serão somados ao total do documento durante o ano de 2026**.
• A partir de **2027**, a CBS vigorará oficialmente (até 2035).
• A partir de **2029**, o IBS vigorará oficialmente (até 2035).
• A partir de **2036**, mantém-se a alíquota definida para o ano anterior.
• Se houver **redução de alíquota** configurada para o IBS Estadual, será necessário informar também o percentual de redução para o IBS Municipal, mesmo que a alíquota municipal seja zero, para evitar a rejeição 1074.

### CAUSA

A rejeição ocorre porque a **Nota Técnica NFe 2025.002** e a **Lei Complementar nº 214/2025** estabelecem alíquotas obrigatórias durante o período de transição da Reforma Tributária. A validação é realizada pela SEFAZ com base nos artigos 343, 344 e 346 da referida lei, sendo uma verificação rigorosa que não permite arredondamentos. Antes da emissão da nota fiscal, o sistema valida se as alíquotas configuradas estão em conformidade com essas regras. Caso haja qualquer divergência, a SEFAZ rejeitará o documento.
