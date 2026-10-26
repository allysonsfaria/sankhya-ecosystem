---
id: "360057141853"
titulo: "Processo de Integração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:11:35Z"
rotulos: ["Configuração", "Requisições", "Portal de Vendas", "XML", "Integração", "br.com.sankhya.tim.rotinas.TimProcessoIntegracao", "Tipos de Imóveis e Portais Online", "Configuração de campos e sub-abas", "Preencher campos e processar para gerar requisição", "JSON", "Imobiliária"]
---

# Processo de Integração

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311457841047) Módulo: Imobiliária > Rotinas    ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311461914263) Versão disponível: a partir da 3.31
```

---

Existem duas telas principais para que todo o processo de integração do Sankhya Om com os Portais Online seja funcional:

- Processo de Integração;
- [Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis).

Acesse os links abaixo para facilitar sua navegação nos processos de integrações:

[Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#tiposdeim%C3%B3veis)                                                                           [Processo de Integração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

[Gerar Requisição](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#gerarrequisi%C3%A7%C3%A3o)

## Tipos de Imóveis

A primeira ação que você precisará fazer, é criar Tipos de Imóveis que estejam vinculados com os Portais disponíveis visto que, cada Portal Online tem seu estilo de requisição. Esse procedimento é realizado através da tela [Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis), aba **"Portais Web"**.

![Imagem 3: A primeira ação que você precisará fazer, é criar Tipos de Imóveis que estejam vinculados com os Portais disponíveis…](https://ajuda.sankhya.com.br/hc/article_attachments/360093662254)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#top)

## Processo de Integração

Após configurar os Tipos de Imóveis, crie um Processo de Integração. Essa etapa serve para filtrar os imóveis passados na requisição para o Portal.

Na aba **"Processo de Integração"** estão todos os campos de combinação para gerar a requisição.

![Imagem 4: Na aba "Processo de Integração" estão todos os campos de combinação para gerar a requisição.](https://ajuda.sankhya.com.br/hc/article_attachments/360095917073)

Acesse os links abaixo para verificar a configuração dos campos de Combinação:

[Sub-aba Portais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abaportais)          [Sub-aba Fontes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abafontes)           [Sub-aba Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abafiltros)            [Sub-aba Ordenadores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abaordenadores)

[Sub-aba Coletores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abacoletores)     [Sub-aba Tradutores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abatradutores)   [Sub-aba Geradores](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#sub-abageradores)    [Outras sub-abas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#outrassub-abas)

---

**Sub-aba Portais**

Através desta sub-aba você cadastra novos portais. Caso os campos desta sub-aba sejam preenchidos, somente serão processados os imóveis inclusos em algum plano do Portal especificado.

![Imagem 5: Através desta sub-aba você cadastra novos portais. Caso os campos desta sub-aba sejam preenchidos, somente serão…](https://ajuda.sankhya.com.br/hc/article_attachments/360093666114)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Sub-aba Fontes**

Esta sub-aba tem o objetivo de selecionar, via SQL, os imóveis que irão para a requisição (faz um select no banco de dados).

**Nota:** Já existe um padrão a ser utilizado, porém, pode ser alterado por você.

![Imagem 6: Nota: Já existe um padrão a ser utilizado, porém, pode ser alterado por você.](https://ajuda.sankhya.com.br/hc/article_attachments/360095920593)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Sub-aba Filtros**

Nesta sub-aba, é feito o filtro via SQL, dos Imóveis encontrados em **"fontes"**.

**Observação:** Também já existe um padrão pré-definido, podendo ser alterado.

![Imagem 7: Observação: Também já existe um padrão pré-definido, podendo ser alterado.](https://ajuda.sankhya.com.br/hc/article_attachments/360095920733)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Sub-aba Ordenadores**

Aqui você pode realizar a ordenação via SQL, dos dados filtrados pelas outras duas sub-abas: [Fontes](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853#sub-abafontes) e [Filtros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853#sub-abafiltros).

![Imagem 8: Aqui você pode realizar a ordenação via SQL, dos dados filtrados pelas outras duas sub-abas: Fontes e Filtros .](https://ajuda.sankhya.com.br/hc/article_attachments/360095920873)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Sub-aba Coletores**

Na sub-aba Coletores, deve ser passado o nome de uma classe em Java que possua a função de coletar as fotos dos imóveis filtrados.

![Imagem 9: Na sub-aba Coletores , deve ser passado o nome de uma classe em Java que possua a função de coletar as fotos dos…](https://ajuda.sankhya.com.br/hc/article_attachments/360093666614)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Sub-aba Tradutores**

Nesta sub-aba é configurado o tradutor de determinado Portal. Os tradutores são feitos em Java e servem para passar os tipos e subtipos da aba **"Portais Web"** da tela [Tipos de Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360055936693-Tipos-de-Im%C3%B3veis) de uma forma diferente para a requisição

Um bom exemplo é quando o Portal exige os campos em inglês; assim, no campo **"Class Name"** deve ser informado o nome da Classe Java que realiza essa tradução.

![Imagem 10: Um bom exemplo é quando o Portal exige os campos em inglês; assim, no campo "Class Name" deve ser informado o nome da…](https://ajuda.sankhya.com.br/hc/article_attachments/360093666774)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Sub-aba Geradores**

Esta sub-aba é de extrema importância. Nela, você deverá informar:

- Módulo de Integração (Classe);
- Nome da Classe (exemplo: br.com.sankhya.timimob.model.integracao.Controller);
- Codificação (exemplo: UTF-8, ISO-8859-1);
- Linguagem (exemplo: java/javascript);
- Nome da Pasta (onde serão salvos os arquivos das requisições);
- Nome do Arquivo (nome padrão ao gerar os arquivos das requisições);
- Extensão do Arquivo (sendo **"JSON"** ou **"XML"**).

**Importante:** Existem Portais que utilizam o padrão XML para receber os dados e outros que utilizam JSON, sendo que esses dois layouts são aceitos nesta tela de Processo de Integração.

**Nota:** Todos os campos já possuem um valor padrão, que é informado ao preencher um portal automaticamente através do botão ![Botão](https://ajuda.sankhya.com.br/hc/article_attachments/15507731422871) **"Outras Opções"**.

![Imagem 12: Nota: Todos os campos já possuem um valor padrão, que é informado ao preencher um portal automaticamente através do…](https://ajuda.sankhya.com.br/hc/article_attachments/360095921693)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o)

---

**Outras sub-abas**

Na aba **"Planos"** você registra as especificações dos planos com os Portais, por exemplo, a quantidade de anúncios contratados.

![Imagem 13: Na aba "Planos" você registra as especificações dos planos com os Portais, por exemplo, a quantidade de anúncios…](https://ajuda.sankhya.com.br/hc/article_attachments/360095923173)

A sub-aba **"Informações"** (localizada ao lado da sub-aba **"Combinação"**) permite que você veja se a requisição já foi gerada e os caminhos para acessar o arquivo.

![Imagem 14: A sub-aba "Informações" (localizada ao lado da sub-aba "Combinação" ) permite que você veja se a requisição já foi…](https://ajuda.sankhya.com.br/hc/article_attachments/360093669134)

[[voltar ao subtítulo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#processodeintegra%C3%A7%C3%A3o) [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#top)

## Gerar Requisição

Para gerar a requisição, é necessário preencher os campos corretamente e clicar no botão ![Imagem 15: Para gerar a requisição, é necessário preencher os campos corretamente e clicar no botão "Processar" . Neste momento,…](https://ajuda.sankhya.com.br/hc/article_attachments/360095925153) **"Processar"**. Neste momento, começará um processamento assíncrono, que permite que você utilize o sistema enquanto está acontecendo a execução:

[GIF animado: Imagem 16: Para gerar a requisição, é necessário preencher os campos corretamente e clicar no botão "Processar" . Neste momento,…](https://ajuda.sankhya.com.br/hc/article_attachments/360095926133)

Ao finalizar, uma notificação será exibida na área de notificações do sistema e os caminhos do arquivo com a requisição ficam disponíveis na aba **"Informações"**.

Para finalizar, concluímos que a integração com o Portal escolhido está funcional e a Imobiliária deverá passar o link gerado para o Portal. Com isso, algumas vezes o Portal acessa o link e preenche os Imóveis, de acordo com o plano escolhido.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057141853-Processo-de-Integra%C3%A7%C3%A3o#top)
