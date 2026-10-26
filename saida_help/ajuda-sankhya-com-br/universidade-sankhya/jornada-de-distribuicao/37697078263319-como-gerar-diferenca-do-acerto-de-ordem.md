---
id: "37697078263319"
titulo: "Como gerar diferença do acerto de ordem de carga para o financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro"
trilha: "Universidade Sankhya > Jornada de Distribuição"
atualizado_em: "2026-07-22T14:09:57Z"
rotulos: ["Ordem de Carga", "Configuração", "Relatórios", "Parceiro", "Movimentação Financeira", "Financeiro"]
---

# Como gerar diferença do acerto de ordem de carga para o financeiro

| Categoria |
| --- |
| [Como funciona a geração de diferença do acerto de ordem de carga e quais seus benefícios?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro#h_01KF0ZWQTK5TDV91N2V1FF1ZP5) |
| [Quais são os riscos de não utilizar a geração de diferença no acerto da ordem de carga?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro#h_01KF0ZW549ZYJCYQPHF25E99RF) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro#h_01KFDSWH797NG4TM67CY2BZXQN) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro#h_01KF0ZVSFMDQP0ZJ2C961QDHPD) |
| [Agora vamos realizar na prática, dentro do ERP Sankhya!](https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro#h_01KF0ZV6ZRMF267VAX7GKR6Q7W) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37697078263319-Como-gerar-diferen%C3%A7a-do-acerto-de-ordem-de-carga-para-o-financeiro#h_01KF0ZTJE4TSMXQ3V678PG4K1R) |

## Geração de diferenças de acerto no financeiro

#### Como funciona a geração de diferença do acerto de ordem de carga e quais seus benefícios?

A geração de diferença no acerto da ordem de carga consiste em registrar, no sistema, as divergências entre o valor previsto no pedido e o valor efetivamente faturado ou recebido no retorno da entrega. Essa prática permite que o setor financeiro identifique automaticamente valores a ajustar, como devoluções, avarias ou faltas, sem depender de lançamentos manuais, assegurando maior precisão e rastreabilidade. Além de melhorar o controle logístico e financeiro, essa automação reduz erros, agiliza a conferência dos documentos de transporte e contribui para a tomada de decisão mais assertiva, com base em dados confiáveis.

#### Quais são os riscos de não utilizar a geração de diferença no acerto da ordem de carga?

Ao deixar de utilizar essa funcionalidade, a empresa corre o risco de realizar ajustes financeiros de forma manual e descentralizada, o que pode resultar em inconsistências nos registros contábeis, perda de informações importantes sobre devoluções ou avarias e maior exposição a erros humanos. Além disso, sem o controle automatizado, torna-se mais difícil identificar falhas recorrentes na operação logística, comprometendo a rastreabilidade e dificultando a conformidade com normas fiscais e auditorias. 

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1067046419)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa **Axis** precisa garantir que, ao realizar o acerto com um parceiro, qualquer diferença entre o valor esperado e o valor efetivamente retornado possa ser registrada no sistema. Para isso, é necessário que o sistema permita gerar um lançamento financeiro correspondente à diferença, garantindo que o acerto possa ser concluído posteriormente sem comprometer o controle financeiro.

**Tarefa:** Simule no sistema um acerto com valor diferente do esperado e verifique se o lançamento financeiro da diferença foi gerado corretamente para ajuste futuro. Em seguida, emita o relatório de resumo do acerto. 

#### Agora vamos realizar na prática, dentro do ERP Sankhya!

1. **Preferência**

- Acessea tela **Preferência**
  Menu: Configurações » Avançado » Preferências
- Localize o parâmetro **GERDIFACOC**
- No campo Ligado/Desligado: **Ligado**

**Observação:** Se o parâmetro estiver desligado, a funcionalidade **"Gerar Diferença do Acerto de OC p/ Financeiro"** não será habilitada na tela de acerto, e o caixa poderá ser fechado com diferenças.

2. **Geração da diferença no financeiro**

- Acesse a tela **Acerto de Ordem de Carga**
  Menu: Financeiro » Rotinas » Acertos » Acerto de Ordem de Carga
- Com o caixa devidamente aberto e as notas conferidas, na aba **Resumo do Acerto**,  localize o tipo de título usado para recebimento das notas e verifique a coluna “**Valor retornado”** (aqui é onde definiremos o valor que foi de fato entregue pelo parceiro que realizou a entrega).
- Para simular um cenário em que há a necessidade de geração da diferença no financeiro preencha esse campo com um valor menor do que o esperado.
- Clique em **Confirmar**.
- Clique em **Gerar diferença p/ financeiro.**
- Após isso, veja que o campo foi renomeado para **Visualizar financeiro da diferença**, clique sobre ele e confira o financeiro gerado na tela **Movimentação Financeira.**

3. **Gerar o relatório de resumo do acerto:**

- Após a realização das etapas anteriores, clique na opção **Rel. Resumo Acerto**.
- Insira a **Data do Acerto** e clique em **Visualizar** para gerar o relatório.
- Revise as informações do relatório para garantir que todos os registros estejam corretos.
- Clique em **Ref. fechamento caixa/acerto**

**Preencha as preferências de impressão:**

- **Crédito/Débito**
- **Vendas**
- **Produtos**
- Clique em **Visualizar Relatório.**

#### Correção e Repetição

- Certifique-se de que, ao inserir um valor menor no campo **Valor retornado**, o sistema gerou corretamente o financeiro da diferença.
- Confirme se o registro da diferença foi criado conforme esperado.
- Verifique se o **Relatório de Resumo do Acerto** apresenta todas as informações corretas, incluindo os valores ajustados e a geração da diferença no financeiro.
- Caso não consiga gerar a diferença no financeiro, confirme se o parâmetro **GERDIFACOC** está ativado e se as alterações foram aplicadas corretamente no sistema. Se necessário, feche e reabra a tela **Acerto de Ordem de Carga**.
