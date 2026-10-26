---
id: "360045115373"
titulo: "Cálculo de Juros e Multas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:44:31Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Juros", "Financeiro", "CONSJURMULNEG", "Cálculo de juros", "Cálculo de Juros e Multas", "Cálculo de multas", "Juro composto", "Juro simples", "br.com.sankhya.fin.rotina.calculojurosmulta", "Cálculo de Juros e Multas manual", "USAVLRLIQGERCOB", "VARCAMBJURMULT", "Cálculo de Juros/Multas", "Configurações de Filtros", "Gravar Resultados Cálculos", "Multa"]
---

# Cálculo de Juros e Multas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312456725783) Módulo: Financeiro > Rotinas
```

---

Através dessa tela, é possível realizar o cálculo de Juros e Multas de Receitas ou Despesas. Você poderá visualizar os cálculos realizados e gravá-los no Banco de Dados.

[Painel de Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#paineldefiltros)                                                      [Grade de Resultados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#gradederesultados)

[Botão Outras opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#bot%C3%A3ooutrasop%C3%A7%C3%B5es...)                                          [Como utilizar o Cálculo de Juros e Multa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#comoutilizaroc%C3%A1lculodejurosemulta)

[Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#par%C3%A2metrosqueinfluenciamestarotina)

![Imagem 2: Parâmetros que influenciam esta rotina](https://ajuda.sankhya.com.br/hc/article_attachments/360082180274)

**Observação:** para o funcionamento desta rotina, é necessário ter as permissões configuradas na tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos).

## Painel de Filtros

Ao lado esquerdo da tela, temos os campos para Filtros. Além da possibilidade de configurar um filtro personalizado, os títulos podem ser filtrados pelos seguintes campos:

**Número único:** Informe o número único do título que se deseja calcular os juros e/ou multas.

**Receita/Despesa:** Defina se serão apresentados títulos de receita ou despesa para realização do cálculo.

**Vencimento:** Preencha um período que enquadre a data de vencimento dos títulos a serem calculados.

**Parceiro:** Este filtro pode ser utilizado da seguinte forma:

- Através do botão **"Adicionar"**, você pode adicionar um ou mais parceiros para filtragem de uma única vez. Ao clicar no botão, o sistema exibirá uma tela de pesquisa, onde você seleciona os parceiros desejados;
- O botão **"Remover"**, remove o Parceiro selecionado;
- O botão **"Limpar"**, remove da lista todos os Parceiros que foram adicionados.

**Observação:** a **rotina [Gerência de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606894-Ger%C3%AAncia-de-Cobran%C3%A7a) não permite filtrar parceiros inativos, visto que não é possível realizar operações para cadastros inativados no sistema.**

#### Seção Juros/Multa

Logo abaixo do campo **"Parceiro"**, temos a seção **"Juros/Multa"**, onde informam-se os dados que serão utilizados para o cálculo.

![Imagem 3: Logo abaixo do campo "Parceiro" , temos a seção "Juros/Multa" , onde informam-se os dados que serão utilizados para o…](https://ajuda.sankhya.com.br/hc/article_attachments/360083306493)

**Carência (dias):** Neste campo, informe a quantidade de dias de carência que serão utilizados nos cálculos.

**Multa (%):** Preencha aqui, a porcentagem de multa que será aplicada no cálculo.

**Juros diários (%):** Informe neste campo, o percentual de juros que serão calculados dia a dia.

**Observação:** ao inserir um valor nesse campo que ultrapasse dez casas decimais, o sistema irá arrendondá-lo para que permaneça com dez casas, por exemplo, ao inserir o valor 0,0496410254789, será ajustado para 0,0496410255.

**Tipo de juros:** Defina aqui, se os juros serão calculados de forma **"Simples"**, ou se serão **"Compostos"**.

As informações apresentadas nos campos da seção Juros/Multa são alimentadas automaticamente por parâmetros globais. O botão **"Salvar"** tem a função de gravar as novas informações que forem inseridas nesses campos; ao pressioná-lo, será exibido o pop-up **"Cálculo de Juros e Multa"** com a seguinte mensagem:

**"Você está alterando os parâmetros GLOBAIS de Juros e Multa do Sistema. Estes novos valores serão utilizados em todas as rotinas. Confirma Alteração?"**

Optando por confirmar a alteração, todas as rotinas que utilizem os referidos parâmetros serão afetadas. Caso não confirme, os valores serão utilizados somente para o cálculo atual efetuado nesta rotina, sem alterar os parâmetros globais.

#### Seção Cálculo

![Imagem 4: Seção Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/360082185854)

Nesta seção, informe inicialmente o campo **"Data base"**, que representa a data base para cálculo. Serão calculados juros e multas a partir deste dia, subtraindo os dias de carência.

**Nota:** ao informar uma Data base futura, o sistema apenas projetará o valor previsto de juros considerando a data futura, pois os valores calculados com base em data futura não serão gravados nas tabelas do Financeiro.

A marcação **"Considerar títulos com juros/multas já calculados?"**, possibilita que sejam exibidos na grade, títulos com juros e multas que já foram gravados. Quando esta marcação não estiver selecionada, os títulos já gravados não serão apresentados na grade.

O botão **"Recalcular"** refaz o cálculo conforme os percentuais informados na seção **"Juros/Multa"**, porém, não será realizada nenhuma gravação no Banco de Dados, servindo apenas para visualização.

Para gravar o que foi calculado, clique no botão **"Gravar"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#top)

## Grade de Resultados

![Imagem 5: Grade de Resultados](https://ajuda.sankhya.com.br/hc/article_attachments/360082186054)

Acima da grade onde os títulos são apresentados, existem além do botão de configuração da grade padrão do sistema, os botões **"Remover selecionados"** e **"Remover NÃO selecionados"**, utilizados para remover e/ou manter títulos da grade.

Para selecionar mais de um item na grade, mantenha pressionada a tecla "Ctrl" e clique sobre os itens que se deseja selecionar; em seguida, pressione um dos dois botões, para remover os títulos selecionados ou os não selecionados.

As colunas **"Multa Calculada"**, **"Juros Calculados"** e **"Total Calculado"** da grade serão atualizadas no momento em que você clicar em **"Recalcular"**.

Abaixo da grade, encontram-se os totalizadores da tela. O totalizador **"Desdob."** traz o valor total dos desdobramentos dos títulos da grade. Em **"Juros/Multa"**, teremos os totais dos Juros e Multas. Logo à frente, é apresentado em cor vermelha, o total do valor dos desdobramentos, somados aos juros e multas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#top)

## Botão Outras Opções...

![Imagem 6: Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/article_attachments/360082186214)

Se a opção **"PDD (Provisão de Devedores Duvidosos)"** for selecionada, nos títulos, a coluna com este nome (PDD), serão marcados como **"Sim"**; se for desmarcada será indicado como **"Não"**. Se o título estiver contabilizado, a opção aparece desabilitada.

Acesse mais detalhes sobre Contabilização de títulos de devedores duvidosos em [Contabilização de Devedores Duvidosos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607634).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#top)

## Como utilizar o Cálculo de Juros e Multa

1. Primeiramente, configure o filtro para que sejam apresentados apenas os títulos que terão os juros e multa calculados.
2. Cadastre os valores desejados nos campos da área **"Juros/Multas"**.
3. Clique no botão **"Aplicar"** para que sejam apresentados os títulos desejados. Esses títulos serão apresentados na grade com os cálculos de juros e multa efetuados. Nesse momento, o sistema apresenta os cálculos para que estes sejam visualizados.
4. Se desejar refazer os cálculos, bastará cadastrar os novos valores em **"Juros/Multas"** e clicar em **"Recalcular"**.
5. Para que estas informações sejam gravadas no Financeiro, clique no botão **"Gravar"** ou, se quiser somente visualizar os valores, basta sair da tela sem gravar as informações.

**Nota:** serão calculados juros e multas a partir da data base, menos os dias de carência informados no campo **"Carência (dias)"** em **"Juros/Multas"**. 

Uma vez selecionado um título e acionado o botão **"Baixar"** na tela de [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874 "Movimentação Financeira"), a tela de baixa é carregada com os valores dos juros e multa calculados, conforme as configurações da tela de Cálculo de Juros e Multas.

Os valores da baixa só serão recalculados se houver mudança de registros selecionados para baixa na grade, ou quando pedir o cancelamento de uma baixa anteriormente efetuada.

Quando houver modificações nas Preferências de Cálculo de Juros e Multas, e a tela de baixa já tiver sido carregada, basta clicar em cancelar que, quando for novamente realizada a baixa do título, serão consideradas as novas taxas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#top)

## Parâmetros que influenciam esta rotina

**Considera Variação Cambial p/ Juros e Multas? - VARCAMBJURMULT:** quando estiver ativado, juntamente com o parâmetro **"Utiliza Sankhya Civil? - USASNKCIVIL"**, o Cálculo de Juros e Multas será feito tendo como base o valor cheio (Vlr. Desdobramento + Variação Cambial).

**Considerar juros e multas negociados no cálculo dos juros de mora? - CONSJURMULNEG**: quando ligado, será realizado o cálculo dos juros de mora sobre o valor dos juros e multas que foram gerados por uma renegociação. Imaginemos um título a ser pago que foi originado de uma renegociação; nesta renegociação, foram calculados juros e multa; com o parâmetro mencionado ativado, o cálculo dos juros pertinentes ao atraso do título irá utilizar como base além do valor do desdobramento do título, os juros e multa negociados que foram calculados na renegociação.

**Usar Vlr. líquido para calcular juros/multa? - USAVLRLIQGERCOB:** quando estiver ativado, será utilizado o Valor Líquido do título como base para realização do cálculo de juros e multas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115373-C%C3%A1lculo-de-Juros-e-Multas#top)
