---
id: "39384016034199"
titulo: "Erro no lançamento do valor do plano de saúde no informe de rendimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39384016034199-Erro-no-lan%C3%A7amento-do-valor-do-plano-de-sa%C3%BAde-no-informe-de-rendimento"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:33Z"
rotulos: ["Folha", "eSocial", "Configuração Funcionários", "Plano de Saúde", "Erro", "Artigo criado KCS", "Informe de Rendimentos", "Sankhya RH - KCS"]
---

# Erro no lançamento do valor do plano de saúde no informe de rendimento

**Mensagem**

Valores do plano de saúde estão sendo apresentados de forma incorreta ou em duplicidade no Informe de Rendimentos, principalmente no **Campo 7 – Informações Complementares**.

**Situação**

Ao emitir o **"Informe de Rendimentos"** dos colaboradores, os valores relacionados ao plano de saúde apresentam inconsistências, como:

- Valores duplicados para dependentes no campo 7 - Informações Complementares
- Evento incorreto sendo utilizado no lançamento.
- Agrupamento incorreto quando existem múltiplos convênios com o mesmo CNPJ cadastrados

**Solução**

Para corrigir os erros no lançamento do plano de saúde no informe de rendimentos, siga os passos abaixo:

**(1)** Acesse a tela **"Planos de Saúde"** (Pessoal+ » Cadastros » Plano de Saúde) e verifique se existem múltiplos convênios cadastrados com o mesmo CNPJ.

**(2)** Caso sejam identificados convênios duplicados, remova o evento de desconto do plano de saúde na aba '**Eventos'** do cadastro do convênio. Se o plano não estiver vinculado a **nenhum colaborador**, faça a exclusão do cadastro duplicado para evitar inconsistências nas informações e nos cálculos.

**(3)** Verifique se o evento descontado na folha do colaborador está corretamente vinculado ao plano de saúde cadastrado para ele. Para isso, acesse **"Configuração de Funcionários"** (**Pessoal+ > Cadastros > Configuração de Funcionários**) e confirme se o plano de saúde associado ao colaborador corresponde ao mesmo plano vinculado ao evento informado no **cadastro do convênio** e utilizado no **desconto em folha**.

![Imagem 1: (1) Acesse a tela "Planos de Saúde" (Pessoal+ » Cadastros » Plano de Saúde) e verifique se existem múltiplos convênios…](https://ajuda.sankhya.com.br/hc/article_attachments/40953218348311)![Imagem 2: (1) Acesse a tela "Planos de Saúde" (Pessoal+ » Cadastros » Plano de Saúde) e verifique se existem múltiplos convênios…](https://ajuda.sankhya.com.br/hc/article_attachments/40952528312471)

![Imagem 3: (1) Acesse a tela "Planos de Saúde" (Pessoal+ » Cadastros » Plano de Saúde) e verifique se existem múltiplos convênios…](https://ajuda.sankhya.com.br/hc/article_attachments/40951594114839)

**(4)** Caso o evento esteja incorreto, realize a retificação dos lançamentos, informando o evento correto, e recalcule a folha de pagamento do colaborador. Caso identifique que o plano de saúde não está devidamente vinculado ao cadastro do colaborador, ou do dependente, efetue a vinculação correspondente para que os valores sejam consolidados corretamente no sistema.

**Importante:** atente-se ao campo **Optante**, pois é essa configuração que determina se o desconto do evento será atribuído ao **titular** ou ao **dependente** do plano de saúde.

![Imagem 4: Importante: atente-se ao campo Optante , pois é essa configuração que determina se o desconto do evento será atribuído…](https://ajuda.sankhya.com.br/hc/article_attachments/40952612213271)

**(5)** Verifique também se não existem cadastros duplicados do mesmo plano de saúde sem **referência** final. Quando há dois ou mais registros ativos do mesmo plano para o colaborador, os valores podem ser considerados em duplicidade na geração do **Informe de Rendimentos**. Isso se aplica tanto ao titular quanto ao dependente, de forma distinta.

Nesse cenário, apenas um cadastro deve permanecer sem data de **referência** final, pois ele será considerado o registro ativo do colaborador. Os demais cadastros devem ser encerrados com a respectiva data de término para evitar a duplicidade das informações.

**(6)** Após os ajustes, emita novamente o **"Informe de Rendimentos"** e verifique se os valores do plano de saúde estão corretos no **"Campo 7 - Informações Complementares"**.

**Pontos de atenção:**

Caso identifique que o valor foi descontado na folha de pagamento, mas não foi enviado ao eSocial, acesse o **Gerenciador de Folhas** (**Pessoal+ > Rotinas Folha > Gerenciador de Folhas**), selecione a referência correspondente ao cálculo e localize o colaborador. Lembre-se de que o IR é apurado pela **data de pagamento**, e isso inclui os valores de plano de saúde.

Em seguida, abra a folha, clique no card do colaborador, habilite a seleção e utilize a opção **"Atualizar dados do plano de saúde"**.

Ao realizar esse procedimento, as informações do evento serão atualizadas no cadastro do plano de saúde. Após bloquear e liberar novamente a folha, o evento passará a compor corretamente os dados enviados ao eSocial para o colaborador, e, após o reenvio do S-1210, na rotina **S-5002 - Conferência de IRRF (**Pessoal+ » Consultas » S-5002 - Conferência IRRF**)** clique em reprocessar consolidação para que os valores **sejam ajustados** no dashboard.

![Imagem 5: Ao realizar esse procedimento, as informações do evento serão atualizadas no cadastro do plano de saúde. Após bloquear…](https://ajuda.sankhya.com.br/hc/article_attachments/40952487459095)

 ![Imagem 6: Ao realizar esse procedimento, as informações do evento serão atualizadas no cadastro do plano de saúde. Após bloquear…](https://ajuda.sankhya.com.br/hc/article_attachments/40952487460503)

![Imagem 7: Ao realizar esse procedimento, as informações do evento serão atualizadas no cadastro do plano de saúde. Após bloquear…](https://ajuda.sankhya.com.br/hc/article_attachments/40952937116055)

**Causa**

Os erros no lançamento do plano de saúde no informe de rendimentos podem ocorrer por:

- **Múltiplos convênios cadastrados com o mesmo CNPJ:** o sistema agrupa os valores de todos os convênios com CNPJ idêntico, causando duplicidade nos valores dos dependentes.
- **Evento incorreto vinculado ao plano:** quando o evento utilizado não corresponde ao tipo correto de lançamento para plano de saúde.
- **Cadastro incompleto do plano de saúde:** falta de informações essenciais no cadastro do convênio ou na vinculação com os funcionários e dependentes.
- **Incidência incorreta** do evento de descosto de plano de saúde.
