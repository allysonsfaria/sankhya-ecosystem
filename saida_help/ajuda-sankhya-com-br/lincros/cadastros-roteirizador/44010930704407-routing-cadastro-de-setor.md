---
id: "44010930704407"
titulo: "[Routing] - Cadastro de Setor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010930704407--Routing-Cadastro-de-Setor"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T18:50:28Z"
rotulos: ["sync_hc", "lincros", "sync_hash_633d76e08974", "lincros_13432298"]
---

# [Routing] - Cadastro de Setor

**Menu**: Cadastros > Setor

**Objetivo**: Como realizar o cadastro de setores

**Considerações**:

- O cadastro de setor é obrigatório para o Roteirizador;
- Aqui definimos as regiões de atendimento, veículos ou tipos de veículos preferenciais para atendimento de um determinado setor, pontos de apoio e se os setores são atendidos de forma exclusiva;
- É por estes setores que o roteirizador vai se basear para montar as rotas;
- Possibilidade de realizar o desenho do setor automaticamente por Estado, Município ou Bairro ou desenho manual;
- É possível pré-determinar os veículos ou tipos de veículos que irão atender essa região;
- É necessário ter os campos abaixo já cadastrados no Router para iniciar o cadastramento de setores:

- [Depósito](https://intercom.help/ajudalincros/pt-BR/articles/14443341-routing-cadastro-de-deposito);
- [Rodízio de Placas](https://sankhya.zendesk.com/hc/pt-br/articles/44010867331991);
- [Grupo de Rotas](https://sankhya.zendesk.com/hc/pt-br/articles/44010924653463);
- [Ponto de Apoio](https://intercom.help/ajudalincros/pt-BR/articles/13438682-routing-pontos-de-apoio);

Para o cadastro de setor é necessário informar os seguintes campos:

1. **Depósito**: Para o cadastro do setor é necessário vincular ele à um depósito;
2. **Nome**: Nome que será dado ao setor. Este nome será utilizado na criação das rotas;
3. **Setor exclusivo**: Habilitando esta opção, este setor se tornará exclusivo gerando uma ou mais rotas somente para este setor;
4. **Veículos (Placas)**: Informar o número das placas dos veículos;
5. **Somente estes veículos poderão efetuar entregas neste setor (Exclusivos)**;
6. **Estes veículos poderão efetuar entregas somente neste setor (Reservados)**;
7. **Preferencialmente estes veículos efetuarão entregas neste setor (Preferenciais)**;
8. **Veículos bloqueados (Placas)**: Informe as placas dos veículos que não poderão atender aquele determinado setor;
9. **Tipos de veículos**: Informe os tipos de veículos que irão atender este setor;
10. **Ponto de Apoio**: O ponto de apoio indica que o veículo deverá partir dele, e não do depósito;
11. **Grupo**: Informe o grupo de rotas;
12. **Cor**: Informe uma cor da paleta de cores para este setor;
13. **Tempo de espera**: Informe o tempo que o motorista irá aguardar no cliente;
14. **Máximo Dias em rota**: Informe o número máximo de dias em que o veículo poderá estar em rota;
15. **% ajuste de velocidade**: Percentual de ajuste sobre a velocidade das vias. Valor positivo = mais lento; valor negativo = mais rápido;
16. **Valor Fórmula**: Variável da fórmula de custo configurada na transportadora;
17. **Valor Alvo**: Valor meta para apresentação visual do atingimento da rota. [Clique aqui para verificar este cadastramento](https://intercom.help/ajudalincros/pt-BR/articles/13438690-routing-valor-alvo-para-as-rotas);
18. **Rodízio de Placas**: Informe o rodízio de placas para esse setor.

Após cadastrar os setores, é possível definir os horários de trabalho de cada um clicando no ícone de horário na listagem.

O desenho do setor pode ser feito de forma manual (desenho de polígono) ou automática (por Estado, Município ou Bairro).

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
