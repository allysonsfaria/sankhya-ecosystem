---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/documentacao"
titulo: "6 publicações com a etiqueta \"documentação\""
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/documentacao"
trilha: "Blog > Tags > Documentacao"
---

# 6 publicações com a etiqueta "documentação"

## [Liberando uma nova tela no Design System](https://gilded-nasturtium-6b64dd.netlify.app/blog/liberacao-telas-ds)

27 de maio de 2024 · 5 min para ler

![Leonardo Jorge](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LeonardoJorge.png)

Leonardo Jorge

Software Architect

## Objetivo

Esse artigo visa definir como é o fluxo de liberação de telas nolayout do design system nos seguintes cenários:

- Telas portadas do HTMML5/Flex
  - Liberação apenas em ambiente de `desenvolvimento` e `teste`
  - Liberação em produção
- Novas telas

## Statsig

Hoje está sendo utilizado o [Statsig](https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/statsig.com) para fazer o gerenciamento de liberação das
telas no DS, antes de prosseguir com esse artigo, é necessário realizar a leitura das seguintes
docs do statsig:

- [O que é feature flag?](https://docs.statsig.com/feature-flags/working-with)
- [O que é dynamic config](https://docs.statsig.com/dynamic-config)

## Fluxogram para abertura de telas

Para abertura de uma tela mapeada no SankhyaOM, existe uma configuração dinâmica, e algumas feature flags que podem impactar em como essa tela será aberta, isso pode ser visto no fluxograma a seguir:

![Fluxograma abertura de telas](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/fluxograma-screen-ds-780a1f4312fc36d7bb002702168296bb.jpg)

### Itens do fluxograma

- `isPlatformLabs=true`: é um atributo mapeado no item de menu do SankhyaW, esse deve ser utilizado para novas telas que têm apenas o layout do DS pois nesse caso não será realizada nenhuma checagem e será aberta diretamente no layout do DS.
- `moduleScreenStatus`: Essa é uma dynamic config que fica no statsig, fazendo o mapeamento de metainformação de uma tela, o nome da config é sempre composto por `nome do módulo + -mapeamento-telas`, por exemplo: `mgecom-bff-mapeamento-telas`, `mgefin-bff-mapeamento-telas`.
  - dataFimBeta: É a data que está programado para que a tela saia da versão beta e entre na versão de convivência.
  - dataFimConvivencia: É da data programada para a tela sair de convivência e entrar em GA(produção)
  - versaoMinima: É a versão minima do SankhyaOM requerida para a tela.

O conteúdo da configuração será:

```
{
  "telas": {
    "br.com.sankhya.fin.cad.movimentacaoFinanceira": {
      "dataFimBeta": "15/05/2024",
      "dataFimConvivencia": "31/05/2024",
      "versaoMinima": 4.21
    },
    "br.com.sankhya.fin.cad.movimentacaoBancaria": {
      "dataFimBeta": "15/05/2024",
      "dataFimConvivencia": "31/05/2024",
      "versaoMinima": 4.21
    },
  },
}
```

- `ignorePartnerV3`: feature flag utilizado para definir parceios que não vão utilizar aquela tela no DS.
- `forceUseV3`: feature flag utilizado para definir parceios que vão ser forçados a utilizar a tela no DS.
- `isBetaPartner`: define se o parceiro é um beta testar daquela tela.

### Liberando uma tela portada do HTMML5/Flex em base de teste

#### Criar dynamic config

O primeiro passo é criar uma configuração dinâmica para mapear o status da tela, lembrando que a regra é `nome do módulo + -mapeamento-telas`, caso a dynamic config já exista, devemos apenas adicionar o resourceID da tela na configuração já existente.

dica

Para obter informções de nome do módulo e do resourceID da tela pode ser virificado com o desenvolvedor referência ou arquiteto do projeto. Neste artigo vamos utilizar a liberação de limites como exemplo:

- resourceID: `br.com.sankhya.liberacao.limites`
- módulo: `mge-bff`

- Para criar a dynamic config, acessar `Dynamic Configs` do statsig, ir na opção `+ create`.
- No popup, informar o nome da config, no nosso caso, `mge-bff-mapeamento-telas`, depois ir em create.

![Cadastrando dynamic config](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/criando-config-ae9cb02ee4a7598a3d508f896bcf2e9b.png)

- Para que a regra se aplique ao ambiente de teste é necessário criar uma regra especifica, para isso clicar na opção `Add Targeting`

![Regra personalizada para teste](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/regra-especica-teste-cba83021b80d00b62c477243be3f872a.png)

- Clicar em `Add New Rule`
- Informar o campo customizado `clientGaId` com o valor `03030ed40c6908460ab306c209046d3b4a85773050`
  ![Adicionar regra por usuários](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/add_new_rule-dcb5fd0d30d967d1b8cbbf545bd1a62e.png)
- Clicar em `Add more conditions`
- Informar o campo customizado `userName` com os valores `SANKHYADS,SANKHYADS2,sankhyads,sankhyads2,MARIDS,DENISDS`
  ![Adicionar condição por usuários](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/add_new_condition-fddab8ea84fe446a1fc77c61261f778d.png)
- Outra regra que deve ser adicionada é a `Base teste Sankhya - Forçar convivência` os campos:

  - `clientGaId` com o valor `03030ed40c6908460ab306c209046d3b4a85773050`
  - `environment` com o valor `staging`
- A última regra que deve ser adicionada é a `Sem SAS - Forçar Convivência` com o campo:

  - `clientGaId` isNull

para essas três regras, adicionar o JSON no seguinte padrão:

![Adicionando JSON personalizado](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/add_json-2259fc412662a38ad5202332ed8f2d09.png)

```
{
  "telas": {
    "br.com.sankhya.liberacao.limites": {
      "dataFimBeta": "01/01/2024"
    },
  },
}
```

dica

Observe que para essa tela, o dataFimBeta está com uma data passada, então, os usuários que atenderem as regras
definidas anteriormente, vão estar com status de convivência para essa tela, o que é o ideal em ambiente
de desenvolvimento ou ambiente de testes tendo em vista que é necessário realizar testes de comparação no layout anterior

No final a config ficará dessa forma:

![Config final](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/teste-final-config-2076bd23f08aafb044cbf3cea8500c51.png)

Após essa configuração, caso a tela esteja disponível dentro do módulo ela já será aberta no DS.

### Liberando uma tela portada do HTMML5/Flex em produção

#### Criar dynamic config

Primeiro é necessário mapear a tela no valor padrão da dynamic config `mge-bff-mapeamento-telas`

```
{
  "telas": {
    "br.com.sankhya.liberacao.limites": {
        "dataFimBeta": "01/12/2030",
        "dataFimConvivencia": "01/12/2035"
    },
  },
}
```

Por exemplo:

![Config padrão](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/default_dynamic_config-3befe5f90578689f4edada311f391772.png)

dica

Observe que para essa regra, o dataFimBeta está para 01/12/2030, nesse caso, a tela só vai aparecer para clientes que estejam mapeados como beta tester no feature flag `isBetaPartner` daquela tela.
A partir dessa data a tela vai ficar disponível como convivência até a data 01/12/2035 e após essa data a tela ficará em GA.

## Liberando novas telas

- Novas telas que existem apenas no DS e estão em um módulo BFF devem ser criadas com o atributo `isPlatformLabs=true` mapeado no menu do SankhyaOM. Exemplo:

```
<url>
    <![CDATA[/mgecom/GestaoCaixaPDV.xhtml5?mgeSession=${mge.session.id}&resourceID=${resourceID}&isPlatformLabs=true]]>
</url>
```

dica

Neste caso o sufixo `-bff` será adicionado automaticamente ao nome do módulo ficando: `mgecom-bff`, logo esse atributo só vai funcionar caso a tela esteja dentro de um módulo BFF.

- Novas telas que existem apenas no DS e estão em um novo módulo, micromudulos por exemplo, devem ser criadas com o atributo `nativeV3=true` mapeado no menu do SankhyaOM. Exemplo:

```
<url>
    <![CDATA[/mgecom/GestaoCaixaPDV.xhtml5?mgeSession=${mge.session.id}&resourceID=${resourceID}&nativeV3=true]]>
</url>
```

dica

Neste caso nada será adicionado ao nome do módulo ficando: `mgecom`, logo esse atributo vai funcionar para módulos que não são um módulo BFF.
