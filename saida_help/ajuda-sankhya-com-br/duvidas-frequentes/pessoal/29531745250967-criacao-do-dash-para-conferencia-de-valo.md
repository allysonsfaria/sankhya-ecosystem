---
id: "29531745250967"
titulo: "Criação do dash para conferência de valores DIRF por funcionário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29531745250967-Cria%C3%A7%C3%A3o-do-dash-para-confer%C3%AAncia-de-valores-DIRF-por-funcion%C3%A1rio"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-13T17:51:08Z"
rotulos: ["Configuração", "Relatórios", "Funcionários", "BI", "DIRF", "Folha de Pagamento", "Criação do dash para conferência de valores DIRF por funcionário"]
---

# Criação do dash para conferência de valores DIRF por funcionário

**Veja abaixo o passo a passo para criação do dash para conferência de valores DIRF por funcionário:**

![Imagem 1: Acesse a tela " Construtor de Componentes de BI" (Configurações » Avançado » Construtor de Componentes de BI)](https://ajuda.sankhya.com.br/hc/article_attachments/29534601651223) Acesse a tela **"Construtor de Componentes de BI"** (Configurações » Avançado » Construtor de Componentes de BI)

![Imagem 2: Selecione a opção "+"](https://ajuda.sankhya.com.br/hc/article_attachments/29534601658391) Selecione a opção **"+"**

![Imagem 3: Selecione a opção "+"](https://ajuda.sankhya.com.br/hc/article_attachments/29538429745815)

![Imagem 4: Dê o título para a tela, sugestão: "DASH CONFERÊNCIA DIRF 2025" e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/29534616657303) Dê o título para a tela, sugestão: **"DASH CONFERÊNCIA DIRF 2025"** e salve:

![Imagem 5: Dê o título para a tela, sugestão: "DASH CONFERÊNCIA DIRF 2025" e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/29538413741591)

![Imagem 6: Arraste o controle tabela nos componentes para a área amarela:](https://ajuda.sankhya.com.br/hc/article_attachments/29534616663575) Arraste o controle **tabela** nos componentes para a área amarela:

![Imagem 7: Arraste o controle tabela nos componentes para a área amarela:](https://ajuda.sankhya.com.br/hc/article_attachments/29531719854871)

![Imagem 8: Dê dois cliques na tabela arrastada:](https://ajuda.sankhya.com.br/hc/article_attachments/29534616668311) Dê dois cliques na tabela arrastada:

![Imagem 9: Dê dois cliques na tabela arrastada:](https://ajuda.sankhya.com.br/hc/article_attachments/29538429751703)

![Imagem 10: Selecione o botão "Editar" :](https://ajuda.sankhya.com.br/hc/article_attachments/29534601690263) Selecione o botão **"Editar"**:

![Imagem 11: Selecione o botão "Editar" :](https://ajuda.sankhya.com.br/hc/article_attachments/29538413754647)

(1)**  Informações referente ao plano de saúde:**

**(2)**Parâmetro **FPDTPLANOSAUDE:** - Data para gravação do plano de saúde;

**(2)**A tabela TFPVPS grava as informações de acordo com o dado definido no parâmetro citado acima;

**(2)**Se configurado como **Referência**, irá gravar por exemplo em 01/01/2024 o valor do plano de saúde que foi calculado na folha da referência 01/2024, independente da data de pagamento.

**(2)**Se configurado como **Data de pagamento**, irá gravar por exemplo em 01/01/2024 o valor do plano de saúde que foi calculado na folha da referência 12/2023 e com data de pagamento 05/01/2024.

Portanto,

![Imagem 12: Insira a consulta SQL abaixo na aba "Consulta" :](https://ajuda.sankhya.com.br/hc/article_attachments/29535761058839) Insira a consulta SQL abaixo na aba **"Consulta"**:

**Importante!**

**(1)** Se você utiliza o parâmetro FPDTPLANOSAUDE como **Data de pagamento,** use a consulta:

**Banco SQL:** [SQL DIRF PLANO DATA DE PAGAMENTO](https://drive.google.com/file/d/1nmbdZFVW_FGQTCVh8lRg5k4MSgApDj6M/view?usp=drive_link)

**Banco ORACLE:** [ORACLE DIRF PLANO DATA DE PAGEMTNO](https://drive.google.com/file/d/1A1ZjsZ7kk3Dl6lclkaPmuWb-R7lhxitH/view?usp=drive_link)

**(1)** Se você utiliza o parâmetro FPDTPLANOSAUDE como **Referência,** use a consulta:

**Banco SQL:** [SQL DIRF PLANO REFERÊNCIA](https://drive.google.com/file/d/1nmbdZFVW_FGQTCVh8lRg5k4MSgApDj6M/view?usp=drive_link)

**Banco ORACLE:** [ORACLE DIRF PLANO REFERÊNCIA](https://drive.google.com/file/d/17hdVTOX6byims7W2yod3kosEXY2ip1Tz/view?usp=drive_link)

![Imagem 13: Banco ORACLE: ORACLE DIRF PLANO REFERÊNCIA](https://ajuda.sankhya.com.br/hc/article_attachments/29538429764503)

![Imagem 14: Se estiver tudo certo com a consulta, as colunas serão carregadas:](https://ajuda.sankhya.com.br/hc/article_attachments/29536750952983) Se estiver tudo certo com a consulta, as colunas serão carregadas:

![Imagem 15: Se estiver tudo certo com a consulta, as colunas serão carregadas:](https://ajuda.sankhya.com.br/hc/article_attachments/29538429767191)

![Imagem 16: Reescreva a descrição das colunas, conforme abaixo (se desejável):](https://ajuda.sankhya.com.br/hc/article_attachments/29536767364503) Reescreva a descrição das colunas, conforme abaixo (se desejável):

![Imagem 17: Reescreva a descrição das colunas, conforme abaixo (se desejável):](https://ajuda.sankhya.com.br/hc/article_attachments/29538413767703)

![Imagem 18: Desative o visível para o campo “ORDEM”:](https://ajuda.sankhya.com.br/hc/article_attachments/29536750964759)  Desative o visível para o campo **“ORDEM”:**

![Imagem 19: Desative o visível para o campo “ORDEM”:](https://ajuda.sankhya.com.br/hc/article_attachments/29538413769623)

![Imagem 20: Salve e volte no botão abaixo (se não voltar automático após o salvamento):](https://ajuda.sankhya.com.br/hc/article_attachments/29536750966935) **Salve**  e **volte** no botão abaixo (se não voltar automático após o salvamento):

![Imagem 21: Salve e volte no botão abaixo (se não voltar automático após o salvamento):](https://ajuda.sankhya.com.br/hc/article_attachments/29538429791895)

![Imagem 22: Insira o parâmetro CPF, para isso selecionar +:](https://ajuda.sankhya.com.br/hc/article_attachments/29536767388183)  Insira o parâmetro CPF, para isso selecionar +:

![Imagem 23: Insira o parâmetro CPF, para isso selecionar +:](https://ajuda.sankhya.com.br/hc/article_attachments/29538413773463)

![Imagem 24: Preencha os dados do parâmetro conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/29536767388183) Preencha os dados do parâmetro conforme abaixo:

**ID**: CPF

**Descrição**: CPF do colaborador

**Tipo**: Texto

**Requerido**: sim

**Salvar o último valor**: sim

**Limite de caracteres**: 11

![Imagem 25: Limite de caracteres : 11](https://ajuda.sankhya.com.br/hc/article_attachments/29531719903383)

![Imagem 26: Salve as alterações caso não esteja salvo e pré-visualize o dash criado:](https://ajuda.sankhya.com.br/hc/article_attachments/29536750982935) Salve as alterações caso não esteja salvo e pré-visualize o dash criado:

![Imagem 27: Salve as alterações caso não esteja salvo e pré-visualize o dash criado:](https://ajuda.sankhya.com.br/hc/article_attachments/29538413777559)

![Imagem 28: Será aberta uma janela com o dash criado. Informe o parâmetro para testar o funcionamento:](https://ajuda.sankhya.com.br/hc/article_attachments/29536750991511) Será aberta uma janela com o dash criado. Informe o parâmetro para testar o funcionamento:

![Imagem 29: Será aberta uma janela com o dash criado. Informe o parâmetro para testar o funcionamento:](https://ajuda.sankhya.com.br/hc/article_attachments/29531745200407)

![Imagem 30: Leitura do DASH:](https://ajuda.sankhya.com.br/hc/article_attachments/29536750997143) Leitura do DASH:

![Imagem 31: Leitura do DASH:](https://ajuda.sankhya.com.br/hc/article_attachments/29531719910807)

(1)** Valores por referência, data de pagamento e por tipo de contribuição na DIRF.**

As linhas azuis representam o total de cada código configurado para a BASE DIRF, para facilitar a conferência no PGD se necessário.

![Imagem 32: Liberação do dash criado nas telas e publicação para os usuários:](https://ajuda.sankhya.com.br/hc/article_attachments/29536751001367) **Liberação do dash** criado nas telas e publicação para os usuários:

É necessário inserir o dash criado em um menu. Para isso, acesse a tela: **"Construtor de Dashboards"** (Configurações » Avançado » Construtor de Dashboards), selecione **"+",** depois clique em **"Nova Solução"**:

![Imagem 33: É necessário inserir o dash criado em um menu. Para isso, acesse a tela: "Construtor de Dashboards" (Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/29538429797143)

![Imagem 34: Insira o mesmo título do dash criado: DASH CONFERÊNCIA DIRF 2025](https://ajuda.sankhya.com.br/hc/article_attachments/29536751007767) Insira o mesmo título do dash criado: DASH CONFERÊNCIA DIRF 2025

![Imagem 35: Insira o mesmo título do dash criado: DASH CONFERÊNCIA DIRF 2025](https://ajuda.sankhya.com.br/hc/article_attachments/29538413787927)

![Imagem 36: Pesquise o DASH criado na galeria e arraste-o para a área amarela e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/29536767416983) Pesquise o DASH criado na galeria e arraste-o para a área amarela e salve:

![Imagem 37: Pesquise o DASH criado na galeria e arraste-o para a área amarela e salve:](https://ajuda.sankhya.com.br/hc/article_attachments/29531745218455)

![Imagem 38: Em outras opções, selecione a opção “Adicionar Lançador”](https://ajuda.sankhya.com.br/hc/article_attachments/29536751017367) Em outras opções, selecione a opção **“Adicionar Lançador”**

![Imagem 39: Em outras opções, selecione a opção “Adicionar Lançador”](https://ajuda.sankhya.com.br/hc/article_attachments/29538429803287)

![Imagem 40: Escolha a descrição da tela, sugere-se ser o mesmo nome do DASH DASH CONFERÊNCIA DIRF 2025 , defina o menu no qual…](https://ajuda.sankhya.com.br/hc/article_attachments/29536767426199) Escolha a descrição da tela, sugere-se ser o mesmo nome do DASH DASH CONFERÊNCIA DIRF 2025, defina o menu no qual deseja que o dash seja inserido, (como por exemplo Pessoal + > Rotinas Folha) e clique em **"Concluir":**

![Imagem 41: Escolha a descrição da tela, sugere-se ser o mesmo nome do DASH DASH CONFERÊNCIA DIRF 2025 , defina o menu no qual…](https://ajuda.sankhya.com.br/hc/article_attachments/29538413798423)

![Imagem 42: Vá até a tela de acessos e libere o dash (tela) criado para os usuários ou grupos desejados:](https://ajuda.sankhya.com.br/hc/article_attachments/29536767430935)  Vá até a tela de acessos e libere o dash (tela) criado para os usuários ou grupos desejados:

![Imagem 43: Vá até a tela de acessos e libere o dash (tela) criado para os usuários ou grupos desejados:](https://ajuda.sankhya.com.br/hc/article_attachments/29538429809175)

**Importante:** salientamos que este DASH é **personalizado**. Caso queira realizar qualquer ajuste ou complemento, solicite o apoio da Equipe de Serviços (**Unidade**).
