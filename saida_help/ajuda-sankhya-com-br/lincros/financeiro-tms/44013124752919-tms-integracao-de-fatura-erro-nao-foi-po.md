---
id: "44013124752919"
titulo: "[TMS] - Integração de fatura - Erro: Não foi possível determinar o tipo de frete"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013124752919--TMS-Integra%C3%A7%C3%A3o-de-fatura-Erro-N%C3%A3o-foi-poss%C3%ADvel-determinar-o-tipo-de-frete"
trilha: "Lincros > TMS > Financeiro - TMS"
atualizado_em: "2026-10-05T19:47:52Z"
rotulos: ["sync_hc", "lincros", "lincros_13432955", "sync_hash_54b19f32d0b3"]
---

# [TMS] - Integração de fatura - Erro: Não foi possível determinar o tipo de frete

**Menu**: Financeiro > Faturas

**Objetivo**: Ao realizar a integração da fatura está ocorrendo a seguinte mensagem: "Não foi possível determinar o tipo de frete"

**Considerações**:

- Possuir faturas cadastradas/importadas no sistema;

Segue abaixo os procedimentos:

1. Esta mensagem ocorre, pois existe alguma nota fiscal vinculada a fatura que está sem a natureza de operação informada;
2. Através da chamada via postman é possível descobrir qual nota fiscal está sem a natureza de operação, abaixo segue um exemplo:

   ![Imagem 1: Através da chamada via postman é possível descobrir qual nota fiscal está sem a natureza de operação, abaixo segue um…](https://ajuda.sankhya.com.br/hc/article_attachments/44013124987031)
3. Na chamada acima, pesquisar pelo campo 'ValorProporcionalICMS’, conforme exemplo abaixo:

   ![Imagem 2: Na chamada acima, pesquisar pelo campo 'ValorProporcionalICMS’, conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013108769815)
4. Verificar que abaixo desse campo, não tem o campo informando a natureza de operação, logo é essa nota que está com problema;
5. Após, basta consultar a mesma no menu: Operacional > Documentos de despacho > Notas Fiscais;

   ![Imagem 3: Após, basta consultar a mesma no menu: Operacional > Documentos de despacho > Notas Fiscais;](https://ajuda.sankhya.com.br/hc/article_attachments/44013108907799)
6. Sendo assim, é necessário informar qual a natureza de operação desta nota fiscal;
7. Após, basta clicar em 'Salvar' e importar novamente o arquivo da fatura;

**Obs.:** Mesmo que o Ct-e e as notas fiscais foram importadas com sucesso é no momento da importação da fatura que é feito essa validação.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
