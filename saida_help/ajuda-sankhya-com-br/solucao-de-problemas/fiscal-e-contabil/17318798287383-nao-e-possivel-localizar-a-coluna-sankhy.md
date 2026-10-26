---
id: "17318798287383"
titulo: "Não é possível localizar a coluna \"sankhya\" ou a função ao agregação definida pelo usuário \"sankhya.SNK_GET_UNDALT0220\", ou o nome é ambíguo."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17318798287383-N%C3%A3o-%C3%A9-poss%C3%ADvel-localizar-a-coluna-sankhya-ou-a-fun%C3%A7%C3%A3o-ao-agrega%C3%A7%C3%A3o-definida-pelo-usu%C3%A1rio-sankhya-SNK-GET-UNDALT0220-ou-o-nome-%C3%A9-amb%C3%ADguo"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:53:25Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "EFD", "Preferências", "Função 'SNK_GET_UNDALT0220' não encontrada ou ambígua.", "Crie a função conforme regras do fornecedor.", "Suporte pode ser interno ou consultor", "Erro"]
---

# Não é possível localizar a coluna "sankhya" ou a função ao agregação definida pelo usuário "sankhya.SNK_GET_UNDALT0220", ou o nome é ambíguo.

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17323613870743) MENSAGEM:**

Não é possível localizar a coluna "sankhya" ou a função ao agregação definida pelo usuário "sankhya.SNK\_GET\_UNDALT0220", ou o nome é ambíguo.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17318790673047)SOLUÇÃO:**

![Imagem 3: É necessário que a função 'SNKGETUNDALT0220' seja criada/personalizada com a implementação das regras passadas pelo…](https://ajuda.sankhya.com.br/hc/article_attachments/17323597581335) É necessário que a função 'SNKGETUNDALT0220' seja criada/personalizada com a implementação das regras passadas pelo fornecedor.

![Imagem 4: Atualmente, a criação da função é realizada com apoio de um consultor de implantação da unidade ou internamente caso a…](https://ajuda.sankhya.com.br/hc/article_attachments/17323597590039) Atualmente, a criação da função é realizada com apoio de um consultor de implantação da unidade ou internamente caso a empresa possua uma equipe de TI interna.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17323597595159) CAUSA:**

Ocorre quando a opção 'Gerar registro 0220 utilizando UND enviada pelo Fornecedor' está marcada nas preferências da empresa, aba EFD" e a função 'SNKGETUNDALT0220' não é criada ou parametrizada corretamente a mensagem é apresentada.
