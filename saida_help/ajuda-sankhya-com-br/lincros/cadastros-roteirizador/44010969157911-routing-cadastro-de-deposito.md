---
id: "44010969157911"
titulo: "[Routing] - Cadastro de Depósito"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010969157911--Routing-Cadastro-de-Dep%C3%B3sito"
trilha: "Lincros > Roteirizador > Cadastros - Roteirizador"
atualizado_em: "2026-10-05T18:51:29Z"
rotulos: ["sync_hc", "lincros", "lincros_14443341", "sync_hash_2a27b6435ed0"]
---

# [Routing] - Cadastro de Depósito

**Menu:** Cadastros > Depósito

**Objetivo:** Como realizar o cadastro do depósito no Routing, que é o ponto de origem das operações de roteirização.

## Considerações:

- O depósito é o cadastro central do Routing — todos os demais cadastros (veículos, motoristas, setores, clientes etc.) são vinculados a ele;
- Ao criar um depósito, o sistema gera automaticamente um **Parâmetro padrão** (janela 00:00–23:59) e uma **Estratégia de Roteirização padrão**, ambos vinculados ao depósito;
- Cada depósito deve possuir exatamente um conjunto de parâmetros vinculados.

## Abaixo seguem os procedimentos:

1. Acesse o menu **Cadastros > Depósito** e clique em **'Novo'**;
2. Preencha os campos obrigatórios:

- **Nome:** nome de identificação do depósito;
- **Endereço / Cidade / Estado / CEP:** endereço completo do depósito;
- **Latitude e Longitude:** coordenadas geográficas do depósito. Se preferir, arraste o marcador no mapa que as coordenadas são preenchidas automaticamente;

3. Preencha os campos opcionais conforme necessidade:

- **Horário de trabalho (início/término):** define a janela de atendimento padrão do depósito, que afeta a geração de rotas. Pedidos fora desse horário ficam como não roteirizados;
- **Depósito TMS:** habilite este parâmetro se o depósito recebe pedidos importados do TMS. Necessário para a integração funcionar corretamente;
- **Programação de múltiplas transferências:** habilite para rotas de transferência entre múltiplos pontos de apoio;
- **Distância entre praças de pedágio:** distância em metros para distinguir praças próximas (padrão recomendado: 500m);

4. Clique em **'Confirmar'** para salvar o depósito.

Após salvar, o sistema cria automaticamente os parâmetros padrão e uma estratégia de roteirização inicial vinculados ao depósito. Esses podem ser ajustados posteriormente em **Cadastros > Estratégias de Roteirização**.

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
