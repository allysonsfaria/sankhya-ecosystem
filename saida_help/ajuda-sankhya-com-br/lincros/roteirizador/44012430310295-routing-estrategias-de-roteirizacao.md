---
id: "44012430310295"
titulo: "[Routing] - Estratégias de Roteirização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012430310295--Routing-Estrat%C3%A9gias-de-Roteiriza%C3%A7%C3%A3o"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T19:29:08Z"
rotulos: ["sync_hc", "lincros", "sync_hash_21cdac9762a5", "lincros_13433572"]
---

# [Routing] - Estratégias de Roteirização

**Menu**: Roteirizador> Cadastros> Estratégias de Roteirização

**Objetivo**: Como realizar a configuração das estratégias de roteirizações, com filtros finos, de acordo com a necessidade de cada início de sessão de roteirização. Essa função tem por finalidade, parametrizar o sistema, para que a roteirização seja elaborada de acordo com a necessidade de cada região e/ou usuário. Exemplo: para uma região mais distante, precisa ser aplicado uma configuração de usar menos veículos, através desse cadastro é possível ajustar a estratégia para esse uso.

## Considerações:

- Possuir acesso ao Routing;
- O cadastro da estratégia de roteirização é feito através do menu: Roteirizador > Cadastros > Estratégias de Roteirização, mas a utilização da ferramenta será feita ao criar uma sessão;
- Essa função é opcional, não sendo cadastrado ou selecionado uma estratégia de Roteirização, o Routing respeitará as parametrizações do depósito;
- Após cadastrar uma estratégia de roteirização, pode ser clonado o mesmo, abrindo o cadastro, efetuando as alterações, e finalizando com a opção 'Salvar como';

Abaixo segue os procedimentos de como realizar o cadastro de uma 'Estratégia de Roteirização':

1. Acessar o menu: Roteirizador > Cadastros > Estratégias de Roteirização > Novo;
2. Selecionar o depósito (campo obrigatório);
3. Colocar um nome para a Estratégia de Roteirização (campo obrigatório);
4. Marcar a flag "Estratégia padrão do depósito", caso queira (opcional);
5. Configurar os parâmetros gerais, são eles:

- Priorizar menos veículos - (Preferir menor quantidade de veículos em rota ao invés de distância);
- Permitir roteirização nos finais de semana;
- Permitir dividir o tempo de atendimento entre vários dias, em rotas de mais de um dia;
- Tempo mínimo de recarga - (Tempo mínimo restante dos veículos no dia para gerar rotas de recarga);
- Quantidade máxima de atividades permitidas na rota - Essa opção vem como ilimitada, se desejar, pode ser informado um número para limitar;
- Agrupar todos os pedidos do mesmo cliente em uma única atividade;
- Percentual de ajuste de velocidade na movimentação do veículo - (Para aumentar a velocidade, informe um valor negativo);
- Tolerância das janelas de atendimento em segundos (Antes) - (Inicialmente a opção vem como ilimitado, havendo a necessidade pode ser preenchido);
- Tolerância do agendamento de pedidos em segundos (Antes) - (Inicialmente a opção vem como ilimitado, havendo a necessidade pode ser preenchido);
- Tolerância do agendamento de pedidos em segundos (Depois) - (Inicialmente a opção vem como ilimitado, havendo a necessidade pode ser preenchido);
- Valor alvo - É o valor total de pedidos na roteirização, se preenchido, aparecerá da seguinte forma na sessão: Caso o valor da rota seja inferir ao valor alvo, ficará em amarelo. Caso o valor da rota seja superior ao valor alvo, ficará em vermelho;
- Considerar prioridades dos pedidos ao sequenciar as atividades.

     6. Configurar os Parâmetros Atividades a pé, são eles:

- Raio de atendimento a pé (Metros);
- Tempo máximo (Em segundos) para a entrega a pé;
- % Tolerância para entrega no raio a pé;
- Peso máximo para atendimento a pé (Kg);
- Cubagem máxima para atendimento a pé.

**Obs.:** Todos os parâmetros atividades a pé, vem com configuração de ilimitado, e pode ser informado os valores necessários.

     7. Clicar em 'Confirmar';

Para utilizar a estratégia de roteirização, basta seguir os passos ao criar uma sessão, através do caminho:

1. Acessar: Roteirizador > Roteirizador > Iniciar uma nova sessão;
2. Selecionar o depósito;
3. Selecionar a 'Estratégia de Roteirização', e seguir com o processo de roteirização:

![Imagem 1: Selecionar a 'Estratégia de Roteirização', e seguir com o processo de roteirização:](https://ajuda.sankhya.com.br/hc/article_attachments/44012455852183)

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
