---
id: "37646645325207"
titulo: "Como validar as atualizações geradas devolução de compra"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37646645325207-Como-validar-as-atualiza%C3%A7%C3%B5es-geradas-devolu%C3%A7%C3%A3o-de-compra"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:00Z"
rotulos: ["Configuração", "Devolução de Compra", "DANFE", "Impostos", "Estoque", "Financeiro"]
---

# Como validar as atualizações geradas devolução de compra

| Categoria |
| --- |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37646645325207-Como-validar-as-atualiza%C3%A7%C3%B5es-geradas-devolu%C3%A7%C3%A3o-de-compra#h_01KFBNHWVMKQC525YM40RJ02JA) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37646645325207-Como-validar-as-atualiza%C3%A7%C3%B5es-geradas-devolu%C3%A7%C3%A3o-de-compra#h_01KEW6ZYEWHAW9KB00YCBMZGJ7) |
| [Chegou a sua vez! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37646645325207-Como-validar-as-atualiza%C3%A7%C3%B5es-geradas-devolu%C3%A7%C3%A3o-de-compra#h_01KEW70RW1ZH21GV1ZPYCCXMPR) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37646645325207-Como-validar-as-atualiza%C3%A7%C3%B5es-geradas-devolu%C3%A7%C3%A3o-de-compra#h_01KEW73CNFSZS7EXPVPS23FB57) |

## Validação das atualizações geradas, devolução de compra - Estoque, Financeiro, impostos e DANFE

##### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1066968558)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Após realizar a devolução total da Nota de Compra registrada no Portal de Compras, referente ao pedido com produtos divergentes e avariados (conforme cenário da aula anterior), a compradora da **Axis** precisa validar se todas as atualizações geradas no processo foram registradas corretamente. 

Essa validação é essencial para garantir que o estoque, o financeiro, os impostos e a emissão da DANFE estejam em conformidade com as normas fiscais e internas da empresa. 

Um processo de devolução completo não termina apenas com a emissão da nota; é fundamental confirmar que todas as áreas impactadas foram devidamente ajustadas para evitar inconsistências futuras**.**

**Tarefa:** Valide se as informações no **Estoque**, no **Financeiro**, nos **Impostos** e na **DANFE** foram atualizadas corretamente após a devolução. Siga as instruções abaixo para realizar a conferência de cada etapa.

#### Chegou a sua vez! Realize as movimentações no ERP Sankhya

1. **Validação do estoque**

- Acesse a tela **Gerência de Produtos**
  Menu: Comercial » Gerente » Gerência de Produtos

- Para visualizar as informações corretamente, preencha os campos no painel **Filtros Rápidos**:
- **Produto**: Informe o **produto** devolvido anteriormente.
- **Período de Negociação:** Defina o período **inicial e final** da análise.
- **Grupo TOP:** Selecione os grupos de **TOP’s relevantes**. Para análise de compras, marque os grupos relacionados ao movimento de entrada.
- Controle por Embalagem: Se o produto possui controle adicional, selecione essa opção.
- O campo **Local** pode ser preenchido para visualizar as informações do produto em um local específico no estoque.

Analise os dados por meio das abas.

**Aba Extrato**

- Movimentações configuradas para atualizar estoque - independentemente do filtro de Grupos de TOP aplicado -.
- Verifique nas colunas **Nro.Nota** e **Qtd. Neg** as movimentações ocorridas no registro das notas de compra e devolução.

2. **Validação do financeiro**

- Acesse a tela **Portal de Compras**
  Menu: Comercial » Consulta » Portal de Compras

- No campo **Tipo de Movimento** localizado na porção superior esquerda, selecione **Devolução de Compra**.
- Utilize os “**Filtros rápidos” (Data de Negociação, Data do Movimento ou Número Único)** para localizar a nota.
- Selecione o registro correspondente com um duplo clique.

O sistema irá direcioná-lo para a tela **Central de Compras**. 

- Na aba **Financeiro**, clique em "**Mov. Financeira**", localizada no rodapé da tela,

O sistema irá direcioná-lo para a tela **Movimentação Financeira**.

- Dê um duplo clique sobre o registro apresentado.
- No menu lateral, clique na aba **Lançamento** para visualizar os detalhes da nota de devolução.

**Valide as Informações:**

- Confirme se a movimentação gerou a **despesa** corretamente..
- Verifique se o valor do desdobramento está correto
- Analise se o **Tipo de Título** está adequado.
- Confira o **Tipo de Negociação** aplicado no lançamento.

3. **Validação do Impostos**

- Na tela **Central de Compras** é possível realizar a validação de duas formas:

**Validação pelo Rodapé – Aba Impostos:**

- Exibe o agrupamento de impostos de todos os produtos da devolução.
- Permite visualizar a carga tributária total aplicada.

**Validação Individual – Grade de Itens:**

- Selecione um produto e clique no botão **Outras opções (...)**, selecione a opção **Consultar/Alterar Dados do Imposto do Item**.
- Na janela aberta, selecione o imposto, que será validado e confira os campos disponíveis para garantir que estão corretos e calculados devidamente.

4. **Validação do DANFE**

- Na tela **Central de Compras** siga os passos:

- Clique no botão “**Pré-Visualizar**”, localizado no canto superior esquerdo
- Selecione a opção **Pré-Visualizar Nota** para exibir o DANFE.

Após a visualização, valide todas as informações fiscais da nota, incluindo **impostos (ICMS, IPI, PIS, COFINS e ISS), valores bruto e líquido, base de cálculo, quantidade de produtos e dados do parceiro** para garantir a conformidade.

#### Correção e Repetição

- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Verifique as configurações da TOP de Devolução de Compras
- Analise as informações no Portal de Compras e na Central de Compras.
- Para praticar, experimente criar novamente nova Nota de Compra, com outros produtos, quantidades e fornecedores, para realizar a Devolução de Compras.
