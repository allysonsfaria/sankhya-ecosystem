---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitInMemoryLoader/"
titulo: "DataUnitInMemoryLoader"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitInMemoryLoader/"
trilha: "Docs > Utilities > Components > Dataunitinmemoryloader"
---

# DataUnitInMemoryLoader

O **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)** atua como uma camada de abstração entre o back-end e a interface do usuário, proporcionando uma solução eficaz para o gerenciamento de dados.

Porém, devido a necessidade de implementação de loaders, gerenciamento de metadados e paginação,
sua utilização pode trazer um nível de complexidade que não faça sentido para determinados contextos.

Pensando nisso, desenvolvemos o **DataUnitInMemoryLoader** que nada mais é, do quê um utilitário que nos entrega de forma
bastante simplificada, uma instância de **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)** pronta para uso, com seus loaders já configurados e
realizando o gerenciamento dos registros em memória.

Importante

O **DataUnitInMemoryLoader** implementa automaticamente o método `dataLoader` e outros métodos necessários do DataUnit, abstraindo a complexidade de paginação, ordenação e filtragem.
Caso deseje sobrescrever esses métodos para implementar comportamentos personalizados (como integração com APIs específicas), consulte a documentação do [**DataUnit**](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit/#dataloader) para entender como implementar corretamente esses métodos.

![Imagem 1: O DataUnitInMemoryLoader implementa automaticamente o método dataLoader e outros métodos necessários do DataUnit,…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Configurações

Existem algumas opções de configurações que permitem um certo nível de customização no **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)** criado pelo **DataUnitInMemoryLoader**.

Essas configurações devem ser passadas para o contrutor do **DataUnitInMemoryLoader**, seguindo a interface
`DataUnitInMemoryLoaderConfig` disponibilizada pelo `sankhyacore`.

```
export interface DataUnitInMemoryLoaderConfig {
  autoLoad?: boolean; // Define se os dados devem ser carregados automaticamente.
  pageSize?: number; // Controla a quantidade de registros por página
  recordDateFormat?: RECORD_DATE_FORMAT; // Define o formato padrão dos campos do tipo Data
}

export enum RECORD_DATE_FORMAT {
  DD_MM_YYYY = 'DD/MM/YYYY',
  ISO = 'ISO'
}
```

## Controle de Paginação

Por padrão, o **DataUnitInMemoryLoader** define um total de **150** registros por página. Porém, caso o desenvolvedor deseje
personalizar isso, na instanciação do **DataUnitInMemoryLoader**, além dos parâmetros `metadata` e `records`,
basta informar também o parâmetro `config` com a propriedade `pageSize` contendo o valo desejado.

> Propriedade utilizada: **pageSize**

### Tamanho da página

No exemplo abaixo, mostramos como criar um **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)** com um tamanho de página de 5 registros.

![Imagem 2: No exemplo abaixo, mostramos como criar um DataUnit com um tamanho de página de 5 registros.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

### Escondendo controle de paginação

Existem cenários onde desejamos esconder o controle de paginação, para manter um layout mais clean, por exemplo.

Nesses casos, para fazer isso, basta definir a propriedade `pageSize` com o valor **0**. Isso fará com que,
além de todos os registros serem carregados em uma única página, o controle de paginação fique oculto.

![Imagem 3: Nesses casos, para fazer isso, basta definir a propriedade pageSize com o valor 0 . Isso fará com que, além de todos os…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Carregando de dados

> Propriedade utilizada: **autoLoad**

Por padrão, o **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)** irá carregar os dados assim que for renderizado na tela.
Porém, podemos inibir esse comportamento, para que esse carregamento seja feito no momento que for mais adequado.

Para isso, podemos utilizar a propriedade `autoLoad` das configuraçõs definida com o valor `false`
e quando for o momento de carregar os dados, chamar a função `loadData` do **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)**.

![Imagem 4: Para isso, podemos utilizar a propriedade autoLoad das configuraçõs definida com o valor false e quando for o momento…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## Padrão de campos tipo DATE

> Propriedade utilizada: **recordDateFormat**

A princípio, o **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)** gerado pelo **DataUnitInMemoryLoader** está preparado para receber
em seus campos do tipo `DATE` o padrão DD/MM/YYYY.
Porém, existem casos onde o padrão adotado pelo desenvolvedor é o ISO.

Para atender asse cenário de forma simples e rápida, basta na criação da instância do **DataUnitInMemoryLoader**, informar a propriedade
`recordDateFormat` com o valor `ISO`, podendo utilizar o enum `RECORD_DATE_FORMAT` fornecido pela `sankhyacore`.

![Imagem 5: Para atender asse cenário de forma simples e rápida, basta na criação da instância do DataUnitInMemoryLoader , informar…](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---
