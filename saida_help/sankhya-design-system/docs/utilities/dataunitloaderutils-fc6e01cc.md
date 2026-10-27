---
id: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitLoaderUtils/"
titulo: "DataUnitLoaderUtils"
url: "https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataUnitLoaderUtils/"
trilha: "Docs > Utilities > Components > Dataunitloaderutils"
---

# DataUnitLoaderUtils

Ao implementar o dataLoader do **[DataUnit](https://gilded-nasturtium-6b64dd.netlify.app/docs/utilities/components/dataunit)**, o desenvolvedor tem a responsabilidade de lidar com
a **paginação**, **ordenação** e **filtragem** de dados.

Pensando nisso, disponibilizamos um utilitário que pode ajudar nessas abstrações, o **DataUnitLoaderUtils**.

Esse utilitário possibilita implementar toda a lógica de paginação, ordenação, filtragem e contrução do retorno exigito pelo dataLoader `Promise<LoadDataResponse>`.
Como também, disponibiliza métodos que lidam com cada funcionalidade de forma isolada, permitindo mais flexibilidade ao desenvolvedor.

## buildLoadDataResponse

`buildLoadDataResponse(recordsIn: Array<Record>, dataUnit: DataUnit, request: LoadDataRequest): Promise<LoadDataResponse>`

Esse método abstrai toda a lógica de **paginação**, **ordenação** e **filtragem** e retorna os dados já na estrutura esperada.

![Imagem 1: Esse método abstrai toda a lógica de paginação , ordenação e filtragem e retorna os dados já na estrutura esperada.](https://gilded-nasturtium-6b64dd.netlify.app/img/logo-sankhya.svg)

---

## applyFilter

`applyFilter(records: Array<Record>, dataUnit: DataUnit, filters: Array<Filter>): Array<Record>`

Responsável por lidar com os filtros aplicados, geralmente os filtros de coluna. Retorna o array de registros resultante.

## applySorting

`applySorting(records: Array<Record>, dataUnit: DataUnit, sorting: Array<Sort>): Array<Record>`

Lida com a ordenação aplicada nos registros. Retorna o array de registros com os dados ordenados.

## getPagesByRecords

`getPagesByRecords(records: Record[], offset = 0, limit = 0): Array<Record>`

Retorna os registros de uma paginação específica, a partir de um offset até um limit especificados.

## buildPaginationInfo

`buildPaginationInfo({recordsLength = 0, offset = 0, recordsPerPage = 0}: PaginationInfoBuilderParams): PaginationInfo | undefined`

Retorna as informações de uma determinada paginação.

Dica

A interface do método dataUnitLoader recebe como parâmetro um argumento do tipo **LoadDataRequest**, que por sua vez contém as informações de filtro, ordenação
entre outras, que devem ser aplicadas na listagem dos registros.
