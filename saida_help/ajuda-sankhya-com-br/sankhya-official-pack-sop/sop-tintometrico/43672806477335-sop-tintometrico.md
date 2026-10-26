---
id: "43672806477335"
titulo: "SOP Tintométrico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43672806477335-SOP-Tintom%C3%A9trico"
trilha: "Sankhya Official Pack - SOP > SOP Tintométrico"
atualizado_em: "2026-10-19T18:05:51Z"
---

# SOP Tintométrico

**Manual de Usabilidade**

O Módulo Tintométrico é a extensão do Sankhya que conecta máquinas tintométricas e catálogos de fabricantes de tinta ao ERP.

### 1. Visão geral do produto

O Módulo Tintométrico é uma extensão do Sankhya que conecta o ERP às máquinas tintométricas e aos catálogos de cores dos fabricantes de tinta, permitindo vender tinta com cor sob medida direto no pedido, orçamento ou venda rápida, já com a fórmula pronta para a produção na loja.

**Fabricantes suportados:** Suvinil (SU), Montana (MO), Sumaré (SM), Marfim (MA), Lazzumix (LZ), Iquine (IQ) e Sherwin-Williams (SW).

#### Para que serve:

1. Importa o catálogo de cores, bases, pigmentos e fórmulas de cada fabricante para dentro do Sankhya.
2. Cadastra os produtos (bases, pigmentos, embalagens, acabamentos) que a loja usa na manipulação.
3. Insere a tinta personalizada como item de venda, já calculando o preço pela fórmula.
4. Controla a produção da tinta na tela do Colorista (fila de manipulação).
5. Permite cadastrar cores próprias da loja, fora do catálogo do fabricante.
6. Gera lançamentos de reclassificação de estoque (matéria-prima → tinta acabada), quando a loja controla estoque tintométrico.

#### Principais benefícios:

- Elimina erro de cálculo manual de fórmula e preço.
- Rastreia quem produziu cada lata e quando.
- Evita venda de cor incompatível com a base ou o acabamento escolhido, com filtros em cascata no momento da venda.
- Padroniza o processo entre lojas que trabalham com mais de um fabricante de tinta.

### 2. Configuração inicial

Faça esta configuração uma única vez, antes de começar a vender tinta manipulada.

#### 2.1 Preferências do sistema

**Administração » Preferências**

Busque cada parâmetro pelo nome e preencha conforme a operação da loja. As alterações valem imediatamente, sem precisar reiniciar.

| Parâmetro | Tipo | Padrão | Para que serve |
| --- | --- | --- | --- |
| DVC\_LANCNTINT | Sim/Não | Sim | Permite lançar mais de uma tinta no mesmo documento sem fechar o popup de venda |
| MODETIQUETA | Número | 0 | Código do modelo de relatório da etiqueta da tinta manipulada (parâmetros NUNOTA e SEQUENCIA) |
| TIMEREFRESHCOL | Número (ms) | 30000 | Intervalo de atualização automática da tela do Colorista |
| MODENTRRECLASS | Número | 0 | Modelo de nota usado na entrada da reclassificação de estoque |
| MODMSAIRECLASS | Número | 0 | Modelo de nota usado na saída da reclassificação de estoque |
| DVC\_RECLASSIFCA | Sim/Não | Não | Liga a rotina agendada de reclassificação de estoque |
| DVC\_NAOGERAFORM | Sim/Não | Não | Impede a geração da formulação no lançamento (uso pontual) |
| DVC\_PRECOFIXOIQ | Sim/Não | Não | Usa o preço fixo cadastrado no produto em vez do calculado pela fórmula (Iquine) |

#### 2.2 Cadastro do fabricante e importação do catálogo

**Tintométrico » Configuração dos Fabricantes**

**(1)** Abra a tela e selecione a marca desejada (SU, MO, SM, MA, LZ, IQ ou SW).

**(2)** Preencha o Fator de Conversão (Pulso x ML) — campo obrigatório, usado para converter os pulsos da máquina em mililitros de pigmento.

**(3)** Vincule o Layout de Processamento correspondente à marca.

**(4)** Anexe o(s) arquivo(s) do fabricante (ou configure a integração via API, no caso da Suvinil) e clique em Realizar Integração.

