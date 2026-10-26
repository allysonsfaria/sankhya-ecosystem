---
id: "15820042027543"
titulo: "Como o sistema gera a informação do NCM no 0200"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/15820042027543-Como-o-sistema-gera-a-informa%C3%A7%C3%A3o-do-NCM-no-0200"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:56:13Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Impostos", "NCM", "Marque NCM como obrigatório", "Ajuste afeta todos", "Sistema busca automático"]
---

# Como o sistema gera a informação do NCM no 0200

(3)** SOLUÇÃO:**

O campo do NCM, aparentemente não é um campo obrigatório de forma nativa, ele não vem com o sinal de \* e esse sinal pode ser feito, nas configurações da tela, marcando o campo como obrigatório.
Caso deseje poderá acessar essa configuração e desativar a obrigatoriedade do NCM, porém isso afetaria todos os produtos.
 
**![Atenção](https://ajuda.sankhya.com.br/hc/article_attachments/15914770532119) IMPORTANTE:**

O sistema constrói o NCM no 0200 pegando os oito caracteres presentes no cadastro do produto, e se não tiver nada nesse campo, o sistema analisa se no cadastro do produto tem Alíquota de IPI configurada, havendo, ele vai na tela de alíquotas de IPI, e pega os oito primeiros caracteres do campo "Código Fiscal (NPC, NBM)".
