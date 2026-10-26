---
id: "43675002056471"
titulo: "Como garantir que o cálculo de tributos no dissídio seja realizado corretamente e não gere valores incorretos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675002056471-Como-garantir-que-o-c%C3%A1lculo-de-tributos-no-diss%C3%ADdio-seja-realizado-corretamente-e-n%C3%A3o-gere-valores-incorretos"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-14T15:56:40Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como garantir que o cálculo de tributos no dissídio seja realizado corretamente e não gere valores incorretos?

### Como funciona o cálculo do INSS no dissídio?

O correto é que, ao calcular o dissídio, o sistema some a base mensal de cada competência com a diferença salarial retroativa, formando uma nova base de cálculo para o **INSS**. Em seguida, deve recalcular o valor devido e subtrair o INSS já descontado na competência original, para que a folha de dissídio apresente apenas a diferença devida.

**Exemplo:**

- **Base mensal original:** R$ 6.500,45
- **INSS descontado na folha original:** R$ 719,64
- **Diferença salarial retroativa:** R$ 63,93
- **Nova base de cálculo:** R$ 6.564,38

Com a aplicação do dissídio, o sistema deverá recalcular o INSS sobre a nova base e descontar na folha de dissídio somente a diferença entre o valor recalculado e o valor já recolhido na folha original.

### Configurações necessárias

**1. Evento de INSS**

Acesse **Eventos (Pessoal+ » Cadastros » Eventos)** e verifique se o campo **“Tem seus valores recalculados”** está marcado nos eventos relacionados ao INSS, como, por exemplo, o evento **9010**.

![Imagem 1: Acesse Eventos ( Pessoal+ » Cadastros » Eventos) e verifique se o campo “Tem seus valores recalculados” está marcado…](https://ajuda.sankhya.com.br/hc/article_attachments/44240983496471)

**2. Eventos de base do INSS**

Verifique também se os eventos de base relacionados ao INSS, como, por exemplo, o evento **1901**, estão configurados com a regra de cálculo adequada para a folha de dissídio, conforme demonstrado nas imagens de referência.

![Imagem 2: Verifique também se os eventos de base relacionados ao INSS, como, por exemplo, o evento 1901 , estão configurados com…](https://ajuda.sankhya.com.br/hc/article_attachments/44240983498647)

**Orientação:** caso identifique divergências nessas configurações, realize os ajustes necessários conforme as orientações acima e efetue um novo cálculo do dissídio para validar os valores apresentados.

### Como funciona o cálculo do IRRF no dissídio?

O cálculo do IRRF no dissídio considera os valores gerados na própria folha de dissídio, de acordo com a data de pagamento. Dessa forma, o sistema apura o imposto sobre os valores tributáveis calculados nessa folha, sem considerar o IRRF já descontado nas folhas originais das competências anteriores.

Isso ocorre porque o IRRF é apurado com base na data de pagamento, diferentemente do INSS, cujo cálculo no dissídio considera a base de cada competência e a diferença entre o valor devido e o valor já descontado anteriormente.

**Orientação:** Para a apuração do IRRF, a folha de dissídio será recomposta considerando todas as folhas pagas na mesma referência de pagamento. Assim, o sistema considerará os valores tributáveis dessas folhas em conjunto para realizar o cálculo do imposto devido.