![Imagem 1: (4) Anexe o(s) arquivo(s) do fabricante (ou configure a integração via API, no caso da Suvinil) e clique em Realizar…](https://ajuda.sankhya.com.br/hc/article_attachments/44363109693335)

Imagem: Tela Configuração dos Fabricantes — exemplo com a marca Suvinil (SU).

| **Resultado esperado:** cores, bases, pigmentos e fórmulas do fabricante ficam disponíveis nas tabelas do módulo e a data da última integração é atualizada no cadastro. |
| --- |

| **IMPORTANTE:** a integração traz apenas o catálogo do fabricante. Ela não cria os produtos no Sankhya automaticamente — o cadastro de produto (próximo passo) precisa ser feito manualmente para cada base, pigmento, embalagem e acabamento que a loja usa. Consulte a seção Integrações para o detalhe de arquivos por marca. |
| --- |

#### 2.3 Cadastro de produtos — aba Tintométrico

**Produtos » Cadastro de Produtos (aba Tintométrico)**

| Tipo | O que é | Campos obrigatórios |
| --- | --- | --- |
| C — Acabamento | Tinta final vendida ao cliente | Sistema Tintométrico, Tipo = C |
| B — Base | Base bruta que recebe os pigmentos | Sistema, Tipo = B, Cód Base, Volumetria |
| P — Pigmento | Corante usado na fórmula | Sistema, Tipo = P, Cód Pigmento |
| E — Embalagem | Lata/galão tratado à parte | Sistema, Tipo = E, Cód Embalagem |

![Imagem 2: Sistema, Tipo = E, Cód Embalagem](https://ajuda.sankhya.com.br/hc/article_attachments/44363131614359)

Imagem: Aba Tintométrico no Cadastro de Produtos.

**(1)** Selecione o Sistema Tintométrico (marca) e o Tipo do produto.

**(2)** Preencha o campo de vínculo com o catálogo do fabricante conforme o tipo (Cód Base, Cód Pigmento, Cód Embalagem ou Cód Produto Tintométrico).

**(3)** Para produtos automotivos (Lazzumix), preencha também Peso Específico nos pigmentos e Acabamento Automotivo nos acabamentos.

**(4)** Salve.

**Erros comuns de validação:**

- Tipo Base sem Cód Base: “Se o tipo do produto for Base é obrigatório o preenchimento do campo Cód Base.”
- Tipo Pigmento sem Cód Pigmento ou Tipo Embalagem sem Cód Embalagem: mensagem análoga.
- Tipo em branco com algum campo tintométrico preenchido: “Favor preencher o campo Tipo.”
- Pigmento ou acabamento já vinculado a outro produto: “O pigmento/acabamento já está associado ao produto <código> - <descrição>.”

#### 2.4 Configuração da TOP (Tipo de Operação)

**Vendas » Tipos de Operação (aba (Dvc) Tintometro)**

![Imagem 3: Vendas » Tipos de Operação (aba (Dvc) Tintometro)](https://ajuda.sankhya.com.br/hc/article_attachments/44363109695767)

Imagem: Aba (Dvc) Tintometro no cadastro da TOP.

Na TOP que será usada para vender tinta:

**(1)** Marque Top é considerada na tela do Colorista — sempre obrigatório; sem isso, o pedido nunca aparece para produção.

**(2)** Marque Gera Reclassificação apenas se a loja usa o processo de reclassificação de estoque.

**(3)** Salve.

Com isso, a configuração inicial está completa e a loja já pode vender tinta manipulada (próxima seção).

### 3. Guia de uso

#### 3.1 Inserir tinta manipulada na venda (“Insere Tinta”)

**Vendas » Central de Vendas**

Use esta ação em pedidos, orçamentos ou na venda rápida. Não adicione o produto de tinta manualmente pelo grid — sempre pelo popup.

**(1)** Abra o documento usando a TOP configurada na seção anterior.

**(2)** No grid de itens, clique no botão de ação Insere Tinta.

**(3)** No popup, preencha em sequência: Sistema Tintométrico → Acabamento → Base/Cor → Pigmentos. Cada campo filtra as opções do próximo.

**(4)** Informe o Controle — nome que diferencia essa cor das demais dentro da mesma nota.

**(5)** Informe Unidade e Quantidade.

**(6)** Clique em Cálculo de Preço para conferir o valor calculado pela fórmula.

**(7)** Clique em Insere Item.

![Imagem 4: (7) Clique em Insere Item.](https://ajuda.sankhya.com.br/hc/article_attachments/44363109699479)

Imagem: Central de Vendas — menu de ações com a opção Insere Tinta.

![Imagem 5: Imagem: Central de Vendas — menu de ações com a opção Insere Tinta.](https://ajuda.sankhya.com.br/hc/article_attachments/44363109700119)

Imagem: Popup Inclusão de Tintas — exemplo de preenchimento.

**Resultado esperado:** o item de tinta é incluído no grid com os campos Cor, Sistema, Controle e Volume preenchidos. Os componentes da fórmula (base + pigmentos) são criados automaticamente no documento — não é preciso adicioná-los à mão.

**Avisos:**

- Volume fracionado maior que o da embalagem: “Volume fracionado superior ao volume da embalagem escolhida.”
- Volume sem de-para cadastrado: “Não existe De-para para o volume <código> - <descrição>. Ou o mesmo se encontra sem volumetria.”
- Com DVC\_LANCNVTINT ligado, dá para lançar outra tinta sem fechar o popup.
- Para vender uma cor personalizada, marque Cor Personalizada = Sim antes de escolher o acabamento (a cor precisa já estar cadastrada — veja 3.3).

#### 3.2 Consultar a composição de uma tinta já vendida

**Vendas » Central de Vendas**

**(1)** Selecione o item de tinta manipulada no grid do documento.

**(2)** Clique em Mostra Composição.

**Resultado esperado:** um popup mostra a base e os pigmentos com as quantidades da fórmula. Em itens que não são de tinta manipulada, o botão não faz nada (sem erro).

#### 3.3 Cadastrar uma cor personalizada

**Tintométrico » Cores Personalizadas**

Use quando a cor não existe no catálogo do fabricante — uma fórmula própria da loja.

![Imagem 6: Use quando a cor não existe no catálogo do fabricante — uma fórmula própria da loja.](https://ajuda.sankhya.com.br/hc/article_attachments/44363131633943)

Imagem: Tela Cores Personalizadas — exemplo de preenchimento.

**(1)** Clique em Incluir.

**(2)** Preencha Sistema Tintométrico, Controle (nome da cor), Acabamento, Base, Tipo e, para Lazzumix, a Embalagem (obrigatória para essa marca).

**(3)** Na aba de componentes, adicione cada pigmento com a quantidade (gramas/pulsos).

**(4)** Salve.

**Resultado esperado:** o código da cor é gerado automaticamente no padrão PER\_<SISTEMA>\_<ID> e a cor passa a aparecer no popup Insere Tinta.

**Avisos:** nome repetido para o mesmo produto/sistema → “Já existe uma cor com o nome <nome>.”; Lazzumix sem embalagem → “Para Lazumix é obrigatória a indicação de embalagem.” Cores personalizadas ficam vinculadas a um cliente específico.

#### 3.4 Produzir a tinta — tela Colorista

**Tintométrico » Colorista**

**(1)** A tela lista os itens vendidos com uma TOP marcada como “considerada no Colorista” e ainda não produzidos.

**(2)** Selecione o item e clique em Assumir Produção — grava o usuário responsável; a partir daí, só quem assumiu continua o item.

**(3)** Manipule a tinta na máquina conforme a fórmula exibida.

**(4)** Clique em Imprimir Etiqueta (exige MODETIQUETA configurado) — atenção: imprimir a etiqueta já marca o item como produzido.

**(5)** Ou clique direto em Marcar como Produzida, se não precisar imprimir etiqueta.

![Imagem 7: (5) Ou clique direto em Marcar como Produzida, se não precisar imprimir etiqueta.](https://ajuda.sankhya.com.br/hc/article_attachments/44363131634583)

Imagem: Tela Colorista — grid Tinta Produzida e Componentes, exemplo preenchido.

**Resultado esperado:** o item sai da fila do Colorista; ficam gravados o usuário e a data/hora de produção.

A tela atualiza sozinha a cada TIMEREFRESHCOL milissegundos (padrão 30s), e também pode ser atualizada manualmente.

#### 3.5 Reclassificação de estoque (opcional)

**Tintométrico » Reclassificação**

![Imagem 8: Tintométrico » Reclassificação](https://ajuda.sankhya.com.br/hc/article_attachments/44363109703447)

Imagem: Tela Reclassificação — cadastro de embalagem (exemplo).

Use apenas se a loja controla estoque de matéria-prima tintométrica, com DVC\_RECLASSIFCA ligado e a TOP com Gera Reclassificação marcada.

**(1)** Venda e produza a tinta normalmente (passos 3.1 a 3.4).

**(2)** O job agendado (por volta das 19h) gera duas notas por empresa: uma de saída dos componentes usados (bases/pigmentos) e uma de entrada da tinta acabada.

**(3)** Confira no cabeçalho da nota original os campos de Entrada/Saída Reclassificação para saber se já foi processada.

Sem MODENTRRECLASS e MODMSAIRECLASS preenchidos com o número dos modelos de nota, o job bloqueia pedindo para configurar a preferência.

### 4. Integrações

O módulo integra o Sankhya com o catálogo de cada fabricante de tinta. Todas as integrações são ativadas na mesma tela, Configuração dos Fabricantes (veja o passo a passo em 2.2); o que muda de marca para marca é a forma de envio dos dados.

| Fabricante (código) | Como integra | Arquivos | Processamento |
| --- | --- | --- | --- |
| Suvinil (SU) | API SelfColor | Nenhum — busca direto na API | Assíncrono, em segundo plano |
| Lazzumix (LZ) | Upload de arquivo | 2 arquivos (Produto + Fórmula) | Síncrono |
| Montana (MO) | Upload de arquivo | 4 arquivos, um por família, um de cada vez | Síncrono |
| Sumaré (SM) | Upload de arquivo | 1 arquivo | Síncrono |
| Marfim (MA) | Upload de arquivo | 1 arquivo | Síncrono |
| Iquine (IQ) | Upload de arquivo | 1 arquivo | Síncrono |
| Sherwin-Williams (SW) | Upload de arquivo | 1 arquivo | Síncrono |

#### Fluxo ponta a ponta (qualquer marca)

- O fabricante disponibiliza o catálogo (arquivo para download ou API).
- A loja aciona a integração pelo Sankhya, na tela Configuração dos Fabricantes.
- O Sankhya processa o arquivo (ou a resposta da API) e grava cores, bases, pigmentos, embalagens e fórmulas nas tabelas internas do módulo.
- As cores importadas são consolidadas na base usada pelo popup de venda.
- A loja cadastra manualmente os produtos correspondentes na aba Tintométrico (passo 2.3) — esse vínculo não é criado sozinho pela integração.
- A partir daí, o fluxo de venda (seção 3) já enxerga o catálogo importado e os produtos cadastrados.

#### Por que a Suvinil funciona diferente

O catálogo da Suvinil chega a cerca de 100 MB. Processar esse volume dentro da mesma requisição do usuário estourava o tempo limite do navegador/gateway (erro 504). Por isso, só para essa marca, a integração roda em segundo plano: a tela libera na hora e o usuário é avisado pela Central de Avisos quando o processamento terminar — com sucesso (“Integração concluída com sucesso em <data>.”) ou com falha (“Falha na integração: <mensagem>.”).

### 5. Dicas e boas práticas

- Cadastre o produto assim que integrar um fabricante novo. Sem o vínculo manual na aba Tintométrico, a cor existe no catálogo mas não pode ser vendida.
- Marque “Top é considerada na tela do Colorista” em toda TOP de venda de tinta. É a causa mais comum de “o pedido não aparece no Colorista”.
- Configure o MODETIQUETA antes de liberar a produção. Sem ele, a impressão de etiqueta fica bloqueada na tela do Colorista.
- Confira o Fator de Conversão de cada marca separadamente, se a loja trabalha com mais de um fabricante — ele é específico por marca e não se repete entre elas.
- Cores personalizadas ficam vinculadas a um cliente. Para usar a mesma fórmula em outro cliente, cadastre a cor novamente.
- Só ligue DVC\_RECLASSIFCA e configure os modelos de nota se a loja realmente controla estoque de matéria-prima tintométrica — caso contrário, deixe desligado para não gerar notas de ajuste desnecessárias.
- Após integrar a Suvinil, espere a notificação na Central de Avisos antes de considerar o catálogo atualizado — a tela libera na hora, mas o processamento continua rodando em segundo plano por alguns minutos.
- Revise sempre o Colorista com dois usuários distintos em operação, se a loja tiver mais de um responsável pela manipulação: assim que um assume a produção de um item, ele sai da fila dos demais, evitando retrabalho.
