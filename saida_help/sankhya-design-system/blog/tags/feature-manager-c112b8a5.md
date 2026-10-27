---
id: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/feature-manager"
titulo: "Uma publicação com a etiqueta \"feature-manager\""
url: "https://gilded-nasturtium-6b64dd.netlify.app/blog/tags/feature-manager"
trilha: "Blog > Tags > Feature Manager"
---

# Uma publicação com a etiqueta "feature-manager"

## [Plano de Convivência das telas no novo layout (Design System)](https://gilded-nasturtium-6b64dd.netlify.app/blog/plano-de-convivencia)

20 de maio de 2024 · 4 min para ler

![Victor Uehara](https://gilded-nasturtium-6b64dd.netlify.app/img/authors/VictorUehara.png)

Victor Uehara

Developer

## Introdução

O Plano de Convivência é o modelo adotado para a disponibilização gradual das telas migradas no novo Design System para
clientes. Este modelo consiste em 3 etapas: Beta controlado, Convivência e disponibilidade geral (GA - General Availability) que serão abordados neste artigo.

## Beta

Na etapa de validação em beta, selecionamos um grupo de clientes / usuários que utilizará exclusivamente a nova solução em ambiente
de produção. Durante esse período, mantemos uma equipe de suporte para atendimento emergencial, garantindo a segurança do uso da
nova solução. Além disso, estamos próximos dos clientes, acompanhando de perto suas rotinas de uso, até alcançar o nível de
confiança necessário para o lançamento oficial.

Atenção

Durante o teste beta de uma tela a ser lançada na nova interface, **usuários realizarão suas rotinas diárias em ambiente de produção,
sem possibilidade de convivência** com os layouts antigos.

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/forcedDS-2c88708bfb6896e208fc5bbb4ec1abd7.png "Imagem mostrando indisponibilidade da troca de layouts")

Os objetivos deste momento são:

1. Obter uma percepção mais realista da vivência da tela na operação diária dos usuários;
2. Realizar a coleta de pontos críticos (impeditivos, ou que afetam diretamente na satisfação) para tratativa emergencial, antes do
   lançamento oficial;
3. Validar funcionalidades antes da disponibilização geral;

## Convivência

Nos preparativos da descontinuação dos layouts anteriores, **a tela migrada para a nova interface permite aos usuários alguns dias de curva de aprendizagem e costume à nova experiência com um período de convivência**. A virada de clientes para este período é realizada em ‘ondas’.

A sugestão de impacto no Plano de Convivência padrão é que sejam liberadas as telas no novo layout para os clientes(Parceiro) dentro de 8 semanas. A distribuição será da seguinte forma:
10% dos clientes na primeira semana
40% dos clientes na segunda semana
70% dos clientes na terceira semana
100% dos clientes até a oitava semana. (totalizando 60 dias de convivência).

**Para a etapa de convivência é importante considerar:**

• Clientes que participaram da fase beta e clientes em implantação possuem acesso exclusivo à nova interface, sem possibilidade de migração entre layouts.

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/FluxogramaConvivencia-78aff018983260152c4550a39c3855c9.png "Fluxograma do modelo de convivência")

• Usuários recorrentes que optaram por não adotar a nova interface serão impactados a cada novo dia de trabalho com a tela do DS e a possibilidade de retornar para as versões anteriores. Caso tenham adotado a nova interface, a abertura ocorrerá sem impactos.

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/OptOut-e4b130d450c9800890007da9e760747c.png "Pop-up com opção de voltar para layout anterior")

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/interfaceLayoutConvivencia-c7b9d79b2f1300b30cc70a88be9076ff.png "Pop-up de escolha do layout durante convivência")

• Após 15 dias do início da convivência, uma tarja (webcomponent) precisa ser configurada na tela com um aviso sobre uma nova experiência estar sendo preparada para o usuário. O texto informativo deverá redirecionar o usuário a um
[‘saiba mais’](https://ajuda.sankhya.com.br/hc/pt-br/articles/21882233482775-Nova-interface-Sankhya):

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/alert-webcomponent-94983978a9cdffb8a91a34bb467ee65f.png "Imagem da tarja gerada pelo alert-webcomponent")

• Enquanto utilizam as versões anteriores do ERP (HTML5 e Flex) usuários serão impactados com um contador de tempo até a migração obrigatória

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/invite-webcomponent-3126566b45e3a4271eb0b1eeb9bb7136.png "Imagem da contagem gerada pelo invite-webcomponent")

• O Fluxo de tratativa de Problemas (bugs e impeditivos), Dúvidas e Sugestões deste período junto ao Service Desk e Manutenção pode ser acessado na página abaixo:

[SD - Atendimento ao DS](https://www.notion.so/SD-Atendimento-ao-DS-ee2931745bf14d7fb210e2028f88f0fe?pvs=21)

## Disponibilidade Geral (GA)

Após algumas semanas em convivência, as telas migradas ao novo layout precisarão passar por uma análise que definirá a descontinuação das interfaces antigas (flex e HTML5), fazendo com que os usuários possam acessá-la única e exclusivamente no Design System.

![alt text](https://gilded-nasturtium-6b64dd.netlify.app/assets/images/forcedDS-2c88708bfb6896e208fc5bbb4ec1abd7.png "Imagem mostrando indisponibilidade da troca de layouts")

Algumas premissas são consideradas para este momento.

1. **Comunicação prévia da descontinuação.**
   1. Contagem regressiva precisa ser apresentada na tela pelo menos 15 dias antes.
   2. Reforços de comunicação precisam ser realizados em canais consumidos pelos usuários que serão impactados.
2. **Tela estável.**
   1. A abertura de OSs precisa ter atingido um cenário onde não tivemos nenhum acionamento durante 01 semana em sequência, com disponibilidade de uso de 100% da base. Lembrando que é a partir de 02 semanas em sequência que as OSs são assumidas por Manutenção.
3. **CSAT apontando somente melhorias, não manutenção.**
   1. As coletas de respostas abertas do CSAT, possíveis entrevistas com usuários ou qualquer outro ponto de contato proativo precisa ter como feedback somente pontos de melhoria sugerida, não correção.
