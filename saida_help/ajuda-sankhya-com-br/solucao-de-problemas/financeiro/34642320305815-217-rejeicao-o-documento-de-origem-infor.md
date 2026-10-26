---
id: "34642320305815"
titulo: "217  Rejeição: O Documento de Origem informado não e usado pela Receita informada na UF favorecida"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34642320305815-217-Rejei%C3%A7%C3%A3o-O-Documento-de-Origem-informado-n%C3%A3o-e-usado-pela-Receita-informada-na-UF-favorecida"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-09-30T14:21:01Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Tipo de Documento", " Portal GNRE", "217  Rejeição", "Documento de Origem informado", "não e usado pela Receita informada na UF favorecida", "Tipo da Informação"]
---

# 217  Rejeição: O Documento de Origem informado não e usado pela Receita informada na UF favorecida

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/34642320263319) **MENSAGEM:**

217  Rejeição: O Documento de Origem informado não e usado pela Receita informada na UF favorecida

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/34642320267543)SOLUÇÃO:**

**(1)** Acesse a tela **“Estados” (**Configurações» Cadastros» Endereços» Estados) e localize o Estado de destino para o qual a GNRE está sendo gerada.

**(2)** Na aba **''Geral'' (**Configurações» Cadastros» Endereços» Estados) identifique o campo**''Código da Receita''** utilizado no envio.

**(3)** Verifique se os campos ''**Tipo de Documento''** e ''**Tipo da Informação''**estão preenchidos conforme as exigências do [**Portal GNRE**](https://www.gnre.pe.gov.br:444/gnre/portal/consultarTabelas.jsp) para o código de receita informado.

![Imagem 3: (3) Verifique se os campos '' Tipo de Documento'' e '' Tipo da Informação'' estão preenchidos conforme as exigências do…](https://ajuda.sankhya.com.br/hc/article_attachments/34642320280471)![Imagem 4: (3) Verifique se os campos '' Tipo de Documento'' e '' Tipo da Informação'' estão preenchidos conforme as exigências do…](https://ajuda.sankhya.com.br/hc/article_attachments/34642315147159)

**Dica:** consulte a documentação oficial do Portal GNRE para confirmar quais tipos são aceitos para cada receita.

**(4)** Realize os ajustes necessários no cadastro do Estado no campo**''Tipo de Documento''**.

**(5)** Após as correções, gere um novo lote e reenvie ao portal da GNRE.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/34642320290199)CAUSA:**

Esta rejeição ocorre quando o valor informado no campo **''Tipo de Documento'** não está preenchido conforme as normas estabelecidas para o Estado de destino no Portal GNRE.
