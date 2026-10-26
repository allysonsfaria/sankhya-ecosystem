---
id: "44011480950551"
titulo: "[Routing] - Depósito não é uma unidade TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011480950551--Routing-Dep%C3%B3sito-n%C3%A3o-%C3%A9-uma-unidade-TMS"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T19:03:50Z"
rotulos: ["sync_hc", "lincros", "sync_hash_e884743e36b8", "lincros_13438328"]
---

# [Routing] - Depósito não é uma unidade TMS

**Menu**: Cadastros > Depósitos

**Objetivo**: Entender o motivo da crítica 'Depósito "XXXXX" não é uma unidade TMS' e como corrigi-lá.

**Considerações**:

- Necessário ter pedidos importados do TMS;

Abaixo segue os procedimentos:

Durante a importação de pedidos provenientes do TMS para o Routing, caso haja falta de parametrização é bem provável que o sistema apresente a seguinte crítica: 'Integração TMS Depósito "XXXXX" não é uma unidade TMS', que impedirá dar continuidade no processo de importação de pedidos.

![Imagem 1: Durante a importação de pedidos provenientes do TMS para o Routing, caso haja falta de parametrização é bem provável…](https://ajuda.sankhya.com.br/hc/article_attachments/44011451391127)

Contudo, a correção desta crítica é bem simples, pra isso será necessário realizar a seguinte configuração no Routing:

1. Acessar a opção: Cadastros > Depósitos;
2. Selecionar o depósito que apresentou a crítica e clicar no ícone de lápis para editar o cadastro;
3. Habilitar o parâmetro: 'Depósito TMS';
4. Clicar em 'Confirmar', para salvar a alteração;

![Imagem 2: Clicar em 'Confirmar', para salvar a alteração;](https://ajuda.sankhya.com.br/hc/article_attachments/44011469222807)

5. Feito os passos acima, poderá prosseguir com o processo de importação de pedidos do TMS sem que o sistema apresente a crítica mencionada acima.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
