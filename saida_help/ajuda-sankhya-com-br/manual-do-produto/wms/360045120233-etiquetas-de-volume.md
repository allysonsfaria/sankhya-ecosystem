---
id: "360045120233"
titulo: "Etiquetas de Volume"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:15:43Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios Formatados", "WMS", "Volume", "Etiquetas", "Preferências", "INTERVIMPETQVOL", "br.com.sankhya.mgewms.rot.impressaoetiquetavolume", "Etiquetas de Volume manual", "Filtre visualize e imprima etiquetas", "Defina modelo e impressora para etiquetas", "Utilize Job de Impressão e Sankhya Print Service", "WMSSEQETQVOLDCA"]
---

# Etiquetas de Volume

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311588604439) Módulo: WMS > Rotinas
```

---

Através desta tela, você realizará a pré-visualização e/ou impressão das Etiquetas de Volume.

Para utilização desta rotina, é necessário configurar previamente o modelo de etiqueta a ser utilizado (tela **"Relatórios Formatados"**) e determinar a impressora a ser utilizada para impressão; esta configuração pode ser por **"Preferências da Empresa"** ou por **"Área de Separação"**.

A seguir, trataremos dos detalhes sobre as configurações a serem executadas no sistema, bem como seu consequente comportamento:

[Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#configuraes)                                                                [Comportamento da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#comportamentodatela)

[Modelo de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#modelodeimpresso)                                                  [Roteamento de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#roteamentodeimpresso)

[Job de Impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#jobdeimpresso)                                                        [Impressão de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#Impress%C3%A3odeEtiquetas%C2%A0)

## Configurações

As pré-condições para utilização das Etiquetas de Volume, são:

[Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados):

Nesta tela, será configurado o modelo de impressão de etiquetas de volume a ser utilizado:

![Imagem 2: Nesta tela, será configurado o modelo de impressão de etiquetas de volume a ser utilizado:](https://ajuda.sankhya.com.br/hc/article_attachments/360077579033)

[Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa):

Na definição das Preferências da Empresa, na aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa#abawms) informe os campos **"Modelo padrão de Etiqueta de Volume"** e **"Impressora padrão da Etiqueta de Volume"**:

![Imagem 3: Na definição das Preferências da Empresa , na aba WMS informe os campos "Modelo padrão de Etiqueta de Volume" e…](https://ajuda.sankhya.com.br/hc/article_attachments/360076436014)

[Área de Separação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054):

No cadastro da Área de Separação, na aba [Impressão de Etiquetas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054-%C3%81rea-de-Separa%C3%A7%C3%A3o#abaimpressodeetiquetas), teremos os campos **"Impressora da Etiqueta de Volume"** e **"Modelo de Etiqueta de Volume"**:

![Imagem 4: No cadastro da Área de Separação , na aba Impressão de Etiquetas , teremos os campos "Impressora da Etiqueta de Volume"…](https://ajuda.sankhya.com.br/hc/article_attachments/360077579093)

No primeiro campo, informe a impressora a ser utilizada na impressão; o segundo recebe o modelo de etiqueta anteriormente inserido na tela Relatórios Formatados.

**Importante:** cada configuração é independente, ou seja, se for configurado o modelo de impressão na Área de Separação, porém não foi informada a impressora, e fez a configuração inversa nas Preferências da Empresa, informando-se a impressora padrão e não informando o modelo, o sistema irá utilizar o modelo da Área de Separação e a impressora inserida nas Preferências da Empresa.

Caso algum dos campos citados não esteja informado tanto na Área de Separação quanto nas Preferências da Empresa, a rotina exibirá uma das seguintes mensagens:

**"Modelo de etiqueta de volume não encontrado para a empresa XX"**

**"Impressora para impressão de etiquetas não configurada para a empresa YY"**

**Importante:** a impressora informada nas configurações mencionadas, deverá estar configurada através do [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714) para que ocorra a impressão.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#top)

## Comportamento da tela

![Imagem 5: Comportamento da tela](https://ajuda.sankhya.com.br/hc/article_attachments/360076436034)

Uma vez realizadas as devidas configurações, na tela Etiquetas de Volume, você pode filtrar a etiqueta desejada por meio dos seguintes campos:

- Empresa;
- Ordem de Carga;
- Produto;
- Conferente;
- Área de Separação;
- Pedido/Nota;
- Situação da impressão - esta pode ser **"Não impresso"**, **"Reimpressão"** ou **"Ambos"**.

Depois de definidos os filtros desejados, clique em **"Aplicar"** serão exibidas na grade as etiquetas que atendem o filtro configurado.

Quando o parâmetro **"Sequenciar Etiquetas na Form. Volumes por Produto - WMSSEQETQVOLDCA"** estiver ativado, o sistema irá gerar uma sequência numérica na coluna **"Sequência Etiqueta"** para cada produto que tenha o mesmo **"Nro. Único Nota"**. Por exemplo, se existirem 10 produtos com o Nro. Único Nota iguais, a coluna Sequência Etiqueta atribuirá números sequenciais a esses produtos de 1 a 10.
**Observação:** se o parâmetro estiver desativado, a coluna Sequência Etiqueta não será preenchida e permanecerá zerada.

No alto da tela, temos os seguintes botões:

![Imagem 6: Remover selecionados: por este botão, será retirado da grade as etiquetas que não serão trabalhadas no momento.](https://ajuda.sankhya.com.br/hc/article_attachments/16845035048855) **Remover selecionados:** por este botão, será retirado da grade as etiquetas que não serão trabalhadas no momento.

![Imagem 7: Remover NÃO selecionados: este botão realiza o procedimento inverso do anterior, ou seja, retira da grade as etiquetas…](https://ajuda.sankhya.com.br/hc/article_attachments/16845035055255) **Remover NÃO selecionados:** este botão realiza o procedimento inverso do anterior, ou seja, retira da grade as etiquetas não selecionadas.

**Observação:** uma etiqueta é selecionada, ao manter pressionado a tecla **"Ctrl"** no teclado e clicando-se na linha correspondente à etiqueta desejada.

![Imagem 8: Baixar modelo padrão: Através deste botão realize a baixa do modelo padrão de impressão de etiquetas, que é…](https://ajuda.sankhya.com.br/hc/article_attachments/360076438714) **Baixar modelo padrão:** Através deste botão realize a baixa do modelo padrão de impressão de etiquetas, que é disponibilizado no sistema.

![Imagem 9: Pré-visualizar: O acionamento deste botão abre uma tela contendo a prévia da etiqueta que será impressa.](https://ajuda.sankhya.com.br/hc/article_attachments/360077583193) **Pré-visualizar:** O acionamento deste botão abre uma tela contendo a prévia da etiqueta que será impressa.

![Imagem 10: Imprimir: Este botão efetua a impressão da(s) etiqueta(s) selecionada(s).](https://ajuda.sankhya.com.br/hc/article_attachments/360076438854) **Imprimir:** Este botão efetua a impressão da(s) etiqueta(s) selecionada(s).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#top)

## Modelo de Impressão

São disponibilizados nesta tela dois modelos padrões de impressão, sendo que, estes serão obtidos através do botão ![Imagem 11: São disponibilizados nesta tela dois modelos padrões de impressão, sendo que, estes serão obtidos através do botão .](https://ajuda.sankhya.com.br/hc/article_attachments/360076438714).

Ao acionar o botão acima mencionado, será apresentado um pop-up de mesmo nome; no campo **"Tipo de Arquivo"** temos os seguintes modelos padrões:

- Arquivo .jrxml
- Arquivo .zpl

Caso seja necessário configure de maneira personalizada, os seguintes campos são disponibilizados para configuração na rotina de impressão:

- RAZAOSOCIAL
- ORDEMCARGA
- NUMPEDIDO
- PARCEIRO
- CODPARC
- IDREV
- AREASEP
- VOLUME
- CONFERENTE
- DOCA
- TRANSPORTADORA
- ENDERECOPARCEIRO

Assim como informado na seção Configurações, o modelo deve ser incluído na tela de [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) para que possa ser configurado nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Empresa) e/ou na [Área de Separação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044613054).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#top)

## Roteamento de Impressão

O Roteamento de impressão permite que um usuário conferente ao efetuar o login no emulador do coletor de dados utilizando um computador, consiga acessar a impressora configurada para o mesmo.  

**Observações:**

- Esse roteamento só funcionará com o Emulador (SuperWaba);
- Cada usuário do coletor deverá possuir também um usuário no Windows e seu respectivo arquivo login.properties com a impressora informada.

**1.** Foi adicionada a linha de atalho a expressão a seguir, ficando no seguinte formato:

C:\SuperWaba1\SuperWaba.exe br/com/sankhya/wms/visao/MainWMS WMS WMSK %SystemDrive%%HoMePath%

Caso a variável de ambiente não esteja no padrão (HomePath), a linha de atalho deve ser alterada para:  

C:\SuperWaba1\SuperWaba.exe br/com/sankhya/wms/visao/MainWMS WMS WMSK %USERPROFILE%

**2.** Deve-se criar na pasta do usuário, o arquivo login.properties com o conteúdo IMPRESSORAETIQVOL=Canon iR1020/1024/1025 ADM;

**3.** Ao selecionar um registro da tela Expedição de Mercadorias com a situação **"Aguardando Conferência"**, e solicitar a impressão de etiquetas, na coluna **"Nome da impressora"** teremos o nome da impressora que foi impressa fisicamente a etiqueta (Configurada no SPS).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#top)

## Job de Impressão

O sistema conta com um Job de Impressão (mecanismo interno que realiza as impressões), que é executado por padrão, a cada 1 (um) minuto, verificando se existem etiquetas a serem impressas.

O tempo de execução deste Job, pode ser modificado por meio do parâmetro **"Intervalo para impressão da etiqueta de volume - INTERVIMPETQVOL"**, que deve receber o valor desejado, em minutos.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#top)

## Impressão de Etiquetas

Para realizar a impressão das etiquetas, acesse a tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [WMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abawms) e faça as seguintes configurações:

1. Efetue a marcação **"Imprimir etiquetas de volume na conferência"**;
2. Ative a marcação **"Imprime etiquetas de separação por OC"**;
3. Informe a **"Impressora padrão da Etiqueta de Volume"**.

Em seguida, faça o download do modelo padrão na tela [Etiquetas de Volume](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume) e vincule o modelo baixado no [Relatório Formatado](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694) que deve ser criado previamente e, em seguida, informe o código do referido relatório no campo **"Modelo Padrão de Etiqueta de Volume"** (tela Preferências da Empresa, aba WMS).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120233-Etiquetas-de-Volume#top)
