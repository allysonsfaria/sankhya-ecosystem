---
id: "360043156434"
titulo: "Sistema está repetindo o controle do item anterior durante o lançamento "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043156434-Sistema-est%C3%A1-repetindo-o-controle-do-item-anterior-durante-o-lan%C3%A7amento"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:34Z"
rotulos: ["#PUBLIFER", "Configuração", "Controle", "Estoque", "Preferências", "Ajustar parâmetro \"REPETECONTANT\" em Preferências", "Sugere controle do item anterior", "Parâmetro ativado sugere controle automaticamente"]
---

# Sistema está repetindo o controle do item anterior durante o lançamento 

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16309812514839) **SOLUÇÃO:**

**(1)** Verifique/ajuste o parâmetro "**REPETECONTANT",** para isso:

**(2)** Acesse a tela [**Preferências**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências);

**(2)** Busque a chave **"REPETECONTANT - Repete último controle digitado?".**

![Imagem 2: (2) Busque a chave "REPETECONTANT - Repete último controle digitado?".](https://ajuda.sankhya.com.br/hc/article_attachments/14340835803159)

**Se estiver Sim**, quando o usuário incluir um item que tenha controle e informá-lo, ao incluir novo item que também tenha controle, o sistema já sugerirá o controle do anterior.

![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16309812521111) **CAUSA:**

Situação ocorre quando ativado o parâmetro REPETECONTANT, fazendo com que ao incluir um item que tenha controle, o próximo item tenha o mesmo controle sugerido.
