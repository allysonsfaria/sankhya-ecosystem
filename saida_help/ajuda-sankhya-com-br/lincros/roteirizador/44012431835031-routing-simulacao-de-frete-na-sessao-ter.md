---
id: "44012431835031"
titulo: "[Routing] - Simulação de frete na sessão (Terceiro/Fracionado) - Integração entre Routing x TMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012431835031--Routing-Simula%C3%A7%C3%A3o-de-frete-na-sess%C3%A3o-Terceiro-Fracionado-Integra%C3%A7%C3%A3o-entre-Routing-x-TMS"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T19:29:31Z"
rotulos: ["sync_hc", "lincros", "lincros_13433565", "sync_hash_99369fd09499"]
---

# [Routing] - Simulação de frete na sessão (Terceiro/Fracionado) - Integração entre Routing x TMS

**Menu**: Roteirizador> Roteirizar> Iniciar uma nova sessão

**Objetivo**: Utilizar a opção disponível no Routing de simulação de fretes, através da ferramenta: **Terceirizado/Fracionado** na sessão iniciada

**Considerações**: Para a correta funcionalidade dessa função, existem alguns pré-requisitos entre o Routing e TMS, sendo eles:

- Existir uma tabela de frete criada no TMS, a mesma precisa estar com a vigência ativa; atender a faixa de região da entrega; estar deferida; possuir componentes de frete que atendam a entrega em questão;
- A transportadora precisa estar cadastrada no Routing e TMS;
- No routing o cliente precisa estar com a opção "Cliente TMS" marcado;
- O pedido precisa ter originalmente vindo do TMS;
- Ao exportar a sessão é criado uma Ordem de coleta no TMS, não um embarque;
- Por padrão o TMS retorna a menor tabela, porém, há um parâmetro no Roteirizador que retorna todas as tabelas, ao invés da menos, o parâmetro é 'Buscar todas as tabelas de frete do TMS nas rotas fracionadas/terceirizadas' para habilitar o parâmetro acione o suporte Lincros.

Passo-a-passo:

1. Acessar o Roteirizador> Roteirizar> Iniciar uma nova sessão;
2. Filtrar os pedidos do TMS;
3. Criar a sessão;
4. Através da função laço

   ![Imagem 1: Através da função laço](https://ajuda.sankhya.com.br/hc/article_attachments/44012432007191)

    selecione as entregas que deseja realizar a simulação do frete;
5. Será aberto uma janela com a informação "Mover atividade(s);
6. Selecionar a opção: Terceirizado/Fracionado;

   ![Imagem 2: Selecionar a opção: Terceirizado/Fracionado;](https://ajuda.sankhya.com.br/hc/article_attachments/44012457501975)

       7. O Routing trará as opções de transportadoras aptas para realizar o transporte, com a informação de custo previsto;

       8. Deve ser selecionado a opção que for viável, e confirmar:

![Imagem 3: 8. Deve ser selecionado a opção que for viável, e confirmar:](https://ajuda.sankhya.com.br/hc/article_attachments/44012432363543)

## Informações adicionais:

Em tela no Routing, caso seja selecionado a opção "Terceirizado/Fracionado", as informações apresentadas diferirão do que normalmente o Routing apresenta, conforme imagens:

- **Informações da Rota selecionada** - Informação que fica normalmente localizada na parte lateral direita da tela de roteirização:

![Imagem 4: Informações da Rota selecionada - Informação que fica normalmente localizada na parte lateral direita da tela de…](https://ajuda.sankhya.com.br/hc/article_attachments/44012457819543)

- A informação **Rota** que aparece na lateral esquerda, na parte inferior também virá levemente diferente, será apresentado um ícone de presente

  ![Imagem 5: A informação Rota que aparece na lateral esquerda, na parte inferior também virá levemente diferente, será apresentado…](https://ajuda.sankhya.com.br/hc/article_attachments/44012440709399)

   em tela:

![Imagem 6: em tela:](https://ajuda.sankhya.com.br/hc/article_attachments/44012458238615)

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
