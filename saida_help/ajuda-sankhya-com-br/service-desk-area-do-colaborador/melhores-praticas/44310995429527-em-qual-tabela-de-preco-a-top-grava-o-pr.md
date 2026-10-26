---
id: "44310995429527"
titulo: "Em qual tabela de preço a TOP grava o preço de venda?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44310995429527-Em-qual-tabela-de-pre%C3%A7o-a-TOP-grava-o-pre%C3%A7o-de-venda"
trilha: "Service Desk | área do colaborador  > Melhores práticas"
atualizado_em: "2026-10-21T11:25:44Z"
---

# Em qual tabela de preço a TOP grava o preço de venda?

Quando a TOP de uma nota que movimenta custo, como a de compra, está com o campo **"Precifica"** em **"Atualiza custo e preço de venda"**, o sistema recalcula o preço de venda dos produtos ao confirmar a nota. A TOP, porém, não define em qual tabela esse preço será gravado. Isso depende do parâmetro **CUSTOPOREMP** (controle de custo por empresa) e do cadastro da empresa.

Com o parâmetro **CUSTOPOREMP** desligado, o preço é **sempre gravado na tabela 0**. Não importa como as vendas buscam o preço nem qual tabela está informada no cadastro da empresa.

### Como o sistema define a tabela que será atualizada

- **CUSTOPOREMP desligado:** o preço é gravado sempre na **tabela 0**.
- **CUSTOPOREMP ligado:** o preço é gravado na tabela informada no campo **"Tabela de preço padrão"** da empresa da nota (Comercial » Preferências » Empresa, aba "Estoque/Preço"). Nas transferências, vale a empresa de negociação. Se o campo estiver vazio, o preço vai para a tabela 0.

Nenhuma outra configuração interfere nessa escolha. A TOP não tem campo de tabela para essa atualização. O parâmetro **"TIPTABPRECOS - Tabela de preços por:"** (por Parceiro, Parceiro/Empresa, Região etc.) também não é considerado, porque ele só define de qual tabela as vendas leem o preço.

### Como conferir a configuração

**(1)**  Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

**(2)**  Localize o parâmetro **CUSTOPOREMP** e veja se está ligado ou desligado. Se estiver desligado, o preço será sempre gravado na tabela 0.

**(3)**  Se estiver ligado, acesse a tela **"Empresa"** (Comercial » Preferências » Empresa).

**(4)**  Selecione a empresa da nota e, na aba **"Estoque/Preço"**, confira o campo **"Tabela de preço padrão"**.

**(5)**  Na TOP da nota (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), confirme que o campo **"Precifica"** está como **"Atualiza custo e preço de venda"**.

### Observações importantes

- **Vigência:** o preço é gravado na vigência da tabela com a mesma data da nota. Essa data é definida pelo parâmetro **"DTPDTVIGOR - Campo de Data para Vigor da tab. de preço"** (por padrão, a data de negociação). Se ainda não existir uma vigência com essa data, o sistema cria uma nova.
- **"Alt. Preço Igual" = "Não Atualiza":** os itens da nota com essa opção não têm o preço atualizado.
- **Preço menor que o atual:** o novo preço só é gravado se o parâmetro **"DIMINUIPRECO - Atualizar preço se menor que o em vigor?"** estiver ligado, ou se o item estiver com **"Alt. Preço Igual" = "Atualiza menor"**.
