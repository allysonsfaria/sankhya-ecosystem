---
id: "11244652964119"
titulo: "Camada de autorização para API"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-12T21:35:42Z"
rotulos: ["Configuração", "Segurança", "Portal de Vendas", "Financeiro", "API", "Implementação da Camada de Autorização para API no Sankhya Om"]
---

# Camada de autorização para API

```
 ![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310448872215) Versão disponível: A partir da 4.16
```

---

O **Sankhya Om** possui uma API que permite sua integração com outras aplicações. 

O funcionamento básico desta API consiste em logar na plataforma com um usuário válido, e, em seguida, realizar a chamada de um serviço que efetuará uma determinada ação no **Sankhya Om** como, por exemplo, a inserção de um registro ou consulta de dados.

Visando aumentar a segurança neste cenário, criamos a camada de autorização para API (Authorization Layer), que permite ao usuário responsável pela nossa plataforma de ERP, delimitar o acesso de seus serviços a partir de integrações via API, ou seja, além da necessidade de possuir um usuário válido e realizar sua autenticação, as aplicações integradas à plataforma **Sankhya Om** precisaram possuir autorização para consumir determinado serviço da plataforma Sankhya.

Por exemplo, é de interesse que ocorra a integração para a inclusão de pedidos no **Sankhya Om**. Para isso, além das credenciais de acesso que devem ser compartilhadas, o usuário que será utilizado na integração deverá receber acesso à tela [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654).

Trataremos neste artigo os seguintes tópicos:

