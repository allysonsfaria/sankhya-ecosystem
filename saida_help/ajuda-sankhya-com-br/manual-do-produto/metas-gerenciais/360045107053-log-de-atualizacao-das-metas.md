---
id: "360045107053"
titulo: "Log de Atualizacao das Metas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107053-Log-de-Atualizacao-das-Metas"
trilha: "Manual do Produto > Inteligência e Análise > Gestão Estratégica > Metas gerenciais"
atualizado_em: "2026-09-23T17:45:31Z"
rotulos: ["AJUDA DO SKW", "manual", "log", "log de metas", "br.com.sankhya.mgegi.logatualizacaometas", "Log de Atualizacao das Metas manual", "Configuração", "Atualização", "Gestão Estratégica", "Exibe logs das atualizações das Metas Gerenciais", "Filtros para meta período e evento; colunas mostram detalhes da execução", "Define armazenamento de logs e atualizações de metas com erros", "Metas Gerenciais"]
---

# Log de Atualizacao das Metas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311296235671) Módulo: Gestão Estratégica > Configurações
```

---

Nesta tela, serão apresentados os Logs da atualização das Metas Gerenciais do GPD.

![Imagem 2: Nesta tela, serão apresentados os Logs da atualização das Metas Gerenciais do GPD .](https://ajuda.sankhya.com.br/hc/article_attachments/9452080337687)

No **"Painel de Filtros"**, pode-se utilizar os filtros rápidos da tela, além de permitir a criação de **"Filtros Personalizados"**.

No botão **"Aplicar"** o filtro selecionado será aplicado.

O campo **"Meta"** será utilizado para pesquisar uma meta por meio de seu número.

Em **"Período"**, pode-se filtrar a meta desejada pelo seu período.

No campo **"Evento Ult. Exec."**, você poderá também filtrar a meta desejável por meio de seu evento de execução, neste campo tem-se as opções:

- Todos;
- Erro;
- Atualização.

Na Grade Principal da tela, tem-se as colunas:

Na coluna **"Nro. Meta"**, será exibido o número da meta em execução.

Em **"Descrição (Meta)"** a tela apresentará a descrição da meta.

Tem-se ainda, a coluna **"Dh. Ult. Exec."** em que será exibido a data da última execução do cálculo de meta.

A grade mostrará em **"Evento Ult. Exec."** o evento da última execução, em que pode ser erro que ocorreu na última execução da meta, ou uma atualização, caso esta tenha sido executada com sucesso.

O **"Tempo Total"** corresponde à soma do tempo de todas as execuções da meta gerencial.

Abaixo da Grade de Detalhes, além dos campos descritos acima, tem-se ainda:

O **"Cód. Exercício"** que exibirá o código do exercício que foi calculado.

Em **"Dh. Inclusão"**, consta a data da inclusão do log na Tabela.

A coluna **"Evento"** mostrará o evento da execução em que, poderá constar como erro se houver algum tipo de erro durante a execução do cálculo, ou Atualização se a execução efetuada ocorrer com sucesso.

O **"Tempo Total"** será a soma total de todos os tempos para atualização, este será exibido no formato de time.

Na coluna **"Tempo Real"** será apresentado o tempo gasto na atualização do **"Realizado Acumulado"**.

O **"Tempo Prev."** exibirá o tempo gasto na atualização do **"Previsto Acumulado"**.

Ao selecionar uma das linhas na grade de detalhes e clicar no botão ![Imagem 3: Ao selecionar uma das linhas na grade de detalhes e clicar no botão "Ver Log" , será apresentado um pop-up em que será…](https://ajuda.sankhya.com.br/hc/article_attachments/15613255788311) **"Ver Log"**, será apresentado um pop-up em que será exibido o log com mais detalhes:

![Imagem 4: Ao selecionar uma das linhas na grade de detalhes e clicar no botão "Ver Log" , será apresentado um pop-up em que será…](https://ajuda.sankhya.com.br/hc/article_attachments/9452185773335)

Além do botão, você poderá abrir o referido pop-up dando um clique duplo na linha.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107053-Log-de-Atualizacao-das-Metas#top)

## Parâmetros que atuam nesta rotina

Nesta aba, são inseridas as principais informações que irão caracterizar a meta.

Referente ao parâmetro **"Gravar o log da atualização de metas em tabelas? - LOGMETASTABLE"**, caso este esteja desligado, as informações do log desta tela serão salvas na máquina do usuário. Se estiver ligado, estas informações serão salvas no banco de dados, e assim, exibidas nesta tela.

Ainda com o parâmetro acima habilitado, ao clicar no botão **"Recalcular selecionados"** localizado na tela [Metas Gerenciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608534-Metas-Gerenciais), o sistema exibirá uma mensagem em que é questionado se o usuário deseja recalcular as metas selecionadas.

Se no recálculo das metas houver erros, a seguinte mensagem será exibida:

**"Houve erro(s) durante a determinação dos valores da meta. Os arquivos de log dos erros se encontram no repositório de arquivos. Deseja ir para a tela de log?"**

Caso o usuário clique no botão **"Sim"**, o mesmo será redirecionado para a tela Log de Atualização das Metas; optando por não exibir a tela, o pop-up com a mensagem será fechada.

Com o parâmetro **"Atualiza dt.próx. execução de indicadores c/ erro? - APROXEXECINDERR"** pode-se definir a atualização com a data/hora da próxima execução da meta, desse modo, ao configurar o parâmetro a meta gerencial terá a data/hora da próxima modificação atualizada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107053-Log-de-Atualizacao-das-Metas#top)
