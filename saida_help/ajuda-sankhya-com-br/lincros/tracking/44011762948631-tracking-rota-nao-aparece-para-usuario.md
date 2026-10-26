---
id: "44011762948631"
titulo: "[Tracking] Rota não aparece para Usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011762948631--Tracking-Rota-n%C3%A3o-aparece-para-Usu%C3%A1rio"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T19:11:44Z"
rotulos: ["sync_hc", "lincros", "lincros_13434727", "sync_hash_e382b3c14f9a"]
---

# [Tracking] Rota não aparece para Usuário

## Objetivo

Identificar o motivo no qual rota não aparece para usuário em tela de Monitoramento.

## Caminho

Ao longo das informações serão passados os passo a passo, devido possuir alguns motivos que afetam não estar sendo visualizado a rota em tela.

## Pré- Requisitos

Possuir acesso Administrador no caso de liberação para usuário .

## Possuem alguns motivos que podem levar um usuário não visualizar uma rota, segue>>

## 1.0  Usuário Não possuir vínculo com Unidade de Negócio e Transportadora

Usuário precisa ter seu login vinculado a Unidade de Negócio e Transportadora da Rota.

Neste caso se torna necessário acessar o cadastro de Usuários e nela realizar o vínculo da Unidade de Negócio e Transportadora, veja como>>

Menu > Cadastros > Usuários

Localize o usuário filtrando pelo seu nome ou login>>

Veja o exemplo abaixo, farei a busca pelo Login do usuário admin, veja>>

![Imagem 1: Veja o exemplo abaixo, farei a busca pelo Login do usuário admin, veja>>](https://ajuda.sankhya.com.br/hc/article_attachments/44011769997463)

![Imagem 2: Veja o exemplo abaixo, farei a busca pelo Login do usuário admin, veja>>](https://ajuda.sankhya.com.br/hc/article_attachments/44011770194583)

OBS>> O mesmo processo deve ser realizado no Campo Transportadoras, assim realizando os vínculos necessários, deve salvar sair do sistema e logar novamente, para que as configurações fiquem salvas.

## 1.1 Cadastro do Veículo não estar ativo

Para que o veículo esteja em tela necessário estar com seu cadastro ativo.

Menu > Cadastros > Veículos

Localize o veículo usando o filtro, veja>>

![Imagem 3: Localize o veículo usando o filtro, veja>>](https://ajuda.sankhya.com.br/hc/article_attachments/44011779671959)

![Imagem 4: Localize o veículo usando o filtro, veja>>](https://ajuda.sankhya.com.br/hc/article_attachments/44011822298007)

## 1.2 Cadastro do veículo não possuir as configurações necessárias

Veículo precisa ter a informação de Transportadora, Unidade de Negócio, Odômetro. E os campos Rastreador e Teclado Logístico, devem estar como "MOBILE"

![Imagem 5: Veículo precisa ter a informação de Transportadora, Unidade de Negócio, Odômetro. E os campos Rastreador e Teclado…](https://ajuda.sankhya.com.br/hc/article_attachments/44011822429463)

## 1.3 Cadastro de Transportadora Errado

Se torna necessário o cadastro de Transportadora estar ativo para que o veículo seja mostrado em tela de Monitoramento.

Menu > Cadastros > Transportadoras

Deve localizar a Transportadora da rota e nela verificar se está Ativa, veja>>

![Imagem 6: Deve localizar a Transportadora da rota e nela verificar se está Ativa, veja>>](https://ajuda.sankhya.com.br/hc/article_attachments/44011771029655)

Obs: Nesta mesma tela se torna possível vincular um usuário.

## Lembrando que somente usuário já vinculado no cadastro da Transportadora conseguirá realizar a configuração.

## 1.4 Cadastro de Unidade de Negócio Errado

Se torna necessário o cadastro de Unidade de Negócio estar Ativos, para que o veículo seja mostrado em tela de Monitoramento.

Menu > Cadastros > Unidade de Negócio

Deve localizar a Unidade desejada para verificar se está ativa>>

![Imagem 7: Deve localizar a Unidade desejada para verificar se está ativa>>](https://ajuda.sankhya.com.br/hc/article_attachments/44011814767895)

Obs: Neste tela também é possível vincular um usuário na Unidade de Negócio.

## Lembrando que para conseguir visualizar a Unidade somente usuário Administrador possui permissão.
