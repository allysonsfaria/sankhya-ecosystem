---
id: "33806772753431"
titulo: "Como o Sistema Trata o INSS sobre Férias e Folha Mensal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33806772753431-Como-o-Sistema-Trata-o-INSS-sobre-F%C3%A9rias-e-Folha-Mensal"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:30:14Z"
rotulos: ["Configuração", "Eventos", "Impostos", "INSS", "eSocial", "Folha de Pagamento", "Como o Sistema Trata o INSS", "sobre Férias e Folha Mensal", "Cálculo da folha mensal", "Provisão de Desconto INSS", "Ressarcimento INSS Férias", "INSS Descontado nas Férias", "Cálculo de férias"]
---

# Como o Sistema Trata o INSS sobre Férias e Folha Mensal

No cálculo da folha de férias, o sistema gera uma provisão demonstrativa do INSS por meio do evento **Provisão de Desconto INSS**. No entanto, o desconto efetivo do INSS ocorre apenas na folha mensal ou na rescisão, considerando os dias trabalhados e os de férias.

Para garantir o desconto correto, o sistema utiliza o evento **Ressarcimento INSS Férias**, que estorna a provisão, permitindo o cálculo efetivo pelos eventos **INSS Descontado nas Férias** e **INSS (desconto padrão)**.

Quando as férias abrangem mais de uma competência, tanto o ressarcimento quanto o desconto são proporcionais aos dias de férias de cada referência.

É essencial que os eventos de desconto estejam corretamente configurados para o **eSocial**, assegurando o envio adequado das informações conforme o manual oficial.

**Atenção:** A soma dos valores descontados nos eventos **INSS Descontado nas Férias** e **INSS (desconto padrão)** não deve ultrapassar o teto do INSS vigente, conforme a legislação previdenciária.

#### Exemplo de férias distribuídas entre duas referências:

**(1)** Cálculo de férias:

![Imagem 1: (1) Cálculo de férias:](https://ajuda.sankhya.com.br/hc/article_attachments/34012915431831)

**(1)** Cálculo da folha mensal:

- **Folha mensal 1:**

![Imagem 2: Folha mensal 1:](https://ajuda.sankhya.com.br/hc/article_attachments/34012874827159)

- **Folha mensal 2:**

![Imagem 3: Folha mensal 2:](https://ajuda.sankhya.com.br/hc/article_attachments/34012915436439)
