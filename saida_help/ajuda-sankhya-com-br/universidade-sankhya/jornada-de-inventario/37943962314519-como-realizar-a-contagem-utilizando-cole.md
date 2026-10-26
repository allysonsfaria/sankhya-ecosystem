---
id: "37943962314519"
titulo: "Como realizar a contagem utilizando coletor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor"
trilha: "Universidade Sankhya > Jornada de Inventário"
atualizado_em: "2026-07-22T14:04:11Z"
rotulos: ["Produtos", "Inventário", "Importação", "Estoque", "Coletor de Dados"]
---

# Como realizar a contagem utilizando coletor

| Categoria |
| --- |
| [Qual é o objetivo de se realizar a contagem por coletor de dados?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQWC8EV0745QCEPBA1AXQ0) |
| [Quais problemas esse recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQWQXET8PVMWWGXH7TQWWK) |
| [Quais os riscos de não se fazer o ajuste de estoque por série?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQWXD3EVXJ0YMFAH4XB4V9) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQX2SF4D0J527V80B7JYH4) |
| [Cenário prático e passo a passo para realizar a atividade no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQXENM3BT3EY4KFCWV4BJZ) |
| [Hora de colocar a mão na massa! Realize as movimentações necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQXN3JDYJYZ3381AAQPJNN) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37943962314519-Como-realizar-a-contagem-utilizando-coletor#h_01KFXQXVR7KYTG98J6N4GQNJHB) |

## Importação de contagem via coletar (contagem por coletor)

#### Qual é o objetivo de se realizar a contagem por coletor de dados?

A contagem de estoque com coletor de dados tem como objetivo automatizar o registro das contagens físicas, permitindo que as leituras de código de barras sejam transmitidas diretamente ao ERP Sankhya com rapidez e segurança. Isso garante agilidade, integração entre etapas e redução do esforço manual durante o processo de inventário. O uso do coletor é especialmente eficaz em estoques com grande volume de itens ou alto nível de rotatividade, proporcionando mais fluidez, organização e rastreabilidade desde a coleta até a consolidação dos dados.

#### Quais problemas esse recurso resolve?

- Erros frequentes causados por digitação manual durante a contagem.
- Processos lentos e pouco padronizados na realização de inventários.
- Falta de agilidade em estoques com muitos itens ou alta complexidade.
- Dificuldade para organizar e registrar as informações em tempo real.
- Necessidade de retrabalho por inconsistência nos registros físicos x sistema.

#### Quais os riscos de não se fazer o ajuste de estoque por série?

A ausência dessa tecnologia aumenta a exposição a erros manuais, atrasos e inconsistências nos dados registrados. Em estoques com grande volume ou produtos controlados por número de série, a contagem manual dificulta a rastreabilidade e torna o processo mais suscetível a falhas operacionais. Isso pode resultar em divergências, retrabalho, baixa eficiência na apuração dos inventários, dificuldade para atender exigências fiscais e, em última instância, prejuízos financeiros e quebra de confiança na gestão de estoque.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1051994196)

#### Cenário prático e passo a passo para realizar a atividade no sistema

**Contexto:** Durante a preparação para o inventário trimestral, a TechTools identificou a necessidade de realizar a contagem de estoque no setor de notebooks e materiais eletrônicos — itens que possuem controle por códigos de barras e números de série. Para garantir agilidade e precisão no processo, a equipe decidiu utilizar tecnologia adequada ao perfil dos produtos.

**Tarefa:** Simule a utilização do coletor de dados para realizar a contagem física dos produtos, registrando as informações de código de barras e número de série diretamente no dispositivo. Após a finalização, importe os dados para o sistema ERP Sankhya, garantindo que o estoque refletirá com precisão a situação real apurada no inventário.

#### Hora de colocar a mão na massa! Realize as movimentações necessárias

1. **Arquivo .txt**

- Acesse a tela **Produtos**
  Menu: Configurações » Cadastro » Produtos » Produtos
- Selecione um produto cadastrado em sua base de testes com um duplo clique.
- Consulte o código descrito no campo **EAN/GTIN**, localizado na aba **Geral**.
  Caso o campo esteja vazio, o sistema irá buscar o **Código de barras** na aba Unidades alternativas.
- Abra o bloco de notas.
- Insira o código de barras identificado e a quantidade do produto, os separando por vírgula. (Ex.: XXXXXXXXXXXXXX,YYY)
- Salve o arquivo.

2. **Importar dados do coletor**

- Acesse a tela **Importação de Dados Coletor**
  Menu: Inventário » Avançado » Importação de Dados Coletor
- Informe a **Data Contagem** no campo indicado.
- No campo **Arquivo de Origem**, clique em **Selecionar arquivo** e insira o arquivo txt criado no passo anterior.
- No campo **Modelo de arquivo** selecione a opção **Modelo 1**.
- Informe a **Empresa** no campo indicado.
- Informe o **Local** no campo indicado.
- Clique no botão “**Importar**”.

3. **Validar importação**

- Acesse a tela **Contagem de Estoque**
  Menu: Inventário » Arquivo » Contagem de Estoque
- Selecione a opção **Alterar uma contagem de estoque existente**.
- Clique em **Próximo**.
- Selecione a data da cópia.
- Clique em **Próximo**.
- Selecione a última contagem registrada.
- Clique em **Concluir**.

Na coluna Estoque será possível identificar a quantidade encontrada para o produto que foi feita a contagem utilizando o coletor de dados.  

#### Correção e Repetição

- Revise os registros para confirmar se as operações foram concluídas.
- Crie novos arquivos para utilizar de exemplo em outras importações.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo, retorne no vídeo demonstrativo novamente caso necessário.
