---
id: "4405808570519"
titulo: "Como inserir logomarca no DANFE? "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405808570519-Como-inserir-logomarca-no-DANFE"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:22:32Z"
rotulos: ["Configuração", "Impressão", "Empresa", "NF-e", "DANFE", "não apagar", "Inserindo Logomarca no DANFE", "Documentos Eletrônicos"]
---

# Como inserir logomarca no DANFE? 

**![Imagem 1: Inserir logomarca no DANFE](https://ajuda.sankhya.com.br/hc/article_attachments/16370238988439) Inserir logomarca no DANFE**

O passo a passo abaixo é destinado aos usuários que desejam inserir ou alterar a logomarca impressa no DANFE.

**(1)** Acesse o caminho: Comercial » Preferências » Empresa » Aba 'Documentos Eletronicos'.

**(1)** Acesse a aba **NF-e/NFC-e**,  sub-aba **NF-e.** Localize o campo **"Arquivo Logomarca"** e preencha com o caminho em que foi salva a logomarca da empresa, para que seja impressa no DANFE:

![Imagem 2: (1) Acesse a aba NF-e/NFC-e , sub-aba NF-e. Localize o campo "Arquivo Logomarca" e preencha com o caminho em que foi…](https://ajuda.sankhya.com.br/hc/article_attachments/21674871902743)

**![Imagem 3: Definição de caminhos](https://ajuda.sankhya.com.br/hc/article_attachments/16370239003543) Definição de caminhos**

Este caminho pode ser definido de duas formas diferentes:

**(1)**O arquivo será obtido a partir da pasta no servidor definida pelo parâmetro **"Pasta de modelos para impressão - SERVDIRMOD"**.

**Exemplo:** Considerando que o parâmetro seja /home/mgeweb/modelos e que o nome do arquivo seja logoemp1.jpg, então o valor do campo **"Arquivo Logomarca"** deve ser logoemp1.jpg. Naturalmente, o arquivo deve ter sido copiado para dentro da pasta /home/mgeweb/modelos para que tudo funcione.

**(1)**Use uma path relativa ao repositórios de arquivos do Sankhya Om, assim:

Repo://imagens/logoemp1.jpg

Note o prefixo 'Repo://', isso determina que o caminho seja relativo ao repositório de arquivos e neste caso sistema irá buscar o arquivo logemp1.jpg no repositório de arquivos dentro da pasta imagens.

**![Imagem 4: Repositório de arquivos](https://ajuda.sankhya.com.br/hc/article_attachments/16370269074071) Repositório de arquivos**

Com os arquivos inseridos no**"Repositório de Arquivos"**, o usuário estará possibilitado a ter acesso a estes documentos mesmo não estando presente em seu local de trabalho. Isso devido ao fato de que o Sankhya-W pode ser acessado via internet de qualquer lugar do mundo, possibilitando ao usuário acessar os arquivos no servidor que roda o sistema. Sendo assim, o usuário poderá inserir no Repositório de Arquivos, qualquer tipo de arquivo que desejar, e poderá permitir acesso a outros usuários, possibilitando assim, fácil acesso a estes arquivos.

**3.1. Inserindo arquivos**

Quando a pasta selecionada não possui nenhum arquivo inicial, o sistema apresenta a seguinte mensagem:

**"Esta página não contém arquivos, clique aqui para adicionar!"**

Sendo assim, ao clicar em **"clique aqui",** o sistema apresenta uma janela que é utilizada para buscar o arquivo e inseri-lo no repositório de arquivos.

É possível copiar ou mover os arquivos de uma pasta para outra, para isso selecione os arquivos a serem copiados ou movidos e arraste com o mouse para a pasta destino.

**Nota:** Para selecionar mais de um arquivo pressione **"Ctrl"** e clique com o mouse sobre a linha de cada arquivo ou pressione **"Shift"** e com as setas direcionais do teclado selecione os arquivos que serão incluídos na seleção.

Após a inserção do arquivo, a tela passa a apresentar um novo modo de visualização e habilita os botões presentes em sua parte superior.

A opção **"Adicionar Arquivos"** é utilizada para inserir novos itens na pasta. Os arquivos são posicionados na grade, como pode ser observado na imagem acima.

Após selecionar o arquivo desejado na grade, caso necessário, pode-se utilizar a opção **"Remover Selecionados"** para excluí-los da pasta. Através da opção **"Visualizar/Baixar"**, realiza-se o download de um arquivo na máquina.

Já a opção **"Renomear"** possibilita dar um novo nome ao arquivo. Com a opção **"Atualizar"** é possível substituir o arquivo selecionado por outro, para isso, o sistema apresentará a mesma janela utilizada para buscar e inserir os arquivos no repositório.

A opção **"Propriedades"** apresenta uma pequena janela com informações sobre o arquivo selecionado.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16370269077783) OBSERVAÇÃO:**

O layout do DANFE definido pela Secretaria da Fazenda possui um lugar onde opcionalmente pode-se colocar uma “logomarca”, desde que a mesma não comprometa as informações de "Identificação do emitente", que estão posicionadas ao lado da logomarca. O componente usado no DANFE possui largura = 65 pixels, altura = 72 pixels e está configurado para centralizar a imagem. Esse componente não possui a função de redimensionar a imagem, ajustando-a ao seu tamanho.
