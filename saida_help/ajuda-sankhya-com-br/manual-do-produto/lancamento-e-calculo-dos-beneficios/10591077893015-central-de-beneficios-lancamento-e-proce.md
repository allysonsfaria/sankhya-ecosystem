---
id: "10591077893015"
titulo: "Central de Benefícios+: lançamento e processamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento"
trilha: "Manual do Produto > Pessoas+ > Benefícios > Lançamento e Cálculo dos Benefícios"
atualizado_em: "2026-10-15T15:57:36Z"
rotulos: ["Rotinas", "Financeiro", "Pessoal", "Folha de Pagamento", "Central de Benefícios +", "br.com.sankhya.rh.CentralBeneficios", "FPATUMOVBEN", "Lançamento de benefícios", "Processamento e integração", "Vinculação de beneficiários", "Benefícios"]
---

# Central de Benefícios+: lançamento e processamento

```
 Módulo: Pessoal + > Rotinas Folha
```

---

### Antes de começar

Antes de usar a **Central de Benefícios+** pela primeira vez, confira se as configurações abaixo estão feitas. Sem elas, a tela pode não abrir ou os colaboradores podem não aparecer para vínculo ao cálculo.

**Acesso do usuário**

- **Acesso à tela:** a tela **Central de Benefícios+** precisa estar liberada para o usuário na tela **Acessos** (Configurações > Controle de Acesso). Essa liberação é feita pelo administrador do sistema.
- **Usuário do Departamento Pessoal:** o usuário precisa estar marcado como **Pertence ao DP/RH** na tela **Configuração Funcionários** (Pessoal+ > Cadastros), aba **Configurações**.
- **Grupo de Decisores e permissões:** o usuário precisa fazer parte de um **Grupo de Decisores** e ter as permissões configuradas no **Painel de Configurações** (Pessoal+ > Configurações).

📚 Para saber mais, acesse: [Como liberar o acesso às telas do Pessoas+ para novos colaboradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/38583858942743).

**Cadastros dos benefícios**

- **Tipo de Benefício:** os tipos de benefício (vale-alimentação, vale-refeição, vale-transporte, plano de saúde etc.) precisam estar cadastrados na tela **Tipo de Benefício** (Pessoal+ > Cadastros).
  📚 Configure isso em: [Como cadastrar Tipos de Benefício](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405110225175).
- **Benefícios+:** cada benefício precisa estar cadastrado na tela **Benefícios+** (Pessoal+ > Cadastros), com as fórmulas de cálculo, os eventos da folha e os colaboradores vinculados.
  📚 Configure isso em: [Benefícios+: cadastro de benefícios e fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943).

**Cadastro dos colaboradores**

- **Dados do colaborador:** os colaboradores que receberão o benefício precisam estar com os dados obrigatórios preenchidos no cadastro, na tela **Configuração Funcionários** (Pessoal+ > Cadastros).

