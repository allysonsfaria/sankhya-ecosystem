---
id: "43548734064535"
titulo: "Por que a OP não está reservando materiais automaticamente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548734064535-Por-que-a-OP-n%C3%A3o-est%C3%A1-reservando-materiais-automaticamente"
trilha: "Dúvidas Frequentes > Produção"
atualizado_em: "2026-10-15T13:36:20Z"
rotulos: ["Artigo criado KCS", "Produção - KCS"]
---

# Por que a OP não está reservando materiais automaticamente?

Quando uma Ordem de Produção (OP) é lançada no ERP Sankhya, o sistema pode reservar automaticamente os materiais necessários para o processo produtivo, conforme a configuração realizada no processo e na composição do produto. No entanto, em algumas situações, pode ocorrer de a OP não realizar essa reserva, impactando o controle de estoque e o andamento da produção. Este artigo apresenta as principais causas para esse comportamento e orienta como proceder para garantir a correta reserva de materiais.

### Verificação da composição do produto

Acesse a tela **"Composição do Produto"** (Produção » Cadastros » Composição do Produto) e confira se os materias estão corretamente vinculados ao produto e o processo produtivo.

**(1)** Na aba **"Matérias-primas"**, verifique as **MPs** e/ou **PIs** vinculados à composição e valide se a marcação **"Gera requisição"** está marcada, caso contrário, precisa marcar essa opção, ela é essencial para que o material seja inserido na nota gerada pela operação de estoque.

**(2)** Valide se o produto usado como **MP** (Matéria-prima) e/ou **PI** (Produto Intermediário) está efetivamente ativo na tela de **"Cadastro de Produtos"** (Configurações » Cadastros » Produtos » Produtos).

**(3)** Através da tela **Processo Produtivo - NOVA**(Produção » Cadastros » Processo Produtivo - Nova), botão **"Roteiro"** acesse a atividade que gera a reserva, aba **"Operações de Estoque"**, o campo **"Tipo Material",** pode ser definido para reservar **'Ambos', 'Somente MPs'** ou **'Somente PIs'.**

### Parâmetros e configurações do processo produtivo

Ajuste parâmetros que impactam a reserva de materiais na OP. Certifique-se de que os parâmetros relacionados à edição e validação de materiais estão configurados conforme a necessidade do processo. Parâmetros como **"PERMITEDITLSTMP"** e **"PERMITEDITMP"** podem influenciar a possibilidade de editar a composição após o lançamento de ordens de produção, o que pode afetar a reserva automática.

**Obs.:** No caso da reserva já ter ocorrido na **OP** e ter sido realizada uma alteração na composição posteriormente.

Além disso, verifique se a versão do processo produtivo utilizada na OP está atualizada e ativa. Caso a OP esteja sendo lançada para uma versão desatualizada ou sem composição, a reserva dos materiais não será realizada.

### Outros pontos de atenção

Considere situações específicas que podem impedir a reserva, como personalização ou rotinas especificas no processo produtivo. Por fim, valide sempre se há saldo suficiente em estoque para os materiais envolvidos. A falta de saldo pode impedir a reserva, mesmo que todas as configurações estejam corretas.
