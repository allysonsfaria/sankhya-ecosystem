---
id: "360044044794"
titulo: "Como realizar a importação de XML de notas emissão própria?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044044794-Como-realizar-a-importa%C3%A7%C3%A3o-de-XML-de-notas-emiss%C3%A3o-pr%C3%B3pria"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-30T18:02:20Z"
rotulos: ["DUVIDANF", "#PUBLIFER", "Configuração", "NF-e", "XML", "Importação", "TOP", "Importação de XML de Notas de Emissão Própria", "Notas de emissão própria"]
---

# Como realizar a importação de XML de notas emissão própria?

**(1)** Para importação de XML de notas emissão própria, siga as orientações abaixo:

![Imagem 1: Tela 'Portal de Importação de XML' » Outras Opções » Preferências para importação de NF-e de Emissão Própria:](https://ajuda.sankhya.com.br/hc/article_attachments/16779668576407) Tela 'Portal de Importação de XML' » Outras Opções » Preferências para importação de NF-e de Emissão Própria:

**(1)** Acionando-se está opção tem-se a exibição do pop-up **"Preferências para importação de NF-e de Emissão Própria"**:

![Imagem 2: (1) Acionando-se está opção tem-se a exibição do pop-up "Preferências para importação de NF-e de Emissão Própria" :](https://ajuda.sankhya.com.br/hc/article_attachments/14765345499671)

**(1)**Através deste pop-up serão inseridas as informações que irão possibilitar a importação dos arquivos de XML das notas fiscais eletrônicas de emissão própria. Sendo que, as TOP's utilizadas deverão conter as seguintes configurações:

![Imagem 3: Tela "Tipos de Operação-TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros):](https://ajuda.sankhya.com.br/hc/article_attachments/16779668596759) Tela **"Tipos de Operação-TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros):

**(1)** Na aba **"Impressão"**, configure o campo **"NF-e"** com a opção **"Emissão Própria"**;

**(1)** Configure na aba **"Impostos"**, o campo **"Cálculo de ICMS, IPI e ISS",** selecionando a opção **"Não calcula e digita"**;

**(1)** Na aba **"Desp.Acessórias"** configure todos os impostos pertinentes as despesas acessórias de frete, destaque, embalagem e seguro.

**IMPORTANTE**: 

A funcionalidade de importação de XML de emissão própria é projetada para ser utilizada com Tipos de Operação (TOPs) de **Compra** ou **Venda**.

Atualmente, o sistema **não suporta** a seleção pela tela **''Portal de Mov. Internas''** (Comercial » Consulta » Portal de Mov. Internas) com tipo de movimento de **Transferência** durante este processo de importação. Ao tentar realizar o procedimento com uma TOP de transferência, o sistema não permitirá a seleção ou o prosseguimento da operação.

![Imagem 4: Tela "Empresa" (Caminho de acesso: Comercial » Preferências), aba "NF-e/NFC-e" , acione a marcação "Importa NF-e de…](https://ajuda.sankhya.com.br/hc/article_attachments/16779690991895) Tela **"Empresa"** (Caminho de acesso: Comercial » Preferências), aba **"NF-e/NFC-e"**, acione a marcação **"Importa NF-e de emissão própria?"**:

Para que uma nota de emissão própria pelo [Portal de importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML) fique com o Status NF-e igual à **"Aprovada" e " Confirmada"**, é necessário que o parâmetro **"Importa compra e venda na mesma base? - IMPCOMVENMESBAS"**esteja desligado.

Porém, para que o parâmetro acima assuma o comportamento descrito, o parâmetro IMPCOMVENMESBAS deve ser ligado, caso contrário, o mesmo XML não será importado novamente e será exibida a mensagem:

**"Chave de acesso já existe no portal de vendas, número único xxxx, chave de acesso: 00000000000000000000000000000000000000000000000000000"**

Além disso, ao habilitar apenas o parâmetro IMPCOMVENMESBAS, o sistema ainda importará o mesmo XML duas vezes, mas na posição invertida, ou seja, priorizando a Compra e, posteriormente, a Emissão Própria.

**![Imagem 5: NOTA:](https://ajuda.sankhya.com.br/hc/article_attachments/16779690998807) NOTA:**

O Tipo de Negociação utilizado irá determinar como serão gerados os financeiros das notas importadas.
