---
id: "44011470994199"
titulo: "[Tracking] - Gestão de ativos integrada com o Lincros Management"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011470994199--Tracking-Gest%C3%A3o-de-ativos-integrada-com-o-Lincros-Management"
trilha: "Lincros > Tracking > Cadastros - Tracking"
atualizado_em: "2026-10-05T19:04:05Z"
rotulos: ["sync_hc", "lincros", "lincros_13438319", "sync_hash_34e987d5e21e"]
---

# [Tracking] - Gestão de ativos integrada com o Lincros Management

**Menu**: Cadastros > Ativos

**Objetivo**: Este artigo tem como objetivo esclarecer a funcionalidade de Gestão de ativos presente no Tracking e integrada com o Lincros Management.

## Considerações:

- Atualmente alguns de nossos clientes embarcadores buscam realizar o controle da entrega e coleta de ativos imobilizados para seus clientes;
- O ativo é um item que é entregue praticamente em todas as entregas. Entendem-se por ativos imobilizados pallets, cestos plásticos ou caixas de cerveja, por exemplo;
- O Tracking ainda não atende de forma plena o lançamento de ativos. A funcionalidade proposta visa integrar o modelo de negócio com intuito de validar a abordagem;
- Espera-se que nas próximas versões esse processo de lançamento seja otimizado em um novo recurso mais simples e prático, atualmente o controle é realizado em conjunto com a solução Lincros Management;

Abaixo segue os pré-requisitos:

## - Como configurar a Unidade de Negócio

A unidade de negócio do Tracking deve possuir um CNPJ e deve corresponder com o CNPJ da Filial cadastrada no Lincros Management. No Tracking, deve-se ir em: Cadastros > Unidades de negócio.

![Imagem 1: A unidade de negócio do Tracking deve possuir um CNPJ e deve corresponder com o CNPJ da Filial cadastrada no Lincros…](https://ajuda.sankhya.com.br/hc/article_attachments/44011486336279)

No Lincros Management deve-se seguir o caminho: Cadastros gerais > Unidades da empresa > Unidades.

## - Como configurar Clientes

O cliente deve possuir um CNPJ (Documento) cadastrado no Tracking e deve corresponder com o CNPJ da Pessoa cadastrada no Lincros Management.

O CNPJ do cliente deve ser informado no XML da rota que será importado, no campo Documento.

![Imagem 2: O CNPJ do cliente deve ser informado no XML da rota que será importado, no campo Documento.](https://ajuda.sankhya.com.br/hc/article_attachments/44011486545687)

Para verificar clientes com saldos de ativos já existentes no Lincros Management, deve-se acessar o menu: Operacional> Gestão de Ativos e selecionar o ativo desejado.

## - Como Cadastrar Ativos

É necessário cadastrar previamente o ativo no Tracking, onde deve-se informar o 'Código Externo' e a 'Descrição'. Essas informações devem corresponder com as informações de ativos cadastradas no Lincros Management.

No Tracking deve-se ir em Cadastros > Ativos:

![Imagem 3: No Tracking deve-se ir em Cadastros > Ativos:](https://ajuda.sankhya.com.br/hc/article_attachments/44011481923735)

No Lincros Management deve-se acessar: Cadastros Gerais > Gestão de Ativos > Itens.

## - Como Habilitar a propagação de ocorrências

A configuração 'Propagar ocorrência' deve estar habilitada no Tracking, em Configurações > Parâmetros > Monitoramento:

![Imagem 4: A configuração 'Propagar ocorrência' deve estar habilitada no Tracking, em Configurações > Parâmetros > Monitoramento:](https://ajuda.sankhya.com.br/hc/article_attachments/44011482125207)

## - Como configurar integrações de enriquecimento e propagação de pacotes

As seguintes integrações devem ser ativadas:

- Serviço de enriquecimento e propagação de ocorrências
- Serviço de envio de requisições para ambiente de terceiros
- Integração com Lincros Management para envio de ocorrências.
- Serviço de processamento de filas de ocorrências.

Deve-se inserir a chave de autenticação (token) nas integrações do Tracking. Para encontrar a chave de autenticação no Lincros Management basta acesar o menu: Sistema > Acesso > Usuário > Usuários da empresa e buscar por 'ws.tracking'.

![Imagem 5: Deve-se inserir a chave de autenticação (token) nas integrações do Tracking. Para encontrar a chave de autenticação no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011482269719)

![Imagem 6: Deve-se inserir a chave de autenticação (token) nas integrações do Tracking. Para encontrar a chave de autenticação no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011472209175)

Abaixo segue algumas limitações dessa funcionalidade:

- Não será possível lançar a coleta ou entrega de ativos de algum cliente que não estiver na rota do motorista;
- A coleta e a entrega do ativo deverá ser o primeiro processo a ser realizado pelo motorista, isso por que ao registrar a entrega, o card correspondente à entrega desaparecerá do aplicativo;
- Se algum dos pré-requisitos para movimentação de estoque for inválido, o Lincros Management NÃO processará a movimentação, sendo necessário que a movimentação seja realizada pelo embarcador no Lincros Management;

## Passo a passo no Lincros App

1. Inicie a viagem com a placa;
2. Selecione a entrega em que se deseja realizar a movimentação de ativos e selecione '+ Adicionar' em 'Ocorrências no Cliente';

![Imagem 7: Selecione a entrega em que se deseja realizar a movimentação de ativos e selecione '+ Adicionar' em 'Ocorrências no…](https://ajuda.sankhya.com.br/hc/article_attachments/44011503123607)

3

3. Em seguida, selecione o tipo de movimentação que você pretende fazer e toque em 'Confirmar';

![Imagem 8: 3. Em seguida, selecione o tipo de movimentação que você pretende fazer e toque em 'Confirmar';](https://ajuda.sankhya.com.br/hc/article_attachments/44011497697047)

4. Selecione a quantidade de ativos que você pretende movimentar e toque em 'Confirmar';

![Imagem 9: 4. Selecione a quantidade de ativos que você pretende movimentar e toque em 'Confirmar';](https://ajuda.sankhya.com.br/hc/article_attachments/44011472610839)

5. Para consultar se a ocorrência foi integrada corretamente, verifique os logs das integrações 'Serviço de enriquecimento e propagação de ocorrências' e 'Serviço de envio de requisições para ambiente de terceiros';

Também é possível verificar o saldo de ativos no Lincros Management, em Operacional > Gestão de Ativos.

**Obs:** Caso não possua acesso para realizar as configurações necessárias, entre em contato com nossa equipe de suporte.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

O cliente deve possuir um CNPJ (Documento) cadastrado no Tracking e deve corresponder com o CNPJ da Pessoa cadastrada no Lincros Management. O CNPJ do cliente deve ser informado no XML da rota que será importado, no campo Documento.

Para verificar clientes com saldos de ativos já existentes no Lincros Management deve ir sem Operacional> Gestão de Ativos e selecionar o ativo desejado.
