---
id: "44010804994711"
titulo: "[TMS] - Cadastrar tabela TMS na plataforma VTEX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010804994711--TMS-Cadastrar-tabela-TMS-na-plataforma-VTEX"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:47:24Z"
rotulos: ["sync_hc", "lincros", "lincros_13432582", "sync_hash_8034c21d2169"]
---

# [TMS] - Cadastrar tabela TMS na plataforma VTEX

Este é um artigo complementar. Para saber mais sobre a integração Lincros com VTEX acesse [este artigo](https://sankhya.zendesk.com/hc/pt-br/articles/44010754196759).

## Objetivo:

Este artigo tem como objetivo instruir como importar uma tabela de fretes no modelo VTEX dentro da plataforma VTEX

## Pré-requisitos:

Possuir habilitada a funcionalidade da Integração VTEX.

Possuir a integração com a VTEX configurada.

Possuir arquivo de tabela de frete modelo VTEX (saiba como exportar do TMS [clicando aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44010661832215))

---

## Instruções:

Como pré-requisito, é necessário que a política de envio esteja previamente cadastrada na VTex no menu Estoque e entrega > Estratégia de envio, clicar em Criar política de envio.

![Imagem 1: Como pré-requisito, é necessário que a política de envio esteja previamente cadastrada na VTex no menu Estoque e…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963025640/cf643ab122d17454370a54a92d7d/5F10974930551FAEA425E98491138938?expires=1791331200&signature=2880633b4477f49de91f65a6d3c0641a4444a9f435d2f7a466886e455fa26d7d&req=dSkhFcl8mIdbWfMW3nq%2BgUbKgyOg4iORs549Gc8daT3WMBMLB%2BbVZf25EBvN%0AkP479zS9QLPxj8rqKjNP34iYw3I%3D%0A)

Na tela de edição de política de envio informar o nome da tabela de fretes, o ID (que deverá ser preenchido na tabela no TMS também), e o método de envio (cadastrado na VTex).

- Tendo a tabela no modelo VTex exportada pelo TMS, efetuar o download dela no e-mail e importar na política de envio.
- Clicar em Salvar alterações.
- Este processo leva alguns minutos para processar, logo em seguida a política deverá ficar na situação Ativa.

Para que esta tabela fique disponível para ser utilizada, deve-se retornar à tela de Estratégias de envio e clicar em Docas > escolher a doca desejada > editar

![Imagem 2: Para que esta tabela fique disponível para ser utilizada, deve-se retornar à tela de Estratégias de envio e clicar em…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963025653/e68ba05226b8caf4f74bb8b6627d/22DDA11AD076AAAC16E71C9BE1AB9C25?expires=1791331200&signature=d717db3a5d1dbe471e3395c5bc52a420406843b5b14e7c4a32c4aaad45100bf5&req=dSkhFcl8mIdaWvMW3nq%2BgZDqiIb3t1H9enyMFDzPN974hweGQX7Ptbg3CyrA%0AcUb12x34e3LtMEW7rtTwdk4%2B%2FLY%3D%0A)

Inserir a política de envio cadastrada e salvar.

![Imagem 3: Inserir a política de envio cadastrada e salvar.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963025660/d068329636e886c15d37f83dc81f/411675BEE407A7848C86C902B6CA439B?expires=1791331200&signature=6c29e6bd4ed53d05a7d4b144596a86b3db96b0fd3be4940ed8c32dab7badf92f&req=dSkhFcl8mIdZWfMW3nq%2BgV%2BbyPGicUMcQFowX3sCHFfFcFN7gzWpNmD1OEG5%0AW3519%2BDH9MHxMocfIJIxGFgPe6s%3D%0A)

Feitos estes passos, já podem ser realizadas simulações de frete, no menu Estoque e entrega > Simulador de envio

![Imagem 4: Feitos estes passos, já podem ser realizadas simulações de frete, no menu Estoque e entrega > Simulador de envio](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963025669/b087e27f0d768590cdfb122cf723/9FA711DAF35A477B2B2D79087DA96900?expires=1791331200&signature=69f7c86c0dfff9cfe7585a81e19ba60fba30a8f406dae2caddd85f7385413d3f&req=dSkhFcl8mIdZUPMW3nq%2BgcIue5jzLx1qym%2FJKm%2FSJoIkGZXZFh3NtQ%2FRa7YY%0AObcPSHHreUdPM1r%2B9im5Gla4oTM%3D%0A)
