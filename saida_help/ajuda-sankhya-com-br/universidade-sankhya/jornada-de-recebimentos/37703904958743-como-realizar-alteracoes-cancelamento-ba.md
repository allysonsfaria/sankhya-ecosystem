---
id: "37703904958743"
titulo: "Como realizar alterações, cancelamento, baixa e conciliação de boletos rápidos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos"
trilha: "Universidade Sankhya > Jornada de Recebimentos"
atualizado_em: "2026-10-01T20:02:06Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Boleto", "Financeiro", "API", "Artigo atualizado KCS", "Financeiro - KCS"]
---

# Como realizar alterações, cancelamento, baixa e conciliação de boletos rápidos

| Categoria |
| --- |
| [O que é e como funciona o processo de alterações, cancelamento, baixa e conciliação de boletos rápidos?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BJJZ6AZ40W5SZEPCN8KKK) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BJ61QFRM095NGX3ZSVP4D) |
| [Quais os riscos de não utilizar essa prática?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BHZC2T08TZXNX1FSYA6Q8) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BHQPN7SNQVV26AZPARHA8) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BHG4Z270DWPWD6CKRTAVG) |
| [Em seguida, você verá o passo a passo para configurar e aplicar o processo corretamente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BH7Q8NA1ACF3DF3BQ4TJ6) |
| [Alterações nos boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BH2QMR9T87FKRQWS41T5C) |
| [Cancelamento de boletos](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BGWBNSWQCA5D0BMHZXAS0) |
| [Baixa e conciliação de boletos rápidos](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BGNN42Z97SR4ZJJWEG3DC) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703904958743-Como-realizar-altera%C3%A7%C3%B5es-cancelamento-baixa-e-concilia%C3%A7%C3%A3o-de-boletos-r%C3%A1pidos#h_01KF1BG8KBM2FVP28E2VTZ6ZJJ) |

## Bolepix Boleto rápido - API (Banco do Brasil, Itaú e Santander)

#### O que é e como funciona o processo de alterações, cancelamento, baixa e conciliação de boletos rápidos?

No Sankhya, o processo de alterações e cancelamento de boletos rápidos, é totalmente integrado e automatizado e mantêm comunicação direta com o banco, eliminando a necessidade de enviar arquivos manualmente para registrar mudanças ou cancelamentos.
Quando uma alteração é feita, como a prorrogação de vencimento ou atualização do valor, o sistema comunica automaticamente o banco, garantindo que as informações sejam atualizadas em tempo real. No caso de cancelamento, o boleto é imediatamente invalidado, e o banco recebe a solicitação de forma instantânea, evitando qualquer risco de pagamento por parte do cliente.

Além disso, quando o pagamento de um boleto é identificado, o sistema realiza automaticamente a baixa e a conciliação, garantindo que os registros financeiros estejam sempre atualizados e corretos.

#### Quais problemas este recurso resolve?

- **Lentidão nos processos manuais:** automatiza alterações e cancelamentos, eliminando a necessidade de enviar arquivos para o banco, o que reduz o tempo de processamento e aumenta a eficiência operacional.
- **Erros e inconsistências nos registros:** garante que todas as alterações ou cancelamentos sejam registrados e comunicados ao banco de forma automática e precisa, evitando, problemas como pagamentos de boletos com dados incorretos.
- **Risco de pagamento indevido:** cancela boletos diretamente no sistema e informa o banco em tempo real, invalidando qualquer tentativa de pagamento de boletos cancelados.
- **Falta de controle sobre atualizações de boletos:** proporciona uma gestão centralizada e confiável, permitindo que a empresa acompanhe todas as modificações ou cancelamentos realizados.
- **Baixa e conciliação manuais:** sem a automação, o reconhecimento de pagamentos e a atualização de registros financeiros exigem mais esforço e são mais suscetíveis a erros, o que compromete a precisão e o controle.

#### Quais os riscos de não utilizar essa prática?

Sem o recurso de alterações e cancelamento automatizado de boletos rápidos, a empresa está sujeita a erros nos registros, como boletos desatualizados ou cancelamentos não informados ao banco, resultando em pagamentos indevidos e retrabalho. A ausência de baixa e conciliação automáticas agrava esses problemas, exigindo conferências manuais que aumentam a chance de inconsistências e atrasos no controle financeiro.
A ineficiência operacional também aumenta, já que realizar esses processos manuais demandam mais tempo e esforço, impactando a produtividade da equipe. Além disso, atrasos na atualização dos boletos podem comprometer o fluxo de caixa e dificultar o controle financeiro.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1057573841)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa emite diariamente diversos boletos para seus clientes. Certo dia, um cliente solicita a prorrogação do vencimento de um boleto. Sem o recurso de boletos rápidos, o analista financeiro precisaria ajustar o vencimento manualmente, enviar o arquivo ao banco e reenviar o boleto atualizado, correndo o risco de atrasos e erros.
Com a funcionalidade de boletos rápidos no Sankhya, o analista acessa o sistema, atualiza a data de vencimento com poucos cliques, e o banco é automaticamente notificado. Em minutos, o cliente recebe o boleto atualizado com o novo vencimento e o QR code para pagamento via PIX, sem complicações.

