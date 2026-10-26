---
id: "9150588390935"
titulo: "O que é JSON de Nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9150588390935-O-que-%C3%A9-JSON-de-Nota"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T15:10:05Z"
rotulos: ["XML", "Importação", "Nota Fiscal", "não apagar", "Sankhya Checkout", "#criadoFran", "Verifique JSON em \"Administração do Checkout\" no Sankhya Om", "Edite JSON na mesma tela com cautela", "JSON: formato texto para armazenamento e transmissão", "JSON"]
---

# O que é JSON de Nota?

**(1)** JSON (JavaScript Object Notation) é um modelo para armazenamento e transmissão de informações no formato texto. Apesar de muito simples, tem sido bastante utilizado por aplicações Web devido a sua capacidade de estruturar informações de uma forma bem mais compacta do que a conseguida pelo modelo XML, tornando mais rápido o parsing dessas informações.

#### Imagem 1: Como verificar o Json de um lançamento realizado no Sankhya Checkout? Como verificar o Json de um lançamento realizado no Sankhya Checkout?

Na tela Administração do Checkout no Sankhya Om

![Imagem 2: Na tela Administração do Checkout no Sankhya Om](https://ajuda.sankhya.com.br/hc/article_attachments/9150466836247)

- Aba **'Importação de Movimentações'**, selecione o registro que encontra-se preso na tela, clique em **"Inspecionar JSON";**
- Será possível visualizar as informações pertinentes ao lançamento;
- Caso queira verificar a nível de banco de dados, é possível visualizar na **tabela TFXITV**

#### Imagem 3: E se houver a necessidade de Editar o Json? E se houver a necessidade de Editar o Json?

Os campos disponíveis para edição são apresentados na tela **"Administração do Checkout no Sankhya Om",** aba **"Importação de Movimentações",** opção **"Editar Json"**.

![Imagem 4: Os campos disponíveis para edição são apresentados na tela "Administração do Checkout no Sankhya Om", aba "Importação…](https://ajuda.sankhya.com.br/hc/article_attachments/16674641941015)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16674639077399) OBSERVAÇÃO:**

Campos não existentes para edição na Administração do Checkout deverão ser bem avaliados quanto a sua alteração, já que a mesma é a nível de banco de dados.
