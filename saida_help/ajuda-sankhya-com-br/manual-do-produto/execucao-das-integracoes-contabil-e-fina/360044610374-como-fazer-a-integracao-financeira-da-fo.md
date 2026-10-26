---
id: "360044610374"
titulo: "Como fazer a integração financeira da folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610374-Como-fazer-a-integra%C3%A7%C3%A3o-financeira-da-folha"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Execução das Integrações Contábil e Financeira"
atualizado_em: "2026-10-05T18:06:32Z"
rotulos: ["Configuração", "Movimentação Financeira", "Integração Financeira", "Financeiro", "Folha", "ID: br.com.sankhya.rh.GerenciadorFolha", "Gerenciador de Folhas", "Guia para Integração Financeira de Folha"]
---

# Como fazer a integração financeira da folha

A **Integração Financeira** é o processo no qual são enviados os dados do líquido da folha para o setor financeiro da empresa, o qual fará a baixa para realização dos pagamentos. Portanto, é um processo que só é possível após a realização do cálculo da folha de pagamento e quando a folha não tiver com avisos e advertências.

Para realizar a **Integração Financeira** é necessário que se tenha efetuado previamente a [Configuração de Integração Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/10219654027799). Sendo que, essa integração faz parte do [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599).

Antes de iniciar o procedimento, confira se o card da folha está com o status **"Pronto para a Integração Financeira"** e sem o símbolo amarelo de avisos pendentes. Esse símbolo indica que ainda existem avisos ou advertências não resolvidos no cálculo, e a integração não deve ser realizada enquanto eles não forem conferidos. Para ver quais avisos existem e a quais funcionários eles se referem, abra o card da folha no **Gerenciador de Folhas** e consulte a aba **Avisos**.

Para realizar a integração financeira, acesse o gerenciador e selecione o card que deseja realizar a integração. Ele deve estar com o status **"Pronto para a Integração Financeira"**.

![Imagem 1: Para realizar a integração financeira, acesse o gerenciador e selecione o card que deseja realizar a integração. Ele…](https://ajuda.sankhya.com.br/hc/article_attachments/360061939613)

Ao clicar na aba **"Folha"**, ative o **"Modo Seleção"** por meio do botão localizado na parte superior direita. Depois, deverá filtrar os funcionários que estão prontos para a integração e selecioná-los. Posteriormente, acione o botão **"Realiza Integração Financeira"**.

[GIF animado: Imagem 2: Ao clicar na aba " Folha" , a tive o " Modo Seleção" por meio do botão localizado na parte superior direita. Depois,…](https://ajuda.sankhya.com.br/hc/article_attachments/360061020414)

Após preencher os campos obrigatórios, selecione a Configuração para Integração Financeira previamente cadastrada e clique no botão **"Confirma integração"** para iniciar o processo de integração.

Pronto, a Integração Financeira dos funcionários selecionados foi realizada com sucesso.

**Importante:** para levar o centro de custo corretamente para a Movimentação Financeira (TGFFIN) são necessárias as configurações abaixo:

- Caso a empresa opte por utilizar o centro de custo do departamento do funcionário para ambas as integrações financeiras da folha, não realize a marcação **"Utiliza Centro de resultado"** das [Preferências da Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa).
- Caso contrário, temos as possibilidades:

1. Na Integração Financeira sem lançamento único, cadastre um centro de custo válido na Empresa.
2. Na Integração Financeira com lançamento único, cadastre um centro de custo válido na Configuração de Integração Financeira.

**Observação:** quando houver cálculo de rateio para um funcionário, o sistema irá considerar o centro de resultado do próprio rateio e não o centro de resultado do departamento. Para rateios com um único Centro de Resultado ou Projeto, veja a configuração adicional necessária em [Rateios da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/7092297445911).
