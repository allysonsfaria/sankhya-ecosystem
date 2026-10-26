---
id: "9324003622295"
titulo: "Grupo de documentos informado inválido para remetente que emite NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9324003622295-Grupo-de-documentos-informado-inv%C3%A1lido-para-remetente-que-emite-NF-e"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:38Z"
rotulos: ["CT-e", "Configuração", "NF-e", "SEFAZ", "TOP", "não apagar", "540", "Problema de Grupo de Documentos em CT-e", "Documentos Eletrônicos"]
---

# Grupo de documentos informado inválido para remetente que emite NF-e

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16363646699031) MENSAGEM**:

540 - Grupo de documentos informado inválido para remetente que emite NF-e;

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16363678572695) SOLUÇÃO:**

Verifique as configurações em:

**"Tipos de Operação - TOP"**

Aba: **"CT-e/MD-e"**

Observe se está preenchido como:

- Tipo do CT-e (tpCTe) **igual** à "0 - Normal" ou "3 - Substituição";
- Tipo de Serviço (tpServ) **diferente**de "3 - Redespacho Intermediário" ou "4 - Serviço Vinculado";
- Modal **diferente** de Dutoviário;

![Grupo](https://ajuda.sankhya.com.br/hc/article_attachments/15822132876823)

- UF de início (UFIni) da prestação **diferente** da UF do término da prestação (UFFim);
- CNPJ do remetente do CT-e habilitado no CNE para e missão de Nota Fiscal Eletrônica;

- Grupo de Documentos com NF em papel (modelo 1/1A).

No Rodapé da nota na aba (Notas do Conhecimento de Transporte): informe o modelo de documento 55, pois o modelo 1/1A não é um modelo válido.

![Grupo](https://ajuda.sankhya.com.br/hc/article_attachments/15822132879255)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16363653499927)CAUSA:**

Quando for emitido um CT-e com as seguintes informações:

- Tipo do CT-e (tpCTe) **igual** à "0 - Normal" ou "3 - Substituição";
- Tipo de Serviço (tpServ) **diferente**de "3 - Redespacho Intermediário" ou "4 - Serviço Vinculado";
- Modal **diferente** de Dutoviário;
- UF de início (UFIni) da prestação **diferente** da UF do término da prestação (UFFim);
- CNPJ do remetente do CT-e habilitado no CNE para e missão de Nota Fiscal Eletrônica;
- Grupo de Documentos com NF em papel (modelo 1/1A).

Será retornado rejeição "540 - Grupo de documentos informado inválido para remetente que emite NF-e".

**Exemplo:**

Foi emitido um CT-e de Tipo "0 - Normal", com Tipo de Serviço "1 - Normal", com tipo do Modal como Rodoviário, com a UF de início da prestação PR (Paraná) e UF do término da prestação SP (São Paulo), com Remetente obrigado a emitir Nota Fiscal Eletrônica (NF-e) e com o Grupo de Documentos com NF em papel (modelo 1/1A). Nessa situação, a NF-e será rejeitada pelo motivo 540.
