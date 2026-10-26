---
id: "42427413992983"
titulo: "Nova Integração Power BI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427413992983-Nova-Integra%C3%A7%C3%A3o-Power-BI"
trilha: "PLOOMES: Automação de propostas  > Integrações nativas"
atualizado_em: "2026-08-10T18:01:11Z"
rotulos: ["sync_hc", "ploomes", "ploomes_8250782", "sync_hash_53b48c78fd9c"]
---

# Nova Integração Power BI

O Power BI é uma ferramenta de inteligência de dados da Microsoft que permite a realização de análises complementares às realizadas pelo módulo de relatórios do Ploomes, possibilitando uma maior variedade de gráficos e análises estatísticas.

A integração com o Power BI permite conectar os dados do Ploomes ao Power BI de forma simples e configurar atualizações recorrentes das informações exportadas.

## Requisitos para a Integração

Para utilizar a integração, é necessário possuir uma conta Microsoft com acesso ao Power BI.

## Como ativar a integração

1. No menu lateral do Ploomes, acesse **Administração > Integrações plug-and-play**.
2. Localize a integração **Power BI**.
3. Clique em **Habilitar integração**.
4. Em seguida, clique em **Ativar integração**.

![Interface gráfica do usuário, AplicativoDescrição gerada automaticamente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427627865/c847083fa747a8850964db46a63e/Y6zkVt9WWaZNXUBpx84GFc7F3A85qlYuctaguZZ3ebHkVf6XQ0uWnsc3fWb2ypsWGnRcrINWhocJhv9c1vNLEZ5rFbSP493MnL2j_ovSDZvBDT3FcIrTVbMixtEscbE7kSqDD99-W9m9I0zBm6BGNg?expires=1786536000&signature=4e1bd06a16c8c5e22af6e4505572dddc774b5fb4adb6fafe2ce368ff75e89486&req=diQlEc98molZXPMW3nq%2BgcgIK3aqYaf1iqEzE1oHxF1NAuhGh5LBG%2F6b0p9I%0AxOwmrGb9MPDSUpQC00xV0TpyfLE%3D%0A)

![Imagem 2: Em seguida, clique em Ativar integração .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427628370/10f14f001c01f4d80c0547da0449/OkZ29SdTagk_Kh7AszQWv6bihcYMhQY7nezBbnJaKTccwBMGEM6GY2XapGUNIfV0aZ80rmqUWcYhWVLRFsbVGHUGI-ItYMwyFUTc91GjGlfCNrn1FEhNKL2dRaxUozFdR1CdKgJmXtBw2R5-phfPVQ?expires=1786536000&signature=bf19434a795ffb8b409ecbfecbdc412410d369c82de40a19dbd9e9f03b060618&req=diQlEc98lYJYWfMW3nq%2BgfSeGYnfkf84t2g2dqDQ%2FiAsZIY8%2FzoLPRz4fgQy%0ARu6DD2eynjL2B1ydEDWj7zoStas%3D%0A)

Ao ativar a integração, um usuário de integração chamado **Power BI** será criado automaticamente. Esse usuário mantém a conexão ativa entre o Ploomes e o Power BI, mesmo sem usuários logados na conta.

## Configuração de expiração dos links

Durante a ativação, é possível definir se os links de exportação irão expirar.

![Interface gráfica do usuário, Aplicativo, TeamsDescrição gerada automaticamente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427630261/b0bd077e0ace634b3b3be2cfcac6/r6dLPN9oMaSSV1ljHUoPZPxFyfYiaRpjm19H5YiNPgSP6Bbv10NB-wagUa6nJ7a36rhuFaqGtkERrZ51i5fQeC6_Q9af53SIUfRDpGSnWHsQbpVsjRxZkweh6hUuG8lPmVKc454hYsM7a2Ys2xk7Ww?expires=1786536000&signature=71db2d90f5878de096cbbbfedec46453b0c387766c97a3b0d786fb61db5aab22&req=diQlEc99nYNZWPMW3nq%2BgfLkGp4jPrfiq0Z%2F2GqJ910RBloLfldZL4gAi59i%0AIO9NfG61iouebbxVV7tCWhhNUjU%3D%0A)

