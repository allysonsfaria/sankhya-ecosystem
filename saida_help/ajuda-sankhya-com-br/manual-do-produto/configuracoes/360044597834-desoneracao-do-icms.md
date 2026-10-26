---
id: "360044597834"
titulo: "Desoneração do ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597834-Desonera%C3%A7%C3%A3o-do-ICMS"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:46:46Z"
rotulos: ["Configuração", "Fiscal", "Desoneração", "Desoneração do ICMS manual", "NF-e", "SUFRAMA", "ICMS", "Impostos", "HABFORMASREPRED", "desoneração", "benefícios fiscais"]
---

# Desoneração do ICMS

Neste artigo trataremos dos procedimentos necessários para o preenchimento das informações da NF-e destinadas à SUFRAMA e outras situações com benefícios fiscais da Isenção ou Não-Incidência, os quais exigem a desoneração do ICMS (Valor ICMS desonerado e motivo da Desoneração).

Para iniciar este processo, habilite o parâmetro **"Habilitar formas alternativas de repasse de ICMS? - HABFORMASREPRED"**.

Temos duas formas de configurar o sistema:

**1)** Se a desoneração for em decorrência do Parceiro pertencer à Zona Franca de Manaus ou Área de Livre Comércio:

Primeiramente, na tela [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros), aba [Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal), preencha o campo **"Código SUFRAMA"**.

