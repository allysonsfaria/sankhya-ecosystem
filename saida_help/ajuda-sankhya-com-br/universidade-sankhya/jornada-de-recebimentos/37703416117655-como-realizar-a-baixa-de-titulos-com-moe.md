---
id: "37703416117655"
titulo: "Como realizar a baixa de títulos com moeda estrangeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira"
trilha: "Universidade Sankhya > Jornada de Recebimentos"
atualizado_em: "2026-09-17T15:11:51Z"
rotulos: ["Configuração", "Moeda", "Movimentação Financeira", "Financeiro", "ERP Sankhya"]
---

# Como realizar a baixa de títulos com moeda estrangeira

| Categoria |
| --- |
| [O que é e como funciona a baixa de títulos com moeda estrangeira?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AXQA1FYGASY7ZA5HJ85PS) |
| [Quais problemas são resolvidos com essa prática?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AXDHETHYYST2PJGHMAZSG) |
| [Quais os riscos de não a utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AX7TCNXCV8H0CGF87G0NC) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AX1HETJ03QMFZYT4F7SCN) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AWWJJ90Q02E7VY70DQKBA) |
| [Hora de colocar a mão na massa! Realize as movimentações necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AWGAM9JN2SCXMDS0PTP1S) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37703416117655-Como-realizar-a-baixa-de-t%C3%ADtulos-com-moeda-estrangeira#h_01KF1AW1806HBS33VTKTF9YNBV) |

## Baixa de títulos com moeda estrangeira

#### O que é e como funciona a baixa de títulos com moeda estrangeira?

Este procedimento permite registrar a liquidação de títulos financeiros em moedas diferentes da moeda funcional da empresa. Durante o processo, o sistema considera a conversão cambial, aplicando as taxas de câmbio configuradas para calcular o valor equivalente na moeda principal.
Além disso, a funcionalidade oferece flexibilidade para lidar com múltiplas moedas e automatiza a conversão cambial, reduzindo erros e aumentando a eficiência. Também garante confiabilidade nos registros financeiros e proporciona um controle claro das transações internacionais, permitindo uma gestão financeira mais organizada e precisa.

#### Quais problemas são resolvidos com essa prática?

- **Falta de controle sobre transações internacionais:** proporciona um processo padronizado e confiável para lidar com pagamentos e recebimentos em moeda estrangeira.
- **Erros de conversão cambial:** sem um processo automatizado, calcular e aplicar taxas de câmbio manualmente pode gerar erros nos valores registrados.
- **Dificuldade em integrar transações:** facilita a integração das transações em moeda estrangeira com os relatórios contábeis e financeiros.
- **Desorganização nos registros:** garante a rastreabilidade e a conformidade das transações com normas internacionais.

#### Quais os riscos de não a utilizar?

A falta de um processo adequado para a baixa de títulos com moeda estrangeira pode acarretar diversos riscos significativos. Entre eles, estão as inconsistências nos registros financeiros, já que a inexistência de um procedimento padronizado pode levar a erros nos cálculos de conversão cambial, comprometendo a confiabilidade dos relatórios. Empresas que não seguem práticas apropriadas também podem enfrentar sanções ou dificuldades durante auditorias fiscais e financeiras, resultando em desconformidade legal. A ineficiência na gestão das transações internacionais ainda pode levar à perda de competitividade, dificultando a atuação da empresa em mercados globais.

#### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1057573790)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A **Axis** recebeu recentemente um pagamento em dólares americanos (USD) de um parceiro. O valor refere-se a uma venda já registrada no sistema, e agora o setor financeiro precisa registrar a baixa do título no ERP Sankhya, aplicando corretamente a conversão cambial com base na taxa do dia da transação.
O objetivo é garantir que o lançamento reflita corretamente o valor em reais, de forma consistente com as configurações de moeda estrangeira no sistema.

**Tarefa:** Realize a baixa do título recebido em dólares no ERP Sankhya, aplicando a conversão cambial do dia da transação e garantindo que os valores sejam corretamente registrados em moeda nacional.

#### Hora de colocar a mão na massa! Realize as movimentações necessárias

1. **Conferência de informações no título**

- Acesse a tela **Movimentação Financeira**
  Menu: Financeiro » Rotinas » Movimentação Financeira.
- Localize um título pendente para simular a baixa. Utilize os filtros para busca:

  - Marque as seguintes opções: Receitas, Real, Pendentes.
  - Abra o título e na aba **Geral**, preencha o campo **Moeda** com o código da moeda cadastrada previamente.
  - Verifique se no campo **Vlr Moeda** o sistema atualizou a cotação configurada anteriormente.

2. **Baixa do título**

- Clique no botão **Baixar**.
- No quadrante **Moeda Estrangeira**, valide as informações:
- **Valor da moeda:** se refere ao valor cadastrado da moeda cadastrado anteriormente.
- **Valor de desdobramento da moeda:** valor do título considerando a moeda utilizada na baixa, por exemplo, se o dólar tem a cotação de R$ 6,20, e o título tem um valor de R$ 1.000,00 então esse campo teria o valor $ 161,29.
- **Desdobramento:** Valor do título na moeda padrão utilizada pela empresa.
- Confira as seguintes informações em **Dados básicos**:
- **Data de Baixa:** Data atual
- **Conta Bancária**
- **TOP**
- Clique em **Baixar título**

3. **Validação dos resultados**

- Localize o campo **Vlr Moeda na Baixa** e verifique se ele foi atualizado com as informações definidas anteriormente.

#### Correção e Repetição

- Verifique se após a baixa as informações da moeda foram registradas no título.
- Repita a operação com outro título financeiro para reforçar o que aprendeu.
