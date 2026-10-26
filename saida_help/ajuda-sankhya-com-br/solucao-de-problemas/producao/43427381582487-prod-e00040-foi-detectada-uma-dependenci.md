---
id: "43427381582487"
titulo: "PROD_E00040: Foi detectada uma dependência cíclica entre o PI Cód. produto XYZ Cód.Processo XYZ e o PI Cód. produto XYZ Cód.Processo XYZ."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43427381582487-PROD-E00040-Foi-detectada-uma-depend%C3%AAncia-c%C3%ADclica-entre-o-PI-C%C3%B3d-produto-XYZ-C%C3%B3d-Processo-XYZ-e-o-PI-C%C3%B3d-produto-XYZ-C%C3%B3d-Processo-XYZ"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-09-11T21:17:09Z"
rotulos: ["Produção - KCS"]
---

# PROD_E00040: Foi detectada uma dependência cíclica entre o PI Cód. produto XYZ Cód.Processo XYZ e o PI Cód. produto XYZ Cód.Processo XYZ.

**MENSAGEM:**

Foi detectada uma dependência cíclica entre o PI Cód. produto XYZ Cód.Processo XYZ e o PI Cód. produto XYZ Cód.Processo XYZ.

Código: PROD\_E00040

**SITUAÇÃO:**

Ocorre ao gerar/lançar uma Ordem de Produção para um **PA (Produto Acabado)** cuja árvore de composição contém um mesmo **PI (Produto Intermediário)** configurado como Sub-ordem em mais de um ramo, sendo que um desses ramos está aninhado dentro de outro PI que também compõe essa mesma árvore, formando uma referência circular entre os dois.

**Exemplo**: Considere que o PA 1 possui o PI 2 como Sub-ordem. Porém, dentro da composição do PI 2, existe o PI 3, que possui o PI 4 como Sub-ordem. Por sua vez, o PI 4 possui novamente o PI 2 em sua composição como Sub-ordem.

Ao chegar novamente ao **PI 2**, o sistema precisa gerar sua Sub-ordem, mas, para isso, volta a explodir sua composição e encontra novamente o **PI 4**, que referencia o **PI 2**. Dessa forma, a estrutura entra em um **ciclo de dependência**, sem conseguir concluir a geração das Ordens de Produção.

**SOLUÇÃO:**

Revisar a árvore de composição do PA e processo produtivo envolvido, e ajustar a configuração de Sub-ordem dos PIs identificados na mensagem de erro, de forma que um mesmo PI não apareça como Sub-ordem em dois ramos que se cruzam (um aninhado dentro do outro) dentro da mesma árvore. 

Normalmente basta reavaliar se ambos os PIs realmente precisam estar marcados como Sub-ordem, ou se um deles deve ser tratado apenas como Estoque (sem gerar OP) em um dos dois pontos.

**CAUSA:**

O erro ocorre quando um mesmo **PI (Produto Intermediário)** está configurado como **Sub-ordem** em mais de um ponto da árvore de composição do mesmo **PA (Produto Acabado)**, sendo que um desses pontos está aninhado dentro de outro PI que também integra essa árvore.

Ao montar a árvore de PIs que precisam ter OP própria gerada, o sistema percorre a composição de forma recursiva: ao encontrar um PI já configurado como Sub-ordem em outro ponto da árvore, ele volta a explodir a composição desse PI como se fosse a primeira vez,  o que leva de novo ao PI que o referencia, que leva de novo ao PI original, e assim sucessivamente.
