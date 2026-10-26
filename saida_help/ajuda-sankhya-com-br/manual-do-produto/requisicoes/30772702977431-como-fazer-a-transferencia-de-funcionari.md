---
id: "30772702977431"
titulo: "Como fazer a transferência de funcionário entre empresas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30772702977431-Como-fazer-a-transfer%C3%AAncia-de-funcion%C3%A1rio-entre-empresas"
trilha: "Manual do Produto > Pessoas+ > Autoatendimento: Portal RH, App e Requisições > Requisições"
atualizado_em: "2026-10-15T13:08:44Z"
rotulos: ["Configuração", "Requisições", "Funcionários", "eSocial", "Central do eSocial", "Transferência de trabalhador", "FPCODFUNCTRANSF"]
---

# Como fazer a transferência de funcionário entre empresas

**Módulo:** Pessoas+
**Caminho de acesso:** Pessoal+> Rotinas Folha > RequisiçõesRequisições > Transferência
**ID da Tela:** br.com.sankhya.rh.Requisicoes

---

A **transferência de funcionário** permite movimentar um colaborador de uma empresa ou filial para outra, mantendo o vínculo de trabalho conforme o tipo de transferência realizada.

A solicitação é feita pela tela **Requisições** (Pessoal+> Rotinas Folha) e, depois de aprovada, os eventos correspondentes devem ser gerados e enviados para o **eSocial**, de acordo com a transferência realizada.

O processo pode ser utilizado, por exemplo, em movimentações entre empresas do mesmo grupo ou entre filiais.

### Antes de começar

Antes de solicitar a transferência, verifique:

- Você possui permissão para visualizar e transferir funcionários.

  Líderes visualizam seus liderados diretos e indiretos; o Departamento Pessoal visualiza os funcionários conforme suas permissões. Essas permissões são definidas no  [Painel de configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559).
- O funcionário é contratado pelo regime **CLT**. Para autônomos, é necessário desligar o profissional da empresa de origem e realizar uma nova contratação na empresa de destino.
- O funcionário não possui **folha calculada na referência da transferência**.
- O funcionário não está **em período de férias**.

### Solicitar uma transferência

