---
id: "44010479431319"
titulo: "[TMS] Como realizar a anulação de um CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010479431319--TMS-Como-realizar-a-anula%C3%A7%C3%A3o-de-um-CT-e"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T18:39:01Z"
rotulos: ["sync_hc", "lincros", "lincros_13434440", "sync_hash_2d5fa6c03eac"]
---

# [TMS] Como realizar a anulação de um CT-e

**Menu**: Documentos eletrônicos > CT-es
**Objetivo**: Entender qual o procedimento para realizar a anulação de um CT-e dentro do TMS.

**Considerações:**

- Ter um CT-e importado via CONEMB e ou via XML na plataforma TMS

No dia a dia de um processo logístico em alguns momentos se faz necessário a anulação de um CT-e, isso pode ocorrer devido a vários fatores, como por exemplo, a emissão do CT-e com informações erradas. Podemos apontar outro exemplo mais pratico como por exemplo quando a transportadora emite uma fatura contendo seus CT-es, mas, um desses CT-es foi emitidos erroneamente, para que possamos descartar esse CT-e para que o mesmo não seja levado em conta no cálculo realizado, podemos fazer a anulação do CT-e.

No exemplo abaixo, temos uma fatura vinculada a dois CT-es sendo que um dos CT-e foi emitido erroneamente, com isso, o valor calculado e realizado fica diferente do valor faturado:

![Imagem 1: No exemplo abaixo, temos uma fatura vinculada a dois CT-es sendo que um dos CT-e foi emitido erroneamente, com isso, o…](https://ajuda.sankhya.com.br/hc/article_attachments/44010481354135)

Neste caso, sabemos que o CT-e incorreto é o de número 6229, podemos observar isso dentro da fatura na aba "Conhecimentos eletrônicos" :

![Imagem 2: Neste caso, sabemos que o CT-e incorreto é o de número 6229, podemos observar isso dentro da fatura na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/44010481541655)

Para realizar a anulação do CT-e precisamos acessar o mesmo, isso pode ser feito tanto pela tela de faturas conforme mostrado na imagem acima clicando no número do CT-e, ou então, acessando o CT-e pela tela: Documentos eletrônicos > CT-es

Uma vez acessado, vamos observar que existe um botão chamado 'Anular':

![Imagem 3: Uma vez acessado, vamos observar que existe um botão chamado 'Anular':](https://ajuda.sankhya.com.br/hc/article_attachments/44010506540183)

Ao clicar nele e caso esse CT-e esteja vinculado a uma fatura o TMS vai apresentar uma mensagem de aviso, com os dados da fatura, exemplo:

![Imagem 4: Ao clicar nele e caso esse CT-e esteja vinculado a uma fatura o TMS vai apresentar uma mensagem de aviso, com os dados…](https://ajuda.sankhya.com.br/hc/article_attachments/44010482029207)

Clicando em 'Sim' o TMS irá solicitar um motivo da anulação, que pode ser um texto livre, podendo ser encaminhado via E-mail, conforme imagem abaixo:

![Imagem 5: Clicando em 'Sim' o TMS irá solicitar um motivo da anulação, que pode ser um texto livre, podendo ser encaminhado via…](https://ajuda.sankhya.com.br/hc/article_attachments/44010498045463)

Logo após a anulação do CT-e, podemos voltar a fatura de exemplo e vamos perceber que a tela de 'Conhecimentos eletrônicos' está agora, com apenas 1 CT-e:

![Imagem 6: Logo após a anulação do CT-e, podemos voltar a fatura de exemplo e vamos perceber que a tela de 'Conhecimentos…](https://ajuda.sankhya.com.br/hc/article_attachments/44010514224663)

Para nossa validação final, podemos voltar para a tela de fatura e visualizar o descritivo dos valores:

![Imagem 7: Para nossa validação final, podemos voltar para a tela de fatura e visualizar o descritivo dos valores:](https://ajuda.sankhya.com.br/hc/article_attachments/44010494297239)

Outra forma de anulação de um CT-e é a importação do evento de cancelamento, o evento de cancelamento se trata de um XML emitido pela transportadora e pode ser importado por esse caminho: Operacional > Importação > Eventos CT-e > Importação

**Importante**: A anulação de um CT-e deve ser alinhada previamente com a transportadora que emitiu o CT-e.

## Anulação (botão "Anular") x Cancelamento (evento SEFAZ): quando dá para reverter

As duas ações descritas acima levam o CT-e a situações diferentes no sistema, e isso muda o que é possível fazer depois:

- **Anulação pelo botão "Anular" (situação fica ANULADO):** essa é uma ação feita diretamente no TMS, sem depender de um evento da SEFAZ. Se a anulação foi feita **por engano** — por exemplo, anulou-se o CT-e errado, ou não era realmente necessário anular — **é possível reverter**. Acesse novamente o CT-e (Documentos eletrônicos > CT-es) e utilize o botão **"Reabrir"**: o CT-e retorna para a situação anterior (Não faturado ou Faturado, conforme o contexto em que estava antes da anulação), e o histórico da reabertura fica registrado no CT-e.
- **Cancelamento via importação do evento SEFAZ (situação fica CANCELADO):** quando o CT-e é anulado através da importação do evento de cancelamento (XML autorizado pela SEFAZ, emitido pela transportadora), a situação resultante é **diferente** da anulação manual e **não tem opção de reabertura** no sistema. Isso é esperado: o cancelamento já foi formalmente registrado e autorizado na SEFAZ, então não é uma ação que o TMS possa desfazer unilateralmente. Se o CT-e foi cancelado indevidamente nesse fluxo, a correção não é "reabrir" — é necessário que a transportadora emita a documentação corretiva cabível junto à SEFAZ (por exemplo, um novo CT-e) para regularizar a operação.

**Resumo prático:** se você anulou o CT-e pelo botão "Anular" e foi engano, use "Reabrir". Se o CT-e está com o evento de cancelamento da SEFAZ importado, não existe botão de reabertura — trate como definitivo e alinhe com a transportadora a emissão do documento correto.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
