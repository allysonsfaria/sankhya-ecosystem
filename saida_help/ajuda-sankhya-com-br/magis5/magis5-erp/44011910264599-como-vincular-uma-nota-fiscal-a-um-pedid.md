---
id: "44011910264599"
titulo: "Como vincular uma Nota Fiscal a um Pedido de Compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011910264599-Como-vincular-uma-Nota-Fiscal-a-um-Pedido-de-Compra"
trilha: "Magis5 > Magis5 ERP"
atualizado_em: "2026-10-05T19:15:10Z"
rotulos: ["sync_hc", "magis5", "magis5_210766010886", "sync_hash_534d796a251e"]
---

# Como vincular uma Nota Fiscal a um Pedido de Compra

## Neste guia, você aprenderá como realizar o vínculo de uma Nota Fiscal de entrada a um pedido de compra no  Magis5 ERP

---

Com a implementação dessa funcionalidade, os processos de pedido de compra e nota fiscal passam a se comunicar de forma integrada, permitindo que o sistema realize o vínculo entre eles. Isso reduz gargalos operacionais, como pendências indevidas e entradas duplicadas no estoque.

Além disso, o recurso foi desenvolvido para identificar e controlar divergências de quantidade, como nos casos em que o fornecedor entrega volumes superiores aos solicitados.

Feito login no Magis5 ERP acesse a opção **"Suprimentos"** e por fim  "**Pedido de Compras (Beta)".**

