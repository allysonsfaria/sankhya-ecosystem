---
id: "24163290261911"
titulo: "Como instalar/atualizar um SOP?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24163290261911-Como-instalar-atualizar-um-SOP"
trilha: "Sankhya Official Pack - SOP > SOP"
atualizado_em: "2026-07-22T14:47:31Z"
rotulos: ["Produtos", "Configuração", "Atualização", "Sankhya Place", "Extensões"]
---

# Como instalar/atualizar um SOP?

**Os SOPs são distribuídos na loja de soluções do Sankhya Place**.

Veja mais detalhes em:

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=8BXN0apRmIY)

## Ambiente Linux

Para realizar a instalação ou atualização das extensões no Sankhya inicialmente precisa **copiar o arquivo da extensão ( .ext ) para o diretório de extensões** que fica no servidor onde está o wildfly do cliente, caso já exista, deve substituir o arquivo.

Para o ambiente de produção no linux, o **diretório padrão é:**
/home/mgeweb/sankhyaW\_gerenciador\_de\_pacotes/extensions/wildfly\_producao

**Para realizar a transferência do arquivo pode ser utilizado o winscp, filezilla** e copiar o arquivo para o diretório acima, caso seja uma atualização o arquivo deve ser substituído, apenas renomear o arquivo vai trazer erros durante a atualização.

A transferência do arquivo deve ser feita com o **usuário mgeweb**.

Após a transferência, **logar utilizando o putty com o usuário mgeweb e executar os comandos:**

**"killprod" para parar o servidor de produção.**
**"pkg" para abrir o gerenciador de pacotes**

