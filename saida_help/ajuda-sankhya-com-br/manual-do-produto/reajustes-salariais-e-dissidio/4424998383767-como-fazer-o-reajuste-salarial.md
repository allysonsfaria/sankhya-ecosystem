---
id: "4424998383767"
titulo: "Como fazer o reajuste salarial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4424998383767-Como-fazer-o-reajuste-salarial"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Reajustes Salariais e Dissídio"
atualizado_em: "2026-10-02T15:38:38Z"
rotulos: ["Configuração", "ID: br.com.sankhya.rh.ReajusteSalarial", "eSocial", "Folha de Pagamento", "Sindicato", "reajuste salarial", "reajuste sindical", "FPCODHISREA", "FPREAJANTECIPA", "FPHISTLOTACAO", "Configuração e Aplicação de Reajuste Salarial", "Pessoal+", "Convenção Coletiva", "FPUSASALATUREC"]
---

# Como fazer o reajuste salarial

```
 Módulo: Pessoal+ > Rotinas Folha              Versão disponível: A partir da 4.11
```

---

O reajuste salarial tem por objetivo adequar a remuneração dos funcionários para garantir o seu poder de compra, baseado na inflação anual e em outros fatores econômicos. Seu cálculo é realizado conforme a inflação do ano vigente, sendo geralmente concedido no período conhecido como data-base e, por isso, o mês em que passa a vigorar pode variar de acordo com a categoria. Vale ressaltar que essa negociação envolve a empresa, o sindicato da categoria e os próprios funcionários.

Por meio da tela **Reajuste salarial**, é possível programar diferentes tipos de reajuste, como aumento por promoção, mudança de cargo, equiparação e reajuste sindical, além de realizar o cancelamento de reajustes.

A rotina permite definir a **referência em que a alteração será aplicada**, evitando que um reajuste programado para uma competência futura seja considerado indevidamente no cálculo da folha atual.

| **⚠️** **Atenção**  Para programar um reajuste salarial que deverá entrar em vigor em uma **competência futura**, utilize a rotina **Reajuste salarial**.  A tela **Requisições** aplica as alterações diretamente no cadastro do colaborador. Por isso, uma alteração realizada nessa tela pode impactar o cálculo da **folha da competência atual**, mesmo que seja informada uma data de vigência futura.  Para que o reajuste seja considerado somente a partir da competência desejada, realize a programação pela rotina **Reajuste salarial**. O reajuste será considerado no cálculo da folha da referência informada na rotina. |
| --- |

