---
id: "42427259079703"
titulo: "Por que não utilizar dispensa para descontar a ausência do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427259079703-Por-que-n%C3%A3o-utilizar-dispensa-para-descontar-a-aus%C3%AAncia-do-colaborador"
trilha: "PONTOTEL: Sistema de marcação de ponto > Folha de ponto"
atualizado_em: "2026-08-07T16:17:45Z"
rotulos: ["sync_hc", "pontotel_6a3329d72dbb32f7f5ec552b", "pontotel", "sync_hash_a3b8fa08b24b"]
---

# Por que não utilizar dispensa para descontar a ausência do colaborador

Quando um colaborador não comparece ao trabalho, o sistema registra automaticamente essa ausência como falta, ou convertendo-a para banco de horas caso haja regra de banco ativa para o colaborador, desde que a jornada esperada para o dia seja de trabalho. No entanto, uma dúvida comum entre gestores é se a justificativa "dispensa" pode ser utilizada quando o objetivo é descontar o dia do colaborador.

A resposta é: **não**. Isso porque a dispensa não é interpretada como uma falta, e sim como uma **ausência justificada**. Vamos entender melhor a diferença entre esses conceitos e como utilizar corretamente cada um.

## Qual a diferença entre falta e dispensa?

- **Falta:** ocorre quando o colaborador não comparece ao trabalho sem uma justificativa válida. Dependendo da política da empresa, essa ausência pode resultar em desconto na folha de pagamento ou abatimento do saldo no banco de horas. Para saber como converter uma falta para banco de horas ou reprovar o saldo acumulado para que seja gerado o evento de falta, consulte este [artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427328039447).
- **Dispensa:** é uma justificativa utilizada quando a empresa libera o colaborador do expediente sem prejuízo salarial. Ou seja, o sistema entende que essa ausência foi autorizada pela empresa e, por isso, não gera descontos na folha nem afeta o saldo do banco de horas.

## Dúvidas comuns sobre dispensa

1. **Por que a dispensa não deve ser utilizada para descontar a ausência?**

   Se o objetivo for descontar a ausência do colaborador, seja no pagamento ou no banco de horas, o ideal é **permitir que o sistema registre a falta automaticamente**, sem utilizar a justificativa "dispensa". Isso porque a**dispensa abona a falta do dia.**
   Por padrão, ao lançar uma dispensa, o sistema entende que a ausência foi concedida pela empresa e, portanto, não gera desconto no dia em questão.

   **Existe uma exceção:** é possível registrar uma falta junto com um lançamento de dispensa, mas essa opção é voltada para dias sem jornada de trabalho esperada ou para casos em que a justificativa de dispensa precisa ser registrada, mas sem abonar o período dispensado. Nesse caso, não há possibilidade de gerar um desconto parcial, ou seja, o dia inteiro será considerado como falta. Caso a dispensa seja lançada parcialmente, a falta não será registrada.
   Para lançar a dispensa registrando um falta no dia, habilite a opção **"dia inteiro"** na seção "informações da dispensa", e escolha a opção **"considerar como falta"** na seção "configurações de cálculo".

   ![Imagem 1: Existe uma exceção: é possível registrar uma falta junto com um lançamento de dispensa, mas essa opção é voltada para…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_4pzc6e.png)

   ![Imagem 2: Existe uma exceção: é possível registrar uma falta junto com um lançamento de dispensa, mas essa opção é voltada para…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_jcvx1x.png)
2. **Por que a dispensa não gera saldo negativo no banco de horas?**

   Se o colaborador utiliza banco de horas, a ausência só será descontada do saldo caso seja considerada como falta. Se for utilizada a justificativa de dispensa sem essa opção marcada, o sistema não computará a ausência como saldo negativo, pois a dispensa indica que a empresa autorizou a ausência.
3. **O sistema já considera a falta automaticamente?**

   Se a jornada do colaborador esteja configurada corretamente (sendo uma jornada de trabalho esperada), e ele não registra o ponto, o sistema identificará isso como falta. Assim, dependendo da configuração da empresa, o desconto ocorrerá na folha de pagamento ou no banco de horas.
4. **Por que não aparece “falta parcial” no sistema?**

   Uma dúvida comum é o motivo pelo qual não aparece "falta parcial" em casos em que o colaborador esteve ausente por apenas um período do dia. Isso acontece porque a dispensa **não representa uma falta, mas sim uma ausência autorizada**.
   Se o objetivo for descontar as horas não trabalhadas, não utilize a justificativa "dispensa". O próprio sistema identificará a ausência e aplicará os apontamentos adequados. O tempo não trabalhado será computado como **atraso** ou **saída antecipada**, dependendo do período de ausência.
5. **Como garantir que as ausências sejam tratadas corretamente no sistema?**

   - **Quer que a ausência seja descontada?** Não registre como "dispensa"; deixe o sistema considerar automaticamente como falta. Para isso, o dia deve ter uma jornada de trabalho esperada.
   - **Cliente possui banco de horas e deseja que a ausência seja descontada do saldo?** [Aprove](https://sankhya.zendesk.com/hc/pt-br/articles/42427328039447) o saldo de banco de horas do dia para que o desconto ocorra corretamente.
   - **Colaborador saiu mais cedo ou entrou mais tarde e há uma justificativa?** Faça o lançamento de uma [dispensa parcial](https://sankhya.zendesk.com/hc/pt-br/articles/42427219038871).

---

Caso teha dúvidas de como fazer o lançamento de dispensas, consulte os artigos abaixo:

- [Como registrar uma dispensa/atestado para o dia todo ou vários dias](https://sankhya.zendesk.com/hc/pt-br/articles/42427229767959)
- [Como registrar uma dispensa/atestado parcial ou de horas](https://sankhya.zendesk.com/hc/pt-br/articles/42427219038871)

Com essa clareza na utilização das justificativas, você evita inconsistências nos registros e garante um controle de jornada preciso e transparente para todos.
Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
