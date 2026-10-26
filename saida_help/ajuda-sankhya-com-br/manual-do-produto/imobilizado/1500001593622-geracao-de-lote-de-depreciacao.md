---
id: "1500001593622"
titulo: "Geração de Lote de Depreciação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001593622-Gera%C3%A7%C3%A3o-de-Lote-de-Deprecia%C3%A7%C3%A3o"
trilha: "Manual do Produto > Financeiro e Patrimônio > Imobilizado"
atualizado_em: "2026-07-29T16:03:14Z"
rotulos: ["Imobilizado", "Projeto", "Contabilização", "Preferências", "Lançamentos Contábeis", "Depreciação", "br.com.sankhya.mgeimob.geracaolotedepreciacao", "Geração de Lote de Depreciação", "Data Movimento Usar Projeto? Projeto obrigatório", "Número Documento Gravar código empresa origem Preferências Contabilidade", "Não agrupar Agrupar por Produto/Conta/C.R Agrupar por Grupo de Produto/Conta/C.R"]
---

# Geração de Lote de Depreciação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42315060545559) Módulo: Imobilizado > Rotinas
```

---

Por meio desta tela, você poderá realizar a contabilização da depreciação.

![Imagem 2: Por meio desta tela, você poderá realizar a contabilização da depreciação.](https://ajuda.sankhya.com.br/hc/article_attachments/18196754026263)

A **"Data do Movimento"**, quando informada, será enviada para o lançamento contábil.

A marcação **"Usar Projeto?"** poderá ser acionada se no registro da **"Empresa do Lote"** nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa), aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos), a marcação **"Utiliza Projeto"** também for ligada. Para que, assim, o **"Projeto"** informado na tela [Departamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610254) seja utilizado no lançamento contábil da empresa.
Lembre-se ainda que quando a marcação **"Projeto obrigatório"** do [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054) da empresa utilizada também estiver ligado, mas a marcação Usar Projeto? estiver desativada, o sistema exibirá a mensagem:

**"Para a conta contábil xxx o projeto é obrigatório."**

Porém, caso o campo Projeto da tela Departamentos não for configurado, a mensagem abaixo será apresentada:

**"Para usar projeto no lançamento de depreciação, é necessário informar um projeto no departamento do bem."**

Quando a marcação **"Utilizar Número do documento na Baixa do Bem"** for selecionada, ao efetuar o processo de contabilização dos lotes de depreciação/baixa do bem, você deverá preencher o campo **"Nro. Documento"** da tela [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis) ao adicionar um lançamento.

Quando a marcação **"Gravar o código da empresa de origem"** estiver realizada, o sistema irá gravar o código da empresa do bem nos lançamentos contábeis referente à depreciação. 

**Nota:** a marcação acima apenas será habilitada para edição quando a marcação **"Gravar Empresa de Origem nos lançamentos"** da tela [Preferências da Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa) estiver feita. 

**Observação:** a nova funcionalidade impactará o agrupamento dos lançamentos configurados a partir das opções de Tipos de Agrupamento da seguinte forma:

- Quando a marcação não estiver feita, o sistema não irá impactar na funcionalidade dos tipos de agrupamento e não irá gravar o código da empresa no campo Empresa de Origem da tela de [Lançamentos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116173-Lan%C3%A7amentos-Cont%C3%A1beis).
- Com a marcação feita e o Tipo de Agrupamento igual à **"Não agrupar"**, será gravado o código da empresa da TCIBEM no campo Empresa de Origem.
- Se a marcação estiver realizada e o Tipo de Agrupamento for **"por Produto/Conta/C.R"**, o sistema irá agrupar considerando também o código da empresa da TCIBEM e irá gravá-lo no campo Empresa de Origem da tela Lançamentos Contábeis.
- Por fim, se a marcação estiver feita e o Tipo de Agrupamento for **"por Grupo de Produto/Conta/C.R**", o sistema irá agrupar considerando também o código da empresa da TCIBEM e gravará o código da empresa no campo Empresa de Origem da tela Lançamentos Contábeis.

Ao **"Gerar"** o lote, o pop-up **"Processos"** será exibido durante a geração, em que teremos os processos, a mensagem de finalização e, caso ocorra algum erro durante a geração este também será exibido:

![Imagem 3: Ao "Gerar" o lote, o pop-up "Processos" será exibido durante a geração, em que teremos os processos, a mensagem de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500001531001)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001593622-Gera%C3%A7%C3%A3o-de-Lote-de-Deprecia%C3%A7%C3%A3o#top)
