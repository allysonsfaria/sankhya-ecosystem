---
id: "37319322334615"
titulo: "Erro 404: \"O path solicitado não existe\" em integrações via API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37319322334615-Erro-404-O-path-solicitado-n%C3%A3o-existe-em-integra%C3%A7%C3%B5es-via-API"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-13T01:57:01Z"
rotulos: ["Atualização", "Integração", "API", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Erro 404", "Requisitos específicos de sistema", "Documentação do endpoint", "Validação Técnica", "Limpeza e Reexecução de Módulos", "Servidor de aplicação não localiza recurso ou serviço solicitado", "Artigo atualizado KCS", "Plataforma - KCS", "Deploy"]
---

# Erro 404: "O path solicitado não existe" em integrações via API

**Mensagem**

{ "statusCode": 404, "error": { "code": "NOT\_FOUND", "message": "Item não encontrado!", "details": "O path solicitado não existe!" } }

![Imagem 1: { "statusCode": 404, "error": { "code": "NOT_FOUND", "message": "Item não encontrado!", "details": "O path solicitado…](https://ajuda.sankhya.com.br/hc/article_attachments/37319322323863)

**Situação**

Ao enviar uma requisição para um endpoint da API do Sankhya Om (por exemplo, em uma integração via Gateway), o retorno é o erro 404 acima, com o detalhe **"O path solicitado não existe!"**. Ou seja, o endereço (path) chamado não foi encontrado.

**Observação:** a API também retorna 404 quando um registro não existe (por exemplo, um código de produto inexistente). Este artigo trata apenas do caso em que o detalhe é "O path solicitado não existe!".

**Solução**

(1)** Verificação de Pré-Requisitos e Documentação**

Alguns recursos de integração possuem **requisitos específicos de sistema** para funcionarem corretamente. Dessa forma, recomenda-se seguir os passos abaixo:

- **Consulte a documentação do endpoint**
  Antes de qualquer ação, verifique na **página do endpoint**, no [**Portal do Desenvolvedor Sankhya**](https://developer.sankhya.com.br/reference), se existe uma **versão mínima do sistema** exigida para utilização do serviço (por exemplo: "disponível a partir da versão 4.31").
- **Confira o endereço da requisição**
  Compare a URL e o método (GET, POST etc.) usados na integração com os informados na página do endpoint, e confirme se o endereço é o do ambiente correto (produção ou sandbox). Um path digitado errado também gera esse erro.
- **Valide o ambiente**
  Confirme se a versão atual do seu sistema é compatível com os requisitos informados na documentação do endpoint utilizado.
- **Atualização do sistema**
  Caso o recurso esteja disponível apenas em versões superiores à instalada, avalie a **atualização do sistema**, garantindo que todos os serviços e componentes de comunicação estejam disponíveis e atualizados.

(2)** Limpeza e Reexecução de Módulos (Deploy)**

Caso a versão do sistema já seja compatível e o erro persista, pode haver um **problema no carregamento dos serviços** no servidor de aplicação.

**Importante:** os passos abaixo são feitos diretamente no servidor e devem ser executados pela equipe de TI ou de infraestrutura responsável por ele. Se o servidor for hospedado pela Sankhya, abra um chamado para que a equipe responsável faça o procedimento.

Siga os passos abaixo:

- Acesse a pasta **deployments** , dentro do diretório de instalação do servidor de aplicação (exemplo: `/home/mgeweb/wildfly/standalone/deployments`).
- Localize arquivos relacionados à API ou serviço em questão com a extensão **.failed**.
- Exclua **somente** o arquivo **.failed**. Não exclua o arquivo **.ear** nem arquivos **.deployed**: excluir um .deployed desliga o módulo correspondente.
- Reinicie o servidor de aplicação para que o deploy seja executado novamente.

(3)** Validação Técnica**

Após o reinício do servidor, realize as seguintes validações:

- Verifique se os arquivos na pasta **deployments** foram recriados com a extensão **.deployed**.
- Confirme se a **data e hora de modificação** desses arquivos correspondem ao momento do reinício do servidor.
- Caso o módulo volte a apresentar o estado **.failed**, será necessário analisar os **logs do servidor de aplicação** para identificar o erro técnico ocorrido durante o carregamento do serviço.

**Causa**

Esse erro ocorre quando o **servidor de aplicação não consegue localizar o recurso ou serviço solicitado** na requisição. As principais causas são:

- **Endereço da requisição incorreto**
  O path ou o método usado não corresponde ao informado na documentação do endpoint.
- **Versão do sistema**
  O ambiente está em uma versão que ainda não contempla o recurso ou micromódulo utilizado na integração.
- **Falha no deploy**
  O arquivo responsável por disponibilizar o serviço (extensão **.ear**) não foi carregado corretamente pelo servidor de aplicação.
- **Arquivos de falha no servidor**

Quando o carregamento falha, o servidor cria um arquivo com a extensão **.failed** na pasta **deployments**. Enquanto esse arquivo existir, o servidor não tenta carregar o serviço novamente, e o recurso continua indisponível.
