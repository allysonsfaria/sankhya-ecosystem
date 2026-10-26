---
id: "360043101553"
titulo: "The content of element 'ICMS' is not complete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043101553-The-content-of-element-ICMS-is-not-complete"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:08:36Z"
rotulos: ["ERRONF", "Configuração", "Fiscal", "NF-e", "ICMS", "Impostos", "Dados Incompletos no Elemento 'ICMS'", "Erro"]
---

# The content of element 'ICMS' is not complete

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16482554952855) MENSAGEM:**

vc-complex-type.2.4.b: The content of element 'ICMS' is not complete. One of '{"http://www.portalfiscal.inf.br/nfe":ICMS00, "http://www.portalfiscal.inf.br/nfe":ICMS10, "http://www.portalfiscal.inf.br/nfe":ICMS20, "http://www.portalfiscal.inf.br/nfe":ICMS30, "http://www.portalfiscal.inf.br/nfe":ICMS40, "http://www.portalfiscal.inf.br/nfe":ICMS51, "http://www.portalfiscal.inf.br/nfe":ICMS60, "http://www.portalfiscal.inf.br/nfe":ICMS70, "http://www.portalfiscal.inf.br/nfe":ICMS90, "http://www.portalfiscal.inf.br/nfe":ICMSPart, "http://www.portalfiscal.inf.br/nfe":ICMSST, "http://www.portalfiscal.inf.br/nfe":ICMSSN101, "http://www.portalfiscal.inf.br/nfe":ICMSSN102, "http://www.portalfiscal.inf.br/nfe":ICMSSN201, "http://www.portalfiscal.inf.br/nfe":ICMSSN202, "http://www.portalfiscal.inf.br/nfe":ICMSSN39, "http://www.portalfiscal.inf.br/nfe":ICMSSN900}' is expected.
erro.handshake=true

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16482578532759) SOLUÇÃO:**

Para correção deste erro, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/article_attachments/16482554963479) Acesse: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS

Identifique a regra de ICMS que incidiu na NF-e, acesse o cadastro de Alíquota e verifique o CST na aba: **"Geral"** e o CSOSN na aba: **"Simples Nacional".**

Empresas do Simples Nacional precisam destacar o CSOSN em suas NF-e's e existe uma relação/combinação de CST x CSOSN.

![Imagem 4: Contacte a área Fiscal/Contábil da Empresa para que seja informado corretamente a CST e CSOSN.](https://ajuda.sankhya.com.br/hc/article_attachments/16482578541335) Contacte a área Fiscal/Contábil da Empresa para que seja informado corretamente a CST e CSOSN.

![Imagem 5: Após os ajustes, inutilize a nota e fature novamente. Certifique os ajustes anteriormente feitos e gere Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16482578545559) Após os ajustes, inutilize a nota e fature novamente. Certifique os ajustes anteriormente feitos e gere Lote.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16482554972951) CAUSA:**

Esta mensagem pode ocorrer quando o CST e o CSOSN informados nos itens não são compatíveis ou se um deles não foi preenchido.
