---
id: "360044613434"
titulo: "Produtos Compatíveis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613434-Produtos-Compat%C3%ADveis"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:14:57Z"
rotulos: ["Produtos", "AJUDA DO SKW", "manual", "Configuração", "WMS", "Estoque", "Compatíveis", "br.com.sankhya.wms.cad.produtoscompativeis", "Produtos Compatíveis manual", "Configuração de Compatibilidade de Produtos no WMS", "Squad WMS"]
---

# Produtos Compatíveis

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311593832471) Módulo: WMS > Cadastros
```

---

Através desta tela, você configura a compatibilidade dos produtos para armazenamento. Determine um produto e efetue a seleção de quais outros produtos podem ser armazenados juntamente com o mesmo.

![Imagem 2: Através desta tela, você configura a compatibilidade dos produtos para armazenamento. Determine um produto e efetue a…](https://ajuda.sankhya.com.br/hc/article_attachments/360086476713)

Esta é uma tela dividida em duas seções, onde você informa a **"Ligação de Origem"** e a **"Ligação de Destino"** do produto, respectivamente.

Na seção Ligação de Origem, são apresentados 3 (três) campos cujo o preenchimento é feito de acordo com a regra de armazenamento a ser configura. Sendo eles:

- Cód. Produto (Origem);
- Cód. Grupo (Origem);
- Marca (Origem).

Na seção Ligação de Destino, determine os produtos compatíveis ou não com os produtos informados anteriormente. Informe os seguintes dados:

- Cód. Produto (Destino);
- Cód. Grupo (Destino);
- Marca (Destino);
- **Tipo:** Determine neste campo, a ligação pertinente à armazenagem do produto de destino, ou seja, se será **"Permitido"** ou **"Negado"** que o produto seja armazenado junto ao Produto (Origem).

O funcionamento desta tela é simples; suponhamos que seja informado um produto X qualquer no Cód. Produto (Origem); no Cód. Grupo (Destino) informou-se um grupo Y (pode ser diferente ou não do grupo do produto de origem) e definiu-se o campo Tipo com a alternativa Permitido. Nesta situação, teremos as seguintes hipóteses:

1. Será autorizado que todos os produtos pertencentes ao grupo Y, sejam armazenados juntamente com o produto X;
2. Os produtos pertencentes ao grupo Y, só poderão ser armazenados juntamente com o produto X;
3. Os produtos pertencentes ao grupo Y, poderão ser armazenados sozinhos;
4. Os produtos x, poderão ser armazenados sozinhos.

Caso o campo Tipo seja definido como Negado, teremos as seguintes possibilidades:

1. Será proibido que todos os produtos pertencentes ao grupo Y, sejam armazenados juntamente com o produto X;
2. Os produtos pertencentes ao grupo Y, poderão ser armazenados com outros produtos;
3. Os produtos pertencentes ao grupo Y, poderão ser armazenados sozinhos;
4. Os produtos x, poderão ser armazenados sozinhos.

**Importante:** a validação de compatibilidade levará, inicialmente, em consideração a negativação do produto, ou seja, em um endereço que contém cinco produtos positivos e um negativo, o sistema não irá efetuar o armazenamento dos mesmos. Além disto, os produtos com vínculo positivo só poderão ser armazenados entre si.
