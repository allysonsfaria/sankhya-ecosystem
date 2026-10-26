---
id: "360045120293"
titulo: "Conferência Manual"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120293-Confer%C3%AAncia-Manual"
trilha: "Manual do Produto > Suprimentos e Estoque > WMS"
atualizado_em: "2026-07-29T14:15:51Z"
rotulos: ["Pedidos", "AJUDA DO SKW", "manual", "Conferência", "WMS", "Expedição", "Conferência Manual", "br.com.sankhya.wms.conferenciamanualsimples", "Conferência Manual manual", "Conferência de Pedidos e Peças", "Tratamento de Divergências", "Finalização e Envio para Doca", "Coletor de Dados"]
---

# Conferência Manual

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311599058455) Módulo: WMS > Rotinas
```

---

Pedidos que estão com status **"Aguardando Conferência"** poderão ser conferidos tanto pelo Coletor de Dados quanto manualmente através desta rotina do Sankhya Om. Porém, uma vez iniciado o processo, ele deverá ser finalizado da mesma forma, ou seja, se a conferência for iniciada pelo Coletor deverá ser concluída pelo mesmo e, se for iniciada pela tela de Conferência Manual, deverá ser concluída através dela.

[Conferência por pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120293-Confer%C3%AAncia-Manual#confer%C3%AAnciaporpedido)                                                    [Conferência por peça](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120293-Confer%C3%AAncia-Manual#confer%C3%AAnciaporpe%C3%A7a)

![Imagem 2: Conferência por pedido Conferência por peça](https://ajuda.sankhya.com.br/hc/article_attachments/1500000776962)

No caso da Conferência ser realizada manualmente pelo Sankhya Om, quando finalizada, deverá ser enviada para a doca por meio do botão **"Enviar para a Doca..."**.

Quando a conferência for efetuada em áreas de **"Não paletizados"**, não deverá ser informado a **"Área de conferência"**.

Assim, finalizadas a rotina de Conferência, a situação da expedição no WMS passará a ser **"Conferência Validada"**, a partir deste momento para conclusão do processo será necessário apenas a liberação da doca.

## Conferência por pedido

O parâmetro **"Quantidade padrão na conferência por pedidos - QTDCONFPEDWMS"** quando ativado, permitirá a inserção da quantidade que será exibida no campo **"Quantidade"** no momento da conferência.

O parâmetro **"Proibir digitação de qtd. na conferência por pedido - PROIBDIGCONFPED"** inibe a edição do campo Quantidade e funciona em conjunto com o parâmetro QTDCONFPEDWMS; caso o mesmo não possua quantidade padrão, o campo não será desabilitado.

**Observação:** quando um pedido é enviado para expedição através da opção **"Enviar para o WMS (Expedição)"** disponível no botão [Outras Opções...](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604014) da tela [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654), para que seja realizada a Conferência de Saída através do Coletor de Dados, ao bipar um produto controlado por Série, o sistema identifica esta característica e solicitará que o conferente informe o número de série correspondente ao produto em questão, de modo que este número seja apresentado na Nota Fiscal que será gerada.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120293-Confer%C3%AAncia-Manual#top)

## Conferência por peça

Após uma conferência por peça que possua divergência, no Sankhya Om acessamos a tela de [Expedição de Mercadorias](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044611474) para aplicar a tratativa de recontagem na separação.

[GIF animado: Imagem 3: Após uma conferência por peça que possua divergência, no Sankhya Om acessamos a tela de Expedição de Mercadorias para…](https://ajuda.sankhya.com.br/hc/article_attachments/360061028174)

No coletor será puxada a tarefa de Conferência por Peça e logo após iniciada a Recontagem, você deverá realizar a leitura do endereço de checkout para que o sistema busque as informações do endereço e descubra se esta é a primeira recontagem ou se é outra subsequente. No caso da primeira recontagem, ela será realizada conforme a conferência por peça, você insere a quantidade de peças e depois realiza a leitura do código de barras de uma das peças. Se tudo estiver "OK", a conferência será validada.

[GIF animado: Imagem 4: No coletor será puxada a tarefa de Conferência por Peça e logo após iniciada a Recontagem , você deverá realizar a…](https://ajuda.sankhya.com.br/hc/article_attachments/360061944613)

Caso a recontagem apresente uma nova divergência, a mesma deverá ser tratada no pop-up de divergência da tela de Expedição de Mercadorias. No coletor o usuário deve selecionar a tarefa de Conferência por peça e clicar em recontagem.

Após realizar a leitura do endereço, o sistema captura a informação se a recontagem já é uma segunda ou outra subsequente e entrega uma tela que espera do usuário a leitura de item a item, o usuário tem que realizar a leitura pelo coletor de cada item no checkout. Depois de ler item a item deverá ser enviada a recontagem, caso não tenha divergência a conferência é validada.

Caso contrário, será apresentada a tela de **"Troca de Lote"**, na qual será:

**1.** Informado que houve uma divergência e a quantidade divergente;

**2.** Sugerido que você encontre um endereço que tenha a quantidade;

Você irá realizar a leitura de um endereço e do produto, se o endereço for:

- **O próprio checkout:** O botão **"Excluir lote"** será habilitado e deverá ser acionado, dessa forma o item bipado será excluído da recontagem e será movimentado de forma atômica para o endereço de retorno de expedição;
- **Um picking:** O botão **"Adicionar lote"** será habilitado e deverá ser acionado, dessa forma o item bipado será adicionado à recontagem, sendo realizada uma movimentação de forma atômica do endereço que não era o checkout para o endereço de checkout;

Ao terminar as movimentações para suprir a quantidade necessária, acione o botão **"Concluir"** para que o sistema considere os itens adicionados e os primeiros recontados antes da tela de troca de lote. Os outros que ainda não foram encontrados, será gerada tarefas atômicas para o endereço de divergência automaticamente.

[GIF animado: Imagem 5: Ao terminar as movimentações para suprir a quantidade necessária, acione o botão "Concluir" para que o sistema…](https://ajuda.sankhya.com.br/hc/article_attachments/360061944653)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120293-Confer%C3%AAncia-Manual#top)
