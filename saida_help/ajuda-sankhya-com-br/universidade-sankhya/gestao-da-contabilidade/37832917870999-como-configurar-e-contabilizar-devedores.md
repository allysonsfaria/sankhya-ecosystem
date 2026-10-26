---
id: "37832917870999"
titulo: "Como configurar e contabilizar Devedores Duvidosos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37832917870999-Como-configurar-e-contabilizar-Devedores-Duvidosos"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-07-22T14:07:20Z"
rotulos: ["Configuração", "Movimentação Financeira", "Contabilização", "Preferências", "Financeiro"]
---

# Como configurar e contabilizar Devedores Duvidosos

#### Contabilização de Devedores Duvidosos

A contabilização da Provisão para Devedores Duvidosos (PDD) tem como objetivo registrar de forma preventiva as possíveis perdas decorrentes da inadimplência de clientes. No ERP Sankhya, esse processo permite que os valores de títulos vencidos há longos períodos sejam provisionados automaticamente, refletindo a realidade financeira da empresa com maior prudência. Ao aplicar essa prática, a gestão assegura que as demonstrações contábeis — como o DRE e o Balanço Patrimonial — representem não apenas os direitos a receber, mas também os riscos associados à sua realização.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118227983)

#### Cenário de aplicação

A empresa Axis LTDA., do segmento atacadista, possui um volume significativo de vendas a prazo. Com o aumento da inadimplência e a existência de títulos vencidos há mais de 180 dias, o setor financeiro identificou a necessidade de adotar controles mais rigorosos. Para atender aos princípios contábeis de prudência e transparência, a gestão decidiu implementar no ERP Sankhya a contabilização da Provisão para Devedores Duvidosos (PDD), assegurando que as perdas potenciais sejam refletidas de forma adequada nas demonstrações financeiras.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo abaixo para configurar os parâmetros da PDD no sistema. Defina critérios como prazos de inadimplência e percentuais estimados de perda, garantindo que os lançamentos contábeis sejam gerados corretamente e integrados ao DRE e ao Balanço Patrimonial.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Preferências** 
   **Menu:** Configuração  »  Avançado  »  Preferências

- Digite o parâmetro **DIASDEVDUVIDOSO** no campo (Chave ou Descrição e tecle ENTER) e pressione **ENTER** para carregar as informações.
- No campo **Interio** informe o valor **180**.
- Salve a alteração.

2. Acesse a tela **Movimentação Financeira**

**Menu:** Financeiro  »  Rotinas  »  Movimentação Financeira

- No menu principal superiot, acione o botão “**+ Filtros**”.
- Abra a aba de Filtros rápidos e selecione Receitas.
- Defina no campo de vencimento o período correspondente aos últimos 180 dias até a data atual.
- Selecione o registro com um duplo clique.
- No menu lateral, acesse a aba **Outras informações**.
- Localize o campo PDD e realize a marcação.
  Realize a marcação em todos os lançamentos filtrados.

3. Acesse a tela **Contabilização de Devedores Duvidosos**

**Menu:** Contabilização  »  Arquivos »  Contabilização de Devedores Duvidosos

- Na seção Filtros rápidos informe:

  - Empresa
  - Data Movimento
  - Numero do lote
  - Debitar (conta responsável pela perda de crédito) PERDAS CREDITO LIQUIDEZ DUVIDOSA
  - Creditar (conta redutora do ativo de contas a receber) ( - ) PCLD
  - Dias atraso (alimentado pelo valor definido na preferência DIASDEVDUVIDOSO)
- Acione o botão “**Aplicar**” para buscar os lançamentos.
- Clique em “**Contabilizar**”.
  Neste momento um pop-up Informação sinalizará a efetividade do processo.

4. Acesse a tela **Lotes Contábeis**

**Menu:** Contabilidade  »  Arquivos »  Lotes Contábeis

- Na seção Filtros rápidos, informe no campo Intervalo de Lotes, o lote gerado na Contabilização de Devedores Duvidosos.
- Aplique o filtro para buscar o lote gerado.
- Selecione o lote desejado com um clique e pressione o teclado ctrl + L.

No menu principal, acione o botão “**...**” (**Outras** **opções…**) e selecione a opção **Visualizar Lançamentos (Ctrl** **+ L)**.
