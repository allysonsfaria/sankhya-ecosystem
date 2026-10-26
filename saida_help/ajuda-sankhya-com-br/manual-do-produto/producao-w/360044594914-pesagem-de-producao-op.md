---
id: "360044594914"
titulo: "Pesagem de Produção (OP)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594914-Pesagem-de-Produ%C3%A7%C3%A3o-OP"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:50:54Z"
rotulos: ["AJUDA DO SKW", "manual", "br.com.sankhya.prod.pesagemproducaoop", "Pesagem de Produção (OP) manual", "Configuração", "Produção", "Balança", "Configuração da balança", "Pesagem por OP", "Peso bruto e líquido", "Pesagem", "Etiqueta"]
---

# Pesagem de Produção (OP)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312657020055) Módulo: Produção > Rotinas
```

---

Esta tela pesará o resultado de uma produção a partir do Número da OP.

![Imagem 2: Esta tela pesará o resultado de uma produção a partir do Número da OP .](https://ajuda.sankhya.com.br/hc/article_attachments/6922506930583)

Para determinar se uma atividade terá apontamento de pesagem, é necessário que a atividade em questão tenha uma configuração pré-definida na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo), aba [Apontamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo#abaapontamento) no campo **"Tipo de Apontamento"**, a opção **"Pesagem de Volumes"** deverá ser marcada.

**Observação:** não é possível configurar mais de uma atividade com o Tipo de Apontamento igual à Pesagem de Volumes.

**Nota:** somente pessoas configuradas, considerando a regra de candidatos executantes, poderão executar a atividade Pesar Produto. Caso uma pessoa não configurada para tal atividade tentar executá-la, o sistema mostrará a seguinte mensagem:

**"Executante não tem permissão para acessar OP/Atividade [PESAR PRODUTO]."**

Se dois usuários realizarem a aceitação de uma mesma OP e efetuarem o apontamento desta nas telas Pesagem de Produção (OP) e/ou [Pesagem de Produção (ID Volume)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594774), o sistema irá alertar ambos sobre a edição por meio da mensagem:

**"Existem outros usuários editando os apontamentos dessa OP. Deseja atualizar a grade para confirmar o apontamento?"**

O visor ![leitura](https://ajuda.sankhya.com.br/hc/article_attachments/15534392563735) permite que você visualize de forma online se a balança já está estável para que seja feita a coleta de dados. Para isso, configure a **"Busca de peso"** para **"Ao Solicitar"**.

**Observação:**o visor não atuará em casos de configuração de múltiplas balanças.

Por meio do botão **"Configurações"**, você definirá como o sistema deve obter o peso da balança:

![Imagem 4: Por meio do botão " Configurações" , você definirá como o sistema deve obter o peso da balança:](https://ajuda.sankhya.com.br/hc/article_attachments/6922498188183)

Neste pop-up, temos o campo **"Busca de Peso"** para selecionar entre duas opções:

- Por meio da opção **"Constante"**, após a seleção de uma OP/Atividade, o sistema abrirá a comunicação com a balança e irá aguardar o envio de peso da mesma.
- Na opção **"Ao Solicitar"** O sistema aguardará o usuário clicar no botão **"Pesar"** para buscar o peso da balança.

**Observação:** para esta configuração, a balança deve estar configurada para o envio de peso constante.

Além disso, temos a marcação **"Confirma apontamento automático"** que, ao ser acionada, fará com que o sistema tente fazer a confirmação automática das pesagens pendentes, no momento em que você selecionar uma nova OP para realizar pesagem.

Em relação ao botão **"[F8] Nova OP"**, localizado na parte inferior esquerda da tela, este irá limpar a seleção de OP e permitirá a digitação de um novo Nro de OP levando o foco no campo.

O botão **"[F6] Capturar Peso"** será exibido conforme a configuração do campo Busca de Peso, ou seja, se a opção Constante estiver selecionada, a opção será substituída pelo texto **"Aguardando Peso ..."**; caso a opção Ao Solicitar for escolhida, o botão [F6] Capturar Peso será habilitado.

Por meio do botão **"[F2] Reimprimir"**, você poderá reimprimir as etiquetas de volume já pesadas, sendo assim, podemos inserir a **"ID inicial"** e **"ID final"** que serão reimpressos de acordo com o intervalo definido.

No botão **"[F9] Excluir"**, serão excluídos os volumes selecionados na grade, com a possibilidade da seleção de um ou mais volumes.

**Nota:** ao excluir um apontamento que tenha associação ao **"Apontamento de Volumes - TPRAVO"**, será apresentado um pop-up de confirmação antes da execução da ação.

O botão **"[F7] Confirmar"** irá confirmar a pesagem de volumes; a confirmação desta irá inserir e confirmar um apontamento para a OP/Atividade/Produto considerando o somatório de todas as pesagem pendentes até o momento.

No rodapé da tela, ao lado da aba **"Totais"**, temos a aba **"Informações adicionais"** que será exibida caso você opte por incluir campos adicionais na tabela TPRAVO.

**Observação:** os parâmetros de campos da tabela TPRAVO estão disponíveis para a criação do modelo de etiqueta, são eles:

- ID;
- IDIPROC;
- CODPROD;
- DESCRPROD;
- CONTROLE;
- NROLOTE;
- PESOBRUTO
- PESOLIQ;
- TIPO.

**Nota:** o sistema utilizará as configurações nos campos **"Modelo de etiqueta"** da tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) (sub-aba Pesagem), campo **"Modelo de etiqueta"** (tela Empresa, aba Manufatura) e o parâmetro **"Modelo de etiqueta pesagem - MODETIPES"** que irá definir o modelo da etiqueta. O sistema respeita a hierarquia descrita anteriormente para definir qual o modelo de etiqueta será utilizado na impressão:

- **1º Produto -** Se o produto possui modelo de etiqueta, então utiliza o modelo do produto para impressão.
- **2º Empresa -** Se o produto não possui modelo de etiqueta, mas a empresa da planta da ordem possui modelo de etiqueta, então utiliza o modelo da empresa para a impressão.
- **3º Parâmetro -** Se o produto e a empresa da planta da ordem não possuem modelo de etiqueta, mas o parâmetro possui um modelo de etiqueta especificado, então utiliza o modelo do parâmetro para a impressão.

Temos ainda, a chamada de retorno do peso bruto e líquido que referem-se aos pesos brutos e totais do produto, ou seja, considera-se o peso das embalagens a serem utilizadas neste.

Considere o exemplo:

O produto Tecido será armazenado em rolos, portanto na embalagem será considerado o rolo interno (denomina-se tarugo), que possui um peso próprio e este possui ainda o plástico em que é embalado o tecido e o tarugo, que também possui um peso, tem-se então a soma total do peso dos componentes do produto Tecido, em que dispõe o Tarugo + Tecido + Embalagem. Logo, o peso bruto será o peso destes componentes enquanto que o peso líquido será somente o peso do produto em si.

Contudo, para a gestão de estoque da empresa é preciso considerar o peso líquido, pois apenas o Tecido é ponderado na venda, mas para os processos de entrega e geração da nota fiscal do produto é preciso realizar a cotação dada a importância do peso total do item, pois o produto será transportado como um todo.

Deste modo, temos a chamada de retorno do peso bruto e líquido conforme a balança. Os parâmetros de entrada deste são:

- CODPROD NUMBER;
- CONTROLE VARCHAR2;
- IDIPROC NUMBER;
- PESO FLOAT.

Temos ainda, os parâmetros de saída:

- PESOBRUTO OUT FLOAT ;
- PESOLIQUIDO OUT FLOAT.

O sistema dispõe do modelo da procedure:

BUSCA\_INCREMENTO\_PESAGEM

- P\_CODPROD NUMBER - Código da PA;
- P\_CONTROLE VARCHAR2 - Controle adicional do PA;
- P\_IDIPROC NUMBER - Número da Ordem de Produção;
- P\_PESO OUT FLOAT - Qtd. do peso da balança;
- P\_PESOBRUTO OUT FLOAT - Qtd. peso bruto que será calculada pela procedure;
- P\_PESOLIQUIDO OUT FLOAT - Qtd. peso líquido que será calculada pela procedure;

) AS

BEGIN

  P\_PESOBRUTO := 0;

  P\_PESOLIQUIDO := 0;

END;

Os produtos pesados nesta tela poderão ser consultados por meio da tela [Consulta de Volumes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594794-Consulta-de-Volumes).

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594914-Pesagem-de-Produ%C3%A7%C3%A3o-OP#top)
