---
id: "44010058717847"
titulo: "FitScore: o que é e como configurar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010058717847-FitScore-o-que-%C3%A9-e-como-configurar"
trilha: "Meetime > Fit Score"
atualizado_em: "2026-10-05T18:29:40Z"
rotulos: ["sync_hc", "meetime_414", "sync_hash_5d0e20c27a14", "meetime"]
---

# FitScore: o que é e como configurar

O FitScore ajuda você a priorizar seus leads na hora da prospecção!

É uma ferramenta altamente personalizável e permite que você organize a prospecção do seu time baseado no **perfil dos leads**.

Segundo as regras criadas, cada lead receberá uma **pontuação**, e então, os leads serão distribuídos e disponibilizados na tela de execução dos usuários por ordem decrescente de pontuação, ou seja, os leads com mais fit ao seu produto/solução ficam no **topo da lista**.
Além disso, quando o SDR for iniciar a prospecção de novos leads (Tela de execucção > Iniciar novas prospecções), os leads com maiores notas serão priorizados. Isso significa que se você possui uma base com 1.000 leads com status de “Aguardando Início”, por exemplo, a distribuição dos leads aos SDRs priorizará os melhores perfis.

Isso facilita o trabalho dos usuários, que saberão com quem devem conversar prioritariamente, tornando a prospecção ainda mais organizada e certeira!

As regras configuradas irão somar ou subtrair os pontos conforme as características desejáveis, ou indesejáveis e a ferramenta irá calcular a **nota do lead**:

0 a 3 - **não desejável**

4 a 7 - **regular**

8 a 10 - **desejável**

Passando o cursor do mouse sobre a nota do lead, o Meetime Flow irá apresentar quais foram as regras aplicadas ao lead que resultaram na nota indicada.

