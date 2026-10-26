---
id: "360050373853"
titulo: "Controle de Portaria"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria"
trilha: "Manual do Produto > Suprimentos e Estoque > Armazéns Gerais"
atualizado_em: "2026-07-29T15:07:31Z"
rotulos: ["WMS", "Veículos", "Parceiro", "Contrato", "br.com.sankhya.armazem.controle.portarias", "portaria movimentação veículos", "Armazéns Gerais"]
---

# Controle de Portaria

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42313224344087) Módulo: Armazéns Gerais > Rotinas
```

---

Nessa tela, pode-se registrar as movimentações de entrada e saída dos veículos para o controle da fila e movimentações no armazém. Além disso, também é possível vincular esse registro à informação do [Contratos de Armazéns de Grãos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armazenagem) ao qual o veículo está relacionado.

| Funcionalidades da tela | |
| --- | --- |
| [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#painelprincipal) | [Aba Contratos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#abacontratos) |
| [Botão Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#bot%C3%A3ooutrasop%C3%A7%C3%B5es) |  |

### Painel Principal

![Imagem 2: Painel Principal](https://ajuda.sankhya.com.br/hc/article_attachments/20267952721303)

Uma **"Senha Portaria"** será gerada ao inserir um registro. Esta irá controlar a fila de veículos e poderá ser utilizada no [Laudo de Classificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595074) e na [Pesagem](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595054) para buscar as informações já registradas nessa etapa. 

A Senha Portaria tem sua numeração controlada por empresa e pode ser definida de forma manual ou automática através do botão ![Imagem 3: A Senha Portaria tem sua numeração controlada por empresa e pode ser definida de forma manual ou automática através do…](https://ajuda.sankhya.com.br/hc/article_attachments/16343162789143) **"Configuração da Tela"**, opção **"Numeração"**.

Indique no campo **"Tipo de Movimentação"** se a movimentação será de **"Carga"** ou **"Descarga"**.

No campo **"Modalidade de Contrato"** selecione o tipo do contrato por meio das opções **"Armazenagem"** ou **"Comercialização"**. 

**Nota:** assim como o seu filtro no Painel de Filtros, o campo acima será exibido apenas para clientes com acesso à licença do módulo **"30935 - Comercialização de Grãos"**.

Referente aos campos Tipo de Movimentação e Modalidade de Contrato, considere:

- Ao selecionar a opção Carga ou Descarga do campo Tipo de Movimentação, e a opção Armazenagem do campo Modalidade de Contrato do painel de Contratos dessa tela, apenas os Contratos de Armazéns de Grãos estarão disponíveis para seleção;
- Porém, se a opção Descarga junto à opção Comercialização dos respectivos campos ditos acima forem definidas, no painel de Contratos estarão disponíveis para seleção apenas os contratos de Comercialização do tipo **"Compra Fixada"** (campo **"Tipo de Contrato"**, tela [Contratos de Armazéns de Grãos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595254-Contratos-de-Armaz%C3%A9ns-de-Gr%C3%A3os));
- Caso seja definida as opções Carga e Comercialização, apenas os contratos de Comercialização do tipo Venda Fixada estarão disponíveis para seleção.

O campo **"Veículo"** deve ser preenchido com a informação do veículo da respectiva movimentação. O cadastro do veículo em questão deve ser feito na tela [Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533-Ve%C3%ADculos-). Ainda sobre esse campo:

- Caso o Veículo informado já possua uma movimentação registrada na Portaria, com o status diferente de **"Fechado"**, o sistema exibirá a seguinte mensagem:

**"Proibida a entrada de um veículo que já esteja com movimentação em andamento no armazém".**

- Se o Veículo informado possuir Motorista vinculado a ele em seu cadastro, essa informação será carregada automaticamente, porém, pode-se editá-la se necessário.

Preencha o campo **"Motorista"** com o motorista da respectiva movimentação. O registro dele deve ser realizado na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros).

A **"Dt. Chegada/hora"** é obrigatória na inserção do registro e será atribuída à informação da data e hora de chegada do veículo ao armazém.

Já a **"Dt. Entrada"**, deve ser preenchida com a data e hora de entrada do veículo nas dependências internas do armazém.

O campo **"Dt. Peso Bruto"** será preenchido com a informação da data e hora em que o peso bruto do veículo foi realizada.

**Nota:** para o tipo Carga, o peso bruto refere-se à Pesagem Final e para o tipo Descarga à Pesagem Inicial.

Referente ao campo **"Dt. Tara"** será destinado à informação da data e hora em que a pesagem da tara do veículo foi realizada, sendo que, para o tipo Carga, o peso bruto refere-se à Pesagem Inicial e para o tipo Descarga à Pesagem Final.

O campo **"Dt. Saída"** é destinado à informação da data e hora e saída do veículo do armazém.

Em **"Observação"**, é possível incluir qualquer informação que seja considerada relevante em relação à portaria para o registro.

O **"Status"** é um campo indicativo sobre a situação atual da movimentação do veículo no armazém. Nele, pode-se escolher uma das seguintes opções:

- **Aberto:** será a Data de Chegada registrada;
- **Aguardando Pesagem:** Data de Entrada registrada;
- **Pesagem Inicial Registrada:** Pesagem do Peso Bruto ou Tara registrados, a depender do tipo de movimentação;
- **Pesagem Final Registrada:** Pesagem do Peso Bruto ou Tara registrados, a depender do tipo de movimentação;
- **Fechado:** Data de Saída registrada;
- **Cancelado:** esse status é apontado quando for efetuado o cancelamento no botão [Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#bot%C3%A3ooutrasop%C3%A7%C3%B5es), opção **"Cancelar Controle de Portaria"**.

**Observação:** nessa tela, também será possível limitar o acesso dos usuários para que eles possam visualizar apenas os registros das empresas desejadas. Para essa ação, é necessário criar uma regra na tela [Central de Certificações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110053-Central-de-Certifica%C3%A7%C3%B5es) e, em seguida, vinculá-la no cadastro dos [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#top) desejados na aba [Validações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abavalidaes).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#top)

### Aba Contratos

![Imagem 4: Aba Contratos](https://ajuda.sankhya.com.br/hc/article_attachments/20291588574487)

Nessa aba, temos os campos:

O campo **"Contrato"** é destinado à informação do número do contrato de armazenagem ou de comercialização do parceiro, a definir conforme a seleção do campo Modalidade do Contrato no [Painel Principal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853#painelprincipal).

Em **"Parceiro"** será inserido o parceiro do contrato informado.

O campo **"Produto"** relaciona-se ao produto do contrato indicado.

Identifique no campo **"Procedência"** o terceiro responsável pela entrega do produto a favor de um respectivo contrato. Considere o seguinte exemplo:

A empresa X fecha uma compra de uma certa quantidade de grãos de um produtor e acerta para que ele entregue no Armazém. Ao chegar nele, a carga será aplicada no contrato da empresa X, mas com a informação de que foi o referido produtor que realizou a entrega.

Sendo assim, nesse campo, os Parceiros ativos para a busca deverão ser listados.

Informe ou pesquise no campo **"Nota Transporte"** a NF de transporte que já foi previamente lançada. Desse modo, ao informar o contrato na tela, a pesquisa do campo Nota Transporte será restringida apenas às NF's de Transporte confirmadas e pendentes no contrato.

O **"NF Produtor"** será destinado à informação do número da NF relacionada à movimentação.

No campo **"Peso NF"**, pode-se informar a quantidade de peso na NF relacionada à movimentação.

Pode-se preencher também no campo **"Vlr. Unitário"**, o valor unitário do produto da NF da movimentação.

O **"Vlr. Total"** deve ser preenchido com o valor total do produto da NF referente à movimentação.

O campo **"Chave NF-e"** é destinado para a informação da nota fiscal da movimentação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#top)

### Botão Outras Opções...

O botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15993414460439) **"Outras Opções..."** localizado na parte superior direita da tela, possui as seguintes opções:

#### Cancelar Controle de Portaria

Através dessa opção, cancele o registro inserido que por diversos motivos, possa não ter efetivado a carga ou descarga do produto no armazém, mantendo assim, o registro da presença do veículo na empresa.

![Imagem 6: Através dessa opção, cancele o registro inserido que por diversos motivos, possa não ter efetivado a carga ou descarga…](https://ajuda.sankhya.com.br/hc/article_attachments/20352244377239)

#### Cad. Simplif. Veículos 'CTRL + 1'

Por meio do botão Outras Opções... e utilizando a combinação de teclas "CTRL+1", o pop-up **"Cadastro Simplificado de Veículo"** será apresentado para o registro de veículos que ingressarão na portaria. Neste pop-up, encontra-se o botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/16027526118039) **"Ações"**, o qual permite a criação de ações na tela. Vale destacar que esse botão também está disponível na tela [Veículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111533).

![Imagem 8: Por meio do botão Outras Opções... e utilizando a combinação de teclas "CTRL+1", o pop-up "Cadastro Simplificado de…](https://ajuda.sankhya.com.br/hc/article_attachments/20352244390295)

**Nota:** quando há registros na tela Controle de Portaria é aberto o pop-up, o botão ![Imagem 9: Nota: quando há registros na tela Controle de Portaria é aberto o pop-up, o botão "Selecionar" fica disponível para…](https://ajuda.sankhya.com.br/hc/article_attachments/17886154154007) **"Selecionar"** fica disponível para inserir no campo Veículo o veículo exibido; por outro lado, quando não registros na tela, esse botão fica indisponível.

#### Cad. Simplif. Parceiro 'F2'

Ainda temos essa opção no botão Outras Opções... ou quando posicionamos o mouse em alguma parte dessa tela e utilizamos o botão **"F2"** do teclado. Assim, o pop-up **"Cadastro Simplificado de parceiros"** será exibido, possibilitando o cadastro dos parceiros que darão entrada na portaria. 

![Imagem 10: Ainda temos essa opção no botão Outras Opções... ou quando posicionamos o mouse em alguma parte dessa tela e utilizamos…](https://ajuda.sankhya.com.br/hc/article_attachments/20352244394903)

Ao inserir um novo parceiro **"Motorista"** na tela Controle de Portaria, o tipo Motorista já é marcado automaticamente no pop-up Cadastro Simplificado de parceiros.

**Nota:** ao abrir o pop-up, o botão **"Selecionar Parceiro"** não é exibido caso não haja nenhum registro selecionado. No entanto, quando há um registro selecionado, o mencionado botão torna-se visível.

#### Zerar numeração

Através dessa opção, pode-se reiniciar a numeração da Senha de Portaria por Empresa.

![Imagem 11: Através dessa opção, pode-se reiniciar a numeração da Senha de Portaria por Empresa .](https://ajuda.sankhya.com.br/hc/article_attachments/20352244404503)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360050373853-Controle-de-Portaria#top)
