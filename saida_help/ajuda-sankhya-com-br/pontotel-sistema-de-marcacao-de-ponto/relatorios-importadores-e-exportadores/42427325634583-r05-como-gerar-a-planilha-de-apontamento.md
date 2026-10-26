---
id: "42427325634583"
titulo: "R05 - Como gerar a planilha de apontamentos do mês (Resumo de Folha)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427325634583-R05-Como-gerar-a-planilha-de-apontamentos-do-m%C3%AAs-Resumo-de-Folha"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:53:26Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a33ede44becd40653e4ee7e", "sync_hash_9247cc4900b8"]
---

# R05 - Como gerar a planilha de apontamentos do mês (Resumo de Folha)

O **R05 - Planilha de apontamentos dos empregados no mês** é uma ferramenta essencial para a conferência final da folha de pagamento.

Diferente do Espelho de Ponto (R01), que mostra o dia a dia, o R05 traz os **totais consolidados** do período. Ele soma todas as horas extras, atrasos, faltas e outros eventos de cada colaborador, entregando uma visão resumida e pronta para análise gerencial ou envio para a contabilidade.

---

## Como Gerar o Relatório

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de Relatórios (à direita), selecione a opção **R05 - Planilha de apontamentos dos empregados no mês**.
3. Defina os filtros para a sua consulta:

   - **Filtro principal:** Você pode filtrar por **locais de trabalho**, **empregadores** ou**grupos**.
   - **Período:** Selecione o mês e o ano que deseja consultar.
4. Configure os campos opcionais da seção "quais informações mostrar?":

   - **PIS, função e empregador dos empregados**: Inclui essas informações no relatório para facilitar a identificação dos colaboradores.
   - **Supervisor do local de trabalho**: Exibe o nome do supervisor responsável pelo colaborador ou local de trabalho.
   - **Estados e cidades dos locais de trabalho**: Mostra a localização geográfica de cada local de trabalho.
   - **Ignorar demitidos no mês**: Exclui colaboradores demitidos do relatório.
5. Configure as "opções extras":

   - **Enviar os resultados do relatório por e-mail**: Marque essa opção caso deseje receber o relatório também por e-mail. O arquivo será enviado automaticamente para o endereço de e-mail cadastrado no usuário que realizou a solicitação.
   - **Formato hora/minuto (hh:mm)**: Por padrão, o relatório apresenta os valores em formato decimal. Marque essa opção para que os valores dos apontamentos venham em formato de hora e minuto.

   ![Imagem 1: Formato hora/minuto (hh:mm) : Por padrão, o relatório apresenta os valores em formato decimal. Marque essa opção para…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_cvddy2.png)
6. Clique em **Gerar Excel** (o botão verde no canto inferior direito).

---

## Como baixar o Relatório

Após clicar em "gerar excel", a plataforma processará o relatório em segundo plano:

1. Clique no **ícone de sino** (Notificações), no canto inferior esquerdo do menu de navegação, para acompanhar o arquivo ser gerado.
2. Quando for finalizado, o relatório será baixado para seu computador automaticamente.
3. O R05 é baixado como um arquivo compactado (ZIP). Ao extrair o arquivo, você verá três planilhas:

   - **r05-sucesso:** O relatório principal com todos os dados.
   - **r05-status:** Um arquivo técnico sobre o status da geração.
   - **r05-erro:** Lista eventuais erros na geração.
4. Abra o arquivo **r05-sucesso** para iniciar sua análise.

---

## Como fazer a leitura do relatório

A planilha R05 consolida os **totais** do mês. Cada linha representa um colaborador e as colunas trazem o somatório de cada tipo de evento.

| Grupo de Informações | Colunas Principais | Dicas de Auditoria (Sua Gestão) |
| --- | --- | --- |
| **Identificação** | Nome, Código, CPF, RG, Data de admissão, Local de Trabalho, Dia de início da folha, Data de demissão, Razão social e CNPJ. | Utilize o **Código** ou **CPF** para cruzar os dados com segurança na comparação com o seu sistema de folha de pagamento. |
| **Jornada e Frequência** | **H. Trabalhadas**, **H. Previstas**, **Dias Trab**, **Dias Trab. previstos**. | Compare "H. Trabalhadas" com "H. Previstas" para ter uma visão macro de quem cumpriu a carga horária ou quem teve muitas variações. |
| **Horas Extras** | **H. Extra**, **H. Extra Not** (Noturna), **H. Extra Ext.** (Extras em folga/feriado), **H. Extra Especial**. | O relatório separa as horas extras por tipo (diurna, noturna, feriado). Verifique os totais para garantir que estão dentro do orçamento da área. |
| **Ausências e Descontos** | **H. de Atraso**, **H. Saída Antecipada**, **H. em Faltas**, **Faltas** (em dias), Dias dispensa, Dias susp., **Dias s/ DSR** (Desconto de Repouso). | **Atenção ao DSR:** A coluna "Dias s/ DSR" indica quantos dias de descanso semanal remunerado o colaborador perdeu devido a faltas ou atrasos na semana. |
| **Noturno e Adicionais** | **Adic. Noturno** (Adicional), **Red. noturna** (Hora reduzida), **H. de Inter-Jornada**. | **Conformidade:** Verifique se a coluna "H. de Inter-Jornada" possui valores, pois isso indica que o colaborador não descansou as 11h obrigatórias entre turnos. |
| **Status da Folha** | **Folha travada**. | Indica "Sim" ou "Não". Garante que você está usando dados de uma folha que já foi auditada e fechada pelo gestor. |

![Imagem 2: Indica "Sim" ou "Não". Garante que você está usando dados de uma folha que já foi auditada e fechada pelo gestor.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1onwllr.png)

---

O R05 é o seu "resumão" do mês. Ele transforma todos os registros diários em números consolidados, agilizando o fechamento da folha e garantindo que os pagamentos e descontos sejam feitos com precisão.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
