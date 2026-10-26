---
id: "44012656086935"
titulo: "[TMS] - Integração de Embarques Routing x TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012656086935--TMS-Integra%C3%A7%C3%A3o-de-Embarques-Routing-x-TMS"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:18Z"
rotulos: ["sync_hc", "lincros", "lincros_13433404", "sync_hash_46c8d5ed26db"]
---

# [TMS] - Integração de Embarques Routing x TMS

**Menu: -**No roteirizador acessar a tela da sessão do Embarque/Rota;

- No TMS acessar o menu: Operacional > Importações > Cargas > Embarques > Log;

**Objetivo**: Como analisar e verificar a integração de Embarques do Router para o TMS.

**Considerações**:

- Neste momento, é importante ter em mãos todas as informações da sessão e pedidos contidos dentro das rotas;
- Com o numero da sessão e pedidos conseguimos analisar o log da integração do embarque entre o Router e o TMS;
- Embarques já integrados com o TMS é necessário desbloquear a sessão no Roteirizador para novamente podermos enviar ao TMS;

OBS: Verificar se no TMS já não consta o embarque para o pedido. Pois está ação irá descontruir os vínculos que já foram atribuídos ao embarque. Exemplo: tabela de preço.

 Para analisar a integração de Embarques entre o Router e o TMS, iremos precisar acessar as seguintes telas:

1. No roteirizador acessar a tela da sessão do Embarque/Rota;
2. No TMS acessar o menu: Operacional>Importações>Cargas>Embarques>Log;

Primeiro devemos analisar se o Embarque de fato chegou no log de importação do TMS, e em qual situação está o status do embarque:

![Imagem 1: Primeiro devemos analisar se o Embarque de fato chegou no log de importação do TMS, e em qual situação está o status do…](https://ajuda.sankhya.com.br/hc/article_attachments/44012663088023)

No caso evidenciado temos status com erro de integração e outros que foram integrados normalmente.

Na tela do filtro de importação conseguimos pesquisar pela data e horário assim como, unidade, grupo de unidade e transportadora.

![Imagem 2: Na tela do filtro de importação conseguimos pesquisar pela data e horário assim como, unidade, grupo de unidade e…](https://ajuda.sankhya.com.br/hc/article_attachments/44012649782679)

Para analisarmos uma integração com erro basta clicar sobre o campo código, no log de importações com erro:

![Imagem 3: Para analisarmos uma integração com erro basta clicar sobre o campo código, no log de importações com erro:](https://ajuda.sankhya.com.br/hc/article_attachments/44012656487575)

No caso o embarque abaixo não foi integrado por não ter localizado a pré nota dentro do TMS:

![Imagem 4: No caso o embarque abaixo não foi integrado por não ter localizado a pré nota dentro do TMS:](https://ajuda.sankhya.com.br/hc/article_attachments/44012618341911)

Ela pode ter sido excluída do TMS, e ao fazer o retorno ao TMS não localizar a pré-nota. Como o usuário de integração pode não ter acesso a integrar Embarques/Rotas desta unidade de negócios.

 Há casos em que a integração foi efetuada, porem a situação do embarque está em amarelo(Em importação) Neste caso será necessário verificar se não há uma instabilidade na plataforma do TMS.

![Imagem 5: Há casos em que a integração foi efetuada, porem a situação do embarque está em amarelo(Em importação) Neste caso será…](https://ajuda.sankhya.com.br/hc/article_attachments/44012656716823)

Caso a exportação tenha sido efetuada do Roteirizador para o TMS e não aparecer no log de importação do Embarque será necessário exportar a sessão para o TMS novamente em Exportar sessão dentro da sessão do Roteirizador:
OBS Desbloquear a sessão primeiramente.

![Imagem 6: Caso a exportação tenha sido efetuada do Roteirizador para o TMS e não aparecer no log de importação do Embarque será…](https://ajuda.sankhya.com.br/hc/article_attachments/44012663932823)

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
