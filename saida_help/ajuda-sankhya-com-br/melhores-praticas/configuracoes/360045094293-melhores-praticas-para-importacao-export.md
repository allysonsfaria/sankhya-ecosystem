---
id: "360045094293"
titulo: "Melhores Práticas para Importação/Exportação de Certificado Digital - Cadeia Completa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094293-Melhores-Pr%C3%A1ticas-para-Importa%C3%A7%C3%A3o-Exporta%C3%A7%C3%A3o-de-Certificado-Digital-Cadeia-Completa"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-07-22T15:51:20Z"
rotulos: ["CERTIFICADO DIGITAL", "Configuração", "Segurança", "NF-e", "Importação", "SEFAZ", "Guia para Certificados Digitais: Importação e Exportação", "Exportacao"]
---

# Melhores Práticas para Importação/Exportação de Certificado Digital - Cadeia Completa

#### Importação/ Exportação de Certificados Digitais - Cadeia Completa

Desde novembro de 2014 a Receita Estadual de Goiás, passou a exigir a cadeia completa no certificado digital. Essa cadeia representa a hierarquia de emissão do certificado digital, que tem como raiz o ICP-Brasil (Infraestrutura de Chaves Públicas Brasileira). A maioria das autoridades certificadoras já geram o certificado contendo essa cadeia. A emissão do certificado varia de uma emissora para outra, por isso pode ocorrer de um determinado certificado não ser gerado com a referida cadeia.

Um certificado gerado sem a cadeia, irá funcionar em qualquer outro estado, porém para o estado de Goiás, alguns problemas serão gerados.

No nosso emissor de NFe, o SanNFe, foi feita a validação do certificado, a fim de identificar que o mesmo não possui a cadeia, e apresentar uma mensagem para o usuário. Essa mensagem pode ser desativada se o arquivo "**url-webservices.xml**" do SanNFe for modificado. Caso isso seja feito, o sistema não irá apresentar uma mensagem legível ao usuário, pois a Sefaz faz essa validação antes mesmo de chegar ao sistema que processa o envio/recebimento de NFe, causando um erro de comunicação no HTTPS, especificamente no handshake.

Para solucionar esse problema, o cliente deve entrar em contato com a empresa que emitiu o certificado digital, e explicar a necessidade da presença de tais informações no certificado, para que este seja gerado com a cadeia completa.

Como o envio de uma NF-e, é um serviço crítico e pode comprometer o faturamento de uma empresa, tem-se a seguir um passo-a-passo de como exportar o certificado conforme exigido para a Sefaz do estado de Goiás.

Para que os passos a seguir funcionem, é necessário que a máquina em que o procedimento será executado, tenha as cadeias do emissor do certificado já instaladas. Na maioria das vezes, essas cadeias já vem instaladas no navegador, mas caso o procedimento não funcione, será necessário instalá-las. O procedimento de como instalar as cadeias raízes, não será contemplado nesse documento.

- **Importação**

Depois de adquirido o Certificado Digital junto ao órgão emissor, é necessário que seja feita a importação deste arquivo para a máquina. Para realização deste procedimento, deve-se seguir os seguintes passos:

**Passo 1** - Através de um duplo clique sobre o Certificado Digital, será aberta a seguinte tela:

