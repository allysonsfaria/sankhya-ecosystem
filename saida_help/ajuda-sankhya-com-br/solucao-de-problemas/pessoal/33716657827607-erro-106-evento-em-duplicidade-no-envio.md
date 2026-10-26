---
id: "33716657827607"
titulo: "[Erro 106] Evento em duplicidade no envio ao e-Social"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33716657827607--Erro-106-Evento-em-duplicidade-no-envio-ao-e-Social"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-10-02T15:23:27Z"
rotulos: ["Eventos", "Fiscal", "Folha", "eSocial", "Central do eSocial", "Erro", "[Erro 106]", "Evento em duplicidade no envio ao e-Social", "S-1200 (Remuneração)", "S-1210 (Pagamentos"]
---

# [Erro 106] Evento em duplicidade no envio ao e-Social

**MENSAGEM:**

[Erro 106] Foi localizado no sistema um evento em duplicidade com o evento a ser enviado, mesmo Tipo de Inscrição, Número de Inscrição

**SITUAÇÃO:**

Ao tentar realizar o envio do evento **"S-1200 (Remuneração)",** **"S-1210 (Pagamentos)" e outros** eventos pela **"Central do eSocial"** (Pessoal+» Rotinas Folha» Central do eSocial) a mensagem de erro é apresentada.

**CAUSA:**

O erro ocorre quando há perda do recibo do evento. Isso acontece quando o envio ao portal do e-Social é concluído com sucesso, mas, devido a uma falha de conexão durante a transmissão do recibo para o sistema, a informação não é registrada corretamente.

Como resultado, o evento é gerado novamente e, ao tentar reenviá-lo, ocorre o erro de duplicidade, pois o e-Social já possui o evento registrado.

**SOLUÇÃO:**

**(1)** Realize a geração geral dos eventos no sistema; 

![Imagem 1: (1) Realize a geração geral dos eventos no sistema;](https://ajuda.sankhya.com.br/hc/article_attachments/33985448608151)

**(2)** Localize o evento e o colaborador correspondente:

- Clique em **"Alterar Dados";**

  ![Imagem 2: Clique em "Alterar Dados";](https://ajuda.sankhya.com.br/hc/article_attachments/33985448612247)

**(3)** Selecione a opção **"Finalizar Evento"** e insira o **número do recibo** disponível no portal do e-Social; 

![Imagem 3: (3) Selecione a opção "Finalizar Evento" e insira o número do recibo disponível no portal do e-Social; Repita o…](https://ajuda.sankhya.com.br/hc/article_attachments/33985448613399)

![Imagem 4: (3) Selecione a opção "Finalizar Evento" e insira o número do recibo disponível no portal do e-Social; Repita o…](https://ajuda.sankhya.com.br/hc/article_attachments/33985165750679) Repita o procedimento para todos os eventos que apresentaram erros; 

**(5)** Após ajustar os eventos que apresentaram erro, realize o envio de **um evento que tenha sido gerado e ainda não tenha sido enviado**. Essa etapa é necessária para que o sistema processe corretamente o retorno do eSocial e **efetive a gravação do número do recibo** no evento ajustado.

Caso não existam outros eventos pendentes para envio, realize o **envio do fechamento da referência**, garantindo que haja uma transmissão processada com sucesso para que a gravação do recibo seja concluída corretamente.

**Atenção:**  É essencial realizar o envio de um evento com sucesso após os ajustes. Apenas informar o número do recibo e finalizar o evento não é suficiente para concluir o processo de gravação no sistema. O envio bem-sucedido de um evento ou do fechamento da referência é necessário para que o número do recibo seja registrado corretamente e o evento deixe de ser considerado pendente ou seja gerado novamente.