| **⚠️** **Atenção**  No **Cadastro inicial** do cálculo, confira se as datas de início e de fim da **Referência de Apuração dos Benefícios** e da **Referência de Apuração de Faltas, Atestados e Afastamentos** estão preenchidas. Sem essas datas, o sistema não exibe erro, mas os colaboradores não aparecem ao clicar em **Vincular**.  📚 Para saber mais, acesse: [Não é possível vincular funcionários ao benefício na tela Central de Benefícios, veja o que fazer](https://ajuda.sankhya.com.br/hc/pt-br/articles/31030254851735). |
| --- |

### Jornada de uso

Por meio desta tela realiza-se a rotina mensal do lançamento de benefícios cadastrados anteriormente na tela [Benefícios+](https://ajuda.sankhya.com.br/hc/pt-br/articles/4570924321943).

![Imagem 1: Por meio desta tela realiza-se a rotina mensal do lançamento de benefícios cadastrados anteriormente na tela…](https://ajuda.sankhya.com.br/hc/article_attachments/17688582583959)

![Imagem 2: Ao acessar essa tela, verifique qual é a "Referência" indicada. Caso seja necessária a alteração, clique no calendário…](https://ajuda.sankhya.com.br/hc/article_attachments/16538533774103) Ao acessar essa tela, verifique qual é a **"Referência"** indicada. Caso seja necessária a alteração, clique no calendário ao lado da data.

Acesse os links abaixo para facilitar sua navegação nas funcionalidades desta tela:

| Funcionalidades da tela | |
| --- | --- |
| [Cadastro inicial](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Cadastroinicial) | [Vincular Beneficiários ao cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#VincularBenefici%C3%A1riosaoc%C3%A1lculo) |
| [Lançar evento](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Lan%C3%A7arevento) | [Processar/Simular eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Processar/Simulareventos) |
| [Lançar movimentos na folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Lan%C3%A7armovimentosnafolha) | [Exclusão de movimento na folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Exclus%C3%A3odemovimentonafolha) |
| [Integração financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Integra%C3%A7%C3%A3ofinanceira) | [Executando a rotina de modo coletivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#Executandoarotinademodocoletivo) |

---

## Cadastro inicial

O cadastro das informações iniciais é feito de forma individual através do botão ![Imagem 3: O cadastro das informações iniciais é feito de forma individual através do botão "Novo cálculo" .](https://ajuda.sankhya.com.br/hc/article_attachments/17688709262359) **"Novo cálculo"**.

![Imagem 4: O cadastro das informações iniciais é feito de forma individual através do botão "Novo cálculo" .](https://ajuda.sankhya.com.br/hc/article_attachments/17688896510615)

Preencha o nome do benefício no campo **"Descrição"**, selecione o **"Código"** do benefício e informe o **"Número da Nota"**, que geralmente será o número da nota fiscal entregue pelo fornecedor do benefício. Preencha também o **"Valor da Nota"**.

A referência apresentada será a mesma definida anteriormente, porém o campo **"Referência"** estará disponível para que ela possa ser alterada.

Indique a **"Data de Vencimento"** da nota.

As seções **"Referência de Apuração dos Benefícios"** e **"Referência de Apuração de Faltas, Atestados e Afastamentos"** serão preenchidas automaticamente e apresentarão a **"Data de Início da Referência"** e a **"Data de Fim da Referência"** conforme a Referência escolhida. 

Efetue a marcação **"Fragmenta referência em período"** quando o benefício for calculado em fragmentação.  Nesse caso, defina o período fragmentado correspondente à compra do benefício.

Clique no botão ![Imagem 5: Clique no botão "Confirmar alterações" para salvar o cadastro e confirmar o novo cálculo.](https://ajuda.sankhya.com.br/hc/article_attachments/17705320809751) **"Confirmar alterações"** para salvar o cadastro e confirmar o novo cálculo.

Logo após, são exibidos os botões **"Duplicar"** e**"Excluir"**, sendo que, quando for realizada a duplicação do registro, será apresentado um pop-up para alteração dos campos Referência e Data Vencimento. 

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

|  | Vincular Beneficiários ao cálculo |
| --- | --- |

O próximo passo será vincular os beneficiários ao cálculo do benefício, para isso; clique no botão Vincular.

Assim, será apresentado um pop-up para confirmar se deseja vincular todos os beneficiários. Clique em **"SIM"**.

Para visualizar os funcionários incluídos, clique no botão **"Beneficiários"** ao lado esquerdo da tela.

[GIF animado: Imagem 6: Para visualizar os funcionários incluídos, clique no botão "Beneficiários" ao lado esquerdo da tela.](https://ajuda.sankhya.com.br/hc/article_attachments/17708283245591)

#### Vincular novos beneficiários

Se for necessária a inclusão de outros beneficiários em uma referência específica para aquele cálculo, clique em **"Incluir beneficiários"**.

![Imagem 7: Se for necessária a inclusão de outros beneficiários em uma referência específica para aquele cálculo, clique em…](https://ajuda.sankhya.com.br/hc/article_attachments/17708357401239)

Selecione os funcionários que deseja incluir e, em seguida, salve a inclusão clicando em ![Imagem 8: Selecione os funcionários que deseja incluir e, em seguida, salve a inclusão clicando em "Incluir beneficiários" .](https://ajuda.sankhya.com.br/hc/article_attachments/17705320809751) **"Incluir beneficiários"**.

As **"Informações do beneficiário"** poderão ser visualizadas ao clicar sobre o seu card. 

[GIF animado: Imagem 9: As "Informações do beneficiário" poderão ser visualizadas ao clicar sobre o seu card.](https://ajuda.sankhya.com.br/hc/article_attachments/17708457167127)

#### Excluir beneficiários

Caso queira excluir algum beneficiário do cálculo, clique em **"Ativa Seleção"**, no alto da tela à direita. Em seguida, selecione o funcionário e clique no botão **"Remover beneficiários"** e confirme a exclusão.

![Imagem 10: Caso queira excluir algum beneficiário do cálculo, clique em "Ativa Seleção" , no alto da tela à direita. Em seguida,…](https://ajuda.sankhya.com.br/hc/article_attachments/17710063808791)

| ℹ️ **Funcionários desligados e transferidos**  Colaboradores desligados ou transferidos que continuam vinculados a um benefício são apresentados normalmente na **Central de Benefícios+**, junto com os demais colaboradores elegíveis. Assim, você consegue:   - conferir o vínculo desses colaboradores ao processar o benefício da competência; - incluir manualmente um colaborador desligado ou transferido que ainda deva ter o benefício calculado (por exemplo, quando o desligamento ocorreu depois do fechamento da competência anterior); - remover o vínculo quando o benefício não fizer mais sentido para aquele colaborador.   A decisão de manter, incluir ou remover esses vínculos fica a critério do Departamento Pessoal, conforme a regra de cada benefício. |
| --- |

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

| Imagem 11: (voltar ao topo) | Lançar evento |
| --- | --- |

Em alguns casos, pode haver a necessidade de inclusão de valores extras que vieram na fatura do benefício, por exemplo, uma segunda via de carteirinha.
Para isso, tem-se o botão Lançar evento que será exibido quando o botão Ativa Seleção estiver habilitado.
Após acioná-lo, selecione o funcionário desejado e informe o valor dos custos extras, correspondente a cada funcionário. 

[GIF animado: Imagem 12: Em alguns casos, pode haver a necessidade de inclusão de valores extras que vieram na fatura do benefício, por exemplo,…](https://ajuda.sankhya.com.br/hc/article_attachments/17710762793495)

Caso tenha que inserir um mesmo valor para vários funcionários, clique no botão **"Lançar valor único"**. Selecione as opções desejadas, se será para **"Titulares"** e/ou **"Dependentes"**, se deve **"Substituir valores diferentes de zero"** e informe o **"Valor"**. Em seguida, confirme.

![Imagem 13: Caso tenha que inserir um mesmo valor para vários funcionários, clique no botão "Lançar valor único" . Selecione as…](https://ajuda.sankhya.com.br/hc/article_attachments/17714167121815)

Quando os valores estiverem preenchidos, para ser realizado o desconto na folha do funcionário, basta clicar no botão **"Escolher eventos"**. Desse modo, o pop-up **"Lançar Eventos"** será apresentado, nele selecione o **"Evento Titulares"** ou o **"Evento Dependentes"**. É importante ressaltar que no evento que não for selecionado deverá ser incluído o código **"0"** para que o botão **"Confirmar"** fique disponível.

Logo após, confirme o lançamento do evento para os beneficiários.

![Imagem 14: Logo após, confirme o lançamento do evento para os beneficiários.](https://ajuda.sankhya.com.br/hc/article_attachments/17714325676823)

**Nota:** os benefícios não podem ser lançados com os mesmos eventos para um mesmo funcionário.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

| Imagem 15: (voltar ao topo) | Processar/Simular eventos |
| --- | --- |

Após a determinação dos eventos deve-se calcular o benefício para que os valores do beneficiário e da empresa sejam preenchidos. Esta rotina é realizada por meio do botão Processar/Simular, em que, todos os beneficiários terão seus valores calculados, não só os que foram vinculados (beneficiários adicionados de maneira avulsa também terão o cálculo realizado). Para isso, retorne ao cálculo clicando no botão **"Configurações Gerais"**.

![Imagem 16: Após a determinação dos eventos deve-se calcular o benefício para que os valores do beneficiário e da empresa sejam…](https://ajuda.sankhya.com.br/hc/article_attachments/17715261388695)

Em seguida, clique no botão Processar/Simular e confirme no pop-up. Verifique se os valores foram recalculados.

![Imagem 17: Em seguida, clique no botão Processar/Simular e confirme no pop-up. Verifique se os valores foram recalculados.](https://ajuda.sankhya.com.br/hc/article_attachments/17715426240535)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

| ![Imagem 18: (voltar ao topo)](https://ajuda.sankhya.com.br/hc/article_attachments/42315085773079) | Lançar movimentos na folha |
| --- | --- |

Após o cálculo é preciso lançar movimentos na folha. Para realizar esta rotina, basta clicar no botão Lançar movimentos na folha, feito isso, os valores serão lançados da seguinte forma:

- O valor do beneficiário será lançado com o código do evento preenchido no cadastro do benefício como **"Evento Beneficiário"**;
- Já o valor da empresa será lançado com o código do evento preenchido no cadastro do benefício como **"Evento Empresa"**.

Se houver valores extras para o beneficiário, pode ocorrer duas situações:

1. Se o valor extra e o código de evento estiverem preenchidos, esse valor extra será lançado com o código de evento preenchido na configuração do cálculo do evento, ou seja, um terceiro movimento.
2. Se o valor extra estiver preenchido, porém, sem o evento, o valor extra do beneficiário será acumulado ao valor do beneficiário e será lançado com o código do evento preenchido no cadastro do benefício. Já se tiver valor extra para a empresa, ele sempre será acumulado ao valor empresa e lançado com o código do evento do cadastro do benefício.

Ao clicar no botão Lançar movimentos na folha, será apresentado o pop-up com as opções de lançamento de movimento.

![Imagem 19: Ao clicar no botão Lançar movimentos na folha , será apresentado o pop-up com as opções de lançamento de movimento.](https://ajuda.sankhya.com.br/hc/article_attachments/17715818780951)

Defina se será incrementada uma nova sequência para o desconto na folha ou se um movimento que já existe será atualizado. Em seguida, confirme.

**Observação:** quando o parâmetro **"Calcula mov mensal lançado por benefício em férias - FPATUMOVBEN"** estiver ligado, será verificado na ocasião do cálculo de férias se existe algum evento lançado pelo módulo de benefícios tornando-o movimento de férias. Se por algum motivo o cálculo de férias do funcionário for realizado, mas não for salvo, na ocasião do cálculo mensal o sistema verifica a existência de movimentos lançados pelo módulo benefícios e confere com a existência de folha de férias.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

| Imagem 20: (voltar ao topo) | Exclusão de movimento na folha |
| --- | --- |

Se houver a necessidade de refazer o processo, por algum erro após o lançamento do movimento, clique em **"Remover movimentos da folha"** e confirme no pop-up.

![Imagem 21: Se houver a necessidade de refazer o processo, por algum erro após o lançamento do movimento, clique em "Remover…](https://ajuda.sankhya.com.br/hc/article_attachments/17716315044119)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

|  | Integração financeira |
| --- | --- |

Após o benefício ser calculado e pronto para lançamento ao financeiro, clique no botão **"Integrar ao financeiro"**. Preencha o formulário do pop-up com as datas e clique em **"Confirma Integração"**.

Ao efetuar a marcação **"Gerar lançamento único no Financeiro"**, a folha será integrada em um lançamento único e o histórico será o nome do benefício seguido pela referência.

Com a marcação **"Usar parceiro dos Funcionários"** ativada, a folha será integrada por parceiros cadastrados nos funcionários e empresas, e o histórico será o nome do benefício seguido pela referência e nome do funcionário.

![Imagem 22: Com a marcação "Usar parceiro dos Funcionários" ativada, a folha será integrada por parceiros cadastrados nos…](https://ajuda.sankhya.com.br/hc/article_attachments/17717065076759)

Por meio do botão **Desfazer integração financeira** é possível reverter o status de um cálculo concluído, ou seja, de um cálculo que já realizou a integração ao financeiro.

| **⚠️** **Atenção**  O botão **Desfazer integração financeira** altera **somente o status do cálculo** na Central de Benefícios+. Os lançamentos já gerados na **Movimentação Financeira não são excluídos nem estornados automaticamente**. |
| --- |

Caso seja necessário refazer a integração, **estorne ou exclua manualmente o lançamento financeiro na Movimentação Financeira antes de desfazer a integração na Central de Benefícios**. Essa ordem é necessária para evitar a duplicidade do lançamento financeiro.

Após o estorno ou a exclusão do lançamento na **Movimentação Financeira**, utilize o botão **Desfazer integração financeira** para alterar o status do cálculo e permitir que o processo seja realizado novamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)

### Executando a rotina de modo coletivo

Nessa tela também é possível fazer a gestão dos benefícios de forma coletiva, para isso clique em Ativa Seleção. Selecione os benefícios e, em seguida, clique no botão desejado para executar a operação.

[GIF animado: Imagem 23: Nessa tela também é possível fazer a gestão dos benefícios de forma coletiva, para isso clique em Ativa Seleção .…](https://ajuda.sankhya.com.br/hc/article_attachments/17687951406743)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/10591077893015-Central-de-Benef%C3%ADcios-lan%C3%A7amento-e-processamento#top)
