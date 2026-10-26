---
id: "44011205437975"
titulo: "[TMS] - Como configurar a alçada de aprovação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011205437975--TMS-Como-configurar-a-al%C3%A7ada-de-aprova%C3%A7%C3%A3o"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:58:03Z"
rotulos: ["sync_hc", "lincros", "lincros_13439012", "sync_hash_425f35671744"]
---

# [TMS] - Como configurar a alçada de aprovação

**Menu**: Cadastros gerais > Configurações da empresa > Workflow > Alçadas de aprovação

**Objetivo**: Alçada de aprovação funciona como um fluxo de workflow que determina a hierarquia de aprovação de um determinado processo.

Para controle de aprovações e liberações, o TMS disponibiliza a configuração de alçadas de aprovação, ideal para todos os clientes que necessitam que apenas um perfil específico consiga realizar determinada ação em uma rotina.

**Considerações**: A alçada de aprovações poderá ser aplicada em: Cotações ([Cotação spot](https://transpobrasil.atlassian.net/wiki/spaces/EDD/pages/298745938/Al+ada+para+Cota+o+Spot), [Cotações contrato](https://transpobrasil.atlassian.net/wiki/spaces/EDD/pages/304119866/Al+ada+para+Cota+o+Contrato)), [Cargas](https://transpobrasil.atlassian.net/wiki/spaces/EDD/pages/298713089/Al+ada+para+Conhecimento), [Faturas](https://transpobrasil.atlassian.net/wiki/spaces/EDD/pages/304316463/Al+ada+para+Faturas) e Calculadora de fretes.

- Uma alçada de aprovação possui uma faixa de valores à qual se enquadra, juntamente com o tipo da faixa e restrições de projeção:

  - O tipo da faixa poderá ser valor do frete ou percentual do valor do frete sobre o valor das mercadorias;
  - A alçada poderá ser classificada em Perfis, Centros de Custo, Departamentos e Unidades da empresa;
  - A alçada pode ser configurada para níveis hierárquicos de aprovações, possibilitando, por exemplo a aprovação de um analista, posteriormente coordenador, gerente e diretor, conforme critérios de faixa de valor a ser considerado para cada alçada.

- O Sistema permite o envio de e-mails para comunicação de aprovação pendente, possibilitando que seja efetuado o deferimento ou indeferimento através de um link

  - Deferir: quando defere a pendência ela pode ser concluída, ou caso precise de aprovação, segue à alçada.
  - Indeferir: quando indefere a pendência ela retorna para o usuário origem refazer;

O primeiro passo é verificar as configurações:

1. No menu: Cadastros gerais > Configurações da empresa > Parâmetros - Empresa, cadastrar os seguintes parâmetros:
   usarAlcadaAprovacao = true. Esse parâmetro indica que o sistema  utiliza a rotina de aprovação para todos os tipos de documentos;
   usarAlcadaAprovacaoRespeitandoHierarquia = true. Esse parâmetro indica que o sistema  utiliza a hierarquia nas aprovações. Ele obriga que a aprovação respeite os níveis informados no cadastro das alçadas;

**Obs**.: Sempre que um cliente for usar alçada de aprovação, é preciso entender duas coisas: se ele vai usar alçada para algum processo específico, tipo só pra fatura ou conhecimento ou tabela  de frete, ou se ele vai usar pra tudo.

- Se for usar somente para um ou alguns processos específicos, então o parâmetro usarAlcadaAprovacao não deve ser incluído, e sim, deve ser incluído o parâmetro correspondente ao processo que o cliente vai utilizar (usarAlcadaAprovacaoFatura; usarAlcadaAprovacaoConhecimento etc);
- Nesses casos, tem que ter cadastrada a Alçada de Aprovação somente para esses parâmetros específicos incluídos e que estiverem como "true";-
- Se for usar alçada para tudo, então, deve ser incluído somente o parâmetro geral "usarAlcadaAprovacao", e cadastrar alçada de aprovação para todos os processos que existem alçada;

1. No menu: Sistema > Acesso > Usuário > Usuário da empresa, cadastrar os usuários que serão os aprovadores da empresa (usuário folha e usuário raiz). Aqui é necessário informar o e-mail para cada um dos usuários;
2. No menu: Cadastros gerais > Configurações da empresa > Workflow > Justificativa de ação, cadastrar uma justificativa para Deferimento e uma justificativa para Indeferimento;
3. O fluxo de alçada de aprovação é cadastrado no menu: Cadastros gerais > Configurações da empresa > Workflow > Alçadas de aprovação;

![Imagem 1: O fluxo de alçada de aprovação é cadastrado no menu: Cadastros gerais > Configurações da empresa > Workflow > Alçadas…](https://ajuda.sankhya.com.br/hc/article_attachments/44011209444759)

5.  A alçada por hierarquia possui o comportamento de níveis obrigatórios de aprovação, ou seja, ela exige que cada nível aprove respeitando sempre os níveis anteriores. Para isso é necessário informar os níveis de aprovação no cadastro: Perfil, definido como usuário folha e Próximo perfil a aprovar, definido como usuário raiz;

As restrições determinam quais rotinas o perfil poderá realizar a aprovação, sendo ainda possível restringir por um determinado marcador e determinar se é necessário a aprovação de outro perfil após esse;

Por exemplo: o perfil X pode aceitar faturas com valor de 0 a 9.999.999.999.999,00, porém o perfil Y está definido como o próximo a aprovar. Quando o perfil X aprovar a fatura a mesma será enviada para aprovação do perfil Y e apenas após a aprovação do mesmo é que ela será considerada como aceita;

O perfil Y poderá ou não realizar a aprovação sem a aprovação do perfil X conforme o cadastro do parâmetro [usarAlcadaAprovacaoRespeitandoHierarquia];

![Imagem 2: O perfil Y poderá ou não realizar a aprovação sem a aprovação do perfil X conforme o cadastro do parâmetro…](https://ajuda.sankhya.com.br/hc/article_attachments/44011197421719)

O Tipo de alçada determina que esse perfil poderá aprovar rotinas porém com restrições que podem ser Valor, Quantidade e Frete/Faturamento;

Por exemplo, é possível configurar que o perfil X poderá realizar a aprovação de faturas que possuam valor de 0 a 2.000, o perfil Y poderá aprovar de 2.000 a 999.999,00 e o perfil Z poderá aprovar de 0 a 9.999.999.999.999,00. Ao acessar uma fatura de valor 2.500,00 apenas o perfil Y e Z poderão realizar a aprovação;

![Imagem 3: Por exemplo, é possível configurar que o perfil X poderá realizar a aprovação de faturas que possuam valor de 0 a…](https://ajuda.sankhya.com.br/hc/article_attachments/44011209689879)

Os Filtros podem ser configurados para restringir a aprovação do perfil pela Unidade, Centro de custo ou Departamento.

![Imagem 4: Os Filtros podem ser configurados para restringir a aprovação do perfil pela Unidade, Centro de custo ou Departamento.](https://ajuda.sankhya.com.br/hc/article_attachments/44011188523415)

As Justificativas  determinam se será obrigatório ou não a inclusão de uma justificativa no momento de aprovação ou não, e as opções Envia email indeferimento e Envia email deferimento habilitam o envio de e-mail no momento em que a aprovação for deferida ou indeferida.

O e-mail que receberá o deferimento/indeferimento é informado no cadastro do usuário, que deve possuir o determinado perfil configurado na alçada;

![Imagem 5: O e-mail que receberá o deferimento/indeferimento é informado no cadastro do usuário, que deve possuir o determinado…](https://ajuda.sankhya.com.br/hc/article_attachments/44011206182551)

## Vamos a um exemplo na prática:

Cadastrar as regras abaixo para aprovação de alçada de 'Fatura':

João vai aprovar faturas até R$ 2.500,00;

João, Maria, Suellen vão aprovar faturas de R$ 2.501,00 à R$8.0000;

João, Maria, Suellen vão aprovar faturas de apartir de R$8.001;

1. Primeiramente verificar o perfil de cada aprovador em: Sistema > Acesso > Usuários > Usuário da Empresa; Neste exemplo temos: João Perfil Cotação 1, Maria Perfil Cotação 2 e Suellen Perfil Cotação 3;
2. Acessar o menu:  Cadastros gerais > Configurações da empresa > Workflow > Alçadas de aprovação;
3. Clicar no botão 'Novo';
4. Configurar as regras conforme abaixo:

cadastro de 0 a 2500,99 com o perfil cotação 1;

cadastro de 2501,00 a 8.000,99com o perfil cotação 1 e no campo próximo perfil a provar, o cotação 2;

cadastro de 2501,00 a 8.000,99com o perfil cotação 2 e no campo próximo perfil a aprovar, o cotação 3;

cadastro de 2501,00 a 8.000,99com o perfil cotação 3;

cadastro de 8000,01 a 999.999.999 com o perfil cotação 1 e no campo próximo perfil a aprovar, o cotação 2;

cadastro de 8000,01 a 999.999.999 com o perfil cotação 2 e no campo próximo perfil a aprovar, o cotação 3;

cadastro de 8000,01 a 999.999.999 com o perfil cotação 3;

5. Para saber se a alçada realmente ficou certa, basta verificar no final da página se o sistema conseguiu montar a árvore;

![Imagem 6: 5. Para saber se a alçada realmente ficou certa, basta verificar no final da página se o sistema conseguiu montar a…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1965017741/db617b1c963fa18337fd79f0cf50/8C099D32FC1C5F7E1E5C67443E95C0AC?expires=1791331200&signature=4be0221efd3859bf390d76fce3445aaa5d2475cb682ea2fb8955cfbd2e840b90&req=dSkhE8l%2FmoZbWPMW3nq%2BgWVi1UfU%2Bu2gqBdnIisEkM9joZNhibu4NOym0s4G%0ALY%2FsPMROIMowSUr16y9G9iHmcD8%3D%0A)

**Obs.:**Caso apresente a mensagem '"**Você não possui permissão para escolher esta transportadora**", verificar se o usuário em questão faz parte dos perfis que estão configurados na alçada de aprovação.

Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
