---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/config"
titulo: "Uma publicação com a etiqueta \"config\""
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/config"
trilha: "Blog > Tags > Config"
---

# Uma publicação com a etiqueta "config"

## [Como utilizar o Feature Manager](https://gilded-nasturtium-6b64dd.netlify.app/blog/como-utilizar-feature-manager)

3 de junho de 2024 · 6 min para ler

Thiago Oliveira

Developer

![Victor Uehara](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/VictorUehara.png)

Victor Uehara

Developer

## Introdução

Para solucionar a necessidade de introduzir novas funcionalidades de maneira iterativa e controlada nas aplicações,
foi criado o Feature Manager. Que permite utilizar feature flags, também conhecidas como toggles ou switches,
isso permite aos interessados ativar ou desativar determinadas características da aplicação,
oferecendo uma abordagem flexível para testes, experimentação e liberação gradual de novas funcionalidades.
Essa prática contribui para um desenvolvimento mais ágil, possibilitando a implementação incremental de recursos e
a coleta de feedback valioso antes de uma liberação completa.

## FeatureManagerFactory

A classe FeatureManagerFactory é responsável por conectar-se a um serviço de gerenciamento de recursos (feature manager)
e facilitar o acesso a funcionalidades e configurações dinâmicas.

O construtor dessa classe recebe um objeto para instanciar as informações do serviço, como a chave da API, contexto do usuário e o serviço,
podendo ser uma depedência ou biblioteca que fará as requisições e retornará as informações, por padrão há um conector default que é o Statsig.

```
constructor({ context, apiKey, service }: FeatureManagerFactoryProps)
```

## IFeatureManagerService

Interface disponível para implementação dos serviços a serem utilizados e injeção dos conectores:

Exemplo de implementação - TypeScript:

```
import { FlagsmithConnector } from "../adapters/connectors";
import { IDynamicConfig } from "../interfaces/IDynamicConfig";
import { IEnvironmentContext } from "../interfaces/IEnvironmentContext";
import { IFeatureManagerService } from "../interfaces/IFeatureManagerService";

export class FlagsmithFeatureManagerService implements IFeatureManagerService {
    connectorInstance: FlagsmithConnector;

    constructor(ctx: IEnvironmentContext, apiKey: string) {
        this.connectorInstance = new FlagsmithConnector(ctx, apiKey);
    }

    isFeatureActive(featureName: string): Promise<boolean> {
        return this.connectorInstance.fetchIsFeatureActive(featureName);
    }

    getConfig(configName: string, defaultValue?: any): Promise<IDynamicConfig | any> {
        return this.connectorInstance.fetchConfig(configName, defaultValue);
    }
}
```

Exemplo de Conector customizado - TypeScript:

```
import IFeatureManagerConnector from "@sankhya-frontend/feature-manager/src/interfaces/IFeatureManagerConnector";
import { IEnvironmentContext } from "@sankhya-frontend/feature-manager/src/interfaces/IEnvironmentContext";
import { HttpClient, httpClient, HttpClientResponse } from "@sankhya-frontend/feature-manager/src/lib/http-client";
import { ConfigPayload, ConfigResponse, FeatureGatePayload, FeatureGateResponse } from "./interface";
import { IDynamicConfig } from "@sankhya-frontend/feature-manager/src/interfaces/IDynamicConfig";

export class FlagsmithConnector implements IFeatureManagerConnector {
    private httpClient: HttpClient;
    context: IEnvironmentContext;
    apiKey: string;

    constructor(ctx: IEnvironmentContext, apiKey: string) {
        this.context = ctx;
        this.apiKey = apiKey;

        this.httpClient = httpClient({
            //http client params for Flagsmith
        });
    }

    private getUserContext(ctx: IEnvironmentContext = this.context) {
        return {
            //get user context specific for Flagsmith
        }
    }

    async fetchIsFeatureActive(featureName: string): Promise<boolean> {

        const response = await this.httpClient.request<unknown, HttpClientResponse<FeatureGateResponse>, FeatureGatePayload>({
            //payload for fetching Flagsmith feature gate
        });

        const hasActiveFeature = response?.data?.value || false;

        return Promise.resolve(hasActiveFeature)
    }

    async fetchConfig(configName: string, defaultValue?: any): Promise<IDynamicConfig | any> {
        const response = await this.httpClient.request<unknown, HttpClientResponse<ConfigResponse>, ConfigPayload>({
            //payload for fetching Flagsmith dynamic config
        });

        if (response?.data?.value != undefined) return response.data.value;
        return defaultValue;
    }
}
```

