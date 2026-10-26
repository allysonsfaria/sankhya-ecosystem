---
id: "360044615873"
titulo: "Volume alternativo não pode ser alterado. Já existem lançamentos para este produto/unidade"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044615873-Volume-alternativo-n%C3%A3o-pode-ser-alterado-J%C3%A1-existem-lan%C3%A7amentos-para-este-produto-unidade"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:41Z"
rotulos: ["#PUBLIFER", "CORE_E00471", "Produtos", "Configuração", "Fiscal", "XML", "Estoque", "CORE_E00471-Restrição de Alteração de Volume Alternativo", "Erro"]
---

# Volume alternativo não pode ser alterado. Já existem lançamentos para este produto/unidade

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16593748431767) MENSAGEM:**

[CORE\_E00471]: Volume alternativo não pode ser alterado. Já existem lançamentos para este produto/unidade. Esta operação não é permitida devido ao impacto no Sped Fiscal.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16593773957911) SOLUÇÃO:**

Visto que não é permitido alterar informações de volume alternativo, quando já existem movimentações no sistema para o respectivo produto/unidade a ser alterado, avalie entre as possibilidade destacadas abaixo, qual delas melhor se adequará a sua empresa. Para tal, realize sintonias internas junto ao implantador do sistema e/ou usuários certificados com conhecimento no processo.

**![Imagem 3: Excluir os lançamentos registrados com o respectivo produto/unidade:](https://ajuda.sankhya.com.br/hc/article_attachments/16593773960471) Excluir os lançamentos registrados com o respectivo produto/unidade:**

**(1)** Caso as movimentações geradas para o respectivo produto/unidade sejam movimentos que permitam exclusão, sem impactos para a empresa, proceda com a mesma.

**(1)** Realizada a exclusão dos lançamentos que utilizaram tal unidade, será possível realizar os ajustes desejados no cadastro da 'Unidade Alternativa'. Após isso refaça os lançamentos.

**(1)** Esteja ciente que essa solução é recomendada para registros com poucas movimentações, como por exemplo uma única nota de compra.

**![Imagem 4: Inative o produto atual e realize o cadastro de um novo produto:](https://ajuda.sankhya.com.br/hc/article_attachments/16593773965975) Inative o produto atual e realize o cadastro de um novo produto:**

Caso essa alteração seja necessária após registro de movimentações que não podem ser excluídos, o sistema de fato não permitirá as alterações, por questões fiscais. Dessa forma:

**(1)** Realize um ajuste de saída do estoque atual desse produto, em seguida inative o mesmo.

**(1)** Realize o **cadastro de um novo produto que substitua esse**, informando os cadastros de unidade corretamente. Realize um ajuste de entrada de estoque referente ao produto inativado.

**(1)** Para essa possível solução, atente-se ao fato de análises gerenciais referente ao produto se tornarão "incompletas", visto que as movimentações do produto inativo deixarão de ser consideradas.

**![Imagem 5: Inative a unidade alternativa "incorreta" e cadastre uma nova unidade:](https://ajuda.sankhya.com.br/hc/article_attachments/16593773968663) Inative a unidade alternativa "incorreta" e cadastre uma nova unidade:**

**(1)** Como possibilidade, o cadastro de uma unidade alternativa com outra descrição de 'unidade' e inativação da unidade alternativa incorreta:

**Exemplo:**

Unidade utilizada atualmente que encontra-se com cadastro incorreto:

![Imagem 6: Unidade utilizada atualmente que encontra-se com cadastro incorreto:](https://ajuda.sankhya.com.br/hc/article_attachments/15185868734743)

Acesse a tela **"Unidades"** (Caminho de acesso: Configurações » Cadastros » Produtos) e criamos:

- Unidade: **CY**
- Descrição: Caixa

Vincule a unidade alternativa CY no cadastro do produto e essa passará a ser utilizada nas movimentações.

Para a unidade CX, desmarque a opção "**Ativo**".

**![Imagem 7: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16593773974295) IMPORTANTE:**

Essa terceira possibilidade deve ser alinhada internamente, principalmente se for utilizada nas movimentações de saída, visto que serão enviadas via XML/DANFE e poderá causar desconforto junto aos clientes, por não utilizar a 'Tabela Padrão de unidade de medida'.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16593748452503) CAUSA:**

Mensagem apresentada ao tentar alterar informações de 'unidade alternativa' do cadastro do produto, quando já existirem movimentações/lançamentos para o respectivo produto/unidade.
