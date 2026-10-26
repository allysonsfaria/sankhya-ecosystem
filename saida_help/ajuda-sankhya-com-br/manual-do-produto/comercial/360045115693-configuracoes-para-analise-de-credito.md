---
id: "360045115693"
titulo: "Configurações para Análise de Crédito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:32:52Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Crédito", "Financeiro", "Limite de crédito", "Análise de Crédito", "Configurações para Análise de Crédito", "Crédito do parceiro", "br.com.sankhya.mgecom.rot.configuracoesanalisecred", "Configurações para Análise de Crédito manual", "Análise automática de crédito", "Configuração de regras", "Fórmulas de cálculo"]
---

# Configurações para Análise de Crédito

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312095429271) Módulo: Comercial > Rotinas > Análise de Crédito
```

---

Esta tela permite que se defina regras para a análise automática de crédito dos parceiros, incluindo a sugestão do limite de crédito a ser concedido, por meio de uma fórmula configurável.

Aqui, pode-se incluir informações do balanço ou balancete de seus clientes como, patrimônio líquido, direitos, obrigações, caixa, endividamento, etc. Além dos resultados de consulta, junto aos órgãos de proteção ao crédito e dados oriundos do próprio Financeiro e Comercial como, volume médio de compras, histórico de pagamentos, atraso médio, perfil de parceiro, entre outros. Para compor um método de análise de crédito confiável que norteie a decisão dos gestores de cobrança.

Nesta tela, pode-se estabelecer grupos de clientes que estarão sujeitos a análise de crédito de tipos diferenciados, como, por exemplo:

- Parceiros de um determinado segmento como comércio, indústria e outros que poderão ter uma análise de crédito baseada em uma análise de balanço, uma avaliação do SERASA, um histórico de compras e demais.
- Parceiros pessoa física, que poderão ser avaliados pela declaração de imposto de renda, propriedade de imóveis, carteira de trabalho...
- Parceiros públicos como governos, prefeituras e demais que poderão ser avaliados pelo histórico de relacionamento, nível médio de atraso...

Aqui, pode-se também montar as definições que serão utilizadas para fazer o cálculo da análise de crédito.

Para acessar as funcionalidades desta tela, basta acessar os links abaixo:

| Funcionalidades da Tela | |
| --- | --- |
| [Aba Definição das Informações](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito#AbaDefini%C3%A7%C3%A3odasInforma%C3%A7%C3%B5es) | |
| [Abas Fórmula Limite Crédito e Fórmula](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito#AbasF%C3%B3rmulaLimiteCr%C3%A9ditoeF%C3%B3rmulaLimiteCr%C3%A9ditoMensal) [Limite](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito#AbasF%C3%B3rmulaLimiteCr%C3%A9ditoeF%C3%B3rmulaLimiteCr%C3%A9ditoMensal) [Crédito Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito#AbasF%C3%B3rmulaLimiteCr%C3%A9ditoeF%C3%B3rmulaLimiteCr%C3%A9ditoMensal) | |

---

### Aba Definição das Informações

Esta aba apresenta duas partes distintas:

#### Seção Grupo p/ informações de análises de Crédito

Esta seção apresentará os agrupadores de informações para o cálculo, cada grupo descrito aqui poderá conter várias informações, definidas e ordenadas na aba **"Informações para o Cálculo"**.

**Descrição:** nome do grupo, como, por exemplo: Análise Financeira, Informações Externas, Informações Imobiliárias, dentre outros.

**Ordem:** indicará a ordem em que o grupo será apresentado na tela de [Cálculo de Limite de Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114933-C%C3%A1lculo-de-Limite-de-Cr%C3%A9dito). 

![Imagem 2: Ordem : indicará a ordem em que o grupo será apresentado na tela de Cálculo de Limite de Crédito .](https://ajuda.sankhya.com.br/hc/article_attachments/22215305169303)

Assim, tem-se na tela Cálculo de Limite de Crédito:

![Imagem 3: Assim, tem-se na tela Cálculo de Limite de Crédito :](https://ajuda.sankhya.com.br/hc/article_attachments/22215458489239)

#### Seção Informações para o Cálculo

Nesta parte, pode-se criar variáveis/informações que farão parte da **"Análise de Crédito"**.

**Descrição:** nome da variável/informação que irá compor o grupo para informações de análises de Crédito. Exemplo de Informação (variáveis): Patrimônio Líquido, Direitos, Caixa, Média Mensal de Compras, Atraso Médio, Prazo Médio de Pagamento, Intervalo Médio de Compras. Como já dito anteriormente, em Grupo para informações de análises de Crédito, um grupo poderá conter várias informações.

**Chave:** nome da variável.

**Tipo:** existem quatro tipos de entradas:

- **SQL** = Select que se pode montar conforme as regras definidas, por exemplo:

SELECT COUNT(1) FROM TGFCAB WHERE CODPARC = :CODPARC AND DTNEG >= :DTCALC – 60

Esta opção habilita o campo **"Comando SQL"**, no rodapé da tela para a digitação de uma condição.

- Valor = Valor informado manualmente e não calculado.
- Lista = Habilita o campo **"Lista"** no rodapé da tela para listagem de informações. Como, por exemplo, se o cliente é: **"Bom"**, **"Mal"** ou **"Ótimo"** pagador.
- **Fórmula** = Campo que será calculado pelo sistema. Esta opção habilita o campo **"Fórmula"** no rodapé da tela, para digitação da mesma.

**Periodicidade:** período de reavaliação; neste campo, pode-se estipular o prazo de validade para o limite de crédito concedido.

**Nota:** este campo não possui funcionalidade nativa no sistema. Contudo, pode ser utilizado em personalizações como agendadores ou regras de negócio.

**Ordem:** ordem em que a informação será apresentada dentro do grupo.

**Casas Decimais:** número de casas decimais definidas para a variável.

**Obrigatório?:** se marcada, a informação será considerada obrigatória no Cálculo de Limite de Crédito.

**Observação:** campo aberto para digitação de dados que se pode julgar relevantes.

![Imagem 4: Observação : campo aberto para digitação de dados que se pode julgar relevantes.](https://ajuda.sankhya.com.br/hc/article_attachments/22214768689815)

O cálculo da análise de crédito é feito baseado em parâmetros configurados e, após o cálculo, é possível atualizar automaticamente no [Cadastro de Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) os campos **"Limite de Crédito"** e **"Limite de Crédito Mensal"**, o processo de efetivação do limite calculado pode ser feito manualmente, essa possibilidade depende da marcação **"Efetiva Lim. Créd. Calc. automaticamente?"** que fica na aba [Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros#abacrdito) do Cadastro de Parceiros.

Após a configuração da análise de crédito, deve-se configurar no Cadastro de Parceiros aba Crédito o campo **"Fórm. p/Cálculo Lim. Crédito"**.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito#top)

### Abas Fórmula Limite Crédito e Fórmula Limite Crédito Mensal

![Imagem 5: Abas Fórmula Limite Crédito e Fórmula Limite Crédito Mensal](https://ajuda.sankhya.com.br/hc/article_attachments/22215763967895)

Nestas abas, pode-se criar as fórmulas para efetuar os cálculos baseados nos campos informados na aba **"Definição das informações"**, estabelecendo assim, se o cliente deve ou não ter concessão de crédito e para os que terão crédito, a equação irá sugerir um limite de crédito.

Por exemplo: Cred('IND1') \* 2

Onde IND1 corresponde a um índice criado na aba de Definição das informações, sendo este, um campo do tipo Calculado. Atente-se ao utilizar Cred('XXX'), onde XXX é a chave da variável; caso esse Cred ('') não seja colocado em cada variável, o sistema não conseguirá avaliar a fórmula.

Após configurados, os cálculos serão feitos na tela [Cálculo de Limite de Crédito](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114933).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115693-Configura%C3%A7%C3%B5es-para-An%C3%A1lise-de-Cr%C3%A9dito#top)