## Implementação

Existem algumas formas de se utilizar o Sankhya Feature Manager dependendo do contexto. Atualmente temos os seguintes usos:

- Utilização dentro do SankhyaW;
- Utilização em projeto JAVA externo ao SankhyaW (micro-modules ou micro-services);
- Utilização em projeto TypeScript externo ao SankhyaW (micro-modules ou micro-services);

---

### Utilização dentro do SankhyaW

Podemos lançar mão do utilitário
[FeatureManagerUtils](https://gitlab.sankhya.com.br/erp/sankhyaw/-/blob/4.28-DEV/MGE-Modelcore/src/br/com/sankhya/modelcore/featuremanager/FeatureManagerUtils.java)
que facilita e resolve o uso do Statsig pela biblioteca
[sankhya-feature-manager](https://gitlab.sankhya.com.br/erp/libraries/sankhya-feature-manager)
dentro do SankhyaW.

#### FeatureManagerUtils

O FeatureManagerUtils possui um sistema de cache implementado que garante maior estabilidade no gerenciamento de flags e menor
dependência do serviço terceiro. Com isso é possível ter resiliência na comunicação de forma que a última configuração válida é utilizada
em caso de falha de comunicação.

#### Referência de API

| Método Descrição Tipo do retorno| `isFeatureActive()` Retorna valor em cache ou se existe um feature gate com o nome e resourceID ativo no Statsig. boolean| `fetchConfig()` Retorna valor em cache ou da DynamicConfig com nome e resourceID no Statsig. DynamicConfig| `getfeatureManagerService()` Retorna uma promessa que será resolvida com a instância atual de `IFeatureManagerService`. IFeatureManagerService| `clearCache()` Limpa cache do contexto atual, possibilitando uma nova busca de informações do Statsig. void| `getEnvironmentContext()` Preenche dados do contexto necessários para a comunicação com Statsig. EnvironmentContext| `buildEnvironmentVariables()` Retorna um Map com as variaveis de ambiente obtidas pelo contexto e informações do sistema. `Map<String, String\>` | | | | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

---

### Utilização em projeto JAVA externo ao SankhyaW

#### Importação do projeto

Adicionar a importação do projeto no gradle.dependencies:

```
implementation "br.com.sankhya.graphql:sankhya-feature-manager:master"

#### Utilização

 - Obter o apiKey e userID da conta no Statsig;
 - Criar uma instância do EnvironmentContext setando o userID;
 - Criar uma instância do FeatureManagerFactory passando o EnvironmentContext e apiKey obrigatórios (new FeatureManagerFactory(environmentContext, apiKey));
 - Fazer a chamada dos métodos através do FeatureManagerService obtido por meio do "getInstance" no factory;

#### Obtendo a instância do service
```java
IFeatureManagerService featureManagerService = new FeatureManagerFactory(environmentContext, apiKey).getInstance();

#### Verificando se a feature flag está ativa
```java
featureManagerService.isFeatureActive(featureName);

#### Obtendo a configuração dinâmica do cliente
```java
featureManagerService.getConfig(configName);
#### Propriedades do context
```java
    String userID;
	String userName;
	String partnerName;
	String sysVersion;
	String environment;
	String clientGaId;
	String appName;
	String moduleVersion;
	String resourceID;
	String environmentTier = "production";
	String originalResourceID;

#### Referência de API

FeatureManagerFactory

| Método                       | Descrição                                                                                       |Tipo do retorno       |
|------------------------------|-------------------------------------------------------------------------------------------------|----------------------|
| `FeatureManagerFactory()`    | Cria uma nova instância do FeatureManagerFactory utilizando o serviço padrão (Statsig).         |---               |
| `getInstance()`              | Cria e/ou retorna uma instância do Service utilizado.                                           |IFeatureManagerService|

(IFeatureManagerService) FeatureManagerFactory.getInstance()

| Método                       | Descrição                                                                                       |Tipo do retorno       |
|------------------------------|-------------------------------------------------------------------------------------------------|----------------------|
| `isFeatureActive()`          | Retorna se existe um feature gate ativo com o nome especificado no Statsig.                     |boolean               |
| `getConfig()`                | Retorna valor da DynamicConfig com nome especificado no Statsig.                                |DynamicConfig         |
| `setTimeout()`               | Configura tempo de espera máximo pela resposta do Statsig.                                      |void                  |

_________________________________________________________________________________________________________________________________________________________

### Utilização em projeto TypeScript externo ao SankhyaW

Para implementação da ferramenta é necessário instalar a depedência no projeto, isso pode ser feito de 2 maneiras:

Via NPM (Node Package Manager) Adicionando no arquivo `.npmrc` o seguinte registro:
```

@sankhya-frontend:registry=<https://maven.sankhya.com.br/repository/npm-releases>

```
E após executar o comando abaixo:

```bash
npm i @sankhya-frontend/feature-manager
```

Também é possível importar o script global acessando o [link](https://maven.sankhya.com.br/#browse/browse:npm-releases:%40sankhya-frontend%2Ffeature-manager).
Escolha uma versão e faça o download do pacote. Depois, extraia a pasta `dist` e a importe no seu projeto.

```
<script type="module" src="/dist/sankhya-featuremanager.js"></script>
```

Após a instalação é necessário importar os modulos na aplicação, podendo ser feito da seguinte forma:

```
import { useEffect, useState } from "react";
import { FeatureManagerFactory } from "@sankhya-frontend/feature-manager";

export default function MyApp() {

    const [featureManager, setFeatureManager] = useState();
    const [featureManagerService, setFeatureManagerService] = useState();

    useEffect(() => {
        const myFeatureManager = new FeatureManagerFactory({
            context: {
                userID: "1";
                userName: "USER";
                partnerName: "PARCEIRO 1";
                sysVersion: "4.27b105";
                environment: "TESTE";
                clientGaId: "Chave_SAS_do_Parceiro";
                appName: "Movimentação Financeira";
                contractDate: "2024/05/29";
                resourceID: "br.com.sankhya.fin.cad.movimentacaoFinanceira";
                environmentTier: "production";
                moduleVersion: "1.12.1";
            },
            apiKey: '<API_CONNECTOR_TOKEN>'
        });
        setFeatureManager(myFeatureManager);

    }, [featureManager]);

    if (featureManager) {
        setFeatureManagerService(await featureManager.getfeatureManagerService())
        await featureManagerService.isFeatureActive('my_feature_name').then(()=>{
            //do something
        });
    }
}
```

Ou da seguinte forma:

```
<script type="module">
    (async function () {
        window.fm = new FeatureManagerFactory(myFeatureManegerProps);

        await fm.getfeatureManagerService().then(async featureManagerservice => {
            await featureManagerservice.isFeatureActive('my_feature_name').then(()=>{
                //do something
            })
        });
    })()
</script>
```

#### Referência de API

FeatureManagerFactory

| Método Descrição Tipo do retorno| `constructor()` Cria uma nova instância do FeatureManagerFactory. ---| `getfeatureManagerService()` Retorna instância do Service utilizado. IFeatureManagerService | | | | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

(IFeatureManagerService) FeatureManagerFactory.getfeatureManagerService()

| Método Descrição Tipo do retorno| `isFeatureActive()` Retorna se existe um feature gate ativo com o nome especificado no Statsig. boolean| `getConfig()` Retorna o valor da DynamicConfig com nome especificado no Statsig. DynamicConfig | | | | --- | --- | --- | | | | | --- | --- | --- | --- | --- | --- | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