Caso a expiração seja habilitada:

- O prazo deve ser definido em dias;
- O limite máximo permitido é de 1000 dias.

Se nenhum prazo for definido, o link terá expiração padrão de 60 dias.

### Observações importantes

- Links gerados por usuários desativados são expirados automaticamente.
- Quando o link expira, não é possível mais utilizá-lo para acessar os dados da aba **no** Power BI; é necessário exportar novamente a aba.
- A atualização dos dados continuará funcionando mesmo que o usuário encerre sua sessão no Ploomes.

## Como exportar abas para o Power BI

Após ativar a integração, a opção **Exportar para Power BI** ficará disponível nas ações da aba.

Para gerar um link de exportação:

1. Acesse a aba desejada.
2. Clique em **Exportar para Power BI**.
3. Aguarde a preparação do link.
4. Copie o link gerado.

![Imagem 4: Copie o link gerado.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427635114/b5600a875a268592a1bb74374872/image.png?expires=1786536000&signature=df9a344b434392b5618b046c454e037a3e94a31ab7e79724264ce06556cccf11&req=diQlEc99mIBeXfMW3nq%2BgV7WKWN7ytGmYrPSjuGdZtdvjxkFx6DpMJ2zm7mm%0AKMuNKLfyIH9vilEVdeClwqQhlDs%3D%0A)

### Observações

- Os links possuem atualização automática padrão a cada 60 horas.
- O horário inicial padrão da atualização é às 12h.
- Apenas usuários com permissão de exportação habilitada em **Perfis > Outros** poderão utilizar a funcionalidade.

  ![Imagem 5: Apenas usuários com permissão de exportação habilitada em Perfis > Outros poderão utilizar a funcionalidade.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427635962/3e91e45e14b43651146206244fc8/image.png?expires=1786536000&signature=2ac6beb005cb6a1b7dcba77756eb066e8259d6139045ad9f2e1e2d157f0b5f9c&req=diQlEc99mIhZW%2FMW3nq%2BgdT9nSOUCvth9OdFg0Q9GrqMna840veRaCIKO5pM%0ATRM8CYJ3VBsFiwSd%2BuTNvHyCY3Y%3D%0A)

## Como utilizar o link no Power BI

## Para abas menores (até 10 mil linhas)

1. Abra o Power BI.
2. Clique em **Obter Dados**.
3. Escolha a opção **Web**.
4. Cole o link de exportação.

![TextoDescrição gerada automaticamente com confiança baixa](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427642952/e8f7751f01e91bc558e7e4474f60/JaSyfMFzVifx9NmOf-0QxAGVchwiWjpU1oQmBdQyNVa5_VIC8ggN1TAH8OZgoSTOnrCmXQVlO7XZ4mBq5uFBRGmJ5afMjRrtBZlenuVkpCkhIGdWo3wsoabrUUgMyZU-3yYguVTLEiy26WWSWjPV7w?expires=1786536000&signature=2b08da87b15599fc68229da65b1ebee6f1330d745997f550c8e6e36cb81ab690&req=diQlEc96n4haW%2FMW3nq%2BgZJffs77T5s3yY0e1GFPaQ926RhJr2AhVOQOsg5I%0A1tJAHye%2Fx9teMYyfzP8XQraLDlM%3D%0A)

## Para abas maiores (acima de 10 mil linhas)

Para abas maiores, recomenda-se utilizar a importação via **Web Avançada**.

Nesse caso:

- Configure o campo **Tempo limite do comando em minutos**;
- Isso evita que a importação seja interrompida antes da conclusão.

Após finalizar a importação, aguarde o carregamento completo da aba para iniciar a análise dos dados.

Para substituir os links da versão anterior da integração pelos novos links, veja a seção "Expiração do link de exportação"**.**

## Como gerenciar exportações

Existem duas formas de gerenciar as exportações:

- Pelo ícone de exportação no canto superior direito;
- Pela aba **Suas Exportações** no perfil do usuário.