![Imagem 1: Passando o cursor do mouse sobre a nota do lead, o Meetime Flow irá apresentar quais foram as regras aplicadas ao lead…](https://ajuda.sankhya.com.br/hc/article_attachments/44010050049559)

## Como configurar o Fit Score?

Acesse o menu **Prospecção** (barra superior preta) > **Ajustes** > **Fit Score**

![Imagem 2: Acesse o menu Prospecção (barra superior preta) > Ajustes > Fit Score](https://ajuda.sankhya.com.br/hc/article_attachments/44010090189207)

1. Clique em “**Adicionar regra”**
2. Preencha a **pontuação** relacionada ao campo

   Quanto mais desejável for uma característica, **maior** deverá ser sua pontuação, por exemplo, para utilizar o Meetime Flow é indispensável que o lead possua um CRM, portanto se o campo **CRM** for preenchido com alguma informação a pontuação será +10.

   Para a Meetime, é importante que o lead tenha o e-mail com domínio de uma empresa, portanto se o lead preencher o campo **E-mail** com domínio gmail/hotmail, a pontuação será -3.
3. Selecione o campo do lead que será atribuída a pontuação
4. Selecione o critério de avaliação

   Seguindo o exemplo acima, os critérios serão:

   Campo = **CRM** → Critério = **Não é vazio**

   Campo = **E-mail** → Critério = **Contém**
5. Selecione o valor desejado

   Dependendo do critério selecionado, essa informação não precisará ser preenchida. Por exemplo, no caso do critério “**Não é vazio**” não é necessário preencher um valor, pois qualquer informação que o lead preencher nesse campo irá contabilizar a pontuação atribuída.

   No caso do critério “**Contém**” é necessário indicar o que deve conter nesse campo para que a pontuação seja aplicada.

   Para adicionar mais de uma regra, clique em “**+ Adicionar Regra**” e repita o procedimento anterior.
6. Após adicionar todas as regras, clique em “**Salvar**”.

   ![Imagem 3: Após adicionar todas as regras, clique em “ Salvar ”.](https://ajuda.sankhya.com.br/hc/article_attachments/44010076439575)

## Como a ferramenta calcula a nota do lead?

A soma ou subtração das pontuações definidas nas regras do Fit Score irá resultar em uma **pontuação máxima** e uma **pontuação mínima** possível. Baseado nesses valores, e utilizando regras de normalização de notas e regra de três, a ferramenta irá calcular qual a porcentagem da pontuação de cada lead.

Por exemplo, se a pontuação do lead resulta em 40% da pontuação máxima, sua nota será 4.

Para entender como as pontuações traduzem em notas, vamos analisar um exemplo prático:

Temos dois leads, ambos com os campos **Nome**, **E-mail**, **Cargo** e o **Setor** da empresa preenchidos.

![Imagem 4: Temos dois leads, ambos com os campos Nome , E-mail , Cargo e o Setor da empresa preenchidos.](https://ajuda.sankhya.com.br/hc/article_attachments/44010063802135)

**Regra 1:** E-mail é diferente de @ gmail = + 1 ponto

Pontuação máxima = 1 ponto

Pontuação mínima = 0 pontos

![Imagem 5: Os dois leads receberam nota 10, pois ambos atenderam ao critério da regra 1 e receberam a pontuação máxima.](https://ajuda.sankhya.com.br/hc/article_attachments/44010081974167)Os dois leads receberam nota 10, pois ambos atenderam ao critério da regra 1 e receberam a pontuação máxima.

Agora vamos adicionar uma nova regra:

**Regra 1:** E-mail é diferente de @ gmail = + 1 ponto

**Regra 2:** Cargo é igual a Diretor = + 2 pontos

Pontuação máxima = 3 pontos.

Pontuação mínima = 0 pontos
![Imagem 6: Pontuação mínima = 0 pontos](https://ajuda.sankhya.com.br/hc/article_attachments/44010064246679)

Como a Marta atende a essas duas regras ela fica com 3 pontos e continua com a pontuação máxima, portanto sua nota é 10.

Já o Milton atende só uma das regras, pois não possui cargo de Diretor, então ele fica com 1 ponto, que é 30% da pontuação máxima. Nesse caso a nota do Milton fica 3.

Adicionando uma terceira regra, o cenário fica da seguinte forma:

**Regra 1:** E-mail é diferente de @ gmail = + 1 ponto

**Regra 2:** Cargo é igual a Diretor = + 2 pontos

**Regra 3:** Setor é igual a Público = - 7 pontos

Pontuação máxima = 3 pontos

Pontuação mínima = - 7 pontos

![Imagem 7: O pior somatório de um lead, de acordo com as regras configuradas no exemplo dado, será -7. No Fit Score esse número é…](https://ajuda.sankhya.com.br/hc/article_attachments/44010094146327)O pior somatório de um lead, de acordo com as regras configuradas no exemplo dado, será -7. No Fit Score esse número é normalizado em uma escala de 0 a 10, então o somatório -7 resulta na nota 0 do Fit Score, veja:

![Imagem 8: O pior somatório de um lead, de acordo com as regras configuradas no exemplo dado, será -7. No Fit Score esse número é…](https://ajuda.sankhya.com.br/hc/article_attachments/44010111227031)

O resultado da soma dos pontos recebidos pela Marta, segundo as regras configuradas, passa a ser - 4 pontos. Já o Milton manteve seu + 1 ponto.

Podemos pensar na escala de 0 a 10 em porcentagem, onde o 0% é o pior fit e o 100% o melhor fit, portanto a pontuação do Milton resulta em 80% da escala, ou seja, ele recebe nota 8. E a Marta recebe nota 3, pois possui 30% da escala. Veja:

![Imagem 9: Podemos pensar na escala de 0 a 10 em porcentagem, onde o 0% é o pior fit e o 100% o melhor fit, portanto a pontuação…](https://ajuda.sankhya.com.br/hc/article_attachments/44010111464599)

Se nenhum valor presente nos campos do lead estiver definido nas regras do Fit Score, a ferramenta irá calcular a nota comparando com o melhor ou o pior perfil possível, conforme as regras configuradas.

Se o lead não tem nenhum dos critérios preenchidos, o somatório dele será 0, já que nada foi somado e nem subtraído. Seguindo o exemplo acima, o lead terá nota do Fit Score igual a 7. Veja:

![Imagem 10: Se o lead não tem nenhum dos critérios preenchidos, o somatório dele será 0, já que nada foi somado e nem subtraído.…](https://ajuda.sankhya.com.br/hc/article_attachments/44010065049111)

Acessando [esse vídeo](https://vimeo.com/528467385?fl=pl&fe=sh), você pode verificar mais detalhes sobre a página.

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
