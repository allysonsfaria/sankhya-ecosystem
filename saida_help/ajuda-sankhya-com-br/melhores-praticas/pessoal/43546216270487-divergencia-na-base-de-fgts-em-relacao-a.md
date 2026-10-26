---
id: "43546216270487"
titulo: "Divergência na Base de FGTS em relação ao valor apresentado no Totalizador do FGTS no Resumo de Folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546216270487-Diverg%C3%AAncia-na-Base-de-FGTS-em-rela%C3%A7%C3%A3o-ao-valor-apresentado-no-Totalizador-do-FGTS-no-Resumo-de-Folha"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-06T13:29:54Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Divergência na Base de FGTS em relação ao valor apresentado no Totalizador do FGTS no Resumo de Folha

Ao emitir o **Resumo da Folha**, pode ocorrer diferença entre a **base de FGTS da folha** e a base apresentada no **totalizador do FGTS**. Também pode haver diferença entre o **valor de FGTS calculado pelo sistema** e o valor apresentado no totalizador.

Essa diferença pode ocorrer quando existem **rescisões calculadas na referência seguinte** à referência que está sendo analisada.

### Por que isso acontece?

De acordo com as regras de recolhimento do **FGTS Digital**, quando um desligamento que **gera direito ao saque do FGTS** ocorre entre os dias **1º e 9º do mês**, o FGTS referente à competência anterior deve ser recolhido junto com os valores da rescisão, seguindo o prazo de recolhimento rescisório (**D+10**), conforme o **art. 18 da Lei nº 8.036/1990**.

Por esse motivo, o valor do FGTS da folha mensal pode deixar de aparecer no totalizador da competência anterior e ser levado para a **referência do desligamento**.

### Como verificar se a diferença está relacionada a uma rescisão?

Sempre que encontrar uma diferença no **Resumo da Folha**, verifique também a **referência seguinte**.

Por exemplo, se o **Resumo da Folha de 08/2026** apresentar uma diferença na base ou no valor de FGTS, emita também o **Resumo da Folha de 09/2026** para verificar se existe algum desligamento que explique a diferença.

### Exemplo

Na folha mensal de **08/2026**, o funcionário possui:

- **Base de FGTS:** R$ 2.500,00.

Ao consultar os **Dados FGTS** da referência 08/2026, pode não ser apresentado o valor de FGTS desse funcionário.

Isso ocorre quando o funcionário foi **desligado entre os dias 1º e 9º de 09/2026** e o desligamento gera direito ao saque do FGTS.

Nesse caso, o FGTS referente à folha mensal de 08/2026 será recolhido juntamente com os valores da rescisão.

![Imagem 1: Nesse caso, o FGTS referente à folha mensal de 08/2026 será recolhido juntamente com os valores da rescisão.](https://ajuda.sankhya.com.br/hc/article_attachments/44012494779031)

Ao emitir o **Resumo da Folha de 09/2026**, referência em que ocorreu o desligamento, o valor da folha mensal de 08/2026 será apresentado juntamente com os valores da rescisão.

Nos **Dados GRRF**, a remuneração da competência anterior deverá ser apresentada no campo **“Remuneração mês Ant.”**.

Assim, a diferença identificada no Resumo da Folha de 08/2026 pode ser justificada pelo desligamento realizado na referência seguinte.

![Imagem 2: Assim, a diferença identificada no Resumo da Folha de 08/2026 pode ser justificada pelo desligamento realizado na…](https://ajuda.sankhya.com.br/hc/article_attachments/44012486382999)

### Atenção: desligamentos que não geram direito ao saque do FGTS

Esse comportamento deve ocorrer **somente nos desligamentos que geram direito ao saque do FGTS**.

Caso o sistema esteja levando a remuneração da competência anterior para a rescisão de um funcionário cujo desligamento **não gera direito ao saque do FGTS**, será necessário **recalcular a folha de rescisão**.

Ao realizar o cálculo, na aba **Info. Tipo Rescisão o FGTS** e **campo “Calcula Mês Anterior” deve estar desmarcado.**

Com essa opção desmarcada, o sistema não irá considerar a remuneração da competência anterior no cálculo rescisório para esse tipo de desligamento, evitando que o valor seja levado indevidamente para os **Dados GRRF** e garantindo que o **Resumo da Folha seja apresentado corretamente**.

![Imagem 3: Com essa opção desmarcada, o sistema não irá considerar a remuneração da competência anterior no cálculo rescisório…](https://ajuda.sankhya.com.br/hc/article_attachments/44012494781719)

###
