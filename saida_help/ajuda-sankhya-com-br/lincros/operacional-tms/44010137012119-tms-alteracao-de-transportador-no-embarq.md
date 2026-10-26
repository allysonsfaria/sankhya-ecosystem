---
id: "44010137012119"
titulo: "[TMS] - Alteração de transportador no embarque e no pré-conhecimento: cenários e restrições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010137012119--TMS-Altera%C3%A7%C3%A3o-de-transportador-no-embarque-e-no-pr%C3%A9-conhecimento-cen%C3%A1rios-e-restri%C3%A7%C3%B5es"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:30:27Z"
rotulos: ["sync_hc", "lincros", "lincros_13433331", "sync_hash_f4a5a65dea51"]
---

# [TMS] - Alteração de transportador no embarque e no pré-conhecimento: cenários e restrições

**Menu**: Operacional > Cargas > Embarques

**Objetivo**: Como realizar a alteração do transportador no embarque e no pré-conhecimento, e quais restrições se aplicam em cada cenário

**Considerações**:

- Quando o pré-conhecimento está vinculado a um embarque, a transportadora **não é alterada diretamente no pré-conhecimento**: a alteração deve ser feita no embarque, e o ajuste é refletido nos dois;
- Possuir um embarque vinculado ao pré conhecimento;

Abaixo segue os procedimentos:

1. Verifique se o embarque e o pré conhecimento estão vinculados no caminho: Operacional > Cargas > Embarques;

   ![Imagem 1: Verifique se o embarque e o pré conhecimento estão vinculados no caminho: Operacional > Cargas > Embarques;](https://ajuda.sankhya.com.br/hc/article_attachments/44010131115031)
2. Com o vínculo realizado, caso a transportadora esteja incorreta no pré-conhecimento e no embarque, a mesma pode ser alterada no embarque no item 'Cargas', conforme print abaixo:

   ![Imagem 2: Com o vínculo realizado, caso a transportadora esteja incorreta no pré-conhecimento e no embarque, a mesma pode ser…](https://ajuda.sankhya.com.br/hc/article_attachments/44010131303447)

**Importante**: Esse ajuste não se aplica, caso o embarque tenha uma cotação spot confirmada;

1. Após realizar a alteração da transportadora, clicar em 'Salvar';
2. O ajuste será aplicado tanto no pré-conhecimento quanto no embarque, ou seja, ambos ficarão com a mesma transportadora.

## Situações em que a alteração é bloqueada ou exige outro caminho

- **Não encontro o embarque do pré-conhecimento:** se a busca em Operacional > Cargas > Embarques retornar 'Nenhum registro encontrado', o pré-conhecimento pode não estar vinculado a nenhum embarque. Confirme o vínculo pelo pré-conhecimento antes de seguir; sem embarque, este procedimento não se aplica;
- **Documentos fiscais já vinculados ao embarque:** em embarques roteirizados, o Lincros não permite alterar ou remover a transportadora quando o embarque já possui documentos fiscais vinculados;
- **Redespacho:** a transportadora do pré-conhecimento de Redespacho precisa ser diferente da transportadora do pré-conhecimento Normal de origem. Se a transportadora informada for a mesma da origem, o sistema não permite salvar;
- **Cotação spot confirmada:** conforme informado acima, a alteração no embarque não se aplica;
- **Ordem de coleta confirmada/enviada à transportadora:** consulte o artigo '[TMS] - Alteração da transportadora de um pré-conhecimento vinculado a uma ordem de coleta confirmada/enviada à transportadora'.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