![Imagem 1: Passo 1 - Através de um duplo clique sobre o Certificado Digital, será aberta a seguinte tela:](https://ajuda.sankhya.com.br/hc/article_attachments/20653711358871)

**Passo 2** – Clicando-se em “Avançar”, será aberta a tela para que seja feita a busca do Certificado na máquina; esta busca é realizada clicando-se no botão “Procurar...”.

![Imagem 2: Passo 2 – Clicando-se em “Avançar”, será aberta a tela para que seja feita a busca do Certificado na máquina; esta…](https://ajuda.sankhya.com.br/hc/article_attachments/20653711373719)

**Passo 3** – Localizado o arquivo, e clicando-se novamente em **“Avançar”,** será aberta a tela, para que seja informada a senha do certificado digital. A senha aqui informada, diz respeito a senha fornecida pelo órgão emissor do certificado, no momento de sua aquisição.

**Importante:**

Neste passo, é de extrema importância, que a marcação em destaque (Marcar esta chave como exportável. Isso possibilitará o backup e o transporte das chaves posteriormente), seja efetuada, pois sua não marcação, irá interferir negativamente no processo de geração da cadeia completa de certificados.

![Imagem 3: Neste passo, é de extrema importância, que a marcação em destaque (Marcar esta chave como exportável. Isso…](https://ajuda.sankhya.com.br/hc/article_attachments/20653723800087)

**Passo 4** – Clicando-se em “Avançar”, será aberta a tela para seleção do repositório de certificados. Por padrão, esta tela é apresentada com a marcação em destaque. Sugerimos que esta não seja alterada.

![Imagem 4: Passo 4 – Clicando-se em “Avançar”, será aberta a tela para seleção do repositório de certificados. Por padrão, esta…](https://ajuda.sankhya.com.br/hc/article_attachments/20653723819031)

**Passo 5** – Depois de clicar-se em “**Avançar**”, será aberta uma última tela, apresentando as configurações especificadas durante o processo de importação do certificado. Para finalizar, clica-se em “**Concluir**”.

![Imagem 5: Passo 5 – Depois de clicar-se em “ Avançar ”, será aberta uma última tela, apresentando as configurações especificadas…](https://ajuda.sankhya.com.br/hc/article_attachments/20653711414295)

- **Exportação**

Finalizado o processo de Importação do Certificado Digital, realiza-se a Exportação do mesmo para a máquina.

**Passo 1 –** Para início do processo de exportação, clica-se em "**Iniciar > Painel de Controle > Opções da Internet**"; neste momento será aberta a seguinte tela:

![Imagem 6: Passo 1 – Para início do processo de exportação, clica-se em " Iniciar > Painel de Controle > Opções da Internet ";…](https://ajuda.sankhya.com.br/hc/article_attachments/20653711423255)

Em seguida, clica-se na aba "**Conteúdo > botão Certificados**". Será aberta a seguinte tela, onde deve-se clicar no botão “**Exportar**”.

![Imagem 7: Em seguida, clica-se na aba " Conteúdo > botão Certificados ". Será aberta a seguinte tela, onde deve-se clicar no…](https://ajuda.sankhya.com.br/hc/article_attachments/20667867708439)

**Passo 2** – Depois de acionado o botão de exportação citado acima, será aberta a tela correspondente ao Assistente de Exportação de Certificados, onde será dado início no processo de exportação do arquivo, clicando-se em “**Avançar**”.

![Imagem 8: Passo 2 – Depois de acionado o botão de exportação citado acima, será aberta a tela correspondente ao Assistente de…](https://ajuda.sankhya.com.br/hc/article_attachments/20653711458711)

**Passo 3** – Feito isso, será aberta a tela questionando sobre a exportação da chave privada juntamente com o certificado.

**Importante**:

É essencial que a marcação em destaque neste passo, seja mantida.

![Imagem 9: É essencial que a marcação em destaque neste passo, seja mantida.](https://ajuda.sankhya.com.br/hc/article_attachments/20667834748311)

**Passo 4** – Depois de clicar-se em “Avançar”, a tela que se abrirá a seguir, é primordial para sucesso no procedimento de geração da cadeia completa dos certificados digitais.

**Importante**:

A marcação em destaque, deve ser realizada para êxito final no processo.

![Imagem 10: A marcação em destaque, deve ser realizada para êxito final no processo.](https://ajuda.sankhya.com.br/hc/article_attachments/20667834753687)

**Passo 5** – Efetuada a marcação mencionada acima, e clicando-se em “**Avançar**”, será aberta a tela, onde informa-se a senha de Exportação do certificado digital.

**Importante:**

A senha informada nos campos a seguir, não é a senha passada pelo órgão emissor no momento da aquisição do certificado. Esta é uma nova senha digitada pelo próprio usuário na execução deste passo.

![Imagem 11: A senha informada nos campos a seguir, não é a senha passada pelo órgão emissor no momento da aquisição do certificado.…](https://ajuda.sankhya.com.br/hc/article_attachments/20667834755607)

**Passo 6** – Informada a senha, clica-se em “**Avançar**”, onde será aberta a tela para especificação do nome do certificado que se deseja exportar.

Sugerimos aqui, que seja feita a utilização de um nome que facilite a identificação do certificado, de modo que se entenda também que o arquivo, passou pelo processo de “Geração de Cadeia Completa de Certificados”, por exemplo, “**CadeiaComplNomeDaEmpresa**”.

![Imagem 12: Sugerimos aqui, que seja feita a utilização de um nome que facilite a identificação do certificado, de modo que se…](https://ajuda.sankhya.com.br/hc/article_attachments/20667834767511)

**Passo 7** – Definido e informado o nome do certificado, clica-se em “**Avançar**”, onde serão apresentadas as configurações especificadas durante o processo de exportação do certificado, onde clica-se em “**Concluir**”.

![Imagem 13: Passo 7 – Definido e informado o nome do certificado, clica-se em “ Avançar ”, onde serão apresentadas as configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/20667834773655)

**Passo 8** – Feito isso, será apresentada a seguinte tela de aviso de sucesso no procedimento:

![Imagem 14: Passo 8 – Feito isso, será apresentada a seguinte tela de aviso de sucesso no procedimento:](https://ajuda.sankhya.com.br/hc/article_attachments/20667867732503)

- **SanNFe**

Finalizados os processos de Importação e Exportação do certificado, realiza-se a inserção deste no SanNFe. Depois que este for inserido no SanNFe, deve-se atentar para as seguintes situações, que irá caracterizar ou não, o sucesso do procedimento de geração da cadeia completa.

Clicando-se no ícone ![Imagem 15: Clicando-se no ícone será aberta a Tela 1 , que caracteriza que o processo não foi realizado com êxito, ou seja, o…](https://ajuda.sankhya.com.br/hc/article_attachments/20667867736727) será aberta a **Tela 1**, que caracteriza que o processo não foi realizado com êxito, ou seja, o certificado não possui a cadeia completa. Observe que é apresentado apenas o certificado, sem nenhuma informação precedente.

Clicando-se no mesmo ícone citado acima, e sendo aberta a **Tela 2,** está caracterizado o sucesso no procedimento, ou seja, o arquivo possui a cadeia completa.

- **Os principais erros que podem ser resolvidos, com esta documentação, seria:**

Erro na validação do EFD-Reinf:

**Erro MS0003-Erro na cadeia do certificado digital do signatário ou do solicitante da informação.**

Erro Rejeição de NF-e:

**293-Rejeição: Certificado Assinatura - erro Cadeia de Certificação.**
