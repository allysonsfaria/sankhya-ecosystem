---
id: "37665511142807"
titulo: "Como definir tabela de preço por região do vendedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor"
trilha: "Universidade Sankhya > Jornada de Precificação"
atualizado_em: "2026-07-22T14:11:34Z"
rotulos: ["Configuração", "Vendedores", "Região", "Comercial", "Tabelas de Preço"]
---

# Como definir tabela de preço por região do vendedor

| Categoria |
| --- |
| [Qual é o objetivo de se definir uma tabela de preço considerando a região do vendedor?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KEY8F7P78D4Q632E1EKGD2JB) |
| [Quais problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KEY8F7PAA1W1MTYKEXEJB1NQ) |
| [Quais os riscos de não utilizar essa prática?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KEY8F7PK3W154WKCQTS1MKAB) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KFBQR3QCTHNP7WYN1XWM1ND9) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KEY8J8M9R4B2QXWHHKQ5XZ4G) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KEY8HDBTJA69QZAZ7SYP67CK) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37665511142807-Como-definir-tabela-de-pre%C3%A7o-por-regi%C3%A3o-do-vendedor#h_01KEY8FRCM634PRKC4KTW1DEYT) |

## Definição de tabela de preço por região do vendedor

#### Qual é o objetivo de se definir uma tabela de preço considerando a região do vendedor?

Essa tabela é usada quando a empresa atua em diferentes regiões e precisa ajustar os preços conforme as condições de cada local, como concorrência, custo logístico ou perfil dos clientes. O sistema identifica automaticamente de qual região é o vendedor e aplica a tabela certa, sem que ele precise escolher manualmente. Isso torna a venda mais rápida, os preços mais competitivos e evita erros. É ideal para empresas que vendem em várias regiões com características diferentes.

#### Quais problemas este recurso resolve?

- Preços iguais em regiões com realidades diferentes.
- Dificuldade em competir com empresas locais.
- Margem de lucro desequilibrada por região.
- Erros ou lentidão na hora de aplicar a tabela certa na venda.

#### Quais os riscos de não utilizar essa prática?

Sem esse controle, a empresa pode praticar preços inadequados para determinadas regiões, perdendo vendas por não acompanhar o mercado local ou tendo margens muito baixas por causa dos custos logísticos. Também aumenta o risco de erro na escolha da tabela e dificulta o planejamento por área de atuação, o que enfraquece a presença da empresa em mercados regionais.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052296455)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** A empresa Axis LTDA atende clientes em diversas regiões do país, incluindo grandes centros urbanos e áreas rurais. Durante uma análise de desempenho, a equipe de gestão descobriu que a precificação uniforme para todas as regiões não estava refletindo as realidades locais. Em áreas remotas, os custos logísticos aumentaram significativamente as margens de lucro, enquanto nas regiões urbanas a concorrência mais acirrada aumentou os preços mais competitivos. Além disso, os vendedores enfrentam dificuldades para negociar devido à falta de flexibilidade nos preços aplicados em suas regiões. Para resolver esses problemas, a empresa decidiu criar tabelas de preços personalizadas por região, facilitando as operações comerciais e melhorando a competitividade.

**Tarefa:** Crie uma tabela para as regiões específicas do vendedor, com base nos dados da sua base de testes, seguindo as orientações indicadas.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. Acesse a tela **Tabelas de Preços** 
   Menu: Comercial » Arquivo » Tabelas de Preços

- Clique no botão “**+**” (**Cadastrar Cadastro de Tabela de Preço**).
- Informe um número de identificação no campo **Código**.
- Defina um nome para identificação no campo indicado.
- Clique em **Salvar**.

**Aba Histórico de atualizações**

- Informe o código **0** no campo **Tabela de origem**
- Preencha o campo **Dt. Vigor** com a data atual
- Informe **-10,00** no campo **Percentual**. 
  Esse campo definirá a aplicação de acréscimo ou desconto sobre o preço da tabela de origem.
- Clique em **Salvar**.

2. Acesse a tela **Preferências** 
   Menu: Configurações » Avançado » Preferências

- Pesquise a chave **TIPTABPRECO** e tecle ENTER.
- Selecione **Região do vendedor** no campo **Valor**.
- Clique em **Salvar**.
  Após alterar o parâmetro acima, feche a tela de **Tabela de Preço** para que a alteração seja refletida e, em seguida, abra-a novamente.

3. Acesse a tela **Tabelas de Preços** 
   Menu: Comercial » Arquivo » Tabelas de preços

- Ative o **Modo grade**.
- Localize a tabela de preço criada nesta aula.
  Ao lado da aba de **Histórico de atualizações** foi criada uma nova aba.

**Aba Regiões**

- Informe a região que deseja aplicar essas regras (EX.: “**Triângulo Mineiro**”)
- Clique em **Salvar**.

4. Acesse a tela **Vendedores/Compradores** 
   Menu: Configurações » Cadastros » Vendedores/Compradores

- Clique em **Mostrar grade**.
- Clique no botão “**Atualizar**”.
- Selecione o registro do vendedor com um duplo clique.

**Aba Geral**

- Vincule a região informada na tabela de preços no campo **Região**.
- Clique em **Salvar**.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro refaça a atividade seguindo o passo a passo novamente.
