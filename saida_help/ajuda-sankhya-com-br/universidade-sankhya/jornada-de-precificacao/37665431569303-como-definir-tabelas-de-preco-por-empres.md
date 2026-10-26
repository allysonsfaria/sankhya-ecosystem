---
id: "37665431569303"
titulo: "Como definir tabelas de preço por empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa"
trilha: "Universidade Sankhya > Jornada de Precificação"
atualizado_em: "2026-07-22T14:11:35Z"
rotulos: ["Configuração", "Empresa", "Estoque", "Preferências", "Tabelas de Preço"]
---

# Como definir tabelas de preço por empresa

| Categoria |
| --- |
| [Qual é o objetivo de se utilizar tabelas de preço por empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa#h_01KEY853S4EWEEA5CNHV43TQTY) |
| [Quais os riscos de não utilizar tabela por empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa#h_01KEY853S7HGXW17RCKMBBTQ73) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa#h_01KFBQNCS8ZMFBDBMM81P9Z5VB) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa#h_01KEY8B18E13Y3CNAVKT78WPZ2) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa#h_01KEY85JE0FPRYHGMD56EPYKFT) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665431569303-Como-definir-tabelas-de-pre%C3%A7o-por-empresa#h_01KEY85JG2T6VDYJ0YKQS472EB) |

## Utilização de tabela de preço por empresa

#### Qual é o objetivo de se utilizar tabelas de preço por empresa?

A tabela de preços por empresa é usada quando o sistema é compartilhado por mais de uma empresa do mesmo grupo e cada uma precisa aplicar preços diferentes, seja por causa de custos, impostos ou políticas comerciais específicas. Com isso, é possível manter o controle separado por empresa, ajustando os preços de forma personalizada para cada realidade. Esse recurso garante que as condições comerciais fiquem alinhadas com a operação de cada unidade, evita erros fiscais e ajuda a manter a rentabilidade de cada negócio.

#### Quais os riscos de não utilizar tabela por empresa?

Se todas as empresas do grupo usarem a mesma tabela, mesmo com regras diferentes entre elas, isso pode gerar prejuízos por causa de preços mal ajustados, além de falhas no cumprimento de exigências fiscais. Também pode haver desequilíbrio de margem entre as unidades, dificuldade de análise por empresa e decisões comerciais erradas por falta de informação separada.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052318778)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A Axis LTDA possui três unidades de negócio localizadas em diferentes estados, cada uma sujeita a regimes tributários específicos. A unidade de São Paulo, por exemplo, está sujeita a ICMS interestadual, enquanto a unidade de Minas Gerais trabalha com incentivos fiscais locais, e a do Rio de Janeiro enfrenta alíquotas mais altas para determinados produtos. Essas diferenças impactam diretamente os custos operacionais e as margens de lucro. Para garantir preços de venda ajustados e competitivos, o responsável pela gestão decidiu configurar tabelas de preço específicas para cada unidade no sistema ERP.

**Tarefa**: Implemente tabela de preço específicas para uma empresa cadastrada em sua base de testes, seguindo as orientações indicadas. 

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Preferências**
   Menu: Configurações » Avançado » Preferências

- Pesquise a chave **CUSTOPOREMP** e tecle ENTER.
- Selecione **Ligado** no campo **Ligado/Desligado**.
- Clique em **Salvar**.
- Pesquise a chave **TIPTABPRECO** e tecle ENTER.
- Selecione **Única** no campo **Valor**.
- Clique em **Salvar**.
- Pesquise a chave **USARCODTABEMP** e tecle ENTER.
- Selecione **Ligado** no campo **Ligado/Desligado**.
- Clique em **Salvar**.

2. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de Preços

- Clique no botão “**+**” (**Cadastrar Cadastro de Tabela de Preço**).
- Informe um número de identificação no campo **Código**.
- Defina um nome para identificação no campo indicado.
- Clique em Salvar.

**Aba Histórico de atualizações**

- Informe o mesmo código definido acima no campo **Tabela de origem**
- Preencha os campos **Dt. Vigor** e **Dt. Alteração** com a data atual
- Clique em Salvar.

**Aba Regras -** Sub aba de Histórico de Atualizações

Como se trata de uma tabela nova, com origem nela mesma, ainda não há histórico de preços para os produtos. Por isso, é necessário informar os valores que serão aplicados a cada item nesta tabela.

- Clique no botão “**+**” (**Cadastrar Exceção de Preço**).
- Informe o produto no campo indicado**.**
- Defina **Valor** no campo **Tipo**.
- Informe o preço do produto.
- Clique em **Salvar**.

3. Acesse a tela **Empresa**
   Menu: Comercial » Preferências » Empresa

- Informe a tabela criada no campo **Tabela de preço para venda**, localizado na aba **Estoque/Preço**.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo novamente.
