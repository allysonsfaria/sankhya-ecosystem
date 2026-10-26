---
id: "28389928043287"
titulo: "Impressões não funcionam em navegadores externos: Como Resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28389928043287-Impress%C3%B5es-n%C3%A3o-funcionam-em-navegadores-externos-Como-Resolver"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-09-22T16:21:35Z"
rotulos: ["Configuração", "Impressão", "Segurança", "Portal de Vendas", "Web Connection", "Passos para resolver", "Razão do erro", "Detalhe do erro", "impressão navegador Google Chrome", "impressão no SankhyaW", "Webconnetcion externo", "botão de impressão", "botão de impressão dos portais não funciona", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Impressões não funcionam em navegadores externos: Como Resolver?

**(1)** Se por exemplo é acessado o portal de vendas e selecionado uma nota/pedido. Ao dar um clique na opção da impressora, nada acontece, nem mesmo o pop-up de seleção de impressoras é aberto.

Essa situação pode acontecer no **webconnection integrado e no webconnection externo. Veja abaixo soluções para ambos os casos:**

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/28389928029719)SOLUÇÃO:**

#### Webconnection integrado

**(1)**Devido à política de segurança **CORS** dos novos navegadores, links **HTTP** não podem realizar requisições para endereços privados, impedindo a abertura do pop-up de impressão. Diante disso, sugerimos algumas alternativas para solucionar essa questão:

![Imagem 2: Configurar um servidor proxy reverso com HTTPS , garantindo que as requisições sejam aceitas conforme as diretrizes de…](https://ajuda.sankhya.com.br/hc/article_attachments/28485972278039) Configurar um servidor proxy reverso com **HTTPS**, garantindo que as requisições sejam aceitas conforme as diretrizes de segurança dos navegadores.

**(2)** Caso seja necessário algum apoio, procurar sua **unidade responsável**.

![Imagem 3: Utilizar o navegador Sankhya para realizar as impressões, pois ele ainda permite requisições HTTP , com ou sem o Web…](https://ajuda.sankhya.com.br/hc/article_attachments/32291488383639) Utilizar o navegador Sankhya para realizar as impressões, pois ele ainda permite requisições **HTTP**, com ou sem o Web Connection embarcado.

#### Webconnection externo

Ao usar **SankhyaOm no Google Chrome**, use a **base em HTTPS**. Não é recomendável usar o ambiente de produção no protocolo HTTP, devido às implicações de segurança que essa prática pode acarretar.

Assim, se o  link de acesso estiver como  **http:**//sdeteste.sankhyacla.com.br/mge, para que funcione corretamente, acione o **TI da sua empresa** e peça para **configurar para: HTTPS** https://sdeteste.sankhyacla.com.br/mge
