---
id: "11790815385367"
titulo: "Códigos de Naturezas de Rendimentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/11790815385367-C%C3%B3digos-de-Naturezas-de-Rendimentos"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Cadastros e Configurações Fiscais"
atualizado_em: "2026-09-15T14:03:20Z"
rotulos: ["Configuração", "Fiscal", "RFB", "Impostos", "Códigos de Naturezas de Rendimentos", "EFD Reinf", "ID: br.com.sankhya.mgeliv.naturezas.rendimentos", "Configurar deduções e tributos", "Transmissão obrigatória EFD-Reinf", "Cadastrar e alterar códigos de rendimentos", "EFD-REINF", "Natureza de Rendimento"]
---

# Códigos de Naturezas de Rendimentos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312895576215) Módulo: Livros Fiscais > Arquivos          ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42312912192535) Versão disponível: a partir da 4.17
```

---

A partir de Abril/2023 será obrigatório transmitir os eventos do Grupo 4000 da [EFD-Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553) de acordo com os códigos de Naturezas de Rendimentos.

Desse modo, nesta tela se encontram todos os Códigos de Naturezas de Rendimentos disponibilizados pela RFB que serão utilizados para geração dos eventos do Grupo 4000 da EFD Reinf e nela será possível alterar e incluir, caso tenha novos códigos que serão associados aos cadastros de [Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113) e [Serviços](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553).

![Imagem 3: Desse modo, nesta tela se encontram todos os Códigos de Naturezas de Rendimentos disponibilizados pela RFB que serão…](https://ajuda.sankhya.com.br/hc/article_attachments/18299151012887)

Para cadastrar os Códigos de Naturezas de Rendimentos, acione o botão ![Imagem 4: Para cadastrar os Códigos de Naturezas de Rendimentos , acione o botão "Inserir novo código" e preencha o " Código…](https://ajuda.sankhya.com.br/hc/article_attachments/16284241263383)**"Inserir novo código"** e preencha o **"Código Natureza Rendimento"** e a **"Descrição Natureza Rendimento"**. 

### Aba Geral

Efetue as marcações quando houver, **"Fundo ou Clube de Investimento"**, **"Décimo Terceiro"** e **"Rendimento Recebido Acumuladamente"**.

Caso haja algum tipo de dedução ou rendimento isento, informe o código nos campos **"Tipo de Dedução"** e **"Tipo Rendimento Isento"**, respectivamente. Havendo mais de um código, utilize o ponto e vírgula (;) para separá-los. 

No campo **"Tipo Tributo"** informe os tipos de impostos referentes aos Tipos Rendimento Isento separados por ponto e vírgula (;).  Sendo eles: IR, CSLL, COFINS, PP, Agreg.

O campo **"Bloco de aplicação"** indicará qual o evento de aplicação correspondente conforme o código de natureza inserido no campo, sendo esses:

- 4010;
- 4020;
- 4040;
- 4080.

Determine o **"Local de Aplicação"** dentre as opções **"Ambos"**, **"Financeiro"** ou **"Serviço"**.

Indique as **"Datas"** de início e fim da validade desses códigos.

Habilite a marcação **"Ativo"** para validar o código cadastrado.

Efetue a marcação **"Gerar sem tributação?"** quando o campo Tipo Tributo estiver vazio, conforme determinação da Receita Federal, assim, poderá ser enviado tanto nota sem retenção de impostos, considerando apenas o valor bruto da nota, como financeiro, considerando apenas valor do desdobramento do título, no [EFD - Reinf](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116553-EFD-Reinf). Nesse caso, os demais campos de valores da sub-aba Documentos, aba Rendimentos, do grupo de eventos 4000 na tela EFD REINF, serão gerados zerados. Porém, quando a marcação estiver desligada, indicando que o rendimento sofre tributação normalmente, o sistema irá validar se há retenções nas tabelas de impostos para gerar os dados no arquivo.

![Imagem 5: A fim de evitar retorno de erro da Receita Federal, utilize a marcação acima apenas nas condições citadas.](https://ajuda.sankhya.com.br/hc/article_attachments/18299418263063) A fim de evitar retorno de erro da Receita Federal, utilize a marcação acima apenas nas condições citadas.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/11790815385367-C%C3%B3digos-de-Naturezas-de-Rendimentos#top)
