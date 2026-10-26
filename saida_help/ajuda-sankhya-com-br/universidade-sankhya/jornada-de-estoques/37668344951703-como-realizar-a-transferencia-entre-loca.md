---
id: "37668344951703"
titulo: "Como realizar a transferência entre locais com emissão de nota (transferência entre empresas)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas"
trilha: "Universidade Sankhya > Jornada de Estoques"
atualizado_em: "2026-07-29T19:12:09Z"
rotulos: ["Produtos", "Parceiro", "Nota Fiscal", "Estoque", "Financeiro", "Transferência"]
---

# Como realizar a transferência entre locais com emissão de nota (transferência entre empresas)

| Categoria |
| --- |
| [O que é e qual o objetivo de realizar transferência entre locais com emissão de nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas#h_01KEYFE19HJ1VZ6NPNY98H1WN1) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas#h_01KEYFDJS6YDNX8YCWZF8MF1B0) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas#h_01KFBTC4X10MHD1J3THH6ESJ5J) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas#h_01KEYFD18SNMQYA599Q3D2Y95X) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas#h_01KEYFCKCZX6S9AV2Q0CQBAVS3) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37668344951703-Como-realizar-a-transfer%C3%AAncia-entre-locais-com-emiss%C3%A3o-de-nota-transfer%C3%AAncia-entre-empresas#h_01KEYFBCRGMWTVFC5XE0GP4BV3) |

## Transferência entre Locais com emissão de Nota

#### O que é e qual o objetivo de realizar transferência entre locais com emissão de nota?

Refere-se ao registro das movimentações do produto entre diferentes locais de armazenamento da empresa, ou entre empresas (matriz/filial), como por exemplo transferências de produtos da empresa matriz para filial, transferências do depósito fechado para a loja, transferências do local depósito para o local prateleira, alteração de local entre as prateleiras, etc. 
Tipicamente, as operações de transferência baixam o estoque no local de origem (saída) e realizam uma entrada de estoque correspondente no local de destino (entrada). No sistema, as operações de transferências exigem que o usuário indique os locais de origem e destino e já realiza, automaticamente, a movimentação de estoque correspondente. O objetivo desta prática de registrar corretamente as transferências de produtos é garantir o controle preciso do estoque entre diferentes locais de armazenamento, assegurando a rastreabilidade e a integridade das informações.

#### Quais problemas este recurso resolve?

- **Inconsistência no estoque**: Diferenças entre o estoque físico e o registrado, impactando o controle e a confiabilidade das informações.
- **Falta de rastreabilidade**: Dificuldade em identificar o histórico e localização dos produtos movimentados.
- **Erros manuais e retrabalho**: Lançamentos incorretos ou esquecidos que geram retrabalho e baixa produtividade.
- **Decisões baseadas em dados imprecisos**: Informações erradas de estoque comprometem o planejamento e a tomada de decisões.
- **Desorganização entre setores ou unidades**: Transferências descontroladas geram falhas operacionais e atrasos internos.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1068117868)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa **Axis** identificou a necessidade de transferir uma quantidade de produtos para sua filial **ABC**, para atender um pedido de compra realizado pelo **Ideal Max**. Para isso será necessário realizar a transferência de mercadoria entre empresas oficializando a operação por meio da emissão de uma nota fiscal. 

**Tarefa:** Emitir uma nota fiscal de transferência entre empresas registrando tanto a saída quanto a entrada. 

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Para registrar a saída, acesse a tela **Portal de Vendas**
   Menu: Comercial » Consulta » Portal de Vendas

- Selecione o **Tipo de Movimento** igual a **Venda**.
- Clique no ícone de seta ao lado do campo Novo Documento(**+**) e selecione a TOP de **Transferência entre Filiais - Saída** do tipo de movimento = V-Venda.

**Observação**: Valide se os campos da seção **Geração de Nota de Remessa na Confirmação** da tela Tipo de Operação -TOP (Menu: Comercial » Arquivo » Cadastros) estão devidamente configurados, assegurando que o registro da entrada seja executado de forma automática. 

- Preencha os dados do cabeçalho da nota e o painel de itens.

**Observação:** Lembre-se de indicar no campo **Parceiro Destinatário** o código do cadastro da empresa na qual será registrada a entrada da mercadoria.

- Clique em **Confirmar**.

2. Acesse a tela **Portal de Compras**
   Menu: Comercial » Consulta » Portal de Compras

- Filtre o **número único** da nota gerada automaticamente como entrada no processo de transferência.
- Dê um duplo clique sobre o registro para acessar diretamente a **Central de Compras** e visualizar os detalhes da nota.
- Altere o campo **Parceiro**, informando o código da empresa de origem da transferência — ou seja, a unidade de onde a mercadoria foi enviada.
- Clique em **Confirmar**.

3. **Valide os saldos dos estoques transferidos**

- Acesse a tela **Gerência de Produtos**
  Menu: Comercial » Gerente » Gerência de Produtos
- Informe no campo **Produto** o produto utilizado na movimentação.
- No campo **Período de negociação**: Quando não é informado nenhum filtro no campo, o sistema, por padrão, retorna os lançamentos dos últimos 120 dias.
- Selecione o **Grupos TOP** e em seguida clique em **Aplicar**.
- Carregando as informações referente os filtros indicados.
- Selecione a Aba “**Estoque**” apresenta os dados das movimentações independente do filtro feito no Grupo TOP, desde que a TOP's que tenham sido utilizadas nos lançamentos, estejam configuradas para atualizarem estoque.

#### Correção e Repetição

- Valide os saldos dos estoques transferidos e as informações estão corretas e coerentes com as notas fiscais emitidas.
- Realize a transferência de novos produtos para exercitar.
- Caso haja erro nos registros, refaça a atividade seguindo o passo a passo novamente.
