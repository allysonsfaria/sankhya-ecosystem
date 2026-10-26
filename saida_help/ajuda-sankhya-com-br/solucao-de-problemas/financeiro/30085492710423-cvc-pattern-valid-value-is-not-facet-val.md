---
id: "30085492710423"
titulo: "cvc-pattern-valid: VALUE '' IS not facet-valid with respect to pattern '[0-9]{2,16}' for type'TIe'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30085492710423-cvc-pattern-valid-VALUE-IS-not-facet-valid-with-respect-to-pattern-0-9-2-16-for-type-TIe"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-09-01T19:46:12Z"
rotulos: ["Configuração", "Parceiro", "SEFAZ", "Impostos", "GNRE", "Passos para resolver", "Razão do erro", "Detalhe do erro", "cvc-pattern-valid: VALUE '' IS not facet-valid with respect to pattern '[0-9]{216}' for type'TIe'."]
---

# cvc-pattern-valid: VALUE '' IS not facet-valid with respect to pattern '[0-9]{2,16}' for type'TIe'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30085492706071) **MENSAGEM:**

Erro na recepção do arquivo de lote.
Causa do erro: cvc-pattern-valid: VALUE '' IS not facet-valid with respect to pattern '[0-9]{2,16}' for type'TIe'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30085485560855)SOLUÇÃO:**

Acesse o cadastro de **Parceiros** (Configurações » Cadastros » Parceiros) e verifique se o campo "Insc. Estadual / Identidade" está preenchido com o IE correto. Caso seja Consumidor Final Não Contribuinte, é necessário que seja inserido no campo, a informação **ISENTO**.

![Imagem 3: Acesse o cadastro de Parceiros (Configurações » Cadastros » Parceiros) e verifique se o campo "Insc. Estadual /…](https://ajuda.sankhya.com.br/hc/article_attachments/30091472803095)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30085492708759)CAUSA:**

Ocorre ao tentar enviar um lote GNRE e o campo IE (Insc. Estadual / Identidade) está vazio ou incorreto.
