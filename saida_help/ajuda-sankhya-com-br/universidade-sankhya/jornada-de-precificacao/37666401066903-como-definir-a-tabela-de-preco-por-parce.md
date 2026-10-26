---
id: "37666401066903"
titulo: "Como definir a tabela de preço por Parceiro e Empresa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa"
trilha: "Universidade Sankhya > Jornada de Precificação"
atualizado_em: "2026-07-22T14:11:28Z"
rotulos: ["Configuração", "Parceiro", "ERP Sankhya", "Comercial", "Tabelas de Preço"]
---

# Como definir a tabela de preço por Parceiro e Empresa

| Categoria |
| --- |
| [Qual é o objetivo de combinar tabela de preço por parceiro e empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa#h_01KEYAWM5QRSD5QM7DAP5T75K9) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa#h_01KEYAWM5TJF03GASC907NAV02) |
| [Quais os riscos de não utilizar uma tabela de preço que combine parceiro e empresa?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa#h_01KEYAWM64VC1JHBKQPNEY8J6D) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa#h_01KFBRT3D6Y44AWKNB2GHPTW0R) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa#h_01KEYB3S7J7NPX64B4GM21QS96) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37666401066903-Como-definir-a-tabela-de-pre%C3%A7o-por-Parceiro-e-Empresa#h_01KEYAXC8HGRP9D9TAP8FK73DW) |

## Definição de tabela de preço por parceiro e empresa

#### Qual é o objetivo de combinar tabela de preço por parceiro e empresa?

O objetivo de combinar tabelas de preços por parceiro e empresa é garantir uma precificação mais inteligente e contextualizada, alinhada tanto às condições comerciais de cada unidade da organização quanto às necessidades específicas do cliente. Essa prática permite adaptar os preços com base em variáveis como políticas internas, estrutura de custos, localização e estratégias comerciais específicas da filial. Dessa forma, um mesmo cliente pode receber ofertas diferentes ao negociar com unidades distintas, refletindo com mais precisão as realidades operacionais de cada ponto de venda, fortalecendo a gestão comercial e promovendo negociações mais consistentes e equilibradas.

#### Quais problemas este recurso resolve?

- Falta de alinhamento entre políticas comerciais de diferentes empresas ou filiais.
- Dificuldade em atender clientes que negociam com múltiplas unidades da empresa.
- Inconsistências nos preços aplicados em diferentes localidades.
- Gestão ineficiente de múltiplas entidades comerciais.
- Problemas na análise de rentabilidade por unidade.

#### Quais os riscos de não utilizar uma tabela de preço que combine parceiro e empresa?

Não utilizar uma tabela que considere tanto o parceiro quanto a empresa pode gerar desorganização na precificação, levando à aplicação de valores genéricos e desalinhados com os custos e contextos regionais. Isso pode resultar em margens de lucro distorcidas, redução da competitividade e dificuldade de responder de forma adequada às demandas comerciais de cada cliente. A falta dessa personalização também compromete o controle por unidade, dificulta a análise de rentabilidade por operação e aumenta o risco de inconsistências nos registros, impactando diretamente a eficiência da gestão e a experiência do cliente.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052311726)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa Axis LTDA possui três unidades operacionais distintas: uma matriz localizada em São Paulo e duas filiais, uma em Minas Gerais e o outro no Rio de Janeiro. O grupo atende um grande distribuidor nacional, o Distribuidor Ideal, que realiza pedidos regularmente para ambas as unidades. A matriz em São Paulo lida com altos custos logísticos e impostos estaduais, enquanto a filial em Minas Gerais usufrui de incentivos fiscais regionais e custos operacionais menores. No entanto, o Distribuidor Ideal está aceitando o mesmo preço de ambas as unidades, independentemente das diferenças regionais, o que examinou em margens inconsistentes e dificuldades nas negociações. Para resolver esta situação, a empresa decidiu implementar tabelas de preços que combinam parceiro e empresa, ajustando os preços às condições específicas de cada unidade.

**Tarefa:** Configure tabelas personalizadas para os parceiros cadastrados em sua base de testes, seguindo as orientações indicadas.  

**É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya**

1. Acesse a tela **Tabelas de Preços** 
   Menu: Comercial » Arquivo » Tabelas de Preços

- Clique no botão “**+**” (**Cadastrar Cadastro de Tabela de Preço**).
- Informe um número de identificação no campo **Código**.
- Defina um nome para identificação no campo indicado (EX.: CLIENTE A/EMPRESA1).
- Clique em **Salvar**.

**Aba Histórico de atualizações**

- Informe o código **0** no campo **Tabela de origem**
- Preencha os campos **Dt. Vigor** e **Dt. Atualização** com a data atual.
- Informe **-5,00** no campo **Percentual**. 
  Esse campo definirá a aplicação de acréscimo ou desconto sobre o preço da tabela de origem.
- Clique em **Salvar**.

Na sub aba **Exceções** pode-se criar exceções para produtos específicos, adicionando mais descontos ou acréscimos, ou também informando preços fixos diferenciados

2. Acesse a tela **Preferências** 
   Menu: Configurações » Avançado » Preferências

- Pesquise a chave **TIPTABPRECO** e tecle ENTER.
- Selecione **Parceiro/empresa** no campo **Valor**.
- Clique em **Salvar**.
  Após alterar o parâmetro acima, feche a tela de **Tabela de Preço** para que a alteração seja refletida.

3. Acesse a tela **Parceiros**
   Menu: Configurações » Cadastros » Parceiros

- Clique em **Modo Grade**.
- Clique no botão “**Atualizar**”.
- Selecione o parceiro associado à tabela criada com um duplo clique.

**Aba Grupo ICMS/ISS** **por Empresa**

- Clique no botão “**+**” (**Cadastrar Grupo ICMS/ISS por Empresa**).
- Informe o código da sua empresa no campo **Empresa**.
- Informe o código da tabela criada nesta aula no campo **Tabela de preço**, localizado na aba “Geral”.
- Clique em Salvar.

4. Acesse a tela **Tabelas de Preços**
   Menu: Comercial » Arquivo » Tabelas de Preços

- Localize a tabela de preço que foi criada.
  Ao lado da aba de **Histórico de atualizações** foi criada a aba **Parceiro/Empresa,** as informações do vínculo feito entre a empresa e a tabela de preço no cadastro do parceiro, poderão ser visualizadas nesta aba.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo novamente.
