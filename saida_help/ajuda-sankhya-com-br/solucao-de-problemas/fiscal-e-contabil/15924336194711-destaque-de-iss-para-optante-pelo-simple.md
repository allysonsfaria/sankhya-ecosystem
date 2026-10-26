---
id: "15924336194711"
titulo: "Destaque de ISS para Optante Pelo Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15924336194711-Destaque-de-ISS-para-Optante-Pelo-Simples-Nacional"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:55:54Z"
rotulos: ["ISS", "Configuração", "Parceiro", "Alíquota de ISS", "Simples Nacional", "Impostos", "Alíquota ISS Ret/Simples: Ativação necessária", "Retém ISS: Imposto retido", "Implementação Futura: Nova OS necessária"]
---

# Destaque de ISS para Optante Pelo Simples Nacional

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/15924364049175) SOLUÇÃO:**

Para que o sistema utilize a **"Alíquota ISS Ret/Simples",** acesse a tela **"Parceiros"** (Caminho: Configurações » Cadastros » Parceiros), vá até a aba **"Identificação"** e, no campo **"Tipo",** defina o parceiro como fornecedor.

![Imagem 2: Para que o sistema utilize a "Alíquota ISS Ret/Simples", acesse a tela "Parceiros" (Caminho: Configurações » Cadastros…](https://ajuda.sankhya.com.br/hc/article_attachments/26454582145047)

Em seguida, ainda na tela Parceiros, vá até a aba **"Fiscal"** e ative os campos **"Retém ISS"** e **"Optante pelo Simples Nacional"**

![Imagem 3: Em seguida, ainda na tela Parceiros , vá até a aba "Fiscal" e ative os campos "Retém ISS" e "Optante pelo Simples…](https://ajuda.sankhya.com.br/hc/article_attachments/18787940168087)

Vale destacar que com a opção "Retém ISS" ativa o sistema irá Reter o ISS e não Destacar.

Também é importante ressaltar que, com esse três campos configurados dessa maneira, é possível utilizar a alíquota e alterá-la manualmente. 
 
**Atualmente o sistema não está preparado para o cenário apresentado, conforme segue:**
 
**"O campo 'Alíquota ISS Ret/Simples:' realmente só funciona com a retenção do imposto?**
Atualmente sim, apenas nos casos que existe a retenção a alíquota do parceiro é levada.
 
**Como parametrizar o sistema para que a alíquota simples nacional seja levada em consideração em casos em que a empresa não retém o imposto?**
Atualmente no sistema não é previsto que este comportamento seja realizado. Caso exista necessidade de tal comportamento, deverá ser criada uma nova OS para a implementação junto à Unidade.
