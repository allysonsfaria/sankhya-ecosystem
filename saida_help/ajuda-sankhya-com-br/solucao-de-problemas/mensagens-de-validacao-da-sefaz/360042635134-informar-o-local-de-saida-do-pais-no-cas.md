---
id: "360042635134"
titulo: "Informar o local de saída do Pais no caso da exportação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042635134-Informar-o-local-de-sa%C3%ADda-do-Pais-no-caso-da-exporta%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:07:53Z"
rotulos: ["ERRONF", "#RevisadoGui", "Configuração", "NF-e", "Portal de Vendas", "XML", "SEFAZ", "355", "Falta de informações no XML de exportação", "Rejeição [355] - Local de saída do País não informado", "Preencher \"Local do Embarque\" e \"UF Local Embarque\"", "Exportacao"]
---

# Informar o local de saída do Pais no caso da exportação

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16505572750999) **MENSAGEM:**

[355 - Rejeição]: Informar o local de saída do Pais no caso da exportação.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16505572752407) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Comercial » Consulta » Portal de Vendas](https://ajuda.sankhya.com.br/hc/article_attachments/16505572754327) Acesse: Comercial » Consulta » Portal de Vendas

![Imagem 4: Acesse a NF-e e preencha os campos: " Local do Embarque" e " UF Local Embarque" :](https://ajuda.sankhya.com.br/hc/article_attachments/16505572755735) Acesse a NF-e e preencha os campos: **"Local do Embarque"** e **"UF Local Embarque"**:

![Imagem 5: Acesse a NF-e e preencha os campos: " Local do Embarque" e " UF Local Embarque" :](https://ajuda.sankhya.com.br/hc/article_attachments/14600878894743)

- Geralmente os campos ficam dispostos na aba: Transporte do Rodapé da nota, mas caso não esteja disponível, acesse a tela: **"Comercial"** » Configuração » Configurador de Layout da Nota e faça o ajuste no respectivo Layout, que é usado para o Tipo de Movimento de Venda. Insira os dois campos em qualquer local do Layout da Nota, para que seja preenchido sempre que houver a necessidade.

![Imagem 6: Após os ajustes, salve o cabeçalho da nota e gere o lote novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/16505572758295) Após os ajustes, salve o cabeçalho da nota e gere o lote novamente.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16505602040855) CAUSA:**

Ocorre quando a NF-e é do tipo exportação no qual é gerado no XML do Grupo de Exportação  (<exporta>), e as informações de Local e UF do Embarque, não estão devidamente preenchidos.
