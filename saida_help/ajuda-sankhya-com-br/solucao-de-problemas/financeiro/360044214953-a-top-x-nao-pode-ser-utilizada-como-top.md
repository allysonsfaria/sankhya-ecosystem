---
id: "360044214953"
titulo: " A Top 'X' não pode ser utilizada como Top para Baixa de acordo com as configurações de restrição/exceção da TOP 'Y' do financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044214953--A-Top-X-n%C3%A3o-pode-ser-utilizada-como-Top-para-Baixa-de-acordo-com-as-configura%C3%A7%C3%B5es-de-restri%C3%A7%C3%A3o-exce%C3%A7%C3%A3o-da-TOP-Y-do-financeiro"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:40Z"
rotulos: ["#criadoRoger", "CORE_E02934", "Configuração", "Movimentação Financeira", "TOP", "Financeiro", "Ajuste de Restrições na Baixa Financeira", "Baixa de Títulos Financeiros", "Restrição de Baixa na TOP Financeira", "Erro"]
---

#  A Top 'X' não pode ser utilizada como Top para Baixa de acordo com as configurações de restrição/exceção da TOP 'Y' do financeiro

**![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/16197114428951) MENSAGEM**

[CORE\_E02934] A Top 'X' não pode ser utilizada como Top para Baixa de acordo com as configurações de restrição/exceção da TOP 'Y' do financeiro.

**![Imagem 2: SITUAÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16197119083543) SITUAÇÃO**

Ao clicar em **"Baixar"** um titulo Financeiro, ocorre a mensagem

**![Imagem 3: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/16197119085079) SOLUÇÃO**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16197119086359) Acesse: Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP

Identifique a TOP de Financeiro (Tipo de Movimento= I-Financeiro), do título e pesquise no cadastro de TOP.

![Imagem 5: Acesse o botão: "Outras Opções" , opção "Restrições/Exceções"](https://ajuda.sankhya.com.br/hc/article_attachments/16197114443415) Acesse o botão: **"Outras Opções"**, opção **"Restrições/Exceções"**

Identifique na opção **"TOP para Baixa"** a respectiva restrição que está impedindo a baixa com determinada TOP de Recebimento/Pagamento.

![Imagem 6: Identifique na opção "TOP para Baixa" a respectiva restrição que está impedindo a baixa com determinada TOP de…](https://ajuda.sankhya.com.br/hc/article_attachments/14612256427543)

- Se for um Despesa, a TOP de Baixa que estará vinculado será uma TOP de Pagamento
- Se for uma Receita, a TOP de Baixa que estará vinculado será uma TOP de Recebimento.

**(1)** Sugerimos que alinhe com o Gestor Financeiro para que possa verificar a restrição feita e entender o motivo e, caso seja necessário, efetuar o ajuste ou efetuar a baixa com a TOP que é permitido.

**![Imagem 7: CAUSA](https://ajuda.sankhya.com.br/hc/article_attachments/16197114448535) CAUSA**

Ocorre quando há restrição/exceção na TOP de Financeiro, limitando quais são as TOP's de Baixa que podem ser usadas.
