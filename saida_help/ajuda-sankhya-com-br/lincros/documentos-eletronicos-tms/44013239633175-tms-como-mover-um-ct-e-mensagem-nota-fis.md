---
id: "44013239633175"
titulo: "[TMS] - Como mover um CT-e - mensagem: Nota fiscal X não localizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013239633175--TMS-Como-mover-um-CT-e-mensagem-Nota-fiscal-X-n%C3%A3o-localizada"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:50:52Z"
rotulos: ["sync_hc", "lincros", "lincros_13432837", "sync_hash_c5ea7dfe60c9"]
---

# [TMS] - Como mover um CT-e - mensagem: Nota fiscal X não localizada

**Menu**: Documentos eletrônicos > CT-e

**Objetivo**: A opção Mover CT-e é utilizada para tratar erro de importação de CT-e.

**Considerações**:

- A situação de integração do CT-e precisa ser diferente de 'Integrado' ou 'Aguardando Integração';
- Uma vez que o CT-e esteja nestas situações, indica que está ocorrendo ou já ocorreu comunicação entre o TMS e o ERP para gravação do documento;
- A função de mover CT-e pode ser utilizada para tratar outros tipos de erro importação de CT-e, não necessariamente igual ao caso utilizado como exemplo. Para executar, basta possuir o número do pré-conhecimento para qual você deseja mover o CT-e;

## Funcionalidade

Tratar erro de importação de CT-e através do botão 'Mover CT-e', é utilizado quando o erro de importação não pode ser tratado com a reimportação do XML do CT-e.

Isso ocorre, por exemplo, quando a transportadora utiliza como identificador do documento transportado, apenas o número da NF-e, não a chave de acesso.

![Imagem 1: Isso ocorre, por exemplo, quando a transportadora utiliza como identificador do documento transportado, apenas o número…](https://ajuda.sankhya.com.br/hc/article_attachments/44013179121687)

Nesse caso, mesmo importando o CT-e, o Sistema não encontrará a nota fiscal  para realizar o vínculo, pois a busca é realizada através da chave de acesso.

Sendo assim, identificando a nota fiscal no Sistema, é possível mover o CT-e para o pré-conhecimento da Nota Fiscal.

## Movendo o CT-e

1. Acesse o CT-e com o erro, através do menu: Documentos eletrônicos > CT-e;

![Imagem 2: 1. Acesse o CT-e com o erro, através do menu: Documentos eletrônicos > CT-e;](https://ajuda.sankhya.com.br/hc/article_attachments/44013210031383)

2. Clicando no número do CT-e, identificar o número da nota fiscal referenciada (buscar no campo de informações de importação);

![Imagem 3: 2. Clicando no número do CT-e, identificar o número da nota fiscal referenciada (buscar no campo de informações de…](https://ajuda.sankhya.com.br/hc/article_attachments/44013240021783)

3. Acesse o menu Documentos eletrônicos > NF-es, e pesquise pela nota fiscal mencionada no CT-e.

Clicando no número da Nota fiscal, acesse a aba 'Conhecimentos' e copie o número do Pré-conhecimento para qual deseja mover o Ct-e;

![Imagem 4: Clicando no número da Nota fiscal, acesse a aba 'Conhecimentos' e copie o número do Pré-conhecimento para qual deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/44013193949463)

4. Acesse novamente o CT-e, e clique no botão 'Mover CT-e';

![Imagem 5: 4. Acesse novamente o CT-e, e clique no botão 'Mover CT-e';](https://ajuda.sankhya.com.br/hc/article_attachments/44013202074007)

 5. Irá abrir uma nova janela, após, selecione a opção 'mover para outro conhecimento' e insira o número do pré-conhecimento copiado no passo anterior;

![Imagem 6: 5. Irá abrir uma nova janela, após, selecione a opção 'mover para outro conhecimento' e insira o número do…](https://ajuda.sankhya.com.br/hc/article_attachments/44013240329239)

6. Após, clique em 'Confirmar';

7. O CT-e será movido com sucesso para o Pré-conhecimento selecionado, e o erro de importação será corrigido;

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