![cancelar](https://ajuda.sankhya.com.br/hc/article_attachments/15298354397591)

## Lançar Reajuste

Para realizar o lançamento de um reajuste, clique no card **Lançar reajuste** e informe primeiramente, a **Empresa** e o **Mês referência** para qual será aplicado, em seguida, preencha as informações abaixo considerando o tipo de reajuste a ser concedido:

**Exemplo:** se o reajuste deverá entrar em vigor em **julho/2026**, informe **07/2026** como mês referência. Dessa forma, o reajuste será considerado no cálculo da folha de julho/2026.

![Imagem 2: Exemplo: se o reajuste deverá entrar em vigor em julho/2026 , informe 07/2026 como mês referência. Dessa forma, o…](https://ajuda.sankhya.com.br/hc/article_attachments/4425007156375)

**(1)** Na seção **"Realiza Reajuste Sindical?"**:

Quando não se tratar de Reajuste Sindical, selecione a opção **"Não"**.

Se optar por **"Sim"**, informe o **"Sindicato"** e sendo necessário, marque as opções **"Aplicar reajuste p/ demitidos entre data base e assinatura"** e **"Considera projeção do aviso prévio indenizado dentro do mês data base"** de acordo ao tipo de reajuste aplicado.

**Observação:** com a opção Considera projeção do aviso prévio indenizado dentro do mês data base marcada, ao clicar no botão **"Selecionar funcionários"**, além dos funcionários ativos, serão apresentados também os demitidos na referência anterior e que possuem dias de aviso prévio indenizado projetados dentro do mês data base.

Ao aplicar um Reajuste Sindical com uma sequência múltipla de CCT ou um reajuste parcelado, sendo parte em uma referência e o restante em outra distinta, serão consideradas as seguintes regras:

**1 -** Quando aplicar o primeiro reajuste e selecionar a próxima sequência e/ou o próximo ano, o sistema irá validar se o reajuste anterior foi realizado para todos os funcionários selecionados e efetuar o próximo. Caso contrário, será exibida uma mensagem de alerta informando que existem funcionários que não possuem o reajuste anterior aplicado e questionando se deseja continuar.

Se marcar a opção **"Não"**, a operação será cancelada. Todavia, escolhendo **"Sim"**, o reajuste será aplicado e o anterior não poderá ser realizado posteriormente.

**2 -** Caso tente calcular uma sequência/parcela anterior para um funcionário que já tenha um reajuste posterior efetivado, será apresentada uma mensagem informando que o funcionário em questão já possui um reajuste aplicado e que para realizar essa operação será necessário cancelar o reajuste posterior.

**(1)** Nas seções **"Tipo de Arredondamento (mensalistas)"** e **"Tipo de Arredondamento (não  mensalistas)"**:

Marque a opção que atenda ao valor do arredondamento, conforme abaixo:

- Nenhum
- Para cima
- Para baixo

**(1)** Em **"Outros valores"**:

Aqui você informará a **"Porcentagem"** ou o **"Valor final"** para o reajuste.

Ao efetuar a marcação **"Readequar o salário dos colaboradores admitidos após data base ao piso do sindicato?"** serão apresentados somente os funcionários que foram admitidos após a data base. Além disso, o sistema verificará se o valor do salário destes funcionários está menor que o salário mínimo da classe que foi passado e, em caso positivo, readequará o valor desses salários.

**Nota:** não havendo Reajuste Sindical, será possível realizar nesta seção o reajuste salarial **"Por valor"**. Assim, informe o **"Valor do aumento?"** no mês antecedente a referência em que o reajuste será aplicado.

Caso seja realizado o reajuste sindical com readequação de salário de colaboradores admitidos até a data base, deve-se preencher o campo **"Qual salário mínimo da classe?"** com o valor do reajuste desejado, sendo este maior que o salário atual do funcionário.

![Imagem 3: Informações adicionais:](https://ajuda.sankhya.com.br/hc/article_attachments/16533206982551) **Informações adicionais:**

- Para aplicar o percentual de um Reajuste Sindical utilizando o método cumulativo ou não cumulativo, considere o salário base da referência indicada no campo **"Ref. Salário Base"** da tela [Sindicato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953), aba Convenção coletiva, Acordo coletivo ou Sentença Normativa.

**Observação:** para que o sistema possa calcular o reajuste salarial de todos os funcionários admitidos após a data base, é necessário que o campo Ref. Salario Base seja informado com o mês anterior a assinatura da convenção. Por exemplo, se a assinatura for na data 10/2023, o campo Ref. Salario Base deve ser preenchido com a data 09/2023.

- Quando estiver definido um teto máximo para aplicação do percentual de Reajuste Sindical ou um valor específico para os casos acima do teto na Convenção Coletiva de Trabalho, estes valores deverão ser informados nos campos **"Valor limite do teto"** e **"Valor aplicado a partir do limite do teto"** da tela [Sindicato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953), aba Convenção coletiva, Acordo coletivo ou Sentença Normativa.

**(1)** Na seção **"Informações sobre a Ocorrência"**:

Nesta seção serão apresentadas a **"Descrição"** e o **"Código"** do tipo de reajuste que será exibido no cálculo do funcionário.

Após o preenchimento de todas as informações, o botão Selecionar funcionários será habilitado para escolha e confirmação da aplicação do reajuste aos mesmos.

**Observação:** ao confirmar o reajuste dos funcionários, se a marcação **"Ocorrência de reajuste salarial sindical"** da tela [Ocorrências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610494) estiver habilitada e estes funcionários estiverem com situação do eSocial igual a S2205/S2206, será exibido o pop-up **"Registro S-2206 eSocial"** no qual você deverá informar a **"Data Alteração"** para que o evento S-2206 seja enviado ao eSocial com a data da alteração salarial.

[GIF animado: Imagem 4: Observação: ao confirmar o reajuste dos funcionários, se a marcação "Ocorrência de reajuste salarial sindical" da tela…](https://ajuda.sankhya.com.br/hc/article_attachments/6442317419415)

Confirmada a Data Alteração neste pop-up, você poderá visualizá-la no **"Registro de envio para o e-Social"** localizado no painel lateral esquerdo do cadastro de [Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610454).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424998383767-Como-fazer-o-reajuste-salarial#top)

---

## Cancelar Reajuste

Caso seja necessário cancelar um reajuste aplicado, clique na opção **"Cancelar Reajuste"** e preencha as informações solicitadas no pop-up:

![popup](https://ajuda.sankhya.com.br/hc/article_attachments/15298525726231)

Selecione a **"Empresa"** e a **"Referência do reajuste"** aplicado. Em seguida, se houve **"Reajuste Sindical?"**, marque a opção **"Sim"** e indique qual é o **"Sindicato"**, não havendo, basta escolher a opção **"Não"** e **"Selecionar os funcionários"** que terão seus reajustes cancelados. Depois é só confirmar a operação.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424998383767-Como-fazer-o-reajuste-salarial#top)

## Parâmetros que influenciam nesta rotina

**Cód. Hist. Ocorr. para Reajuste de Salário - FPCODHISREA:** este parâmetro contém a lista de códigos de ocorrências que podem ser utilizados no registro da ocorrência de uma alteração de salário.

**Cód. Hist. Ocorr. p/ Mudança de Cargo (LOTACAO) - FPHISTLOTACAO:** este parâmetro permite definir o código do histórico de ocorrências utilizado para registrar mudanças de cargo (lotação) de funcionários. Esse código deve ser diferente do código informado no parâmetro FPCODHISREA.

**Cód.Hist.Ocor. p/ Antecipação de Reajuste Sindical - FPREAJANTECIPA:** este parâmetro possui o código de ocorrência utilizado para registro quando há uma antecipação do reajuste sindical, antes de sair a convenção coletiva oficial.

**Utiliza salário atual para recálculo do dissídio - FPUSASALATUREC**: define qual salário será considerado pelo sistema durante o recálculo de dissídio.

Quando habilitado, o sistema utiliza o salário atual do colaborador, já reajustado pela Convenção Coletiva de Trabalho (CCT), para recalcular os valores envolvidos no dissídio. Em seguida, compara esse resultado com o cálculo realizado utilizando o salário registrado no histórico da referência de origem, apurando corretamente a diferença devida.

Por padrão, o parâmetro é disponibilizado **desligado**, o sistema utiliza o salário registrado na referência original para realizar os cálculos relacionados ao dissídio.

A habilitação deste parâmetro é recomendada em situações nas quais houve alteração salarial entre a data-base da convenção e a efetiva assinatura ou aplicação do dissídio.

Nesses cenários, utilizar apenas o salário histórico pode gerar divergências nos valores das diferenças apuradas, especialmente quando existem reajustes salariais ocorridos após a competência original.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424998383767-Como-fazer-o-reajuste-salarial#top)
