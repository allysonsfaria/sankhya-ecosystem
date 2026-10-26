---
id: "44012673798679"
titulo: "[TMS] - Como é feito o cálculo do Advalorem (Frete valor) no embarque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012673798679--TMS-Como-%C3%A9-feito-o-c%C3%A1lculo-do-Advalorem-Frete-valor-no-embarque"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:54Z"
rotulos: ["sync_hc", "lincros", "sync_hash_e48d67fbc8d8", "lincros_13433373"]
---

# [TMS] - Como é feito o cálculo do Advalorem (Frete valor) no embarque

**Menu**: Operacional > Cargas > Embarques

**Objetivo**: Apresentar como é feito o cálculo do componente Advalorem (Frete valor) no embarque

Considerações:

- Possuir embarque cadastrado/importado no sistema e que nos movimentos tenha o componente Advalorem/Frete Valor

No TMS o embarque funciona da seguinte forma:

1. Na aba 'Movimentos' nos valores do embarque (conforme print abaixo), o sistema realiza o cálculo da carga fechada.

   ![Imagem 1: Na aba 'Movimentos' nos valores do embarque (conforme print abaixo), o sistema realiza o cálculo da carga fechada.](https://ajuda.sankhya.com.br/hc/article_attachments/44012682179223)
2. Após o sistema calcular o valor do embarque, ele fará a distribuição do rateio para os conhecimentos vinculados a ele, conforme print abaixo, ou seja, cada conhecimento terá uma porcentagem de rateio até que feche 100% do embarque;

   ![Imagem 2: Após o sistema calcular o valor do embarque, ele fará a distribuição do rateio para os conhecimentos vinculados a ele,…](https://ajuda.sankhya.com.br/hc/article_attachments/44012689051159)
3. Verificando o componente de frete valor, a transportadora cobra 0,04% em cima do valor da nota;
4. Se pegarmos o valor da nota, por exemplo, temos o valor de R$ 1.206,54, que multiplicado por 0,04% resulta em 0,48;
5. Dessa forma, vemos que a transportadora não está rateando esse componente de frete valor de acordo com o rateio do embarque. Em princípio eles só estão realizando o rateio do frete peso;
6. Essa funcionalidade de ratear apenas determinados componentes no embarque não existe no sistema, o mesmo rateia de forma geral;
7. Diante dessa informação, é necessário alinhar/orientar a transportadora para que quando se tratar de embarques, cargas fechadas, os mesmos realizem o rateio de todos os componentes.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