- [Configurações necessárias](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API#Configura%C3%A7%C3%B5esnecess%C3%A1rias)
- [Utilização](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API#Utiliza%C3%A7%C3%A3o)
- [Consulta de dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API#ConsultadeDados)

---

#### Configurações necessárias

**01- Propriedade da JVM**

No servidor de aplicação (Jboss/Wildfly), adicione a seguinte propriedade:

```
-Dsnk.authorization.layer.enable=true
```

Feito isso, você deve habilitá-la como uma propriedade da JVM no arquivo de configurações de inicialização do servidor de aplicação.

Vale lembrar que, para Wildfly esta configuração pode ser feita em três arquivos:

- /wildfly/bin/standalone.conf
- /wildfly/bin/standalone.conf.bat
- /wildfly/bin/standalone.bat

Confira na imagem abaixo um exemplo de configuração no arquivo standalone.bat.

![Imagem 2: Confira na imagem abaixo um exemplo de configuração no arquivo standalone.bat.](https://ajuda.sankhya.com.br/hc/article_attachments/11244812282903)

**Inclusão da propriedade no arquivo standalone.bat**

**02**- **Concessão de acesso**

Com o servidor de aplicação já em execução, agora iremos conceder a permissão de acesso aos serviços do **Sankhya Om** ao usuário que irá consumir a API de integração.

O primeiro passo para essa ação é a classificação do usuário que irá ser utilizado na integração, para isso acesse a tela [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874) e na aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), campo **"Tipo usuário"** deve-se classificar o usuário como **"Integração"**.

Na sequência, acesse a tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) e inclua a permissão ao usuário na tela cujo serviço a ser chamado é utilizado. Por exemplo, a liberação do acesso de consulta a tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753) para o consumo do serviço "DatasetSP.loadRecord" na entidade Financeiro (tabela TGFFIN).

![Imagem 3: Na sequência, acesse a tela Acessos e inclua a permissão ao usuário na tela cujo serviço a ser chamado é utilizado. Por…](https://ajuda.sankhya.com.br/hc/article_attachments/11245224438679)

**Concedendo acesso ao consumo de dados da entidade Financeiro (TGFFIN) a partir do serviço DatasetSP.loadRecord ao usuário Integração01.**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API#top)

#### Utilização

Com essa iniciativa não foi implementado alterações nas chamadas de serviços da API, o único ponto que passa a ser de suma importância é a concessão de acesso para o devido consumo e caso o usuário não receba a devida autorização, ao realizar a chamada receberá o retorno conforme demonstrado na imagem abaixo.

![Imagem 4: Com essa iniciativa não foi implementado alterações nas chamadas de serviços da API, o único ponto que passa a ser de…](https://ajuda.sankhya.com.br/hc/article_attachments/11245280626711)

**Utilização negada do serviço DatasetSP.loadRecords devido a falta de autorização**

![Imagem 5: Existe uma mudança em andamento referente a API de integração, porém, não possui relação com este recurso. Para mais…](https://ajuda.sankhya.com.br/hc/article_attachments/22189666315799) Existe uma mudança em andamento referente a API de integração, porém, não possui relação com este recurso. Para mais informações acesse o artigo [API de Serviços Gateway](https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API#top)

#### Consulta de dados

Pode-se gerir a consulta de dados direto na entidade por meio de uma view, o que o permitirá limitar o acesso para apenas as informações nessa aplicação.

Para realizar essa consulta, deve-se utilizar o serviço **"CRUDServiceProvider.loadView"** de forma que é preciso efetivar a requisição do login, e logo depois, do serviço da seguinte maneira:

```
curl --location 'https://api.sankhya.com.br/gateway/v1/mge/service.sbr?
serviceName=CRUDServiceProvider.loadView&outputType=json&preventTranform=false&globalID=B8
93D5559FFD17C20D29B9B20140EB1B' \
--header 'Content-Type: text/plain' \
--header 'Cookie: JSESSIONID=7ymCJoN_1mjPl9k5AACPaCB-HkFtLUjB1wiQvE0j' \
--data '{
    "serviceName": "CRUDServiceProvider.loadView",
    "requestBody": {
        "query": {
            "viewName": "[NOMEview]"
       }
    }
}'
```

![Imagem 6: A requisição pode conter filtros. Porém, dentro desse contexto a estrutura dessa forma atende o proposto.](https://ajuda.sankhya.com.br/hc/article_attachments/22189653138327) A requisição pode conter filtros. Porém, dentro desse contexto a estrutura dessa forma atende o proposto.

É necessário que o usuário do tipo integração possua acesso ao LoadView para a execução da chamada nesse serviço em ambientes em que a camada de autorização está ativa. O acesso a este recurso é concedido por meio da tela [Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854):

[GIF animado: Imagem 7: É necessário que o usuário do tipo integração possua acesso ao LoadView para a execução da chamada nesse serviço em…](https://ajuda.sankhya.com.br/hc/article_attachments/22189867175447)

Desse modo, caso não possua esse acesso, ao executar a requisição, o retorno abaixo será recebido:

**"O usuário logado não possui permissão para acessar a View."**

![Imagem 8: Pode-se verificar todas as views disponíveis por meio do caminho "Módulos > Configuração > View" .](https://ajuda.sankhya.com.br/hc/article_attachments/22189666351639) Pode-se verificar todas as views disponíveis por meio do caminho **"Módulos > Configuração > View"**.

---

![Imagem 9: Informações adicionais acerca da View:](https://ajuda.sankhya.com.br/hc/article_attachments/22189666360471)**Informações adicionais acerca da View:**

- A validação deve ocorrer apenas quando a camada de autorização estiver ativa, conforme abaixo:

```
                           -Dsnk.authorization.layer.enable=true
```

- Com a camada de autorização ativa e o valor do parâmetro **"AUTHLAYERVIEW"** false, será validado se o usuário possui a configuração **"Consultar"** do serviço LoadView e se sim, este terá acesso a todas as views criadas no ambiente.
- Caso o parâmetro AUTHLAYERVIEW seja alterado para true, deve-se verificar se o usuário possui acesso para realizar as consultas. Assim, caso tenha permissão apenas para **"Alterar"**, **"Excluir"**, **"Configurar"**, **"Numeração"** ou **"Filtro avançado"**, este não poderá consultar a view, ou seja, é necessário que a opção Consultar da tela de Acessos seja configurada para um usuário ou grupo de usuários.
- Se a View for configurada apenas no Banco de Dados, ou seja, não é exibida na tela de Acessos ou ainda, compartilhada quando requisitada via serviço, o usuário receberá a mensagem que este não possui permissão para o acesso.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/11244652964119-Camada-de-autoriza%C3%A7%C3%A3o-para-API#top)