## Ícone de exportação

Ao clicar no ícone de exportação, é possível:

- Acompanhar exportações em andamento;
- Visualizar exportações em fila;
- Consultar exportações concluídas recentemente.

![Imagem 7: Consultar exportações concluídas recentemente.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427654480/dc2b1d23a1027802eab7e661b528/image.png?expires=1786536000&signature=b212a32e520606cf1bd961ccc87db41291480c301990db431369858e8558398c&req=diQlEc97mYVXWfMW3nq%2BgTi1keQeokq%2BfcWnfQ8ZE5Cns7aLy772wprdTOIX%0ATfYnlP3NbNKwyeuqyH9iGDnuW5c%3D%0A)

### Observações

- O número de exportações paralelas depende do plano contratado.
- O ícone exibe apenas as 3 últimas exportações concluídas.

## Suas Exportações

Na aba **Suas Exportações**, é possível:

- Visualizar exportações realizadas;
- Copiar links de exportação;
- Configurar a frequência de atualização dos dados.

![Tela de computador com texto preto sobre fundo brancoDescrição gerada automaticamente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427656782/0db2ffc401d454500297b7410813/gB5RozJW2va4jpuK3NFzBa_az4xRgI3SC1uXFfa5tMwil48PUXjPvIBIWsQswYF_HrChI1iFO7yvkDSA5Kh-Q7yAEQJVVul4BZREYlK9CCc5wNSId6ALYRMxqMdc879bURnXKltrKmsUr4lKlOS1Fg?expires=1786536000&signature=4be8b7e1365fe72aef8f4dd4f8afa0ae78c58a99e216ab49704880ec10e4dfd0&req=diQlEc97m4ZXW%2FMW3nq%2BgVBVVsN87gQxam4u0HnXV5EzhkJHL8TumIPjlJlN%0A%2B3X4R4JJbZI7NqSaJa8qqgODkd4%3D%0A)

## Limitações da integração

1. As alterações realizadas nas abas do Ploomes não aparecem automaticamente no Power BI em tempo real. A atualização ocorre conforme a frequência configurada para o link exportado e respeita os limites do plano contratado.
   Para consulta do plano contratado e seus limites basta seguir o passo a passo abaixo:

   ![Tela de computador com texto preto sobre fundo brancoDescrição gerada automaticamente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427663515/f6c92d598b173f37b57fd69b2457/c7Y-CpdTrN8G5OikAPtXLuUl5xM8j_Pse6bWzAv9O2A72PdABeTrg6nlx5b-TCAt7t78xQ6uFUfNFp1Ai7rDef2yvEM_alzwRzaFejNu9XDAZPidWnPrK8qZqUKJ85owCNGY7IBrtKHk7xvREY9gXg?expires=1786536000&signature=9d433918e493ddbde3914acc1a1c8eb7cb463e4c4cf237f663f33ad2a19b9880&req=diQlEc94noReXPMW3nq%2Bga6wMTHeDWkNLsI0jRbZuK4gr30LedlBW8eblKS9%0ACu4NLG4v38gORlmj%2BR4Ivrc83iE%3D%0A)
2. Abas muito grandes não podem ser integradas (por exemplo acima de 50 mil linhas e 30 colunas).
   Para abas acima de 50 mil linhas, recomendamos:

- Dividir os dados em abas menores;
- Aplicar filtros para reduzir o volume exportado.

## Limites por plano

| **Recurso** | **FREE** | **PRO** |
| --- | --- | --- |
| Abas integradas por conta | 10 | 50 |
| Frequência de atualização | 1 atualização a cada 8h | 1 atualização a cada 1h |
| Abas em exportação paralela (nova exportação ou atualização) | 5 | 10 |
| Colunas por aba | 30 | 30 |
| Linhas por aba | 50.000 | 50.000 |
| Abas em fila de espera (nova exportação ou atualização) | 50 | 50 |

**Observações:** atualizações futuras dos dados também podem ser realizadas sempre que necessário, respeitando os limites do plano contratado, mesmo que o usuário encerre sua sessão no Ploomes. Ou seja, uma vez feita a integração, não é mais necessário repetir o processo de obtenção de dados da web para atualização deles.

