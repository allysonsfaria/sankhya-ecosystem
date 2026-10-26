---
id: "42427312393751"
titulo: "R19 - Como gerar a Planilha de Histórico Disciplinar (Dispensas, Suspensões e Observações)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427312393751-R19-Como-gerar-a-Planilha-de-Hist%C3%B3rico-Disciplinar-Dispensas-Suspens%C3%B5es-e-Observa%C3%A7%C3%B5es"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-07T16:17:39Z"
rotulos: ["sync_hc", "pontotel", "sync_hash_cf9773fa3dba", "pontotel_6a3329f6bfcc21bf3d3c4c1b"]
---

# R19 - Como gerar a Planilha de Histórico Disciplinar (Dispensas, Suspensões e Observações)

O relatório **R19 - Planilha de Histórico Disciplinar** é uma ferramenta de **gestão** que gera uma visão consolidada de todos os eventos de ausência e disciplina lançados na folha de ponto dos colaboradores, como [dispensas](https://sankhya.zendesk.com/hc/pt-br/articles/42427229767959) (atestados), [suspensões](https://sankhya.zendesk.com/hc/pt-br/articles/42427237531671) e observações.

Este relatório é crucial para conferências internas, análise de padrões e auditoria de documentos.

---

## Como gerar o Relatório

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de Relatórios (à direita), selecione a opção **R19 - Planilha de Histórico Disciplinar**.
3. Defina os filtros para a sua consulta:

   - **Filtro principal:** Você pode filtrar por **locais de trabalho**, **empregadores**, **empregados** ou **grupos**.
   - **Período:** Selecione o intervalo de datas (início e fim) que deseja consultar. É essencial que este período abranja as datas dos eventos que você quer visualizar.
4. Se necessário, utilize as opções avançadas:

   - **considerar empregados demitidos:** Inclui colaboradores que foram demitidos dentro do período filtrado.
   - **considerar dispensas do mesmo tipo posteriores ao período filtrado:** Permite que dispensas longas que começaram no período selecionado, mas terminam até 180 dias depois, sejam incluídas.
   - **Enviar os resultados do relatório por e-mail:** Recebe uma cópia do arquivo por e-mail
5. Clique em **Gerar Excel**.

![Imagem 1: Clique em Gerar Excel .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_y2wsxe.png)

---

## Como baixar o Relatório gerado

Após clicar em "Gerar Excel", a plataforma processará o relatório em segundo plano:

1. No menu de navegação, clique no **ícone de sino** (Notificações), para acompanhar o arquivo ser gerado.
2. Quando chegar a "100%", o relatório será baixado automaticamente.
3. Caso o download não tenha sido feito automaticamente, clique no **ícone de nuvem** (download) ao lado do nome do relatório para baixar o arquivo para o seu computador.
4. O arquivo será baixado como um arquivo compactado (ZIP), contendo três planilhas internas:

   - **r19-sucesso:** O relatório principal com todos os dados.
   - **r19-status:** Uma planilha de status da importação.
   - **r19-erro:** Uma planilha que lista eventuais erros que ocorreram durante a geração dos dados.
5. Abra o arquivo compactado e localize a planilha **r19-sucesso** para a sua conferência.

---

## Como fazer a leitura do relatório

![Visão da aba Planilha Detalhada](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1of7w0m.png)

Visão da aba Planilha Detalhada

O R19 contém três abas principais, oferecendo diferentes níveis de detalhe para a sua **auditoria** e **gestão**:

| Aba (Planilha) | Coluna(s) Chave | O que a informação representa | Dicas de Auditoria (Sua Gestão) |
| --- | --- | --- | --- |
| **Planilha Detalhada** | **TIPO** e **MOTIVO**, **JORNADA DO DIA**. | Lista linha por linha cada dia e tipo de evento lançado (Dispensa, Suspensão, etc.). Inclui o link direto para o **Atestado** (se houver). | **Rastreabilidade:** Utilize a coluna final (URL) para **acessar os anexos** (atestados/documentos) e verificar o comprovante original. |
| **Planilha Agregada** | **TIPO**, **MOTIVO**, **TOTAL DE DIAS**, **HORAS DISPENSADAS**, **NOME DO MÉDICO**, **CRM**. | Agrupa as informações de eventos idênticos (ex: 3 dias de atestado do mesmo tipo). | **Conferência de Dados:** Foco na **Especialidade** e **CRM** para cruzar com as informações de atestados e documentos médicos. |
| **Resumo** | **DISPENSAS EM DIAS**, **SUSPENSÕES EM DIAS**, **TOTAL DE INCIDÊNCIAS**. | Visão consolidada e quantificada dos dias de incidências (Dispensa, Suspensão e Observação) por colaborador. | **Absenteísmo:** Ideal para métricas de **pessoas** e **evolução**. Use o **TOTAL DE INCIDÊNCIAS** para monitorar a frequência de eventos por colaborador. |

---

O R19 oferece a **transparência** necessária para auditorias de afastamentos justificados ou eventos disciplinares. Com o relatório em mãos, você tem todos os dados para a **gestão** de folha e análise de padrões de ausência.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