[GIF animado: Imagem 1: Primeiramente, na tela Cadastro de Parceiros , aba Fiscal , preencha o campo "Código SUFRAMA" .](https://ajuda.sankhya.com.br/hc/article_attachments/4403421733015)

Depois, na tela [Cadastro de Tipos de Operação – TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal) configure a TOP de Venda para as CFOP’s provenientes do SUFRAMA, ou seja, 5109 e 6109 ou 6110.

![Imagem 2: Depois, na tela Cadastro de Tipos de Operação – TOP , aba Livro Fiscal configure a TOP de Venda para as CFOP’s…](https://ajuda.sankhya.com.br/hc/article_attachments/4403421744151)

**2)** Caso a desoneração não seja pelo primeiro motivo citado:

Na tela [Cadastro de Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), preencha o campo **"Tributação"** com uma das seguintes opções:

- 40-Isenta;
- 41-Não tributada;
- 30-Isenta e não tribut.e c/cobrança por subst.;
- 50-Suspensão.

Ao informar outras opções, o sistema irá apresentar a mensagem:

**"Cód.Mot.Desoneração ICMS: Só pode ser informado se o campo "Tributação" for "Isenta", "Não tributada", "Isenta ou não tributada e com cobrança do ICMS por substituição tributária" ou "Suspensão"."**

Em seguida, na seção **"Repassar para o cliente"** marque a opção **"Redução do imposto"** ou **"ICMS"**.

[GIF animado: Imagem 3: Em seguida, na seção "Repassar para o cliente" marque a opção "Redução do imposto" ou "ICMS" .](https://ajuda.sankhya.com.br/hc/article_attachments/4403421762583)

Se houver mais de uma opção marcada o sistema emitirá a mensagem:

**"Campo "Repassar para o cliente" não pode ter mais de uma opção marcada."**

Caso na seção Repassar para o cliente esteja marcada a opção **"Redução da BASE"** e o campo **"Cód.Mot.Desoneração ICMS"** esteja preenchido, o sistema apresentará a mensagem:

**"Cód.Mot.Desoneração ICMS: Só pode ser informado se o campo "Repassar para o cliente" for "Redução do imposto" ou "ICMS"."**

**Observação:** preencha o parâmetro **"UF que permite deduzir vlr repasse ICMS da BC IRRF - UFDEDREPICMSIRF"** com a UF desejada. Desta forma, ao selecionar essa mesma UF na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414) durante a emissão da nota com desoneração de ICMS e retenção de IR, o valor do repasse será deduzido da base de cálculo do IRRF.

---

![Imagem 4: Considerações sobre o SUFRAMA:](https://ajuda.sankhya.com.br/hc/article_attachments/16242416403735) **Considerações sobre o SUFRAMA:**

Em caso de Substituição Tributária - Cálculo - Zona Franca, pela legislação da SUFRAMA é necessário calcular o ST considerando o valor do ICMS já abatido o desconto referente ao repasse do benefício.

Ao informar o campo **"Cód. Mot. Desoneração ICMS"** com a opção **"7-SUFRAMA"** e o campo **"Tributação"** igual a **"Isenta e não tribut. e c/ cobrança por subst."**, na geração dos impostos do item o sistema irá subtrair o valor do desconto referente à desoneração, da base de cálculo utilizada para a aplicação do MVA no cálculo do ST.

**Observação:** todos os motivos de desoneração, excetuando-se o motivo 7 - SUFRAMA, não necessitam que o **"Código SUFRAMA"** localizado na [aba Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros#abafiscal) do [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Parceiros) esteja preenchido, pois, são casos que não dependem do Parceiro estar na Zona Franca de Manaus. Além do preenchimento correto do motivo da desoneração nas [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025232854-Al%C3%ADquotas-de-ICMS), deve-se atentar para a configuração de repasse de ICMS realizada na seção Repassar para o Cliente também nesta tela.

---

Após realizar as configurações acima, para que o sistema gere a tag **<motDesICMS>** e tag **<vICMSDeson>** no XML da NF-e para a impressão do Danfe, é necessário que na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS):

1. Uma das marcações da seção **"Repassar para o Cliente"** esteja realizada ([Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS), [aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral));
2. O campo **"Cód.Mot.Desoneração ICMS"** esteja preenchido.

Não havendo campo específico para demonstração dos valores de ICMS Desonerado e o Motivo da Desoneração, estes deverão estar no campo **"Informações Complementares"** do DANFE; salvo legislação específica caso contrário.

Assim o sistema gera a NF-e normalmente no sistema, contudo na impressão do DANFE os campos referentes à base de cálculo do ICMS, alíquota do ICMS e valor do ICMS devem ser zerados.

Além disso, o XML deverá possuir as tag's **<motDesICMS>** e **<vICMSDeson>**, geradas normalmente pelo sistema.

| ```                                        Imagem 5: A tag <vICMSDeson> será preenchida apenas se a tag <motDesICMS> estiver informada.     A tag <vICMSDeson> será preenchida apenas se a tag <motDesICMS> estiver      informada. ``` |
| --- |

Na seção Repassar para o Cliente, vista acima, ao efetuar a marcação**"Redução do Imposto"**, será calculado o valor da diferença entre o imposto normal e o imposto calculado sobre a base reduzida; esse valor será armazenado no campo Desconto de Redução de Base. Exemplo:

```
![Imagem 6: Na seção Repassar para o Cliente , vista acima, ao efetuar a marcação "Redução do Imposto" , será calculado o valor da…](https://ajuda.sankhya.com.br/hc/article_attachments/42310658196631) VLRREPRED = (BaseSemRed * ALIQICMS / 100) - VLRICMS
```

Ao efetuar a marcação **"ICMS"**, será repassado o valor integral do ICMS calculado no item para o campo Desconto de Redução de Base. Exemplo:

```
 ![Imagem 7: Ao efetuar a marcação "ICMS" , será repassado o valor integral do ICMS calculado no item para o campo Desconto de…](https://ajuda.sankhya.com.br/hc/article_attachments/42310658196631) VLRREPRED = VLRICMS
```

Realizando a marcação **"Redução da Base"**, será calculado o valor da diferença entre a base de cálculo para o ICMS normal e a base de cálculo reduzida e esse valor será armazenado no campo Desconto de Redução de Base. Exemplo: 

```
![Imagem 8: Realizando a marcação "Redução da Base" , será calculado o valor da diferença entre a base de cálculo para o ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/42310658196631) VLRREPRED = BaseSemRed - BASEICMS
```

Quando o campo **"% da Base ICMS"** estiver configurado com um percentual, no lançamento de uma nota que calcule ICMS, o sistema irá gerar um valor de repasse de ICMS ao cliente, resultante da operação:

```
![Imagem 9: Quando o campo "% da Base ICMS" estiver configurado com um percentual, no lançamento de uma nota que calcule ICMS, o…](https://ajuda.sankhya.com.br/hc/article_attachments/42310658196631) Base ICMS * % Base ICMS / 100
```

---

![Imagem 10: Informações adicionais referentes à seção Repassar para o Cliente :](https://ajuda.sankhya.com.br/hc/article_attachments/16242416403735) **Informações adicionais referentes à seção Repassar para o Cliente:**

Ao utilizar a marcação Redução do Imposto ou Redução da BASE, o repasse será calculado com base no percentual de redução configurada no campo Redução da base da aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS#abageral), da tela [Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS).

Além disso, com o uso da marcação ICMS a alíquota informada no campo Alíquotas irá realizar a desoneração integral do ICMS.

Tem-se abaixo, os exemplos de uso de cada marcação disponível na seção:

**(1)** **Redução do Imposto**

Quando essa marcação for configurada, o sistema irá aplicar o percentual de redução sobre o valor da base de cálculo do ICMS. Em seguida, o valor da desoneração será calculado considerando a diferença entre o imposto normal e o imposto calculado sobre a base reduzida. Observe:

- **Redução da base:** 30%;
- **Alíquota de ICMS:** 12%;
- **Base de cálculo:** R$ 200,00;
- **Base de cálculo reduzida:** R$ 200,00 \* 30% = R$ 60,00 / R$ 200,00 - R$ 60,00= R$ 140,00;
- **Valor de ICMS sobre a base integral:** R$ 200,00 \* 12% = R$ 24,00;
- **Valor de ICMS sobre a base reduzida:** R$ 140,00 \* 12% = R$ 16,80;
- **Valor de Repasse da redução (ICMS Desonerado):** R$ 24,00 - R$ 16,80 = R$ 7,20.

![Imagem 11: Valor de Repasse da redução (ICMS Desonerado): R$ 24,00 - R$ 16,80 = R$ 7,20.](https://ajuda.sankhya.com.br/hc/article_attachments/20465286103063)

O mesmo cálculo aplica-se ao ICMS do produto, pois este se enquadrou na mesma regra de ICMS do frete.

![Imagem 12: O mesmo cálculo aplica-se ao ICMS do produto, pois este se enquadrou na mesma regra de ICMS do frete.](https://ajuda.sankhya.com.br/hc/article_attachments/20465286110743)

Foi incluído na tag **<vICMSDeson>** do XML, a soma dos dois ICMS's calculada sobre a diferença entre os impostos, uma vez que: R$ 7,2 + R$ 2,88 = R$ 10,08.

**(1)** **Redução da Base**

Ao configurar esta, o sistema irá aplicar o percentual de redução sobre o valor de base de cálculo do ICMS. Em seguida, o valor da desoneração será calculado de forma a considerar a diferença entre a base de cálculo para o ICMS normal e a base de cálculo reduzida. Considere o exemplo:

- **Redução da base:** 30%;
- **Alíquota de ICMS:** 12%;
- **Base de cálculo:** R$ 200,00;
- **Base de cálculo reduzida:** R$ 200,00 \* 30% = R$ 60,00 / R$ 200,00 - R$ 60,00 = R$ 140,00;
- **Valor de ICMS sobre a base integral:** R$ 200,00 \* 12% = R$ 16,80;
- **Valor de repasse da redução (ICMS Desonerado):** R$ 200,00 \* 30% = R$ 60,00.

O mesmo cálculo foi aplicado ao ICMS do produto, pois se enquadrou na mesma regra de ICMS do frete.

![Imagem 13: O mesmo cálculo foi aplicado ao ICMS do produto, pois se enquadrou na mesma regra de ICMS do frete.](https://ajuda.sankhya.com.br/hc/article_attachments/20465286128023)

Foi incluído na tag **<vICMSDeson>**no XML a soma dos dois ICMS, sendo esta calculada sobre a diferença das bases de ICMS, desse modo: R$ 60,00 + R$ 56,00 = R$ 84,00.

**(1)** **ICMS**

O sistema irá realizar o cálculo da desoneração conforme repassado o valor integral do ICMS calculado. Sabendo disso, considere o exemplo abaixo:

- **Alíquota de ICMS:** 12%;
- **Base de Cálculo:** R$ 200,00;
- **Valor de ICMS sobre a base integral:** R$ 200,00 \* 12% = R$ 24,00;
- **Valor de repasse da redução (ICMS Desonerado):** R$ 200,00 \* 12% = R$ 24,00.

O mesmo cálculo será aplicado ao ICMS do produto, pois este se enquadra na mesma regra de ICMS do frete.

![Imagem 14: O mesmo cálculo será aplicado ao ICMS do produto, pois este se enquadra na mesma regra de ICMS do frete.](https://ajuda.sankhya.com.br/hc/article_attachments/20465286132503)

Na tag **<vICMSDeson>**do XML será incluída a soma dos dois ICMS calculada sobre o repasse integral do ICMS, assim: R$ 24,00 + R$ 9,60 = R$ 33,60.

**(1)** **% da Base ICMS**

Quando um percentual for configurado durante o lançamento de uma nota com cálculo de ICMS, o sistema irá gerar um valor de repasse de ICMS ao cliente. Além disso, o campo % da Base ICMS não possui relação com as marcações da seção Repassar para o cliente; desse modo, ao configurar uma alíquota, o sistema irá calcular a desoneração aplicando o percentual sobre a base de ICMS.

Porém, ao configurar o percentual no campo acima e de maneira simultânea, realizar a configuração da desoneração por meio das marcações da seção Repassar para o Cliente, a desoneração será calculada de forma duplicada. Observe:

- **Alíquota de Desoneração:** 17%;
- **Alíquota de ICMS:** 12%;
- **Base de cálculo:** R$ 200,00;
- **Valor de ICMS sobre a base integral:** R$ 200,00 \* 12% = R$ 24,00;
- **Valor de repasse da redução (ICMS Desonerado):** R$ 200,00 \* 17% = R$ 34,00.

Este mesmo cálculo foi aplicado ao ICMS do produto, pois foi inserido na mesma regra de ICMS do frete.

![Imagem 15: Este mesmo cálculo foi aplicado ao ICMS do produto, pois foi inserido na mesma regra de ICMS do frete.](https://ajuda.sankhya.com.br/hc/article_attachments/20465286140567)

A tag **<vICMSDeson>** foi incluída no XML com a soma dos dois ICMS's referente à alíquota de desoneração aplicada sobre a base de ICMS, assim, tem-se: R$ 34,00 + R$ 13,60 = R$ 47,60.

**Importante:** com o parâmetro **"Substituição Tributária embutida no preço - STEMBUT"** ligado, o valor do imposto não será incluído no total da nota fiscal. Quando desativado, o imposto será retirado do total adicionado. É crucial considerar este parâmetro em operações com ICMS-ST.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597834-Desonera%C3%A7%C3%A3o-do-ICMS#top)