## Casos específicos

## 1. Expiração do link de exportação

O prazo de expiração do link de exportação é estabelecido em dias, e este valor pode ser personalizado de acordo com suas preferências, seguindo o passo a passo do vídeo abaixo. Se não for estabelecido um prazo de expiração, o sistema utilizará como padrão 60 dias para expiração do link.

![Imagem 10: O prazo de expiração do link de exportação é estabelecido em dias, e este valor pode ser personalizado de acordo com…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427674717/6e72f0220a8130829144274adc42/qcX08KzKbg8HS09rn4ICAH88X1xYmfSZJ7PMUBzM8pQDAcIuik61k2IsGEkqKv2XbPptY3sJ9_X_EhgtwbYxwK_XZgpY6rDKA0q4ANl9twDbLJ1g-qCWMSRiA2ElkYwpATM3J8jjddGRc8Ho2sTgQQ?expires=1786536000&signature=9451937968cdb45f35ae4c23005f8340c1788dc89f6f7154f44a614a65337431&req=diQlEc95mYZeXvMW3nq%2BgcK8mblPuCX7PNu5R57Qv36TtCJVycMRKQ5Bnx7p%0Ae4lxR7bu%2B6zdqc6Znb5rRRlVh0k%3D%0A)

Durante esse período de expiração, é possível realizar a revalidação do link seguindo o passo a passo abaixo.

![Imagem 11: Durante esse período de expiração, é possível realizar a revalidação do link seguindo o passo a passo abaixo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427674716/6a9f11aac4c36c86666098a3d2ed/LWuglbT3Tt1z_EdbQ3vbbw3J752c7RivyBdzrYj9Zjh2Jk0SS2PlI9o8y4Y1RdzsKb6IgGi-ERk-q3jOVadZXUsrOPE_mK1qhQJhjoAZ-jhmFNB2g6XfcoZHVp_GC47yiStgz0hJqvDkZfdbYoFy0Q?expires=1786536000&signature=67ce7c53e2e9a66bc5b1ba656b06997e1a7362b0f908bb6c463be9ee3001ce18&req=diQlEc95mYZeX%2FMW3nq%2BgfQy9Wp6cCjxFhpKTPHG45L7vai6W6p8alZ%2FlRLt%0AtUJcO9vrEGKhOV2pnDGmio48Las%3D%0A)

Caso o prazo do período de expiração seja atingido, será necessário gerar um novo link de exportação. Em caso de expiração do link, o procedimento de renovação é simples. Basta gerar um novo link, definir seu prazo de expiração e seguir o procedimento de atualização no Power BI.

## 2. Atualização limitada de dados conforme frequência do plano

Após clicar em "Atualizar Dados" no Power BI, a atualização ocorrerá de acordo com a frequência permitida pelo plano, mesmo que a sessão no Ploomes seja encerrada. Isso significa que, após a integração, não é necessário repetir o processo de obtenção de dados da web. Cada plano possui uma capacidade de atualização específica para equilibrar a demanda de dados e a performance. Os dados serão atualizados conforme as limitações e recursos do plano escolhido.

Para atualizações mais frequentes, considere o plano de nível superior, o Plano Pro, que oferece uma capacidade de atualização robusta para atender às necessidades de análises dinâmicas.

## 3. Atualizações realizadas durante as exportações

Nosso sistema opera com uma atualização dinâmica, processando dados linha por linha. Ao exportar, é essencial considerar o seguinte cenário:

Imagine que você exporte uma planilha com 10.000 linhas. Durante esse processo, se você atualizar uma linha, por exemplo, a linha 2.000, essa atualização pode não ser refletida na versão exportada da planilha. Isso acontece porque a linha já foi processada durante o processo de exportação em andamento.

Para garantir a integridade dos dados exportados, recomendamos adotar as seguintes práticas:

1. Certifique-se de que todas as atualizações necessárias foram feitas antes de iniciar o processo de exportação.
2. Garanta que todos os dados que você deseja incluir na exportação estejam atualizados e precisos antes de iniciar a exportação.

