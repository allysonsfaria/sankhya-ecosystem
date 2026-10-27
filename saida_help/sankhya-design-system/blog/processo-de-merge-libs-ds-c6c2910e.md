---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/processo-de-merge-libs-ds"
titulo: "Processo de merge em bibliotecas do DS"
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/processo-de-merge-libs-ds"
trilha: "Blog > Processo De Merge Libs Ds"
---

# Processo de merge em bibliotecas do DS

21 de maio de 2023 · 3 min para ler

![Leonardo Jorge](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/LeonardoJorge.png)

Leonardo Jorge

Software Architect

## Objetivo

Esse artigo visa definir como é o fluxo de merge em projetos de bibliotecas de componentes do design system, tanto para implementações (feat) e correções (bugfix e hotfix).

## Implementações

O fluxo de merge de implementações pode ser visualizado no fluxograma a seguir:

![Merge features](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/merge-feat-9fd673ab561aadd03b3cac9a04ba8656.jpg)

Observe que no fluxograma sempre é criada uma branch de feature onde as user storys são mergeadas, porém, existe uma excessão para esse caso, que é quando uma feature tem apenas
uma user story, para esses casos não é necessária a criação da branch de feature, apenas a de user story.

## Fluxo de Homologação (Subida de implementações para produção)

Na primeira semana de cada mês, será executado o processo de homologação de implementações que estão na develop das bibliotecas do design system, esse processo
é feito seguindo o fluxograma abaixo:

![Merge prod](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/merge-prod-308a7cc7139fe63db5365918c229d1e1.jpg)

## Fluxo de hotfix

O processo de hotfix acontece quando estamos tratando erros que ocorreram em produção, ou issues abertas pelos times internos da Sankhya, que estão impactando no desenvolvimento
de projetos que utilizam o design system.

![Merge hotfix](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/merge-hotfix-8aaf2815889084075457bcfae9d43bdc.jpg)

Observe que no caso de hotfix o merge é feito para as 3 branchs, sem aguardar o processo de homologação, pois para esses casos precisamos liberar os ajustes de forma instantânea.

A ordem dos merges devem ser:

- `develop`
- `release`
- `master`

É necessário aguardar que a pipeline da branch finalize para prosseguir com o merge na próxima branch.

## Fluxo de bugfix

O processo de bugfix é utilizado para defeitos encontrados fora do ambiente de produção ou seja, branch develop ou release durante o processo de homologação

- no fluxograma a seguir, destacamos o processo a partir de erros encontrados na branch develop

![Merge bugfix develop](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/merge-bugfix-6af7d0c1f177612d91f533dacdef1842.jpg)

- no fluxograma a seguir, destacamos o processo a partir de erros encontrados na branch release

![Merge bugfix release](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/merge-bugfix-release-76f446d63c6918ff80d11b12f28f15e8.jpg)

A liberação desses ajustes para produção, será feita pelo [Fluxo de Homologação](https://gilded-nasturtium-6b64dd.netlify.app/blog/processo-de-merge-libs-ds#fluxo-de-hologa%C3%A7%C3%A3o-subida-de-implementa%C3%A7%C3%B5es-para-produ%C3%A7%C3%A3o)

## Links uteis

- [Nomeclatura de Branchs](https://comunidade.sankhya.com.br/t/sankhya-gitflow-padroes-de-nomenclatura-de-branch-para-um-fluxo-de-desenvolvimento-eficiente/7189)
- [Utilitário CZ Commit para padronizar gitflow](https://comunidade.sankhya.com.br/t/formatando-mensagens-de-commit-com-cz-sankhya/7191)
- [Criando branch de feature](https://comunidade.sankhya.com.br/t/sankhya-gitflow-fluxo-de-trabalho-de-uma-branch-feat-dev/7226)
- [Criando branch de hotfix](https://comunidade.sankhya.com.br/t/sankhya-gitflow-fluxo-de-trabalho-de-uma-branch-hotfix-ga/7233)
- [Criando branch de bugfix](https://comunidade.sankhya.com.br/t/sankhya-gitflow-fluxo-de-trabalho-de-uma-branch-bugfix-dev/7190)
