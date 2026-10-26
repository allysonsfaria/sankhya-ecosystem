---
id: "21343597486231"
titulo: "Personalização de e-mail em Notas Não Fiscais: Como alterar o texto padrão do corpo do e-mail para Pedidos/Notas (Não Fiscais)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21343597486231-Personaliza%C3%A7%C3%A3o-de-e-mail-em-Notas-N%C3%A3o-Fiscais-Como-alterar-o-texto-padr%C3%A3o-do-corpo-do-e-mail-para-Pedidos-Notas-N%C3%A3o-Fiscais"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T14:50:11Z"
rotulos: ["Configuração", "NF-e", "TOP", "E-mail", "Alterar texto padrão do corpo de e-mails de Pedidos/Notas", "Documentos Eletrônicos"]
---

# Personalização de e-mail em Notas Não Fiscais: Como alterar o texto padrão do corpo do e-mail para Pedidos/Notas (Não Fiscais)

É possível alterar o texto do corpo do e-mail enviado por meio de pedidos/notas, porém é importante deixar claro que essa configuração só terá efeito para envio de e-mails vindo de lançamentos **Não fiscais**.

![Imagem 1: Crie um modelo TXT e vincule ao campo ' Arquivo modelo de e-mail ' através da tela de cadastro de TOP's ( Tipos de…](https://ajuda.sankhya.com.br/hc/article_attachments/21922520889111) Crie um modelo TXT e vincule ao campo '**Arquivo modelo de e-mail**' através da tela de cadastro de TOP's (Tipos de Operação - TOP » aba E-mails da TOP);

**(1)** Caso o valor do campo Arquivo modelo de e-mail esteja nulo ou vazio, o corpo do e-mail será enviado conforme a mensagem fixa existente no Sankhya:

"Segue em anexo nota de número 9999 em formato pdf gerado em dd/mm/yyyy hh:mm.
Número Único: 99999
Parceiro: Razão social do parceiro
Valor: R$ 9999,99
Esta é uma mensagem automática, favor não respondê-la."

![Imagem 2: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21922511843095) **OBSERVAÇÃO:**

Ainda na aba E-mails da TOP, o campo Texto p/ e-mail apenas inclui uma informação adicional ao escopo do e-mail padrão citado acima.

**(1)** **Para vincular um cadastro de modelo de e-mail (TXT), siga os passos abaixo:**

![Imagem 3: Acesse a tela "Repositório de Arquivos" ( Caminho: Configurações » Avançado » Repositório de Arquivos) e inclua o…](https://ajuda.sankhya.com.br/hc/article_attachments/21922520889111) Acesse a tela **"Repositório de Arquivos"** (Caminho: Configurações » Avançado » Repositório de Arquivos) e inclua o arquivo em alguma pasta de sua preferência. Após importar o arquivo clique em Propriedades para copiar seu caminho.

![Imagem 4: No cadastro da TOP, aba E-mails da TOP, informe o caminho do repositório no campo Arquivo modelo de e-mail . Exemplo:…](https://ajuda.sankhya.com.br/hc/article_attachments/25166437384855) No cadastro da TOP, aba E-mails da TOP, informe o caminho do repositório no campo Arquivo modelo de e-mail. Exemplo: Repo://modelos/email\_template.txt, onde Repo:// é uma constante para indicar que já está cadastrada no sistema a raiz do repositório no parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"**, e o próximo nível do diretório é a pasta modelos e dentro tem o arquivo e-mail\_template.txt.

**(2)** **Exemplo de Modelo TXT**

Segue abaixo algumas orientações que devem ser seguidas para configurar o arquivo modelo de e-mail, bem como um exemplo de modelo TXT:

```
*** SIADE ***
Nota da empresa: &razsoc
Segue em anexo nota de número: &numnot
em formato pdf gerado em &datsisx
Número Único: &TGFCAB.NUNOTA
Parceiro: &nomcli &cgccpf
Valor: R$ &totnot
```

(1)** A primeira linha** do arquivo TXT deve conter a constante '\*\*\* SIADE \*\*\*' para que o arquivo seja válido.

(1)** A segunda linha** é o assunto do e-mail veja: 'Nota da empresa: **&razsoc**'. Este é opcional e se não quiser informar deixe uma linha em branco que o sistema irá informar o assunto com as regras já existentes. Se o parâmetro **"Usar descrição da TOP p/assunto de Ped/Nota?** -**EMAILASSUNTTOP"** estiver ligado o sistema insere a descrição da TOP como o assunto do e-mail e se estiver desligado insere o texto: Nota emitida por 'razão social da empresa' de número '999'.

(1)** A partir da terceira linha** começa a definição do corpo de e-mail, neste corpo podem ser utilizadas todas as variáveis disponíveis para o TXT da nota. Veja que as variáveis começam com 'e comercial (&)'.

**Nota:** no Help [Variáveis TXT](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109013-Vari%C3%A1veis-de-TXT) é possível ver mais exemplos de variáveis a serem usadas no TXT.

![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/21922511843095) **OBSERVAÇÃO:**

Este corpo de e-mail irá aparecer se o modelo da nota para envio estiver no formato JRXML, ou seja, onde o PDF será anexado ao e-mail e o corpo da mensagem será no modelo definido. Se o modelo da nota for TXT, será enviado no corpo do e-mail a própria nota e o modelo de e-mail não será enviado.
