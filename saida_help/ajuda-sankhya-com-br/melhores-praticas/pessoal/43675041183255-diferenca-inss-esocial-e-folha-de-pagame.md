---
id: "43675041183255"
titulo: "Diferença INSS eSocial e Folha de Pagamento: Desconto indevido no teto do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43675041183255-Diferen%C3%A7a-INSS-eSocial-e-Folha-de-Pagamento-Desconto-indevido-no-teto-do-colaborador"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-05T14:40:17Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Diferença INSS eSocial e Folha de Pagamento: Desconto indevido no teto do colaborador

A divergência pode ocorrer quando o colaborador possui **mais de um cálculo de folha na mesma competência**, **desligamento e readmissão no mesmo mês** ou **INSS descontado em outra empresa**.

Nessas situações, o sistema pode não recompor corretamente a **base de INSS**, fazendo com que o valor enviado ao eSocial fique **acima do teto previdenciário**, mesmo que o cálculo apresentado na folha esteja correto.

Para identificar a causa, é necessário verificar o **histórico de cálculos da competência**, as bases de INSS e os descontos considerados em cada processamento.

### Procedimento para identificar e corrigir o desconto indevido

(1)** Como identificar o desconto indevido**

Uma das ferramentas disponíveis para identificar diferenças de INSS é a tela **S-5001 - Conferência INSS/PIS** (Pessoal+ » Consultas » S-5001 - Conferência INSS/PIS), essa tela funciona como um relatório de conferência e auxilia na identificação de funcionários que apresentam diferenças relacionadas ao INSS.

Caso queira saber mais sobre essa tela, consulte o artigo: [Relatório S-5001 (Contribuições sociais por trabalhador)](https://ajuda.sankhya.com.br/hc/pt-br/articles/36419467638551-Relat%C3%B3rio-S-5001-Contribui%C3%A7%C3%B5es-sociais-por-trabalhador)

(2)** Como analisar a diferença**

Após identificar o funcionário com divergência, acesse o **Totalizador do Trabalhador** no portal do eSocial e compare as informações com as apresentadas no sistema.

No totalizador do eSocial, verifique:

- **Base de cálculo do INSS** utilizada pelo eSocial;
- **Valor de INSS descontado** do trabalhador;
- **Valor de INSS calculado** pelo eSocial.

Os valores de INSS descontado e calculado devem ser compatíveis. Caso exista diferença, é necessário identificar a origem da divergência.

(3)** Como corrigir**

O primeiro passo é comparar a **base de INSS apresentada pelo eSocial** com a **base de INSS utilizada no cálculo da folha de pagamento**.

Caso sejam identificadas diferenças, verifique quais eventos estão contribuindo para a divergência e avalie se suas configurações estão corretas tanto no sistema quanto no eSocial.

Para realizar os ajustes no sistema acesse a tela Eventos (Pessoal+ » Cadastros » Eventos) e avaliar as abas **Avançado**, **eSocial** e **Bases de Cálculo**.

As configurações dessas abas influenciam diretamente o cálculo realizado pelo sistema e as informações enviadas ao eSocial. Portanto, é importante garantir que os eventos estejam corretamente parametrizados para evitar divergências entre a folha de pagamento e os valores apresentados pelo eSocial.

Na aba **Avançado** e em **Bases de Cálculo**, as configurações definem como o evento será considerado no cálculo da folha.

Por exemplo, o campo **INSS**, na aba **Avançado**, determina se o evento irá ou não compor a base de INSS e referente a qual tipo de folha. Após realizar um ajuste nesse campo, é importante conferir se a configuração correspondente também está refletida na aba **Bases de Cálculo**.

Assim, ao configurar o campo **INSS** como **INSS**, a respectiva base, como a **Base de INSS (1901)**, deve estar corretamente vinculada na aba **Bases de Cálculo**.

![Imagem 1: Assim, ao configurar o campo INSS como INSS , a respectiva base, como a Base de INSS (1901) , deve estar corretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44000615255831)![Imagem 2: Assim, ao configurar o campo INSS como INSS , a respectiva base, como a Base de INSS (1901) , deve estar corretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44000585387543)

As informações preenchidas na aba **eSocial** são enviadas ao eSocial para que as incidências sejam consideradas no cálculo interno.

É importante que essas configurações estejam **de acordo com o cálculo realizado pelo sistema**. Por exemplo, se um evento compõe a base de INSS, o campo **INSS** deve estar configurado com a incidência **11 – Mensal**.

Dessa forma, as incidências configuradas no sistema e enviadas ao eSocial permanecem consistentes, evitando divergências nos cálculos.

![Imagem 3: Dessa forma, as incidências configuradas no sistema e enviadas ao eSocial permanecem consistentes, evitando…](https://ajuda.sankhya.com.br/hc/article_attachments/44000585393175)

Caso seja identificada alguma divergência, será necessário realizar a correção de acordo com a origem do problema.

- **Ajustes nas abas Avançado e Bases de Cálculos:** é necessário **recalcular a folha** para que a alteração seja aplicada ao cálculo e ao resumo da folha. Após o recálculo, é necessário **reenviar o evento S-1200** ao eSocial.
- **Ajustes na aba eSocial:** é necessário **enviar o evento S-1010** com a nova configuração da rubrica. Antes do envio, verifique a **data de início de validade da rubrica**. Após o processamento do S-1010, será necessário **reenviar o S-1200**.

Após realizar o procedimento, é necessário **conferir novamente as informações** e validar se os valores foram corrigidos tanto no sistema quanto no eSocial.

Essa conferência garante que a divergência foi solucionada e que os valores estão sendo considerados corretamente.

**(1)** **Casos de remuneração de outras empresas**

Para casos de remuneração de outras empresas se faz necessário conferir as devidas configurações necessárias conforme o artigo [Como cadastrar a remuneração recebida em outras empresas](https://ajuda.sankhya.com.br/hc/pt-br/articles/28137503967255-Como-cadastrar-a-remunera%C3%A7%C3%A3o-recebida-em-outras-empresas)

Após de conferir e se necessário realizar ajuste será necessário recalcular a folha e posteriormente enviar os dados ao e-social.

### Boas práticas para evitar divergências futuras

Para evitar novas divergências entre a folha de pagamento e o eSocial, recomenda-se:

- **Manter os eventos corretamente parametrizados**, garantindo que as configurações das abas **Avançado, Bases de Cálculos e eSocial** estejam de acordo com o cálculo realizado pelo sistema.
- **Verificar as remunerações de outras empresas ou vínculos**, garantindo que as informações e configurações estejam corretas.
- **Após alterações nas configurações dos eventos, enviar o S-1010**, para que os ajustes realizados sejam refletidos no eSocial.
