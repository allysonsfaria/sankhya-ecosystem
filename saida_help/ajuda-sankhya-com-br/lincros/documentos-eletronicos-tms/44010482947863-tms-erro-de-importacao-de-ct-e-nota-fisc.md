---
id: "44010482947863"
titulo: "[TMS] - Erro de importação de CT-e: Nota fiscal não localizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010482947863--TMS-Erro-de-importa%C3%A7%C3%A3o-de-CT-e-Nota-fiscal-n%C3%A3o-localizada"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T18:39:20Z"
rotulos: ["sync_hc", "lincros", "lincros_13432835", "sync_hash_9270cfbee000"]
---

# [TMS] - Erro de importação de CT-e: Nota fiscal não localizada

**Menu**: Para verificar o CT-e > Documentos eletrônicos > CT-es
Para verificar a importação da NF-e > Documentos eletrônicos > NF-es
Para importar uma NF-e > Operacional > Importação > NF-e > Importação
Para importar um CT-e > Operacional > Importação > CT-e > Importação

**Objetivo**: Auxiliar o embarcador na resolução do erro de importação de CT-e: Nota fiscal não localizada;

**Considerações**
 - Possuir um CT-e com erro de importação, cuja mensagem aponte que as notas fiscais não foram localizadas;

**Por que ocorre esta situação?**
Costuma ocorrer quando um CT-e é enviado para importação antes da NF-e. Normalmente, ao validar a importação da NF-e, ela de fato não está importada. Mas, há ocasiões onde a nota está na plataforma, então, por que ocorre o erro?
Através dos históricos de importação, é possível validar os horários de importação dos dois arquivos (CT-e e NF-e). Muitas vezes, há uma diferença de minutos entre a importação de um arquivo e outro, onde o CT-e entra antes e causa esta situação;

**Atenção — nem toda mensagem de "nota fiscal não localizada" é esse cenário de timing:** antes de seguir o passo a passo abaixo, confirme se o CT-e realmente referencia uma NF-e. Se, ao verificar o XML, o documento vinculado ao CT-e for do tipo **Malote (documento não fiscal, código 99)**, é esperado que ele não referencie nenhuma NF-e — a transportadora emitiu o CT-e sem associar uma nota fiscal a ele, e não há nota "não localizada" para importar. Nesse caso, o ajuste não é técnico: verifique junto à transportadora se a modalidade do documento (Malote x CT-e vinculado a NF-e) está correta para a operação.

## Validando o erro de importação do CT-e

1. Acesse a tela de listagem de CT-es e busque pelo CT-e com erro de importação. Pode ser através da chave ou número;

   ![Imagem 1: Acesse a tela de listagem de CT-es e busque pelo CT-e com erro de importação. Pode ser através da chave ou número;](https://ajuda.sankhya.com.br/hc/article_attachments/44010465878935)
2. Acesse o CT-e com erro de importação e role a página até a seção 'Mensagem de importação'. Nesta seção, a mensagem estará informando o número da chave das notas fiscais que não foram localizadas no momento da importação;

   ![Imagem 2: Acesse o CT-e com erro de importação e role a página até a seção 'Mensagem de importação'. Nesta seção, a mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/44010499274135)

**Verificando se as NF-es estão importadas**

1. Copie a chave de cada uma das notas para verificar se elas de fato ainda não foram importadas. Na tela de listagem de notas fiscais (Documentos eletrônicos → NF-es), informe as chaves separadas por ;.

Caso seja exibida a mensagem 'Nenhum registro encontrado', significa que é necessário importar a NF;

![Imagem 3: Caso seja exibida a mensagem 'Nenhum registro encontrado', significa que é necessário importar a NF;](https://ajuda.sankhya.com.br/hc/article_attachments/44010466155287)

2. A tela de listagem de NF-es possui um filtro de 30 dias, então, caso se trate de um documento antigo, utilize o botão 'Filtros' e limpe a data de início.

![Imagem 4: 2. A tela de listagem de NF-es possui um filtro de 30 dias, então, caso se trate de um documento antigo, utilize o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010466349335)

Se a NF-e de fato não estiver importada, será necessário realizar a importação desta para depois disso, seguir para o próximo passo. Caso a nota esteja importada com situação 'Gerada';

![Imagem 5: Se a NF-e de fato não estiver importada, será necessário realizar a importação desta para depois disso, seguir para o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010515773719)

1. Acesse a nota, clicando em seu número e verifique a modalidade de frete. Verifique se é modalidade de frete 9, a nota estará com 0 conhecimentos;

   ![Imagem 6: Acesse a nota, clicando em seu número e verifique a modalidade de frete. Verifique se é modalidade de frete 9, a nota…](https://ajuda.sankhya.com.br/hc/article_attachments/44010508770583)
2. Clique no botão 'Adicionar conhecimento';
3. Confirme clicando em 'Sim';

   ![Imagem 7: Confirme clicando em 'Sim';](https://ajuda.sankhya.com.br/hc/article_attachments/44010495882519)
4. Feito isto, siga para o próximo passo;

## Como reimportar o CT-e

1. Retorne para a tela do CT-e;
2. Clique no botão 'Download XML';

   ![Imagem 8: Clique no botão 'Download XML';](https://ajuda.sankhya.com.br/hc/article_attachments/44010466916759)
3. Um arquivo zipado será baixado. Verifique na pasta de downloads, buscando por um arquivo de nome 'CT-es.zip' ou semelhante.

   ![Imagem 9: Um arquivo zipado será baixado. Verifique na pasta de downloads, buscando por um arquivo de nome 'CT-es.zip' ou…](https://ajuda.sankhya.com.br/hc/article_attachments/44010516479255)
4. Acesse o menu de importação de CT-e em: Operacional > Importação > CT-e > Importação;
5. Arraste o arquivo baixado anteriormente para a área indicada, ou utilize o botão Adicionar;

   ![Imagem 10: Arraste o arquivo baixado anteriormente para a área indicada, ou utilize o botão Adicionar;](https://ajuda.sankhya.com.br/hc/article_attachments/44010500782359)
6. Após seguir este passo a passo, o erro de importação do CT-e estará corrigido;

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