![Imagem 1: "killprod" para parar o servidor de produção. "pkg" para abrir o gerenciador de pacotes](https://ajuda.sankhya.com.br/hc/article_attachments/24339068907031)

usar a **opção [2]** para selecionar o servidor

![Imagem 2: usar a opção (2) para selecionar o servidor](https://ajuda.sankhya.com.br/hc/article_attachments/24339045689623)

Selecionar o **[1]** para servidor de produção

![Imagem 3: Selecionar o (1) para servidor de produção](https://ajuda.sankhya.com.br/hc/article_attachments/24339045697559)

Selecionar a **opção [13]** - tanto para instalar quanto para atualizar as extensões

**A rotina vai executar a instalação ou atualização de todos os arquivos de extensão que estiverem no diretório de extensões** e no final apresentar a mensagem extensão instalada com sucesso.

Selecione a opção [14] para voltar e depois [5] para sair do gerenciador de pacotes.

Usa o comando "jb\_startprod" para iniciar o servidor.

## Ambiente Windows

Para realizar a instalação ou atualização das extensões no Sankhya inicialmente **precisa copiar o arquivo da extensão ( .ext ) para o diretório de extensões** que fica no servidor onde está o wildfly do cliente, caso já exista, deve substituir o arquivo.

Para o ambiente de produção no Windows, o **diretório padrão é:**
C:\Sankhya\sankhyaW\_gerenciador\_de\_pacotes\extensions\Wildfly\_producao

![Imagem 4: Para o ambiente de produção no Windows, o diretório padrão é:…](https://ajuda.sankhya.com.br/hc/article_attachments/24339068957719)

![Imagem 5: Para o ambiente de produção no Windows, o diretório padrão é:…](https://ajuda.sankhya.com.br/hc/article_attachments/24339045711767)

Após a transferência, **procurar por “Serviços”** no menu Windows, abrir a tela.

Depois **localize e pare o serviço Wildfly Produção**.

![Imagem 6: Depois localize e pare o serviço Wildfly Produção .](https://ajuda.sankhya.com.br/hc/article_attachments/24339068965783)

![Imagem 7: Depois localize e pare o serviço Wildfly Produção .](https://ajuda.sankhya.com.br/hc/article_attachments/24339045717655)

Retorne ao **diretório do Gerenciador** de pacotes e execute o gerenciador de pacotes

![Imagem 8: Retorne ao diretório do Gerenciador de pacotes e execute o gerenciador de pacotes](https://ajuda.sankhya.com.br/hc/article_attachments/24339045720471)

Na tela do **gerenciador de pacotes, escolha a opção 2** para Selecionar o Servidor que será atualizado:

![Imagem 9: Na tela do gerenciador de pacotes, escolha a opção 2 para Selecionar o Servidor que será atualizado:](https://ajuda.sankhya.com.br/hc/article_attachments/24339045726871)

**Informe** **o número** de acordo com o **servidor** que será atualizado e d**epois escolha a opção 13** - ‘Instalar Extensões’, esta é utilizada para instalar e para atualizar as extensões.

![Imagem 10: Informe o número de acordo com o servidor que será atualizado e d epois escolha a opção 13 - ‘Instalar Extensões’, esta…](https://ajuda.sankhya.com.br/hc/article_attachments/24339068995351)

Ao final será apresentado a mensagem indicando que as extensões foram instaladas com sucesso.

![Imagem 11: Ao final será apresentado a mensagem indicando que as extensões foram instaladas com sucesso.](https://ajuda.sankhya.com.br/hc/article_attachments/24339045731991)

Volte ao Serviços do Windows e inicie o Wildfly novamente:

## Após o envio pela equipe Dev Center do link atualizado para instalação da extensão atualizada qual processo devo seguir?

### 1. Ativy (Wevy)

#### 1.1 Anexar o link da EXT atualizada enviada pelo time Dev Center.

#### 1.2 Na descrição, insira as seguintes informações:

**(1)** Remover a EXT (Nome da EXT enviada pelo time Dev Center) que estiver no servidor, mantendo as demais;
**(1)** Enviar a nova EXT para ser instalada no lugar da versão removida.

#### 1.3 Salvar e enviar.

Após seguir esse processo, a própria equipe da Ativy (Wevy) entrará em contato e realizará a instalação solicitada.

### 2. Sankhya Cloud

Para realizar a instalação da extensão, você precisará abrir um chamado pelo SaaS, seguindo o seguintes passo abaixo:

#### 2.1 Anexar no ticket o link da EXT atualizada enviada pelo time Dev Center.

#### 2.2 Na descrição, insira as seguintes informações:

**(1)** Por gentileza remover a EXT (Nome da EXT enviada pelo time Dev Center) que estiver no servidor, mantendo as demais e instalar a nova EXT em anexo para ser instalada no lugar da versão removida;

**(1)** (Inserir a data e horário programada para que o time do do Sankhya Cloud realize a instalação, pois esse processo irá gerar aproximadamente 20 minutos de indisponibilidade ao cliente.)

#### 2.3 Salvar e enviar.

Assim, a equipe do Sankhya Cloud realizará a instalação.

**Considerações Importantes:**

![Imagem 12: No ticket é obrigatório informar data e horário que o time do Sankhya Cloud poderá fazer a instalação, pois irá gerar…](https://ajuda.sankhya.com.br/hc/article_attachments/24339234611735) No ticket é obrigatório informar data e horário que o time do Sankhya Cloud poderá fazer a instalação, pois irá gerar aproximadamente 20 minutos de indisponibilidade ao cliente;
![Imagem 13: No ticket é obrigatório informar data e horário que o time do Sankhya Cloud poderá fazer a instalação, pois irá gerar…](https://ajuda.sankhya.com.br/hc/article_attachments/24339234613271) A abertura do ticket pode ser feita tanto pelo consultor ou pelo próprio cliente.

### 3. Datacom

Através do seu login na plataforma da Datacom, por favor, abra um ticket com as seguintes solicitações:

#### 3.1 Anexar o link da EXT atualizada enviada pelo time Dev Center.

#### 3.2 Na descrição, insira as seguintes informações:

**(1)** Remover a EXT (Nome da EXT enviada pelo time Dev Center) que estiver no servidor, mantendo as demais;

**(1)** Enviar a nova EXT para ser instalada no lugar da versão removida.

#### 3.3 Salvar e enviar.

Após seguir esse processo, a própria equipe da Datacom entrará em contato e realizará a instalação solicitada.

### 4. Sankhya Place (Apenas para extensões em EXTS)

Para atualizar o cliente é obrigatório estar nas versões abaixo do Sankhya. Assim deve:

4.26 (Gestão de Frotas e TMS)
4.27b60 (ImpEx)
4.24 (Demais SOP’s)

![Imagem 14: Acessar o Place;](https://ajuda.sankhya.com.br/hc/article_attachments/24339234611735) Acessar o Place;

![Imagem 15: Buscar pelo número do Pacote de atualização;](https://ajuda.sankhya.com.br/hc/article_attachments/24339234613271) Buscar pelo número do Pacote de atualização;

![Imagem 16: Clicar no botão Download;](https://ajuda.sankhya.com.br/hc/article_attachments/24339589292311) Clicar no botão Download;

![Imagem 17: O Place vai retornar uma mensagem informando que a instalação ocorreu com sucesso.](https://ajuda.sankhya.com.br/hc/article_attachments/24339549277079) O Place vai retornar uma mensagem informando que a instalação ocorreu com sucesso.

Para os demais datacenters não mencionados, o time do Dev Center disponibilizará o link da extensão com a versão mais atualizada. Se encontrar dificuldades durante o processo de instalação, solicitamos que entre em contato com o seu Gerente de Relacionamento, que poderá alocar um consultor da unidade para fornecer suporte na instalação.
