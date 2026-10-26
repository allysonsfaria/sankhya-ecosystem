---
id: "360042870594"
titulo: "Os produtos desta nota não permitem desconto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042870594-Os-produtos-desta-nota-n%C3%A3o-permitem-desconto"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:27Z"
rotulos: ["Produtos", "Configuração", "NF-e", "Impostos", "CORE_E02700", "COM_E00223", "Produtos da nota não permitem desconto", "Ajuste parâmetros e percentual de desconto", "Produtos não configurados para desconto", "Erro"]
---

# Os produtos desta nota não permitem desconto

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16114018040215) MENSAGEM:**

[CORE\_E02700] Os produtos desta nota não permitem desconto.

[COM\_E00223]  Os produtos desta nota não permitem desconto

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16114018044695) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16113986801815) Acesse: Configurações » Avançado » Preferências

**(2)** Analise a configuração atual dos 3 parâmetros abaixo:

(3)**"DISTJDCONF - Distribuir desc. na confirmação da nota?"**

(3)**"DISTDESCNFE - Distribuir desc.na confirmação da NFE?"**

(3)**"VALDESCMAX - Valida desconto máximo."**

Com os parâmetros "**DISTJDCONF ou DISTDESCNFE"** ligados, o sistema tentará distribuir o desconto do rodapé da nota entre os itens, obedecendo o % de desconto máximo do cadastro de produtos.

Caso exceda e o parâmetro VALDESCMAX esteja **desligado,**a mensagem será apresentada, sendo necessário aplicar as duas soluções listadas nos itens 3 e 4 abaixo:

![Imagem 4: Ajuste o parâmetro VALDESCMAX para diferente de "Não Valida" .](https://ajuda.sankhya.com.br/hc/article_attachments/16113986812823) Ajuste o parâmetro VALDESCMAX para **diferente** de **"Não Valida"**.

![Imagem 5: No cadastro de " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) para todos os itens da…](https://ajuda.sankhya.com.br/hc/article_attachments/16114018075031) No cadastro de **"[Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-)"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) para todos os itens da nota, ajuste a informação contida no campo **"%Desconto Máximo",** aba **"Venda"** para um percentual que atenda a necessidade de aplicação de desconto atual.

![Imagem 6: No cadastro de " Produtos " (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos) para todos os itens da…](https://ajuda.sankhya.com.br/hc/article_attachments/14557321385879)

![Imagem 7: Por fim, proceda com uma nova tentativa de confirmação da respectiva NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16114018079511) Por fim, proceda com uma nova tentativa de confirmação da respectiva NF-e.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16113986824599) CAUSA:**

Ocorre quando o(s) produto(s) não estão devidamente configurados para receber desconto, distribuídos pela confirmação da nota.
