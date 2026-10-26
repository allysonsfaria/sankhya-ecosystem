---
id: "4411800642327"
titulo: "Operações Monitoradas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4411800642327-Opera%C3%A7%C3%B5es-Monitoradas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:02:09Z"
rotulos: ["Configuração", "Monitoramento", "Agendamento", "Preferências", "br.com.sankhya.mge.ConfiguracaoDeProcessos", "Telemetria da aplicação", "Operações Monitoradas", "Controle de Acesso", "Gerenciamento de Agendamentos de Monitoramento"]
---

# Operações Monitoradas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311126402711) Módulo: Configurações > Controle de Acesso       ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311126410391) Versão: a partir da 4.19
```

---

![Imagem 3: Para utilizar esta tela é necessário habilitar o parâmetro "Habilitar tela da Telemetria - HABILITATEAPP" na tela de…](https://ajuda.sankhya.com.br/hc/article_attachments/16673157948055) Para utilizar esta tela é necessário habilitar o parâmetro **"Habilitar tela da Telemetria - HABILITATEAPP"** na tela de [Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834).

Aqui, você pode realizar agendamentos de monitoramentos por diferentes tipos de operações.

![Imagem 4: Aqui, você pode realizar agendamentos de monitoramentos por diferentes tipos de operações.](https://ajuda.sankhya.com.br/hc/article_attachments/4411794074903)

No Painel de Filtros, você pode utilizar os filtros **"Código"**, **"Nome Agendamento"**, **"Job"**, **"Data"**, **"Hora"** e/ou **"Status"** para localizar um agendamento.

Para criar um cadastro, clique no botão ![Imagem 5: Para criar um cadastro, clique no botão "Adicionar" , e assim, será aberto o pop-up "Cadastrar Agendamento" onde você…](https://ajuda.sankhya.com.br/hc/article_attachments/16673326649239) **"Adicionar"**, e assim, será aberto o pop-up **"Cadastrar Agendamento"** onde você irá inserir as seguintes informações:

![Imagem 6: Para criar um cadastro, clique no botão "Adicionar" , e assim, será aberto o pop-up "Cadastrar Agendamento" onde você…](https://ajuda.sankhya.com.br/hc/article_attachments/4411792484631)

O **"Código"** será preenchido pelo sistema.

Informe um **"Nome agendamento"** para a identificação do mesmo.

Selecione o **"Tipo Operação"** que deseja acompanhar conforme as opções:

- Default;
- Job-legacy;
- Job;
- Report job;
- Http.

No campo **"Serviço"**, preencha um ou mais serviços que deseja monitorar. Caso queira monitorar mais de um serviço, separe-os por vírgula.

Em **"Job"**, insira um ou mais Job’s que serão monitorados, separando-os por vírgula.

No campo **"Tempo mínimo para dump(ms)"**, deve ser informado um valor mínimo de tempo para monitoramento, é necessário que esse valor seja superior a 1000 ms. Considere ainda que, tudo o que possuir menos que o valor mínimo informado será descartado.

Selecione o **"Usuário Monitorado"**.

Você pode definir nos campos referente à **"Data"**, o intervalo de dias para realização do monitoramento.

Em **"Hora"**, preencha a quantidade de horas que deseja monitorar.

Selecione a opção **"Habilitar Agendamento"** para que a aplicação possa monitorar as atividades.

Além disso, no botão **"Excluir"** da tela é possível realizar exclusões dos agendamentos cadastrados.

Além do botão **"Limpar Samples"**, que irá deletar os arquivos que foram baixados através do botão **"Download"**.

Todos os agendamentos cadastrados na tela serão monitorados ao habilitar a marcação **"Monitorar"**. Ao desabilitá-la nenhum dos agendamentos serão monitorados.

**Observação:** se desejar pausar um monitoramento específico, desabilite a marcação Habilitar Agendamento no pop-up **"Editar Agendamento"**.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4411800642327-Opera%C3%A7%C3%B5es-Monitoradas#top)
