---
id: "360044594834"
titulo: "Liberação de Desvios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594834-Libera%C3%A7%C3%A3o-de-Desvios"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:44:24Z"
rotulos: ["Configuração", "Liberação de Limites", "Liberação de Desvios manual", "Apontamento", "Produção", "Controle de Desvios de Produção", "Desvio"]
---

# Liberação de Desvios

Este processo refere-se à Liberação de Desvios que ocorrerá somente se a marcação **"Solicitar Liberação ao exceder desvio"** estiver selecionada; assim, o sistema irá solicitar a liberação sempre que os valores dos desvios forem divergentes daqueles informados nos campos **"% Desvio Superior"** e **"% Desvio Inferior"** na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611314-Processo-Produtivo) ([botão Roteiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109793-Bot%C3%A3o-Roteiro), [aba Produtos (PA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#abaprodutospa), [sub-aba Lista de MPs](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601674-Configura%C3%A7%C3%A3o-de-Atividades#sub-abalistademps), sub-aba **"Desvios"**).

![Imagem 1: Este processo refere-se à Liberação de Desvios que ocorrerá somente se a marcação "Solicitar Liberação ao exceder…](https://ajuda.sankhya.com.br/hc/article_attachments/9451833298455)

**Importante:** a liberação deverá ser realizada apenas pelo usuário que possui permissão para este evento.

Para a confirmação do desvio de apontamento, considera-se que, se ao final de uma produção houver um desvio, este deverá ser informado na tela [Operações de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o), no campo **"Qtd. Apontada"** (aba [Apontamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611274-Opera%C3%A7%C3%B5es-de-Produ%C3%A7%C3%A3o#abaapontamentos), sub-aba **"Materiais"**).

Quando você confirmar o apontamento por meio do botão **"Confirmar"**, caso o percentual de desvio seja diferente daquele informado na aba Desvios, será aberto o pop-up **"Liberações solicitadas"** solicitando que o evento [81 - Desvio na quantidade apontada de PA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites#81-desvionaquantidadeapontadadepa) seja liberado:

![Imagem 2: Quando você confirmar o apontamento por meio do botão "Confirmar" , caso o percentual de desvio seja diferente daquele…](https://ajuda.sankhya.com.br/hc/article_attachments/9451870007575)

Ao clicar em **"Salvar"**, pode-se notar a mensagem ao lado do botão Confirmar:

**"Apontamento pendente, com solicitação de liberação"**

Ao solicitar a liberação, esta será executada na tela [Liberação de Limites](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601034-Libera%C3%A7%C3%A3o-de-Limites) pelo usuário liberador de tal processo, sendo assim, ao clicar no botão **"Liberar"**, será permitido que o  apontamento possa ser confirmado posteriormente na tela Operações de Produção, como exibido acima.

Caso você clique no botão **"Negar..."**, na tela Operações de Produção, o desvio não será aprovado e será exibida uma mensagem informando que não será possível a confirmação deste, pois a liberação em questão foi reprovada. Desta forma, deve-se remover o apontamento e criá-lo novamente.

**Observação:** caso o desvio seja inferior, o sistema terá o mesmo comportamento descrito acima.

**Nota:** para apontamentos de desvios que possuam mais de uma divergência, os valores destes deverão ser informados um a um no campo Qtd. Apontada para que sejam salvos e, em seguida, estas serão aprovadas ou negadas individualmente na tela de Liberações de Limites.

#### Liberação de Desvios -  Tela Apontamento de Produção

Nesta tela, o procedimento será o mesmo da tela Operações de Produção.

Quando o apontamento for confirmado e a solicitação de liberação lançada, o registro do apontamento será salvo na base de dados, ou seja, não ficará somente em memória como é feito com o apontamento regular.

![Imagem 3: Quando o apontamento for confirmado e a solicitação de liberação lançada, o registro do apontamento será salvo na base…](https://ajuda.sankhya.com.br/hc/article_attachments/9451923902999)

Com esta marcação habilitada, o sistema irá solicitar a liberação de limites do liberador, caso seja aprovada, a atividade poderá ser finalizada.
