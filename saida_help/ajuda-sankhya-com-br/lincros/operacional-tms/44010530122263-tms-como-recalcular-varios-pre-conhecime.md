---
id: "44010530122263"
titulo: "[TMS] - Como recalcular vários pré-conhecimentos de uma única vez"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010530122263--TMS-Como-recalcular-v%C3%A1rios-pr%C3%A9-conhecimentos-de-uma-%C3%BAnica-vez"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:39:25Z"
rotulos: ["sync_hc", "lincros", "lincros_13433318", "sync_hash_e6e99cdf342f"]
---

# [TMS] - Como recalcular vários pré-conhecimentos de uma única vez

**Menu**: Operacional > Cargas > Pré-conhecimentos

**Objetivo:** Recalcular pré-conhecimentos em lote, tendo em vista realizar a auditoria do valor calculado, após alterar ou ajustar a tabela de frete vinculada ao pré-conhecimento.

**Considerações**:

- Possuir pré-conhecimentos que tenham a necessidade de recalculo após ajuste na tabela de frete, por exemplo.

## Como recalcular os pré conhecimentos:

1. Acessar o menu: Operacional > Cargas > Pré-conhecimentos;
2. Clicar em 'Filtros', o sistema irá mostrar as opções de filtros que poderão ser utilizadas para buscar os conhecimentos em questão;
3. Selecionar os conhecimentos que serão recalculados através do 'checkbox', conforme exemplo abaixo:

   ![Imagem 1: Selecionar os conhecimentos que serão recalculados através do 'checkbox', conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44010530309655)
4. Clicar na seta indicando para baixo ao lado do ícone 'Recalcular'. Ao clicar na seta, o sistema irá retornar as opções para o recalculo, conforme imagem abaixo:

   ![Imagem 2: Clicar na seta indicando para baixo ao lado do ícone 'Recalcular'. Ao clicar na seta, o sistema irá retornar as opções…](https://ajuda.sankhya.com.br/hc/article_attachments/44010467751319)

4. O botão de recalcular possuí as seguintes opções:

**Selecionados**: o sistema irá apenas recalcular os pré-conhecimentos selecionados.
**Obs:** Este processo não desvincula a tabela de frete do pré-conhecimento antes de recalcular;

**Selecionados (ignorar tabela)**: está opção fará com que o sistema desvincule a tabela de frete que já está vinculada aos pré-conhecimentos selecionados, e após isso, irá recalcular apenas os registros selecionados, buscando novamente a tabela que atenda o mesmo para realizar o vinculo;

**Todos**: o sistema irá recalcular TODOS os pré-conhecimentos que estiverem na tela, independente se os pré-conhecimentos estiverem selecionados ou não;

**Todos (ignorar tabela)**: está opção fará com que TODOS os conhecimentos que estiverem na tela (independente se o pré-conhecimento estiver selecionado ou não) tenham suas tabelas de frete desvinculadas e os pré-conhecimentos sejam recalculados;

5. Utilizando o botão de recalcular, temos a opção de recalcular vários pré-conhecimentos de uma única vez. Após utilizar o filtro para buscar os registros necessários, podemos usar as opções que tenham na descrição (ignorar tabela), deste modo é possível desvincular a tabela de frete já vinculada aos pré-conhecimentos e posteriormente recalcular, desta forma, podemos ajustar os valores calculados dos conhecimentos selecionados.

**Obs:** Antes de utilizar o recurso, validar se a alteração será feita para TODOS os conhecimentos que estiverem na tela, ou se serão apenas os conhecimentos selecionados, pois há uma forma de recalcular apenas os que estão selecionados, e outra para recalcular TODOS que estiverem na tela.

**Divergência envolvendo IBS/CBS:** se após o recálculo o valor total ainda ficar divergente e a diferença envolver os tributos da Reforma Tributária (IBS/CBS), o recálculo do pré-conhecimento sozinho não resolve — é necessário também conferir o cadastro das alíquotas na aba IBS/CBS de Cadastros Gerais > Configurações da Empresa > Taxas > Taxas Estaduais (ou Municipais) para o estado/município da rota, e se o componente da tabela de frete está com "Calcular IBS/CBS" marcado. Só depois desse cadastro o recálculo reflete o valor correto.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
