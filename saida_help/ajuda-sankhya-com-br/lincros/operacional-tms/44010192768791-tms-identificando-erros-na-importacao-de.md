---
id: "44010192768791"
titulo: "[TMS] - Identificando erros na importação de EDI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010192768791--TMS-Identificando-erros-na-importa%C3%A7%C3%A3o-de-EDI"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:32:05Z"
rotulos: ["sync_hc", "lincros", "lincros_13433429", "sync_hash_914aaf9e087e"]
---

# [TMS] - Identificando erros na importação de EDI

**Menu**: Operacional > Importação > EDI > Log

**Objetivo**: Identificar o erro ou motivo que ocasionou a não importação do arquivo de EDI

**Considerações**:

- Possuir arquivos de EDI importados com erros no sistema;

## Identificando o erro na importação de EDI

Todos os arquivos importados para o TMS geram informações de logs que ficam armazenadas na plataforma. Essas informações nos auxiliam a identificar erros e motivos que levaram esses arquivos a não serem importados.

Na imagem abaixo podemos ver que alguns arquivos estão com um ícone vermelho com um 'X' e o outros com um ícone verde e com um sinal de check;

![Imagem 1: Na imagem abaixo podemos ver que alguns arquivos estão com um ícone vermelho com um 'X' e o outros com um ícone verde e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010193025175)

1. O ícone vermelho quer dizer que houve erro na importação e o verde indica que foi importado com sucesso;
2. Para entender o porque houve erro na importação, basta clicar no código da linha que está em vermelho;
3. Irá abrir uma tela com as informações da importação e na aba 'Erro' poderemos identificar o que de fato ocorreu;

   ![Imagem 2: Irá abrir uma tela com as informações da importação e na aba 'Erro' poderemos identificar o que de fato ocorreu;](https://ajuda.sankhya.com.br/hc/article_attachments/44010212176535)

Nela estará informando o motivo do erro. Neste caso estamos importando um arquivo de Ocorrência, ou seja, um OCORREN;

O motivo apresentado é que a nota fiscal já possui uma ocorrência com a ação finalizadora e por isso não pode mais receber outra ocorrência com a mesma ação, ou seja, a nota já recebeu a ocorrência '01 - Entregue', por exemplo, e está sendo importado novamente um arquivo com a mesma ocorrência '01 - Entregue' para a mesma nota.

Já a mensagem de que o conhecimento não foi localizado com a transportadora X para determinado documento, significa que a nota fiscal não está com a mesma transportadora que se refere o arquivo OCORREN. Nesse caso, é necessário entender se de fato na nota a transportadora está incorreta e ajustar conforme CNPJ do arquivo.

![Imagem 3: Já a mensagem de que o conhecimento não foi localizado com a transportadora X para determinado documento, significa que…](https://ajuda.sankhya.com.br/hc/article_attachments/44010167795223)

Outro erro de importação para ser tratado é a mensagem 'Transportadora X sem padrão EDI definido' no momento da importação de um EDI no menu: Operacional > Importação > EDI > Importação.

![Imagem 4: Outro erro de importação para ser tratado é a mensagem 'Transportadora X sem padrão EDI definido' no momento da…](https://ajuda.sankhya.com.br/hc/article_attachments/44010181094295)

Para corrigir essa mensagem, basta acessar o menu Cadastro gerais > Transportadoras > Transportadora (empresa), buscar a transportadora em questão acessando pelo código da mesma, e no campo 'EDI Padrão' preencher com o EDI utilizado, seja o 3.0, 3.1 ou 5.0.

![Imagem 5: Para corrigir essa mensagem, basta acessar o menu Cadastro gerais > Transportadoras > Transportadora (empresa), buscar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010151677847)

![Imagem 6: Para corrigir essa mensagem, basta acessar o menu Cadastro gerais > Transportadoras > Transportadora (empresa), buscar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010151795223)

O erro abaixo, se trata da importação de um CONEMB quando na verdade já houve a importação do XML do CT-e. A importação do XML cria o CT-e com chave de acesso, tratando-se de um documento eletrônico com validação no site da Sefaz, já a importação do CONEMB realiza a criação do CT-e no sistema sem chave de acesso e validação na Sefaz.

O erro nada mais é do que um aviso de que já foi importado o XML antes do CONEMB e por isso o sistema não processa o arquivo.

Ressaltamos que o ideal é a utilização de somente uma das formas de criação de CT-e, onde uma exclui a necessidade de importação da outra.

![Imagem 7: Ressaltamos que o ideal é a utilização de somente uma das formas de criação de CT-e, onde uma exclui a necessidade de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010151934359)

O erro abaixo referente a não localização de nota fiscal, significa que houve a importação de um OCORREN para vincular uma ocorrência a uma nota existente no sistema, porém o XML da nota ainda não foi importado, portanto, basta importar o XML da nota e processar/importar novamente o OCORREN.

![Imagem 8: O erro abaixo referente a não localização de nota fiscal, significa que houve a importação de um OCORREN para vincular…](https://ajuda.sankhya.com.br/hc/article_attachments/44010152122519)

Já o erro abaixo se refere a importação de um EDI DOCCOB, o qual é responsável pela criação de faturas no sistema.

No momento que um CT-e já está vinculado a uma fatura, ele não pode ser utilizado em outra sem antes remover o vínculo da fatura atual.

A mensagem informada se trata de um aviso, de que o CT-e X já está vinculado a determinada fatura, dessa forma o sistema barra a importação para não gerar duplicidade de informações.

![Imagem 9: A mensagem informada se trata de um aviso, de que o CT-e X já está vinculado a determinada fatura, dessa forma o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010152290455)

O erro abaixo também de refere ao EDI DOCCOB, o qual foi importado com determinados CT-es informados, porém esses CT-es não estão importados no sistema para gerar a fatura.

Dessa forma, basta importar o XML do CT-e ou criá-lo a partir do CONEMB e reprocessar/importar o DOCCOB novamente.

![Imagem 10: Dessa forma, basta importar o XML do CT-e ou criá-lo a partir do CONEMB e reprocessar/importar o DOCCOB novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/44010168967319)

**CT-e complementar pendente sem vínculo:** se o erro envolve um CT-e do tipo Complementar, verifique se o CT-e original (ao qual o complementar se refere) já está importado no sistema. O CT-e complementar depende do original já estar presente para conseguir localizar a referência e concluir o vínculo automaticamente. Se o complementar for importado antes do original, o sistema não encontra essa referência e gera a pendência. Para corrigir: garanta que o CT-e original seja importado primeiro e, em seguida, reprocesse ou reimporte o complementar.

Uma vez identificado o erro, basta tomar as ações necessárias para a correção da pendência e reprocessar o arquivo, ou até mesmo importar novamente se for o caso.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
