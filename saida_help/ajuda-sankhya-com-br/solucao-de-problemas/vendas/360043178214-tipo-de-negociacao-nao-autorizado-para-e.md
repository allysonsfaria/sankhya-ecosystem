---
id: "360043178214"
titulo: "Tipo de negociação não autorizado para este cliente! Ver Grupo autorização. Parceiro: X Tipo Negociação: Y"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178214-Tipo-de-negocia%C3%A7%C3%A3o-n%C3%A3o-autorizado-para-este-cliente-Ver-Grupo-autoriza%C3%A7%C3%A3o-Parceiro-X-Tipo-Negocia%C3%A7%C3%A3o-Y"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:09Z"
rotulos: ["#criadoRoger", "CORE_E01861", "Configuração", "Parceiro", "Crédito", "Tipos de Negociação", "Autorização incompatível", "Verificar e ajustar grupos", "Redigitar parceiro", "Comercial"]
---

# Tipo de negociação não autorizado para este cliente! Ver Grupo autorização. Parceiro: X Tipo Negociação: Y

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16162811503895) MENSAGEM:**

[CORE\_E01861] Tipo de negociação não autorizado para este cliente! Ver Grupo autorização. Parceiro: X Tipo Negociação: Y

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16162811505559) SITUAÇÃO:**

Ao tentar efetuar o lançamento de um documento, ocorre a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16162796756375) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse a tela " Parceiros " (Caminho de acesso: Configurações » Cadastros) e na aba "Crédito" verifique:](https://ajuda.sankhya.com.br/hc/article_attachments/16162811510295) Acesse a tela **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** (Caminho de acesso: Configurações » Cadastros) e na aba **"Crédito"** verifique:

**(2)** Campo **"Grupo de Autorização":** Verifique quais são os grupos configurados

![Imagem 5: Acesse a tela " Tipos de Negociação " (Caminho de acesso: Comercial » Arquivo » Cadastros) e na aba "Características"…](https://ajuda.sankhya.com.br/hc/article_attachments/16162796760087) Acesse a tela **"[Tipos de Negociação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o)"** (Caminho de acesso: Comercial » Arquivo » Cadastros) e na aba **"Características"** verifique:

**(2)** Campo **"Grupo de Autorização"**: Verifique o Grupo de Autorização do Tipo de Negociação

![Imagem 6: Após os ajustes, redigite parceiro no documento para conseguir confirmar o documento.](https://ajuda.sankhya.com.br/hc/article_attachments/16162811514391) Após os ajustes, redigite parceiro no documento para conseguir confirmar o documento.

(1)** EXEMPLO:**

Tipo de Negociação X, o Grupo de Autorização é **A** e o Grupo de Autorização do Parceiro Y é **A, B, C**, significa que é possível usar o Tipo de Negociação X com o parceiro Y.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16162811518231) CAUSA:**

Ocorre quando o Grupo de Autorização do Parceiro é diferente do Grupo de Autorização do Tipo de Negociação.

**A Regra é:** Vários Grupos de Autorização no Parceiro e um único grupo de Autorização para cada Tipo de Negociação. Então, caso precise autorizar diferentes tipos de negociação, informe vários grupos de autorização no Parceiro sempre separado por vírgula.

![Imagem 8: A Regra é: Vários Grupos de Autorização no Parceiro e um único grupo de Autorização para cada Tipo de Negociação.…](https://ajuda.sankhya.com.br/hc/article_attachments/14705803664535)
