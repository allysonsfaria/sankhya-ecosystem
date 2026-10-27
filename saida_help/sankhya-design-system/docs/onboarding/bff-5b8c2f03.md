---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/onboarding/onboarding/bff/"
titulo: "Onboarding"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/onboarding/onboarding/bff/"
trilha: "Docs > Onboarding > Onboarding > Bff"
---

# Onboarding

## Criando novas telas utilizando o Design System

A primeira decisão que devemos tomar ao criar uma nova tela utilizando o Design System é onde criá-la.

Para podermos fazer entregas rápidas e independentes devemos partir da premissa que deve ser possível realizar atualizações a quente,
ou seja, devemos ter módulos desacoplados do monólito.
Para isso temos duas opções:

- Se o módulo que contém a tela já tiver um projeto desacoplado podemos criar a tela diretamente neste projeto;
- Se o módulo que contém a tela ainda estiver dentro do monólito, devemos solicitar a criação de um novo módulo BFF.

informação

Procure o Arquiteto da Squad para obter estas informações.

### O que é um BFF e quando usar?

Os BFFs são módulos de apoio ao Design System baseados na arquitetura
[BFF](https://medium.com/jeitosanar/backend-for-frontend-uma-estrat%C3%A9gia-sob-demanda-para-a-entrega-de-microsservi%C3%A7os-2f12d4cb9e3f)
(Backend for Frontend) que visam permitir atualizações a quente do front-end de módulos do sistema que ainda não foram desacoplados do monólito.

Sempre que formos criar uma tela que seu projeto base ainda se encontra dentro do monólito (Projeto SankhyaW), devemos solicitar que a equipe
da Quebra do Monólito realize e criação de um novo módulo BFF que será utilizado até que o módulo no monólito seja desacoplado.

![Diagrama de decisão sobre quando criar BFF](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/diagramModulesBFF-e3f3d48dfa1bdf493ae9253addd87db4.png)

## Como adicionar uma tela a um módulo separado do monólito?

Este processo se aplica tanto a módulos desacoplados quanto BFFs.

### 1 - Clonar projeto react-app-starter

Solicitar acesso ao projeto:

- [Projeto react-app-starter](https://gitlab.sankhya.com.br/dti/design-system/react-app-starter)

Clonar o repositório:

```
git clone https://gitlab.sankhya.com.br/dti/design-system/react-app-starter.git
```

### 2 - Copiar conteúdo do projeto react-app-starter para o diretório que irá conter a nova tela

Copiar o conteúdo da raiz do projeto

![Copiando react-app-starter para projeto](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/copy-73d14c491c370ba11e36316f397e2adf.png)

dica

Garanta que o arquivo .env suba para o repositório remoto, pois normalmente ele esta na lista de ignorados do .gitignore
![Arquivo dotEnv](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATAAAACCCAYAAADBjpQ5AAAQWElEQVR4Ae2bX2gbyR3HE659K7RwcA99sB7q/r9SeqXQyiBKAjlD2oeGEOrU1FzhYgwCw7kOCHNgYoibgjHGwQeuCTaoVZGLaoNAYIN8qBUIZBRs0IOoYGGLHrYs7FPhoA/fMrtaaSStsnK8tnbk78Og1f6Znf39vvOZ78xKt+7emURkbJyFMaAGqAHlNHCLACO8OYBRA6pqgADjqKvcqKtqZ2O7gx8oCDACjACjBpTVAAFG8SorXjqa4B2NajElwAgwAowaUFYDBBjFq6x4VXMLbG/wjpEAI8AIMGpAWQ0QYBSvsuKlowne0agWUwKMACPAqAFlNUCAUbzKilc1t8D2Bu8YCTACjACjBpTVAAFG8SorXjqa4B2NajElwAgwAowaUFYDgQDss60/4eTkH57lw3u/UDY4qo1GbC8dyU3TQCAAE/ASEJuf/31H2d//O0T58Qc/JcQ4ylMD1EDgGggMYAJe3fQX4BIA8zrWfS6/0z1QA9TARTUQGMD6TSH99q88W+0B30UfgudT+NTAzdRAYADzmkJ2Tym7v7trZ57im0xgJ1dBTTOgnZdwsBFHtGnBZ7cLKB/v4tlGFuW6gbNMwoHgZALJY3GNjtppAenV9jWe96Cl5+BBDSitgcAA9jbTRHGNcGi9cFnAQc1Co1pAei+F5GEFmmmguBGzz13K6TANCw2tglwqhZ3VOCKPdlFutK9JH1fRMA2UX8141H8zR6veODMOjInaGggpwHZRFsBaawd3fmUN8w9kgJWwNdE+bkNNO8KSvC9ZQj65TIDRZVADI6qBkALMcWBmo45yLoOt5RnckxLQglVr3xTS5xa0HGFFR9Ee1BiL0Y9FSAE2jshEHC/2CyhXdTQMC2ajioNPJQcm3FYLYAnk6gQYO+zod1jmuDPH4QXY5P2265qI2w7LLO2218A6ADaO9aIF83S3tdAvEh19stCadjLxnYlnPBiPUdBAOAH29AiaqSO/ct9Zu5h8jrxmoVHY7Auw6GoBDVNHsfm2MvpgzXZljaJzzSgki89A6FADnRoIDGDB/owihqWMeItowWyWxvkR1qedxveugYn9MSzuVaCJ6WbrmmzHoj6T35l8xoPxUF0DgQBM/Nre7wer/Y4L8PUP4n08novjo+bbx/7nyUJ0rnk8Ke/j9mCxY5wYJ7U0EAjAmHS1ks58MV+jogECrPUmk6IeFVHzOW6OlgkwAuwNU/ib0xEIPTVzTYARYAQYNaCsBggwildZ8dI1qemagswbAUaAEWDUgLIaIMAoXmXFG+RIzrrUdHMEGAFGgFEDymqAAKN4lRUvXZOarinIvBFgBBgBRg0oqwECjOJVVrxBjuSsS003R4ARYAQYNaCsBggwildZ8dI1qemagswbAUaAEWDUgLIasAF2984kWBgDaoAaUE0DdGAcfZUdfYOcirAuNaejBBgBRoBRA8pqgACjeJUVL12Tmq4pyLx5Auy3730d//7Sl4Fbt1iGGAORg4V33yNgOMhQA3004Amw/7zzDsE1RHDJA8cXt29TvH3EG+RIzrrUdHOeAJM7ELeH70LZudTsXMzb1efNF2BMwtUnwSvG8sDhdZz7hpMXxj1ccSfAQjo9IcDC1VEIrnDmgwAjwLjGFlINEJr+0CTAQipeOjB/8bKDM0YEGAFGBxZSDRDQ/oAmwEIqXjowf/GygzNGBBgBRgcWUg0Q0P6AJsBCKl46MH/xsoMzRoEDbOKDb3aM6H7fKUJvERJg3nGhXhgXWQOBA+yfn30ff135Xgtift/lxnC7LU4CrB0L6oKx6KcBAoxTyNZg008k3E+AhFUDVwqwT37zbWh/ex/ChYltEYRuRxbWwAy7XXRghMawNajC/QMHmJg+iiLWvgS83CLAJQLy9gCLYXYji+K5jka9iuLhJmYn2iJ/tl9BeX/NPqdc1aFVKzhYm3HcxdMUiqUCduba54u2LCVLKB9uhtKBEGCduVKhM7GN15+zwAHml8S3BdhSVodp6CgfppDcy6KsWTCrGcw3p4A7pxbMhgHtvID0XgoHJR2mqSOXEEF9jrxuoXa4IMFqE0XDwllyStp3/QnoFy8CLDy56Jcj7h9+jgIFmICTXESC1+a/axc32W8FsIldlE0D+dVYGzbTGZyZFoobThBtgNWyLaBFxpaR0yxouWX7mvnDOkzpePRlCaZZRfLR8JPgxkb+JMDCmRc5R9wefo4CA5iYMoqpoztlFOASCe4GltjvrocNLIDVAhpmHfk94b7ckkVZt6BlE/Z9bICd7rYBNzYOsc8FWGQui5qA4IoIegxbRQtmcRtRLuJ3xGzgnIQ0bmz/8KFynTkIDGBuo7uBJX8XkJOLe43v53YFpmmgVqqg3FXy2/HBADY2heRrC43j54i0HF14k00HFt7c+OqVcL+2QfHaACbA9b/Pf9AqwqkNLISnR9DMOg7isqhjiEqL+L4ObGwc0VcVmHoB683PZyEWGgEm55rbA/eVEGv6Kp7hWgH26MNvtdbIBND6P9AU1k90aCebeGgnZAbpcwuN1xksTgoxizeSJWj2upgj7kEAFpnYRtHQUat1L+iHr4MQYOHLSX+9sq3Dis21Acx9QHlK6e7r/YwjXbVgakdouaTpTeTODZim5RTDwFlmubWGNRDAxsbx4kTU0e3mwidAAix8OenVKds47JgEDjD3d2Dug/l9d88b9DP64GPMzs3g3ohbZQKMcBi0T9zk8wIH2E0OZpDPToARYEHqaVTrIsBC6uQIMAJsVKET5HMRYATYG16mECJBdjbWFbyeCDACjAALqQYIPH/gEWAhFS+nkP7iZQdnjAgwAowOLKQaIKD9AU2AhVS8dGD+4mUHZ4wIMAKMDiykGiCg/QFNgIVUvHRg/uJlB2eMCDACjA4spBogoP0B7Qsw2Qlw+xaGEQMK2V/IjNHNjJEnwL64fXsoHXUYcFDhnuycN7NzMu/+efcE2B++9i4Bdms4bqsbqMmvfJVTPE7xqIE+GvAEGMnvT37GiDGiBoavARtgd+9MgoUxoAaoAdU0QAfWx5pydB3+6MocMAd+GiDACDCur1ADymqAAKN4lRWv3+jM46Pv4AgwAowAowaU1QABRvEqK146rNF3WH45JsAIMAKMGlBWAwQYxauseP1GZx4ffYdGgBFgBBg1oKwGCDCKV1nx0mGNvsPyyzEBRoARYNSAshogwCheZcXrNzrz+Og7NAKMACPAqAFlNUCAUbzKipcOa/Qdll+OCTACjACjBpTVQOAA+9Hv1vCTT/7SU8R+P5ryOEdUaoAauIgGAgXY+79awJ0//7cDXrGX/8LPVj639xNiHuKcmMJHczO4d2UuYAbr+1lsLcQ4gFxZjD3yyntdi96uBGAyQV039o0fxggxL1EnjqCZFex4HXubfY+WsbW3hnn32rkMaqYFLZu4FkHJuec2wXbVGrg2gIkHIcQ8BB00wDzqi07eR9QFGj8J8hHSwLUCTIbYd37+6wsKKYbZjSyK5zoa9SqKh5uYnWgD4dl+BeX9NfucclWHVq3gYG3GucfTFIqlAnbm2ueLtiwlSygfbuKXXQmd3S6gfLyLxacp5Jv3y+8lpGnec6RLFaTXEkgW6tD0EraadUSfbOKgUIWm6zgrHPVM3TqOH6ew+KnswJr1rsjtFPu62j6ZQPK4gpqmo3ZaQHo17gBqJYPyax2maaBWEvF4jshYb50dbehu49wu8uJ+C+IezecQ7ZRifdWjKuuX88/tN+nhWgAm1sW6i1gve1PDuo8tZXWYho7yYQrJvSzKmgWzmmlNlXZOLZgNA9p5Aem9FA5KoiPryCWEAJ4jr1uoHcr33ETRsHCWnOppx1JOh6nr0LQq8qkUkocl1BoWGsXNppPZRdkU99NRK2SRTG1jSQAskUXNsKCVskjKbfi0uf40vYuyqKfZxvRxHVpdR6M1hXTqLb+SRSv2uc8xjsijZh1V5znTx1U0TAPlVzOIxNeQPKygYdaR30sh+UfxvF11+rXRdnAWGnoz1qmC/ezm6S4edoG+O0f8LueN29ehhysHmHBaAlZyETC7EMAmRCc0kF+VFqKnMzgzLRQ3HKHYAKtlW0CLjC0jp1nQcss2oOYP6zCl49GXJZhmFclHvUKzAWbWcRBvH4uuFmwwHNguzoFCJxBjsNvwOoXHrY4ew1bRgvk6ZXf+Z8cGTO3IgZ19TgwvTgyYFwCY3TZRh+SIhJPMJ5cdJ9kzhZQB5t/GSBNgxZftWEdfVaQ2tmNyHQLlPRjvN2ngygHmdfMLA6wJD9tVCGdhlyzKentx2obH6W6HmxL7XIBF5rKoCQja07MmWIrbnmtDLUi0QCRE5Dg2xx3JUHAFtma7vLO9dse3n33b7fxTSJ9L7XHr3hAgdRfxveoV+1wH1qcOty7x+UaA+bXRvd69X/PZeup0n5mfXvrmvuvThRoAsyHQXNcRaztSyW/HbWj5AmxsCsnXFhrHzxFpOTrvQHsDzOn8/QHmBZ9xRGz4CkAlkKt7AKxjDcyrDhlgfeoYGGBe9cttJMAIH+8+Eda4qAGwp2Khu3NKFxmLISpNo/wBNg57KqQXsC6mRHoBz+SOL207U8gKdqT6Ww5uVSTYCwRxHNR6ATWbqbfutVOyINaS5DeCD1NVyYF5OCTbObYd0bqYknbVEX2ygPkHTefX45bktvq30XFw7fvZwu2pUy2Rh7XzsV2X11FIATaF9RMd2slmc+F4xp5+NV5nsDgpHlq8kSxBs9fFnCAMArDIxDaKho5arWtBP5HBWb2KtL3gPw4HYBa0QvNN50QcyVN5/UqGQjsJjwWMjCrST+/brvBePGUv2tcyzsuD6EYJDVNHccN5axh94hxvTyEdl2jWj/BCAGlyAcmSWCNrA8VZi5PqeLBmO7vWCwYbNnWkp912dbbVr40EmBs3fqoA2JACLI501bIXvFsuaXoTuXPRmS2nGAbOMsstNzMQwMbGm4vmXW5uTYDFwtme80bSmUIWcHAi3mQ276dXkG79mr0TCu1Ez2A9J94KNq8RPyAtbHcs6i9lpONGHbk9+WcU44guZOy1Pfu+hni7mJHWwESnimFxrwLNaN+jcZ6VFvVnsGNDz3l5EO1xiz5ttAHYBqb9bHRgHWur7XwTcsOORaAAE28cxQK9++v7fp/inIv/DswRS/TBx5i90r/eNB1Y822hfb9px1ENnCz770Ef46E8BZWmqJFA/j50H4/n4nhsO9K36Eh+bZTby20CLKQaCBRgooP3+zO3DLOw/yfSexH/LSAR0qQPDGK2n+AKuQYCB9godI5FMc07z2Ix5MkbhVjzGTgwXkYDBBghRZdBDSirAQKM4lVWvJcZuXntaDg/AowAI8CoAWU1QIBRvMqKly5qNFzUZfJIgBFgBBg1oKwGCDCKV1nxXmbk5rWj4d4IMAKMAKMGlNUAAUbxKiteuqjRcFGXySMBRoARYNSAshogwCheZcV7mZGb146GeyPACDACjBpQVgMEGMWrrHjpokbDRV0mjzbA7t6ZBAtjQA1QA6ppgA6MDowOjBpQVgMEGMWrrHgvM/XgtaMx/STACDACjBpQVgMEGMWrrHjpokbDRV0mj/8HZndD92S3vEoAAAAASUVORK5CYII=)

Podemos forçar o commit do .env com o comando

```
git add .env -f
```

### 3 - Setup inicial da tela

#### Ajustar .env

- SKW\_URL: URL do servidor de aplicação com o sankhyaW rodando;
- VITE\_APP\_APP\_DESCRIPTION: Nome da tela;
- VITE\_APP\_MODULE\_NAME: Nome do módulo;
- VITE\_APP\_RESOURCE\_ID: Resource ID da tela;

![Arquivo dotEnv](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/ajusteDotEnv-b7655b9591a272d69faa57ed1f284b95.png)

#### Ajustar .env.production

- BASE\_PATH: path dentro do SankhyaOm para acessar a tela (substituir o nome do módulo e da tela)

![Arquivo dotEnv.production](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/ajusteDotEnvProduction-ad9f56b6672a52d75cd6ef5c0c4dd102.png)

#### Ajustar package.json da tela:

Trocar referências do projeto:
![Ajustes no package.json da tela](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/packageJson-d5033dc2db61afe94d1ec92d64bfa952.png)

#### Realizar o install e rodar o projeto:

```
npm install

npm run dev
```

### 4 - Ajustar configurações de pipeline

As configurações da pipeline podem ter muitas particularidades dependendo do projeto em que se encontram. Os responsáveis por essas devem fazer
os ajustes necessários.

As pipelines dos módulos BFF atualmente possuem uma configuração padrão de herança dos arquivos de build na raiz do frontend do módulo:

Exemplo:

```
./financeiro-frontend/.gitlab-ci.yml

include:
  - local: '*/**/scripts/gitlab/.*Build.yml'
  ...
```

Isso faz com que qualquer arquivo que siga o padrão descrito seja executado no build da pipeline.

Portando devemos criar a pasta gitlab dentro do diretório scripts contendo os arquivos de configuração do build a tela:

Exemplos dos arquivos:

./financeiro-frontend/MinhaTelaBonitona/scripts/gitlab/.minhaTelaBonitonaBuild.yml

```
workflow:
 rules:
   - when: always

minha-tela-bonitona-build:
 variables:
   PROJECT_PATH: "MinhaTelaBonitona"
 only:
   changes:
     - "financeiro-frontend/MinhaTelaBonitona/**/*"
 extends:
   - .build

minha-tela-bonitona-test:
 variables:
   PROJECT_PATH: "MinhaTelaBonitona"
 needs: ["minha-tela-bonitona-build"]
 only:
   changes:
     - "financeiro-frontend/MinhaTelaBonitona/**/*"
 extends:
   - .test

minha-tela-bonitona-deploy:
 variables:
   PROJECT_PATH: "MinhaTelaBonitona"
 needs: ["minha-tela-bonitona-test"]
 only:
   changes:
     - "financeiro-frontend/MinhaTelaBonitona/**/*"
 extends:
   - .deploy
```

./financeiro-frontend/MinhaTelaBonitona/scripts/gitlab/.minhaTelaBonitonaBuildInstall.yml

```
minha-tela-bonitona-install:
  variables:
    PROJECT_PATH: "MinhaTelaBonitona"
    PACKAGE_NAME: "minha-tela-bonitona"
    JOB_DEPENDENCY: "minha-tela-bonitona-install"
  extends:
    - .build_screen
```

### Hands-on

[Criando uma tela no DS](https://drive.google.com/file/d/1arNhZs5dgVps6_xjNCiA1tlq_rnZ-GqW/view?usp=drive_link)

## Fluxo de desenvolvimento da tela

### Ajustar endereço do servidor e credenciais

Para rodar a tela fora do SankhyaOm, devemos ter um servidor de aplicação contendo o SankhyaW com a versão necessário do backend da tela
(SankhyaW, módulo e/ou BFF) rodando.

Após ter o servidor de aplicação rodando, devemos mapear nos arquivos .env a variável SKW\_URL:

Exemplo:

```
SKW_URL=http://127.0.0.1:8180
...
```

dica

O projeto está inicialmente configurado para acessar com usuário SUP sem senha, caso seja necessário mudar as credenciais acessar o arquivo:

```
./MinhaTelaBonitona/public/workspacemock/workspace.js
```

Na seção Auth, editar o NOMUSU e INTERNO para o nome e senha do usuário respectivamente.
Exemplo:

```
"requestBody": {
    "NOMUSU": {
        "$": "NOVOUSUARIO"
    },
    "INTERNO": {
        "$": "SENHADONOVOUSUARIO"
    }
}
```

### Ajustar o gulpfile

O gulp é responsável por automatizar a tarefa de deploy da tela para dentro do SankhyaOm

Ajustar as variáveis MODULE e APPNAME no arquivo gulpfile.test

![Ajustes no gulpfile.ts da tela](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/gulpFile-ac044260e3dd3f95f90e7c23057d8886.png)

### Fazer link entre projetos

informação

Estes passos só devem ser executados em casos de desenvolvimento de componentes ou em projetos dependência.

Muitas vezes precisamos fazer alterações ou consumir alterações ainda não disponíveis em produção em projetos dependência.
Para isso utilizamos o `npm link`:

Quando rodamos o comando `npm link` em um projeto (dep-proj) criamos um symlink (symbolic link) no node\_modules para que outros projetos tenham facil
acesso aos arquivos.

Quando rodamos o comando `npm link dep-proj` estamos dizendo para a aplicação que estamos utilizar o symlink global da dependência que
criamos anteriormente.

Dessa forma podemos fazer alterações no `dep-proj` e isso será refletido automaticamente (após o build do projeto em alguns casos) no projeto
que está consumindo o link.

Com isso temos um processo padrão para o link dos projetos:

- Acessar dependência;
- `npm install`; (Caso ainda não tenha feito o install)
- `npm link`;
- `npm run build`;
- Acessar projeto consumidor;
- `npm link dep-proj`; (conferir arquivo runlink.sh na pasta scripts)

Após isso, realizar alguma alteração no projeto dependência e verificar que a alteração refletiu na tela.

dica

O VS-Code muitas vezes não atualiza o ícone do Symlink automaticamente.
Pata atualizar, abrir a paleta de comandos

- Show and Run commands (Ctrl+Shift+P)
- Developer: Reload Window

Para verificar o Symlink:
Acesse a paste node\_modules, encontre o caminho da dependência linkada e veja se existe a setinha com o symbolic link
![Conferindo Symlink da dependencia](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/symlink-a8334e6c86d3a292718bffc833248572.png)

O diagrama a seguir representa a base dos links dos projetos BFF:
![Links dos BFFs](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/links-684db82af3c571ee7ab27f3c1f67e63e.png)
