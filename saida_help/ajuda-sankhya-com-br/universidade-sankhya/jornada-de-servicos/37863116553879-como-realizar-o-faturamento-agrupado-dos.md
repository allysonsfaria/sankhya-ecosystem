---
id: "37863116553879"
titulo: "Como realizar o faturamento agrupado dos contratos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-22T14:06:44Z"
rotulos: ["Parceiro", "Faturamento", "Contrato", "Financeiro", "NFS-e"]
---

# Como realizar o faturamento agrupado dos contratos

| Categoria |
| --- |
| [O que acontece quando um contrato é faturado?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos#h_01KFKBMSV4BFBKWE7D5PRKAN69) |
| [Quais problemas esse acompanhamento resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos#h_01KFKBN644EP5N547GA8SGYMH5) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos#h_01KFKBNC25G3TH6PRAMJ4DKN7G) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos#h_01KFKBNVQ14JFZWK22YV4TKJAT) |
| [Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos#h_01KFKBPK6ZV8YMTEBWXPBWYG86) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37863116553879-Como-realizar-o-faturamento-agrupado-dos-contratos#h_01KFKBQ6S0JPVH20QWPXNGF3NY) |

## Faturamento agrupado de contratos

#### O que acontece quando um contrato é faturado?

O faturamento agrupado permite emitir uma única nota fiscal para diferentes contratos com o mesmo cliente, desde que compartilhem as mesmas condições fiscais e comerciais (tipo de operação, natureza, vencimento, etc.).

Essa prática é comum em empresas que prestam vários serviços a um mesmo cliente e desejam consolidar os valores em uma única cobrança, reduzindo o volume de documentos e facilitando o controle financeiro.

#### Quais problemas esse acompanhamento resolve?

- Emissão de várias notas para o mesmo cliente no mesmo período, o que gera mais trabalho e pode confundir o cliente.
- Risco de cobrança duplicada ou com vencimentos diferentes para o mesmo parceiro.
- Falta de controle sobre a consolidação financeira dos contratos com um mesmo cliente.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103869055)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: A Axis LTDA agora presta serviços de manutenção mensal para 2 unidades do cliente Super Mais. Cada unidade tem seu próprio contrato, com o mesmo valor, mesmas regras de cobrança e mesma data de vencimento. Sendo assim, além do contrato que já existia com a unidade principal, foi preciso registrar o novo contrato da unidade 2. No processo de faturamento, foi percebido que esses contratos podem ser faturados juntos para gerar uma única nota.

**Tarefas**: Sua tarefa é registrar um novo contrato para o parceiro **Super Mais** utilizando os dados abaixo e realizar o faturamento deste e do contrato lançado anteriormente de forma agrupada.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Informações necessárias para registro do segundo contrato:**

- Acesse a tela **Contratos**
  Menu: Contratos e Serviços » Arquivos
- Nos **Filtros Personalizados**, utilize o campo **Parceiro** para buscar o cliente Super Mais.
- Selecione o primeiro contrato e clique em **Duplicar**.

Na aba **Geral**:

- Apague a informação do campo **Referência último faturamento** (essa informação veio do contrato anterior que já foi faturado)
- **Data do contrato** - Primeiro dia útil do mês atual

  Na aba **Propriedades**:
- **Data base reajuste** - Mesma data do contrato
- Apague a informação do campo **Referência próximo faturamento** (essa informação veio do contrato anterior que já foi faturado)
- Salve as informações
- Utilize o botão outras opções **(...)** » **Copiar Produtos/Serviços** para copiar o produto do primeiro contrato para este.

Na aba **Produtos/Serviços**, sub-aba **Ocorrências:**

- Registre uma ocorrência de ativação do produto na data do contrato.

2. **Faturamento agrupado:**

- Acesse a tela **Faturamento de Contratos**
  Menu: Contratos e Serviços » Rotinas
- Nos **Filtros Personalizados**, utilize o campo **Parceiro** para buscar o cliente Super Mais.
- Marque a flag **Considerar Contatos/Perfil/Serviço**
- Nos **Parâmetros Obrigatórios**, preencha as seguintes informações:

**Tipo de Operação** - VENDA NFS-E

**Tipo de Título -** 1

**Tipo de Negociação -** 16

**Observação Padrão -** 0

**Data para Faturamento -** Primeiro dia do próximo mês em relação ao mês do **SEGUNDO** contrato (estamos considerando aqui que a empresa realiza os faturamentos sempre no início do mês)

**Mês para Referência -** O mês para referência se trata do mês que ocorrerá o pagamento, sendo assim, mesma data usada no campo anterior

**Série -** NF

**Agrupar Contratos** - Marcado

- Clique em **Aplicar**

1. **Conferência das informações e faturamento dos contratos:**

- Veja se os dois contratos foram apresentados no painel**.**
- Para faturar, clique no botão **Faturar**.
- Será exibido um pop-up informando se o faturamento ocorreu devidamente, caso tenha ocorrido algum impedimento, veja as observações para realizar a correção, caso não,  clique em **Mostrar no Portal**, para visualizar a nota no  **Portal de Vendas**, clicando duas vezes sobre ela, você será direcionado para a **Central de Vendas** e poderá visualizar os dados da NFS-e. O sistema emitirá uma única nota no valor total dos contratos R$36.000,00, automaticamente gera-se também um único financeiro neste valor.

#### Correção e Repetição

- Lembre-se de realizar a ativação do produto no contrato antes de tentar realizar o faturamento.
- Não esqueça de marcar a flag **Agrupar Contratos** para gerar apenas uma nota para os dois contratos.
