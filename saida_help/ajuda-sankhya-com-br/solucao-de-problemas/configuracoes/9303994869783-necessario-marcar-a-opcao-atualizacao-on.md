---
id: "9303994869783"
titulo: "Necessário marcar a opção 'Atualização On-Line'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9303994869783-Necess%C3%A1rio-marcar-a-op%C3%A7%C3%A3o-Atualiza%C3%A7%C3%A3o-On-Line"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:08:53Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Atualização", "CORE_E01260", "Correção de Erro [CORE_E01260]", "Venda por Fórmula"]
---

# Necessário marcar a opção 'Atualização On-Line'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18587309972503) MENSAGEM:**

[CORE\_E01260]  Necessário marcar a opção 'Atualização On-Line'.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18587259373847) SITUAÇÃO:**

Ao tentar alterar um item no lançamento a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18587259386391) CAUSA:**

Ocorre quando se utiliza Venda por Formula de Composição sem antes marcar a fleg de Atualização Online, para utilizar Venda por formula é obrigatório atualização online.

Para mais detalhes sobre a rotina de Venda por Formula de Composição acesse o artigo **[Suporte a Venda de Kits de Produtos.](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111433-Suporte-a-Venda-de-Kits-de-Produtos)**

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18587309994775) SOLUÇÃO:**

Clique "outras opções" dos itens na Central de Vendas, e marcar a opção "Atualização On-line".

![Imagem 5: Clique "outras opções" dos itens na Central de Vendas, e marcar a opção "Atualização On-line".](https://ajuda.sankhya.com.br/hc/article_attachments/18587309999383)

Ao adicionar um produto acabado na grade de itens superior e acionar o botão "Outras Opções...", opção" Revenda (por Fórmula)...", eles serão apresentados no pop-up "Venda por Fórmula de Composição":

Para que esta opção seja apresentada, é necessário que a marcação da opção **"Atualização On-Line"** esteja efetuada, em **"Outras opções"** na parte dos itens. Essa tela permite a alteração das quantidades das matérias-primas, desde que essas alterações respeitem a fórmula de composição do KIT. Considere o seguinte exemplo:

Suponhamos que o produto "KIT Motor de arranque" seja composto por:

- 1 Bobina de Ignição;
- 1 Correia Alternada;
- Impulsor M. Partida.

O total desta fórmula de composição são 3 unidades, logo, no pop-up Venda por Fórmula de Composição, a quantidade dos itens poderá ser alterada desde que a soma dos itens não ultrapasse as 3 unidades da fórmula, podendo ser menor que 3.

**Observação:** A opção de **"Atualização On-Line"** só é apresentada no botão de **"Outras Opções"** caso o parâmetro  **"CONFKITIND"** esteja **DESLIGADO**, quando se trabalha com Kit independente a função de **"Atualização On-Line"** será desativada. É necessário avaliação de impactos para Desligar o parâmetro.
