---
id: "360044595734"
titulo: "IReport - Como embutir imagens no relatório modelo jrxml, diretamente no arquivo?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595734-IReport-Como-embutir-imagens-no-relat%C3%B3rio-modelo-jrxml-diretamente-no-arquivo"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:44:42Z"
rotulos: ["Fonte: Consultor de Implantação Guilherme Hahn", "Configuração", "Relatórios", "XML", "Inclusão de Imagens no Ireport: Guia Rápido", "Imagem", "JasperReports", "Base64"]
---

# IReport - Como embutir imagens no relatório modelo jrxml, diretamente no arquivo?

**Observe as configurações:**

1- Formato da imagem: JPG ou GIF, de preferência JPG para uma resolução melhor.

2- Tenha a imagem já no tamanho final a ser incluído no [Ireport](https://downloads-sankhya-tools.s3-sa-east-1.amazonaws.com/iReport-4.0.1.zip) para evitar que ocupe espaço desnecessário no JRXML.

3- A imagem será transformada em um [hash](https://g.co/kgs/hwx5Tk) BASE 64, existem diversos sites que fazem o encode de uma imagem para Base 64, abaixo está a url utilizada neste manual:

<https://www.base64-image.de/>

4- Informe o caminho da imagem a ser convertida e após a conversão da imagem, clique no botão **"Show Code"**:

![Imagem 1: 4- Informe o caminho da imagem a ser convertida e após a conversão da imagem, clique no botão "Show Code" :](https://ajuda.sankhya.com.br/hc/article_attachments/20789104000791)

6- Copie o hash Base 64 gerado a partir de /9 até o seu final.

![Imagem 2: 6- Copie o hash Base 64 gerado a partir de /9 até o seu final.](https://ajuda.sankhya.com.br/hc/article_attachments/20789121903511)

7- No modelo Ireport crie uma variável com as definições abaixo:

• Nome da variável
• Reset Type = Page
• Initial Value Expression = “CONTEUDO BASE 64 GERADO” → Entre aspas duplas

8- Adicione o componente de imagem ao Ireport, indicando altura e largura conforme sua imagem.

• **Expression Class**: java.io.InputStream

• **Image Expression**: new ByteArrayInputStream(Base64.decodeBase64($V{NOMEVARIAVEL}.getBytes()))

• **Scale Imag**e: Retain Shape

**Observação**: Neste exemplo estamos utilizando uma variável, porém o hash poderia estar contido em uma tabela do banco de dados, tornando a imagem dinâmica, como logo da empresa (multiempresa), etc.

\* Existem diversas maneiras e aplicativos que podemos utilizar para redimensionar ou visualizar as dimensões da imagem, uma maneira fácil é utilizando o próprio Paint.

9- No modo XML do Ireport, inclua o import abaixo logo após as tags <property e antes de qualquer tag

<parameter... ou <querystring... :
           <import value="org.apache.commons.codec.binary.Base64"/>

10- Volte para o modo Designer, salve e pronto. Só subir para Relatórios Formatados e utilizar.

\* Para utilizar imagens estáticas grandes, a solução de subir para o servidor ainda é a mais indicada.
