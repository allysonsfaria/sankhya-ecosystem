---
id: "14466121818519"
titulo: "Parceiro já é outro vendedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14466121818519-Parceiro-j%C3%A1-%C3%A9-outro-vendedor"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:41Z"
rotulos: ["Configuração", "Parceiro", "Vendas", "CORE_E03751", "Parceiro vinculado a um vendedor", "Parceiro já é de outro vendedor", "Habilitar parâmetro PERMNVENDPARC", "Parceiro já vinculado a outro vendedor", "Ativar o parâmetro PERMNVENDPARC", "Parâmetro não habilitado para múltiplos vendedores", "Erro"]
---

# Parceiro já é outro vendedor

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16531722919575) MENSAGEM:**

[CORE\_E03751]: Parceiro já é outro vendedor.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16531722924951)**SOLUÇÃO:**

O parâmetro **"Permitir relação 1xN entre parceiros e vendedores - PERMNVENDPARC"** permitirá que um mesmo parceiro seja incluído à vários vendedores, tanto nesta tela quanto na tela **["Cadastro de Parceiros"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros)**, aba [**"Vendedor/Comprador"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abavendedorcompradorhttps://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abavendedorcomprador) (habilitada quando o Parceiro é marcado como "Vendedor" na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abaidentificao) da referida tela). Desta forma, quando este encontrar-se habilitado, não será realizada a validação no que diz respeito à existência de vendedor já vinculado ao parceiro escolhido.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16531722926871)**CAUSA:**

Ocorre quando deseja que um mesmo parceiro seja incluído a vários vendedores e o parâmetro Permitir relação 1xN entre parceiros e vendedores - PERMNVENDPARC não está habilitado.
