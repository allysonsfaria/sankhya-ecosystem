---
id: "37833110894487"
titulo: "Como registrar lançamentos contábeis manuais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37833110894487-Como-registrar-lan%C3%A7amentos-cont%C3%A1beis-manuais"
trilha: "Universidade Sankhya > Gestão da Contabilidade "
atualizado_em: "2026-10-08T12:54:59Z"
rotulos: ["Configuração", "Contabilidade", "Preferências", "Financeiro", "Lançamentos Contábeis"]
---

# Como registrar lançamentos contábeis manuais

| Categoria |
| --- |
| [Registro de lançamentos contábeis manuais](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833110894487-Como-registrar-lan%C3%A7amentos-cont%C3%A1beis-manuais#h_01KFGPVV4H4TRMRQMXHH3H715P) |
| [Demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833110894487-Como-registrar-lan%C3%A7amentos-cont%C3%A1beis-manuais#h_01KFGPTTP8KD6FV9QYYRHXA4C6) |
| [Cenário de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833110894487-Como-registrar-lan%C3%A7amentos-cont%C3%A1beis-manuais#h_01KFGPV3E51KQ1EFNY6V9RC26E) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37833110894487-Como-registrar-lan%C3%A7amentos-cont%C3%A1beis-manuais#h_01KFGPVCBEH9A9BQ5Z6TZBQPPR) |

#### Registro de lançamentos contábeis manuais

O lançamento contábil manual no ERP Sankhya é um recurso que permite registrar diretamente na contabilidade movimentações que não são originadas de módulos integrados, como compras, vendas ou financeiro. Ele é utilizado em situações específicas, como ajustes de saldo, provisões, reclassificações ou lançamentos de encerramento contábil. Essa prática garante que todas as ocorrências relevantes da empresa, mesmo aquelas que não possuem um documento de origem no sistema, sejam refletidas de forma precisa no razão contábil. Ao dominar esse procedimento, a equipe assegura a integridade das informações contábeis e mantém as demonstrações financeiras alinhadas à realidade da operação.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1118204633)

#### Cenário de aplicação

A empresa Axis LTDA. possui em seu ativo imobilizado diversos veículos utilizados nas operações. No fechamento contábil, foi identificada a necessidade de registrar a depreciação mensal de um desses bens, operação que não é gerada automaticamente pelo sistema. Para que as demonstrações financeiras reflitam corretamente a redução do valor patrimonial do ativo, será necessário realizar um lançamento contábil manual.

**Tarefa:** assista ao vídeo de demonstração prática e siga o passo a passo abaixo para configurar e gerenciar lotes contábeis manuais. Registre a depreciação do veículo no sistema, garantindo que o lançamento seja corretamente agrupado, documentado e rastreado, em conformidade com as exigências contábeis e com as práticas de controle patrimonial da empresa.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Preferências** 
   **Menu:** Configuração  »  Avançado  »  Preferências

- Digite o parâmetro **USALANCPART** no campo (Chave ou Descrição e tecle ENTER) e pressione **ENTER** para carregar as informações.
- No campo **Ligado/Desligado** selecione **Ligado**.
- Salve a alteração.

2. Acesse a tela **Lotes Contábeis**

**Menu:** Contabilidade  »  Arquivos »  Lotes Contábeis

- Clique em “**+**” (**Cadastrar** **Mestres de Lotes**).
- Preencha os campos:

  - **Nro. Lote**
  - **Referência**
  - **Dt. Movimento**
- Salve o registro.
- Selecione o lote gerado com um clique e pressione o teclado ctrl + L.
- No menu principal, acione o botão “**...**” (**Outras** **opções…**) e selecione a opção **Visualizar Lançamentos (Ctrl** **+ L)**.

3. Acesse a tela **Lançamentos Contábeis**

**Menu:** Contabilidade  »  Arquivos » Lançamentos Contábeis

**Para realizar lançamento em Multiplas Partidas**

- Clique em “**+**” (**Novo** **Lançamento**).
- Na janela Lançamento contábil, Informe:
- **Forma de Lançamento Contábil:** Multiplas Partidas

  - **Data Movimento**
  - **Num. Lote**
  - **Num. Documento**
- Na aba Múltiplas Partidas informe:

**1ª Partida**

- **Conta Contábil (Red)**
  Ex.: DEPRECIACAO DE VEICULOS
- Determine se o lançamento será a **Débito** ou **Crédito** alimentando o valor no campo correspondente.
  Ex.: Valor Débito 200
- **Cód. Histórico**
  Ex.: DEPRECIACAO MENSAL
- Salve o registro.

**2ª Partida**

- **Conta Contábil (Red)**
  Ex.: ( - ) DAC VEICULOS
- Determine se o lançamento será a **Débito** ou **Crédito** alimentando o valor no campo correspondente.
  Ex.: Valor Crédito 200
- **Cód. Histórico**
  Ex.: DEPRECIACAO MENSAL
- Salve o registro.

Neste Lançamento Contábil é fundamental a Diferença dos valores totais estar zerada

- Na porção inferior da janela Lançamento contábil, acione o botão “**Salvar**” para finalizar

**Para realizar lançamento em Partida Dobrada**

- Clique em “**+**” (**Novo** **Lançamento**).
- Na janela Lançamento contábil, Informe:
- **Forma de Lançamento Contábil:** Partida Dobrada

  - **Data Movimento**
  - **Num. Lote**
  - **Num. Documento**
- Na aba Partida Dobrada  informe:

**Seção Débito**

- **Conta Contábil (Red)**
  Ex.: DEPRECIACAO DE VEICULOS
- **Cód. Histórico**
  Ex.: DEPRECIACAO MENSAL

**Seção Crédito**

- **Conta Contábil (Red)**
  Ex.: ( - ) DAC VEICULOS
- **Cód. Histórico**
  Ex.: DEPRECIACAO MENSAL

**Seção Dados Gerais**

- Informe o **Valor Lançamento**
  Ex.: 1.000,00
- Na porção inferior da janela Lançamento contábil, acione o botão “**Salvar**” para finalizar

Independentemente da forma de lançamento contábil, é obrigatório preencher os campos essenciais para controle gerencial (como Centro de Resultado, Projeto e Empresa de Origem) sempre conforme o contexto e a realidade da empresa.