[GIF animado: Imagem 1: Solicitar uma transferência](https://ajuda.sankhya.com.br/hc/article_attachments/30786970562711)

**1. Inicie a requisição**

1. Acesse a tela **Requisições** (Pessoal+> Rotinas Folha).
2. Selecione **Transferência**.
3. Clique em **Nova Transferência**.

**2. Informe os dados da transferência**

Preencha os campos obrigatórios:

- **Empresa de origem**: empresa em que o funcionário está atualmente.

  Neste campo só serão apresentadas para seleção as empresas que você tem a permissão concedida pelo [Painel de configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559);
- **Empresa de destino**: empresa para a qual o funcionário será transferido.
- **Departamento de destino**.
- **Referência**.
- **Motivo de desligamento eSocial**, quando aplicável.

Depois, defina se a transferência será:

- **Com ônus**: a empresa cedente continua arcando com os custos do funcionário.
- **Sem ônus**: os custos deixam de ser atribuídos à empresa cedente.

| **⚠️** **Atenção**  **A transferência pode ser feita antes do fechamento da folha**. Assim, o funcionário começa a trabalhar na nova empresa já no primeiro dia do mês, e todas as informações ficam corretas no sistema. **Se precisar desfazer a transferência**, o sistema permitirá selecionar empresas tanto da referência atual quanto das futuras. No entanto, a folha na empresa de origem, só poderá ser calculada para períodos anteriores à data da transferência. |
| --- |

**3. Selecione os funcionários**

Selecione o(s) funcionário(s) clicando em seu(s) respectivo(s) card(s). Vale ressaltar que, os funcionários serão visualizados da seguinte forma:

- líderes verão somente seus liderados diretos e indiretos;
- o DP verá todos os funcionários, conforme suas permissões.

![Imagem 2: o DP verá todos os funcionários, conforme suas permissões.](https://ajuda.sankhya.com.br/hc/article_attachments/43887216394519)

Para facilitar a seleção de funcionários, você pode utilizar os filtros disponíveis, como:

- **Situação Normal**;
- **Afastado**;
- **Liderado Imediato**.

Também é possível personalizar os filtros conforme a necessidade pela opção **Gerenciar Filtros**.

**4. Confirme a requisição**

Depois de preencher os dados e selecionar os funcionários, confirme a requisição.

A solicitação será encaminhada para aprovação do responsável, geralmente o **Departamento Pessoal**.

| ℹ️ **Nota**  Durante a aprovação da requisição, se o parâmetro **Ativa personalização do código do funcionário - FPCODFUNCTRANSF** estiver ligado:   - em uma transferência individual, o sistema apresenta um pop-up para informar o novo código do funcionário; - em transferências coletivas, o código é gerado automaticamente, independente do parâmetro.  ![Imagem 3: em transferências coletivas, o código é gerado automaticamente, independente do parâmetro.](https://ajuda.sankhya.com.br/hc/article_attachments/35364729358359) |
| --- |

#### Transferências entre diferentes tipos de empresa

O comportamento da transferência depende da relação entre a empresa de origem e a empresa de destino.

**🔹Entre empresas com matrizes (CNPJs) diferentes**

Realize a requisição normalmente, informando a empresa de origem, a empresa de destino e os demais dados obrigatórios.

Ao finalizar o processo de transferência, é necessário acessar a **Central do eSocial** e gerar e enviar os eventos de desligamento e admissão correspondentes ao eSocial; a empresa de origem envia o evento S-2299, informando a finalização do vínculo devido à transferência com a data último dia do mês anterior. A empresa de destino envia o evento S-2200, registrando a nova contratação no primeiro dia do mês da transferência.

**Exemplo:** para uma transferência com referência em **01/08**, o sistema gera o desligamento em **31/07** e a admissão em **01/08**.

| **⚠️** **Atenção**  Quando a empresa de origem estiver marcada como **Inapta por inexistência de fato** (aba [Informações gerais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas#abainforma%C3%A7%C3%B5esgerais) no cadastro da [empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas)), o motivo de desligamento eSocial **43 — Transferência de empregado** só pode ser utilizado quando as empresas pertencem ao mesmo grupo econômico e possuem CNPJs diferentes. Esse motivo não se aplica entre matriz e filial, que possuem a mesma raiz de CNPJ, nem quando a empresa de destino também estiver marcada como inapta. |
| --- |

**🔹Entre matriz e filial ou entre filiais**

Quando a transferência ocorre entre empresas com a **mesma raiz de CNPJ**, o campo **Motivo de desligamento eSocial** fica desabilitado automaticamente.

![Imagem 4: Quando a transferência ocorre entre empresas com a mesma raiz de CNPJ , o campo Motivo de desligamento eSocial fica…](https://ajuda.sankhya.com.br/hc/article_attachments/30944823525143)

Nesse caso, a transferência não gera desligamento e admissão no eSocial. É necessário enviar apenas o evento S-2206, informando a mudança de local de trabalho informando a data do primeiro dia do mês da transferência.

**🔹Para uma empresa que não está cadastrada no sistema**

Quando a empresa de destino ainda não está cadastrada:

1. Marque **Empresa não cadastrada no sistema**.
2. Informe o **CNPJ da empresa de destino**.
3. Selecione o(s) funcionário(s).
4. Confirme a requisição.

![Imagem 5: Confirme a requisição.](https://ajuda.sankhya.com.br/hc/article_attachments/30945038336535)

Ao finalizar o processo de transferência, deve-se enviar o evento S-2299 pela empresa de origem. Como a empresa de destino não está no sistema, não haverá conferência.

| **⚠️ Transferência de estagiários**  **Estagiários não podem ser transferidos entre empresas pelo sistema**, inclusive quando as empresas pertencem ao mesmo grupo econômico.  O estagiário é regido pela Lei nº 11.788/2008, a qual estabelece que o estágio não gera vínculo empregatício. A referida lei não contempla a possibilidade de transferência de estagiário entre empresas, ainda que façam parte do mesmo grupo econômico.  O contrato de estágio é formalizado entre a instituição de ensino e a empresa contratante. Por isso, quando houver mudança de empresa ou de CNPJ contratante, **é necessário encerrar o contrato de estágio atual e celebrar um novo Termo de Compromisso de Estágio**, conforme as condições estabelecidas entre as partes.  Dessa forma, a opção de **transferência não está disponível para estagiários**. |
| --- |

####

| 🚨 **Risco operacional**  O sistema não permite selecionar um funcionário que tenha **folha calculada na referência da transferência** ou que esteja **em férias**.  Quando a transferência precisa ser realizada mesmo nessas situações, existem duas alternativas:  **Opção 1: Transferir na referência atual**   1. Calcule normalmente a folha mensal da referência atual. 2. Efetue a transferência do funcionário. 3. Na empresa de destino, calcule as férias.   **Opção 2: Aguardar o retorno das férias**  Aguarde a referência seguinte, após o retorno do funcionário das férias, e então realize a transferência.  Esse comportamento também se aplica a situações de **incorporação, cisão ou fusão empresarial**. A trava ocorre por causa do cálculo existente na referência ou do período de férias, e não pelo motivo da transferência.  📚 Para situações de sucessão, incorporação, cisão ou fusão, consulte também o [**Cadastro de Tipos de Admissão**](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424857334551), que possui um tipo específico para esses casos. |
| --- |

### Desfazer transferência

[GIF animado: Imagem 6: Desfazer transferência](https://ajuda.sankhya.com.br/hc/article_attachments/31453089594007)

Se uma transferência foi realizada indevidamente, é possível desfazer a requisição.

1. Acesse a tela **Requisições** (Pessoal+> Rotinas Folha).
2. Selecione o card **Desfazer Transferência**.
3. Selecione a **Empresa**.
4. Selecione o(s) **Funcionário(s)**.
5. Clique em **Excluir requisição**.
6. Confirme a exclusão.

Para transferências realizadas para uma empresa não cadastrada, o sistema apresenta o card **Empresa não cadastrada** na referência atual ou futura. Por esse card, é possível selecionar a empresa e o funcionário para restaurar os dados na empresa de origem.

![Imagem 7: Para transferências realizadas para uma empresa não cadastrada, o sistema apresenta o card Empresa não cadastrada na…](https://ajuda.sankhya.com.br/hc/article_attachments/31452970386967)

| **⚠️** **Atenção**  Se o funcionário estiver afastado no momento em que a transferência for desfeita, a situação de afastamento permanece registrada na empresa de origem. |
| --- |

Após desfazer a transferência, a folha da empresa de origem só poderá ser calculada para períodos anteriores à data da transferência.

### Perguntas Frequentes

**1. Posso transferir qualquer funcionário?**

Não. A transferência é permitida para funcionários contratados pelo regime **CLT**.

Para autônomos, é necessário desligar o profissional da empresa de origem e realizar uma nova contratação na empresa de destino.

**2. Posso transferir um estagiário entre empresas?**

Não. O processo de transferência entre empresas não se aplica a estagiários.

Para mudar o estagiário de empresa, é necessário encerrar o Termo de Compromisso de Estágio atual e celebrar um novo.

**3. Quando posso solicitar uma transferência?**

A solicitação pode ser realizada a qualquer momento, mas o funcionário não pode estar em férias nem possuir folha calculada na referência da transferência.

A efetivação ocorre no primeiro dia do mês correspondente à transferência.

**4. Qual evento do eSocial é gerado na transferência?**

Depende do tipo de transferência:

- **CNPJs diferentes:** S-2299 na origem e S-2200 no destino.
- **Mesma raiz de CNPJ:** S-2206.
- **Empresa de destino não cadastrada:** S-2299 na origem.

**5. Como ficam as datas dos eventos do eSocial?**

Nas transferências entre CNPJs diferentes, o **S-2299** é gerado no último dia do mês anterior e o **S-2200** no primeiro dia do mês da transferência.

Nas transferências entre empresas com a mesma raiz de CNPJ, o **S-2206** é gerado no primeiro dia do mês da transferência.

**6. Fiz uma transferência por engano. Como desfazer?**

Acesse a tela **Requisições > Desfazer Transferência**, selecione a empresa e o funcionário e clique em **Excluir requisição**.

**7. A empresa de destino não está cadastrada. Posso fazer a transferência?**

Sim. Na nova transferência, marque **Empresa não cadastrada no sistema** e informe o CNPJ da empresa de destino.

**8. O que acontece se o funcionário estiver afastado ao desfazer a transferência?**

A situação de afastamento permanece registrada na empresa de origem.

### Artigos Relacionados

- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
- [Painel de Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559)
- [Cadastro de Tipos de Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424857334551)
- [Como cadastrar ocorrências com estabilidade?](https://ajuda.sankhya.com.br/hc/pt-br/articles/42546913948055)
