---
id: "37880071911831"
titulo: "Como registrar nota de compra pelo contrato de despesa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa"
trilha: "Universidade Sankhya > Jornada de Serviços"
atualizado_em: "2026-07-24T12:43:40Z"
rotulos: ["Faturamento", "Contrato", "Nota Fiscal", "Financeiro", "ERP Sankhya", "Compras"]
---

# Como registrar nota de compra pelo contrato de despesa

| Categoria |
| --- |
| [Como funciona essa operação?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9HYP3J53TWS0PM599Y20W) |
| [Quais problemas essa prática resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9J86YTRYTRF3MFCE07Z8S) |
| [Quais os riscos de não utilizar?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9JDDM2NS5HHT3XSRTBT0K) |
| [Vídeo de demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9JJ5RQ7DF7C8T5WSXCSB0) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9JV4KW7C3XRA9YCSZSVS8) |
| [Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9K3TFV99GWE9878J1T5K1) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37880071911831-Como-registrar-nota-de-compra-pelo-contrato-de-despesa#h_01KFN9KEHJJXTKVB2QK43C6VXH) |

## Registro da nota de compra pelo contrato de despesa

#### Como funciona essa operação?

Registrar uma nota de compra pelo contrato de despesa é o processo que permite vincular a entrada da nota fiscal diretamente a um contrato previamente cadastrado no sistema. Essa funcionalidade é usada quando a empresa contrata serviços recorrentes (como limpeza, manutenção), e precisa registrar a nota recebida do fornecedor vinculando ao contrato correspondente.

Na prática, funciona como um “faturamento invertido”: em vez de gerar uma nota a partir do contrato (como nos contratos de receita), a empresa recebe a nota e vincula ao contrato de despesa, mantendo o controle financeiro, os valores provisionados e a regularidade do serviço contratado.

#### Quais problemas essa prática resolve?

- Falta de controle sobre os serviços contratados e as notas recebidas.
- Lançamentos de despesas fora do escopo contratual.
- Dificuldade em confrontar valores acordados com o que foi cobrado.
- Relatórios financeiros inconsistentes por registros desvinculados dos contratos.

#### Quais os riscos de não utilizar?

Sem a vinculação, a empresa pode perder o controle dos serviços recorrentes, dificultar a conciliação com as provisões e correr o risco de pagamentos indevidos, duplicados ou fora do combinado. Isso também impacta o acompanhamento de reajustes, renovações e encerramentos, comprometendo a gestão financeira.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1103869195)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto**: Após registrar o contrato com a empresa Polar Tech para calibração e certificação dos equipamentos, a Axis LTDA recebeu a primeira nota fiscal de serviço, referente ao mês vigente. Essa nota precisa ser registrada corretamente no sistema, vinculada ao contrato de despesa já cadastrado, garantindo que a provisão seja baixada e o controle financeiro mantido.

**Tarefas**: Lance a nota de compra no sistema informando o fornecedor Polar Tech, utilizando o contrato já registrado como base. Certifique-se de que o lançamento esteja vinculado corretamente ao contrato, e que o sistema reconheça e baixe a provisão gerada anteriormente. Isso garante rastreabilidade, evita pagamentos duplicados e mantém os relatórios financeiros consistentes.

#### Agora é a sua vez! Siga o passo a passo e aproveite o máximo do ERP Sankhya

1. **Registro da nota de compra de serviço:**

- Acesse a tela **Faturamento de Contratos**
  Menu: Contratos e Serviços » Rotinas
- Nos **Filtros Personalizados**, utilize o campo **Parceiro** para buscar o fornecedor Polar Tech.
- Marque a flag **Considerar Contatos/Perfil/Serviço**
- Nos **Parâmetros Obrigatórios**, preencha as seguintes informações:

**Tipo de Operação** - Compra Serviço

**Tipo de Título -** 1

**Tipo de Negociação -** 16

**Observação Padrão -** 0

**Data para Faturamento -** Primeiro dia do próximo mês em relação ao contrato (estamos considerando aqui que a empresa realiza os faturamentos sempre no início do mês)

**Mês para Referência -** O mês para referência se trata do mês que ocorrerá o pagamento, sendo assim, mesma data usada no campo anterior

**Série -** NF

- Clique em **Aplicar**
- Para registrar a nota, clique no botão **Faturar**.
- Será exibido um pop-up informando se o faturamento ocorreu devidamente, caso tenha ocorrido algum impedimento, veja as observações para realizar a correção, caso não,  clique em **Mostrar no Portal**, para visualizar a nota no **Portal de Compras**, clicando duas vezes sobre ela, você será direcionado para a **Central de Compras.**
- Preencha o campo **Nro. Nota** conforme nota recebida.
- Clique em **Confirmar**

#### Correção e Repetição

- Lembre-se de após realizar o “faturamento” preencher o número da nota na **Central** e confirmar o registro, pois só após isso é que o financeiro será atualizado.
- Após realizar o registro da nota, confira se o financeiro foi atualizado devidamente.
