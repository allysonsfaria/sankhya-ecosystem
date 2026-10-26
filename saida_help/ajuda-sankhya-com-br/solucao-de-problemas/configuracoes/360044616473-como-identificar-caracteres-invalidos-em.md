---
id: "360044616473"
titulo: "Como identificar caracteres inválidos em um XML?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616473-Como-identificar-caracteres-inv%C3%A1lidos-em-um-XML"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-07T15:03:47Z"
rotulos: ["Unicode: 0x19", "Configuração", "NF-e", "XML", "SEFAZ", "Identificação de Caracteres Inválidos em um XML", "Erro", "Documentos Eletrônicos"]
---

# Como identificar caracteres inválidos em um XML?

Neste artigo, iremos recomendar uma forma de identificar caracteres inválidos, que a maioria dos nossos clientes e analistas usam, pois torna o diagnostico mais preciso e rápido.

Seguindo as recomendações abaixo, espera-se a efetividade na resolução do incidente.

**![Imagem 1: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942095782679) Instalando o Notepad++**

Uma das ferramentas que utilizamos para identificar caracteres inválidos no XML, é o Notepad++ que é uma ferramenta de edição de texto de licença GLP, ou seja, Open Source (Gratuito).

O download pode ser feito através do link: [https://notepad-plus-plus.org/download](https://notepad-plus-plus.org/download/)

Baixe e instale a versão de acordo coma arquitetura do seu sistema operacional, 32 ou 64 bits.

Após baixar, instale o software normalmente.

**![Imagem 2: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942119416855) Instalando a extensão XML Tools**

Ao abrir o Notepad++ é necessário realizar a instalação do plugin XML Tools para que seja possível realizar a indentação do código XML.

Faça os seguintes passos:

2.1-  Abra o Notepad++, clique em Plugins e em seguida na opção Plugins Admin;

![Imagem 3: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942119419799)

2.2 - Procure pelo Plugin XML Tools, e em seguida clique em Install;

![Imagem 4: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942119422615)

3.1 - Instalado o plugin e reiniciado o Notepad++. Clique na opção Arquivo, e em seguida em Abrir, e selecione o arquivo de XML, conforme as imagens abaixo;

![Imagem 5: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942095798551)![Imagem 6: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942119427863)

![Imagem 7: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942119429783)

4.1 - Após abrir o XML, o mesmo virá sem quebra de linhas, sendo necessário apertar Ctrl + Alt + Shift + B, ou utilizar a seguinte opção;

![Imagem 8: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942119436823)

![Imagem 9: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942095810711) Feito o passo acima, o XML será indentado, fazendo que seja mais fácil sua leitura.

![Imagem 10: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942095811223) Para identificar os caracteres inválidos no XML, selecione a opção de Codificação é UTF-8;

![Imagem 11: Instalando o Notepad++](https://ajuda.sankhya.com.br/hc/article_attachments/18942095814167)

Conforme a imagem acima foi identificado caracteres especiais na tag <xProd> (Nome do produto). As letras 'xAO' são caracteres especiais que ocorrem geralmente por haver espaços em branco no nome do produto, e é ocasionada quando ao invés de se digitar o nome do produto, o usuário copiou e colou nome, levando a ocultação do caractere inválido.

**Importante:**

Espaços em branco indevidos também podem causar essa rejeição.  Conforme .gif abaixo, através do Notepad++ é possível fazer essa análise.  Utilize o filtro **[^0-9A-Za-z\t\n\r\<\>\|\$\?\ \"\=\:\/\-\+\%\@\\*\#\(\)\;\_,.]** dentro da opção 'Localizar',  mencionando modo de pesquisa **'expressão regular'**:

[GIF animado: Imagem 12: Espaços em branco indevidos também podem causar essa rejeição. Conforme .gif abaixo, através do Notepad++ é possível…](https://ajuda.sankhya.com.br/hc/article_attachments/360093713193)

Outros caracteres que podem ser identificados.

Todo conteúdo de um XML passa por uma análise do “parser” específico da linguagem. Alguns caracteres afetam o funcionamento deste “parser”, não podendo aparecer no texto de uma forma não controlada.

Os caracteres que afetam o “parser” são:

• > (sinal de maior),

• < (sinal de menor),

• & (e-comercial),

• “ (aspas),

• ‘ (sinal de apóstrofo).

Alguns destes caracteres podem aparecer especialmente no campo de Razão Social,Endereço e Informação Adicional de uma NF-e. Para resolver esses casos, é recomendável a substituição do caractere que causa o problema.

**Esse processo precisara ser feito uma única vez, após instalado e configurado o Notepad++, basta sempre abrir o XML com problemas, pelo notepad++ para identificar o carácter invalido.**
