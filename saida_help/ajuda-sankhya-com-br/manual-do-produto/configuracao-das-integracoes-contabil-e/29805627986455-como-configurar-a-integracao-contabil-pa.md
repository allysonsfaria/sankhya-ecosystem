---
id: "29805627986455"
titulo: "Como configurar a integração contábil para a reoneração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29805627986455-Como-configurar-a-integra%C3%A7%C3%A3o-cont%C3%A1bil-para-a-reonera%C3%A7%C3%A3o"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Configuração das Integrações Contábil e Financeira"
atualizado_em: "2026-10-02T17:49:55Z"
rotulos: ["Configuração", "Eventos", "Fórmulas", "Impostos", "INSS", "Folha de Pagamento", "Configuração de Integração Contábil", "13º Salário", "Atualizar fórmula INSS", "Fórmulas Contábeis", "Desoneração da folha", "Pessoal+"]
---

# Como configurar a integração contábil para a reoneração

A reoneração da folha de pagamento mudou como algumas empresas calculam a contribuição ao INSS. Segundo a **Lei n.º 14.973/2024**, **empresas desoneradas não pagam a contribuição patronal sobre o 13º salário**, e a alíquota de 20% volta a ser aplicada gradualmente em municípios com baixo índice populacional.

Para garantir que o **Pessoal+** faça corretamente a integração contábil do **INSS parte empresa**, ao calcular o 13º salário (seja em rescisões ou na folha de pagamento), é **necessário** ajustar as [Fórmulas contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/10086051863063) dos eventos usados nesse cálculo.

### O que muda?

A fórmula contábil não deve utilizar a variável "V\_perinss" (percentual INSS) para empresas desoneradas.

### Como configurar?

**(1)** **Fórmula para provisão do INSS 13º salário:**

- antes;

```
(V_totbas + V_Incorpora)* (V_perinss + V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![Imagem 1: antes;](https://ajuda.sankhya.com.br/hc/article_attachments/29806124932247)

- agora.

```
(V_totbas + V_Incorpora)* (V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![Imagem 2: agora.](https://ajuda.sankhya.com.br/hc/article_attachments/29806259852439)

---

(1)** Fórmula para o INSS da folha normal do 13º salário:**

- antes;

```
(V_totbas )* (V_perinss + V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![Imagem 3: antes;](https://ajuda.sankhya.com.br/hc/article_attachments/29806418211223)

- agora.

```
(V_totbas )* (V_pergrps + (V_persegu * V_FAP) + V_perRAT) / 100
```

![Imagem 4: agora.](https://ajuda.sankhya.com.br/hc/article_attachments/29806518131479)

Essas fórmulas devem ser aplicadas **aos eventos de base de cálculo de 13º salário** utilizados na configuração contábil dos [Registros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360057060214) de empresas **optantes** pela desoneração da folha de pagamento.