![Captura de tela 2026-04-09 121413](https://ajuda.sankhya.com.br/hc/article_attachments/44011923210263)

O sistema apresenta os pedidos de compra já realizados e permite a criação de novos pedidos.

![image-png-Apr-09-2026-03-18-43-1768-PM](https://ajuda.sankhya.com.br/hc/article_attachments/44011935610903)

### Vincular Nota Fiscal ao Pedido de Compra

O vínculo de uma nota fiscal a um pedido de compra é realizado a partir de uma nota fiscal já recebida no sistema.

Em **"Pedido de compra (Beta)"**, localize o pedido desejado, clique em **"Detalhes"** (na seta ao lado do pedido) e selecione a opção **"Vincular Nota Fiscal"**.

![Captura de tela 2026-04-09 122943](https://ajuda.sankhya.com.br/hc/article_attachments/44011923384855)

![Captura de tela 2026-04-09 123839](https://ajuda.sankhya.com.br/hc/article_attachments/44011935859607)

Ao selecionar **"Vincular Nota Fiscal"** o sistema abrirá uma listagem de Notas Fiscais Recebidas disponíveis.

Nessa listagem, o sistema exibirá somente:

- Notas fiscais com o mesmo CNPJ do fornecedor do pedido;
- Notas que ainda não foram importadas (ou foram importadas parcialmente);
- Notas que não possuem vínculo com outros pedidos (ou que foram vinculados parcialmente).

Localize e selecione a nota fiscal correspondente ao pedido de compra.

![Imagem 5: Localize e selecione a nota fiscal correspondente ao pedido de compra.](https://ajuda.sankhya.com.br/hc/article_attachments/44011918767255)

![Captura de tela 2026-04-09 132702](https://ajuda.sankhya.com.br/hc/article_attachments/44011910983063)

### Verificando a correspondência dos itens

Após selecionar a nota fiscal desejada, role a página para baixo para visualizar a seção Verificação de Correspondência.

Nessa seção, o sistema apresenta o comparativo entre:

- Os itens informados no Pedido de Compra;
- Os itens constantes na Nota Fiscal Recebida.

![Captura de tela 2026-04-09 132942](https://ajuda.sankhya.com.br/hc/article_attachments/44011949938967)

### Critérios de Correspondência

O sistema realiza a verificação de correspondência dos itens de forma automática, utilizando os seguintes critérios:

- EAN do produto;
- Nome do produto.

Caso ao menos uma dessas informações seja correspondente entre o pedido e a nota fiscal, o sistema considera que houve um match entre os itens.

### Vínculo Automático dos Itens

Quando o match é identificado, o sistema realiza automaticamente o vínculo entre:

- O item do Pedido de Compra;
- O item correspondente da Nota Fiscal.

Nesse caso, o sistema entende que se trata do mesmo produto, dispensando qualquer ação manual.

### Ausência de Match Automático

Caso não seja identificado o match automático, o item permanecerá sem vínculo.
Nessa situação, será necessário realizar a associação manual por meio do vínculo granular, que será detalhado em uma etapa posterior da documentação.

### Confirmação do Vínculo da Nota Fiscal

Após validar todas as informações e confirmar que o match dos itens está correto, clique em **Vincular Notas Fiscais**.

![Captura de tela 2026-04-09 150202](https://ajuda.sankhya.com.br/hc/article_attachments/44011950019735)

Após vincular a nota fiscal, o sistema exibirá um modal com um resumo da nota fiscal vinculada ao pedido:

![Imagem 9: Após vincular a nota fiscal, o sistema exibirá um modal com um resumo da nota fiscal vinculada ao pedido:](https://ajuda.sankhya.com.br/hc/article_attachments/44011903474199)

Para cada nota fiscal vinculada, são apresentadas as seguintes informações:

- Número da nota fiscal vinculada;
- Chave NF-e;
- Nome do fornecedor;
- Data de emissão da nota fiscal;
- Valor total da nota fiscal;
- Status do vínculo
- Correspondência;
- Status da aprovação;
- Usuário responsável pelo vínculo;
- Data do vínculo;
- Status do estoque.

### Correspondência

A correspondência representa a relação entre os itens do Pedido de Compra e os itens da Nota Fiscal Recebida, indicando se os produtos informados na nota correspondem corretamente ao que foi solicitado no pedido.

O sistema classifica a correspondência da nota fiscal em dois tipos:

- **Produtos correspondentes**: indica que todos os itens da nota fiscal possuem correspondência com os itens do pedido de compra, sem divergências.
- **Produtos divergentes**: indica que existe ao menos um item da nota fiscal que não corresponde corretamente aos itens do pedido de compra.

As divergências de correspondência podem ocorrer por diferentes motivos, como:

- Quantidade de produtos divergentes em relação ao pedido;
- Preço de custo divergente;
- Produto divergente, quando o item informado na nota não corresponde ao produto solicitado no pedido.

Quando identificada qualquer divergência, a nota fiscal é classificada como contendo produtos divergentes, exigindo análise e aprovação do setor de Compras para prosseguir.

![Imagem 10: Quando identificada qualquer divergência, a nota fiscal é classificada como contendo produtos divergentes, exigindo…](https://ajuda.sankhya.com.br/hc/article_attachments/44011924116375)

### Aprovação

A coluna Aprovação indica:

- Se a nota fiscal foi aprovada;
- Se foi reprovada;
- Ou se não há necessidade de aprovação, nos casos em que não existem divergências.

Quando um pedido de compra possuir mais de uma nota fiscal vinculada e algumas dessas notas apresentarem produtos divergentes, a aprovação deverá ser realizada nota por nota. O sistema não permite aprovação em massa para notas com divergência. Cada nota fiscal deve ser analisada e aprovada individualmente.

Caso um pedido possua, por exemplo, duas notas fiscais vinculadas:

- Se uma nota estiver aprovada e a outra pendente de aprovação, apenas a nota aprovada poderá seguir para o Controle de Estoque.
- A nota que permanecer pendente não será considerada no processo de entrada em estoque até que seja aprovada.

A aprovação de notas fiscais com produtos divergentes é restrita a usuários que possuam permissão específica do setor de Compras.

Essa permissão deve ser previamente configurada no cadastro do usuário ou no perfil que o usuário está utilizando.

### Status de Estoque

A coluna Estoque informa a situação da nota fiscal em relação à entrada no estoque, podendo indicar:

- **Aguardando importação**: a nota fiscal ainda não foi importada para o estoque;

**Importada**: a nota fiscal já foi importada e o estoque foi atualizado.

### Vínculo de Múltiplas Notas Fiscais ao Pedido

O sistema permite vincular múltiplas notas fiscais até atingir a quantidade total do pedido de compra, mesmo que cada nota contenha apenas parte dos itens.

À medida que os vínculos são realizados, o sistema controla automaticamente a quantidade acumulada. Quando o total do pedido é atendido, novas vinculações são bloqueadas, e o botão de vínculo deixa de ficar disponível.

![Imagem 11: À medida que os vínculos são realizados, o sistema controla automaticamente a quantidade acumulada. Quando o total do…](https://ajuda.sankhya.com.br/hc/article_attachments/44011936732951)

### Finalização do Vínculo e Entrada no Controle de Estoque

Após concluir todo o processo de vínculo, validação das informações e, quando necessário, aprovação das notas fiscais com produtos divergentes, clique na opção **Ir para Controle de Estoque.**
Essa ação direciona o usuário para a tela de Controle de Estoque, onde será realizada a entrada das notas fiscais aprovadas.

### Vínculo do Pedido de Compra à Nota Fiscal

O vínculo de um pedido de compra à uma nota fiscal ocorre à partir de um Pedido de Compra já criado no sistema.

Para iniciar o processo acesse o **"Suprimentos"**, **"Notas Fiscais Recebidas"** localize a nota fiscal desejada e depois clique em **"Importar"**.

![Imagem 12: Para iniciar o processo acesse o "Suprimentos" , "Notas Fiscais Recebidas" localize a nota fiscal desejada e depois…](https://ajuda.sankhya.com.br/hc/article_attachments/44011924357271)

Em seguida, clique em **Vincular Novo Pedido**

![Imagem 13: Em seguida, clique em Vincular Novo Pedido](https://ajuda.sankhya.com.br/hc/article_attachments/44011903980055)

Após selecionar a opção de vínculo, o sistema abrirá uma listagem Pedidos de Compras criados.

Nessa listagem, o sistema exibirá somente:

- Pedidos de Compras com o mesmo CNPJ do fornecedor do pedido;
- Pedidos de Compras que ainda não foram importadas (ou foram importados parcialmente);
- Pedidos de Compras que não possuem vínculo com outras Notas Fiscais (ou que foram vinculados parcialmente).

Localize e selecione o pedido de compra correspondente à nota fiscal.

![Imagem 14: Localize e selecione o pedido de compra correspondente à nota fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/44011950814871)

### Validações e Comportamento após o Vínculo pela Nota Fiscal

Após selecionar o Pedido de Compra e vinculá-lo à Nota Fiscal Recebida, o sistema inicia automaticamente o mesmo fluxo de validação utilizado no vínculo realizado a partir do pedido de compra.

Todas as etapas seguintes são idênticas, independentemente do ponto de origem do vínculo:

- A Verificação de Correspondência entre os itens do pedido e da nota fiscal;
- Os mesmos critérios de correspondência **(EAN e nome do produto)**;
- A classificação de itens como produtos correspondentes ou produtos divergentes.
- As regras de match automático, vínculo granular, aprovação, reprovação e controle de estoque não sofrem nenhuma alteração.

### Finalização do Vínculo e Entrada no Controle de Estoque

Após concluir todo o processo de vínculo, validação das informações e, quando necessário, aprovação dos pedidos de compra, clique na opção **Ir para Controle de Estoque.**
Essa ação direciona o usuário para a tela de Controle de Estoque, onde será realizada a entrada das notas fiscais aprovadas.

### Vínculo Granular de Itens

O vínculo granular é utilizado quando um item do Pedido de Compra não é automaticamente associado a um item da Nota Fiscal Recebida durante a Verificação de Correspondência. Nesses casos, o sistema não consegue identificar automaticamente que se trata do mesmo produto.

Isso ocorre porque a correspondência automática dos itens é realizada com base em:

- EAN do produto;
- Nome do produto.

Quando nenhuma informação coincide entre o pedido e a nota fiscal, a correspondência automática não é encontrada. Ainda assim, o item recebido pode ser o correto, exigindo vínculo manual para garantir a continuidade do processo.

O vínculo granular permite que o usuário associe manualmente os itens entre pedido de compra e nota fiscal, mantendo a consistência e a rastreabilidade. Esse procedimento pode ser feito a partir de qualquer fluxo do sistema — vinculando uma nota fiscal ao pedido ou vice-versa — com o mesmo funcionamento em ambos os casos.

### Como realizar o Vínculo Granular

Quando, ao vincular uma **Nota Fiscal** a um **Pedido de Compra**, o sistema identificar que existe uma divergência e não for possível realizar o match automático dos itens, será necessário utilizar o vínculo granular.

No caso abaixo, o match dos produtos não foi realizado nem por nome, nem por **EAN**

![Imagem 15: No caso abaixo, o match dos produtos não foi realizado nem por nome, nem por EAN](https://ajuda.sankhya.com.br/hc/article_attachments/44011937230359)

Nessa situação

- Acesse o pedido de compra com a nota fiscal já vinculada
- Clique na setinha ao lado de **detalhes**;
- Selecione a opção Vínculos Granulares.

A partir desse ponto, o sistema permite associar manualmente os itens sem correspondência automática, garantindo a continuidade do vínculo entre o pedido de compra e a nota fiscal.

![Imagem 16: A partir desse ponto, o sistema permite associar manualmente os itens sem correspondência automática, garantindo a…](https://ajuda.sankhya.com.br/hc/article_attachments/44011937331479)

- Na tela de Vínculo Granular, clique no botão **Identificar Itens Não Vinculados**.
- O sistema exibirá a lista de todos os itens, inclusive itens que não possuem correspondência automática.
- No item desejado, selecione a opção **Vincular Item**

![Imagem 17: No item desejado, selecione a opção Vincular Item](https://ajuda.sankhya.com.br/hc/article_attachments/44011951133719)

- Após clicar em Vincular Item, role a página para baixo.
- O produto disponível para vínculo será exibido na parte inferior da tela.
- Selecione o item da Nota Fiscal correspondente.
- Selecione a nota fiscal.
- Informe a quantidade a ser vinculada.
- Clique em Criar Vínculo.

![Imagem 18: Clique em Criar Vínculo.](https://ajuda.sankhya.com.br/hc/article_attachments/44011912505495)

Após vincular o produto desejado, uma mensagem de sucesso será exibida confirmando o vínculo.  

![Imagem 19: Após vincular o produto desejado, uma mensagem de sucesso será exibida confirmando o vínculo.](https://ajuda.sankhya.com.br/hc/article_attachments/44011925037975)

Após concluir os vínculos, feche a tela de vínculos granulares, clique novamente em **"Vincular Nota Fiscal"** e prossiga com o processo. A partir daí, a conferência e a importação dos itens no estoque seguem normalmente.

### Comportamento do Sistema após o Vínculo Granular

- O item passa a ser considerado vinculado, mesmo sem correspondência automática.
- A quantidade vinculada é abatida do saldo disponível do pedido e da nota fiscal.
- O item deixa de aparecer como “não vinculado” na análise de correspondência.
- O vínculo granular segue as mesmas regras de aprovação, quando aplicável, especialmente em casos de divergência de quantidade ou valor.

### Validações de Vínculo

Durante o processo de vínculo entre Pedido de Compra e Nota Fiscal Recebida, o sistema executa uma série de validações automáticas.

Estas validações são responsáveis por analisar diferentes cenários que podem ocorrer durante o recebimento de mercadorias, como:

- Diferenças de quantidade entre o pedido e a nota fiscal;

- Diferenças de valor (preço de custo);
- Recebimento parcial em momentos distintos;
- Vínculo de múltiplas notas para um único pedido;
- Vínculo de uma única nota para múltiplos pedidos;
- Identificação de produtos que não correspondem ao pedido original.

Cada validação define como o sistema deve se comportar em determinado cenário, indicando:

- Se o vínculo pode ser realizado automaticamente;
- Se o pedido ou a nota permanecem parciais;
- Se é necessário aprovação do setor de Compras;
- Se haverá bloqueio, alerta ou possibilidade de devolução;
- Como o estoque será impactado.

As validações estão organizadas em 14 situações distintas, que representam os cenários mais comuns no processo de recebimento. O objetivo dessas situações é garantir que, independentemente da forma como o fornecedor envie as mercadorias ou as notas fiscais, o sistema consiga tratar corretamente cada caso.

### Validação 1 - Pedido de Compra e Nota Fiscal com quantidades iguais.

**Cenário**

O Pedido de Compra possui exatamente a mesma quantidade de itens informada na Nota Fiscal Recebida.

**Como o sistema se comporta**

- O sistema identifica que a quantidade total solicitada no pedido é igual à quantidade informada na nota fiscal.
- A verificação de correspondência dos itens é realizada normalmente (por EAN e/ou nome do produto).
- Não havendo divergências de produto, quantidade ou valor, o vínculo é realizado de forma automática.

**Resultado do vínculo**

- O Pedido de Compra é considerado totalmente atendido.
- A Nota Fiscal é considerada totalmente vinculada.
- O pedido segue para o status de concluído após a entrada no estoque.
- A nota fiscal segue para status importada após a entrada no estoque.

**Impacto no estoque**

- Todos os itens da nota fiscal são dados como entrada no estoque.
- Não há pendências, aprovações adicionais ou bloqueios.

![Imagem 20: Não há pendências, aprovações adicionais ou bloqueios.](https://ajuda.sankhya.com.br/hc/article_attachments/44011912713111)

### Validação 2 - Pedido parcial e Nota Fiscal parcial em momentos diferentes

**Cenário**

O Pedido de Compra é atendido por mais de uma Nota Fiscal em momentos diferentes, sendo que cada nota contempla apenas parte da quantidade solicitada.

**Como o sistema se comporta na primeira nota**

- A primeira Nota Fiscal é vinculada ao Pedido de Compra com quantidade inferior à solicitada.
- O sistema realiza a verificação de correspondência dos itens.
- A entrada parcial é permitida.
- O Pedido de Compra permanece com status parcial, pois ainda existem itens pendentes de recebimento.

**Como o sistema se comporta nas notas seguintes**

- Cada nova Nota Fiscal vinculada passa pelo mesmo processo de validação e correspondência.
- O sistema acumula automaticamente as quantidades recebidas.
- Os itens já recebidos anteriormente são mantidos como concluídos.
- Apenas os itens pendentes continuam aguardando vínculo.

**Resultado do vínculo**

- Enquanto a quantidade total do pedido não for atingida, o Pedido de Compra permanece parcial.
- Quando a soma das notas fiscais atingir a quantidade total solicitada:
- O Pedido de Compra é automaticamente marcado como concluído.
- As Notas Fiscais vinculadas são consideradas corretamente processadas.

**Impacto no estoque**

- O estoque é atualizado de forma gradual, conforme cada nota fiscal é importada.
- Não há duplicação de estoque, pois o sistema controla as quantidades já recebidas.

![Imagem 21: Não há duplicação de estoque, pois o sistema controla as quantidades já recebidas.](https://ajuda.sankhya.com.br/hc/article_attachments/44011920716951)

### Validação 3 - Pedido de Compra inteiro atendido por várias Notas Fiscais

**Cenário**

Um único Pedido de Compra é atendido por mais de uma Nota Fiscal, sendo que a soma das quantidades dessas notas corresponde exatamente à quantidade solicitada no pedido.

**Como o sistema se comporta**

- O usuário vincula todas as notas fiscais necessárias ao pedido de compra.
- Cada nota fiscal passa individualmente pelo processo de:
- Verificação de correspondência dos itens;
- Validação de quantidade, produto e valor.
- O sistema soma automaticamente as quantidades recebidas em cada nota vinculada.

**Resultado do vínculo**

- Enquanto nem todas as notas forem vinculadas, o pedido permanece com status parcial.
- Quando a soma das quantidades das notas fiscais atingir exatamente a quantidade solicitada no pedido:
- O Pedido de Compra é considerado totalmente atendido;
- Todas as notas fiscais vinculadas ficam com status vinculado.

**Impacto no estoque**

- A entrada no estoque ocorre de forma controlada, conforme cada nota fiscal é importada.
- O sistema impede a duplicidade de estoque, pois controla o acumulado de quantidades já recebidas.
- Ao final, o estoque reflete exatamente a quantidade solicitada no pedido.

![Imagem 22: Ao final, o estoque reflete exatamente a quantidade solicitada no pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/44011925298839)

---

### Validação 4 - Pedido de Compra inteiro com várias Notas Fiscais, sendo uma com itens de outro pedido

**Cenário**

O Pedido de Compra é atendido por várias notas fiscais, porém uma dessas notas contém itens que não pertencem ao pedido, ou seja, itens que correspondem a outro pedido ou que não possuem correspondência válida.

**Como o sistema se comporta**

- O sistema permite o vínculo de todas as notas fiscais ao pedido de compra.
- Durante a verificação de correspondência:
- Os itens corretos são identificados como produtos correspondentes;
- Os itens que não pertencem ao pedido são identificados como produtos divergentes.
- A nota fiscal que contém itens divergentes recebe status parcial.

**Resultado do vínculo**

- O Pedido de Compra pode ser considerado concluído, desde que a quantidade total dos itens correspondentes tenha sido totalmente atendida.
- A nota fiscal que possui itens divergentes:
- Permanece com status parcial;
- Exige tratamento adicional para os itens que não correspondem ao pedido.

**Impacto no estoque**

- Apenas os itens correspondentes ao pedido são considerados para entrada no estoque.
- Os itens divergentes:
- Não entram automaticamente no estoque;
- Permanecem pendentes até que sejam vinculados a outro pedido, ajustados ou tratados conforme o fluxo definido.
- Esse controle evita que itens incorretos impactem o estoque ou o pedido errado.

![Imagem 23: Esse controle evita que itens incorretos impactem o estoque ou o pedido errado.](https://ajuda.sankhya.com.br/hc/article_attachments/44011920916119)

### Validação 5 - Pedido de Compra com Nota Fiscal que já teve entrada parcial

**Cenário**

Uma Nota Fiscal já havia sido utilizada anteriormente para realizar uma entrada parcial no estoque, atendendo apenas parte de um Pedido de Compra. Posteriormente, o restante da quantidade do pedido é recebido por meio de outra Nota Fiscal.

**Como o sistema se comporta**

- O sistema identifica que a nota fiscal já possui histórico de vínculo e entrada parcial.
- Ao vincular a nova nota fiscal ao pedido:
- Os itens já recebidos anteriormente são mantidos como concluídos;
- Apenas os itens restantes seguem para validação e possível entrada.
- O sistema soma automaticamente as quantidades recebidas nas diferentes notas fiscais.

**Resultado do vínculo**

- Quando a soma das quantidades recebidas atinge a quantidade total solicitada:
- O Pedido de Compra é considerado totalmente atendido;
- A nota fiscal que estava parcial é atualizada para status importada.
- A nova nota fiscal vinculada também passa a fazer parte do histórico do pedido.

**Impacto no estoque**

- O estoque é atualizado apenas com as quantidades que ainda não haviam sido recebidas.
- Não ocorre duplicidade de estoque, pois o sistema respeita as entradas já realizadas.

![Imagem 24: Não ocorre duplicidade de estoque, pois o sistema respeita as entradas já realizadas.](https://ajuda.sankhya.com.br/hc/article_attachments/44011921008663)

### Validação 6 - Pedido de Compra com Nota Fiscal em quantidade menor

**Cenário**

A Nota Fiscal vinculada ao Pedido de Compra possui quantidade inferior à quantidade solicitada no pedido.

**Como o sistema se comporta**

- O sistema permite o vínculo da nota fiscal ao pedido de compra.
- A verificação de correspondência é realizada normalmente.
- A entrada parcial da nota fiscal é permitida.
- O sistema identifica que ainda existem itens pendentes de recebimento.

**Resultado do vínculo**

- O Pedido de Compra permanece com status parcial.
- A Nota Fiscal é considerada válida e pode ser importada no estoque.
- A quantidade restante do pedido permanece em aberto, aguardando novas notas fiscais.

**Impacto no estoque**

- Apenas a quantidade informada na nota fiscal é dada entrada no estoque.
- O saldo restante do pedido não impacta o estoque até que seja recebido por novas notas fiscais.

![Imagem 25: O saldo restante do pedido não impacta o estoque até que seja recebido por novas notas fiscais.](https://ajuda.sankhya.com.br/hc/article_attachments/44011925569047)

### Validação 7 - Pedido de Compra com Nota Fiscal em quantidade maior

**Cenário**

A Nota Fiscal vinculada ao Pedido de Compra possui quantidade superior à quantidade solicitada no pedido.

**Como o sistema se comporta**

- O sistema identifica que a quantidade informada na nota fiscal excede a quantidade solicitada no pedido.
- O vínculo entre pedido e nota fiscal é permitido.
- O Pedido de Compra é considerado atendido em relação à quantidade solicitada.
- A Nota Fiscal recebe status de alerta, indicando a existência de quantidade excedente.

**Resultado do vínculo**

- O Pedido de Compra é finalizado com base na quantidade originalmente solicitada.
- A quantidade excedente da nota fiscal não é automaticamente incorporada ao pedido.
- O sistema disponibiliza opções para tratamento do excedente.

**Tratamento do excedente**

- O usuário pode emitir uma Nota Fiscal de Devolução para devolver as unidades excedentes ao fornecedor.
- Caso não seja realizada a devolução, a quantidade excedente permanece disponível para:
- Ser vinculada a outro Pedido de Compra;
- Ser tratada em um novo pedido criado especificamente para esse saldo.

**Impacto no estoque**

- Apenas a quantidade correspondente ao pedido é considerada para entrada no estoque.
- A quantidade excedente não é importada automaticamente, evitando inconsistências.

![Imagem 26: A quantidade excedente não é importada automaticamente, evitando inconsistências.](https://ajuda.sankhya.com.br/hc/article_attachments/44011938388759)

### Validação 8 - Nota Fiscal e Pedido de Compra com quantidades iguais (Fluxo inverso)

**Cenário**

A Nota Fiscal Recebida possui exatamente a mesma quantidade de itens de um Pedido de Compra existente, e o vínculo é realizado a partir da Nota Fiscal.

**Como o sistema se comporta**

- O usuário seleciona a nota fiscal e vincula um pedido de compra com quantidade equivalente.
- O sistema realiza a verificação de correspondência dos itens.
- Não havendo divergências de produto, quantidade ou valor, o vínculo é realizado automaticamente.

**Resultado do vínculo**

- A Nota Fiscal é considerada totalmente vinculada ao pedido.
- O Pedido de Compra é considerado totalmente atendido.
- Ambos seguem normalmente para o fluxo de entrada no estoque.

**Impacto no estoque**

- Todos os itens da nota fiscal são importados no estoque.
- Não existem pendências, aprovações adicionais ou bloqueios.

![Imagem 27: Não existem pendências, aprovações adicionais ou bloqueios.](https://ajuda.sankhya.com.br/hc/article_attachments/44011913417879)

### Validação 9 – Nota Fiscal e Pedido de Compra parcial em momentos diferentes (Fluxo inverso)

**Cenário**

A Nota Fiscal Recebida possui uma quantidade maior de itens do que um Pedido de Compra existente. O vínculo ocorre inicialmente com apenas parte da nota fiscal, ficando o restante pendente para vínculo com outros pedidos em momentos diferentes.

**Como o sistema se comporta no primeiro vínculo**

- O usuário importa a nota fiscal e vincula um pedido de compra com quantidade inferior à quantidade total da nota.
- O sistema realiza a verificação de correspondência dos itens.
- A entrada parcial da nota fiscal é permitida.
- A Nota Fiscal permanece com saldo pendente para novos vínculos.

**Como o sistema se comporta nos vínculos seguintes**

- Novos pedidos de compra podem ser vinculados à mesma nota fiscal.
- O sistema acumula automaticamente as quantidades já utilizadas.
- Os itens já vinculados anteriormente permanecem registrados como concluídos.

**Resultado do vínculo**

- A Nota Fiscal permanece com status parcial até que toda a sua quantidade seja distribuída entre os pedidos de compra.

- Cada pedido de compra é concluído conforme sua quantidade total é atendida.

**Impacto no estoque**

- O estoque é atualizado conforme cada vínculo aprovado é importado.
- Não ocorre duplicidade de estoque, pois o sistema controla o saldo restante da nota fiscal.

![Imagem 28: Não ocorre duplicidade de estoque, pois o sistema controla o saldo restante da nota fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/44011952164119)

### Validação 10 - Uma Nota Fiscal para vários Pedidos de Compra

**Cenário**

Uma única Nota Fiscal atende vários Pedidos de Compra distintos, sendo necessário distribuir a quantidade da nota entre diferentes pedidos.

**Como o sistema se comporta**

- O usuário vincula a mesma nota fiscal a múltiplos pedidos de compra.
- Cada vínculo passa individualmente pela verificação de correspondência.
- O sistema distribui a quantidade da nota conforme os pedidos selecionados.

**Resultado do vínculo**

- Cada Pedido de Compra é concluído ou permanece parcial de acordo com a quantidade recebida.
- A Nota Fiscal é considerada totalmente vinculada quando toda a sua quantidade for distribuída entre os pedidos.

**Impacto no estoque**

- O estoque é atualizado conforme cada pedido vinculado é aprovado e importado.
- O sistema garante que a quantidade total da nota fiscal seja utilizada apenas uma vez, evitando inconsistências.

![Imagem 29: O sistema garante que a quantidade total da nota fiscal seja utilizada apenas uma vez, evitando inconsistências.](https://ajuda.sankhya.com.br/hc/article_attachments/44011952266903)

### Validação 11 - Nota Fiscal com vários Pedidos de Compra, contendo itens de outro pedido

**Cenário**

Uma Nota Fiscal é vinculada a vários Pedidos de Compra, porém contém itens que não correspondem a todos os pedidos selecionados, ou seja, há produtos que pertencem a outro pedido ou que não possuem correspondência válida.

**Como o sistema se comporta**

- O sistema permite o vínculo da nota fiscal a todos os pedidos selecionados.
- Durante a verificação de correspondência:
- Os itens corretos são identificados como produtos correspondentes;
- Os itens que não correspondem a determinado pedido são identificados como produtos divergentes.
- O pedido que possuir itens divergentes permanece com status parcial.

**Resultado do vínculo**

- Os pedidos que tiveram seus itens totalmente atendidos são considerados concluídos.
- O pedido que contém itens divergentes:
- Permanece parcial;
- Aguarda novo vínculo, ajuste ou tratamento dos itens divergentes.
- A nota fiscal pode permanecer parcialmente vinculada até que todos os itens sejam corretamente tratados.

**Impacto no estoque**

- Apenas os itens corretamente correspondentes a cada pedido são considerados para entrada no estoque.
- Itens divergentes não impactam o estoque até que sejam vinculados ou aprovados corretamente.

![Imagem 30: Itens divergentes não impactam o estoque até que sejam vinculados ou aprovados corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/44011926052375)

### Validação 12 - Nota Fiscal com Pedido de Compra que já teve entrada parcial

**Cenário**

Um Pedido de Compra já recebeu parte de sua quantidade anteriormente. Posteriormente, uma Nota Fiscal é vinculada para atender o saldo restante do pedido.

**Como o sistema se comporta**

- O sistema identifica que o pedido já possui histórico de entrada parcial.
- Ao vincular a nova nota fiscal:
- Os itens já recebidos permanecem como concluídos;
- Apenas a quantidade restante é considerada para validação e possível entrada.
- A verificação de correspondência é realizada normalmente.

**Resultado do vínculo**

- Quando a quantidade restante é totalmente atendida:
- O Pedido de Compra é considerado concluído;
- A Nota Fiscal é considerada corretamente vinculada.
- Caso a nota fiscal não cubra toda a quantidade restante, o pedido permanece parcial.

**Impacto no estoque**

- O estoque é atualizado somente com as quantidades que ainda não haviam sido recebidas.
- O sistema impede qualquer duplicação de entrada para itens já contabilizados anteriormente.

![Imagem 31: O sistema impede qualquer duplicação de entrada para itens já contabilizados anteriormente.](https://ajuda.sankhya.com.br/hc/article_attachments/44011939139607)

### Validação 13 - Nota Fiscal com Pedido de Compra em quantidade menor

**Cenário**

A Nota Fiscal Recebida possui uma quantidade superior à quantidade de um Pedido de Compra específico, e apenas parte da nota é vinculada a esse pedido.

**Como o sistema se comporta**

- O usuário vincula a nota fiscal a um pedido com quantidade inferior à quantidade total da nota.
- O sistema realiza a verificação de correspondência dos itens normalmente.
- Apenas a quantidade correspondente ao pedido é considerada para o vínculo.
- O saldo restante da nota fiscal permanece disponível para vínculo com outros pedidos.

**Resultado do vínculo**

- O Pedido de Compra é considerado atendido em relação à sua quantidade.
- A Nota Fiscal permanece com status parcial, pois ainda possui quantidade não vinculada.
- O sistema permite que a mesma nota seja vinculada a outros pedidos posteriormente.

**Impacto no estoque**

- Apenas a quantidade vinculada ao pedido é importada no estoque.
- O saldo restante da nota não impacta o estoque até que seja corretamente vinculado a outro pedido.

![Imagem 32: O saldo restante da nota não impacta o estoque até que seja corretamente vinculado a outro pedido.](https://ajuda.sankhya.com.br/hc/article_attachments/44011926295575)

### Validação 14 - Nota Fiscal com Pedido de Compra em quantidade maior

**Cenário**

O Pedido de Compra possui quantidade superior à quantidade informada na Nota Fiscal Recebida.

**Como o sistema se comporta**

- O usuário vincula a nota fiscal ao pedido de compra.
- O sistema identifica que a nota não atende toda a quantidade solicitada no pedido.
- A entrada parcial da nota fiscal é permitida.
- O Pedido de Compra permanece com saldo pendente.

**Resultado do vínculo**

- O Pedido de Compra fica com status parcial, aguardando o recebimento do restante da quantidade.
- Para concluir o pedido, será necessário:
- Vincular uma nova nota fiscal com os itens faltantes; ou
- Ajustar o pedido de compra, caso não seja mais esperado o recebimento da quantidade restante.

**Impacto no estoque**

- Apenas a quantidade informada na nota fiscal é importada no estoque.
- A quantidade faltante não impacta o estoque até que seja recebida por uma nova nota fiscal.

![Imagem 33: A quantidade faltante não impacta o estoque até que seja recebida por uma nova nota fiscal.](https://ajuda.sankhya.com.br/hc/article_attachments/44011964552087)
