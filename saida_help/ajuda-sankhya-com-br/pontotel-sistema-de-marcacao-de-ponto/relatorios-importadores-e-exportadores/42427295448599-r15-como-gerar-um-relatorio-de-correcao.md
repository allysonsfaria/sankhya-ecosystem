---
id: "42427295448599"
titulo: "R15 - Como gerar um relatório de correção de pontos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427295448599-R15-Como-gerar-um-relat%C3%B3rio-de-corre%C3%A7%C3%A3o-de-pontos"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:53:18Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_d71af67cfa0f", "pontotel_6a3329f743befeb85350d5fc"]
---

# R15 - Como gerar um relatório de correção de pontos

O **R15 - Relatório de correção de pontos** é uma ferramenta de auditoria essencial para a sua **gestão**. Ele permite que você visualize um histórico detalhado de todas as alterações manuais (inclusões, edições ou exclusões) realizadas nos pontos dos colaboradores.
Este relatório é fundamental para entender:

- **Quem** fez a alteração (o usuário).
- **Quando** a alteração foi feita.
- **O que** foi alterado (o dado antigo e o novo).

---

## Como gerar o Relatório R15

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de Relatórios (à direita), selecione a opção **R15 - Relatório de correção de pontos**
3. Defina os filtros para a sua consulta:

   - **Filtro principal:** Você pode filtrar por **locais de trabalho**, **empregadores** ou **grupos**.
   - **Período:** Selecione o intervalo de datas (início e fim) em que as correções foram realizadas.
4. Se desejar, utilize as opções extras para refinar a busca:

   - **Filtrar pelo dia do Ponto Modificado**: Foca a busca em correções realizadas em um período específico, independentemente do dia em que o ponto foi batido.
   - **Mostrar o Local do ponto alterado**: Inclui o nome do local de trabalho (setor/equipe) ao qual o ponto pertencia antes de ser corrigido.
   - **Mostrar o Empregador do ponto alterado**: Adiciona a informação do empregador (CNPJ) ao qual o ponto estava vinculado.
   - **Mostrar o local do empregado ao invés do local de trabalho do ponto**: Prioriza exibir o local de trabalho **atual** cadastrado para o colaborador, em vez do local onde o ponto foi registrado.
5. Clique em **Gerar excel**.

![Imagem 1: Clique em Gerar excel .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_12dn11h.png)

---

## Como baixar o Relatório gerado

Após clicar em "Gerar", a plataforma processará o relatório em segundo plano.

1. No menu de navegação, clique no **ícone de sino** (Notificações), para acompanhar o arquivo ser gerado.
2. Quando chegar a "100%", o relatório será baixado automaticamente.
3. Caso o download não tenha sido feito automaticamente, clique no **ícone de nuvem** (download) ao lado do nome do relatório para baixar o arquivo em formato Excel (XLSX) para o seu computador.

---

## Como fazer a leitura do relatório

O R15 é baixado como uma planilha (Excel/XLSX), e cada linha representa um evento de correção de ponto. A leitura correta permite que você audite a **evolução** do ponto e monitore as ações de **gestão** realizadas na folha.

![Imagem 2: O R15 é baixado como uma planilha (Excel/XLSX), e cada linha representa um evento de correção de ponto. A leitura…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_x67yqs.png)

Foque na interpretação das seguintes colunas na planilha:

| Coluna(s) | O que a informação representa | Dicas de Auditoria (Sua Gestão) |
| --- | --- | --- |
| **Data do Ponto** e **Tipo** | Indicam qual ponto foi alterado (ex: Entrada, Saída, Pausa, etc.) e em qual dia. | Permite identificar se as correções estão concentradas em um tipo de ponto específico (ex: sempre no retorno de pausa). |
| **Usuário** | Mostra **quem** realizou a alteração. Se o campo estiver preenchido (ex: Matheus Lucas Rh), a correção foi manual. | **Monitore:** Se houver correções em massa, verifique se o usuário que as executou tinha a permissão adequada. |
| **Data da Operação** | Indica a ação exata que foi feita. | **Identifique padrões:** Se a "Operação" for sempre "Ponto adicionado" em um local, pode haver um problema de registro nos coletores desse time. |
| **Motivo** | Explica o motivo da alteração (ex: Correção manual, Criação a partir da rotina cadastrada do funcionário, etc.). | **Foque na rastreabilidade:** Garanta que todos os lançamentos manuais tenham um motivo que justifique a intervenção. |
| **Correção Automática** | Indica se a correção foi realizada automaticamente pelo sistema (valor "Sim") ou se foi uma intervenção manual (campo em branco). | O valor "Sim" geralmente está ligado à funcionalidade de **Correção Automática de Pontos**, que ajuda na prevenção de erros. |

> 💡 Dicas para a sua gestão:

- **Identifique padrões de ajuste:** Use o R15 para verificar se as correções se concentram em um mesmo grupo de colaboradores, em um mesmo Local de Trabalho ou em um mesmo tipo de erro (ex: sempre falta de registro na saída). Isso ajuda a identificar a necessidade de treinamento ou melhorias nos coletores. As abas **Ranking Locais de trabalho**e \*\*Ranking por funcionário \*\* do relatório R15 ajudam nessa análise.
- **Monitore a performance do RH/Gestores:** Verifique quem está realizando as alterações (coluna "Usuário"), a frequência e o tipo de correção. Isso garante que a política de **transparência** na gestão do ponto esteja sendo seguida internamente.

---

Com o R15, você tem o controle total sobre as alterações da folha de ponto, garantindo a segurança e a transparência da sua **gestão** e facilitando auditorias.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
