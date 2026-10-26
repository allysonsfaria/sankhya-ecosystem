---
id: "14399788905751"
titulo: "Configurações da aba Matéria Prima nas centrais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14399788905751-Configura%C3%A7%C3%B5es-da-aba-Mat%C3%A9ria-Prima-nas-centrais"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:58:48Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Estoque", "Preferências", "Configurações da Aba Matéria Prima nas Centrais"]
---

# Configurações da aba Matéria Prima nas centrais

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859230591127) SITUAÇÃO:**

Algumas configurações são necessárias caso queira que apareça ou iniba a aba matéria prima nas centrais.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859230592663)SOLUÇÃO:**

Para que o painel seja apresentado nas Centrais de Notas, na grade de **"Itens"**, habilite os parâmetros:

- **"Tem aba Mat.Prima na Transferência? - TEMMPTRAN";**
- **"Tem aba Mat.Prima na requisição? - TEMMPREQ";**
- **"Tem aba mat.prima na central atend. ao Cliente? - TEMMPVENDA";**
- **"Tem aba mat.prima na central atendimento ao Forn.? - TEMMPCOMPRA";**

Caso o parâmetro **"Configuração para Kit Independente - CONFKITIND"** esteja ligado, o sistema desconsidera o parâmetro TEMMPVENDA. Então, caso trabalhe com kit independente, mas não queira a aba **"Matéria-prima"** exibindo nas centrais quando não usa um produto com componente, ligue o parâmetro abaixo.

- **"Mostrar grid de mat. prima somente quando existir - SHOWGRIDMATPRI"**.

Dessa forma, a aba Matéria-prima só será exibida selecionando os produtos que tem componentes em seu cadastro na grade de itens.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16859267797271) CAUSA:**

Ocorre por falta de configuração.
