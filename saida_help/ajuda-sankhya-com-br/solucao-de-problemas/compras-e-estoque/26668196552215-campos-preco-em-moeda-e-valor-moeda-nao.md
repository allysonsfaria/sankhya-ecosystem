---
id: "26668196552215"
titulo: "Campos 'Preço em moeda' e 'Valor Moeda' não editáveis na cotação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26668196552215-Campos-Pre%C3%A7o-em-moeda-e-Valor-Moeda-n%C3%A3o-edit%C3%A1veis-na-cota%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:40:53Z"
rotulos: ["Configuração", "Cotação", "Parceiro", "Moeda", "TRABMOECOT", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Preço em moeda", "Trabalhar moeda cotacao", "Moeda cotação", "Moeda Cotacao", "Moedas p/ Portal cot.", "Valor Moeda", "Moeda não existe", "Moeda não existe ou não pode ser usado aqui", "Erro"]
---

# Campos 'Preço em moeda' e 'Valor Moeda' não editáveis na cotação

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26672669861399) **SITUAÇÃO:**

Ao ativar a preferência "**TRABMOECOT - Trabalhar com Moedas na Cotação?",** os campos **"Preço em moeda"** e **"Valor Moeda"** são apresentados na cotação, mas não permite edição.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/26668196546455)SOLUÇÃO:**

Para possibilitar o preenchimento dos campos mencionados, primeiro adicione uma moeda na grade.

Se não houver nenhuma moeda disponível para inserção, isso indica que o parceiro fornecedor não possui uma moeda vinculada ao seu cadastro. Podendo ser apresentado o erro **'Moeda não existe ou não pode ser usado aqui: PK[1].'**

Acesse a tela de **"Parceiros"** (Configurações » Cadastros » Parceiros), abra o cadastro do parceiro fornecedor e, na aba **"Moedas p/ Portal cot."**, insira as moedas que poderão ser utilizadas para esse fornecedor.

Após o cadastro, retorne à cotação e será possível inserir uma moeda. Após a inserção da moeda, os campos estarão editáveis conforme o esperado.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26668259376535)CAUSA:**

Ocorre quando não existe uma moeda vinculada ao parceiro fornecedor da cotação.