No mesmo dia, outro cliente informa que precisa cancelar um boleto. O analista realiza o cancelamento diretamente no sistema, e o banco é imediatamente comunicado, invalidando o boleto e evitando possíveis pagamentos indevidos.

**Tarefas:**

1. Selecione um título com boleto rápido emitido e altere sua data de vencimento. Em seguida, cancele outro boleto já emitido e verifique se as alterações foram corretamente refletidas na tela de acompanhamento de boletos.
2. Configure o sistema para que as baixas e conciliações sejam automáticas ao receber o retorno de pagamento do banco. Após isso, acesse a tela de acompanhamento de boletos para conferir se o título foi baixado corretamente e se a conciliação bancária foi realizada com sucesso.

**Aviso importante!**
A simulação exige dados reais, como conta bancária e credenciais. Por isso, não realizaremos a movimentação prática no sistema.

#### Em seguida, você verá o passo a passo para configurar e aplicar o processo corretamente

##### 1. Alterações nos boletos

- Acesse a tela **Movimentação Financeira**: 
  Menu: Financeiro » Rotinas » Movimentação Financeira.
- Utilize os filtros para localizar o título que gerou o boleto que precisa ser alterado.
- Marque as seguintes opções: Receitas, Real, Pendentes.
- Selecione o título.
  - Localize o campo **Dt. Vencimento** e altere o vencimento do boleto.
- Clique em **Salvar.**
- Acesse a tela **Acompanhamento de Boletos - API**: 
  Menu: Financeiro » Consultas » Acompanhamento de Boletos - API
- Utilize os filtros para localizar o título no qual houve a alteração do vencimento.
  - O campo **Data de Negociação** precisa ser preenchido.
- Clique em **Aplicar**.
- Selecione o título na aba **Boletos**.
  - Verifique a alteração na aba **Histórico do boleto**, o sistema gera um histórico com o retorno do banco e situação para acompanhamento.

##### 2. Cancelamento de boletos

O cancelamento do boleto é feito nas seguintes situações:

- Cancelamento da nota fiscal;
- Baixa manual;
- Renegociação do título;
- Deletar o nosso número do título.
- Acesse a tela **Movimentação Financeira**: 
  Menu: Financeiro » Rotinas » Movimentação Financeira.
- Utilize os filtros para localizar o título que gerou o boleto que precisa ser alterado.
- Selecione o título.
  - Localize o campo **Nosso Número** na aba **Cobrança** e apague a informação.
  - No aviso emitido clique em “**Sim”**.
- Clique em **Salvar**.
- Acesse a tela **Acompanhamento de Boletos - API** 
  Menu: Financeiro » Consultas » Acompanhamento de Boletos - API.
- Utilize os filtros para localizar o título no qual houve a alteração do nosso número.
  - O campo **Data de Negociação** precisa ser preenchido.
- Clique em **Aplicar**.
- Selecione o título na aba **Boletos**.
  - Verifique a alteração na aba **Histórico do boleto**, o sistema gera um histórico com o retorno do banco e situação para acompanhamento.

##### 3. Baixa e conciliação de boletos rápidos

- Acesse a tela **Contas**: 
  Menu: Configurações » Cadastros »  Bancários » Contas.
- Selecione a conta usada para emissão dos boletos rápidos.
- Na aba **Boleto(s)/Duplicatas**, confira os campos as área **Ações automáticas ao receber retorno**:
  - **Baixa automática**
  - **Lançamento baixa boleto**
  - **TOP Baixa boleto**
  - **Conciliação Automática**
  - Acesse a tela **Acompanhamento de Boletos - API**: 
    Menu: Financeiro » Consultas » Acompanhamento de Boletos - API
  - Utilize os filtros para localizar os títulos liquidados.
    - Em **Status do Boleto**, ao realizar a marcação das flags **Liquidados** e **Liquidados por PIX**, serão apresentados apenas boletos pagos.
      - O campo **Data de Negociação** precisa ser preenchido.
    - Clique em **Aplicar**.
    - Selecione um título para realizar a conferência.
    - No **Histórico do boleto**, veja a atualização de retorno do banco referente ao pagamento.
    - Acesse a tela **Movimentação Financeira**: 
      Menu: Financeiro » Rotinas » Movimentação Financeira.
    - Utilize o filtro **Nr. Único**, para localizar o título pago conferido na tela anterior.
    - Abra o título e na aba **Lançamento**, confira se o campo **Dt. Baixa** está devidamente preenchido.
    - O campo **Baixa via API** terá a seguinte descrição: **“Título baixado Automaticamente via API” -** caso esse campo não seja apresentado, verifique as configurações da tela.
    - Acesse a tela **Conciliação Bancária**: 
      Menu: Financeiro » Rotinas » Conciliação Bancária.
    - Utilize os filtros rápidos para buscar os títulos “Conciliados” e no campo **Data da Conciliação,** informe a data de baixa do título conferido anteriormente.
    - Localize o título e verifique se foi conciliado devidamente.

#### Correção e Repetição

- Para consolidar o aprendizado, simule um caso de erro intencional, como tentar cancelar um boleto já pago, para entender como o sistema responde e quais mensagens de alerta são exibidas.