Se eventualmente ocorrerem atualizações durante o processo de exportação, é importante notar que essas podem não ser refletidas no link gerado.

## 4. Atualizar colunas da aba integrada com o Power BI.

Para atualizar as colunas da aba integrada com o Power BI, é necessário seguir o passo a passo abaixo:

![Tela de computador com texto preto sobre fundo brancoDescrição gerada automaticamente](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2427676982/5301a0f451acdc69f00afa4bdb5e/dYmzaCkAQHXdaRQKxGm3mGGv2UMbfnwtRMj9t1vaEibHkGmxEPeSaBnn7kCKOxz9Ncv75jQmvj6xw1cHHleUXsbwTo40t7DRf6hyjnpjwRmZfV6V8jT8B7ILPdSSXyqAlquDB-JBx4swt7HUMvg8BQ?expires=1786536000&signature=4a7825cb367d80f75552c159f4e4a4920bfa2caa6f3a2d4352f236d4d13510a3&req=diQlEc95m4hXW%2FMW3nq%2BgWd25gQ3R5sj80caZao0CPmITymw473jrnl1O0hS%0AfGZIKfr%2BGL5heqA4xOCCLB3pk%2F4%3D%0A)

### No Ploomes:

1. Acesse a aba desejada.
2. Adicione ou remova as colunas necessárias.
3. Salve as alterações.
4. Aguarde a atualização do link exportado conforme a frequência configurada.

Para que seja refletido no Power BI, é necessário que a atualização das informações no link de exportação tenha sido concluída após a inclusão ou exclusão dessa nova coluna. A mesma irá ocorrer conforme definido ao configurar a integração. Lembrando que os limites são:

- Plano Free: 1 atualização a cada 8h.
- Plano Pro: 1 atualização a cada 1h.

### No Power BI:

1. Abra o relatório desejado.
2. Acesse: **Arquivo > Opções e Configurações > Opções**.
3. Clique em **Limpar Cache** para as três sessões:
   i. Opções de Gerenciamento de Cache de Dados.
   ii. Opções de Cache de P e R.
   iii. Opções do Cache de Artefatos Patrocinados.
4. Clique em **OK**
5. Vá em: **Transformar Dados > Transformar Dados**.
6. No painel **Etapas Aplicadas** do **Configurador de Consulta**, clique na engrenagem da etapa **Column1 Expandido**.
7. Selecione ou remova as colunas desejadas.
8. Clique em **OK** para confirmar.
9. Atualize os dados do relatório.
   Clique em Atualizar Dados no menu superior.
10. Aguarde o processo de atualização ser concluído.

Dessa forma, as novas colunas incluídas ou removidas no Ploomes serão refletidas no Power BI, garantindo que seus relatórios estejam atualizados.

⚠️ **Atenção**: sempre que houver uma alteração de adição ou remoção de colunas, este passo a passo deverá ser realizado novamente.

## 5. Combinar abas do Ploomes em uma única tabela no Power BI.

Há um limite para o tamanho máximo da aba que pode ser integrada com o Power BI por vez. Portanto, para abas muito extensas, você pode seguir estes passos:

- Dividir uma aba grande em abas menores no Ploomes.

- Exportar cada aba separadamente para o Power BI (uma por vez, repetindo o processo de obtenção de dados via web).

- Utilizar o editor de dados do Power BI para combinar as tabelas.

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 13: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1535812500/79b2e54870f9f88dd67017de7325/Integra%C3%A7%C3%A3o+-+Power+BI.png?expires=1786536000&signature=5daa285714381ecc0d076d6f84d8dbdbf5e767b79865ae6b2ea3cf1708f132ed&req=dSUkE8F%2Fn4RfWfMW3nq%2BgeuH9TBfJcPGmmZBTLPLwMD5KB8Jz2ZoZaiyGv%2Fe%0Af6QxgiLpFqCrLV459P4z77DxN8Q%3D%0A)](https://universidade.ploomes.com/courses/integracao-power-bi-2)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
