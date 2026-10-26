---
id: "35644814485783"
titulo: "Uso do local \"Em Trânsito\" em transferências de imobilizado entre empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35644814485783-Uso-do-local-Em-Tr%C3%A2nsito-em-transfer%C3%AAncias-de-imobilizado-entre-empresas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-15T17:55:21Z"
rotulos: ["Configuração", "Fiscal", "TOP", "Local de Destino", "Local de Origem", "Transferência", "Em Trânsito", "imobilizado", "Uso do local", "em transferências", "entre empresas"]
---

# Uso do local "Em Trânsito" em transferências de imobilizado entre empresas

**MENSAGEM:**

Recomenda-se utilizar o local “Em Trânsito” nas transferências de imobilizado entre empresas para evitar que o bem seja considerado disponível antes da chegada física.

**SITUAÇÃO:**

Ao registrar a nota de transferência diretamente para o local de destino, o sistema passa a considerar o bem como disponível na empresa de destino antes da chegada física, gerando inconsistência entre o controle físico e o controle fiscal.

Utilize o local **"Em Trânsito"** como etapa intermediária para representar o período de transporte e evitar que o bem seja usado ou localizado incorretamente.

**SOLUÇÃO:**

**(1)** Registre a remessa entre empresas:

- Abra o documento de transferência;
- Informe o **"Local de Origem"** com o local atual do bem;
- Informe o **"Local de Destino"** como **"Em Trânsito";**
- Selecione a TOP com **"Atualização do Bem"** adequada (ex.: Transf. Saída/Remessa) e preencher as configurações fiscais conforme a operação.

**(2)** Registre a chegada física (transferência de local):

- Abra o documento de transferência de local;
- Informe o **"Local de Origem"** como **"Em Trânsito";**
- Informe o **"Local de Destino"** como o local definitivo na empresa de destino;
- Use a TOP que atualize o local do bem sem efeito fiscal, se aplicável.

**(3)** Valide o processo:

- Confirme que a nota de remessa representa a saída fiscal e que o bem ficou com local “Em Trânsito”;
- Confirme que a nota de chegada atualiza o local físico do bem para o destino definitivo;
- Confira a ficha patrimonial e os registros fiscais para garantir consistência.

#### Exemplo: Nota de Transferência

![Imagem 1: Exemplo: Nota de Transferência](https://ajuda.sankhya.com.br/hc/article_attachments/36020358617623)

#### Exemplo: Nota de Movimentação de Local

![Imagem 2: Exemplo: Nota de Movimentação de Local](https://ajuda.sankhya.com.br/hc/article_attachments/36020358621463)

#### Exemplo: Ficha Patrimonial

![Imagem 3: Exemplo: Ficha Patrimonial](https://ajuda.sankhya.com.br/hc/article_attachments/36020358623639)

**CAUSA:**

O lançamento direto para o local de destino faz com que o sistema interprete que o bem já está fisicamente disponível na empresa de destino. Isso ocorre por ausência da etapa intermediária que represente o transporte físico, gerando divergência entre disponibilidade física e controle fiscal.
