---
id: "4404428023959"
titulo: " As notas importadas devem possuir o mesmo emitente e destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404428023959--As-notas-importadas-devem-possuir-o-mesmo-emitente-e-destinat%C3%A1rio"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:23:16Z"
rotulos: ["CT-e", "Parceiro", "NF-e", "XML", "Importação", "não apagar", "#publicadoHyago", "#validadoSheyla", "CORE_E02466", "Validação de Emitente e Destinatário", "Conformidade de Emitente e Destinatário", "Consistência entre Emitente e Destinatário", "Erro"]
---

#  As notas importadas devem possuir o mesmo emitente e destinatário

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16347400732439) MENSAGEM**:

 [CORE\_E02466] As notas importadas devem possuir o mesmo emitente, destinatário.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16347400741399) SOLUÇÃO:**

Ao gerar um CT-e deve-se constar os mesmos emitentes e remetentes que a NF-e. Verifique no cabeçalho da notas, os campos:

- **"Parceiro Destinatário" (CODPARCDEST da TGFCAB)**
- **"Parceiro Remetente"** **(CODPARCREMETENTE da TGFCAB)**

Os campos CODPARCDEST e CODPARCREMETENTE devem possuir a mesma informação.

![Imagem 3: Os campos CODPARCDEST e CODPARCREMETENTE devem possuir a mesma informação.](https://ajuda.sankhya.com.br/hc/article_attachments/15330083962903)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16347383044759) CAUSA:**

Existe a seguinte validação de emitente e destinatário para que o XML da NF-e seja importado para inclusão de um CT-e:

- O emitente do XML da NF-e (FornecedorNotaFiscal) deve possuir o mesmo CPF/CNPJ do parceiro Remetente do CT-e;
- O destinatário do XML da NF-e (EmpresaNotaFiscal) deve possuir o mesmo CPF/CNPJ do parceiro Destinatário do CT-e.

Se alguma dessas regras forem violadas, a seguinte mensagem será apresentada: "As notas importadas devem possuir o mesmo emitente, destinatário."
