---
id: "360046065494"
titulo: "Configurações da DIRF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494-Configura%C3%A7%C3%B5es-da-DIRF"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > Declarações federais"
atualizado_em: "2026-09-15T17:35:50Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "Estoque", "Financeiro", "DIRF", "br.com.sankhya.mgeliv.ConfiguracoesDirf", "configurações da dirf", "Vincular movimentação: Código da Receita", "Marcar impostos: PIS COFINS CSLL IRF", "Origem informação: Estoque Financeiro"]
---

# Configurações da DIRF

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42313084643095) Módulo: Livros Fiscais > Arquivos ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42313084644375) Versão disponível: a partir da 4.2
```

---

Nesta tela, será vinculada a movimentação ao Código da Receita. Este incluirá as regras de busca de informações e identificará qual o imposto é correspondente a determinado código.

| [Aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494-Configura%C3%A7%C3%B5es-da-DIRF#abageral) |  | [Aba Naturezas (Financeiro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494-Configura%C3%A7%C3%B5es-da-DIRF#abanaturezas(financeiro)) |
| --- | --- | --- |
| [Aba Produtos\Serviços (Estoque)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494-Configura%C3%A7%C3%B5es-da-DIRF#abaprodutos\servi%C3%A7os(estoque)) |  |  |

![Imagem 3: Aba Produtos\Serviços (Estoque)](https://ajuda.sankhya.com.br/hc/article_attachments/1500003541042)

No campo **"Código"** deverá ser informado o código de receita vinculado ao imposto conforme a lista disponibilizada pela receita.

Em **"Descrição"** deve-se informar a descrição do código de acordo com a lista disponibilizada pela receita.

No campo **"Tipo de Pessoa"** você define se o cadastro em questão é para **"Pessoa Física"** ou **"Pessoa Jurídica"**.

## Aba Geral

Nesta aba, deverão ser marcados a quais impostos o código que foi preenchido no cabeçalho desta tela está vinculado. Por meio destas marcações, o sistema identificará quais valores deverão ser considerados para a geração dos campos **"Rendimentos Tributáveis"** e **"Imposto Retido"**. Sendo assim, tem-se as opções:

- Gerar para PIS?;
- Gerar para COFINS?;
- Gerar para CSLL?;
- Gerar para IRF?.

A marcação **"Gerar para imposto incluso?:"** deverá ser selecionada quando há a intenção de levar as informações dos impostos marcados acima que foram inclusos nos documentos.

Quando você habilitar a marcação **"Gerar para imposto não retido, Pessoa Física?"**, fará com que sejam gerados os valores quando houver e quando não houver IR retido. Caso não seja marcada, só serão gerados os valores quando houver IR retido.

**Observação:** será gerado apenas um registro RTRT, RTIF e RTPO para cada CPF.

O campo **"Gerar para imposto retido?:"** será marcado quando você desejar que os impostos que foram retidos sejam considerados na geração da DIRF.

Referente à seção **"Origem Informação"**, nesta teremos duas marcações que deverão ser selecionadas para informar quais tipos de lançamentos a regra deverá buscar as informações. Tem-se:

- **Estoque?:** O sistema buscará as informações das notas;
- **Financeiro?:** As informações serão provenientes do financeiro.

## Aba Naturezas (Financeiro)

Informa-se aqui, a natureza dos financeiros, caso não haja nenhuma natureza ativa na grade, as informações serão geradas para qualquer natureza.

## Aba Produtos\Serviços (Estoque)

Na aba Produtos\Serviços (Estoque) você irá especificar os produtos ou serviços das notas, se houver algum, caso não tenha nenhum produto ou serviço ativo na grade, as informações serão geradas para qualquer um.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046065494-Configura%C3%A7%C3%B5es-da-DIRF#top)

![Imagem 4: Veja também:](https://ajuda.sankhya.com.br/hc/article_attachments/16285057015959) Veja também:

[Geração do Arquivo DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046692113?flash_digest=948ac5ccfc067c01e2d3344aebbdadc8c43ab568)
