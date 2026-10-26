---
id: "360044594774"
titulo: "Pesagem de Produção (ID Volume)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594774-Pesagem-de-Produ%C3%A7%C3%A3o-ID-Volume"
trilha: "Manual do Produto > Produção > Produção/W"
atualizado_em: "2026-07-29T14:50:42Z"
rotulos: ["AJUDA DO SKW", "manual", "br.com.sankhya.prod.pesagemproducaoidvolume", "Pesagem de Produção (ID Volume) manual", "Configuração", "Etiquetas", "Rotinas", "Estoque", "Produção", "Insira o ID do volume para iniciar a pesagem", "Ajuste balança e configurações de pesagem", "Use peso bruto e líquido para gestão e documentação", "Pesagem"]
---

# Pesagem de Produção (ID Volume)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312639349783) Módulo: Produção > Rotinas
```

---

Nesta tela, a pesagem será efetuada a partir do ID dos volumes gerados, ou seja, ao digitar o ID de um determinado volume o sistema irá carregar a ordem de produção responsável pela sua fabricação e irá aguardar o peso da mesma.

![Imagem 2: Nesta tela, a pesagem será efetuada a partir do ID dos volumes gerados, ou seja, ao digitar o ID de um determinado…](https://ajuda.sankhya.com.br/hc/article_attachments/6922410247447)

**Importante:** a geração dos IDs utilizados nesta tela acontece via personalização; um exemplo que ilustra a geração de ID via personalização seria a impressão da ordem, e das etiquetas da identificação (ID) dos volumes após lançamento da OP via relatório formatado.

O visor ![leitura](https://ajuda.sankhya.com.br/hc/article_attachments/15534397629847) **"Leitura Balançada"** permite que você visualize de forma online se a balança já está estável para que seja feita a coleta de dados. Para isso, configure a **"Busca de peso"** para **"Ao Solicitar"**. 

**Observação:** o visor não atuará em casos de configuração de múltiplas balanças.

Por meio do botão **"Configurar grade"**, você pode incluir colunas adicionais, conforme sua preferência.

O botão ![Imagem 4: O botão Configurar grade proporciona a definição de como o sistema deverá obter o peso da balança, ao ser acionado, o…](https://ajuda.sankhya.com.br/hc/article_attachments/16705595364759) Configurar grade proporciona a definição de como o sistema deverá obter o peso da balança, ao ser acionado, o pop-up **"Configurações"** será exibido:

![Imagem 5: O botão Configurar grade proporciona a definição de como o sistema deverá obter o peso da balança, ao ser acionado, o…](https://ajuda.sankhya.com.br/hc/article_attachments/6922407083159)

Neste referido pop-up, temos o campo **"Busca de Peso"**, na qual você pode selecionar entre duas opções:

- Por meio da opção **"Constante"**, após a seleção de uma OP/Atividade, o sistema abrirá a comunicação com a balança e irá aguardar o envio de peso da mesma.
- Na opção **"Ao Solicitar"** O sistema aguardará o usuário clicar no botão **"Pesar"** para buscar o peso da balança.

**Observação:** para esta configuração a balança deve estar configurada para o envio de peso constante.

Também temos a marcação **"Confirma apontamento automático"** que ao ser acionada, o sistema tentará fazer a confirmação automática das pesagens pendentes no momento em que o usuário selecionar uma nova OP para realizar pesagem.

O Botão **"[F6] Capturar Peso"** será exibido conforme a configuração do campo Busca de Peso, ou seja, se a opção Constante estiver selecionada, a opção será substituída pelo texto **"Aguardando Peso ..."**, caso a opção Ao Solicitar for escolhida, o botão [F6] Capturar Peso será habilitado.

Ao realizar a pesagem de volume por meio do botão [F6] Capturar Peso, o sistema buscará as informações de pesagens atribuídos na tabela TPRAVO, e um pop-up para a escolha para a impressão da etiqueta será exibido.

O botão **"[F2] Reimprimir"**, permitirá a reimpressão de etiquetas de volumes já pesados, na qual você pode inserir **"ID inicial"** e **"ID final"**, logo, as etiquetas serão reimpressas de acordo com o intervalo definido.

Tem-se ainda, a possibilidade de exclusão de um ou mais volumes selecionados na grade.

A confirmação da pesagem criará e confirmará um apontamento para todos os volumes que já foram pesados o aqueles que ainda estão pendentes, esta ação será realizada por meio do botão **"Confirmar"**.

Se dois usuários realizarem a aceitação de uma mesma OP e efetuarem o apontamento desta nas telas [Pesagem de Produção (OP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594914) e/ou Pesagem de Produção (ID Volume), o sistema irá alertar ambos sobre a edição por meio da mensagem:

**"Existem outros usuários editando os apontamentos dessa OP. Deseja atualizar a grade para confirmar o apontamento?"**

No rodapé da tela ao lado da aba **"Totais"**, tem-se a aba **"Informações adicionais"** que será exibida se você optar por incluir campos adicionais na tabela TPRAVO.

**Nota:** os parâmetros de campos da tabela TPRAVO estão disponíveis para a criação do modelo de etiqueta, são eles:

- ID;
- IDIPROC;
- CODPROD;
- DESCRPROD;
- CONTROLE;
- NROLOTE;
- PESOBRUTO
- PESOLIQ;
- TIPO.

**Observação:** o sistema utilizará as configurações nos campos **"Modelo de etiqueta"** da tela de [Cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Produtos-) (Sub-aba Pesagem), campo **"Modelo de etiqueta"** (tela Empresa, aba Manufatura) e o parâmetro **"Modelo de etiqueta pesagem - MODETIPES"** que irá definir o modelo da etiqueta. O sistema respeita a hierarquia descrita anteriormente para definir qual o modelo de etiqueta será utilizado na impressão:

- 1º Produto - Se o produto possui modelo de etiqueta, então utiliza o modelo do produto para impressão.
- 2º Empresa - Se o produto não possui modelo de etiqueta, mas a empresa da planta da ordem possui modelo de etiqueta, então utiliza o modelo da empresa para a impressão.
- 3º Parâmetro - Se o produto e a empresa da planta da ordem não possuem modelo de etiqueta, mas o parâmetro possui um modelo de etiqueta especificado, então utiliza o modelo do parâmetro para a impressão.

Tem-se ainda a chamada de retorno do peso bruto e líquido, que se refere aos pesos brutos e totais do produto, ou seja, considera o peso das embalagens utilizadas neste.

Considere o exemplo:

O produto Tecido será armazenado em rolos, portanto na embalagem será considerado o rolo interno (denomina-se tarugo), que possui um peso próprio e este possui ainda o plástico em que é embalado o tecido e o tarugo, que também possui um peso, tem-se então a soma total do peso dos componentes do produto Tecido, em que dispõe o Tarugo + Tecido + Embalagem. Logo, o peso bruto será o peso destes componentes enquanto que o peso líquido será somente o peso do produto em si.

Contudo, para a gestão de estoque da empresa é preciso considerar o peso líquido, pois apenas o Tecido é ponderado na venda, mas para os processos de entrega e geração da nota fiscal do produto é preciso realizar a cotação dada a importância do peso total do item, pois o produto será transportado como um todo.

Deste modo, tem-se a chamada de retorno do peso bruto e líquido conforme a balança. Os parâmetros de entrada deste são:

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

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594774-Pesagem-de-Produ%C3%A7%C3%A3o-ID-Volume#top)
